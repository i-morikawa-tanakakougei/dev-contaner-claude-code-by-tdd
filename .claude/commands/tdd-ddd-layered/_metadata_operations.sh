#!/bin/bash

# メタデータ操作の共通関数群
# 原子性とエラーハンドリングを確保

set -euo pipefail

# メタデータファイルの原子的更新
update_metadata_atomic() {
    local metadata_file="$1"
    local jq_expression="$2"
    local temp_file="${metadata_file}.tmp.$$"
    
    # 元ファイルの存在確認
    if [[ ! -f "$metadata_file" ]]; then
        echo "エラー: メタデータファイルが存在しません: $metadata_file" >&2
        return 1
    fi
    
    # JSON構文チェック
    if ! jq empty "$metadata_file" 2>/dev/null; then
        echo "エラー: メタデータファイルの JSON 構文が無効です" >&2
        return 1
    fi
    
    # 更新実行（一時ファイルに出力）
    if ! jq "$jq_expression" "$metadata_file" > "$temp_file" 2>/dev/null; then
        echo "エラー: メタデータの更新処理に失敗しました" >&2
        echo "JQ式: $jq_expression" >&2
        rm -f "$temp_file"
        return 1
    fi
    
    # 更新後のJSON構文チェック
    if ! jq empty "$temp_file" 2>/dev/null; then
        echo "エラー: 更新後のメタデータが無効なJSONです" >&2
        rm -f "$temp_file"
        return 1
    fi
    
    # 原子的置換
    if ! mv "$temp_file" "$metadata_file"; then
        echo "エラー: メタデータファイルの置換に失敗しました" >&2
        rm -f "$temp_file"
        return 1
    fi
    
    echo "メタデータを正常に更新しました: $metadata_file"
}

# メタデータファイルの作成（存在しない場合のみ）
create_metadata_if_not_exists() {
    local metadata_file="$1"
    local feature_name="$2"
    local issue_numbers=("${@:3}")
    
    if [[ -f "$metadata_file" ]]; then
        echo "メタデータファイルは既に存在します: $metadata_file"
        return 0
    fi
    
    # ディレクトリ作成
    local metadata_dir=$(dirname "$metadata_file")
    if ! mkdir -p "$metadata_dir"; then
        echo "エラー: メタデータディレクトリの作成に失敗しました: $metadata_dir" >&2
        return 1
    fi
    
    # 初期メタデータ構造
    local initial_metadata
    initial_metadata=$(cat <<EOF
{
  "feature_name": "$feature_name",
  "issue_numbers": [$(IFS=,; echo "${issue_numbers[*]}")],
  "created_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "updated_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "phase": "created",
  "phases": {
    "use_case": {
      "created": false,
      "approved": false,
      "approved_at": null
    },
    "domain_model": {
      "created": false,
      "approved": false,
      "design_file": null
    },
    "tests": {
      "created": false,
      "passed": false,
      "test_count": 0,
      "coverage_percentage": null
    },
    "domain_implementation": {
      "completed": false,
      "entity_count": 0,
      "value_object_count": 0
    },
    "usecase_implementation": {
      "completed": false,
      "usecase_count": 0
    },
    "infrastructure_implementation": {
      "completed": false,
      "repository_count": 0
    },
    "presentation_implementation": {
      "completed": false,
      "endpoint_count": 0
    },
    "all_tests": {
      "executed": false,
      "passed": false,
      "total_tests": 0,
      "failed_tests": 0
    },
    "refactor": {
      "completed": false,
      "refactoring_count": 0,
      "last_refactor_at": null
    },
    "scenario_evolution": {
      "evolved": false,
      "evolution_count": 0,
      "new_scenarios": []
    },
    "review": {
      "reviewed": false,
      "reviewer": null,
      "review_comments": [],
      "approved": false
    },
    "feedback_application": {
      "applied": false,
      "feedback_count": 0,
      "feedback_items": []
    },
    "pull_request": {
      "created": false,
      "pr_number": null,
      "merged": false,
      "merged_at": null
    }
  }
}
EOF
)
    
    # JSON構文チェック
    if ! echo "$initial_metadata" | jq empty 2>/dev/null; then
        echo "エラー: 初期メタデータのJSON構文が無効です" >&2
        return 1
    fi
    
    # ファイル作成
    if ! echo "$initial_metadata" > "$metadata_file"; then
        echo "エラー: メタデータファイルの作成に失敗しました: $metadata_file" >&2
        return 1
    fi
    
    echo "メタデータファイルを作成しました: $metadata_file"
}

