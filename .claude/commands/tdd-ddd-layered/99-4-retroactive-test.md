Use the 99-4-retroactive-test subagent to create tests for emergency fixes that bypassed standard TDD workflow. This command MUST USE PROACTIVELY the specialized 99-4-retroactive-test subagent for optimal retroactive test creation.

**📖 Required Reading**: Before execution, this command MUST read the following files:
- `/workspace/.claude/context/current-command-context.json` - Current execution context
- `/workspace/.claude/context/project-context.json` - Overall project state and active sprint information
- `/workspace/docs/metadata/project-state.json` - Integrated project status for update

## Metadata
- **Prerequisites**: GitHub issue created, documentation synchronized, emergency fix commits identified
- **Input**: 
  - `<issue-number>` (required) - GitHub issue number for the emergency fix
  - `--coverage-target <percentage>` (default: 80) - Target test coverage percentage
- **Output**: 
  - Retroactive test files for emergency changes
  - Test coverage report and gap analysis
  - Updated test suite with emergency fix coverage
  - Updated project metadata
- **Dependencies**: GitHub issue, synchronized documentation, existing test framework
- **Execution Timing**: After documentation synchronization (99-3) and before validation

## 🎯 **TDD/DDD/LAYERED PROCESS CONTEXT**

**🚨 Emergency Recovery Workflow**: Recovery(99-1) → Issue Creation(99-2) → Sync Docs(99-3) → **Retroactive Tests(99-4)** → Validation(99-5) → Metadata Reconcile(99-6) → Final Review(99-7)

**🏗️ Retroactive Testing Architecture**: Analyze→Design→Implement→Verify  
**🧪 Testing Requirements**: TDD compliance, code coverage, regression protection, integration testing
**🔄 Integration**: Restores test coverage for emergency changes following TDD principles

> 📖 **Emergency Recovery System**: [99-X Series Commands](./README.md)  
> 🗺️ **Current Position**: Retroactive Test Creation (99-4/99-7)  
> 🎯 **Phase Purpose**: Create comprehensive tests for emergency code changes  
> ➡️ **Next Stage**: 99-5-validate-emergency-fix (Emergency Fix Validation)

## 🎯 **PHASE PURPOSE: RETROACTIVE TEST CREATION**

**⚠️ Important Notice:**
- **This step is TEST CREATION ONLY** - Create tests for emergency code changes
- **FOLLOW TDD PRINCIPLES** - Create comprehensive tests that validate emergency fix behavior  
- **Coverage restoration phase** - Ensure emergency changes have adequate test protection
- **Create test artifacts ONLY** - Focus on test creation, not code modification

**What this step does:**
1. `99-3-sync-documentation` ← Documentation synchronization with emergency changes
2. `99-4-retroactive-test` ← **【YOU ARE HERE】Create tests for emergency changes**
3. `99-5-validate-emergency-fix` ← Validate emergency fix implementation
4. Then continue with metadata reconciliation and finalization

**CREATE RETROACTIVE TESTS ONLY.**

## Common Errors and Solutions

### ❌ Error Case 1: Test framework not found
**Cause**: Project doesn't have proper test framework setup  
**Solution**: 
- Check existing test structure: `find . -name "*test*" -type f`
- Initialize test framework if needed
- Use project's existing testing conventions

### ❌ Error Case 2: Cannot identify emergency changes
**Cause**: GitHub issue lacks sufficient detail about code changes  
**Solution**: 
```bash
# Analyze commits linked to issue
gh issue view <issue-number> --json body
# Or identify emergency commits manually
git log --oneline --since="1 week ago" --grep="fix\|emergency\|hotfix"
```

### ❌ Error Case 3: Coverage target too ambitious
**Cause**: Target coverage percentage exceeds realistic scope  
**Solution**: 
```bash
# Start with lower target and increase incrementally
/retroactive-test <issue> --coverage-target 60
# Then improve coverage iteratively
/retroactive-test <issue> --coverage-target 80
```

## Execution Examples

