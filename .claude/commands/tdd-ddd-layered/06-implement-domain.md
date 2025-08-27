Use the 06-implement-domain subagent to implement domain layer to make tests pass (TDD GREEN phase). This command MUST USE PROACTIVELY the specialized 06-implement-domain subagent for optimal domain implementation.

**📖 Required Reading**: Before execution, this command MUST read the following files:
- `/workspace/.claude/context/current-command-context.json` - Current execution context
- `/workspace/.claude/context/project-context.json` - Overall project state and active sprint information
- `/workspace/tests/` - All failing test files for implementation guidance
- `/workspace/docs/domain/issue-X-Y-domain-model.md` - Domain design specifications
- `/workspace/docs/use_cases/issue-X-Y.md` - Use case specifications for business logic
- `/workspace/docs/metadata/project-state.json` - Integrated project status for update

## Metadata
- **Prerequisites**: TDD tests created and failing (05-create-tests)
- **Input**: Issue number(s) (required)
- **Output**: 
  - Domain layer implementation in `src/domain/`
  - Updated test results (tests should pass)
  - Updated `docs/use_cases/issue-X-Y.json` metadata
- **Dependencies**: pytest, domain model design documents, Python environment
- **Execution Timing**: TDD GREEN phase - after test creation, before application layer

## 🎯 **TDD/DDD/LAYERED PROCESS CONTEXT**

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Design Review(04.5) → Tests(05) → **Test Review(05.5)** → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Sprint Execution Phase - Domain Layer Implementation (06/16)  
> 🎯 **Phase Purpose**: Implement domain logic to make tests pass (GREEN)  
> ⬅️ **Previous Stage**: 05.5-review-test-design (Test Design Review)  
> ➡️ **Next Stage**: 07-implement-usecase (Application Layer Implementation)
>
> **📋 3-Layer Architecture Operations**:  
> - 🎯 **Strategic**: `docs/use_cases/core/index.md` (Reference domain concepts)  
> - 📊 **Tactical**: `docs/use_cases/index.md` (Update TDD GREEN phase status)  
> - 🔧 **Execution**: `docs/use_cases/issue-X-Y.json` (Track domain implementation)

## 🟢 **TDD GREEN PHASE: MAKE TESTS PASS**

**⚠️ Important Notice:**
- **This step is TDD GREEN PHASE** - Implement minimal code to make tests pass
- **DOMAIN LAYER ONLY** - Implement only domain entities, value objects, and services
- **No external dependencies** - Keep domain pure with no I/O, database, or external calls
- **Minimal implementation** - Write just enough code to make tests pass

**TDD Cycle Position:**
1. `05-create-tests` ← TDD RED (failing tests created)
2. `06-implement-domain` ← **【YOU ARE HERE】TDD GREEN (make tests pass)**
3. `11-refactor` ← TDD REFACTOR (improve code quality)

**Essential TDD Rules:**
- ✅ Make failing tests pass with minimal implementation
- ✅ Keep domain layer pure (no external dependencies)
- ✅ Implement only domain logic (entities, value objects, domain services)
- ❌ Do not implement application, infrastructure, or presentation layers

## 📋 **TDD GREEN PHASE TASK CHECKLIST**

**Use this checklist for domain layer implementation:**

### 🟢 Required Tasks

#### **📖 Test Analysis**
- [ ] **Review failing tests**: Understand what needs to be implemented
- [ ] **Analyze test requirements**: Extract entity behaviors and business rules
- [ ] **Identify domain concepts**: Entities, value objects, aggregates, domain services
- [ ] **Map test scenarios**: Connect tests to domain model design

#### **🟢 Domain Implementation**
- [ ] **Implement entities**: Create domain entities with business logic
- [ ] **Implement value objects**: Create immutable value objects with validation
- [ ] **Implement domain services**: Create domain services for complex business logic
- [ ] **Implement repository interfaces**: Define contracts for data access (interfaces only)

#### **🔍 GREEN Phase Validation**
- [ ] **Run tests**: Execute test suite to verify implementation
- [ ] **Ensure tests pass**: Confirm all domain tests are now green
- [ ] **Verify domain purity**: Ensure no external dependencies in domain layer
- [ ] **Update metadata**: Mark TDD GREEN phase as complete

### 🟡 Recommended Tasks

