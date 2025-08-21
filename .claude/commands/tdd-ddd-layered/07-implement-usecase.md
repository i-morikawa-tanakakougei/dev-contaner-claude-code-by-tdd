Implement application layer use cases to orchestrate domain logic using the 07-implement-usecase agent.

## Metadata
- **Prerequisites**: Domain layer implementation completed (06-implement-domain)
- **Input**: Issue number(s) (required)
- **Output**: 
  - Application layer implementation in `src/application/`
  - Use case classes, DTOs, and application services
  - Updated `docs/use_cases/issue-X-Y.json` metadata
- **Dependencies**: Domain layer classes, pytest, type hints
- **Execution Timing**: After domain implementation, before infrastructure layer

## 🎯 **TDD/DDD/LAYERED PROCESS CONTEXT**

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Sprint Execution Phase - Application Layer Implementation (07/16)  
> 🎯 **Phase Purpose**: Implement use cases and DTOs to orchestrate domain logic  
> ⬅️ **Previous Stage**: 06-implement-domain (Domain Layer Implementation)  
> ➡️ **Next Stage**: 08-implement-infra (Infrastructure Layer Implementation)
>
> **📋 3-Layer Architecture Operations**:  
> - 🎯 **Strategic**: `docs/use_cases/core/index.md` (Reference use case flows)  
> - 📊 **Tactical**: `docs/use_cases/index.md` (Update application layer status)  
> - 🔧 **Execution**: `docs/use_cases/issue-X-Y.json` (Track application implementation)

## Common Errors and Solutions

### ❌ Error Case 1: Domain layer not implemented
**Cause**: Application layer started before domain implementation completion  
**Solution**: 
```bash
# Ensure domain layer is complete
/implement-domain <issue-number>
# Then implement application layer
/implement-usecase <issue-number>
```

### ❌ Error Case 2: Use cases directly manipulating infrastructure
**Cause**: Application layer bypassing domain layer or accessing infrastructure directly  
**Solution**: 
```python
# Bad: Direct database access in use case
from src.infrastructure.database import Session

# Good: Using domain repository interface
from src.domain.repositories import UserRepository
class UserUseCase:
    def __init__(self, user_repo: UserRepository):
        self._user_repo = user_repo
```

### ❌ Error Case 3: Placeholder assertions causing false RED state
**Cause**: Application tests contain `assert False, "RED: ... not implemented yet"` but implementation exists  
**Solution**: 
```python
# Bad: Placeholder assertion (causes false RED)
def test_use_case_execution(self):
    assert False, "RED: Use case execution not implemented yet"

# Good: Actual test implementation
def test_use_case_execution(self):
    use_case = MyUseCase(mock_repository)
    result = use_case.execute(request_dto)
    assert result.success is True
    assert result.data is not None
```
**Recovery**: Replace all placeholder assertions with proper tests that verify actual implementation

### ❌ Error Case 4: DTOs with business logic
**Cause**: Business logic leaked into Data Transfer Objects  
**Solution**: 
- DTOs should only contain data, no business methods
- Move validation to domain entities or value objects
- Keep DTOs as simple data containers

## Execution Examples

### ✅ Success Example
```bash
$ /implement-usecase 15
📱 Issues: #15 のアプリケーション層実装を開始します
🟢 ドメイン層実装確認中...
✅ ドメイン層が正常に実装されています
🏗️ ユースケース実装中...
  ✅ ファイル作成: src/application/use_cases/user_management.py
  ✅ ファイル作成: src/application/dtos/user_dto.py
  ✅ ファイル作成: src/application/exceptions.py
🧪 アプリケーションテスト実行中...
======= 8 passed, 0 failed =======
✅ アプリケーションテストが成功
🎉 アプリケーション層実装完了!
```

### ❌ Failure Example and Fix
```bash
$ /implement-usecase 15
❌ ドメイン層の実装が完了していません
💡 最初にドメイン層を実装してください:
   /implement-domain 15

# Fix: Complete domain layer first
$ /implement-domain 15
$ /implement-usecase 15
```

