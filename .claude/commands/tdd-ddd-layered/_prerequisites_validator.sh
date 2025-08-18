#!/bin/bash

# 前提条件検証フレームワーク
# コマンド実行前の依存関係とフェーズ整合性をチェック

set -euo pipefail

# 依存関係マッピング（コマンド名 -> 必要な前フェーズ）
declare -A PHASE_DEPENDENCIES=(
    ["create-vision"]=""
    ["init-project-structure"]="vision_created"
    ["sprint-planning"]="project_structure_initialized"
    ["create-use-case"]="sprint_planned"
    ["domain-modeling"]="use_case_created"
    ["create-tests"]="domain_model_created"
    ["implement-domain"]="tests_created"
    ["implement-usecase"]="domain_implementation_completed"
    ["implement-infra"]="usecase_implementation_completed"
    ["implement-presentation"]="infrastructure_implementation_completed"
    ["run-all-tests"]="presentation_implementation_completed"
    ["refactor"]="all_tests_passed"
    ["evolve-scenarios"]=""  # 任意のタイミングで実行可能
    ["review-issue"]="refactor_completed"
    ["apply-feedback"]="review_completed"
    ["create-pr"]="feedback_applied"
    ["use-case-status"]=""  # 任意のタイミングで実行可能
)

# 必要なツールの確認
check_required_tools() {
    local required_tools=("jq" "git" "gh")
    local missing_tools=()
    
    for tool in "${required_tools[@]}"; do
        if ! command -v "$tool" &> /dev/null; then
            missing_tools+=("$tool")
        fi
    done
    
    if [[ ${#missing_tools[@]} -gt 0 ]]; then
        echo "エラー: 以下の必要なツールがインストールされていません:" >&2
        printf " - %s\n" "${missing_tools[@]}" >&2
        return 1
    fi
}

# Gitリポジトリ状態の確認
check_git_repository() {
    if ! git rev-parse --git-dir &>/dev/null; then
        echo "エラー: Gitリポジトリではありません" >&2
        return 1
    fi
    
    # リモートリポジトリの存在確認（GitHub関連コマンドの場合）
    if ! git remote -v | grep -q origin; then
        echo "警告: リモートリポジトリ'origin'が設定されていません" >&2
    fi
}

# ワークディレクトリの確認
check_working_directory() {
    local required_dirs=("docs" ".claude/commands/tdd-ddd-layered")
    local missing_dirs=()
    
    for dir in "${required_dirs[@]}"; do
        if [[ ! -d "$dir" ]]; then
            missing_dirs+=("$dir")
        fi
    done
    
    if [[ ${#missing_dirs[@]} -gt 0 ]]; then
        echo "エラー: 以下の必要なディレクトリが存在しません:" >&2
        printf " - %s\n" "${missing_dirs[@]}" >&2
        echo "プロジェクト構造を初期化してください: /init-project-structure" >&2
        return 1
    fi
}

# メタデータファイルの整合性確認
validate_metadata_integrity() {
    local metadata_file="$1"
    
    if [[ ! -f "$metadata_file" ]]; then
        return 0  # ファイルが存在しない場合はスキップ
    fi
    
    # JSON構文チェック
    if ! jq empty "$metadata_file" 2>/dev/null; then
        echo "エラー: メタデータファイルの JSON 構文が無効です: $metadata_file" >&2
        return 1
    fi
    
    # 必須フィールドの存在確認
    local required_fields=("feature_name" "issue_numbers" "phase" "phases")
    for field in "${required_fields[@]}"; do
        if ! jq -e ".$field" "$metadata_file" &>/dev/null; then
            echo "エラー: メタデータに必須フィールド '$field' が存在しません: $metadata_file" >&2
            return 1
        fi
    done
    
    # イシュー番号の形式チェック
    local issue_numbers
    issue_numbers=$(jq -r '.issue_numbers[]' "$metadata_file" 2>/dev/null)
    
    while read -r issue_num; do
        if [[ -n "$issue_num" ]] && ! [[ "$issue_num" =~ ^[0-9]+$ ]]; then
            echo "エラー: 無効なイシュー番号形式: $issue_num" >&2
            return 1
        fi
    done <<< "$issue_numbers"
}

# フェーズの前提条件確認
validate_phase_prerequisites() {
    local command_name="$1"
    local metadata_file="$2"
    
    local required_phase="${PHASE_DEPENDENCIES[$command_name]:-}"
    
    # 前提条件なしの場合はスキップ
    if [[ -z "$required_phase" ]]; then
        return 0
    fi
    
    # メタデータファイルが存在しない場合
    if [[ ! -f "$metadata_file" ]]; then
        echo "エラー: メタデータファイルが存在しません: $metadata_file" >&2
        echo "まず /create-use-case を実行してください" >&2
        return 1
    fi
    
    local current_phase
    current_phase=$(jq -r '.phase // "unknown"' "$metadata_file" 2>/dev/null)
    
    # フェーズ検証ロジック
    case "$required_phase" in
        "vision_created")
            if [[ ! -f "docs/vision/project-vision.md" ]]; then
                echo "エラー: プロジェクトビジョンが作成されていません" >&2
                echo "まず /create-vision を実行してください" >&2
                return 1
            fi
            ;;
        "project_structure_initialized")
            if [[ ! -f "docs/use_cases/core/index.md" ]]; then
                echo "エラー: プロジェクト構造が初期化されていません" >&2
                echo "まず /init-project-structure を実行してください" >&2
                return 1
            fi
            ;;
        "use_case_created")
            if [[ "$current_phase" != "use_case_created" ]] && 
               [[ "$current_phase" != *"use_case"* ]]; then
                echo "エラー: ユースケースが作成されていません" >&2
                echo "現在のフェーズ: $current_phase" >&2
                echo "まず /create-use-case を実行してください" >&2
                return 1
            fi
            ;;
        "domain_model_created")
            local domain_created
            domain_created=$(jq -r '.phases.domain_model.created // false' "$metadata_file" 2>/dev/null)
            if [[ "$domain_created" != "true" ]]; then
                echo "エラー: ドメインモデルが作成されていません" >&2
                echo "まず /domain-modeling を実行してください" >&2
                return 1
            fi
            ;;
        "tests_created")
            local tests_created
            tests_created=$(jq -r '.phases.tests.created // false' "$metadata_file" 2>/dev/null)
            if [[ "$tests_created" != "true" ]]; then
                echo "エラー: テストが作成されていません" >&2
                echo "まず /create-tests を実行してください" >&2
                return 1
            fi
            ;;
        # 他のフェーズも同様に追加...
    esac
}

# GitHub連携の前提条件確認
validate_github_prerequisites() {
    local command_name="$1"
    local issue_numbers=("${@:2}")
    
    # GitHub認証確認
    if ! gh auth status &>/dev/null; then
        echo "エラー: GitHub CLI が認証されていません" >&2
        echo "gh auth login を実行してください" >&2
        return 1
    fi
    
    # イシュー存在確認（GitHub連携コマンドの場合）
    case "$command_name" in
        "create-use-case"|"review-issue"|"apply-feedback"|"create-pr")
            for issue_num in "${issue_numbers[@]}"; do
                if [[ -n "$issue_num" ]]; then
                    if ! gh issue view "$issue_num" &>/dev/null; then
                        echo "エラー: イシュー #$issue_num が存在しません" >&2
                        return 1
                    fi
                fi
            done
            ;;
    esac
}

