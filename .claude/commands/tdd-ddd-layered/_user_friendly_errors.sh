#!/bin/bash

# ユーザーフレンドリーなエラーメッセージシステム
# ビジネスユーザーにも理解しやすいエラー表示とガイダンス

set -euo pipefail

# エラーレベルの定義
declare -g -A ERROR_LEVELS=(
    ["CRITICAL"]="🚨 緊急"
    ["ERROR"]="❌ エラー" 
    ["WARNING"]="⚠️ 警告"
    ["INFO"]="💡 情報"
    ["SUCCESS"]="✅ 成功"
)

# ユーザータイプの定義
declare -g -A USER_TYPES=(
    ["BUSINESS"]="business"      # ビジネスユーザー向け
    ["DEVELOPER"]="developer"    # 開発者向け
    ["MANAGER"]="manager"        # プロジェクトマネージャー向け
)

# 現在のユーザータイプ（環境変数で設定可能）
USER_TYPE="${TDD_USER_TYPE:-developer}"

# 🌟 メインのエラー表示関数
show_user_friendly_error() {
    local error_code="$1"
    local level="${2:-ERROR}"
    local context="${3:-}"
    local additional_info="${4:-}"
    
    echo ""
    echo "${ERROR_LEVELS[$level]} ${error_code}"
    echo "================================"
    
    case "$error_code" in
        "GITHUB_NOT_AUTHENTICATED")
            show_github_auth_error "$level" "$context"
            ;;
        "MISSING_DEPENDENCIES")
            show_dependency_error "$level" "$context" "$additional_info"
            ;;
        "INVALID_ISSUE_NUMBER")
            show_issue_number_error "$level" "$context" "$additional_info"
            ;;
        "METADATA_FILE_MISSING")
            show_metadata_missing_error "$level" "$context" "$additional_info"
            ;;
        "PREREQUISITE_MISSING")
            show_prerequisite_error "$level" "$context" "$additional_info"
            ;;
        "GIT_OPERATION_FAILED")
            show_git_error "$level" "$context" "$additional_info"
            ;;
        "PYTHON_ENV_INVALID")
            show_python_env_error "$level" "$context"
            ;;
        "COMMAND_SEQUENCE_ERROR")
            show_sequence_error "$level" "$context" "$additional_info"
            ;;
        *)
            show_generic_error "$error_code" "$level" "$context" "$additional_info"
            ;;
    esac
    
    echo ""
    show_help_resources
}

# GitHub認証エラー
show_github_auth_error() {
    local level="$1"
    local context="$2"
    
    case "$USER_TYPE" in
        "business"|"manager")
            echo "📋 **状況説明**"
            echo "GitHubとの連携に問題があります。これにより、以下の機能が使用できません："
            echo "• イシューの自動更新"
            echo "• プルリクエストの作成"
            echo "• 進捗の自動通知"
            echo ""
            echo "🎯 **影響範囲**"
            echo "• 開発チームとの連携が一時的に制限されます"
            echo "• 手動での進捗管理が必要になります"
            echo ""
            echo "⏰ **解決予想時間**: 2-5分"
            ;;
        *)
            echo "📋 **技術的詳細**"
            echo "GitHub CLI の認証情報が設定されていないか、有効期限切れです。"
            echo ""
            echo "🔍 **確認方法**:"
            echo "gh auth status"
            ;;
    esac
    
    echo ""
    echo "🛠️ **解決手順**"
    echo "1. 認証設定を実行してください："
    echo "   gh auth login"
    echo ""
    echo "2. 表示される指示に従って認証を完了"
    echo ""
    echo "3. 認証完了後、元のコマンドを再実行"
    
    if [[ -n "$context" ]]; then
        echo ""
        echo "🔄 **再実行コマンド**: $context"
    fi
}