#### **🏗️ Domain Design Implementation**
- [ ] **Follow domain model**: Implement according to existing domain design
- [ ] **Implement aggregates**: Define aggregate boundaries and invariants
- [ ] **Add business rules**: Implement domain-specific business logic
- [ ] **Create domain events**: Implement domain events for side effects

#### **🧪 Implementation Quality**
- [ ] **Add type hints**: Ensure proper typing throughout domain layer
- [ ] **Add docstrings**: Document public domain APIs
- [ ] **Follow naming conventions**: Use ubiquitous language consistently
- [ ] **Maintain immutability**: Ensure value objects are immutable

### 🟢 Optional Tasks

#### **📋 Advanced Domain Patterns**
- [ ] **Implement specifications**: Create reusable business rule specifications
- [ ] **Add domain exceptions**: Create meaningful domain-specific exceptions
- [ ] **Implement factories**: Create domain object factories for complex creation
- [ ] **Add domain validation**: Implement comprehensive validation logic

#### **📊 Phase Completion & Handoff**
- [ ] **Verify test coverage**: Ensure all domain logic is tested
- [ ] **Document implementation**: Update domain model documentation
- [ ] **Prepare for application layer**: Define clear interfaces for use cases
- [ ] **Commit implementation**: Version control all domain code

**💡 Pro Tip**: Implement only what's needed to make tests pass - avoid over-engineering!

## Task Details

**🤖 Agent Integration**: This command MUST USE PROACTIVELY the specialized `06-implement-domain` subagent for optimal TDD GREEN phase implementation. Claude Code should automatically delegate this task to the 06-implement-domain subagent based on the command description.

**Additional Context for Subagent Execution:**
- `docs/index.md` - Project navigation and status overview for understanding domain implementation context
- Existing domain implementation patterns in `src/domain/` directory for maintaining consistent code structure
- Implementation guidelines and coding standards documentation to ensure code quality
- Domain layer architecture conventions to maintain clean architecture principles
- IMPORTANT: Use Read tool to access actual file contents, not just references

 Claude Code should automatically delegate this task to the 06-implement-domain subagent based on the command description.

1. **Pre-execution Validation**:
   ```bash
   # Validate issue number requirement
   if [[ $# -eq 0 ]]; then
       echo "エラー: 少なくとも1つのイシュー番号を指定してください"
       echo "使用例: /implement-domain 1"
       echo "使用例: /implement-domain 1,7 (複数イシュー)"
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
   
   # Verify tests exist and are failing
   echo "🔍 Issues: $(printf '#%s ' "${issue_numbers[@]}")のテスト状態確認中..."
   
   if [[ ! -d "tests/" ]]; then
       echo "❌ エラー: testsディレクトリが見つかりません"
       echo "💡 先に /create-tests を実行してください"
       exit 1
   fi
   ```

2. **Context Preparation and Agent Execution**:
   ```bash
   # 🔄 Prepare context for agent (Pattern B: Hybrid approach)
   echo "🏗️ コンテキスト準備とエージェント起動..."
   
   # Create context file with domain implementation information
   context_file="/workspace/.claude/context/current-command-context.json"
   current_time=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
   
   # Build context JSON for domain implementation
   cat > "$context_file" <<EOF
   {
     "command": "implement-domain",
     "timestamp": "$current_time",
     "issue_numbers": [$(IFS=,; echo "${issue_numbers[*]}")],
     "phase": "tdd-green-phase",
     "context": {
       "expected_outputs": [
         "src/domain/entities/",
         "src/domain/value_objects/",
         "src/domain/services/",
         "src/domain/repositories/"
       ],
       "architecture_patterns": ["TDD", "DDD", "Clean Architecture"]
     },
     "additional_instructions": "TDD GREENフェーズでドメイン層を実装してください。失敗テストを分析し、最小限のコードで全てのテストを成功させる実装を行ってください。ドメインの純粋性を保ち、ビジネスルールと不変条件をドメイン層に適切に配置してください。",
     "special_considerations": [
       "失敗テスト（tests/domain/）の詳細分析と要件抽出",
       "ドメインモデル設計（docs/domain/issue-X-Y.md）との完全一致",
       "ドメイン純粋性の維持（インフラ依存なし）",
       "エンティティと値オブジェクトの不変条件の実装"
     ],
     "custom_context": {
       "tdd_green_phase": true,
       "domain_purity": true,
       "business_rules_focus": true,
       "test_driven_implementation": true
     }
   }
   EOF
   
   echo "✅ コンテキストファイル作成完了: $context_file"
   
   # 🤖 Call the specialized agent with hybrid context
   echo ""
   echo "🏗️ ドメイン実装エージェントを起動します..."
   echo "専門エージェントがTDD GREEN段階のドメイン層を実装します"
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
[06-implement-domain固有のタスクを実行]

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

   # Execute with specialized 06-implement-domain subagent
   # The 06-implement-domain subagent will be automatically invoked based on the task description
   
   agent_exit_code=$?
   echo "✅ 専用エージェント実行完了 (終了コード: $agent_exit_code)"
   
   echo "✅ エージェント呼び出し設定完了"
   echo "エージェントが以下の処理を実行します:"
   echo "  - コンテキストファイルからのイシュー情報取得"
   echo "  - 失敗テストの分析とドメイン要件の抽出"
   echo "  - ドメインエンティティとビジネスルールの実装"
   echo "  - 値オブジェクトと不変条件の実装"
   echo "  - ドメインサービスと複雑ビジネスロジックの実装"
   echo "  - リポジトリインターフェースの定義"
   echo "  - テスト実行とGREEN状態の確認"
   ```

3. **Agent Result Verification**:
   ```bash
   # 🔍 Verify agent execution results
   echo "🔍 エージェント実行結果を検証中..."
   
   # Check that domain layer was created by the agent
   echo "  🔍 ドメイン層の実装確認中..."
   
   # Check for domain directory structure
   domain_dirs=(
       "src/domain"
       "src/domain/entities"
       "src/domain/value_objects"
       "src/domain/services"
   )
   
   # Validate domain structure was created
   missing_domain_dirs=()
   for dir in "${domain_dirs[@]}"; do
       if [[ ! -d "$dir" ]]; then
           missing_domain_dirs+=("$dir")
       fi
   done
   
   # Check for Python files in domain layer
   domain_files_found=0
   if [[ -d "src/domain" ]]; then
       domain_files_found=$(find src/domain -name "*.py" -type f | wc -l)
   fi
   
   # Run tests to verify GREEN state
   echo "  🧪 テスト実行による実装確認中..."
   test_results="UNKNOWN"
   if command -v pytest >/dev/null 2>&1; then
       if pytest tests/ --tb=no -q >/dev/null 2>&1; then
           test_results="PASS"
           echo "    ✅ テストが成功しました（GREEN状態）"
       else
           test_results="FAIL"
           echo "    ❌ テストが失敗しています"
       fi
   else
       echo "    ⚠️ pytestが見つかりません"
   fi
   
   # Report validation results
   if [[ ${#missing_domain_dirs[@]} -gt 0 ]] || [[ $domain_files_found -eq 0 ]] || [[ "$test_results" != "PASS" ]]; then
       echo "❌ エージェント実行検証失敗:"
       if [[ ${#missing_domain_dirs[@]} -gt 0 ]]; then
           echo "  未作成ドメインディレクトリ: ${missing_domain_dirs[*]}"
       fi
       if [[ $domain_files_found -eq 0 ]]; then
           echo "  ドメイン実装ファイルが作成されていません"
       fi
       if [[ "$test_results" != "PASS" ]]; then
           echo "  テストがGREEN状態になっていません: $test_results"
       fi
       exit 1
   fi
   
   echo "✅ エージェント実行結果検証完了"
   
   # 🔧 Load advanced task verification library
   source "$(dirname "${BASH_SOURCE[0]}")/_task_verification.sh"
   
   # ✨ New: Advanced task verification with retry capability
   echo "🔍 Critical tasks確認中..."
   if ! verify_critical_tasks "06-implement-domain" "$latest_report"; then
       echo "⚠️ Critical tasks確認で問題が検出されました - 再実行を試行します"
       prepare_retry_context "06-implement-domain" "1" "${verification_issues[@]}"
       
       # Enhanced context for retry
       echo "🔄 再実行用の強化コンテキスト準備中..."
       prepare_enhanced_context "06-implement-domain" "$context_file" "${verification_issues[@]}"
       
       echo "💡 推奨アクション: エージェントを再実行してください"
       echo "   重点項目: $(IFS='|'; echo "${verification_issues[*]}")"
       exit 1
   fi
   
   echo "✅ Critical tasks確認完了 - 全項目クリア"
   ```

