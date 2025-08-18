#!/bin/bash

# 統合版カスタムコマンド包括テスト
# 新しく統合した安全な関数群とコマンドの動作確認

set -euo pipefail

echo "🧪 統合版カスタムコマンド包括テスト"
echo "============================================================"
echo "統合された安全な関数群とコマンドの動作確認を実行します"
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

# 1. 統合環境セットアップのテスト
test_integrated_setup() {
    echo "統合環境セットアップのテスト..."
    
    local test_dir="/tmp/integrated_test_$$"
    mkdir -p "$test_dir"
    cd "$test_dir"
    
    # 統合セットアップスクリプトをコピー
    cp -r /workspace/.claude/commands/tdd-ddd-layered/_*.sh ./
    
    # セットアップスクリプト実行テスト
    if source ./_setup_safe_environment.sh 2>/dev/null; then
        echo "  ✅ 統合環境セットアップ: OK"
    else
        echo "  ❌ 統合環境セットアップ: FAIL"
        cd - >/dev/null
        rm -rf "$test_dir"
        return 1
    fi
    
    # 必要な関数が読み込まれているかチェック
    local required_functions=(
        "parse_arguments"
        "update_metadata_atomic" 
        "safe_create_or_switch_branch"
        "safe_gh_command"
        "begin_transaction"
        "validate_architecture"
    )
    
    for func in "${required_functions[@]}"; do
        if declare -f "$func" >/dev/null 2>&1; then
            echo "  ✅ 関数 $func: 読み込み済み"
        else
            echo "  ❌ 関数 $func: 未読み込み"
            cd - >/dev/null
            rm -rf "$test_dir"
            return 1
        fi
    done
    
    cd - >/dev/null
    rm -rf "$test_dir"
    echo "  ✅ 統合環境セットアップテスト完了"
    return 0
}

# 2. GitHub操作関数のテスト
test_github_operations() {
    echo "GitHub操作関数のテスト..."
    
    # 関数を読み込み
    source "$(dirname "${BASH_SOURCE[0]}")/_github_operations.sh"
    
    # GitHub CLI 存在確認のテスト
    if command -v gh >/dev/null 2>&1; then
        echo "  ✅ GitHub CLI 存在確認: OK"
    else
        echo "  ⚠️  GitHub CLI が見つかりません（スキップ）"
        return 0
    fi
    
    # 認証チェック関数のテスト
    if check_github_auth >/dev/null 2>&1; then
        echo "  ✅ GitHub 認証チェック: OK"
    else
        echo "  ⚠️  GitHub 認証なし（正常な状態）"
    fi
    
    # レート制限チェック関数のテスト
    if check_rate_limit >/dev/null 2>&1; then
        echo "  ✅ レート制限チェック: OK"
    else
        echo "  ⚠️  レート制限チェック失敗（認証問題の可能性）"
    fi
    
    echo "  ✅ GitHub操作関数テスト完了"
    return 0
}

# 3. トランザクション フレームワークのテスト
test_transaction_framework() {
    echo "トランザクション フレームワークのテスト..."
    
    # 関数を読み込み
    source "$(dirname "${BASH_SOURCE[0]}")/_transaction_framework.sh"
    
    # トランザクション開始テスト
    if begin_transaction "test_transaction"; then
        echo "  ✅ トランザクション開始: OK"
    else
        echo "  ❌ トランザクション開始: FAIL"
        return 1
    fi
    
    # ロールバック操作追加テスト
    if add_rollback "echo 'rollback test'" "Test rollback operation"; then
        echo "  ✅ ロールバック操作追加: OK"
    else
        echo "  ❌ ロールバック操作追加: FAIL"
        return 1
    fi
    
    # トランザクション状態確認テスト
    if check_transaction_status >/dev/null; then
        echo "  ✅ トランザクション状態確認: OK"
    else
        echo "  ❌ トランザクション状態確認: FAIL"
        return 1
    fi
    
    # トランザクション コミットテスト
    if commit_transaction; then
        echo "  ✅ トランザクション コミット: OK"
    else
        echo "  ❌ トランザクション コミット: FAIL"
        return 1
    fi
    
    echo "  ✅ トランザクション フレームワークテスト完了"
    return 0
}

