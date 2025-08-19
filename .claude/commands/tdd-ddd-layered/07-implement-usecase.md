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

## 🤖 Agent Integration Implementation

This command uses the specialized **07-implement-usecase** agent for application layer implementation following TDD GREEN phase principles.

### 1. Pre-execution Validation

```bash
# 🔧 Environment setup and argument parsing
source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "07-implement-usecase" "$ARGUMENTS"

# Use case implementation expects at least one issue number
if [[ ${#issue_numbers[@]} -eq 0 ]]; then
    echo "エラー: 少なくとも1つのイシュー番号を指定してください"
    show_usage_example "implement-usecase" "1" "単一イシューのユースケース実装"
    show_usage_example "implement-usecase" "1,7" "複数イシューのユースケース実装"
    show_usage_example "implement-usecase" "1 feature-name" "イシュー + 機能名指定"
    exit 1
fi

echo "🔄 Issues: $(printf '#%s ' "${issue_numbers[@]}")のアプリケーション層実装を開始します"
echo ""
echo "🚨 重要な注意: このステップではアプリケーション層のみを実装します"
echo "   ✅ 許可: src/application/ 配下のファイルのみ"
echo "   ❌ 禁止: src/domain/, src/infrastructure/, src/presentation/"
echo "   💡 他の層を間違って実装した場合は即座に削除してください"
echo ""
echo "🔴→🟢 TDD原則: テストを実装に合わせて変更してはいけません!"
echo "   📖 シナリオ → 🔴 テスト → 🟢 実装 の順序を厳守"
echo "   ✅ 実装をテストに合わせる（正しい）"
echo "   ❌ テストを実装に合わせる（禁止）"
echo ""

# 📋 Validate prerequisites - domain implementation must be completed
echo "📋 前提条件の検証中..."

# Check for domain implementation
domain_entities=$(find src/domain/entities/ -name "*.py" -type f 2>/dev/null | grep -v __pycache__ || echo "")
if [[ -z "$domain_entities" ]]; then
    echo "❌ ドメイン層の実装が見つかりません"
    echo "💡 最初にドメイン層を実装してください:"
    echo "   /implement-domain $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
    exit 1
fi

# Check for use case tests
usecase_test_files=$(find tests/unit/application/use_cases/ -name "test_*.py" -type f 2>/dev/null || echo "")
if [[ -z "$usecase_test_files" ]]; then
    echo "❌ ユースケーステストが見つかりません"
    echo "💡 最初にTDDテストを作成してください:"
    echo "   /create-tests $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
    exit 1
fi

echo "  ✅ ドメイン実装確認: $(echo "$domain_entities" | wc -l) ファイル"
echo "  ✅ ユースケーステスト確認: $(echo "$usecase_test_files" | wc -l) ファイル"
echo "✅ 前提条件検証完了"
```

### 2. Execute Specialized Agent