# メタデータファイルの検索とフィーチャー名抽出
find_metadata_file() {
    local issue_list="$1"
    local feature_name="${2:-}"
    
    if [[ -n "$feature_name" ]]; then
        # フィーチャー名が指定されている場合
        echo "docs/use_cases/issue-${issue_list}-${feature_name}.json"
        return 0
    fi
    
    # 既存ファイルから検索
    local found_files
    found_files=$(find docs/use_cases -name "issue-${issue_list}-*.json" 2>/dev/null || true)
    
    if [[ -z "$found_files" ]]; then
        echo "エラー: フィーチャー名が指定されておらず、既存のメタデータファイルも見つかりません" >&2
        echo "使用方法: コマンド名 $issue_list フィーチャー名" >&2
        return 1
    fi
    
    local file_count
    file_count=$(echo "$found_files" | wc -l)
    
    if [[ "$file_count" -gt 1 ]]; then
        echo "エラー: 複数のメタデータファイルが見つかりました:" >&2
        echo "$found_files" >&2
        echo "フィーチャー名を明示的に指定してください" >&2
        return 1
    fi
    
    echo "$found_files"
}

# フェーズ更新の共通関数
update_phase() {
    local metadata_file="$1"
    local phase_name="$2"
    local new_phase_status="$3"
    local additional_updates="${4:-}"
    
    local jq_expression=".phases.${phase_name} |= $new_phase_status | .updated_at = \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\" | .phase = \"${phase_name}_updated\""
    
    if [[ -n "$additional_updates" ]]; then
        jq_expression="$jq_expression | $additional_updates"
    fi
    
    update_metadata_atomic "$metadata_file" "$jq_expression"
}

# メタデータからフィーチャー名とイシュー番号を取得
extract_metadata_info() {
    local metadata_file="$1"
    
    if [[ ! -f "$metadata_file" ]]; then
        echo "エラー: メタデータファイルが存在しません: $metadata_file" >&2
        return 1
    fi
    
    local feature_name
    local issue_numbers
    
    feature_name=$(jq -r '.feature_name' "$metadata_file" 2>/dev/null) || {
        echo "エラー: メタデータからフィーチャー名を取得できません" >&2
        return 1
    }
    
    issue_numbers=$(jq -r '.issue_numbers | @csv' "$metadata_file" 2>/dev/null | tr -d '"') || {
        echo "エラー: メタデータからイシュー番号を取得できません" >&2
        return 1
    }
    
    echo "FEATURE_NAME=$feature_name"
    echo "ISSUE_NUMBERS=$issue_numbers"
}

# 現在のフェーズ確認
get_current_phase() {
    local metadata_file="$1"
    
    if [[ ! -f "$metadata_file" ]]; then
        echo "not_found"
        return 1
    fi
    
    jq -r '.phase // "unknown"' "$metadata_file" 2>/dev/null || echo "unknown"
}

# バックアップ作成
create_metadata_backup() {
    local metadata_file="$1"
    local backup_file="${metadata_file}.backup.$(date +%Y%m%d_%H%M%S)"
    
    if [[ -f "$metadata_file" ]]; then
        if cp "$metadata_file" "$backup_file"; then
            echo "バックアップを作成しました: $backup_file"
        else
            echo "警告: バックアップの作成に失敗しました" >&2
        fi
    fi
}