# Python/uv環境の確認
validate_python_environment() {
    if ! command -v uv &> /dev/null; then
        echo "エラー: uv がインストールされていません" >&2
        echo "CLAUDE.md の指示に従って uv をインストールしてください" >&2
        return 1
    fi
    
    # pyproject.toml の存在確認
    if [[ ! -f "pyproject.toml" ]]; then
        echo "警告: pyproject.toml が存在しません。Python プロジェクトでない可能性があります" >&2
    fi
}

# ブランチ状態の確認
validate_git_branch_state() {
    local command_name="$1"
    
    # クリーンな作業ディレクトリが必要なコマンド
    case "$command_name" in
        "create-pr")
            if ! git diff-index --quiet HEAD --; then
                echo "エラー: 作業ディレクトリにコミットされていない変更があります" >&2
                echo "変更をコミットまたはスタッシュしてください" >&2
                return 1
            fi
            ;;
    esac
}

# メイン検証関数
validate_command_prerequisites() {
    local command_name="$1"
    local metadata_file="${2:-}"
    shift 2
    local issue_numbers=("$@")
    
    echo "前提条件を確認中..."
    
    # 基本ツールチェック
    check_required_tools || return 1
    
    # Git リポジトリチェック
    check_git_repository || return 1
    
    # ワークディレクトリチェック
    check_working_directory || return 1
    
    # Python環境チェック（必要な場合）
    case "$command_name" in
        "create-tests"|"implement-domain"|"implement-usecase"|"implement-infra"|"run-all-tests"|"refactor")
            validate_python_environment || return 1
            ;;
    esac
    
    # メタデータ整合性チェック
    if [[ -n "$metadata_file" ]] && [[ -f "$metadata_file" ]]; then
        validate_metadata_integrity "$metadata_file" || return 1
    fi
    
    # フェーズ前提条件チェック
    if [[ -n "$metadata_file" ]]; then
        validate_phase_prerequisites "$command_name" "$metadata_file" || return 1
    fi
    
    # GitHub連携チェック
    case "$command_name" in
        "create-use-case"|"review-issue"|"apply-feedback"|"create-pr"|"evolve-scenarios")
            validate_github_prerequisites "$command_name" "${issue_numbers[@]}" || return 1
            ;;
    esac
    
    # Git ブランチ状態チェック
    validate_git_branch_state "$command_name" || return 1
    
    echo "前提条件チェック完了"
    return 0
}

# 警告表示関数
show_prerequisites_warning() {
    local command_name="$1"
    
    case "$command_name" in
        "create-tests"|"implement-domain"|"implement-usecase"|"implement-infra"|"run-all-tests"|"refactor")
            echo "注意: このコマンドは Python/uv 環境に変更を加えます"
            ;;
        "create-pr")
            echo "注意: このコマンドは Git リポジトリにプッシュし、プルリクエストを作成します"
            ;;
        "evolve-scenarios")
            echo "注意: このコマンドは新しい GitHub イシューを作成します"
            ;;
    esac
}