# 依存関係エラー
show_dependency_error() {
    local level="$1" 
    local context="$2"
    local missing_deps="$3"
    
    case "$USER_TYPE" in
        "business"|"manager")
            echo "📋 **状況説明**"
            echo "開発に必要なツールが不足しています。"
            echo "この問題により、自動化されたワークフローが動作しません。"
            echo ""
            echo "🎯 **影響範囲**"
            echo "• 機能開発の自動化が停止"
            echo "• コード品質チェックが無効"
            echo "• テスト実行が不可能"
            echo ""
            echo "⏰ **解決予想時間**: 5-15分"
            ;;
        *)
            echo "📋 **技術的詳細**"
            echo "必要な依存関係が不足しています: $missing_deps"
            echo ""
            echo "🔍 **環境確認**:"
            echo "which python3 && which jq && which gh"
            ;;
    esac
    
    echo ""
    echo "🛠️ **解決手順**"
    echo "1. パッケージマネージャーでの依存関係インストール："
    echo "   uv add $missing_deps"
    echo ""
    echo "2. インストール完了確認："
    echo "   uv run --frozen pytest --version"
    echo ""
    echo "3. 元のコマンドを再実行"
}

# イシュー番号エラー
show_issue_number_error() {
    local level="$1"
    local context="$2" 
    local provided_number="$3"
    
    case "$USER_TYPE" in
        "business"|"manager")
            echo "📋 **状況説明**"
            echo "指定されたイシュー番号に問題があります。"
            echo "GitHubイシューとの連携に必要な正しい番号が必要です。"
            echo ""
            echo "🎯 **次のステップ**"
            echo "• GitHubで対象のイシューを確認"
            echo "• 正しいイシュー番号で再実行"
            echo ""
            echo "⏰ **解決予想時間**: 1-3分"
            ;;
        *)
            echo "📋 **技術的詳細**"
            echo "無効なイシュー番号: '$provided_number'"
            echo "イシュー番号は正の整数である必要があります。"
            ;;
    esac
    
    echo ""
    echo "🛠️ **解決手順**"
    echo "1. GitHubでイシューリストを確認："
    echo "   gh issue list"
    echo ""
    echo "2. 正しいイシュー番号を確認"
    echo ""
    echo "3. 正しい番号で再実行："
    echo "   例: $context <正しいイシュー番号>"
    
    echo ""
    echo "💡 **ヒント**"
    echo "イシュー番号はGitHubのURL末尾の数字です"
    echo "例: https://github.com/user/repo/issues/123 → 123"
}

# メタデータファイル不足エラー  
show_metadata_missing_error() {
    local level="$1"
    local context="$2"
    local missing_file="$3"
    
    case "$USER_TYPE" in
        "business"|"manager")
            echo "📋 **状況説明**"
            echo "機能の進捗管理ファイルが見つかりません。"
            echo "この機能はまだ初期化されていない可能性があります。"
            echo ""
            echo "🎯 **対処法**"
            echo "• 機能の初期セットアップを実行"
            echo "• 必要に応じて機能仕様から作成を開始"
            echo ""
            echo "⏰ **解決予想時間**: 3-8分"
            ;;
        *)
            echo "📋 **技術的詳細**"
            echo "メタデータファイルが存在しません: $missing_file"
            echo "この機能のワークフローが開始されていません。"
            ;;
    esac
    
    echo ""
    echo "🛠️ **解決手順**"
    echo "1. 機能の初期作成から開始："
    echo "   /create-use-case <イシュー番号> <機能名>"
    echo ""
    echo "2. または既存の進捗を確認："
    echo "   /use-case-status <イシュー番号>"
    echo ""
    echo "3. 進捗に応じて適切なコマンドを実行"
    
    echo ""
    echo "💡 **推奨ワークフロー**"
    echo "/create-use-case → /domain-modeling → /create-tests → /implement-domain"
}

