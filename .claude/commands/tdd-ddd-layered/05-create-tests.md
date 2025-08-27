Use the 05-create-tests subagent to create TDD tests based on Given-When-Then specifications and domain model. This command MUST USE PROACTIVELY the specialized 05-create-tests subagent for optimal test creation implementation.

**📖 Required Reading**: Before execution, this command MUST read the following files:
- `/workspace/.claude/context/current-command-context.json` - Current execution context
- `/workspace/.claude/context/project-context.json` - Overall project state and active sprint information
- `/workspace/docs/use_cases/issue-X-Y.md` - Use case specifications for test creation
- `/workspace/docs/domain/issue-X-Y-domain-model.md` - Domain model design for test implementation
- `/workspace/docs/metadata/project-state.json` - Integrated project status for update

## 🎯 **TDD/DDD/LAYERED PROCESS CONTEXT**

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → **Design Review(04.5)** → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Sprint Execution Phase - TDD Test Creation (05/16)  
> 🎯 **Phase Purpose**: Create failing tests from Given-When-Then scenarios (RED)  
> ⬅️ **Previous Stage**: 04-domain-modeling (Domain Model Design)  
> ➡️ **Next Stage**: 06-implement-domain (Domain Layer Implementation)
>
> **📋 3-Layer Architecture Operations**:  
> - 🎯 **Strategic**: `docs/use_cases/core/index.md` (Reference core scenarios)  
> - 📊 **Tactical**: `docs/use_cases/index.md` (Update TDD RED phase status)  
> - 🔧 **Execution**: `docs/use_cases/issue-X-Y.json` (Track test creation details)

## 🔴 **TDD RED PHASE: FAILING TESTS ONLY**

**⚠️ Important Notice:**
- **This step is TDD RED PHASE** - Create failing tests based on specifications
- **CREATE FAILING TESTS ONLY** - Do not implement any production code  
- **TDD Discipline** - Tests must fail initially to validate TDD cycle
- **No implementation allowed** - Production code comes in next step

**TDD Cycle Position:**
1. `04-domain-modeling` ← Design documentation
2. `05-create-tests` ← **【YOU ARE HERE】TDD RED (failing tests)**
3. `06-implement-domain` ← TDD GREEN (make tests pass)
4. `11-refactor` ← TDD REFACTOR (improve code quality)

**Essential TDD Rules:**
- ✅ Write failing tests that capture specifications
- ❌ Do not write any implementation code
- ✅ Verify all tests fail (RED phase confirmation)

## 📋 **TDD RED PHASE TASK CHECKLIST**

**Use this checklist to create comprehensive failing tests:**

### 🔴 Required Tasks

#### **📖 Specification Analysis**
- [ ] **Read use case specifications**: Parse Given-When-Then scenarios from issue-X-Y.md
- [ ] **Read domain model design**: Extract entity and behavior expectations from design docs
- [ ] **Map scenarios to test cases**: Convert each Given-When-Then to specific test methods
- [ ] **Extract acceptance criteria**: Convert acceptance criteria into testable assertions

#### **🔴 Failing Test Implementation**
- [ ] **Write domain entity tests**: Test entity creation, behavior, and invariants (must fail)
- [ ] **Write value object tests**: Test immutability, validation, and equality (must fail)
- [ ] **Write domain service tests**: Test business logic and rules enforcement (must fail)
- [ ] **Write application service tests**: Test use case orchestration (must fail)

#### **🔍 RED Phase Validation**
- [ ] **Run all tests**: Execute complete test suite using pytest
- [ ] **Verify all tests fail**: Confirm every test fails due to missing implementation
- [ ] **Update metadata**: Mark TDD RED phase as complete in issue-X-Y.json
- [ ] **Commit failing tests**: Version control all test code with clear commit message

### 🟡 Recommended Tasks

#### **🏗️ Test Structure Design**
- [ ] **Design unit tests**: Plan tests for individual entities, value objects, and domain services
- [ ] **Design integration tests**: Plan tests for repository interfaces and application services
- [ ] **Design e2e tests**: Plan tests for complete user scenarios through presentation layer
- [ ] **Plan test organization**: Structure test files following src/ directory hierarchy
- [ ] **Design test naming**: Use descriptive names that capture business intent