4. **Display TDD GREEN Phase Success Summary**:
   ```bash
   # 📊 Display comprehensive TDD GREEN phase summary
   echo ""
   echo "🎉 ドメイン層実装完了（TDD GREEN phase）!"
   echo "============================================="
   
   # Show created domain files
   echo "📁 実装されたドメインファイル:"
   if [[ -d "src/domain" ]]; then
       domain_count=$(find src/domain -name "*.py" -type f | wc -l)
       echo "   ✅ ドメインファイル: ${domain_count} 個"
       find src/domain -name "*.py" -type f | head -5 | while read -r file; do
           echo "      - $file"
       done
       if [[ $domain_count -gt 5 ]]; then
           echo "      - ... (他 $((domain_count - 5)) ファイル)"
       fi
   else
       echo "   ⚠️ ドメインファイルが見つかりません"
   fi
   
   # Show test results
   echo ""
   echo "🟢 TDD GREEN状態確認:"
   echo "   - テスト結果: $test_results"
   echo "   - 失敗テストが成功に変更"
   echo "   - ドメイン層のみ実装（Clean Architecture準拠）"
   echo "   - 外部依存なし（ドメイン純粋性維持）"
   
   echo ""
   echo "📋 次のステップ (アプリケーション層実装):"
   for issue_num in "${issue_numbers[@]}"; do
       echo "   /implement-usecase $issue_num"
   done
   
   echo ""
   echo "📚 重要ドキュメント:"
   echo "   - ドメイン実装: src/domain/"
   echo "   - ドメインモデル: docs/domain/"
   echo "   - テスト: tests/"
   echo ""
   echo "✅ TDD GREEN段階完了 - アプリケーション層実装準備完了!"
   ```

## Common Errors and Solutions

### ❌ Error Case 1: Tests not found or not failing
**Cause**: TDD GREEN phase attempted before RED phase completion  
**Solution**: 
```bash
# Ensure tests exist and are failing
/create-tests <issue-number>
# Verify tests fail
pytest tests/ -v
# Then implement domain
/implement-domain <issue-number>
```

### ❌ Error Case 2: Implementing non-domain layers
**Cause**: Accidentally implementing application, infrastructure, or presentation layers  
**Solution**: Focus only on domain layer (entities, value objects, domain services)

### ❌ Error Case 3: Adding external dependencies
**Cause**: Including database, API, or external service dependencies in domain layer  
**Solution**: Keep domain pure - implement only business logic

## Execution Examples

### ✅ Success Example
```bash
$ /implement-domain 15
🔍 Issues: #15 のテスト状態確認中...
🏗️ ドメイン実装エージェントを起動します...
✅ エージェント実行結果検証完了
🎉 ドメイン層実装完了（TDD GREEN phase）!
```

### ❌ Failure Example and Fix
```bash
$ /implement-domain 15
❌ エラー: testsディレクトリが見つかりません

# Fix: Create tests first
$ /create-tests 15
$ /implement-domain 15
```

## 🔄 Metadata Update Requirements

**CRITICAL**: After successful domain implementation completion, you MUST update the following files:

1. **Project State Update**:
   ```bash
   # Update docs/metadata/project-state.json
   # - Increment domain_layer.implemented_entities count
   # - Increment domain_layer.implemented_value_objects count
   # - Increment domain_layer.domain_services count
   # - Update architecture_overview.domain_layer.completion_rate
   # - Add to recent_activity.last_command_executed
   # - Update workflow_statistics.command_execution_stats
   ```

2. **Project Context Update**:
   ```bash
   # Update .claude/context/project-context.json  
   # - Update architecture_status.domain_layer.key_entities array
   # - Update architecture_status.domain_layer.value_objects array
   # - Update architecture_status.domain_layer.domain_services array
   # - Increment workflow_tracking.command_usage.implement_domain
   # - Set current_state.last_command and last_command_timestamp
   ```

3. **Issue-Specific Metadata**:
   ```bash
   # Update docs/use_cases/issue-X-Y.json
   # - Set domain_layer.status to "completed"
   # - Add implementation_files array with created domain files
   # - Update completion timestamp
   ```

**⚠️ Error Handling**: If standard workflow is disrupted:
- 📖 Consult: [Manual Sync Guide](../../docs/maintenance/manual-sync-guide.md)
- 🔄 Check Status: `/use-case-status` for current project state
- 📊 Verify Context: `.claude/context/current-command-context.json`