# 前提条件不足エラー
show_prerequisite_error() {
    local level="$1"
    local context="$2"
    local missing_prerequisite="$3"
    
    case "$USER_TYPE" in
        "business"|"manager")
            echo "📋 **状況説明**"
            echo "このステップを実行する前に完了すべき作業があります。"
            echo "開発プロセスは段階的に進める必要があります。"
            echo ""
            echo "🎯 **なぜ順序が重要か**"
            echo "• 品質の高いコードを確保"
            echo "• エラーの発生を防止"
            echo "• チーム全体での一貫性維持"
            echo ""
            echo "⏰ **解決予想時間**: 5-15分"
            ;;
        *)
            echo "📋 **技術的詳細**"
            echo "前提条件が満たされていません: $missing_prerequisite"
            echo "TDD/DDDワークフローの順序に従って実行してください。"
            ;;
    esac
    
    echo ""
    echo "🛠️ **解決手順**"
    echo "1. 現在の進捗を確認："
    echo "   /use-case-status <イシュー番号>"
    echo ""
    echo "2. 表示される「次のアクション」に従って実行"
    echo ""
    echo "3. 各ステップ完了後に元のコマンドを再実行"
    
    echo ""
    echo "📋 **標準ワークフロー順序**"
    echo "1. /create-use-case    (仕様作成)"
    echo "2. /domain-modeling    (設計)" 
    echo "3. /create-tests       (テスト作成)"
    echo "4. /implement-domain   (実装開始)"
    echo "5. ..."
}

# Git操作エラー
show_git_error() {
    local level="$1"
    local context="$2"
    local git_error="$3"
    
    case "$USER_TYPE" in
        "business"|"manager")
            echo "📋 **状況説明**"
            echo "コードのバージョン管理で問題が発生しました。"
            echo "他の開発者との作業の競合や、コード変更の問題が考えられます。"
            echo ""
            echo "🎯 **影響範囲**"
            echo "• コード変更の保存ができない"
            echo "• チームとの共同作業に支障"
            echo "• 作業内容の消失リスク"
            echo ""
            echo "⏰ **解決予想時間**: 5-10分"
            ;;
        *)
            echo "📋 **技術的詳細**"
            echo "Git操作でエラーが発生: $git_error"
            echo ""
            echo "🔍 **状態確認**:"
            echo "git status"
            ;;
    esac
    
    echo ""
    echo "🛠️ **解決手順**"
    echo "1. 現在の状況を確認："
    echo "   git status"
    echo ""
    echo "2. コンフリクトがある場合は解決"
    echo ""
    echo "3. 最新版を取得："
    echo "   git pull origin main"
    echo ""
    echo "4. 元のコマンドを再実行"
    
    echo ""
    echo "🆘 **緊急時の対処**"
    echo "作業内容を失いたくない場合："
    echo "1. git stash  (一時保存)"
    echo "2. git pull   (最新取得)"
    echo "3. git stash pop  (作業内容復元)"
}

# Python環境エラー
show_python_env_error() {
    local level="$1"
    local context="$2"
    
    case "$USER_TYPE" in
        "business"|"manager")
            echo "📋 **状況説明**"
            echo "Python開発環境に問題があります。"
            echo "自動化されたテストや品質チェックが実行できません。"
            echo ""
            echo "🎯 **影響範囲**"
            echo "• コード品質の検証ができない"
            echo "• 自動テストが実行できない"
            echo "• 開発効率の大幅な低下"
            echo ""
            echo "⏰ **解決予想時間**: 10-20分"
            ;;
        *)
            echo "📋 **技術的詳細**"
            echo "Python環境またはuvの設定に問題があります。"
            echo ""
            echo "🔍 **環境確認**:"
            echo "which python3 && which uv"
            ;;
    esac
    
    echo ""
    echo "🛠️ **解決手順**"
    echo "1. uvがインストールされているか確認："
    echo "   uv --version"
    echo ""
    echo "2. プロジェクトの依存関係をインストール："
    echo "   uv sync"
    echo ""
    echo "3. 環境の動作確認："
    echo "   uv run python --version"
}

