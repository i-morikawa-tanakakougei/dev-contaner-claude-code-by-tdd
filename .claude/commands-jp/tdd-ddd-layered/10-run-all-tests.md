すべてのテストを実行し、包括的なテストレポートを生成します。安全性と監視機能が強化されています。

## メタデータ
- **前提条件**: すべての実装レイヤーが完了していること（ドメイン、アプリケーション、インフラストラクチャ、プレゼンテーション）
- **入力**: イシュー番号（必須）
- **出力**: 
  - 包括的なテスト実行レポート
  - カバレッジ分析とメトリクス
  - 更新された `docs/use_cases/issue-X-Y.json` メタデータ
- **依存関係**: pytest、カバレッジツール、すべての実装コード
- **実行タイミング**: 実装完了後、リファクタリング前

## 🎯 **TDD/DDD/レイヤードアーキテクチャプロセスコンテキスト**

**🔄 コアワークフロー**: ビジョン(00) → 構造(01) → スプリント(02) → ユースケース(03) → ドメイン(04) → テスト(05) → ドメイン(06) → アプリ(07) → インフラ(08) → UI(09) → テスト(10) → リファクタ(11) → 進化(12) → レビュー(13) → フィードバック(14) → PR(15) → ステータス(16)

**🎨 アーキテクチャ**: クリーンアーキテクチャ（ドメイン→アプリケーション→インフラストラクチャ→プレゼンテーション）  
**🧪 開発手法**: テスト駆動開発（RED→GREEN→REFACTOR）  
**🏗️ 設計手法**: ドメイン駆動設計（エンティティ、値オブジェクト、集約、リポジトリ）  
**📋 要件管理**: Given-When-Thenシナリオによる完全なトレーサビリティ  
**🔄 進化**: /evolve-scenariosコマンドによる継続的シナリオ進化

> 📖 **ドキュメント管理システム**: [README.md](./README.md)  
> 🗺️ **現在位置**: スプリント実行フェーズ - すべてのテスト実行（10/16）  
> 🎯 **フェーズ目的**: 包括的テストスイートの実行とレポート生成  
> ⬅️ **前段階**: 09-implement-presentation（プレゼンテーション層実装）  
> ➡️ **次段階**: 11-refactor（リファクタリング）
>
> **📋 3層アーキテクチャ操作**:
>
> - 🎯 **戦略**: `docs/use_cases/core/index.md`（コアシナリオの検証）
> - 📊 **戦術**: `docs/use_cases/index.md`（包括的テストステータスの更新）
> - 🔧 **実行**: `docs/use_cases/issue-X-Y.json`（詳細テスト結果の記録）

## 🧪 **テスト実行のみ**

**⚠️ 重要な注意事項:**
- **このステップはテスト実行のみ** - テストを実行してレポートを生成
- **実装は行わない** - 既存のテストの実行のみに焦点を当てる
- **品質検証** - すべてのテストを実行して実装を検証
- **レポート生成** - 包括的なテストレポートを作成

**実装後検証:**
1. `09-implement-presentation` ← すべての層が実装済み
2. `10-run-all-tests` ← **【現在地】テスト実行と検証**
3. `11-refactor` ← TDD REFACTOR（コード品質の改善）
4. `13-review-issue` ← 品質レビュー

**テストの実行のみ - 実装は行いません。**

## 📋 **包括的テスト実行タスクチェックリスト**

**徹底的なテスト実行と品質検証のためのチェックリストを使用してください:**

### 🔴 必須タスク

#### **🧪 ユニットテスト実行**
- [ ] **ドメインユニットテストの実行**: `uv run --frozen pytest tests/unit/domain/ -v` を実行
- [ ] **アプリケーションユニットテストの実行**: `uv run --frozen pytest tests/unit/application/ -v` を実行
- [ ] **テスト隔離の検証**: ユニットテストが外部依存関係なしで独立して実行されることを確認
- [ ] **ユニットテスト結果の分析**: 失敗を確認し、適切なテストカバレッジを保証

#### **🔗 統合テスト実行**
- [ ] **リポジトリ統合テストの実行**: `uv run --frozen pytest tests/integration/repositories/ -v` を実行
- [ ] **ユースケース統合テストの実行**: `uv run --frozen pytest tests/integration/use_cases/ -v` を実行
- [ ] **データベース相互作用のテスト**: 適切なデータベース統合とトランザクションを検証
- [ ] **統合テスト結果の分析**: 複雑な相互作用シナリオを確認

#### **📊 テストカバレッジ分析**
- [ ] **カバレッジレポートの生成**: `uv run --frozen pytest --cov=src --cov-report=html --cov-report=term` を実行
- [ ] **カバレッジメトリクスの分析**: ライン、ブランチ、関数のカバレッジを確認
- [ ] **カバレッジ目標の検証**: プロジェクト標準に適合することを確認（目標: 80%以上）
- [ ] **テスト実行メタデータの更新**: issue-X-Y.jsonに包括的なテスト結果を記録