# 🚀 バッチ更新機能: 複数フィールドを1回のjq処理で更新
batch_update_metadata() {
    local metadata_file="$1"
    shift
    local updates=("$@")  # "key=value" 形式の配列
    
    if [[ ${#updates[@]} -eq 0 ]]; then
        echo "エラー: 更新するフィールドが指定されていません" >&2
        return 1
    fi
    
    local temp_file="${metadata_file}.tmp.$$"
    local timestamp=$(date -u +%Y-%m-%dT%H:%M:%SZ)
    
    # 元ファイルの存在確認
    if [[ ! -f "$metadata_file" ]]; then
        echo "エラー: メタデータファイルが存在しません: $metadata_file" >&2
        return 1
    fi
    
    # JSON構文チェック
    if ! jq empty "$metadata_file" 2>/dev/null; then
        echo "エラー: メタデータファイルの JSON 構文が無効です" >&2
        return 1
    fi
    
    echo "📊 バッチ更新実行中: ${#updates[@]} フィールドを一括更新..."
    
    # jq式を構築
    local jq_expression=""
    for update in "${updates[@]}"; do
        local key="${update%%=*}"
        local value="${update#*=}"
        
        # 値がブール値または数値の場合はそのまま、文字列の場合はクォートで囲む
        if [[ "$value" =~ ^(true|false|[0-9]+(\.[0-9]+)?)$ ]]; then
            jq_expression+=".$key = $value | "
        else
            jq_expression+=".$key = \"$value\" | "
        fi
    done
    
    # updated_at を自動追加
    jq_expression+=".updated_at = \"$timestamp\""
    
    echo "  🔧 JQ式: $jq_expression"
    
    # バッチ更新実行（一時ファイルに出力）
    if ! jq "$jq_expression" "$metadata_file" > "$temp_file" 2>/dev/null; then
        echo "エラー: バッチメタデータ更新に失敗しました" >&2
        echo "JQ式: $jq_expression" >&2
        rm -f "$temp_file"
        return 1
    fi
    
    # 更新後のJSON構文チェック
    if ! jq empty "$temp_file" 2>/dev/null; then
        echo "エラー: バッチ更新後のメタデータが無効なJSONです" >&2
        rm -f "$temp_file"
        return 1
    fi
    
    # 原子的置換
    if ! mv "$temp_file" "$metadata_file"; then
        echo "エラー: バッチ更新されたメタデータファイルの置換に失敗しました" >&2
        rm -f "$temp_file"
        return 1
    fi
    
    echo "✅ バッチメタデータ更新完了: ${#updates[@]} フィールドを一括更新"
    return 0
}

# キャッシュ機能: メモリ内メタデータキャッシュ
declare -g -A METADATA_CACHE
declare -g -A CACHE_TIMESTAMPS

cache_metadata() {
    local metadata_file="$1"
    local cache_key=$(basename "$metadata_file")
    
    if [[ -f "$metadata_file" ]]; then
        METADATA_CACHE["$cache_key"]=$(cat "$metadata_file")
        CACHE_TIMESTAMPS["$cache_key"]=$(date +%s)
    fi
}

get_cached_metadata() {
    local metadata_file="$1"
    local cache_timeout="${2:-30}"  # デフォルト30秒キャッシュ
    local cache_key=$(basename "$metadata_file")
    local current_time=$(date +%s)
    local cache_time=${CACHE_TIMESTAMPS["$cache_key"]:-0}
    
    # キャッシュが有効時間内なら使用
    if [[ $((current_time - cache_time)) -lt $cache_timeout ]]; then
        echo "${METADATA_CACHE["$cache_key"]}"
        return 0
    else
        # キャッシュが古い、または存在しない場合は再読み込み
        cache_metadata "$metadata_file"
        echo "${METADATA_CACHE["$cache_key"]}"
    fi
}

# キャッシュからの値取得（jqを使わない高速版）
get_cached_field() {
    local metadata_file="$1"
    local field_path="$2"
    
    local cached_content
    if cached_content=$(get_cached_metadata "$metadata_file"); then
        echo "$cached_content" | jq -r "$field_path // \"null\""
    else
        echo "null"
    fi
}