### ❌ Placeholder Assertion Example and Fix
```bash
$ /implement-usecase 3
🚨 プレースホルダーアサーション発見:
  - tests/unit/application/use_cases/test_data_persistence_use_case.py: 9 個
  - tests/unit/application/dtos/test_data_persistence_dtos.py: 4 個

🚨 CRITICAL ISSUE: これらのテストは意図的にFALSE失敗しています
   - 実装は完了済みだが、テストがプレースホルダーのまま
   - これはTDDプロセス違反の状態です

# Fix: Replace placeholder assertions with real tests
# Edit test files to replace:
#   assert False, "RED: Use case execution not implemented yet"
# With:
#   use_case = DataPersistenceUseCase(mock_repository)
#   result = use_case.save_trade_data(request)
#   assert result.success is True
```

## 📱 **APPLICATION LAYER IMPLEMENTATION ONLY**

**⚠️ Important Notice:**
- **This step is APPLICATION LAYER ONLY** - Implement use cases and orchestration logic
- **NO OTHER LAYERS** - Focus only on application layer components  
- **Domain orchestration** - Coordinate domain objects and business workflows
- **Transaction boundaries** - Handle application-level concerns

**Layer Implementation Sequence:**
1. `06-implement-domain` ← Domain layer (completed)
2. `07-implement-usecase` ← **【YOU ARE HERE】Application layer**
3. `08-implement-infra` ← Infrastructure layer  
4. `09-implement-presentation` ← Presentation layer

## 🚨 **CRITICAL: APPLICATION LAYER ONLY - NO OTHER LAYERS**

**❌ ABSOLUTELY FORBIDDEN in this step:**
- **Infrastructure Layer**: No repository implementations, database code, or external API integrations
- **Presentation Layer**: No controllers, APIs, CLI commands, or web interfaces
- **Domain Layer Modifications**: Domain layer is already complete - DO NOT modify it
- **Cross-layer Code**: No dependency injection setup or configuration management

**✅ ONLY ALLOWED in this step:**
- **Use Cases**: Application services that orchestrate domain logic
- **DTOs**: Data Transfer Objects for input/output boundaries
- **Application Exceptions**: Application-specific error types
- **Application Services**: Coordination and transaction management logic

## 📋 **APPLICATION LAYER TASK CHECKLIST**

**Use this checklist to implement application layer with proper orchestration:**

### 🔴 Required Tasks

#### **📖 Use Case Analysis**
- [ ] **Read Given-When-Then specifications**: Extract use case flows from specification documents
- [ ] **🚨 CRITICAL: Replace placeholder assertions**: Check for and fix `assert False, "RED: ... not implemented yet"` statements in application tests
- [ ] **Verify test authenticity**: Ensure tests actually test implementation, not just placeholder failures
- [ ] **Map to domain operations**: Identify which domain entities/services each use case needs
- [ ] **Define input/output boundaries**: Determine what data flows in and out of use cases
- [ ] **Identify transaction boundaries**: Determine where consistency and atomicity are required

#### **🎯 Use Case Implementation**
- [ ] **Create use case classes**: Implement application services for each main scenario
- [ ] **Implement main flow**: Code the happy path for each Given-When-Then scenario
- [ ] **Orchestrate domain objects**: Coordinate domain entities, services, and repositories
- [ ] **Handle transactions**: Implement transaction boundaries and rollback logic

#### **🧪 Application Layer Testing**
- [ ] **Run application tests**: Execute tests that cover use case logic
- [ ] **Verify use case flows**: Confirm Given-When-Then scenarios work end-to-end
- [ ] **Update metadata**: Mark application layer implementation complete in issue-X-Y.json
- [ ] **Commit application layer**: Version control application layer code

### 🟡 Recommended Tasks

#### **📦 DTO Implementation**
- [ ] **Create input DTOs**: Define data structures for use case inputs
- [ ] **Create output DTOs**: Define data structures for use case outputs
- [ ] **Add validation**: Implement input validation and sanitization logic
- [ ] **Map domain to DTOs**: Implement conversion between domain objects and DTOs
- [ ] **Add serialization**: Ensure DTOs can be properly serialized/deserialized