### 🟡 推奨タスク

#### **🌐 エンドツーエンドテスト実行**
- [ ] **API E2Eテストの実行**: `uv run --frozen pytest tests/e2e/api/ -v` を実行
- [ ] **CLI E2Eテストの実行**: `uv run --frozen pytest tests/e2e/cli/ -v` を実行
- [ ] **完全なユーザーシナリオのテスト**: Given-When-Thenシナリオがエンドツーエンドで動作することを検証
- [ ] **認証フローのテスト**: 完全な認証・認可シナリオを検証
- [ ] **エラーハンドリングフローのテスト**: すべての層を通じた適切なエラー伝播を検証

#### **✅ シナリオ検証**
- [ ] **Given-When-Thenシナリオの検証**: すべての仕様シナリオがテストされていることを確認
- [ ] **受け入れ基準カバレッジの確認**: すべての受け入れ基準が検証されていることを確認
- [ ] **ビジネスルール実施のテスト**: ビジネスルールが適切にテストされていることを確認
- [ ] **エラーシナリオの検証**: 仕様からのエラーケースがカバーされていることを確認
- [ ] **仕様との相互参照**: テスト結果を元の要件と照合

#### **🚫 実装コンプライアンス**
- [ ] **新規実装がないことの検証**: このフェーズがテストのみを実行し、新しいコードがないことを確認
- [ ] **アーキテクチャ整合性の確認**: 層境界が維持されていることを検証
- [ ] **依存関係方向の検証**: クリーンアーキテクチャの原則が保持されていることを確認
- [ ] **テストのみの変更の確認**: 変更はテスト修正のみで、実装ではないことを確認

### 🟢 オプションタスク

#### **🔧 テスト前品質検証**
- [ ] **最終ruffリンティングの実行**: `uv run --frozen ruff check src/ --fix` を実行
- [ ] **最終ruffフォーマッティングの実行**: `uv run --frozen ruff format src/` を実行
- [ ] **最終型チェックの実行**: `uv run --frozen pyright src/` を実行
- [ ] **残存問題の修正**: リンティング、フォーマッティング、型エラーに対処
- [ ] **クリーンなコードベースの検証**: すべての品質ツールがエラーなしでパスすることを確認

#### **🚀 パフォーマンステスト**
- [ ] **パフォーマンスベンチマークの実行**: 利用可能な場合はパフォーマンステストを実行
- [ ] **応答時間の測定**: APIエンドポイントの応答時間を確認
- [ ] **データベースクエリパフォーマンスのテスト**: 遅いクエリと最適化の必要性を分析
- [ ] **メモリ使用量分析**: テスト実行中のメモリ消費量を監視
- [ ] **パフォーマンスボトルネックの特定**: 最適化のためのパフォーマンス問題を文書化

#### **🔍 テスト品質評価**
- [ ] **テスト失敗パターンの確認**: 一般的な失敗原因と不安定なテストを分析
- [ ] **テストアサーションの検証**: テストがビジネス要件を適切に検証していることを確認
- [ ] **テスト保守性の確認**: テストコードの品質と可読性を評価
- [ ] **テストデータ隔離の検証**: テストが互いに干渉しないことを確認
- [ ] **テストドキュメントの評価**: テストの説明とドキュメントの品質を確認

#### **📈 包括的レポーティング**
- [ ] **テスト実行レポートの生成**: すべてのテスト実行の詳細レポートを作成
- [ ] **テストメトリクスの文書化**: 合格/不合格率、カバレッジ、パフォーマンスメトリクスを記録
- [ ] **品質ダッシュボードの作成**: システム全体の品質と健全性を要約
- [ ] **改善領域の特定**: 注意やリファクタリングが必要な領域を文書化
- [ ] **ステークホルダーレポートの生成**: ビジネスフレンドリーな品質要約を作成
- [ ] **テストパフォーマンスの確認**: パフォーマンス問題のためにテスト実行時間を監視
- [ ] **外部サービス統合のテスト**: サードパーティサービス接続を検証
- [ ] **カバレッジギャップの特定**: テストされていないコードパスと重要な欠落テストを発見
- [ ] **カバレッジドキュメントの生成**: ステークホルダー向けカバレッジレポートを作成
- [ ] **最終品質レポートの生成**: 完全な品質評価ドキュメントを作成
- [ ] **品質ゲートの検証**: すべての品質閾値が満たされていることを確認
- [ ] **リファクタリング推奨事項の準備**: コード改善機会を特定
- [ ] **システム準備状況の文書化**: リファクタリングとレビューフェーズへの準備状況を評価