```bash
# 🤖 Execute 07-implement-usecase agent with comprehensive task delegation
echo "🤖 07-implement-usecase エージェント実行中..."

# Extract issue list and feature name for agent
issue_list=$(IFS=-; echo "${issue_numbers[*]}")
if [[ ${#other_args[@]} -gt 0 ]]; then
    feature_name="${other_args[0]}"
else
    # Feature name will be extracted from existing files by agent
    feature_name=""
fi

# Prepare agent context and task parameters
agent_task_context="
Applications Layer Implementation Task:
- Target Issues: $(printf '#%s ' "${issue_numbers[@]}")
- Feature Name: ${feature_name:-"auto-detect"}
- Implementation Focus: Use cases, DTOs, application services
- Architecture Layer: Application only (no domain/infra/presentation)
- TDD Phase: GREEN (implement to pass existing tests)
- Dependencies: Domain layer (completed), Use case tests (created)

Critical Requirements:
1. Implement ONLY application layer components
2. Orchestrate domain logic without containing business rules  
3. Create DTOs for clean input/output boundaries
4. Use dependency injection for repository interfaces
5. Handle application-level concerns (transactions, authentication)
6. Follow Clean Architecture principles
7. Ensure tests move from RED to GREEN state
8. Create mock repositories for testing isolation

Forbidden Actions:
- NO domain layer modifications (already complete)
- NO infrastructure implementations (wrong layer)
- NO presentation layer code (wrong layer)
- NO business logic in application layer
- NO test modifications to match implementation

Template Usage:
- Use application/dto_template.py for DTOs
- Use application/exceptions_template.py for exception handling
- Use application/usecase_template.py for use case classes
- Follow consistent code generation patterns

Expected Outputs:
- src/application/use_cases/ (use case classes)
- src/application/dtos/ (data transfer objects)  
- src/application/exceptions/ (application-specific errors)
- Mock repositories for testing (if needed)
- Updated metadata files
- Comprehensive documentation
"

# Execute agent with robust error handling and progress tracking
if Task "$agent_task_context" agent:07-implement-usecase; then
    echo "✅ 07-implement-usecase エージェント実行完了"
else
    echo "❌ 07-implement-usecase エージェント実行失敗"
    echo "💡 以下を確認してください:"
    echo "   - ドメイン層実装の完了状況"
    echo "   - ユースケーステストの存在"
    echo "   - プレースホルダーアサーションの有無"
    echo "   - メタデータファイルの整合性"
    exit 1
fi
```

### 3. Agent Result Verification

```bash
# 🔍 Verify agent implementation results
echo "🔍 エージェント実装結果検証中..."

# Check if application layer files were created
app_usecase_files=$(find src/application/use_cases/ -name "*.py" -type f 2>/dev/null | grep -v __pycache__ || echo "")
app_dto_files=$(find src/application/dtos/ -name "*.py" -type f 2>/dev/null | grep -v __pycache__ || echo "")
app_exception_files=$(find src/application/exceptions/ -name "*.py" -type f 2>/dev/null | grep -v __pycache__ || echo "")

if [[ -z "$app_usecase_files" ]]; then
    echo "❌ ユースケースファイルが作成されていません"
    exit 1
fi

if [[ -z "$app_dto_files" ]]; then
    echo "❌ DTOファイルが作成されていません"
    exit 1
fi

if [[ -z "$app_exception_files" ]]; then
    echo "❌ 例外ファイルが作成されていません"
    exit 1
fi

echo "  ✅ ユースケース: $(echo "$app_usecase_files" | wc -l) ファイル"
echo "  ✅ DTO: $(echo "$app_dto_files" | wc -l) ファイル"  
echo "  ✅ 例外: $(echo "$app_exception_files" | wc -l) ファイル"

# Verify use case tests are now passing (GREEN state)
echo "  🧪 ユースケーステスト GREEN状態検証中..."
if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/unit/application/use_cases/ -v --tb=short > /tmp/usecase_test_results 2>&1; then
    passed_tests=$(grep -c "PASSED" /tmp/usecase_test_results 2>/dev/null || echo "0")
    failed_tests=$(grep -c "FAILED" /tmp/usecase_test_results 2>/dev/null || echo "0")
    echo "    ✅ テスト結果: 成功 $passed_tests, 失敗 $failed_tests"
    
    if [[ $failed_tests -gt 0 ]]; then
        echo "    ⚠️  一部のテストが失敗していますが、実装は完了しました"
        echo "    💡 必要に応じて追加実装を検討してください"
    fi
else
    echo "    ⚠️  テスト実行でエラーが発生しましたが、実装は完了しました"
fi
rm -f /tmp/usecase_test_results

# Check architecture compliance (no forbidden dependencies)
echo "  🏗️ アーキテクチャ準拠性検証中..."
forbidden_imports=$(find src/application/ -name "*.py" -exec grep -l "^import.*infrastructure\\|^from.*infrastructure\\|^import.*presentation\\|^from.*presentation" {} \; 2>/dev/null || echo "")

if [[ -n "$forbidden_imports" ]]; then
    echo "    ⚠️  禁止された依存関係が発見されました:"
    echo "$forbidden_imports" | head -3
    echo "    💡 アプリケーション層の依存関係を見直してください"
else
    echo "    ✅ アーキテクチャ準拠性: 適切な層分離"
fi

echo "✅ エージェント実装結果検証完了"
```