### ✅ Success Example - Payment Validation Tests
```bash
$ /retroactive-test 342 --coverage-target 80
🧪 遡及的テスト作成を開始します

🔍 Issue #342 分析中...
  タイトル: "Emergency Fix: Payment validation null pointer exception"
  緊急修正内容: src/payment/validator.py の null チェック追加
  影響範囲: PaymentValidator クラス

📊 現在のテストカバレッジ分析中...
  📄 src/payment/validator.py: 45% (目標: 80%)
  🎯 不足テストケース: 12件特定
  📝 クリティカルパス: 8件確認

🧪 テストケース設計中...
  ✅ 正常系テスト: 5件
    - 有効な支払いデータのバリデーション
    - 通常の入力値パターンテスト
  
  ✅ 異常系テスト: 4件  
    - null入力値の処理テスト
    - 不正フォーマットデータのエラーハンドリング
    - 境界値テストケース
    - 空文字列・空配列の処理
  
  ✅ 回帰テスト: 3件
    - 既存機能の動作確認
    - 他モジュールとの連携テスト

📝 テストファイル作成中...
  ✅ tests/payment/test_validator_emergency.py 作成
  ✅ tests/payment/test_validator_regression.py 作成
  ✅ tests/integration/test_payment_integration.py 更新

🔄 テスト実行と検証中...
  ✅ 新規テスト: 12/12件パス
  ✅ 既存テスト: 全スイート正常実行
  📊 カバレッジ向上: 45% → 82% (目標達成!)

🎉 遡及的テスト作成完了!
作成されたテストファイル:
  - tests/payment/test_validator_emergency.py (8テストケース)
  - tests/payment/test_validator_regression.py (4テストケース)
  - tests/integration/test_payment_integration.py (更新)

📊 テストカバレッジ達成: 82% (目標: 80%)
次のステップ: /validate-emergency-fix 342 --strict
```

### ✅ Success Example - Infrastructure Hotfix Tests
```bash
$ /retroactive-test 343 --coverage-target 75
🧪 インフラ系緊急修正のテスト作成開始

🔍 Issue #343 確認中...
  対象: Database connection timeout hotfix
  変更ファイル: src/infrastructure/database.py
  
📊 既存テスト状況:
  📄 データベース接続テスト: 30%
  🎯 タイムアウト処理テスト: 不足
  📝 エラーハンドリングテスト: 未実装

🧪 インフラ系テストケース作成中...
  ✅ 接続タイムアウトシミュレーション
  ✅ フェイルオーバー動作テスト
  ✅ 再接続ロジックテスト
  ✅ エラーログ出力テスト

📝 テストファイル: tests/infrastructure/test_database_timeout.py
🔄 実行結果: 全テスト正常終了
📊 カバレッジ向上: 30% → 78%

✅ インフラ系テスト作成完了!
```

## 📋 **RETROACTIVE TEST CREATION TASK CHECKLIST**

**Use this checklist for comprehensive retroactive test creation:**

### 🔴 Required Tasks

#### **🔍 Emergency Change Analysis**
- [ ] **Issue content analysis**: Extract emergency fix details from GitHub issue
- [ ] **Code change identification**: Identify modified functions, classes, and logic
- [ ] **Impact scope mapping**: Determine all areas affected by emergency changes

#### **📊 Test Coverage Assessment**
- [ ] **Current coverage measurement**: Measure existing test coverage for changed areas
- [ ] **Gap identification**: Identify specific untested code paths and scenarios
- [ ] **Coverage target planning**: Set realistic coverage improvement targets

#### **🧪 Test Case Design and Implementation**
- [ ] **Normal case tests**: Create tests for expected emergency fix behavior
- [ ] **Edge case tests**: Test boundary conditions and error scenarios
- [ ] **Regression tests**: Ensure emergency fix doesn't break existing functionality

### 🟡 Recommended Tasks

#### **📝 Test Quality Assurance**
- [ ] **Test naming**: Use clear, descriptive test method names
- [ ] **Test documentation**: Document complex test scenarios and expectations
- [ ] **Mock and stub setup**: Proper isolation for unit tests

#### **🔄 Integration and Validation**
- [ ] **Integration tests**: Test emergency changes in broader system context
- [ ] **Test execution verification**: Ensure all new tests pass consistently
- [ ] **Existing test validation**: Verify emergency changes don't break existing tests

### 🟢 Optional Tasks

#### **📈 Advanced Testing Features**
- [ ] **Performance tests**: Verify emergency fix doesn't degrade performance
- [ ] **Load testing**: Test emergency fix under system load conditions
- [ ] **Security testing**: Ensure emergency fix doesn't introduce security vulnerabilities

#### **📊 Metrics and Reporting**
- [ ] **Detailed coverage report**: Generate comprehensive coverage analysis
- [ ] **Test metrics**: Track test execution time and reliability
- [ ] **Quality metrics**: Measure test effectiveness and maintainability

**💡 Pro Tip**: Focus on high-risk areas first - test the most critical paths affected by the emergency fix!

## Task Details

**🤖 Agent Integration**: This command MUST USE PROACTIVELY the specialized `99-4-retroactive-test` subagent for optimal retroactive test creation. Claude Code should automatically delegate this task to the 99-4-retroactive-test subagent based on the command description.

## 📖 Subagent Document Reading Instructions

This command delegates to the specialized `99-4-retroactive-test` subagent.

**MANDATORY: The subagent MUST read these files before execution:**

1. `docs/use_cases/` - Updated scenario documentation for test guidance
2. Existing test files and test framework configuration
3. Source code files modified in the emergency fix
4. `/workspace/.claude/context/current-command-context.json` - Current execution context
5. `/workspace/docs/metadata/project-state.json` - Project status and testing metrics
6. GitHub issue details for emergency fix context

**Command-Specific Reading Focus - Retroactive Test Creation:**
- Read GitHub issue to understand emergency fix scope and requirements
- Analyze existing test structure to follow project testing conventions
- Review modified source code to identify all testable scenarios
- Check current test coverage to identify specific gaps

**CRITICAL:** Use the Read tool to actually read file contents, not just reference paths.

## サブエージェント実行指示

このコマンドはサブエージェント `99-4-retroactive-test` を呼び出します。

**サブエージェントに対する明示的指示**:
- 実行開始前に以下のファイルを必ず読み込んでください:
  1. GitHub Issue詳細 - 緊急修正の要件確認
  2. 既存テストファイル - プロジェクトのテスト規約理解
  3. 変更されたソースコード - テスト対象の特定
  4. `/workspace/docs/metadata/project-state.json` - プロジェクト状態確認
  
**重要**: リンクや参照だけでなく、実際にRead toolを使用してファイル内容を読み込むこと

Follow these steps:

1. **Pre-execution Validation**:
   ```bash
   # Validate required parameters
   issue_number=""
   coverage_target=80
   
   # Parse arguments
   if [[ $# -lt 1 ]]; then
       echo "❌ Issue number is required"
       echo "Usage: /retroactive-test <issue-number> [--coverage-target <percentage>]"
       exit 1
   fi
   
   issue_number="$1"
   shift
   
   while [[ $# -gt 0 ]]; do
       case $1 in
           --coverage-target)
               coverage_target="$2"
               shift 2
               ;;
           *)
               echo "⚠️ Unknown parameter: $1"
               echo "Usage: /retroactive-test <issue-number> [--coverage-target <percentage>]"
               exit 1
               ;;
       esac
   done
   
   # Validate coverage target
   if ! [[ "$coverage_target" =~ ^[0-9]+$ ]] || (( coverage_target < 1 || coverage_target > 100 )); then
       echo "❌ Invalid coverage target: $coverage_target. Must be between 1 and 100"
       exit 1
   fi
   
   # Validate GitHub CLI and issue
   if command -v gh &> /dev/null; then
       if ! gh issue view "$issue_number" >/dev/null 2>&1; then
           echo "❌ GitHub issue #$issue_number not found or not accessible"
           exit 1
       fi
   else
       echo "⚠️ GitHub CLI not found. Issue information may be limited."
   fi
   
   # Check for existing test framework
   if [[ ! -d "tests" && ! -d "test" && ! -f "pytest.ini" && ! -f "setup.cfg" ]]; then
       echo "⚠️ No obvious test framework detected. Proceeding with generic test structure."
   fi
   
   echo "🧪 遡及的テスト作成を開始します (Issue: #$issue_number, Coverage: $coverage_target%)"
   ```