**💡 プロのヒント**: このフェーズは実装全体を検証します - 失敗があった場合は、リファクタリングに進む前に対処する必要がある問題を示しています！

## 🛡️ **統合版の主な改善点**

### **✅ 解決された問題**

- **テスト環境不整合**: 安全な環境セットアップとクリーンアップ
- **並列テスト失敗**: テスト隔離と依存関係管理
- **カバレッジ計算エラー**: 正確な測定と閾値チェック
- **パフォーマンス劣化検出**: 継続的な性能監視
- **テスト結果の追跡漏れ**: 包括的なログ記録と履歴管理

### **🆕 新機能**

1. **🔄 テスト環境管理**: 隔離されたテスト実行と環境復旧
2. **📊 包括的メトリクス**: カバレッジ・性能・品質の統合監視
3. **🛡️ 継続的品質保証**: 自動化された品質ゲート
4. **🔍 詳細分析レポート**: テスト結果の可視化と傾向分析
5. **📈 パフォーマンス追跡**: ベースライン比較と劣化検出

## よくあるエラーと解決策

### ❌ エラーケース1: 実装不足によるテスト失敗
**原因**: テスト実行前に実装レイヤーが完了していない  
**解決策**: すべての層を完了させる: ドメイン → アプリケーション → インフラストラクチャ → プレゼンテーション

### ❌ エラーケース2: 低いテストカバレッジ
**原因**: 実装機能に対するテストが不足  
**解決策**: カバーされていないコードパスとエッジケースのテストを追加

### ❌ エラーケース3: 統合テストの失敗
**原因**: 層統合の問題や設定の問題  
**解決策**: 依存性注入と設定セットアップを検証

## 実行例

### ✅ 成功例
```bash
$ /run-all-tests 15
🧪 Issues: #15 の全テスト実行を開始します
🔍 実装完了状態確認中...
✅ 全層の実装が完了しています
🏃 テストスイート実行中...
======= 45 passed, 0 failed =======
Coverage: 92%
✅ 全テストが成功しました
🎉 テスト実行完了!
```

### ❌ 失敗例と修正
```bash
$ /run-all-tests 15
❌ 3 tests failed, 42 passed
💡 失敗したテストを修正してください
# 修正: 失敗したテストに対処してから再実行
$ /run-all-tests 15
```

## タスクの詳細

## 1. **安全な環境のセットアップと引数解析**

```bash
# 🔧 自動引数解析と検証を含むすべての安全操作関数を読み込み
source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "10-run-all-tests" "$ARGUMENTS"

# 引数はセットアップスクリプトによって既に解析・検証済み
# このコマンド固有の追加検証
if [[ ${#issue_numbers[@]} -eq 0 ]]; then
    echo "エラー: 最低1つのイシュー番号が必要です"
    show_usage_example "run-all-tests" "1" "単一イシューのテスト実行"
    show_usage_example "run-all-tests" "1,7" "複数イシューのテスト実行"
    show_usage_example "run-all-tests" "1,integration" "イシュー + テスト種別指定"
    exit 1
fi

# ログ初期化
initialize_operation_logging "run_all_tests"
```

## 2. **トランザクション管理と環境準備**

```bash
# テスト実行のトランザクション開始
transaction_id="run_all_tests_$(date +%s)_$(echo "${issue_numbers[*]}" | tr ' ' '_')"
begin_transaction "$transaction_id"

# テスト環境復旧のセットアップ
add_rollback_handler "echo '🔄 テスト環境をリストア中...'"
add_rollback_handler "rm -rf .coverage* .pytest_cache htmlcov .ruff_cache .pyright_cache 2>/dev/null || true"
add_rollback_handler "git checkout . 2>/dev/null || true"

# メタデータファイルの発見と前提条件の検証
issue_list=$(IFS=-; echo "${issue_numbers[*]}")
if [[ ${#other_args[@]} -gt 0 ]]; then
    test_scope="${other_args[0]}"
    # テストタイプでない場合はフィーチャー名を抽出
    if [[ "$test_scope" =~ ^(unit|integration|e2e|all)$ ]]; then
        feature_name=$(find docs/use_cases -name "issue-${issue_list}-*.md" | head -1 | sed 's/.*issue-[0-9-]*-\(.*\)\.md$/\1/')
    else
        feature_name="$test_scope"
        test_scope="all"
    fi
else
    feature_name=$(find docs/use_cases -name "issue-${issue_list}-*.md" | head -1 | sed 's/.*issue-[0-9-]*-\(.*\)\.md$/\1/')
    test_scope="all"
fi

if [[ -z "$feature_name" ]]; then
    echo "❌ エラー: フィーチャー名を特定できませんでした"
    echo "💡 使用方法: /run-all-tests $issue_list,<feature-name|test-scope>"
    execute_rollback
    exit 1
fi

metadata_file="docs/use_cases/issue-${issue_list}-${feature_name}.json"
spec_file="docs/use_cases/issue-${issue_list}-${feature_name}.md"

# メタデータファイルと前提条件の検証
if [[ ! -f "$metadata_file" ]]; then
    echo "❌ エラー: メタデータファイルが見つかりません: $metadata_file"
    execute_rollback
    exit 1
fi

# プレゼンテーション層が実装されていることを確認
validate_phase_completion "$metadata_file" "presentation_implementation"

echo "✅ 前提条件チェック完了"
echo "📋 テストスコープ: $test_scope"
echo "🎯 フィーチャー: $feature_name"
```