#### **🔗 Repository Integration**
- [ ] **Use repository interfaces**: Integrate with domain repository interfaces (from step 06)
- [ ] **Handle repository errors**: Catch and handle repository-level exceptions
- [ ] **Coordinate multiple repositories**: Implement use cases that span multiple aggregates
- [ ] **Manage repository transactions**: Ensure proper transaction handling across repositories
- [ ] **NO CONCRETE IMPLEMENTATIONS**: Only use interfaces - concrete implementations come in step 08

#### **🚫 Architecture Compliance Check**
- [ ] **No infrastructure implementations**: Confirm NO concrete repository implementations
- [ ] **No presentation layer code**: Confirm NO controllers, APIs, or UI components
- [ ] **No database/external dependencies**: Verify no direct database or external API calls
- [ ] **Only application concerns**: Ensure code only handles orchestration and coordination
- [ ] **Application directory only**: Confirm only src/application/ directory has new files

### 🟢 Optional Tasks

#### **⚠️ Exception Handling**
- [ ] **Create application exceptions**: Define application-specific error types
- [ ] **Handle domain exceptions**: Catch and wrap domain exceptions appropriately
- [ ] **Add error context**: Provide meaningful error messages and context
- [ ] **Implement error recovery**: Add retry logic and fallback mechanisms where appropriate
- [ ] **Log application errors**: Ensure proper error logging for debugging

#### **🔧 Code Quality Validation**
- [ ] **Run ruff linting**: Execute `uv run --frozen ruff check src/ --fix`
- [ ] **Run ruff formatting**: Execute `uv run --frozen ruff format src/`
- [ ] **Run type checking**: Execute `uv run --frozen pyright src/`
- [ ] **Fix quality issues**: Address any linting, formatting, or type errors
- [ ] **Verify clean results**: Ensure all quality tools pass without errors

#### **📊 Advanced Phase Completion**
- [ ] **Plan error handling**: Define how application errors should be handled and propagated
- [ ] **Add alternative flows**: Implement alternate scenarios from specifications
- [ ] **Add error handling**: Implement error scenarios and edge cases
- [ ] **Test error scenarios**: Verify proper error handling and exception propagation
- [ ] **Test DTO conversions**: Ensure proper mapping between domain and DTOs
- [ ] **Mock repository dependencies**: Use mocks since concrete repositories don't exist yet
- [ ] **Domain layer unchanged**: Verify domain layer files were not modified
- [ ] **Document use case flows**: Record implemented use cases and their responsibilities
- [ ] **Prepare for infrastructure**: Ensure repository interfaces are ready for concrete implementations
- [ ] **Verify test coverage**: Confirm application logic is properly tested with mocks

**💡 Pro Tip**: Use cases should orchestrate domain objects without containing business logic - keep business rules in the domain layer!

### ✅ ALLOWED Files (Implementation Targets):
- `src/application/use_cases/` - Use cases for business workflow orchestration
- `src/application/dtos/` - Data Transfer Objects for input/output
- `src/application/exceptions/` - Application-specific exceptions
- `src/application/services/` - Application services (coordination, not business logic)

### ❌ FORBIDDEN Files (DO NOT create/modify in this step):
- `src/domain/` - **Domain Layer (already implemented in previous step)**
- `src/infrastructure/` - **Infrastructure Layer (concrete repositories, databases, external APIs)**
- `src/presentation/` - **Presentation Layer (API endpoints, CLI, web interfaces)**

### 🎯 Implementation Rules:
1. **Orchestrate domain logic ONLY** - Use cases coordinate domain entities and services
2. **No business logic in application layer** - Business rules belong in domain layer
3. **Use DTOs for boundaries** - Transform data at application boundaries
4. **Handle cross-cutting concerns** - Transactions, logging, authentication, authorization
5. **Dependency injection** - Depend on domain interfaces, not concrete implementations

### 💡 If you accidentally implement other layers:
```bash
# Delete incorrectly created files
rm -rf src/infrastructure/ src/presentation/

# Do NOT modify domain layer
# Domain layer should already be complete from step 06
```

**Violating these rules will break the clean architecture and cause dependency issues.**

## 🚨 **CRITICAL TDD PRINCIPLE WARNING**

**🔴→🟢 NEVER MODIFY TESTS TO MATCH IMPLEMENTATION!**

