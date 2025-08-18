Run all tests and generate comprehensive test report with enhanced safety and monitoring capabilities.

## Metadata
- **Prerequisites**: All implementation layers completed (domain, application, infrastructure, presentation)
- **Input**: Issue number(s) (required)
- **Output**: 
  - Comprehensive test execution report
  - Coverage analysis and metrics
  - Updated `docs/use_cases/issue-X-Y.json` metadata
- **Dependencies**: pytest, coverage tools, all implementation code
- **Execution Timing**: After implementation completion, before refactoring

## 🎯 **TDD/DDD/LAYERED PROCESS CONTEXT**

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Sprint Execution Phase - Run All Tests (10/16)  
> 🎯 **Phase Purpose**: Execute comprehensive test suite and generate reports  
> ⬅️ **Previous Stage**: 09-implement-presentation (Presentation Layer Implementation)  
> ➡️ **Next Stage**: 11-refactor (Refactoring)
>
> **📋 3-Layer Architecture Operations**:
>
> - 🎯 **Strategic**: `docs/use_cases/core/index.md` (Validate core scenarios)
> - 📊 **Tactical**: `docs/use_cases/index.md` (Update comprehensive test status)
> - 🔧 **Execution**: `docs/use_cases/issue-X-Y.json` (Record detailed test results)

## 🧪 **TEST EXECUTION ONLY**

**⚠️ Important Notice:**
- **This step is TEST EXECUTION ONLY** - Run tests and generate reports
- **NO IMPLEMENTATION** - Focus only on running existing tests  
- **Quality verification** - Execute all tests and validate implementation
- **Report generation** - Create comprehensive test reports

**Post-Implementation Verification:**
1. `09-implement-presentation` ← All layers implemented
2. `10-run-all-tests` ← **【YOU ARE HERE】Test execution and verification**
3. `11-refactor` ← TDD REFACTOR (improve code quality)
4. `13-review-issue` ← Quality review

**EXECUTE TESTS ONLY - NO IMPLEMENTATION.**

## 📋 **COMPREHENSIVE TEST EXECUTION TASK CHECKLIST**

**Use this checklist for thorough test execution and quality verification:**

### 🔴 Required Tasks

#### **🧪 Unit Tests Execution**
- [ ] **Run domain unit tests**: Execute `uv run --frozen pytest tests/unit/domain/ -v`
- [ ] **Run application unit tests**: Execute `uv run --frozen pytest tests/unit/application/ -v`
- [ ] **Verify test isolation**: Ensure unit tests run independently without external dependencies
- [ ] **Analyze unit test results**: Review failures and ensure proper test coverage

#### **🔗 Integration Tests Execution**
- [ ] **Run repository integration tests**: Execute `uv run --frozen pytest tests/integration/repositories/ -v`
- [ ] **Run use case integration tests**: Execute `uv run --frozen pytest tests/integration/use_cases/ -v`
- [ ] **Test database interactions**: Verify proper database integration and transactions
- [ ] **Analyze integration test results**: Review complex interaction scenarios

#### **📊 Test Coverage Analysis**
- [ ] **Generate coverage report**: Execute `uv run --frozen pytest --cov=src --cov-report=html --cov-report=term`
- [ ] **Analyze coverage metrics**: Review line, branch, and function coverage
- [ ] **Validate coverage targets**: Ensure coverage meets project standards (target: 80%+)
- [ ] **Update test execution metadata**: Record comprehensive test results in issue-X-Y.json

### 🟡 Recommended Tasks

#### **🌐 End-to-End Tests Execution**
- [ ] **Run API e2e tests**: Execute `uv run --frozen pytest tests/e2e/api/ -v`
- [ ] **Run CLI e2e tests**: Execute `uv run --frozen pytest tests/e2e/cli/ -v`
- [ ] **Test complete user scenarios**: Verify Given-When-Then scenarios work end-to-end
- [ ] **Test authentication flows**: Validate complete auth/authz scenarios
- [ ] **Test error handling flows**: Verify proper error propagation through all layers

#### **✅ Scenario Validation**
- [ ] **Validate Given-When-Then scenarios**: Ensure all specification scenarios are tested
- [ ] **Check acceptance criteria coverage**: Verify all acceptance criteria are validated
- [ ] **Test business rule enforcement**: Confirm business rules are properly tested
- [ ] **Validate error scenarios**: Ensure error cases from specifications are covered
- [ ] **Cross-reference with specifications**: Match test results against original requirements

#### **🚫 Implementation Compliance**
- [ ] **Verify no new implementation**: Confirm this phase only executed tests, no new code
- [ ] **Check architecture integrity**: Validate layer boundaries remain intact
- [ ] **Verify dependency directions**: Ensure Clean Architecture principles maintained
- [ ] **Confirm test-only changes**: Any changes should only be test fixes, not implementation

### 🟢 Optional Tasks

#### **🔧 Pre-Test Quality Validation**
- [ ] **Run final ruff linting**: Execute `uv run --frozen ruff check src/ --fix`
- [ ] **Run final ruff formatting**: Execute `uv run --frozen ruff format src/`
- [ ] **Run final type checking**: Execute `uv run --frozen pyright src/`
- [ ] **Fix any remaining issues**: Address any linting, formatting, or type errors
- [ ] **Verify clean codebase**: Ensure all quality tools pass without errors

#### **🚀 Performance Testing**
- [ ] **Run performance benchmarks**: Execute performance tests if available
- [ ] **Measure response times**: Check API endpoint response times
- [ ] **Test database query performance**: Analyze slow queries and optimization needs
- [ ] **Memory usage analysis**: Monitor memory consumption during test execution
- [ ] **Identify performance bottlenecks**: Document performance issues for optimization

#### **🔍 Test Quality Assessment**
- [ ] **Review test failure patterns**: Analyze common failure causes and flaky tests
- [ ] **Validate test assertions**: Ensure tests properly verify business requirements
- [ ] **Check test maintainability**: Assess test code quality and readability
- [ ] **Verify test data isolation**: Ensure tests don't interfere with each other
- [ ] **Assess test documentation**: Review test descriptions and documentation quality

#### **📈 Comprehensive Reporting**
- [ ] **Generate test execution report**: Create detailed report of all test runs
- [ ] **Document test metrics**: Record pass/fail rates, coverage, and performance metrics
- [ ] **Create quality dashboard**: Summarize overall system quality and health
- [ ] **Identify improvement areas**: Document areas needing attention or refactoring
- [ ] **Generate stakeholder report**: Create business-friendly quality summary
- [ ] **Check test performance**: Monitor test execution time for performance issues
- [ ] **Test external service integrations**: Validate third-party service connections
- [ ] **Identify coverage gaps**: Find untested code paths and critical missing tests
- [ ] **Generate coverage documentation**: Create coverage reports for stakeholders
- [ ] **Generate final quality report**: Create complete quality assessment document
- [ ] **Validate quality gates**: Ensure all quality thresholds are met
- [ ] **Prepare refactoring recommendations**: Identify code improvement opportunities
- [ ] **Document system readiness**: Assess readiness for refactoring and review phases

**💡 Pro Tip**: This phase validates the entire implementation - any failures indicate issues that must be addressed before moving to refactoring!

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

## Common Errors and Solutions

### ❌ Error Case 1: Tests failing due to missing implementations
**Cause**: Implementation layers not completed before running tests  
**Solution**: Complete all layers: domain → application → infrastructure → presentation

### ❌ Error Case 2: Low test coverage
**Cause**: Missing tests for implemented functionality  
**Solution**: Add tests for uncovered code paths and edge cases

### ❌ Error Case 3: Integration test failures
**Cause**: Layer integration issues or configuration problems  
**Solution**: Verify dependency injection and configuration setup

## Execution Examples

### ✅ Success Example
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

### ❌ Failure Example and Fix
```bash
$ /run-all-tests 15
❌ 3 tests failed, 42 passed
💡 失敗したテストを修正してください
# Fix: Address failing tests then re-run
$ /run-all-tests 15
```

## Task Details

## 1. **Setup Safe Environment and Parse Arguments**

```bash
# 🔧 Load all safe operation functions with automatic argument parsing and validation
source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "10-run-all-tests" "$ARGUMENTS"

# Arguments are already parsed and validated by setup script
# Additional validation for this specific command
if [[ ${#issue_numbers[@]} -eq 0 ]]; then
    echo "エラー: 最低1つのイシュー番号が必要です"
    show_usage_example "run-all-tests" "1" "単一イシューのテスト実行"
    show_usage_example "run-all-tests" "1,7" "複数イシューのテスト実行"
    show_usage_example "run-all-tests" "1,integration" "イシュー + テスト種別指定"
    exit 1
fi

# Initialize logging
initialize_operation_logging "run_all_tests"
```

## 2. **Transaction Management and Environment Preparation**

```bash
# Begin transaction for test execution
transaction_id="run_all_tests_$(date +%s)_$(echo "${issue_numbers[*]}" | tr ' ' '_')"
begin_transaction "$transaction_id"

# Setup test environment restoration
add_rollback_handler "echo '🔄 テスト環境をリストア中...'"
add_rollback_handler "rm -rf .coverage* .pytest_cache htmlcov .ruff_cache .pyright_cache 2>/dev/null || true"
add_rollback_handler "git checkout . 2>/dev/null || true"

# Discover metadata file and validate prerequisites
issue_list=$(IFS=-; echo "${issue_numbers[*]}")
if [[ ${#other_args[@]} -gt 0 ]]; then
    test_scope="${other_args[0]}"
    # Extract feature name if not a test type
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

# Validate metadata file and prerequisites
if [[ ! -f "$metadata_file" ]]; then
    echo "❌ エラー: メタデータファイルが見つかりません: $metadata_file"
    execute_rollback
    exit 1
fi

# Check that presentation layer is implemented
validate_phase_completion "$metadata_file" "presentation_implementation"

echo "✅ 前提条件チェック完了"
echo "📋 テストスコープ: $test_scope"
echo "🎯 フィーチャー: $feature_name"
```

## 3. **Safe Test Environment Preparation**

```bash
# Prepare clean test environment
echo "🧹 テスト環境を準備中..."

# Backup current state
backup_dir="$(mktemp -d)"
add_rollback_handler "rm -rf '$backup_dir'"

# Clean test artifacts safely
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

    # Clear pytest cache
    uv run --frozen pytest --cache-clear >/dev/null 2>&1 || true
}

safe_clean_test_environment

# Create test results directory
test_results_dir="docs/test_results/issue-${issue_list}-${feature_name}-$(date +%Y%m%d_%H%M%S)"
mkdir -p "$test_results_dir"
add_rollback_handler "rm -rf '$test_results_dir'"

echo "📁 テスト結果ディレクトリ: $test_results_dir"
echo "✅ テスト環境準備完了"
```

## 4. **Comprehensive Test Execution**

```bash
# Execute comprehensive test suite based on scope
echo "🧪 包括的テストスイートを実行中..."

test_summary_file="$test_results_dir/test_summary.json"
test_log_file="$test_results_dir/test_execution.log"

# Initialize test summary
cat > "$test_summary_file" << EOF
{
  "execution_start": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "issues": [$(IFS=','; echo "\"${issue_numbers[*]}\"")],
  "feature": "$feature_name",
  "scope": "$test_scope",
  "results": {}
}
EOF

# Function to run tests safely with detailed logging
run_test_suite() {
    local test_type="$1"
    local test_path="$2"
    local test_args="${3:-}"

    echo "🔍 実行中: ${test_type} テスト..."

    local start_time=$(date +%s)
    local result_file="$test_results_dir/${test_type}_results.json"
    local output_file="$test_results_dir/${test_type}_output.txt"

    # Run tests with comprehensive output capture
    local exit_code=0
    {
        echo "=== ${test_type} テスト実行開始 $(date) ==="
        echo "パス: $test_path"
        echo "引数: $test_args"
        echo ""

        if [[ -d "$test_path" && $(find "$test_path" -name "*.py" -not -name "__*" | wc -l) -gt 0 ]]; then
            # Execute with proper plugin loading
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

    # Parse results and update summary
    if [[ -f "$result_file" ]]; then
        local total_tests=$(jq -r '.summary.total // 0' "$result_file")
        local passed_tests=$(jq -r '.summary.passed // 0' "$result_file")
        local failed_tests=$(jq -r '.summary.failed // 0' "$result_file")
        local skipped_tests=$(jq -r '.summary.skipped // 0' "$result_file")

        # Update test summary
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

# Execute test suites based on scope
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

## 5. **Coverage Analysis and Quality Metrics**

```bash
# Generate comprehensive coverage report
echo "📊 カバレッジ分析を実行中..."

coverage_file="$test_results_dir/coverage_report.json"
coverage_html_dir="$test_results_dir/coverage_html"

if [[ "$test_scope" == "all" ]]; then
    # Run coverage analysis
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

        # Extract per-module coverage
        jq -r '.files | to_entries[] | "\(.key): \(.value.summary.percent_covered_display)"' "$coverage_file" > "$test_results_dir/module_coverage.txt"
    else
        echo "⚠️ カバレッジファイルが生成されませんでした"
        overall_coverage="N/A"
    fi
else
    echo "ℹ️ スコープ限定実行のためカバレッジ分析をスキップ"
    overall_coverage="N/A"
fi

# Run static analysis
echo "🔍 静的解析を実行中..."

# Ruff analysis
ruff_file="$test_results_dir/ruff_analysis.txt"
echo "🧹 Ruff 解析中..."
{
    echo "=== RUFF ANALYSIS ==="
    uv run --frozen ruff check . --statistics --output-format=json > "$test_results_dir/ruff_results.json" || true
    uv run --frozen ruff check . --show-source --statistics || true
} > "$ruff_file" 2>&1