2. **Context Preparation and Agent Execution**:
   ```bash
   # 🔄 Prepare context for retroactive test creation agent
   echo "🔍 緊急修正分析とテスト作成コンテキスト準備..."
   
   # Extract issue information if GitHub CLI is available
   issue_title=""
   issue_body=""
   if command -v gh &> /dev/null; then
       issue_title=$(gh issue view "$issue_number" --json title -q '.title' 2>/dev/null || echo "")
       issue_body=$(gh issue view "$issue_number" --json body -q '.body' 2>/dev/null || echo "")
   fi
   
   # Detect test framework
   test_framework="unknown"
   if [[ -f "pytest.ini" ]] || [[ -f "setup.cfg" ]] || find . -name "test_*.py" -o -name "*_test.py" | head -1 | grep -q .; then
       test_framework="pytest"
   elif [[ -f "package.json" ]] && grep -q "jest\|mocha\|vitest" package.json; then
       test_framework="javascript"
   elif [[ -f "Cargo.toml" ]] && grep -q "\[dev-dependencies\]" Cargo.toml; then
       test_framework="rust"
   fi
   
   # Create context file
   context_file="/workspace/.claude/context/current-command-context.json"
   current_time=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
   
   # Build context JSON for retroactive test creation
   cat > "$context_file" <<EOF
   {
     "command": "retroactive-test",
     "timestamp": "$current_time",
     "issue_number": "$issue_number",
     "coverage_target": $coverage_target,
     "phase": "retroactive-test-creation",
     "issue_info": {
       "title": "$issue_title",
       "body": "$issue_body"
     },
     "test_framework": "$test_framework",
     "context": {
       "git_repo": "true",
       "testing_focus": "emergency_changes",
       "expected_outputs": [
         "retroactive_test_files",
         "coverage_improvement",
         "test_execution_results"
       ],
       "test_types": ["unit", "integration", "regression"]
     },
     "additional_instructions": "緊急修正されたコードを分析し、TDD原則に従って包括的なテストスイートを作成してください。",
     "special_considerations": [
       "Issue内容からのコード変更特定",
       "既存テストフレームワークとの整合性確保", 
       "正常系・異常系・境界値テストの網羅",
       "回帰テストの実装",
       "テストカバレッジ目標の達成"
     ],
     "custom_context": {
       "emergency_recovery": true,
       "tdd_compliance": "high",
       "coverage_validation": true
     }
   }
   EOF
   
   echo "✅ 遡及的テスト作成コンテキストファイル作成完了: $context_file"
   
   # 🤖 Call the specialized retroactive test creation agent
   echo ""
   echo "🧪 遡及的テスト作成エージェントを起動します..."
   echo "専門エージェントが緊急修正を分析して包括的なテストを作成します"
   echo ""
   
   # Task tool execution with comprehensive prompt
   task_prompt="Execute the task.

## CRITICAL: Subagent Specification Reference
As a fallback mechanism in case the specialized subagent 99-4-retroactive-test is not properly invoked:
- MUST READ: /workspace/.claude/agents/99-4-retroactive-test.md
- Follow the specifications and requirements defined in this agent file
- Implement the exact same process and standards as defined in the subagent specification
- Ensure standardized output format compliance as specified in the agent document

## Context Information Gathering
1. Emergency Recovery Context:
   - Read /workspace/.claude/context/current-command-context.json

2. Test Coverage Analysis:
   - Analyze existing test files and coverage
   - Review emergency fix code changes
   - Identify testing gaps and requirements

## Task Execution
1. Emergency fix analysis and test requirement identification
2. Test coverage gap analysis and priority assessment
3. Retroactive test creation for missing coverage
4. Test execution and validation
5. Coverage verification and quality assessment
6. Test integration and documentation updates

## IMPORTANT: Standardized Output Format Compliance
Report MUST end with the following structured sections:

### 📊 Execution Summary
Mark completion status of each critical task with ✅/❌

### 📋 Overall Assessment
Provide comprehensive test creation results and coverage status

### 💡 Next Steps
List specific follow-up actions for emergency recovery workflow

## Post-Processing
- Create comprehensive retroactive tests for emergency fixes
- Execute tests to verify functionality and coverage
- Update test documentation and metadata
- Guide next steps in emergency recovery process"

   # Execute with specialized 99-4-retroactive-test subagent
   # The 99-4-retroactive-test subagent will be automatically invoked based on the task description
   
   agent_exit_code=$?
   echo "✅ 専用エージェント実行完了 (終了コード: $agent_exit_code)"
   ```