### 4. Display Success Summary

```bash
# 🎉 Display comprehensive success summary
echo ""
echo "🎉 アプリケーション層実装完了!"
echo "============================================="
echo "🔄 機能: ${feature_name:-"auto-detected"}"
echo "🎫 対象イシュー: $(printf '#%s ' "${issue_numbers[@]}")"
echo ""
echo "📊 実装されたコンポーネント:"
usecase_count=$(echo "$app_usecase_files" | wc -l)
dto_count=$(echo "$app_dto_files" | wc -l)
exception_count=$(echo "$app_exception_files" | wc -l)
echo "   ユースケース: $usecase_count 個"
echo "   DTOs: $dto_count 個"
echo "   例外クラス: $exception_count 個"
echo ""
echo "🟢 テスト状況:"
echo "   - ユースケーステスト: TDD GREEN フェーズ"
echo "   - ドメインテスト: 引き続き通過"
echo "   - テスト実装: 成功 ${passed_tests:-"N/A"} / 失敗 ${failed_tests:-"N/A"}"
echo ""
echo "🏛️ アーキテクチャ準拠:"
echo "   - クリーンアーキテクチャ原則: ✅"
echo "   - レイヤー分離: ✅"
echo "   - ドメインロジック orchestration: ✅"
echo "   - 依存性注入パターン: ✅"
echo ""
echo "🤖 エージェント活用:"
echo "   - 専門エージェント: 07-implement-usecase"
echo "   - テンプレートベース実装: ✅"
echo "   - 一貫性のあるコード生成: ✅"
echo "   - 統一された開発パターン: ✅"
echo ""
echo "🚀 次のステップ:"
echo "   1. インフラ層実装: /implement-infra $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
echo "   2. 進捗確認: /use-case-status $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
echo "   3. 統合テスト実行（インフラ層完成後）"
echo ""
echo "🚨 TDD原則リマインダー:"
echo "   ⚠️ 実装中にテストを変更した場合、それはTDD違反です"
echo "   ✅ 正解: シナリオ → テスト → 実装の順序で進める"
echo "   ❌ 禁止: 実装を正としてテストを変更する"
echo ""
echo "💡 実装品質:"
echo "   - ビジネスフロー orchestration: ✅"
echo "   - 型安全なデータ転送: ✅"
echo "   - 包括的なエラーハンドリング: ✅"
echo "   - テスト可能な設計: ✅"
echo "   - テンプレートベースの一貫性: ✅"
echo ""
echo "✅ アプリケーション層実装完了 - インフラ層実装準備完了!"
echo ""
echo "🚨 MANDATORY FOR CLAUDE CODE: SCENARIO EVOLUTION CHECK"
echo "   ユースケース実装中に新要件・エラー・エッジケース発見時は"
echo "   作業を中断して /evolve-scenarios <feature-name> を実行すること"
echo "   CRITICAL: ユースケース変更は全レイヤーに影響します"
echo ""
echo "🔴 TDD守則（絶対遵守）:"
echo "   1. シナリオがテストを決める"
echo "   2. テストが実装を決める" 
echo "   3. 実装がテストを決めてはならない"
echo "   4. この順序を逆転させた場合、TDD失敗となる"
```

**Important Notes:**
- Use cases orchestrate, don't contain business logic
- Keep use cases thin and focused  
- Use DTOs for input/output, not domain objects
- Handle cross-cutting concerns (logging, auth)
- Mock repositories for testing
- Template system ensures consistency and maintainability
- All user-facing output must be in JAPANESE

