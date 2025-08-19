Run all tests and generate comprehensive test report.

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

**💡 Pro Tip**: This phase validates the entire implementation - any failures indicate issues that must be addressed before moving to refactoring!

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

**🤖 Agent Integration**: This command uses the specialized `10-run-all-tests` agent for optimal test execution and reporting.

1. **Pre-execution Validation**:
   ```bash
   # Validate issue number requirement
   if [[ $# -eq 0 ]]; then
       echo "エラー: 少なくとも1つのイシュー番号を指定してください"
       echo "使用例: /run-all-tests 1"
       echo "使用例: /run-all-tests 1,7 (複数イシュー)"
       exit 1
   fi
   
   # Extract issue numbers from arguments
   issue_numbers=()
   
   # Parse first argument for issue numbers
   IFS=',' read -ra ISSUE_ARRAY <<< "$1"
   for issue in "${ISSUE_ARRAY[@]}"; do
       if [[ "$issue" =~ ^[0-9]+$ ]]; then
           issue_numbers+=("$issue")
       fi
   done
   
   # Check for presentation layer implementation completion
   missing_presentation=()
   for issue_num in "${issue_numbers[@]}"; do
       # Look for presentation implementation files
       if ! find src/presentation/ -name "*${issue_num}*.py" -o -name "*controller*.py" -type f 2>/dev/null | head -1 >/dev/null; then
           missing_presentation+=("$issue_num")
       fi
   done
   
   if [[ ${#missing_presentation[@]} -gt 0 ]]; then
       echo "❌ エラー: 以下のIssueのプレゼンテーション層実装が見つかりません:"
       printf '  - Issue #%s\n' "${missing_presentation[@]}"
       echo "💡 先に /implement-presentation を実行してください"
       exit 1
   fi
   
   echo "🧪 Issues: $(printf '#%s ' "${issue_numbers[@]}")の全テスト実行を開始します"
   ```

2. **Execute All Tests Agent**:
   ```bash
   # 🤖 Delegate to specialized test execution agent
   echo "🧪 全テスト実行エージェントを起動します..."
   echo "専門エージェントが包括的テストスイートを実行します"
   echo ""
   
   # Call the specialized agent using Claude Code's Task tool
   # The agent will handle:
   # - Unit test execution and analysis
   # - Integration test execution and validation
   # - End-to-end test execution and verification
   # - Coverage analysis and reporting
   # - Quality metrics collection and assessment
   # - Performance testing and benchmarking
   # - Test result analysis and failure investigation
   # - Comprehensive reporting and documentation
   
   # Note: In actual implementation, this would be handled by the Claude Code system
   # when the /run-all-tests command is executed. The agent integration happens
   # automatically through the Task tool with subagent_type="10-run-all-tests"
   
   echo "✅ 全テスト実行エージェント呼び出し完了"
   echo "エージェントが以下の処理を実行しました:"
   echo "  - ユニットテストの実行と分析"
   echo "  - 統合テストの実行と検証"
   echo "  - エンドツーエンドテストの実行と確認"
   echo "  - カバレッジ分析とレポート生成"
   echo "  - 品質メトリクスの収集と評価"
   echo "  - パフォーマンステストとベンチマーク"
   echo "  - テスト結果分析と失敗調査"
   echo "  - 包括的レポート作成とドキュメント化"
   ```

3. **Agent Result Verification**:
   ```bash
   # 🔍 Verify agent execution results
   echo "🔍 エージェント実行結果を検証中..."
   
   # Check that test results were generated
   echo "  🔍 テスト結果ファイルの作成確認中..."
   
   test_results_found=()
   for issue_num in "${issue_numbers[@]}"; do
       # Look for test result files
       result_pattern="docs/test_results/*issue*${issue_num}*"
       if ls $result_pattern 2>/dev/null | head -1 >/dev/null; then
           result_files=$(ls $result_pattern 2>/dev/null)
           for file in $result_files; do
               test_results_found+=("$file")
               echo "    ✅ Issue #$issue_num のテスト結果を確認: $(basename "$file")"
           done
       else
           echo "    ❌ Issue #$issue_num のテスト結果が見つかりません"
       fi
       
       # Check metadata update
       metadata_pattern="docs/use_cases/*issue*${issue_num}*.json"
       if ls $metadata_pattern 2>/dev/null | head -1 >/dev/null; then
           metadata_file=$(ls $metadata_pattern 2>/dev/null | head -1)
           if command -v jq >/dev/null 2>&1; then
               test_status=$(jq -r '.phases.tests.passed // false' "$metadata_file" 2>/dev/null)
               if [[ "$test_status" == "true" ]]; then
                   echo "    ✅ Issue #$issue_num のメタデータが更新されました"
               else
                   echo "    ⚠️ Issue #$issue_num のメタデータ更新が未確認"
               fi
           fi
       fi
   done
   
   # Check if test results directory exists
   if [[ ! -d "docs/test_results" ]]; then
       echo "❌ エラー: docs/test_results ディレクトリが作成されていません"
       exit 1
   fi
   
   # Report validation results
   if [[ ${#test_results_found[@]} -eq 0 ]]; then
       echo "❌ エージェント実行検証失敗: テスト結果ファイルが作成されていません"
       exit 1
   fi
   
   echo "✅ エージェント実行結果検証完了"
   ```

4. **Display Test Execution Success Summary**:
   ```bash
   # 📊 Display comprehensive test execution summary
   echo ""
   echo "🎉 全テスト実行完了!"
   echo "============================================="
   
   # Show created test result files
   echo "📁 作成されたテスト結果ファイル:"
   for file in "${test_results_found[@]}"; do
       if [[ -f "$file" ]]; then
           echo "   ✅ $file"
       fi
   done
   
   # Show test execution summary
   echo ""
   echo "🧪 テスト実行サマリー:"
   if [[ ${#test_results_found[@]} -gt 0 ]]; then
       # Extract test statistics from the first result file
       first_result="${test_results_found[0]}"
       if [[ -f "$first_result" ]]; then
           # Try to extract basic test information
           echo "   📊 テスト結果詳細は各ファイルを確認してください"
       fi
   fi
   
   # Show next steps
   echo ""
   echo "📋 次のステップ (リファクタリング・レビュー):"
   for issue_num in "${issue_numbers[@]}"; do
       echo "   /refactor $issue_num"
       echo "   /review-issue $issue_num"
   done
   
   echo ""
   echo "📚 重要ドキュメント:"
   echo "   - テスト結果: docs/test_results/"
   echo "   - カバレッジレポート: HTMLファイルを確認"
   if [[ ${#test_results_found[@]} -gt 0 ]]; then
       echo "   - 実行結果: ${test_results_found[0]} 他"
   fi
   
   echo ""
   echo "🔗 関連リソース:"
   for issue_num in "${issue_numbers[@]}"; do
       echo "   - Issue #$issue_num: gh issue view $issue_num"
   done
   
   echo ""
   echo "✅ 全テスト実行完了 - 品質検証完了!"
   ```

Important Notes:
- Run tests in isolated environment
- Generate comprehensive reports and metrics
- Validate all layers work together correctly
- Document test results for team review
- All user-facing output must be in JAPANESE