### 🎯 Sacred TDD Flow (DO NOT REVERSE):
```
📖 Scenario (Given-When-Then) 
    ↓
🔴 TDD Tests (Specifications)
    ↓
🟢 Implementation (Code)
```

### ✅ CORRECT Approach:
- **Tests are specifications** - They define WHAT the system should do
- **Implementation serves tests** - Write code to make tests pass
- **Tests come from scenarios** - Business requirements drive tests
- **Fix implementation, not tests** - If tests fail, change the code

### ❌ FORBIDDEN Approach (NEVER DO THIS):
- ~~Modify tests to match existing implementation~~
- ~~Delete failing tests because "implementation works differently"~~
- ~~Change test expectations to fit current code~~
- ~~Justify wrong implementation by changing tests~~

### 🚨 If Implementation Doesn't Match Tests:
1. **STOP** - Do not modify tests
2. **Analyze** - Why are tests failing?
3. **Check Scenarios** - Are tests correctly representing requirements?
4. **Fix Implementation** - Modify code to satisfy test requirements
5. **Only if scenario is wrong** - Then update scenario → test → implementation

### 💡 Emergency Recovery:
```bash
# If you accidentally modified tests
git restore tests/unit/application/

# Return to proper TDD flow
# 1. Read failing tests (these are specifications)
# 2. Implement application code to make tests pass
# 3. Never change test logic to match code
```

**⚠️ CRITICAL: Test modifications break the TDD cycle and invalidate scenario-driven development!**

---

## Task Details

**🤖 Agent Integration**: This command uses the specialized `07-implement-usecase` agent for optimal application layer implementation following TDD GREEN phase principles.

Follow these steps:

1. **Pre-execution Validation**:
   ```bash
   # Validate issue numbers are provided
   if [[ $# -eq 0 ]]; then
       echo "エラー: 少なくとも1つのイシュー番号を指定してください"
       echo "使用例:"
       echo "  /implement-usecase 15     # 単一イシュー"
       echo "  /implement-usecase 15,23  # 複数イシュー"
       exit 1
   fi
   
   # Parse issue numbers
   IFS=',' read -ra ISSUES <<< "$1"
   echo "🔄 Issues: $(printf '#%s ' "${ISSUES[@]}")のアプリケーション層実装を開始します"
   
   # Check domain layer prerequisites
   if [[ ! -d "src/domain/entities" ]] || [[ -z "$(find src/domain/entities/ -name "*.py" 2>/dev/null)" ]]; then
       echo "❌ ドメイン層の実装が見つかりません"
       echo "💡 最初にドメイン層を実装してください:"
       echo "   /implement-domain $1"
       exit 1
   fi
   ```

