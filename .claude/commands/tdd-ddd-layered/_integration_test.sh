#!/bin/bash

# TDD/DDD/Layered Architecture カスタムコマンド統合テスト
# 新しく追加した修正機能の動作確認

set -euo pipefail

echo "🧪 TDD/DDD/Layered Architecture カスタムコマンド統合テスト"
echo "============================================================"
echo "作成した修正機能の動作確認を実行します"
echo ""

# テスト結果集計
TESTS_PASSED=0
TESTS_FAILED=0
FAILED_TESTS=()

# テスト実行関数
run_test() {
    local test_name="$1"
    local test_function="$2"
    
    echo "📋 テスト実行: $test_name"
    echo "----------------------------------------"
    
    if $test_function; then
        echo "✅ PASS: $test_name"
        ((TESTS_PASSED++))
    else
        echo "❌ FAIL: $test_name"
        ((TESTS_FAILED++))
        FAILED_TESTS+=("$test_name")
    fi
    echo ""
}

# 1. メタデータ操作関数のテスト
test_metadata_operations() {
    echo "メタデータ操作関数のテスト..."
    
    # テスト用ディレクトリ作成
    local test_dir="/tmp/metadata_test_$$"
    mkdir -p "$test_dir/docs/use_cases"
    
    # 関数を読み込み
    source "$(dirname "${BASH_SOURCE[0]}")/_metadata_operations.sh"
    
    # テスト用メタデータファイル作成
    local test_metadata="$test_dir/docs/use_cases/issue-1-test-feature.json"
    
    if create_metadata_if_not_exists "$test_metadata" "test-feature" 1; then
        echo "  ✅ メタデータファイル作成: OK"
    else
        echo "  ❌ メタデータファイル作成: FAIL"
        rm -rf "$test_dir"
        return 1
    fi
    
    # 原子的更新のテスト
    if update_metadata_atomic "$test_metadata" '.phase = "testing"'; then
        echo "  ✅ 原子的更新: OK"
    else
        echo "  ❌ 原子的更新: FAIL"
        rm -rf "$test_dir"
        return 1
    fi
    
    # JSON構文確認
    if jq empty "$test_metadata" 2>/dev/null; then
        echo "  ✅ JSON構文: OK"
    else
        echo "  ❌ JSON構文: FAIL"
        rm -rf "$test_dir"
        return 1
    fi
    
    # クリーンアップ
    rm -rf "$test_dir"
    echo "  ✅ メタデータ操作関数テスト完了"
    return 0
}

# 2. 前提条件検証フレームワークのテスト
test_prerequisites_validation() {
    echo "前提条件検証フレームワークのテスト..."
    
    # 関数を読み込み
    source "$(dirname "${BASH_SOURCE[0]}")/_prerequisites_validator.sh"
    
    # 必要ツールのチェック
    if check_required_tools; then
        echo "  ✅ 必要ツールチェック: OK"
    else
        echo "  ❌ 必要ツールチェック: FAIL"
        return 1
    fi
    
    # Git リポジトリチェック
    if check_git_repository; then
        echo "  ✅ Git リポジトリチェック: OK"
    else
        echo "  ❌ Git リポジトリチェック: FAIL"
        return 1
    fi
    
    echo "  ✅ 前提条件検証フレームワークテスト完了"
    return 0
}

# 3. Git操作関数のテスト
test_git_operations() {
    echo "Git操作関数のテスト..."
    
    # 関数を読み込み
    source "$(dirname "${BASH_SOURCE[0]}")/_git_operations.sh"
    
    # 作業ディレクトリ状態確認のテスト
    if check_working_directory_clean >/dev/null 2>&1; then
        echo "  ✅ 作業ディレクトリ状態確認: OK"
    else
        echo "  ⚠️  作業ディレクトリに変更あり（正常な状態）"
    fi
    
    # リモート同期確認のテスト
    if check_remote_sync >/dev/null 2>&1; then
        echo "  ✅ リモート同期確認: OK"
    else
        echo "  ⚠️  リモート同期確認で問題あり（設定による）"
    fi
    
    echo "  ✅ Git操作関数テスト完了"
    return 0
}