## 3. **安全なテスト環境準備**

```bash
# クリーンなテスト環境の準備
echo "🧹 テスト環境を準備中..."

# 現在の状態をバックアップ
backup_dir="$(mktemp -d)"
add_rollback_handler "rm -rf '$backup_dir'"

# テストアーティファクトの安全なクリーンアップ
safe_clean_test_environment() {
    local cleanup_items=(
        ".coverage*"
        ".pytest_cache"
        "htmlcov"
        ".ruff_cache"
        ".pyright_cache"
        "tests/__pycache__"
        "src/**/__pycache__"
    )

    for item in "${cleanup_items[@]}"; do
        find . -name "$item" -type d -exec rm -rf {} + 2>/dev/null || true
        find . -name "$item" -type f -delete 2>/dev/null || true
    done

    # pytest キャッシュをクリア
    uv run --frozen pytest --cache-clear >/dev/null 2>&1 || true
}

safe_clean_test_environment

# テスト結果ディレクトリの作成
test_results_dir="docs/test_results/issue-${issue_list}-${feature_name}-$(date +%Y%m%d_%H%M%S)"
mkdir -p "$test_results_dir"
add_rollback_handler "rm -rf '$test_results_dir'"

echo "📁 テスト結果ディレクトリ: $test_results_dir"
echo "✅ テスト環境準備完了"
```

## 4. **包括的テスト実行**

```bash
# スコープに基づく包括的テストスイートの実行
echo "🧪 包括的テストスイートを実行中..."

test_summary_file="$test_results_dir/test_summary.json"
test_log_file="$test_results_dir/test_execution.log"

# テストサマリーの初期化
cat > "$test_summary_file" << EOF
{
  "execution_start": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "issues": [$(IFS=','; echo "\"${issue_numbers[*]}\"")],
  "feature": "$feature_name",
  "scope": "$test_scope",
  "results": {}
}
EOF

# 詳細ログ付きテストを安全に実行する関数
run_test_suite() {
    local test_type="$1"
    local test_path="$2"
    local test_args="${3:-}"

    echo "🔍 実行中: ${test_type} テスト..."

    local start_time=$(date +%s)
    local result_file="$test_results_dir/${test_type}_results.json"
    local output_file="$test_results_dir/${test_type}_output.txt"

    # 包括的な出力キャプチャ付きテスト実行
    local exit_code=0
    {
        echo "=== ${test_type} テスト実行開始 $(date) ==="
        echo "パス: $test_path"
        echo "引数: $test_args"
        echo ""

        if [[ -d "$test_path" && $(find "$test_path" -name "*.py" -not -name "__*" | wc -l) -gt 0 ]]; then
            # 適切なプラグイン読み込みで実行
            PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest "$test_path" \
                -v --tb=short --json-report --json-report-file="$result_file" \
                $test_args || exit_code=$?
        else
            echo "⚠️ 警告: テストファイルが見つかりません: $test_path"
            echo '{"tests": [], "summary": {"total": 0, "passed": 0, "failed": 0}}' > "$result_file"
        fi

        echo ""
        echo "=== ${test_type} テスト実行完了 $(date) ==="
    } 2>&1 | tee "$output_file"

    local end_time=$(date +%s)
    local duration=$((end_time - start_time))

    # 結果を解析してサマリーを更新
    if [[ -f "$result_file" ]]; then
        local total_tests=$(jq -r '.summary.total // 0' "$result_file")
        local passed_tests=$(jq -r '.summary.passed // 0' "$result_file")
        local failed_tests=$(jq -r '.summary.failed // 0' "$result_file")
        local skipped_tests=$(jq -r '.summary.skipped // 0' "$result_file")

        # テストサマリーを更新
        jq --arg type "$test_type" \
           --argjson exit_code "$exit_code" \
           --argjson duration "$duration" \
           --argjson total "$total_tests" \
           --argjson passed "$passed_tests" \
           --argjson failed "$failed_tests" \
           --argjson skipped "$skipped_tests" \
           '.results[$type] = {
               "exit_code": $exit_code,
               "duration": $duration,
               "total": $total,
               "passed": $passed,
               "failed": $failed,
               "skipped": $skipped,
               "success": ($exit_code == 0)
           }' "$test_summary_file" > "${test_summary_file}.tmp" && mv "${test_summary_file}.tmp" "$test_summary_file"

        echo "📊 ${test_type}: ${passed_tests}/${total_tests} 成功 (${duration}s)"
    else
        echo "⚠️ 結果ファイルが生成されませんでした: $result_file"
    fi

    return $exit_code
}

# スコープに基づくテストスイートの実行
test_execution_success=true

if [[ "$test_scope" == "all" || "$test_scope" == "unit" ]]; then
    if ! run_test_suite "unit" "tests/unit" "--maxfail=10"; then
        test_execution_success=false
        echo "❌ ユニットテストが失敗しました"
    fi
fi

if [[ "$test_scope" == "all" || "$test_scope" == "integration" ]]; then
    if ! run_test_suite "integration" "tests/integration" "--maxfail=5"; then
        test_execution_success=false
        echo "❌ 統合テストが失敗しました"
    fi
fi

if [[ "$test_scope" == "all" || "$test_scope" == "e2e" ]]; then
    if ! run_test_suite "e2e" "tests/e2e" "--maxfail=3"; then
        test_execution_success=false
        echo "❌ E2Eテストが失敗しました"
    fi
fi

echo "✅ テスト実行フェーズ完了"
```