#### **🧪 Test Infrastructure Setup**
- [ ] **Create test fixtures**: Design test data and object factories
- [ ] **Create mock objects**: Design mocks for external dependencies and repositories
- [ ] **Set up test configuration**: Configure pytest settings and test database if needed
- [ ] **Create test utilities**: Build helper functions for common test operations

### 🟢 Optional Tasks

#### **📋 Advanced Test Coverage**
- [ ] **Write repository interface tests**: Test data access contracts (must fail)
- [ ] **Write presentation tests**: Test API endpoints and input validation (must fail)
- [ ] **Identify test boundaries**: Determine unit vs integration vs e2e test placement
- [ ] **Set up test isolation**: Ensure tests are independent and repeatable

#### **📊 Phase Completion & Handoff**
- [ ] **Check test coverage**: Ensure all Given-When-Then scenarios have corresponding tests
- [ ] **Validate test quality**: Ensure tests are readable, maintainable, and focused
- [ ] **Document test implementation**: Create test plan documentation
- [ ] **Document test execution**: Record test run results and failure reasons
- [ ] **Prepare for GREEN phase**: Ensure tests clearly define what needs to be implemented
- [ ] **Confirm NO production code**: Verify absolutely no implementation code was written

**💡 Pro Tip**: All tests MUST fail at this stage - if a test passes, you've accidentally implemented something!  
- ✅ Ensure all tests fail (RED phase)
- ❌ Do not make tests pass yet

**CREATE FAILING TESTS ONLY.**

## Task Details

**🤖 Agent Integration**: This command MUST USE PROACTIVELY the specialized `05-create-tests` subagent for optimal TDD RED phase implementation.
 Claude Code should automatically delegate this task to the 05-create-tests subagent based on the command description.

## 📖 Subagent Document Reading Instructions

This command delegates to the specialized `05-create-tests` subagent.

**MANDATORY: The subagent MUST read these files before execution:**

1. `docs/index.md` - Project overview and current status
2. `.claude/context/project-context.json` - Current project context
3. `/workspace/.claude/context/current-command-context.json` - Current execution context (includes issue numbers)
4. `docs/use_cases/issue-X-Y.md` - Use case specifications with Given-When-Then scenarios
5. `docs/domain/issue-X-Y-domain-model.md` - Domain model design for test structure
6. `docs/vision/project-vision.md` - Project vision for understanding requirements
7. Any existing test files in `tests/` - For pattern consistency and test structure
8. `docs/use_cases/index.md` - Current implementation status for context

**Command-Specific Reading Focus - TDD Test Creation:**
- Convert Given-When-Then scenarios into comprehensive test cases
- Use domain model design to structure entity and value object tests
- Create failing tests that clearly specify expected behavior
- Design test mocks and fixtures based on domain boundaries
- Ensure test independence and proper isolation of external dependencies

**CRITICAL:** Use the Read tool to actually read file contents, not just reference paths.

**Additional Context for Subagent Execution:**
- `docs/index.md` - Project navigation and status overview for understanding test creation context
- Existing test patterns and conventions in `tests/` directory for maintaining consistent test structure
- Testing strategy documentation to align test implementation with project testing approach
- Domain model design patterns to structure tests appropriately for entities and value objects
- IMPORTANT: Use Read tool to access actual file contents, not just references

1. **Pre-execution Validation**:
   ```bash
   # Validate issue number requirement
   if [[ $# -eq 0 ]]; then
       echo "エラー: 少なくとも1つのイシュー番号を指定してください"
       echo "使用例: /create-tests 1"
       echo "使用例: /create-tests 1,7 (複数イシュー)"
       exit 1
   fi
   
   # Extract issue numbers from arguments
   issue_numbers=()
   feature_name=""
   
   # Parse first argument for issue numbers
   IFS=',' read -ra ISSUE_ARRAY <<< "$1"
   for issue in "${ISSUE_ARRAY[@]}"; do
       if [[ "$issue" =~ ^[0-9]+$ ]]; then
           issue_numbers+=("$issue")
       fi
   done
   
   # Optional feature name from second argument
   if [[ $# -gt 1 ]]; then
       feature_name="$2"
   fi
   
   echo "🧪 Issues: $(printf '#%s ' "${issue_numbers[@]}")のTDDテスト作成を開始します（RED phase）"
   ```

2. **Context Preparation and Agent Execution**:
   ```bash
   # 🔄 Prepare context for agent (Pattern B: Hybrid approach)
   echo "🧪 コンテキスト準備とエージェント起動..."
   
   # Create context file with TDD test creation information
   context_file="/workspace/.claude/context/current-command-context.json"
   current_time=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
   
   # Build context JSON for TDD test creation
   cat > "$context_file" <<EOF
   {
     "command": "create-tests",
     "timestamp": "$current_time",
     "issue_numbers": [$(IFS=,; echo "${issue_numbers[*]}")],
     "feature_name": "$feature_name",
     "phase": "tdd-red-phase",
     "context": {
       "expected_outputs": [
         "tests/domain/test_issue_X_Y.py",
         "tests/application/test_issue_X_Y.py",
         "tests/integration/test_issue_X_Y.py"
       ],
       "architecture_patterns": ["TDD", "DDD", "Clean Architecture"]
     },
     "additional_instructions": "TDD REDフェーズの失敗テストを作成してください。Given-When-Thenシナリオを適切なテストケースに変換し、ドメイン駆動の原則に従ったテスト構造を設計してください。外部依存関係は適切にモック化し、テストの独立性を保証してください。",
     "special_considerations": [
       "既存のユースケース仕様（docs/use_cases/issue-X-Y.md）の完全なカバレッジ",
       "ドメインモデル（docs/domain/issue-X-Y.md）との整合性確認",
       "TDD REDフェーズの確実な実行（全テスト失敗状態）",
       "テストデータとモックの適切な設計"
     ],
     "custom_context": {
       "tdd_red_phase": true,
       "domain_driven_tests": true,
       "mock_external_dependencies": true,
       "test_independence": true
     }
   }
   EOF
   
   echo "✅ コンテキストファイル作成完了: $context_file"
   
   # 🤖 Call the specialized agent with hybrid context
   echo ""
   echo "🧪 TDDテスト作成エージェントを起動します..."
   echo "専門エージェントがTDD RED フェーズの失敗テストを作成します"
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
[05-create-tests固有のタスクを実行]

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

   # Execute with specialized 05-create-tests subagent
   # The 05-create-tests subagent will be automatically invoked based on the task description
   
   agent_exit_code=$?
   echo "✅ 専用エージェント実行完了 (終了コード: $agent_exit_code)"
   
   echo "✅ エージェント呼び出し設定完了"
   echo "エージェントが以下の処理を実行します:"
   echo "  - コンテキストファイルからのイシュー情報取得"
   echo "  - ユースケース仕様の分析とテストシナリオの抽出"
   echo "  - Given-When-Thenシナリオのテストケースへの変換"
   echo "  - ドメイン駆動のテスト構造とファイル編成の作成"
   echo "  - 外部依存関係のモック・スタブ設定"
   echo "  - テストデータ準備とテストヘルパーユーティリティの作成"
   echo "  - TDD REDフェーズの検証（全テスト失敗確認）"
   echo "  - 失敗テストの実行確認（TDD RED段階）"
   echo "  - メタデータ更新とGitコミット"
   ```

3. **Agent Result Verification**:
   ```bash
   # 🔍 Verify agent execution results
   echo "🔍 エージェント実行結果を検証中..."
   
   # Check that test files were created by the agent
   echo "  🔍 テストファイルの作成確認中..."
   
   # Check for test directory structure
   test_dirs=(
       "tests/unit"
       "tests/integration"
       "tests/e2e"
   )
   
   # Validate test structure was created
   missing_test_dirs=()
   for dir in "${test_dirs[@]}"; do
       if [[ ! -d "$dir" ]]; then
           missing_test_dirs+=("$dir")
       fi
   done
   
   # Check for test files related to issues
   test_files_found=0
   for issue_num in "${issue_numbers[@]}"; do
       # Look for test files mentioning the issue
       if find tests/ -name "*.py" -type f -exec grep -l "issue.*$issue_num\|#$issue_num" {} \; 2>/dev/null | head -1 >/dev/null; then
           echo "    ✅ Issue #$issue_num のテストファイルを確認しました"
           ((test_files_found++))
       else
           echo "    ⚠️ Issue #$issue_num のテストファイルが見つかりません"
       fi
   done
   
   # Report validation results
   if [[ ${#missing_test_dirs[@]} -gt 0 ]] || [[ $test_files_found -eq 0 ]]; then
       echo "❌ エージェント実行検証失敗:"
       if [[ ${#missing_test_dirs[@]} -gt 0 ]]; then
           echo "  未作成テストディレクトリ: ${missing_test_dirs[*]}"
       fi
       if [[ $test_files_found -eq 0 ]]; then
           echo "  テストファイルが作成されていません"
       fi
       exit 1
   fi
   
   echo "✅ エージェント実行結果検証完了"
   
   # 🔧 Load advanced task verification library
   source "$(dirname "${BASH_SOURCE[0]}")/_task_verification.sh"
   
   # ✨ New: Advanced task verification with retry capability
   echo "🔍 Critical tasks確認中..."
   if ! verify_critical_tasks "05-create-tests" "$latest_report"; then
       echo "⚠️ Critical tasks確認で問題が検出されました - 再実行を試行します"
       prepare_retry_context "05-create-tests" "1" "${verification_issues[@]}"
       
       # Enhanced context for retry
       echo "🔄 再実行用の強化コンテキスト準備中..."
       prepare_enhanced_context "05-create-tests" "$context_file" "${verification_issues[@]}"
       
       echo "💡 推奨アクション: エージェントを再実行してください"
       echo "   重点項目: $(IFS='|'; echo "${verification_issues[*]}")"
       exit 1
   fi
   
   echo "✅ Critical tasks確認完了 - 全項目クリア"
   
   # Clean up context file after successful execution
   if [[ -f "$context_file" ]]; then
       # Archive context to execution history
       echo "{\"timestamp\":\"$(date -Iseconds)\",\"command\":\"create-tests\",\"issues\":\"${issue_numbers[*]}\",\"status\":\"completed\"}" >> /workspace/.claude/context/execution-history.jsonl
       rm -f "$context_file"
       echo "📝 コンテキストを実行履歴に記録し、一時ファイルをクリーンアップしました"
   fi
   ```

4. **Display TDD RED Phase Success Summary**:
   ```bash
   # 📊 Display comprehensive TDD RED phase summary
   echo ""
   echo "🎉 TDDテスト作成完了（RED phase）!"
   echo "============================================="
   
   # Show created test files
   echo "📁 作成されたテストファイル:"
   if find tests/ -name "test_*.py" -type f >/dev/null 2>&1; then
       test_count=$(find tests/ -name "test_*.py" -type f | wc -l)
       echo "   ✅ テストファイル: ${test_count} 個"
       find tests/ -name "test_*.py" -type f | head -5 | while read -r file; do
           echo "      - $file"
       done
       if [[ $test_count -gt 5 ]]; then
           echo "      - ... (他 $((test_count - 5)) ファイル)"
       fi
   else
       echo "   ⚠️ テストファイルが見つかりません"
   fi
   
   # Show test verification
   echo ""
   echo "🔴 TDD RED状態確認:"
   echo "   - すべてのテストが失敗（実装前のため正常）"
   echo "   - Given-When-Thenシナリオからテスト自動生成"
   echo "   - ドメインモデルに基づくエンティティテスト"
   echo "   - アプリケーションユースケーステスト"
   
   echo ""
   echo "📋 次のステップ (TDD GREEN phase):"
   for issue_num in "${issue_numbers[@]}"; do
       echo "   /implement-domain $issue_num"
   done
   
   echo ""
   echo "📚 重要ドキュメント:"
   echo "   - テスト計画: docs/test_plan/"
   echo "   - ドメインモデル: docs/domain/"
   echo "   - ユースケース仕様: docs/use_cases/"
   echo ""
   echo "✅ TDD RED段階完了 - 実装準備完了!"
   ```

## Common Errors and Solutions

### ❌ Error Case 1: Missing use case specifications
**Cause**: Use case specifications not created for the issue  
**Solution**: 
```bash
/create-use-case <issue-number>
```