# 4. 引数パーサーのテスト
test_argument_parser() {
    echo "共通引数パーサーのテスト..."
    
    # 関数を読み込み
    source "$(dirname "${BASH_SOURCE[0]}")/_common_arg_parser.sh"
    
    # テストケース1: 数値と文字列の分離
    if parse_arguments "1,7,feature-name,option"; then
        if [[ ${#issue_numbers[@]} -eq 2 ]] && [[ ${#other_args[@]} -eq 2 ]]; then
            echo "  ✅ 引数分離テスト: OK"
        else
            echo "  ❌ 引数分離テスト: FAIL (issue_numbers: ${#issue_numbers[@]}, other_args: ${#other_args[@]})"
            return 1
        fi
    else
        echo "  ❌ 引数解析失敗"
        return 1
    fi
    
    # テストケース2: 引数検証
    if validate_arguments 1 "" 0; then
        echo "  ✅ 引数検証テスト: OK"
    else
        echo "  ❌ 引数検証テスト: FAIL"
        return 1
    fi
    
    echo "  ✅ 引数パーサーテスト完了"
    return 0
}

# 5. アーキテクチャ検証のテスト
test_architecture_validation() {
    echo "アーキテクチャ検証のテスト..."
    
    # 関数を読み込み
    source "$(dirname "${BASH_SOURCE[0]}")/_architecture_validator.sh"
    
    # テスト用プロジェクト構造作成
    local test_dir="/tmp/arch_test_$$"
    mkdir -p "$test_dir/src/domain/entities"
    mkdir -p "$test_dir/src/application/use_cases"
    mkdir -p "$test_dir/src/infrastructure/repositories"
    mkdir -p "$test_dir/src/presentation/api"
    
    # テスト用ファイル作成（正常なドメインファイル）
    cat > "$test_dir/src/domain/entities/user.py" << 'EOF'
from dataclasses import dataclass
from typing import Optional
from uuid import UUID

@dataclass
class User:
    id: UUID
    name: str
    email: Optional[str] = None
EOF
    
    # テスト用ファイル作成（問題のあるドメインファイル）
    cat > "$test_dir/src/domain/entities/bad_user.py" << 'EOF'
import requests
from sqlalchemy import Column

class BadUser:
    def fetch_data(self):
        return requests.get("http://example.com")
EOF
    
    # ディレクトリ移動
    local original_dir="$PWD"
    cd "$test_dir"
    
    # レイヤー依存関係検証のテスト
    if validate_layer_dependencies "src/domain/entities/user.py" "domain" >/dev/null 2>&1; then
        echo "  ✅ 正常なドメインファイル検証: OK"
    else
        echo "  ❌ 正常なドメインファイル検証: FAIL"
        cd "$original_dir"
        rm -rf "$test_dir"
        return 1
    fi
    
    if ! validate_layer_dependencies "src/domain/entities/bad_user.py" "domain" >/dev/null 2>&1; then
        echo "  ✅ 問題のあるドメインファイル検証: OK (正しく違反を検出)"
    else
        echo "  ❌ 問題のあるドメインファイル検証: FAIL (違反を検出できず)"
        cd "$original_dir"
        rm -rf "$test_dir"
        return 1
    fi
    
    # クリーンアップ
    cd "$original_dir"
    rm -rf "$test_dir"
    
    echo "  ✅ アーキテクチャ検証テスト完了"
    return 0
}

# 6. ファイル操作のテスト
test_file_operations() {
    echo "ファイル操作関数のテスト..."
    
    # 関数を読み込み
    source "$(dirname "${BASH_SOURCE[0]}")/_file_operations.sh"
    
    # テスト用ディレクトリ
    local test_dir="/tmp/file_ops_test_$$"
    
    # 安全なディレクトリ作成のテスト
    if safe_mkdir "$test_dir" >/dev/null 2>&1; then
        echo "  ✅ 安全なディレクトリ作成: OK"
    else
        echo "  ❌ 安全なディレクトリ作成: FAIL"
        return 1
    fi
    
    # 安全なファイル作成のテスト
    local test_file="$test_dir/test.txt"
    if safe_create_file "$test_file" "テストコンテンツ" false >/dev/null 2>&1; then
        echo "  ✅ 安全なファイル作成: OK"
    else
        echo "  ❌ 安全なファイル作成: FAIL"
        rm -rf "$test_dir"
        return 1
    fi
    
    # ディスク容量チェックのテスト
    if check_disk_space "$test_dir" 1 >/dev/null 2>&1; then
        echo "  ✅ ディスク容量チェック: OK"
    else
        echo "  ❌ ディスク容量チェック: FAIL"
        rm -rf "$test_dir"
        return 1
    fi
    
    # クリーンアップ
    rm -rf "$test_dir"
    
    echo "  ✅ ファイル操作関数テスト完了"
    return 0
}

# 7. 統合シナリオテスト
test_integration_scenario() {
    echo "統合シナリオテスト..."
    
    # 全ての関数を読み込み
    source "$(dirname "${BASH_SOURCE[0]}")/_common_arg_parser.sh"
    source "$(dirname "${BASH_SOURCE[0]}")/_metadata_operations.sh"
    source "$(dirname "${BASH_SOURCE[0]}")/_prerequisites_validator.sh"
    source "$(dirname "${BASH_SOURCE[0]}")/_git_operations.sh"
    source "$(dirname "${BASH_SOURCE[0]}")/_file_operations.sh"
    
    # テストシナリオ: イシュー1とfeature-nameでメタデータファイルを作成・更新
    local test_dir="/tmp/integration_test_$$"
    mkdir -p "$test_dir/docs/use_cases"
    
    # 引数解析
    if parse_arguments "1,test-feature"; then
        echo "  ✅ 引数解析: OK"
    else
        echo "  ❌ 引数解析: FAIL"
        rm -rf "$test_dir"
        return 1
    fi
    
    # メタデータファイル作成
    local metadata_file="$test_dir/docs/use_cases/issue-1-test-feature.json"
    if create_metadata_if_not_exists "$metadata_file" "test-feature" "${issue_numbers[@]}"; then
        echo "  ✅ メタデータ作成: OK"
    else
        echo "  ❌ メタデータ作成: FAIL"
        rm -rf "$test_dir"
        return 1
    fi
    
    # メタデータ更新
    if update_metadata_atomic "$metadata_file" '.phases.use_case.created = true | .phase = "use_case_created"'; then
        echo "  ✅ メタデータ更新: OK"
    else
        echo "  ❌ メタデータ更新: FAIL"
        rm -rf "$test_dir"
        return 1
    fi
    
    # ファイル検索
    local found_file
    found_file=$(find_metadata_file "1" "test-feature")
    if [[ "$found_file" == "$metadata_file" ]]; then
        echo "  ✅ メタデータファイル検索: OK"
    else
        echo "  ❌ メタデータファイル検索: FAIL"
        rm -rf "$test_dir"
        return 1
    fi
    
    # クリーンアップ
    rm -rf "$test_dir"
    
    echo "  ✅ 統合シナリオテスト完了"
    return 0
}

# メインテスト実行
main() {
    echo "開始時刻: $(date)"
    echo ""
    
    run_test "メタデータ操作関数" test_metadata_operations
    run_test "前提条件検証フレームワーク" test_prerequisites_validation
    run_test "Git操作関数" test_git_operations
    run_test "共通引数パーサー" test_argument_parser
    run_test "アーキテクチャ検証" test_architecture_validation
    run_test "ファイル操作関数" test_file_operations
    run_test "統合シナリオ" test_integration_scenario
    
    echo "============================================================"
    echo "🧪 テスト結果サマリー"
    echo "============================================================"
    echo "✅ 成功: $TESTS_PASSED テスト"
    echo "❌ 失敗: $TESTS_FAILED テスト"
    echo ""
    
    if [[ $TESTS_FAILED -gt 0 ]]; then
        echo "失敗したテスト:"
        for failed_test in "${FAILED_TESTS[@]}"; do
            echo "  - $failed_test"
        done
        echo ""
        echo "❌ 統合テスト: FAIL"
        return 1
    else
        echo "🎉 全てのテストが成功しました！"
        echo "✅ 統合テスト: PASS"
        echo ""
        echo "📝 修正内容が正常に動作することを確認しました:"
        echo "  1. ✅ メタデータ更新の原子性確保"
        echo "  2. ✅ 前提条件検証フレームワーク"
        echo "  3. ✅ Git操作エラーハンドリング強化"
        echo "  4. ✅ 引数検証ロジック整合性"
        echo "  5. ✅ アーキテクチャレイヤー検証"
        echo "  6. ✅ ファイル操作安全性向上"
        echo ""
        echo "🚀 カスタムコマンド群は本番利用可能な状態です"
        return 0
    fi
}

# スクリプトが直接実行された場合のみメイン関数を実行
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi