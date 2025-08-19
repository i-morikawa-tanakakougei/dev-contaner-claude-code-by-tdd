Apply review feedback using specialized agent for systematic TDD/DDD/Layered Architecture improvements.

## Metadata
- **Prerequisites**: Review completed (13-review-issue)
- **Input**: Issue number(s) (required), feedback details
- **Output**: 
  - Updated implementation addressing feedback
  - Feedback application tracking
  - Updated `docs/use_cases/issue-X-Y.json` metadata
- **Dependencies**: Review report, implementation code, Git configuration
- **Execution Timing**: After review, before final pull request creation

## 🎯 **TDD/DDD/LAYERED PROCESS CONTEXT**

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Review and Feedback Phase - Apply Feedback (14/16)  
> 🎯 **Phase Purpose**: Improve implementation based on review feedback  
> ⬅️ **Previous Stage**: 13-review-issue (Implementation Review)  
> ➡️ **Next Stage**: 15-create-pr (Create Pull Request)
>
> **📋 3-Layer Architecture Operations**:
>
> - 🎯 **Strategic**: `docs/use_cases/core/index.md` (Reference for quality standards)
> - 📊 **Tactical**: `docs/use_cases/index.md` (Update feedback application status)
> - 🔧 **Execution**: `docs/use_cases/issue-X-Y.json` (Track feedback application)

## 🔧 **TARGETED FEEDBACK APPLICATION ONLY**

**⚠️ Important Notice:**
- **This step is TARGETED IMPROVEMENTS ONLY** - Apply specific feedback from review
- **LIMITED IMPLEMENTATION** - Only make changes based on review feedback  
- **Quality improvement focus** - Address specific issues identified in review
- **Follow review recommendations** - No arbitrary changes beyond feedback

**Feedback Application Process:**
1. `13-review-issue` ← Review completed with specific feedback
2. `14-apply-feedback` ← **【YOU ARE HERE】Apply review recommendations**
3. `15-create-pr` ← Create pull request with improvements
4. Merge and close cycle

**Allowed Changes:**
- ✅ Fix issues identified in review
- ✅ Improve code quality based on specific feedback
- ✅ Address test gaps and coverage issues
- ❌ No new features or functionality beyond feedback scope

## Common Errors and Solutions

### ❌ Error Case 1: Review not completed
**Cause**: Feedback application attempted before review completion  
**Solution**: Complete review first with `/review-issue <issue-number>`

### ❌ Error Case 2: Feedback conflicts with existing implementation
**Cause**: Feedback requires changes that break existing functionality  
**Solution**: Analyze impact and create plan to address conflicts safely

### ❌ Error Case 3: Tests break after applying feedback
**Cause**: Changes made without maintaining test compatibility  
**Solution**: Update tests alongside implementation changes or revert changes

## Execution Examples

### ✅ Success Example
```bash
$ /apply-feedback 15
🔄 Issues: #15 のフィードバック適用を開始します
📝 レビューフィードバック分析中...
✅ 3件のフィードバックを発見
🔧 実装更新中...
  ✅ コード品質改善適用
  ✅ アーキテクチャ改善適用
🧪 フィードバック適用後テスト実行...
======= 45 passed, 0 failed =======
✅ フィードバック適用完了
🎉 フィードバック適用完了!
```

### ❌ Failure Example and Fix
```bash
$ /apply-feedback 15
❌ レビューが完了していません
💡 最初にレビューを完了してください:
   /review-issue 15

# Fix: Complete review first
$ /review-issue 15
$ /apply-feedback 15
```

## 📋 **FEEDBACK APPLICATION TASK CHECKLIST**

**Use this checklist for systematic feedback implementation:**

### 🔴 Required Tasks

#### **📊 Review Analysis and Planning**
- [ ] **Parse review findings**: Analyze comprehensive review report from step 13
- [ ] **Categorize feedback items**: Group by Critical/High/Medium/Low priority
- [ ] **Assess implementation effort**: Estimate time and complexity for each item
- [ ] **Plan implementation sequence**: Order improvements by priority and dependencies

#### **🚨 Critical Issues Resolution (Priority 1)**
- [ ] **Fix security vulnerabilities**: Address any security issues identified in review
- [ ] **Resolve Given-When-Then gaps**: Fix missing or incorrect scenario coverage
- [ ] **Fix broken architecture boundaries**: Correct any layer violation issues
- [ ] **Address data integrity issues**: Fix any data handling or validation problems
- [ ] **Fix broken or missing tests**: Address test failures or gaps

### 🟡 Recommended Tasks

#### **⚡ High Priority Improvements (Priority 2)**
- [ ] **Improve test quality**: Enhance test structure, readability, and coverage
- [ ] **Fix code quality issues**: Address complex methods, naming, and duplication
- [ ] **Improve error handling**: Enhance exception handling and error responses
- [ ] **Address API design issues**: Fix endpoint design and response formatting problems
- [ ] **Improve domain model**: Enhance entity, value object, and service design
- [ ] **Fix integration issues**: Address repository and external service integration problems

### 🟢 Optional Tasks

#### **📈 Medium Priority Enhancements (Priority 3)**
- [ ] **Improve documentation**: Enhance code comments, API docs, and user guides
- [ ] **Optimize performance**: Address non-critical performance improvements
- [ ] **Identify risk areas**: Flag changes that might affect system stability
- [ ] **Create implementation roadmap**: Plan systematic approach for applying feedback
- [ ] **Resolve performance bottlenecks**: Fix critical performance issues
- [ ] **Enhance user experience**: Improve CLI usability and API responses
- [ ] **Improve code organization**: Better structure and modularization
- [ ] **Add monitoring/logging**: Enhance observability and debugging capabilities
- [ ] **Improve configuration**: Better configuration management and validation

### **🔧 Code Quality Validation (After Each Priority Level)**
- [ ] **Run ruff linting**: Execute `uv run --frozen ruff check src/ --fix`
- [ ] **Run ruff formatting**: Execute `uv run --frozen ruff format src/`
- [ ] **Run type checking**: Execute `uv run --frozen pyright src/`
- [ ] **Fix quality issues**: Address any linting, formatting, or type errors
- [ ] **Verify clean results**: Ensure all quality tools pass without errors

### **🧪 Continuous Testing (After Each Change)**
- [ ] **Run affected tests**: Execute tests related to changed code
- [ ] **Run full test suite**: Execute `uv run --frozen pytest` for complete validation
- [ ] **Verify all tests GREEN**: Ensure no functionality is broken
- [ ] **Check test coverage**: Verify coverage hasn't decreased
- [ ] **Validate Given-When-Then scenarios**: Ensure scenario tests still pass
- [ ] **Test integration points**: Verify cross-layer integration still works

### **📖 Given-When-Then Coverage Improvements**
- [ ] **Add missing scenario tests**: Implement tests for uncovered scenarios
- [ ] **Improve test clarity**: Make tests better express business intent
- [ ] **Fix scenario-test mismatches**: Align tests with actual scenarios
- [ ] **Add edge case tests**: Implement tests for boundary conditions
- [ ] **Improve error scenario coverage**: Add tests for failure scenarios
- [ ] **Enhance acceptance criteria validation**: Ensure all criteria are tested

### **🏗️ Architecture Compliance Fixes**
- [ ] **Fix layer violations**: Correct any dependency direction issues
- [ ] **Improve interface segregation**: Enhance repository and service interfaces
- [ ] **Fix domain purity issues**: Remove external dependencies from domain layer
- [ ] **Improve aggregate design**: Fix any aggregate boundary issues
- [ ] **Enhance domain model**: Improve entity and value object design
- [ ] **Fix transaction boundaries**: Correct any transaction management issues

### **🔗 Integration and Infrastructure Improvements**
- [ ] **Improve repository implementations**: Fix data access patterns and error handling
- [ ] **Enhance external service integration**: Improve third-party service handling
- [ ] **Fix configuration issues**: Address configuration management problems
- [ ] **Improve error propagation**: Enhance cross-layer error handling
- [ ] **Fix transaction management**: Address database transaction issues
- [ ] **Enhance monitoring**: Improve logging and observability

### **🌐 Presentation Layer Enhancements**
- [ ] **Fix API design issues**: Improve endpoint design and HTTP status codes
- [ ] **Improve input validation**: Enhance request validation and error responses
- [ ] **Fix authentication/authorization**: Address security implementation issues
- [ ] **Improve response formatting**: Enhance response structure and error handling
- [ ] **Fix API documentation**: Correct endpoint documentation issues
- [ ] **Enhance CLI usability**: Improve command-line interface user experience

### **📊 Quality Metrics Validation**
- [ ] **Measure improvement impact**: Compare before/after quality metrics
- [ ] **Validate coverage improvements**: Ensure test coverage has increased
- [ ] **Assess complexity reduction**: Verify code complexity has decreased
- [ ] **Check performance improvements**: Measure any performance gains
- [ ] **Validate maintainability**: Assess code maintainability improvements
- [ ] **Document quality gains**: Record measurable quality improvements

### **🔍 Final Validation and Quality Check**
- [ ] **Run comprehensive test suite**: Execute all tests with coverage
- [ ] **Final code quality check**: Run `uv run --frozen ruff check src/ --fix`
- [ ] **Final formatting check**: Run `uv run --frozen ruff format src/`
- [ ] **Final type checking**: Run `uv run --frozen pyright src/`
- [ ] **Validate all improvements**: Ensure all feedback items are addressed
- [ ] **Check system stability**: Verify system operates correctly after changes

### **📚 Documentation and Handoff**
- [ ] **Update implementation documentation**: Record changes made during feedback application
- [ ] **Update metadata**: Record feedback application results in issue-X-Y.json
- [ ] **Create improvement summary**: Document what was improved and impact
- [ ] **Commit all improvements**: Version control all changes with clear commit messages
- [ ] **Prepare for PR creation**: Ensure code is ready for pull request submission
- [ ] **Generate final quality report**: Create before/after comparison of quality metrics

**💡 Pro Tip**: Apply feedback systematically by priority, and validate continuously - each improvement should make the system measurably better!

## Task Details

**Agent Integration Pattern - 4 Steps:**

1. **Pre-execution Validation**:
   ```bash
   # 🔧 Load all safe operation functions
   source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "14-apply-feedback" "$ARGUMENTS"
   
   # Validate issue number requirement
   if [[ ${#issue_numbers[@]} -eq 0 ]]; then
       echo "エラー: 最低1つのイシュー番号が必要です"
       show_usage_example "apply-feedback" "1" "単一イシューのフィードバック適用"
       show_usage_example "apply-feedback" "1,7" "複数イシューのフィードバック適用"
       show_usage_example "apply-feedback" "1,feature-name" "イシュー + フィーチャー指定"
       exit 1
   fi
   
   # Discover feature name and metadata
   issue_list=$(IFS=-; echo "${issue_numbers[*]}")
   if [[ ${#other_args[@]} -gt 0 ]]; then
       feature_name="${other_args[0]}"
   else
       # Extract feature name from use case file
       feature_name=$(find docs/use_cases -name "issue-${issue_list}-*.md" | head -1 | sed 's/.*issue-[0-9-]*-\(.*\)\.md$/\1/')
       if [[ -z "$feature_name" ]]; then
           echo "❌ エラー: フィーチャー名を特定できませんでした"
           echo "💡 使用方法: /apply-feedback $issue_list,<feature-name>"
           exit 1
       fi
   fi
   
   metadata_file="docs/use_cases/issue-${issue_list}-${feature_name}.json"
   spec_file="docs/use_cases/issue-${issue_list}-${feature_name}.md"
   
   echo "🔄 Issues: #$(IFS=' #'; echo "${issue_numbers[*]}") - ${feature_name} のフィードバック適用を開始します"
   
   # Validate prerequisites
   if [[ ! -f "$metadata_file" ]]; then
       echo "❌ エラー: メタデータファイルが見つかりません: $metadata_file"
       exit 1
   fi
   
   # Check that review is completed
   if command -v jq >/dev/null 2>&1; then
       review_status=$(jq -r '.phases.review.reviewed // false' "$metadata_file" 2>/dev/null)
       if [[ "$review_status" != "true" ]]; then
           echo "❌ エラー: レビューが完了していません"
           echo "💡 最初にレビューを完了してください: /review-issue ${issue_numbers[*]}"
           exit 1
       fi
   fi
   
   echo "✅ 前提条件確認完了: フィードバック適用準備完了"
   ```

2. **Execute Specialized Agent**:
   ```bash
   # 🤖 Call specialized agent with Task tool for feedback application
   echo "🤖 専用エージェント実行中: 14-apply-feedback"
   
   # Build comprehensive task context
   task_context="Feedback Application Request:
   
   Issues: $(printf '#%s ' "${issue_numbers[@]}")
   Feature: $feature_name
   Metadata: $metadata_file
   Spec: $spec_file
   
   Request: Systematic application of review feedback with targeted improvements only
   
   COMPREHENSIVE TASK CHECKLIST:
   
   🔴 Required Tasks:
   
   📊 Review Analysis and Planning:
   - Parse review findings: analyze comprehensive review report from step 13
   - Categorize feedback items: group by Critical/High/Medium/Low priority
   - Assess implementation effort: estimate time and complexity for each item
   - Plan implementation sequence: order improvements by priority and dependencies
   
   🚨 Critical Issues Resolution (Priority 1):
   - Fix security vulnerabilities: address any security issues identified in review
   - Resolve Given-When-Then gaps: fix missing or incorrect scenario coverage
   - Fix broken architecture boundaries: correct any layer violation issues
   - Address data integrity issues: fix any data handling or validation problems
   - Fix broken or missing tests: address test failures or gaps
   
   🟡 Recommended Tasks:
   
   ⚡ High Priority Improvements (Priority 2):
   - Improve test quality: enhance test structure, readability, and coverage
   - Fix code quality issues: address complex methods, naming, and duplication
   - Improve error handling: enhance exception handling and error responses
   - Address API design issues: fix endpoint design and response formatting problems
   - Improve domain model: enhance entity, value object, and service design
   - Fix integration issues: address repository and external service integration problems
   
   🟢 Optional Tasks:
   
   📈 Medium Priority Enhancements (Priority 3):
   - Improve documentation: enhance code comments, API docs, and user guides
   - Optimize performance: address non-critical performance improvements
   - Identify risk areas: flag changes that might affect system stability
   - Create implementation roadmap: plan systematic approach for applying feedback
   - Resolve performance bottlenecks: fix critical performance issues
   - Enhance user experience: improve CLI usability and API responses
   - Improve code organization: better structure and modularization
   - Add monitoring/logging: enhance observability and debugging capabilities
   - Improve configuration: better configuration management and validation
   
   🔧 Code Quality Validation (After Each Priority Level):
   - Run ruff linting: execute uv run --frozen ruff check src/ --fix
   - Run ruff formatting: execute uv run --frozen ruff format src/
   - Run type checking: execute uv run --frozen pyright src/
   - Fix quality issues: address any linting, formatting, or type errors
   - Verify clean results: ensure all quality tools pass without errors
   
   🧪 Continuous Testing (After Each Change):
   - Run affected tests: execute tests related to changed code
   - Run full test suite: execute uv run --frozen pytest for complete validation
   - Verify all tests GREEN: ensure no functionality is broken
   - Check test coverage: verify coverage hasn't decreased
   - Validate Given-When-Then scenarios: ensure scenario tests still pass
   - Test integration points: verify cross-layer integration still works
   
   📖 Given-When-Then Coverage Improvements:
   - Add missing scenario tests: implement tests for uncovered scenarios
   - Improve test clarity: make tests better express business intent
   - Fix scenario-test mismatches: align tests with actual scenarios
   - Add edge case tests: implement tests for boundary conditions
   - Improve error scenario coverage: add tests for failure scenarios
   - Enhance acceptance criteria validation: ensure all criteria are tested
   
   🏗️ Architecture Compliance Fixes:
   - Fix layer violations: correct any dependency direction issues
   - Improve interface segregation: enhance repository and service interfaces
   - Fix domain purity issues: remove external dependencies from domain layer
   - Improve aggregate design: fix any aggregate boundary issues
   - Enhance domain model: improve entity and value object design
   - Fix transaction boundaries: correct any transaction management issues
   
   🔗 Integration and Infrastructure Improvements:
   - Improve repository implementations: fix data access patterns and error handling
   - Enhance external service integration: improve third-party service handling
   - Fix configuration issues: address configuration management problems
   - Improve error propagation: enhance cross-layer error handling
   - Fix transaction management: address database transaction issues
   - Enhance monitoring: improve logging and observability
   
   🌐 Presentation Layer Enhancements:
   - Fix API design issues: improve endpoint design and HTTP status codes
   - Improve input validation: enhance request validation and error responses
   - Fix authentication/authorization: address security implementation issues
   - Improve response formatting: enhance response structure and error handling
   - Fix API documentation: correct endpoint documentation issues
   - Enhance CLI usability: improve command-line interface user experience
   
   📊 Quality Metrics Validation:
   - Measure improvement impact: compare before/after quality metrics
   - Validate coverage improvements: ensure test coverage has increased
   - Assess complexity reduction: verify code complexity has decreased
   - Check performance improvements: measure any performance gains
   - Validate maintainability: assess code maintainability improvements
   - Document quality gains: record measurable quality improvements
   
   🔍 Final Validation and Quality Check:
   - Run comprehensive test suite: execute all tests with coverage
   - Final code quality check: run uv run --frozen ruff check src/ --fix
   - Final formatting check: run uv run --frozen ruff format src/
   - Final type checking: run uv run --frozen pyright src/
   - Validate all improvements: ensure all feedback items are addressed
   - Check system stability: verify system operates correctly after changes
   
   📚 Documentation and Handoff:
   - Update implementation documentation: record changes made during feedback application
   - Update metadata: record feedback application results in issue-X-Y.json
   - Create improvement summary: document what was improved and impact
   - Commit all improvements: version control all changes with clear commit messages
   - Prepare for PR creation: ensure code is ready for pull request submission
   - Generate final quality report: create before/after comparison of quality metrics
   
   CONSTRAINTS:
   - TARGETED IMPROVEMENTS ONLY - apply specific feedback from review only
   - LIMITED IMPLEMENTATION - only make changes based on review feedback
   - Quality improvement focus - address specific issues identified in review
   - Follow review recommendations - no arbitrary changes beyond feedback
   - No new features or functionality beyond feedback scope
   - Maintain TDD/DDD/Clean Architecture principles
   - Apply feedback systematically by priority with continuous validation
   
   OUTPUT REQUIREMENTS:
   - Generate feedback application report in docs/reviews/
   - Update metadata files with application status and metrics
   - Create improved implementation addressing review feedback
   - Commit changes with clear messages
   - Maintain all tests in GREEN state
   - Ensure architecture compliance maintained
   
   CRITICAL SCENARIO EVOLUTION CHECK:
   If new requirements, constraints, or improvement opportunities are discovered during
   feedback application, immediately interrupt work and execute /evolve-scenarios <feature-name>
   Feedback application is a critical opportunity for new scenario discovery"
   
   # Execute the specialized agent
   claude_task="$task_context" \
       claude_agent="14-apply-feedback" \
       claude_working_dir="$(pwd)" \
       claude_issues="$(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')" \
       claude_feature_name="$feature_name" \
       claude --agent
   
   agent_exit_code=$?
   echo "✅ 専用エージェント実行完了 (終了コード: $agent_exit_code)"
   ```

3. **Agent Result Verification**:
   ```bash
   # 🔍 Verify agent execution results
   echo "🔍 エージェント結果検証中..."
   
   verification_issues=()
   
   # Check metadata was updated properly
   if [[ -f "$metadata_file" ]] && command -v jq >/dev/null 2>&1; then
       feedback_applied=$(jq -r '.phases.feedback_application.applied // false' "$metadata_file" 2>/dev/null)
       if [[ "$feedback_applied" == "true" ]]; then
           applied_count=$(jq -r '.phases.feedback_application.applied_improvements // 0' "$metadata_file")
           skipped_count=$(jq -r '.phases.feedback_application.skipped_improvements // 0' "$metadata_file")
           created_issues=$(jq -r '.phases.feedback_application.created_issues // 0' "$metadata_file")
           post_coverage=$(jq -r '.phases.feedback_application.post_coverage // "N/A"' "$metadata_file")
           
           echo "  ✅ メタデータ更新完了"
           echo "    📈 適用完了: ${applied_count} 項目"
           echo "    ⏸️ 保留項目: ${skipped_count} 項目"
           echo "    🆕 新規Issue: ${created_issues} 件"
           echo "    📊 改善後カバレッジ: ${post_coverage}%"
       else
           verification_issues+=("メタデータの適用状況が未確認")
       fi
   else
       verification_issues+=("メタデータファイルの検証に失敗")
   fi
   
   # Check generated feedback application report
   feedback_report_pattern="docs/reviews/*issue*${issue_list}*${feature_name}*feedback*.md"
   feedback_reports=($(ls $feedback_report_pattern 2>/dev/null))
   
   if [[ ${#feedback_reports[@]} -eq 0 ]]; then
       # Try alternative pattern
       feedback_report_pattern="docs/reviews/*issue*${issue_list}*feedback*.md"
       feedback_reports=($(ls $feedback_report_pattern 2>/dev/null))
   fi
   
   if [[ ${#feedback_reports[@]} -eq 0 ]]; then
       verification_issues+=("フィードバック適用レポートが作成されていません")
   else
       feedback_report="${feedback_reports[-1]}"  # Get most recent
       echo "  ✅ フィードバック適用レポート: $(basename "$feedback_report")"
   fi
   
   # Verify tests are still passing
   if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest -q >/dev/null 2>&1; then
       echo "  ✅ 全テストGREEN確認"
   else
       verification_issues+=("テスト失敗を検出")
   fi
   
   # Check for obvious architecture violations
   if find src/ -name "*.py" 2>/dev/null | xargs grep -l "import.*infrastructure" 2>/dev/null | grep -q "domain" 2>/dev/null; then
       verification_issues+=("潜在的なアーキテクチャ違反を検出")
   else
       echo "  ✅ アーキテクチャ準拠性維持"
   fi
   
   # Check agent exit code
   if [[ $agent_exit_code -ne 0 ]]; then
       verification_issues+=("エージェント実行エラー (終了コード: $agent_exit_code)")
   fi
   
   # Report verification results
   if [[ ${#verification_issues[@]} -eq 0 ]]; then
       echo "✅ エージェント結果検証完了"
   else
       echo "❌ エージェント結果検証で問題が発見されました:"
       printf '  - %s\n' "${verification_issues[@]}"
       exit 1
   fi
   ```