## 5. **カバレッジ分析と品質メトリクス**

```bash
# 包括的カバレッジレポートの生成
echo "📊 カバレッジ分析を実行中..."

coverage_file="$test_results_dir/coverage_report.json"
coverage_html_dir="$test_results_dir/coverage_html"

if [[ "$test_scope" == "all" ]]; then
    # カバレッジ分析の実行
    echo "📈 詳細カバレッジ分析中..."

    coverage_exit_code=0
    PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest \
        --cov=src \
        --cov-report=html:"$coverage_html_dir" \
        --cov-report=json:"$coverage_file" \
        --cov-report=term-missing \
        --cov-fail-under=70 \
        tests/ \
        > "$test_results_dir/coverage_output.txt" 2>&1 || coverage_exit_code=$?

    if [[ -f "$coverage_file" ]]; then
        overall_coverage=$(jq -r '.totals.percent_covered_display' "$coverage_file")
        echo "📊 全体カバレッジ: ${overall_coverage}"

        # モジュール別カバレッジの抽出
        jq -r '.files | to_entries[] | "\(.key): \(.value.summary.percent_covered_display)"' "$coverage_file" > "$test_results_dir/module_coverage.txt"
    else
        echo "⚠️ カバレッジファイルが生成されませんでした"
        overall_coverage="N/A"
    fi
else
    echo "ℹ️ スコープ限定実行のためカバレッジ分析をスキップ"
    overall_coverage="N/A"
fi

# 静的解析の実行
echo "🔍 静的解析を実行中..."

# Ruff 解析
ruff_file="$test_results_dir/ruff_analysis.txt"
echo "🧹 Ruff 解析中..."
{
    echo "=== RUFF ANALYSIS ==="
    uv run --frozen ruff check . --statistics --output-format=json > "$test_results_dir/ruff_results.json" || true
    uv run --frozen ruff check . --show-source --statistics || true
} > "$ruff_file" 2>&1

# 型チェック
pyright_file="$test_results_dir/pyright_analysis.txt"
echo "📝 Pyright 型チェック中..."
{
    echo "=== PYRIGHT TYPE CHECKING ==="
    uv run --frozen pyright --outputjson > "$test_results_dir/pyright_results.json" || true
    uv run --frozen pyright --stats || true
} > "$pyright_file" 2>&1

echo "✅ 品質メトリクス収集完了"
```

## 6. **パフォーマンス分析とベンチマーク**