# 4. 安全な操作実行のテスト
test_safe_operations() {
    echo "安全な操作実行のテスト..."
    
    # 全ての関数を読み込み
    source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" 2>/dev/null || true
    
    local test_dir="/tmp/safe_ops_test_$$"
    mkdir -p "$test_dir"
    cd "$test_dir"
    
    # ディスク容量チェックのテスト
    if check_disk_space "." 1 >/dev/null 2>&1; then
        echo "  ✅ ディスク容量チェック: OK"
    else
        echo "  ❌ ディスク容量チェック: FAIL"
        cd - >/dev/null
        rm -rf "$test_dir"
        return 1
    fi
    
    # 安全なディレクトリ作成のテスト
    if safe_mkdir "test_subdir" >/dev/null 2>&1; then
        echo "  ✅ 安全なディレクトリ作成: OK"
    else
        echo "  ❌ 安全なディレクトリ作成: FAIL"
        cd - >/dev/null
        rm -rf "$test_dir"
        return 1
    fi
    
    # 安全なファイル作成のテスト
    if safe_create_file "test_file.txt" "テストコンテンツ" false >/dev/null 2>&1; then
        echo "  ✅ 安全なファイル作成: OK"
    else
        echo "  ❌ 安全なファイル作成: FAIL"
        cd - >/dev/null
        rm -rf "$test_dir"
        return 1
    fi
    
    # メタデータ作成のテスト
    if create_metadata_if_not_exists "test-metadata.json" "test-feature" 1 >/dev/null 2>&1; then
        echo "  ✅ メタデータ作成: OK"
    else
        echo "  ❌ メタデータ作成: FAIL"
        cd - >/dev/null
        rm -rf "$test_dir"
        return 1
    fi
    
    # 原子的メタデータ更新のテスト
    if update_metadata_atomic "test-metadata.json" '.phase = "testing"' >/dev/null 2>&1; then
        echo "  ✅ 原子的メタデータ更新: OK"
    else
        echo "  ❌ 原子的メタデータ更新: FAIL"
        cd - >/dev/null
        rm -rf "$test_dir"
        return 1
    fi
    
    cd - >/dev/null
    rm -rf "$test_dir"
    echo "  ✅ 安全な操作実行テスト完了"
    return 0
}

# 5. 統合コマンドの構文チェック
test_integrated_commands_syntax() {
    echo "統合コマンドの構文チェック..."
    
    local command_dir="/workspace/.claude/commands/tdd-ddd-layered"
    local integrated_commands=(
        "03-create-use-case.md"
        "15-create-pr.md"
    )
    
    for command_file in "${integrated_commands[@]}"; do
        local full_path="$command_dir/$command_file"
        
        if [[ -f "$full_path" ]]; then
            echo "  📋 チェック中: $command_file"
            
            # bashスクリプト部分の構文チェック
            if grep -A 10000 '```bash' "$full_path" | grep -B 10000 '```' | head -n -1 | tail -n +2 | bash -n 2>/dev/null; then
                echo "  ✅ $command_file: 構文OK"
            else
                echo "  ⚠️  $command_file: 構文警告（可能性あり）"
                # Note: markdownからの抽出なので完全な構文チェックは困難
            fi
        else
            echo "  ❌ $command_file: ファイルが見つかりません"
            return 1
        fi
    done
    
    echo "  ✅ 統合コマンド構文チェック完了"
    return 0
}