2. **Context Preparation and Agent Execution**:
   ```bash
   # 🔄 Prepare context for agent (Pattern B: Hybrid approach)
   echo "🏗️ コンテキスト準備とエージェント起動..."
   
   # Create context file with use case implementation information
   context_file="/workspace/.claude/context/current-command-context.json"
   current_time=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
   
   # Extract issue list and feature name
   issue_list=$(IFS=,; echo "${ISSUES[*]}")
   if [[ ${#other_args[@]} -gt 0 ]]; then
       feature_name="${other_args[0]}"
   else
       # Feature name will be extracted from existing metadata files
       feature_name=""
   fi
   
   # Build context JSON for use case implementation
   cat > "$context_file" <<EOF
   {
     "command": "implement-usecase",
     "timestamp": "$current_time",
     "issue_numbers": [$(IFS=,; echo "${ISSUES[*]}")],
     "feature_name": "${feature_name:-"auto-detect"}",
     "phase": "application-layer-implementation",
     "context": {
       "expected_outputs": [
         "src/application/use_cases/",
         "src/application/dtos/",
         "src/application/services/",
         "Updated test files with GREEN status"
       ],
       "architecture_patterns": ["Application Layer", "Use Cases", "DTOs", "Clean Architecture"]
     },
     "additional_instructions": "TDD GREEN段階でアプリケーション層の実装を行ってください。ドメイン層を協調させるユースケース、DTOs、アプリケーションサービスを実装し、すべてのテストがGREEN状態になることを確保してください。",
     "special_considerations": [
       "ドメインロジックの協調のみ（ビジネスロジックはドメイン層）",
       "DTOを使用した境界での変換処理",
       "横断的関心事（トランザクション・認証・ログ）の処理",
       "依存性注入によるドメインインターフェースへの依存"
     ],
     "custom_context": {
       "tdd_green_phase": true,
       "domain_orchestration": true,
       "clean_architecture_compliance": true,
       "application_layer_focus": true
     }
   }
   EOF
   
   echo "✅ コンテキストファイル作成完了: $context_file"
   
   # 🤖 Call the specialized agent with hybrid context
   echo ""
   echo "🏗️ アプリケーション層実装エージェントを起動します..."
   echo "専門エージェントがTDD GREEN phaseでアプリケーション層を実装します"
   echo ""
   
   # Actual Claude Code Task tool invocation with hybrid approach
   cat <<'AGENT_CALL'
   Task tool will be called with:
   - subagent_type: "07-implement-usecase"
   - description: "TDD GREEN phase application layer implementation"
   - prompt: |
     アプリケーション層実装タスクを実行してください。
     
     ## コンテキスト情報の取得
     1. 一時コンテキスト（イシュー情報）:
        - /workspace/.claude/context/current-command-context.json を読み込み
     
     2. ドメイン層の確認:
        - src/domain/ でドメイン実装を確認
        - tests/ でテスト仕様を確認
        - docs/use_cases/ でユースケース仕様を確認
     
     ## 実行タスク
     1. ユースケース実装（ドメインエンティティ・サービスの協調）
     2. DTOs作成（境界での入出力データ変換）
     3. アプリケーションサービス実装（横断的関心事処理）
     4. リポジトリインターフェース依存関係の設定
     5. エラーハンドリングと検証ロジック
     6. テスト実行によるGREEN状態確保
     7. Clean Architecture原則の遵守確認
     8. 実装完了確認とファイル構造検証
     
     ## 処理完了後
     - アプリケーション層実装の完了確認
     - すべてのテストGREEN状態の確保
     - 次のステップ（インフラ層実装）への案内
   AGENT_CALL
   
   echo "✅ エージェント呼び出し設定完了"
   echo "エージェントが以下の処理を実行します:"
   echo "  - コンテキストファイルからのイシュー情報取得"
   echo "  - ユースケース実装（ドメインエンティティ・サービスの協調）"
   echo "  - DTOs作成（境界での入出力データ変換）"
   echo "  - アプリケーションサービス実装（横断的関心事処理）"
   echo "  - リポジトリインターフェース依存関係の設定"
   echo "  - エラーハンドリングと検証ロジック"
   echo "  - テスト実行によるGREEN状態確保"
   echo "  - Clean Architecture原則の遵守確認"
   
   # Execute the specialized agent
   claude_task="$task_context" \
       claude_agent="07-implement-usecase" \
       claude_working_dir="$(pwd)" \
       claude_issues="$(printf '%s,' "${ISSUES[@]}" | sed 's/,$//')" \
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
   
   # Check that application layer files were created
   application_files=(
       "src/application/use_cases/"
       "src/application/dtos/"
   )
   
   # Validate application layer structure
   missing_dirs=()
   for dir in "${application_files[@]}"; do
       if [[ ! -d "$dir" ]]; then
           missing_dirs+=("$dir")
       fi
   done
   
   # Check for application layer implementation files
   usecase_files=$(find src/application/use_cases/ -name "*.py" 2>/dev/null | wc -l)
   dto_files=$(find src/application/dtos/ -name "*.py" 2>/dev/null | wc -l)
   
   # Validate directory creation
   if [[ ${#missing_dirs[@]} -gt 0 ]]; then
       verification_issues+=("未作成ディレクトリ: ${missing_dirs[*]}")
   else
       echo "  ✅ アプリケーション層ディレクトリ構造: 作成済み"
   fi
   
   # Validate file creation
   if [[ $usecase_files -eq 0 ]]; then
       verification_issues+=("ユースケース実装ファイルが見つかりません")
   else
       echo "  ✅ ユースケースファイル: ${usecase_files}個"
   fi
   
   if [[ $dto_files -gt 0 ]]; then
       echo "  ✅ DTOファイル: ${dto_files}個"
   fi
   
   # Check metadata updates
   metadata_updated=0
   for issue_num in "${ISSUES[@]}"; do
       metadata_file=$(find docs/use_cases -name "issue-${issue_num}-*.json" | head -1)
       if [[ -f "$metadata_file" ]] && grep -q "application_implementation" "$metadata_file"; then
           metadata_updated=$((metadata_updated + 1))
       fi
   done
   
   if [[ $metadata_updated -eq ${#ISSUES[@]} ]]; then
       echo "  ✅ メタデータ更新: ${metadata_updated}/${#ISSUES[@]} 完了"
   else
       verification_issues+=("メタデータ更新が不完全: ${metadata_updated}/${#ISSUES[@]}")
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
   echo "🎉 アプリケーション層実装完了!"
   echo "================================="
   echo ""
   echo "📊 実行サマリー:"
   echo "  📂 対象Issues: $(printf '#%s ' "${ISSUES[@]}")"
   echo "  🏗️ ユースケースファイル: ${usecase_files}個"
   echo "  📦 DTOファイル: ${dto_files}個"
   echo "  🔄 更新メタデータ: ${metadata_updated}個"
   echo ""
   
   # Show created files summary
   echo "📁 実装されたファイル:"
   if [[ $usecase_files -gt 0 ]]; then
       echo "   ✅ ユースケース: ${usecase_files}個のファイル"
       echo "     └── src/application/use_cases/"
   fi
   if [[ $dto_files -gt 0 ]]; then
       echo "   ✅ DTO: ${dto_files}個のファイル"
       echo "     └── src/application/dtos/"
   fi
   
   echo ""
   echo "🎯 TDD GREEN フェーズ完了状況:"
   echo "   ✅ ドメイン層: 実装済み (前提条件)"
   echo "   ✅ アプリケーション層: 実装完了"
   echo "   ⏭️ インフラストラクチャ層: 次のステップ"
   echo "   ⏭️ プレゼンテーション層: 後続ステップ"
   
   echo ""
   echo "📋 推奨次のステップ:"
   issue_list=$(IFS=,; echo "${ISSUES[*]}")
   echo "   1. インフラストラクチャ層実装: /implement-infra $issue_list"
   echo "   2. プレゼンテーション層実装: /implement-presentation $issue_list"
   echo "   3. 全テスト実行: /run-all-tests $issue_list"
   echo "   4. リファクタリング: /refactor $issue_list"
   
   echo ""
   echo "📁 生成ファイル:"
   for issue_num in "${ISSUES[@]}"; do
       metadata_file=$(find docs/use_cases -name "issue-${issue_num}-*.json" | head -1)
       if [[ -f "$metadata_file" ]]; then
           echo "  🔄 メタデータ: $metadata_file"
       fi
   done
   echo ""
   echo "🎯 アプリケーション層実装が正常に完了しました!"
   echo ""
   echo "✅ TDD GREEN状態でアプリケーション層実装完了!"
   ```

4. **Advanced Task Verification**:
   ```bash
   # 🔧 Load advanced task verification library
   source "$(dirname "${BASH_SOURCE[0]}")/_task_verification.sh"
   
   # ✨ New: Advanced task verification with retry capability
   echo "🔍 Critical tasks確認中..."
   if ! verify_critical_tasks "07-implement-usecase" "$latest_report"; then
       echo "⚠️ Critical tasks確認で問題が検出されました - 再実行を試行します"
       prepare_retry_context "07-implement-usecase" "1" "${verification_issues[@]}"
       
       # Enhanced context for retry
       echo "🔄 再実行用の強化コンテキスト準備中..."
       prepare_enhanced_context "07-implement-usecase" "$context_file" "${verification_issues[@]}"
       
       echo "💡 推奨アクション: エージェントを再実行してください"
       echo "   重点項目: $(IFS='|'; echo "${verification_issues[*]}")"
       exit 1
   fi
   
   echo "✅ Critical tasks確認完了 - 全項目クリア"
   ```