# Type checking
pyright_file="$test_results_dir/pyright_analysis.txt"
echo "📝 Pyright 型チェック中..."
{
    echo "=== PYRIGHT TYPE CHECKING ==="
    uv run --frozen pyright --outputjson > "$test_results_dir/pyright_results.json" || true
    uv run --frozen pyright --stats || true
} > "$pyright_file" 2>&1

echo "✅ 品質メトリクス収集完了"
```

## 6. **Performance Analysis and Benchmarking**

```bash
# Performance testing (if available)
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

# Security analysis (if bandit available)
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

## 7. **Comprehensive Test Report Generation**

```bash
# Generate detailed test report
echo "📋 包括的テストレポートを生成中..."

test_report_file="$test_results_dir/comprehensive_test_report.md"

# Calculate overall test statistics
total_tests=$(jq -r '[.results[] | .total] | add // 0' "$test_summary_file")
total_passed=$(jq -r '[.results[] | .passed] | add // 0' "$test_summary_file")
total_failed=$(jq -r '[.results[] | .failed] | add // 0' "$test_summary_file")
total_skipped=$(jq -r '[.results[] | .skipped] | add // 0' "$test_summary_file")
total_duration=$(jq -r '[.results[] | .duration] | add // 0' "$test_summary_file")

# Extract individual test type results
unit_results=$(jq -r '.results.unit // {"total":0,"passed":0,"failed":0,"duration":0}' "$test_summary_file")
integration_results=$(jq -r '.results.integration // {"total":0,"passed":0,"failed":0,"duration":0}' "$test_summary_file")
e2e_results=$(jq -r '.results.e2e // {"total":0,"passed":0,"failed":0,"duration":0}' "$test_summary_file")

# Get quality metrics
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

# Add module-specific coverage if available
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

# Add recommendations based on results
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

## 8. **Atomic Metadata Update**

```bash
# Update metadata with comprehensive test results
echo "📊 メタデータを更新中..."

if [[ -f "$metadata_file" ]]; then
    # Determine overall test success
    all_tests_passed=$([[ "$test_execution_success" == "true" && "$total_failed" -eq 0 ]] && echo "true" || echo "false")

    # Update metadata atomically
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

## 9. **Use Case Index Update**

```bash
# Update use case index with comprehensive test status
echo "📋 ユースケースインデックスを更新中..."

if [[ -f "docs/use_cases/index.md" ]]; then
    feature_line="- \\[${feature_name}\\]"

    # Count test files
    unit_test_count=$(find tests/unit/ -name "*.py" -not -name "__*" 2>/dev/null | wc -l)
    integration_test_count=$(find tests/integration/ -name "*.py" -not -name "__*" 2>/dev/null | wc -l)
    e2e_test_count=$(find tests/e2e/ -name "*.py" -not -name "__*" 2>/dev/null | wc -l)

    # Create status indicator
    test_status="✅"
    if [[ "$total_failed" -gt 0 ]]; then
        test_status="❌"
    elif [[ "$total_tests" -eq 0 ]]; then
        test_status="⚠️"
    fi

    # Update with comprehensive test information
    sed -i "s|${feature_line}.*|${feature_line}($(basename ${spec_file})) - Issues: #$(IFS=' #'; echo \"${issue_numbers[*]}\") (Phase: all_tests_completed, Unit: ${unit_test_count}, Integration: ${integration_test_count}, E2E: ${e2e_test_count}, Coverage: ${overall_coverage}, Status: ${test_status})|" docs/use_cases/index.md

    echo "✅ インデックス更新完了"
else
    echo "⚠️ 警告: Use case index not found"
fi
```

## 10. **GitHub Issue Updates**

```bash
# Update GitHub issues with test results
echo "📢 GitHub イシューを更新中..."

# Create detailed test summary for GitHub
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

# Add performance info if available
if [[ -f "$performance_file" ]]; then
    github_summary="${github_summary}

⚡ **パフォーマンス**: 結果は \`${performance_file}\` を参照"
fi

# Add security info if available
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

## 11. **Transaction Commit and Final Cleanup**

```bash
# Commit transaction and provide summary
echo "💾 テスト実行結果をコミット中..."

# Commit transaction
commit_transaction

# Display comprehensive summary
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

## 🚨 MANDATORY FOR CLAUDE CODE: SCENARIO EVOLUTION CHECK

テスト実行中にテスト失敗・新要件・エッジケース発見時は
作業を中断して `/evolve-scenarios <feature-name>` を実行すること
CRITICAL: テスト結果は新シナリオ発見の重要な情報源です