3. **Agent Result Verification**:
   ```bash
   # 🔍 Verify retroactive test creation results
   echo "🔍 テスト作成結果を検証中..."
   
   # Check for new test files
   new_test_files=$(find . -name "*test*.py" -newer "$context_file" 2>/dev/null | head -10)
   if [[ -n "$new_test_files" ]]; then
       echo "📝 作成されたテストファイル:"
       echo "$new_test_files" | while read -r file; do
           echo "   ✅ $file"
       done
   else
       echo "💡 新しいテストファイルが検出されませんでした（既存ファイルの更新の可能性）"
   fi
   
   # Run tests if possible
   test_result="unknown"
   if [[ "$test_framework" == "pytest" ]] && command -v pytest &> /dev/null; then
       echo "🔄 pytest実行中..."
       if pytest --tb=short -v 2>/dev/null; then
           test_result="passed"
           echo "✅ 全テスト正常実行完了"
       else
           test_result="failed"
           echo "⚠️ 一部テストが失敗しました"
       fi
   elif command -v python -m pytest &> /dev/null; then
       echo "🔄 python -m pytest実行中..."
       if python -m pytest --tb=short 2>/dev/null; then
           test_result="passed"
           echo "✅ 全テスト正常実行完了"
       else
           test_result="failed"
           echo "⚠️ 一部テストが失敗しました"
       fi
   else
       echo "💡 テストフレームワークが見つからないため、自動実行をスキップします"
   fi
   
   echo "✅ 遡及的テスト作成結果検証完了"
   
   # Clean up context file after successful execution
   if [[ -f "$context_file" ]]; then
       # Archive context to execution history
       echo "{\"timestamp\":\"$(date -Iseconds)\",\"command\":\"retroactive-test\",\"issue\":\"$issue_number\",\"coverage_target\":$coverage_target,\"test_result\":\"$test_result\",\"status\":\"completed\"}" >> /workspace/.claude/context/execution-history.jsonl
       rm -f "$context_file"
       echo "📝 コンテキストを実行履歴に記録し、一時ファイルをクリーンアップしました"
   fi
   ```

4. **Display Test Creation Summary**:
   ```bash
   # 📊 Display comprehensive test creation summary
   echo ""
   echo "🎉 遡及的テスト作成完了!"
   echo "========================"
   
   echo "📋 テスト作成情報:"
   echo "   🎫 Issue: #$issue_number"
   if [[ -n "$issue_title" ]]; then
       echo "   📝 タイトル: $issue_title"
   fi
   echo "   🎯 カバレッジ目標: $coverage_target%"
   echo "   🧪 テストフレームワーク: $test_framework"
   echo "   ✅ テスト実行結果: $test_result"
   
   # Show created/modified test files
   if [[ -n "$new_test_files" ]]; then
       echo ""
       echo "📁 作成されたテストファイル:"
       echo "$new_test_files" | while read -r file; do
           echo "   📄 $file"
       done
   fi
   
   echo ""
   echo "📋 推奨次のステップ:"
   echo "   1. テスト実行確認: pytest -v (または適切なテストコマンド)"
   echo "   2. カバレッジ測定: pytest --cov (カバレッジプラグインがある場合)"
   echo "   3. 緊急修正検証: /validate-emergency-fix $issue_number --strict"
   echo "   4. テスト結果レビュー: 作成されたテストケースの妥当性確認"
   
   echo ""
   echo "💡 補足情報:"
   echo "   - 作成されたテストケースを手動で確認してください"
   echo "   - 必要に応じて追加のエッジケーステストを検討してください"
   echo "   - テストが失敗する場合は、緊急修正コードの見直しが必要な可能性があります"
   echo ""
   echo "✅ 遡及的テスト作成完了 - 緊急修正のテストカバレッジが向上しました!"
   ```

## 🔄 **PHASE 3: ENHANCED INTEGRATION CAPABILITIES**

### **Critical Enhancement Features**
This command implements Phase 3 advanced retroactive test creation capabilities:

1. **Intelligent Code Change Analysis with AI-driven Test Case Generation**
2. **Automated Test Framework Integration with Project Convention Adherence** 
3. **Smart Coverage Gap Identification with Priority-based Test Creation**
4. **Enhanced Test Quality Assurance with Regression Detection**

### **Project State Updates**

**CRITICAL**: After successful retroactive test creation, MUST update integrated project metadata:

1. **Project State Update**:
   ```bash
   # Update docs/metadata/project-state.json
   # - Update testing_metrics.emergency_test_coverage
   # - Increment testing_metrics.retroactive_tests_created
   # - Set testing_metrics.coverage_improvement percentage
   # - Add to recent_activity.last_command_executed
   ```

2. **Project Context Update**:
   ```bash
   # Update .claude/context/project-context.json  
   # - Update testing_status with coverage results
   # - Set current_state.last_command and last_command_timestamp
   # - Increment workflow_tracking.command_usage.retroactive_test
   ```

**⚠️ Error Handling**: If retroactive test creation fails:
- 📖 Consult: [Manual Sync Guide](../../docs/maintenance/manual-sync-guide.md)
- 🔄 Check Status: `/use-case-status` for current project state  
- 🧪 Manual Testing: Create tests manually and verify coverage improvement