4. **Display Success Summary**:
   ```bash
   # 🎉 Display comprehensive success summary
   echo ""
   echo "🎉 フィードバック適用完了!"
   echo ""
   echo "📊 実行サマリー:"
   echo "  📂 対象Issues: $(printf '#%s ' "${issue_numbers[@]}")"
   echo "  🏷️ フィーチャー: $feature_name"
   echo "  📝 生成レポート: $feedback_report"
   echo "  🔄 メタデータ: $metadata_file"
   echo ""
   
   # Show feedback application summary
   if [[ -f "$metadata_file" ]] && command -v jq >/dev/null 2>&1; then
       applied_count=$(jq -r '.phases.feedback_application.applied_improvements // 0' "$metadata_file")
       skipped_count=$(jq -r '.phases.feedback_application.skipped_improvements // 0' "$metadata_file")
       created_issues=$(jq -r '.phases.feedback_application.created_issues // 0' "$metadata_file")
       post_coverage=$(jq -r '.phases.feedback_application.post_coverage // "N/A"' "$metadata_file")
       post_ruff=$(jq -r '.phases.feedback_application.post_ruff_errors // "N/A"' "$metadata_file")
       post_pyright=$(jq -r '.phases.feedback_application.post_pyright_errors // "N/A"' "$metadata_file")
       tests_passing=$(jq -r '.phases.feedback_application.tests_passing // false' "$metadata_file")
       
       echo "🔄 フィードバック適用結果:"
       echo "   📈 適用完了: ${applied_count} 項目"
       echo "   ⏸️ 保留項目: ${skipped_count} 項目"
       echo "   🆕 新規Issue: ${created_issues} 件"
       echo "   📊 テストカバレッジ: ${post_coverage}%"
       echo "   🔧 Ruffエラー: ${post_ruff} 件"
       echo "   🔍 Pyrightエラー: ${post_pyright} 件"
       echo "   🧪 テスト状態: $(if [[ "$tests_passing" == "true" ]]; then echo "✅ 全GREEN"; else echo "❌ 要修正"; fi)"
       
       # Determine quality status and next steps
       if [[ "$post_ruff" == "0" && "$post_pyright" == "0" && "$tests_passing" == "true" ]]; then
           echo ""
           echo "🎯 品質評価: ✅ 優秀 - 品質基準達成"
           next_step="/create-pr ${issue_numbers[*]}"
       elif [[ "$applied_count" != "0" ]]; then
           echo ""
           echo "🎯 品質評価: 📈 改善 - 品質向上"
           if [[ "$created_issues" != "0" ]]; then
               next_step="新規Issue対応後に /create-pr ${issue_numbers[*]}"
           else
               next_step="/create-pr ${issue_numbers[*]}"
           fi
       else
           echo ""
           echo "🎯 品質評価: ⚠️ 要継続 - さらなる改善必要"
           next_step="/review-issue ${issue_numbers[*]} (再レビュー)"
       fi
   else
       next_step="/review-issue ${issue_numbers[*]} (再レビュー)"
   fi
   
   echo ""
   echo "📋 次のステップ:"
   echo "   💡 $next_step"
   echo "   💡 /use-case-status $(IFS=','; echo "${issue_numbers[*]}")"
   
   echo ""
   echo "📁 生成ファイル:"
   echo "  📝 フィードバック適用レポート: $feedback_report"
   echo "  🔄 メタデータ: $metadata_file"
   echo "  🔧 改善されたソースコード"
   
   echo ""
   echo "🔗 関連リソース:"
   for issue_num in "${issue_numbers[@]}"; do
       echo "   - Issue #$issue_num: gh issue view $issue_num"
   done
   
   echo ""
   echo "🎯 フィードバック適用が正常に完了しました!"
   ```

**💡 Key Benefits of Feedback Application:**
- **Targeted Improvements**: Apply only specific feedback from review process
- **Systematic Quality Enhancement**: Priority-based improvement implementation
- **Continuous Validation**: Maintain test coverage and architecture compliance
- **Measurable Progress**: Track before/after quality metrics
- **Safe Implementation**: Maintain system stability throughout improvements

**🎯 Critical Success Factors:**
- Apply feedback systematically by priority with continuous validation
- Maintain all tests in GREEN state throughout the process
- Address only specific issues identified in review (no new features)
- Ensure architecture compliance is maintained
- Document all improvements for traceability

**🚨 MANDATORY FOR CLAUDE CODE: SCENARIO EVOLUTION CHECK**

フィードバック適用中に新要件・制約・改善案発見時は
作業を中断して `/evolve-scenarios <feature-name>` を実行すること
CRITICAL: フィードバック適用は新シナリオ発見の絶好の機会です