# コマンド順序エラー
show_sequence_error() {
    local level="$1"
    local context="$2"
    local expected_command="$3"
    
    case "$USER_TYPE" in
        "business"|"manager")
            echo "📋 **状況説明**"
            echo "開発プロセスの順序に問題があります。"
            echo "品質を確保するため、決められた順序での実行が必要です。"
            echo ""
            echo "🎯 **なぜ順序が重要か**"
            echo "• エラーの早期発見"
            echo "• 高品質なコード保証"
            echo "• チームでの一貫性"
            echo ""
            echo "⏰ **解決予想時間**: 2-5分"
            ;;
        *)
            echo "📋 **技術的詳細**"
            echo "コマンド実行順序が不正です。"
            echo "期待されるコマンド: $expected_command"
            ;;
    esac
    
    echo ""
    echo "🛠️ **解決手順**"
    echo "1. まず期待されるコマンドを実行："
    echo "   $expected_command"
    echo ""
    echo "2. 完了後、元のコマンドを再実行"
    echo ""
    echo "3. 順序が分からない場合は進捗確認："
    echo "   /use-case-status <イシュー番号>"
}

# 汎用エラー
show_generic_error() {
    local error_code="$1"
    local level="$2"
    local context="$3"
    local additional_info="$4"
    
    case "$USER_TYPE" in
        "business"|"manager")
            echo "📋 **状況説明**"
            echo "予期しない問題が発生しました。"
            echo "システムまたは設定に問題がある可能性があります。"
            echo ""
            echo "🎯 **対処方針**"
            echo "• 技術チームへの報告を推奨"
            echo "• 詳細なエラー情報の収集"
            echo ""
            echo "⏰ **解決予想時間**: 10-30分"
            ;;
        *)
            echo "📋 **技術的詳細**"
            echo "未分類のエラー: $error_code"
            if [[ -n "$additional_info" ]]; then
                echo "追加情報: $additional_info"
            fi
            ;;
    esac
    
    echo ""
    echo "🛠️ **解決手順**"
    echo "1. 進捗状況を確認："
    echo "   /use-case-status <イシュー番号>"
    echo ""
    echo "2. 提案されたコマンドを実行"
    echo ""
    echo "3. 問題が継続する場合はログを確認"
    
    if [[ -n "$context" ]]; then
        echo ""
        echo "🔄 **実行中のコマンド**: $context"
    fi
}

# ヘルプリソースの表示
show_help_resources() {
    echo "📚 **追加リソース**"
    echo "• クイックスタート: QUICKSTART.md を参照"
    echo "• 詳細ガイド: INTEGRATION_GUIDE.md を参照"
    echo "• 進捗確認: /use-case-status <イシュー番号>"
    echo "• コマンド一覧: README.md を参照"
}

# ユーザータイプ設定関数
set_user_type() {
    local type="$1"
    case "$type" in
        "business"|"developer"|"manager")
            export TDD_USER_TYPE="$type"
            echo "ユーザータイプを設定しました: $type"
            ;;
        *)
            echo "エラー: 無効なユーザータイプ: $type" >&2
            echo "有効な値: business, developer, manager" >&2
            return 1
            ;;
    esac
}

# 簡易エラー関数（よく使用される）
error_github_auth() {
    show_user_friendly_error "GITHUB_NOT_AUTHENTICATED" "ERROR" "${1:-}" "${2:-}"
}

error_missing_deps() {
    show_user_friendly_error "MISSING_DEPENDENCIES" "ERROR" "${1:-}" "${2:-}"  
}

error_invalid_issue() {
    show_user_friendly_error "INVALID_ISSUE_NUMBER" "ERROR" "${1:-}" "${2:-}"
}

error_missing_metadata() {
    show_user_friendly_error "METADATA_FILE_MISSING" "ERROR" "${1:-}" "${2:-}"
}

error_missing_prerequisite() {
    show_user_friendly_error "PREREQUISITE_MISSING" "ERROR" "${1:-}" "${2:-}"
}

error_git_operation() {
    show_user_friendly_error "GIT_OPERATION_FAILED" "ERROR" "${1:-}" "${2:-}"
}

error_python_env() {
    show_user_friendly_error "PYTHON_ENV_INVALID" "ERROR" "${1:-}" "${2:-}"
}

error_command_sequence() {
    show_user_friendly_error "COMMAND_SEQUENCE_ERROR" "ERROR" "${1:-}" "${2:-}"
}

echo "ユーザーフレンドリーエラーシステムが読み込まれました"
echo "現在のユーザータイプ: $USER_TYPE"