```bash
# パフォーマンステスト（利用可能な場合）
echo "⚡ パフォーマンス分析中..."

performance_file="$test_results_dir/performance_results.json"

if [[ -d "tests/performance" ]] && [[ $(find tests/performance -name "*.py" -not -name "__*" | wc -l) -gt 0 ]]; then
    echo "🏃 パフォーマンステスト実行中..."

    PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/performance/ \
        --benchmark-only \
        --benchmark-json="$performance_file" \
        > "$test_results_dir/performance_output.txt" 2>&1 || true

    if [[ -f "$performance_file" ]]; then
        echo "📊 パフォーマンス結果記録完了"
    fi
else
    echo "ℹ️ パフォーマンステストが見つかりません"
    echo '{"benchmarks": [], "info": "No performance tests found"}' > "$performance_file"
fi

# セキュリティ分析（bandit が利用可能な場合）
security_file="$test_results_dir/security_analysis.json"

if command -v uv >/dev/null && uv run bandit --version >/dev/null 2>&1; then
    echo "🔒 セキュリティ分析中..."

    uv run bandit -r src/ -f json -o "$security_file" || true

    if [[ -f "$security_file" ]]; then
        security_issues=$(jq '.results | length' "$security_file" 2>/dev/null || echo "0")
        echo "🛡️ セキュリティ問題: ${security_issues} 件"
    fi
else
    echo "ℹ️ Bandit セキュリティスキャナーが利用できません"
    echo '{"results": [], "info": "Bandit not available"}' > "$security_file"
fi

echo "✅ パフォーマンス・セキュリティ分析完了"
```

## 7. **包括的テストレポート生成**

```bash
# 詳細テストレポートの生成
echo "📋 包括的テストレポートを生成中..."

test_report_file="$test_results_dir/comprehensive_test_report.md"

# 全体テスト統計の計算
total_tests=$(jq -r '[.results[] | .total] | add // 0' "$test_summary_file")
total_passed=$(jq -r '[.results[] | .passed] | add // 0' "$test_summary_file")
total_failed=$(jq -r '[.results[] | .failed] | add // 0' "$test_summary_file")
total_skipped=$(jq -r '[.results[] | .skipped] | add // 0' "$test_summary_file")
total_duration=$(jq -r '[.results[] | .duration] | add // 0' "$test_summary_file")

# 個別テストタイプ結果の抽出
unit_results=$(jq -r '.results.unit // {"total":0,"passed":0,"failed":0,"duration":0}' "$test_summary_file")
integration_results=$(jq -r '.results.integration // {"total":0,"passed":0,"failed":0,"duration":0}' "$test_summary_file")
e2e_results=$(jq -r '.results.e2e // {"total":0,"passed":0,"failed":0,"duration":0}' "$test_summary_file")

# 品質メトリクスの取得
ruff_issues=$(jq '.[] | length' "$test_results_dir/ruff_results.json" 2>/dev/null || echo "0")
pyright_errors=$(jq '.summary.errorCount // 0' "$test_results_dir/pyright_results.json" 2>/dev/null || echo "0")

cat > "$test_report_file" << EOF
# 包括的テストレポート: ${feature_name}

## 概要
- **Issues**: #$(IFS=' #'; echo "${issue_numbers[*]}")
- **Feature**: ${feature_name}
- **Test Scope**: ${test_scope}
- **実行日時**: $(date)
- **実行時間**: ${total_duration} 秒

## 🎯 テスト結果サマリー

### 全体統計
- **総テスト数**: ${total_tests}
- **成功**: ${total_passed} ✅
- **失敗**: ${total_failed} ❌
- **スキップ**: ${total_skipped} ⏭️
- **成功率**: $(( total_tests > 0 ? (total_passed * 100) / total_tests : 0 ))%

### 📦 ユニットテスト
$(echo "$unit_results" | jq -r '"- 実行数: " + (.total|tostring) + "\n- 成功: " + (.passed|tostring) + "\n- 失敗: " + (.failed|tostring) + "\n- 実行時間: " + (.duration|tostring) + " 秒"')

### 🔗 統合テスト
$(echo "$integration_results" | jq -r '"- 実行数: " + (.total|tostring) + "\n- 成功: " + (.passed|tostring) + "\n- 失敗: " + (.failed|tostring) + "\n- 実行時間: " + (.duration|tostring) + " 秒"')

### 🌐 E2E テスト
$(echo "$e2e_results" | jq -r '"- 実行数: " + (.total|tostring) + "\n- 成功: " + (.passed|tostring) + "\n- 失敗: " + (.failed|tostring) + "\n- 実行時間: " + (.duration|tostring) + " 秒"')

## 📊 カバレッジ

- **全体カバレッジ**: ${overall_coverage}
EOF

# モジュール固有のカバレッジを利用可能な場合は追加
if [[ -f "$test_results_dir/module_coverage.txt" ]]; then
    echo "- **モジュール別カバレッジ**:" >> "$test_report_file"
    while IFS= read -r line; do
        echo "  - $line" >> "$test_report_file"
    done < "$test_results_dir/module_coverage.txt"
fi

cat >> "$test_report_file" << EOF

## 🔍 品質メトリクス

- **Ruff 問題**: ${ruff_issues} 件
- **Pyright エラー**: ${pyright_errors} 件
- **セキュリティ問題**: $(jq '.results | length' "$security_file" 2>/dev/null || echo "N/A") 件

## 📁 詳細ファイル

- **テスト結果ディレクトリ**: \`${test_results_dir}\`
- **カバレッジHTMLレポート**: \`${coverage_html_dir}/index.html\`
- **詳細ログ**: \`${test_log_file}\`

## ✅ 推奨事項

EOF

# 結果に基づく推奨事項の追加
if [[ "$total_failed" -gt 0 ]]; then
    echo "- ❌ **失敗したテストを修正**: ${total_failed} 件のテストが失敗しています" >> "$test_report_file"
fi

if [[ "$overall_coverage" != "N/A" ]] && [[ $(echo "$overall_coverage" | sed 's/%//') -lt 80 ]]; then
    echo "- 📊 **カバレッジ改善**: 現在 ${overall_coverage}、目標 80% 以上" >> "$test_report_file"
fi

if [[ "$ruff_issues" -gt 0 ]]; then
    echo "- 🧹 **コード品質改善**: ${ruff_issues} 件の Ruff 問題を修正" >> "$test_report_file"
fi

if [[ "$pyright_errors" -gt 0 ]]; then
    echo "- 📝 **型エラー修正**: ${pyright_errors} 件の型チェックエラーを修正" >> "$test_report_file"
fi

if [[ "$total_failed" -eq 0 && "$overall_coverage" != "N/A" ]] && [[ $(echo "$overall_coverage" | sed 's/%//') -ge 80 ]]; then
    echo "- 🎉 **全て良好**: すべてのテストが成功し、カバレッジも基準を満たしています" >> "$test_report_file"
fi

echo "✅ テストレポート生成完了: $test_report_file"
```

