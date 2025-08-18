#!/bin/bash

# TDD/DDD/Layered Architecture カスタムコマンド用安全環境セットアップ
# 全ての修正済み関数群を読み込み、安全な実行環境を提供

set -euo pipefail

# スクリプトディレクトリの取得
SCRIPT_DIR="$(dirname "${BASH_SOURCE[0]}")"

# 安全な関数群の読み込み
echo "🔧 安全な実行環境をセットアップ中..."

# 1. 共通引数パーサー
if [[ -f "$SCRIPT_DIR/_common_arg_parser.sh" ]]; then
    source "$SCRIPT_DIR/_common_arg_parser.sh"
    echo "  ✅ 引数パーサー読み込み完了"
else
    echo "  ❌ 引数パーサーが見つかりません" >&2
    exit 1
fi

# 2. メタデータ操作（原子性確保）
if [[ -f "$SCRIPT_DIR/_metadata_operations.sh" ]]; then
    source "$SCRIPT_DIR/_metadata_operations.sh"
    echo "  ✅ メタデータ操作関数読み込み完了"
else
    echo "  ❌ メタデータ操作関数が見つかりません" >&2
    exit 1
fi

# 2b. メタデータ標準パターン
if [[ -f "$SCRIPT_DIR/_metadata_standards.sh" ]]; then
    source "$SCRIPT_DIR/_metadata_standards.sh"
    echo "  ✅ メタデータ標準パターン読み込み完了"
else
    echo "  ❌ メタデータ標準パターンが見つかりません" >&2
    exit 1
fi

# 3. 前提条件検証
if [[ -f "$SCRIPT_DIR/_prerequisites_validator.sh" ]]; then
    source "$SCRIPT_DIR/_prerequisites_validator.sh"
    echo "  ✅ 前提条件検証関数読み込み完了"
else
    echo "  ❌ 前提条件検証関数が見つかりません" >&2
    exit 1
fi

# 4. Git操作（安全性確保）
if [[ -f "$SCRIPT_DIR/_git_operations.sh" ]]; then
    source "$SCRIPT_DIR/_git_operations.sh"
    echo "  ✅ Git操作関数読み込み完了"
else
    echo "  ❌ Git操作関数が見つかりません" >&2
    exit 1
fi

# 5. ファイル操作（安全性確保）
if [[ -f "$SCRIPT_DIR/_file_operations.sh" ]]; then
    source "$SCRIPT_DIR/_file_operations.sh"
    echo "  ✅ ファイル操作関数読み込み完了"
else
    echo "  ❌ ファイル操作関数が見つかりません" >&2
    exit 1
fi

# 6. アーキテクチャ検証
if [[ -f "$SCRIPT_DIR/_architecture_validator.sh" ]]; then
    source "$SCRIPT_DIR/_architecture_validator.sh"
    echo "  ✅ アーキテクチャ検証関数読み込み完了"
else
    echo "  ❌ アーキテクチャ検証関数が見つかりません" >&2
    exit 1
fi

# 7. GitHub操作（API エラーハンドリング）
if [[ -f "$SCRIPT_DIR/_github_operations.sh" ]]; then
    source "$SCRIPT_DIR/_github_operations.sh"
    echo "  ✅ GitHub操作関数読み込み完了"
else
    echo "  ❌ GitHub操作関数が見つかりません" >&2
    exit 1
fi

# 8. トランザクション フレームワーク
if [[ -f "$SCRIPT_DIR/_transaction_framework.sh" ]]; then
    source "$SCRIPT_DIR/_transaction_framework.sh"
    echo "  ✅ トランザクション フレームワーク読み込み完了"
else
    echo "  ❌ トランザクション フレームワークが見つかりません" >&2
    exit 1
fi

# 9. ユーザーフレンドリーエラーシステム
if [[ -f "$SCRIPT_DIR/_user_friendly_errors.sh" ]]; then
    source "$SCRIPT_DIR/_user_friendly_errors.sh"
    echo "  ✅ ユーザーフレンドリーエラーシステム読み込み完了"
else
    echo "  ❌ ユーザーフレンドリーエラーシステムが見つかりません" >&2
    exit 1
fi

# 10. 自動提案エンジン
if [[ -f "$SCRIPT_DIR/_auto_suggestion_engine.sh" ]]; then
    source "$SCRIPT_DIR/_auto_suggestion_engine.sh"
    echo "  ✅ 自動提案エンジン読み込み完了"
else
    echo "  ❌ 自動提案エンジンが見つかりません" >&2
    exit 1
fi

echo "🚀 安全な実行環境セットアップ完了"

# グローバル設定
export TDD_DDD_SAFE_MODE=true
export TDD_DDD_SCRIPT_DIR="$SCRIPT_DIR"

# 前提条件チェック（実行コマンド名が提供された場合）
if [[ "${1:-}" =~ ^[0-9]{2}-.* ]]; then
    COMMAND_NAME="$1"
    shift
    
    echo "📋 前提条件チェック実行中: $COMMAND_NAME"
    
    # メタデータファイルの特定（イシュー番号が提供された場合）
    METADATA_FILE=""
    if [[ "${1:-}" =~ ^[0-9,]+ ]]; then
        # 引数を解析してメタデータファイルを特定
        parse_arguments "$1"
        if [[ ${#issue_numbers[@]} -gt 0 ]]; then
            issue_list=$(IFS=-; echo "${issue_numbers[*]}")
            if [[ ${#other_args[@]} -gt 0 ]]; then
                feature_name="${other_args[0]}"
                METADATA_FILE="docs/use_cases/issue-${issue_list}-${feature_name}.json"
            else
                # 既存ファイルから検索
                METADATA_FILE=$(find docs/use_cases -name "issue-${issue_list}-*.json" 2>/dev/null | head -1 || echo "")
            fi
        fi
    fi
    
    # 前提条件検証実行
    if validate_command_prerequisites "$COMMAND_NAME" "$METADATA_FILE" "${issue_numbers[@]:-}"; then
        echo "✅ 前提条件チェック完了"
    else
        echo "❌ 前提条件チェック失敗"
        exit 1
    fi
fi

# 使用方法の表示
show_safe_usage() {
    echo ""
    echo "🔧 安全な関数群の使用方法:"
    echo "=========================================="
    echo ""
    echo "📁 メタデータ操作:"
    echo "  create_metadata_if_not_exists <file> <feature> <issues...>"
    echo "  update_metadata_atomic <file> <jq_expression>"
    echo "  find_metadata_file <issue_list> [feature_name]"
    echo ""
    echo "🔍 前提条件チェック:"
    echo "  validate_command_prerequisites <command> <metadata_file> <issues...>"
    echo "  check_required_tools"
    echo "  check_git_repository"
    echo ""
    echo "📦 Git操作:"
    echo "  safe_create_or_switch_branch <branch_name> [base_branch]"
    echo "  safe_git_commit <message> [files...]"
    echo "  safe_git_push [branch_name] [force]"
    echo ""
    echo "📄 ファイル操作:"
    echo "  safe_mkdir <path> [mode]"
    echo "  safe_create_file <path> [content] [backup]"
    echo "  safe_move_file <src> <dest> [backup]"
    echo ""
    echo "🏗️ アーキテクチャ検証:"
    echo "  validate_architecture"
    echo "  validate_specific_layer <layer>"
    echo "  validate_domain_purity"
    echo ""
}

# ヘルプが要求された場合
if [[ "${1:-}" == "--help" ]] || [[ "${1:-}" == "-h" ]]; then
    show_safe_usage
fi