### ❌ Error Case 2: Missing domain model
**Cause**: Domain model design not completed  
**Solution**: 
```bash
/domain-modeling <issue-number>
```

### ❌ Error Case 3: Tests already exist
**Cause**: Tests already created for this issue  
**Solution**: Choose to overwrite or work on different issue

## Execution Examples

### ✅ Success Example
```bash
$ /create-tests 15
🧪 Issues: #15 のTDDテスト作成を開始します（RED phase）
🤖 TDDテスト作成エージェントを起動します...
✅ エージェント実行結果検証完了
🎉 TDDテスト作成完了（RED phase）!
```

### ❌ Failure Example and Fix
```bash
$ /create-tests 15
❌ エラー: Issue #15 のユースケース仕様が見つかりません

# Fix: Create use case specification first
$ /create-use-case 15
```

## 🔄 **PHASE 3: ENHANCED INTEGRATION CAPABILITIES**

### **Critical Enhancement Features**
This command implements Phase 3 advanced integration and test creation capabilities:

1. **Coverage Gap Analysis**: Intelligent test coverage analysis with automated gap detection and priority assessment
2. **Test Quality Optimization**: Smart test quality assessment with maintainability and reliability scoring
3. **TDD Alignment Verification**: Automated verification of TDD RED-GREEN-REFACTOR cycle compliance
4. **Automation Enhancement**: Advanced test automation with CI/CD pipeline integration and quality gates

### **Project State Updates**

**CRITICAL**: After successful test creation completion, MUST update integrated project metadata:

#### Project State Updates (`docs/metadata/project-state.json`)
```json
{
  "project_metadata": {
    "overall_status": "tdd_red_phase_completed",
    "health_score": "RECALCULATE_WITH_TEST_METRICS",
    "last_updated": "CURRENT_TIMESTAMP"
  },
  "architecture_overview": {
    "test_layer": {
      "unit_tests": "UPDATE_UNIT_TEST_COUNT",
      "integration_tests": "UPDATE_INTEGRATION_TEST_COUNT",
      "e2e_tests": "UPDATE_E2E_TEST_COUNT",
      "test_coverage_percentage": "UPDATE_COVERAGE_METRICS"
    }
  },
  "workflow_statistics": {
    "command_execution_stats": {
      "total_command_executions": "INCREMENT_BY_1",
      "create_tests_completions": "INCREMENT_BY_1"
    },
    "subagent_performance": {
      "most_active_agents": "UPDATE_WITH_05_CREATE_TESTS_SUBAGENT"
    }
  },
  "recent_activity": {
    "last_command_executed": "create-tests",
    "last_metadata_update": "CURRENT_TIMESTAMP"
  }
}
```

#### Context File Updates (`.claude/context/project-context.json`)
```json
{
  "current_state": {
    "last_command": "create-tests",
    "last_command_timestamp": "CURRENT_TIMESTAMP"
  },
  "workflow_tracking": {
    "command_usage": {
      "create_tests": "INCREMENT_USAGE_COUNT"
    }
  },
  "test_status": {
    "tdd_red_phase": "completed",
    "test_files_created": "UPDATE_TEST_FILE_LIST",
    "scenario_coverage": "UPDATE_SCENARIO_COVERAGE",
    "quality_score": "UPDATE_TEST_QUALITY_METRICS"
  }
}
```

#### System Integration Updates (`.claude/context/system-integration.json`)
```json
{
  "real_time_metrics": {
    "current_session": {
      "commands_executed": "INCREMENT_BY_1",
      "metadata_syncs": "INCREMENT_BY_1",
      "test_suites_created": "INCREMENT_BY_1"
    }
  },
  "test_quality": {
    "tdd_compliance_score": "UPDATE_TDD_COMPLIANCE",
    "scenario_test_alignment": "UPDATE_ALIGNMENT_METRICS",
    "automation_coverage": "UPDATE_AUTOMATION_METRICS"
  }
}
```

**⚠️ Error Handling**: If standard workflow is disrupted:
- 📖 Consult: [Manual Sync Guide](../../docs/maintenance/manual-sync-guide.md)
- 🔄 Check Status: `/use-case-status` for current project state
- 📊 Verify Context: `.claude/context/current-command-context.json`