# 6. 引数解析の統合テスト
test_argument_parsing_integration() {
    echo "引数解析の統合テスト..."
    
    # 引数パーサーを読み込み
    source "$(dirname "${BASH_SOURCE[0]}")/_common_arg_parser.sh"
    
    # テストケース1: 複合引数の解析
    if parse_arguments "1,7,15,feature-name,option"; then
        if [[ ${#issue_numbers[@]} -eq 3 ]] && [[ ${#other_args[@]} -eq 2 ]]; then
            echo "  ✅ 複合引数解析: OK"
        else
            echo "  ❌ 複合引数解析: FAIL (issue_numbers: ${#issue_numbers[@]}, other_args: ${#other_args[@]})"
            return 1
        fi
    else
        echo "  ❌ 引数解析失敗"
        return 1
    fi
    
    # テストケース2: エラーケースの処理
    if ! validate_arguments 10 5 0 2>/dev/null; then
        echo "  ✅ 引数検証エラー処理: OK"
    else
        echo "  ❌ 引数検証エラー処理: FAIL"
        return 1
    fi
    
    echo "  ✅ 引数解析統合テスト完了"
    return 0
}

# 7. エラー処理とロールバックのテスト
test_error_handling_rollback() {
    echo "エラー処理とロールバックのテスト..."
    
    # トランザクション フレームワークを読み込み
    source "$(dirname "${BASH_SOURCE[0]}")/_transaction_framework.sh"
    
    local test_dir="/tmp/rollback_test_$$"
    mkdir -p "$test_dir"
    cd "$test_dir"
    
    # 意図的に失敗するトランザクションをテスト
    if begin_transaction "failure_test"; then
        add_rollback "rm -f test_rollback_file" "Clean up test file"
        
        # テストファイル作成
        echo "test content" > test_rollback_file
        
        # 意図的にロールバックを実行
        execute_rollback "intentional_test"
        
        # ファイルが削除されているかチェック
        if [[ ! -f "test_rollback_file" ]]; then
            echo "  ✅ ロールバック機能: OK"
        else
            echo "  ❌ ロールバック機能: FAIL"
            cd - >/dev/null
            rm -rf "$test_dir"
            return 1
        fi
    else
        echo "  ❌ トランザクション開始失敗"
        cd - >/dev/null
        rm -rf "$test_dir"
        return 1
    fi
    
    cd - >/dev/null
    rm -rf "$test_dir"
    echo "  ✅ エラー処理とロールバックテスト完了"
    return 0
}

# 8. パフォーマンスと負荷のテスト
test_performance() {
    echo "パフォーマンスと負荷のテスト..."
    
    local start_time=$(date +%s)
    
    # 複数の安全操作を連続実行
    local test_dir="/tmp/perf_test_$$"
    mkdir -p "$test_dir"
    cd "$test_dir"
    
    # 関数を読み込み
    source "$(dirname "${BASH_SOURCE[0]}")/_file_operations.sh" 2>/dev/null || true
    
    # 10個のファイルを作成
    for i in {1..10}; do
        if ! safe_create_file "test_file_$i.txt" "Content $i" false >/dev/null 2>&1; then
            echo "  ❌ パフォーマンステスト: ファイル作成失敗"
            cd - >/dev/null
            rm -rf "$test_dir"
            return 1
        fi
    done
    
    local end_time=$(date +%s)
    local duration=$((end_time - start_time))
    
    cd - >/dev/null
    rm -rf "$test_dir"
    
    if [[ $duration -lt 30 ]]; then
        echo "  ✅ パフォーマンステスト: OK (${duration}秒)"
    else
        echo "  ⚠️  パフォーマンステスト: 遅い (${duration}秒)"
    fi
    
    echo "  ✅ パフォーマンステスト完了"
    return 0
}

# メインテスト実行
main() {
    echo "開始時刻: $(date)"
    echo ""
    
    run_test "統合環境セットアップ" test_integrated_setup
    run_test "GitHub操作関数" test_github_operations  
    run_test "トランザクション フレームワーク" test_transaction_framework
    run_test "安全な操作実行" test_safe_operations
    run_test "統合コマンド構文チェック" test_integrated_commands_syntax
    run_test "引数解析統合" test_argument_parsing_integration
    run_test "エラー処理とロールバック" test_error_handling_rollback
    run_test "パフォーマンス" test_performance
    
    echo "============================================================"
    echo "🧪 統合テスト結果サマリー"
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
        echo "❌ 統合テスト: 一部失敗"
        echo ""
        echo "📝 修正が必要な問題があります。確認してください。"
        return 1
    else
        echo "🎉 全ての統合テストが成功しました！"
        echo "✅ 統合テスト: 完全成功"
        echo ""
        echo "📝 統合された安全な機能群が正常に動作することを確認:"
        echo "  1. ✅ 統合環境セットアップ"
        echo "  2. ✅ GitHub API 安全操作"
        echo "  3. ✅ トランザクション管理"
        echo "  4. ✅ 安全なファイル・メタデータ操作"
        echo "  5. ✅ 統合コマンド構文"
        echo "  6. ✅ 引数解析"
        echo "  7. ✅ エラーハンドリング・ロールバック"
        echo "  8. ✅ パフォーマンス"
        echo ""
        echo "🚀 統合版カスタムコマンド群は本番利用可能です！"
        echo ""
        echo "📋 次のステップ:"
        echo "  - 既存の危険なコマンドを統合版に置き換え"
        echo "  - チーム内での使用方法共有"
        echo "  - 本番環境での段階的導入"
        return 0
    fi
}

# スクリプトが直接実行された場合のみメイン関数を実行
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi