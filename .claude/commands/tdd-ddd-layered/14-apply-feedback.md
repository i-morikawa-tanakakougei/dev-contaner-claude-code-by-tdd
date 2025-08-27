Use the 14-apply-feedback subagent to apply review feedback for systematic TDD/DDD/Layered Architecture improvements. This command MUST USE PROACTIVELY the specialized 14-apply-feedback subagent for optimal feedback application.

**📖 Required Reading**: Before execution, this command MUST read the following files:
- `/workspace/.claude/context/current-command-context.json` - Current execution context
- `/workspace/.claude/context/project-context.json` - Overall project state and active sprint information
- `/workspace/docs/use_cases/issue-X-Y.json` - Issue-specific metadata and implementation status
- `/workspace/docs/reviews/` - Review reports containing feedback to be applied
- `/workspace/docs/metadata/project-state.json` - Integrated project status for update

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

**🤖 Agent Integration**: This command MUST USE PROACTIVELY the specialized `14-apply-feedback` subagent for systematic feedback implementation and improvement.
 Claude Code should automatically delegate this task to the 14-apply-feedback subagent based on the command description.

## 📖 Subagent Document Reading Instructions

This command delegates to the specialized `14-apply-feedback` subagent.

**MANDATORY: The subagent MUST read these files before execution:**

1. `docs/index.md` - Project overview and current status
2. `.claude/context/project-context.json` - Current project context
3. `/workspace/.claude/context/current-command-context.json` - Current execution context
4. `docs/reviews/` - Review reports containing specific feedback to apply
5. `docs/use_cases/issue-X-Y.json` - Issue metadata and current implementation status
6. `src/` directories - Current implementation code that needs improvement
7. `tests/` directories - Test code that may need updates alongside changes

**Command-Specific Reading Focus - Feedback Application:**
- Analyze review reports to identify specific feedback items and priorities
- Understand current implementation structure to plan improvements
- Review test coverage to ensure improvements don't break functionality
- Study architectural patterns to maintain consistency during changes
- Examine code quality issues highlighted in review for targeted fixes

**CRITICAL:** Use the Read tool to actually read file contents, not just reference paths.

Follow these steps:

1. **Pre-execution Validation**:
   ```bash
   # Validate issue number requirement
   if [[ $# -eq 0 ]]; then
       echo "エラー: 最低1つのイシュー番号が必要です"
       echo "使用例:"
       echo "  /apply-feedback 15        # 単一イシューフィードバック適用"
       echo "  /apply-feedback 15,23     # 複数イシューフィードバック適用"
       exit 1
   fi
   
   # Parse issue numbers
   IFS=',' read -ra ISSUES <<< "$1"
   echo "🔄 Issues: $(printf '#%s ' "${ISSUES[@]}")のフィードバック適用を開始します"
   
   # Check review completion
   review_found=false
   for issue_num in "${ISSUES[@]}"; do
       if find docs/reviews/ -name "*${issue_num}*review*" -type f 2>/dev/null | head -1 >/dev/null; then
           review_found=true
           break
       fi
   done
   
   if [[ "$review_found" != "true" ]]; then
       echo "❌ レビューが完了していません"
       echo "💡 最初にレビューを完了してください: /review-issue $1"
       exit 1
   fi
   ```