## 8. **アトミックメタデータ更新**

```bash
# 包括的テスト結果でメタデータを更新
echo "📊 メタデータを更新中..."

if [[ -f "$metadata_file" ]]; then
    # 全体的なテスト成功の判定
    all_tests_passed=$([[ "$test_execution_success" == "true" && "$total_failed" -eq 0 ]] && echo "true" || echo "false")

    # メタデータのアトミック更新
    update_metadata_atomic "$metadata_file" "
        .phases.tests.passed = $all_tests_passed |
        .phases.tests.passed_at = \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\" |
        .phases.tests.total_tests = $total_tests |
        .phases.tests.passed_tests = $total_passed |
        .phases.tests.failed_tests = $total_failed |
        .phases.tests.skipped_tests = $total_skipped |
        .phases.tests.coverage = \"$overall_coverage\" |
        .phases.tests.test_report = \"$test_report_file\" |
        .phases.tests.results_directory = \"$test_results_dir\" |
        .updated_at = \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\" |
        .phase = \"all_tests_completed\"
    "

    echo "✅ メタデータ更新完了"
else
    echo "⚠️ 警告: メタデータファイルが見つかりません: $metadata_file"
fi
```

## 9. **ユースケースインデックス更新**

```bash
# 包括的テストステータスでユースケースインデックスを更新
echo "📋 ユースケースインデックスを更新中..."

if [[ -f "docs/use_cases/index.md" ]]; then
    feature_line="- \\[${feature_name}\\]"

    # テストファイル数のカウント
    unit_test_count=$(find tests/unit/ -name "*.py" -not -name "__*" 2>/dev/null | wc -l)
    integration_test_count=$(find tests/integration/ -name "*.py" -not -name "__*" 2>/dev/null | wc -l)
    e2e_test_count=$(find tests/e2e/ -name "*.py" -not -name "__*" 2>/dev/null | wc -l)

    # ステータスインジケーターの作成
    test_status="✅"
    if [[ "$total_failed" -gt 0 ]]; then
        test_status="❌"
    elif [[ "$total_tests" -eq 0 ]]; then
        test_status="⚠️"
    fi

    # 包括的テスト情報で更新
    sed -i "s|${feature_line}.*|${feature_line}($(basename ${spec_file})) - Issues: #$(IFS=' #'; echo \"${issue_numbers[*]}\") (Phase: all_tests_completed, Unit: ${unit_test_count}, Integration: ${integration_test_count}, E2E: ${e2e_test_count}, Coverage: ${overall_coverage}, Status: ${test_status})|" docs/use_cases/index.md

    echo "✅ インデックス更新完了"
else
    echo "⚠️ 警告: Use case index not found"
fi
```

## 10. **GitHub イシュー更新**

```bash
# テスト結果でGitHub イシューを更新
echo "📢 GitHub イシューを更新中..."

# GitHub用詳細テストサマリーの作成
github_summary="🧪 **包括的テスト実行完了**

📊 **テスト結果サマリー**:
- 総テスト数: ${total_tests}
- 成功: ${total_passed} ✅
- 失敗: ${total_failed} ❌
- スキップ: ${total_skipped} ⏭️
- 成功率: $(( total_tests > 0 ? (total_passed * 100) / total_tests : 0 ))%

📈 **カバレッジ**: ${overall_coverage}

🔍 **品質メトリクス**:
- Ruff 問題: ${ruff_issues} 件
- Pyright エラー: ${pyright_errors} 件

📁 **詳細レポート**: \`${test_report_file}\`
📂 **結果ディレクトリ**: \`${test_results_dir}\`"

# パフォーマンス情報を利用可能な場合は追加
if [[ -f "$performance_file" ]]; then
    github_summary="${github_summary}

⚡ **パフォーマンス**: 結果は \`${performance_file}\` を参照"
fi

# セキュリティ情報を利用可能な場合は追加
if [[ -f "$security_file" ]]; then
    security_count=$(jq '.results | length' "$security_file" 2>/dev/null || echo "0")
    github_summary="${github_summary}

🔒 **セキュリティ**: ${security_count} 件の問題を検出"
fi

for issue_num in "${issue_numbers[@]}"; do
    if safe_gh_command "issue" "comment" "$issue_num" --body "$github_summary"; then
        echo "✅ Issue #$issue_num にテスト結果を報告"
    else
        echo "⚠️ 警告: Issue #$issue_num への報告に失敗"
    fi
done
```

## 11. **トランザクションコミットと最終クリーンアップ**

```bash
# テスト実行結果をコミット
echo "💾 テスト実行結果をコミット中..."

# トランザクションコミット
commit_transaction

# 包括的サマリーの表示
echo ""
echo "🎉 包括的テスト実行完了!"
echo ""
echo "📊 **テスト実行サマリー**:"
echo "   - Issues: #$(IFS=' #'; echo "${issue_numbers[*]}")"
echo "   - Feature: ${feature_name}"
echo "   - Scope: ${test_scope}"
echo "   - Total Tests: ${total_tests}"
echo "   - Success Rate: $(( total_tests > 0 ? (total_passed * 100) / total_tests : 0 ))%"
echo "   - Coverage: ${overall_coverage}"
echo "   - Duration: ${total_duration}s"
echo ""
echo "📋 **結果詳細**:"
echo "   - ユニットテスト: $(echo "$unit_results" | jq -r '"\(.passed)/\(.total)"')"
echo "   - 統合テスト: $(echo "$integration_results" | jq -r '"\(.passed)/\(.total)"')"
echo "   - E2Eテスト: $(echo "$e2e_results" | jq -r '"\(.passed)/\(.total)"')"
echo ""
echo "🔍 **品質指標**:"
echo "   - Ruff問題: ${ruff_issues} 件"
echo "   - 型エラー: ${pyright_errors} 件"
echo ""
echo "📁 **生成ファイル**:"
echo "   - 📋 テストレポート: ${test_report_file}"
echo "   - 📂 結果ディレクトリ: ${test_results_dir}"
if [[ -f "$coverage_html_dir/index.html" ]]; then
    echo "   - 🌐 カバレッジHTML: ${coverage_html_dir}/index.html"
fi
echo ""
echo "🔍 **次のステップ**:"

if [[ "$total_failed" -gt 0 ]]; then
    echo "   - ❌ 失敗したテストを修正してから次に進んでください"
    echo "   - 💡 詳細は ${test_results_dir} の各ログファイルを確認"
elif [[ "$all_tests_passed" == "true" ]]; then
    echo "   - ✅ 全テスト成功! リファクタリング: /refactor ${issue_list}"
    echo "   - 📊 状況確認: /use-case-status ${issue_list}"
    echo "   - 📝 レビュー開始: /review-issue ${issue_list}"
else
    echo "   - ⚠️ 一部テストに問題があります。結果を確認してください"
fi

echo ""
echo "✅ 包括的テスト実行が正常に完了しました"
```

## 重要な注意事項

### **安全性保証**

- テスト実行前の環境クリーンアップとバックアップ
- 失敗時の安全な状態復旧
- メタデータの原子的更新
- テスト結果の完全な追跡可能性

### **包括性**

- ユニット・統合・E2E の全テストカテゴリ対応
- カバレッジ・品質・セキュリティ・パフォーマンス分析
- 詳細レポート生成と履歴管理
- GitHub との完全連携

### **信頼性**

- テスト環境の隔離と再現性確保
- エラー処理と適切なログ記録
- 品質ゲートと継続的監視
- チーム協力のための可視化

**統合版テスト実行コマンドにより、確実で包括的な品質保証が実現されます！**

## 🚨 CLAUDE CODE用必須: シナリオ進化チェック

テスト実行中にテスト失敗・新要件・エッジケース発見時は
作業を中断して `/evolve-scenarios <feature-name>` を実行すること
CRITICAL: テスト結果は新シナリオ発見の重要な情報源です