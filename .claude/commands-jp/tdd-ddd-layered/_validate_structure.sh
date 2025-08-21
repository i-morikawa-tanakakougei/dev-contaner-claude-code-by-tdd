#!/bin/bash

# TDD/DDD/Layered Architecture カスタムコマンド用軽量構造確認スクリプト
# プロジェクト構造の基本的な整合性を保証

set -euo pipefail

# 基本構造確認関数
validate_basic_structure() {
    local command_name="${1:-unknown}"
    
    echo "🔍 基本構造確認: $command_name"
    
    # 作業ディレクトリ確認
    if [[ ! -w "." ]]; then
        echo "❌ 作業ディレクトリに書き込み権限がありません"
        return 1
    fi
    
    # Git リポジトリ確認（必須ではない）
    if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
        echo "  ✅ Git リポジトリ: 検出"
    else
        echo "  ⚠️  Git リポジトリ: 未検出（推奨）"
    fi
    
    echo "  ✅ 基本構造確認完了"
    return 0
}

# プロジェクト構造確認関数（01-init-project-structure用）
validate_project_init_structure() {
    echo "🏗️ プロジェクト初期化構造確認"
    
    # プロジェクト設定ファイル確認
    local has_config=false
    for config_file in "pyproject.toml" "package.json" "Cargo.toml"; do
        if [[ -f "$config_file" ]]; then
            echo "  ✅ 設定ファイル: $config_file 検出"
            has_config=true
            break
        fi
    done
    
    if [[ "$has_config" == "false" ]]; then
        echo "  ⚠️  プロジェクト設定ファイルが見つかりません"
        echo "新しいプロジェクトを初期化しますか？ (y/N): "
        read -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "プロジェクト初期化をキャンセルしました"
            return 1
        fi
    fi
    
    # 既存構造確認
    local existing_dirs=()
    for dir in "src" "docs" "tests"; do
        if [[ -d "$dir" ]]; then
            existing_dirs+=("$dir")
        fi
    done
    
    if [[ ${#existing_dirs[@]} -gt 0 ]]; then
        echo "  ⚠️  既存構造が検出されました: ${existing_dirs[*]}"
        echo "既存の構造を上書きしますか？ (y/N): "
        read -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "プロジェクト初期化をキャンセルしました"
            return 1
        fi
    fi
    
    echo "  ✅ プロジェクト初期化構造確認完了"
    return 0
}

# ドキュメント構造確認関数（12-evolve-scenarios用）
validate_docs_structure() {
    echo "📚 ドキュメント構造確認"
    
    # docs/use_cases ディレクトリ確認
    if [[ ! -d "docs/use_cases" ]]; then
        echo "  ❌ docs/use_cases ディレクトリが見つかりません"
        echo "  💡 最初に /create-use-case でユースケースを作成してください"
        return 1
    fi
    
    # 既存シナリオファイル確認
    local scenario_count=$(find docs/use_cases -name "*.json" -type f 2>/dev/null | wc -l)
    if [[ $scenario_count -eq 0 ]]; then
        echo "  ❌ 既存のシナリオファイルが見つかりません"
        echo "  💡 最初に /create-use-case でユースケースを作成してください"
        return 1
    fi
    
    echo "  ✅ ドキュメント構造確認完了 (シナリオファイル: ${scenario_count}個)"
    return 0
}

# レビュー用構造確認関数（04.5, 05.5, 10.5用）
validate_review_structure() {
    local review_type="${1:-unknown}"
    
    echo "🔍 レビュー構造確認: $review_type"
    
    # 分析対象ディレクトリ確認
    case "$review_type" in
        "domain-design")
            if [[ ! -d "docs/domain" ]]; then
                echo "  ❌ docs/domain ディレクトリが見つかりません"
                echo "  💡 最初に /domain-modeling でドメイン設計を作成してください"
                return 1
            fi
            ;;
        "test-design")
            if [[ ! -d "tests" ]]; then
                echo "  ❌ tests ディレクトリが見つかりません"
                echo "  💡 最初に /create-tests でテストを作成してください"
                return 1
            fi
            ;;
        "test-results")
            if [[ ! -d "tests" ]]; then
                echo "  ❌ tests ディレクトリが見つかりません"
                echo "  💡 最初に /run-all-tests でテストを実行してください"
                return 1
            fi
            ;;
    esac
    
    # レポート出力先確認・作成
    if [[ ! -d "docs/analysis" ]]; then
        echo "  📁 docs/analysis ディレクトリを作成中..."
        mkdir -p "docs/analysis"
    fi
    
    echo "  ✅ レビュー構造確認完了"
    return 0
}

# メイン実行部分
main() {
    local command_name="${1:-}"
    local review_type="${2:-}"
    
    case "$command_name" in
        "01-init-project-structure")
            validate_basic_structure "$command_name"
            validate_project_init_structure
            ;;
        "12-evolve-scenarios")
            validate_basic_structure "$command_name"
            validate_docs_structure
            ;;
        "04.5-review-domain-design")
            validate_basic_structure "$command_name"
            validate_review_structure "domain-design"
            ;;
        "05.5-review-test-design")
            validate_basic_structure "$command_name"
            validate_review_structure "test-design"
            ;;
        "10.5-review-test-results")
            validate_basic_structure "$command_name"
            validate_review_structure "test-results"
            ;;
        *)
            validate_basic_structure "$command_name"
            ;;
    esac
}

# スクリプトが直接実行された場合
if [[ "${BASH_SOURCE[0]:-}" == "${0}" ]]; then
    main "$@"
fi

# 使用方法表示関数
show_usage() {
    echo ""
    echo "🔧 軽量構造確認スクリプト使用方法:"
    echo "=========================================="
    echo ""
    echo "📁 基本使用法:"
    echo "  source _validate_structure.sh"
    echo "  validate_basic_structure <command_name>"
    echo ""
    echo "🏗️ プロジェクト初期化:"
    echo "  source _validate_structure.sh"
    echo "  main \"01-init-project-structure\""
    echo ""
    echo "📚 ドキュメント構造:"
    echo "  source _validate_structure.sh"
    echo "  main \"12-evolve-scenarios\""
    echo ""
    echo "🔍 レビュー構造:"
    echo "  source _validate_structure.sh"
    echo "  main \"04.5-review-domain-design\""
    echo "  main \"05.5-review-test-design\""
    echo "  main \"10.5-review-test-results\""
    echo ""
}

# ヘルプが要求された場合
if [[ "${1:-}" == "--help" ]] || [[ "${1:-}" == "-h" ]]; then
    show_usage
fi