2. **Context Preparation and Agent Execution**:
   ```bash
   # 🔄 Prepare context for agent (Pattern B: Hybrid approach)
   echo "🔄 コンテキスト準備とエージェント起動..."
   
   # Create context file with feedback application information
   context_file="/workspace/.claude/context/current-command-context.json"
   current_time=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
   
   # Build context JSON for feedback application
   cat > "$context_file" <<EOF
   {
     "command": "apply-feedback",
     "timestamp": "$current_time",
     "issue_numbers": [$(IFS=,; printf '%s\n' "${ISSUES[@]}" | paste -sd,)],
     "phase": "feedback-application",
     "context": {
       "expected_outputs": [
         "improved codebase in src/",
         "updated tests in tests/",
         "docs/analysis/improvement-report.md"
       ],
       "architecture_patterns": ["Continuous Improvement", "Quality Enhancement", "TDD"]
     },
     "additional_instructions": "レビューで特定された課題に対して体系的にフィードバックを適用してください。優先度に基づいて改善を実施し、全テストがGREEN状態を維持するように注意してください。アーキテクチャ準拠性、コード品質、テストカバレッジの向上を図ってください。",
     "special_considerations": [
       "レビューフィードバックの優先度に基づく体系的改善",
       "全テストのGREEN状態維持（テスト破綻防止）",
       "アーキテクチャ準拠性の維持・向上",
       "新機能追加ではなく既存機能の品質向上に専念"
     ],
     "custom_context": {
       "feedback_prioritization": true,
       "systematic_improvement": true,
       "test_preservation": true,
       "quality_enhancement": true
     }
   }
   EOF
   
   echo "✅ コンテキストファイル作成完了: $context_file"
   
   # 🤖 Call the specialized agent with hybrid context
   echo ""
   echo "🔄 フィードバック適用エージェントを起動します..."
   echo "専門エージェントが体系的にフィードバックを適用します"
   echo ""
   
   # Actual Claude Code Task tool invocation with hybrid approach
   # Task tool execution with comprehensive prompt
   task_prompt="タスクを実行してください。

## コンテキスト情報の取得
1. 一時コンテキスト（プロジェクト情報）:
   - /workspace/.claude/context/current-command-context.json を読み込み

2. プロジェクト状況の確認:
   - 必要な文書やファイルを確認
   - 既存の実装や設計を参照

## 実行タスク
[14-apply-feedback固有のタスクを実行]

## 重要: 標準化出力形式の遵守
レポートは必ず以下の構造化セクションで終了してください：

### 📊 実行サマリー
各Critical Taskの完了状態を✅/❌で明記

### 📋 総合判定
APPROVED/CONDITIONAL_APPROVAL/REJECTED/COMPLETED のいずれかを明記

### 💡 次のステップ
判定に基づく具体的なアクションアイテムを列挙

## 処理完了後
- 実行結果の報告
- 次のステップへの案内"

   # Execute with specialized 14-apply-feedback subagent
   # The 14-apply-feedback subagent will be automatically invoked based on the task description
   
   agent_exit_code=$?
   echo "✅ 専用エージェント実行完了 (終了コード: $agent_exit_code)"
   
   echo "✅ エージェント呼び出し設定完了"
   echo "エージェントが以下の処理を実行します:"
   echo "  - コンテキストファイルからのイシュー情報取得"
   echo "  - レビューフィードバック分析と優先度付け"
   echo "  - 全レイヤーでの体系的フィードバック実装"
   echo "  - コード品質改善とリファクタリング"
   echo "  - アーキテクチャ準拠性修正"
   echo "  - テストカバレッジ向上とシナリオ整合"
   echo "  - ドキュメント更新と改善"
   ```

3. **Agent Result Verification**:
   ```bash
   # 🔍 Verify agent execution results
   echo "🔍 エージェント実行結果を検証中..."
   
   # Check that improvements were implemented
   git_changes=$(git status --porcelain 2>/dev/null | wc -l)
   
   # Validate feedback application results
   if [[ $git_changes -eq 0 ]]; then
       echo "❌ エージェント実行検証失敗:"
       echo "  フィードバック適用による変更が見つかりません"
       exit 1
   fi
   
   echo "✅ エージェント実行結果検証完了"
   
   # 🔧 Load advanced task verification library
   source "$(dirname "${BASH_SOURCE[0]}")/_task_verification.sh"
   
   # ✨ New: Advanced task verification with retry capability
   echo "🔍 Critical tasks確認中..."
   if ! verify_critical_tasks "14-apply-feedback" "$latest_report"; then
       echo "⚠️ Critical tasks確認で問題が検出されました - 再実行を試行します"
       prepare_retry_context "14-apply-feedback" "1" "${verification_issues[@]}"
       
       # Enhanced context for retry
       echo "🔄 再実行用の強化コンテキスト準備中..."
       prepare_enhanced_context "14-apply-feedback" "$context_file" "${verification_issues[@]}"
       
       echo "💡 推奨アクション: エージェントを再実行してください"
       echo "   重点項目: $(IFS='|'; echo "${verification_issues[*]}")"
       exit 1
   fi
   
   echo "✅ Critical tasks確認完了 - 全項目クリア"
   echo "  - 実装された変更: ${git_changes}個のファイル"
   ```

4. **Display Success Summary**:
   ```bash
   # 📊 Display comprehensive success summary
   echo ""
   echo "🎉 フィードバック適用完了!"
   echo "========================"
   
   # Show summary information
   echo "📊 適用サマリー:"
   echo "  🔄 対象Issues: $(printf '#%s ' "${ISSUES[@]}")"
   echo "  📝 変更ファイル: ${git_changes}個"
   echo ""
   echo "📋 次のステップ:"
   echo "   1. テスト実行: /run-all-tests $1"
   echo "   2. プルリクエスト作成: /create-pr $1"
   echo "   3. ステータス確認: /use-case-status"
   echo ""
   echo "✅ フィードバック適用完了 - プルリクエスト作成準備完了!"
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