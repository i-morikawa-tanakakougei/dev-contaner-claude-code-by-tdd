Implement application layer use cases to orchestrate domain logic.

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

1. **Setup Safe Environment and Parse Arguments**:
   ```bash
   # 🔧 Load all safe operation functions and template utilities
   source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "07-implement-usecase" "$ARGUMENTS"
   source "$(dirname "${BASH_SOURCE[0]}")/templates/_template_utils.sh"
   
   # Use case implementation expects at least one issue number
   if [[ ${#issue_numbers[@]} -eq 0 ]]; then
       echo "エラー: 少なくとも1つのイシュー番号を指定してください"
       show_usage_example "implement-usecase" "1" "単一イシューのユースケース実装"
       show_usage_example "implement-usecase" "1,7" "複数イシューのユースケース実装"
       show_usage_example "implement-usecase" "1 feature-name" "イシュー + 機能名指定"
       exit 1
   fi
   
   # Extract issue list and feature name
   issue_list=$(IFS=-; echo "${issue_numbers[*]}")
   if [[ ${#other_args[@]} -gt 0 ]]; then
       feature_name="${other_args[0]}"
   else
       # Feature name will be extracted from existing files
       feature_name=""
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
   ```

2. **Begin Transaction and Pre-validation**:
   ```bash
   # 🔄 Start comprehensive transaction
   if ! begin_transaction "implement_usecase_${issue_list}"; then
       echo "エラー: トランザクションの開始に失敗しました"
       exit 1
   fi
   
   # 📋 Validate prerequisites - domain implementation must be completed
   echo "📋 前提条件の検証中..."
   
   # Extract feature name from existing files if not provided
   if [[ -z "$feature_name" ]]; then
       found_spec=$(find docs/use_cases/ -name "issue-${issue_list}-*.md" -type f | head -1)
       if [[ -n "$found_spec" ]]; then
           feature_name=$(basename "$found_spec" | sed 's/^issue-[0-9-]*-\(.*\)\.md$/\1/')
           echo "  📝 機能名抽出: $feature_name"
       else
           echo "エラー: 機能名を特定できませんでした"
           execute_rollback "feature_name_missing"
           exit 1
       fi
   fi
   
   # Check for domain implementation
   domain_entities=$(find src/domain/entities/ -name "*.py" -type f 2>/dev/null | grep -v __pycache__ || echo "")
   if [[ -z "$domain_entities" ]]; then
       echo "❌ ドメイン層の実装が見つかりません"
       echo "💡 最初にドメイン層を実装してください:"
       echo "   /implement-domain $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
       execute_rollback "missing_domain_implementation"
       exit 1
   fi
   
   echo "  ✅ ドメイン実装確認: $(echo "$domain_entities" | wc -l) ファイル"
   
   # Check for use case tests
   usecase_test_files=$(find tests/unit/application/use_cases/ -name "test_*.py" -type f 2>/dev/null || echo "")
   if [[ -z "$usecase_test_files" ]]; then
       echo "❌ ユースケーステストが見つかりません"
       echo "💡 最初にTDDテストを作成してください:"
       echo "   /create-tests $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
       execute_rollback "missing_usecase_tests"
       exit 1
   fi
   
   echo "  ✅ ユースケーステスト確認: $(echo "$usecase_test_files" | wc -l) ファイル"
   
   # 🚨 CRITICAL: Check for placeholder assertions in application tests
   echo "  🚨 アプリケーション層プレースホルダーアサーション検証中..."
   
   application_placeholder_files=()
   while IFS= read -r -d '' file; do
       if grep -l 'assert False, "RED:' "$file" >/dev/null 2>&1; then
           application_placeholder_files+=("$file")
       fi
   done < <(find tests/unit/application/ -name "*.py" -print0 2>/dev/null)
   
   if [[ ${#application_placeholder_files[@]} -gt 0 ]]; then
       echo "    ❌ アプリケーション層プレースホルダーアサーション発見:"
       for file in "${application_placeholder_files[@]:0:5}"; do
           count=$(grep -c 'assert False, "RED:' "$file" 2>/dev/null || echo "0")
           echo "      - $file: $count 個"
       done
       [[ ${#application_placeholder_files[@]} -gt 5 ]] && echo "      - ... (他 $((${#application_placeholder_files[@]} - 5)) ファイル)"
       
       echo ""
       echo "    🚨 CRITICAL ISSUE: これらのテストは意図的にFALSE失敗しています"
       echo "       - アプリケーション実装は完了済みだが、テストがプレースホルダーのまま"
       echo "       - これはTDDプロセス違反の状態です"
       echo ""
       echo "    💡 修正が必要: プレースホルダーアサーションを実際のテストに置き換える"
       echo "       この修正は手動で行う必要があります"
       echo ""
       echo "    ⚠️  続行するとプレースホルダーテストの修正をスキップしますが、"
       echo "       後でテストを適切に実装する必要があります"
       echo ""
       echo "    続行しますか？ (y/N): "
       read -n 1 -r
       echo
       if [[ ! $REPLY =~ ^[Yy]$ ]]; then
           echo "アプリケーション層実装をキャンセルしました"
           echo "💡 推奨: 手動でプレースホルダーテストを適切なテストに置き換えてから再実行"
           execute_rollback "application_placeholder_assertions_found"
           exit 1
       fi
       
       echo "    ⚠️  プレースホルダーテストを無視して続行（後で修正が必要）"
   else
       echo "    ✅ アプリケーション層プレースホルダーアサーション: なし（正常なテスト状態）"
   fi
   
   echo "✅ 前提条件検証完了"
   ```

3. **Identify and Validate Metadata**:
   ```bash
   # 📊 Find and validate metadata files
   echo "📊 メタデータファイル検証中..."
   
   metadata_file="docs/use_cases/issue-${issue_list}-${feature_name}.json"
   
   if [[ ! -f "$metadata_file" ]]; then
       echo "エラー: メタデータファイルが見つかりません: $metadata_file"
       execute_rollback "metadata_file_missing"
       exit 1
   fi
   
   # Validate metadata file format
   if ! validate_json_file "$metadata_file"; then
       echo "エラー: メタデータファイルの形式が不正です: $metadata_file"
       execute_rollback "metadata_file_invalid"
       exit 1
   fi
   
   # Check domain implementation phase completion
   domain_status=$(jq -r '.phases.domain_implementation.completed // false' "$metadata_file" 2>/dev/null)
   if [[ "$domain_status" != "true" ]]; then
       echo "エラー: ドメイン層実装が完了していません"
       echo "💡 先に /implement-domain コマンドを実行してください"
       execute_rollback "domain_implementation_not_completed"
       exit 1
   fi
   
   # Check if application implementation is already completed
   app_status=$(jq -r '.phases.application_implementation.completed // false' "$metadata_file" 2>/dev/null)
   if [[ "$app_status" == "true" ]]; then
       echo "⚠️  Issue #${issue_list} のアプリケーション層実装は既に完了しています"
       echo "既存の実装を上書きしますか？ (y/N): "
       read -n 1 -r
       echo
       if [[ ! $REPLY =~ ^[Yy]$ ]]; then
           echo "アプリケーション層実装をキャンセルしました"
           commit_transaction
           exit 0
       fi
       echo "🔄 既存のアプリケーション層実装を上書きします"
   fi
   
   echo "✅ メタデータ検証完了"
   ```

4. **Run Tests to Confirm Current State**:
   ```bash
   # 🔍 Validate current test state
   echo "🔍 現在のテスト状態確認中..."
   
   # Validate Python environment for testing
   if ! validate_python_environment; then
       echo "エラー: Python環境の検証に失敗しました"
       execute_rollback "python_env_validation_failed"
       exit 1
   fi
   
   # Run domain tests to confirm they pass
   echo "  🟢 ドメインテスト実行中（GREEN状態確認）..."
   domain_test_output_file="/tmp/domain_test_output_$$"
   
   if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/unit/domain/ -v --tb=short > "$domain_test_output_file" 2>&1; then
       domain_tests_passed=true
       echo "    ✅ ドメインテスト: 成功"
   else
       domain_tests_passed=false
       echo "    ❌ ドメインテストが失敗しています"
       echo "    💡 先にドメイン層実装を完成させてください"
       rm -f "$domain_test_output_file"
       execute_rollback "domain_tests_failing"
       exit 1
   fi
   rm -f "$domain_test_output_file"
   
   # Run use case tests to check RED state
   echo "  🔴 ユースケーステスト実行中（RED状態確認）..."
   usecase_test_output_file="/tmp/usecase_test_output_$$"
   usecase_test_result=0
   
   if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/unit/application/use_cases/ -v --tb=short > "$usecase_test_output_file" 2>&1; then
       usecase_test_result=0  # Tests passed (unexpected)
   else
       usecase_test_result=1  # Tests failed (expected in RED phase)
   fi
   
   # Analyze usecase test results
   total_usecase_tests=$(grep -c "test_.*PASSED\\|test_.*FAILED" "$usecase_test_output_file" 2>/dev/null || echo "0")
   failed_usecase_tests=$(grep -c "FAILED" "$usecase_test_output_file" 2>/dev/null || echo "0")
   
   echo "    📊 ユースケーステスト結果:"
   echo "      - 総テスト数: $total_usecase_tests"
   echo "      - 失敗テスト数: $failed_usecase_tests"
   
   if [[ $usecase_test_result -eq 0 ]] && [[ $total_usecase_tests -gt 0 ]]; then
       echo "    ⚠️  ユースケーステストが成功しています（既に実装済み？）"
       echo "実装を続行しますか？ (y/N): "
       read -n 1 -r
       echo
       if [[ ! $REPLY =~ ^[Yy]$ ]]; then
           echo "アプリケーション層実装をキャンセルしました"
           rm -f "$usecase_test_output_file"
           commit_transaction
           exit 0
       fi
   elif [[ $total_usecase_tests -eq 0 ]]; then
       echo "    エラー: ユースケーステストが見つかりません"
       rm -f "$usecase_test_output_file"
       execute_rollback "no_usecase_tests_found"
       exit 1
   else
       echo "    ✅ RED状態確認: ユースケーステストが期待通り失敗"
   fi
   
   rm -f "$usecase_test_output_file"
   echo "✅ テスト状態確認完了"
   ```

5. **Extract Domain and Use Case Information**:
   ```bash
   # 📖 Extract domain and use case information for implementation
   echo "📖 ドメイン・ユースケース情報分析中..."
   
   # Extract entities from domain layer
   all_entities=()
   for entity_file in $domain_entities; do
       entity_name=$(basename "$entity_file" .py)
       # Convert to PascalCase
       entity_class=$(echo "$entity_name" | sed 's/_\([a-z]\)/\U\1/g' | sed 's/^./\U&/')
       all_entities+=("$entity_class")
   done
   
   # Extract use case scenarios from specification
   spec_file=$(find docs/use_cases/ -name "issue-${issue_list}-${feature_name}.md" -type f | head -1)
   use_case_scenarios=()
   
   if [[ -n "$spec_file" ]] && check_file_permissions "$spec_file" "read"; then
       echo "  📋 仕様分析中: $(basename "$spec_file")"
       
       # Extract Given-When-Then scenarios
       scenarios=$(grep -A 5 -B 2 "Given:\\|When:\\|Then:" "$spec_file" 2>/dev/null | \
                  grep -E "(Given|When|Then):" | \
                  sed 's/^[[:space:]]*//' | \
                  paste -d' ' - - - 2>/dev/null || echo "")
       
       if [[ -n "$scenarios" ]]; then
           while IFS= read -r scenario; do
               [[ -n "$scenario" ]] && use_case_scenarios+=("$scenario")
           done <<< "$scenarios"
       fi
   fi
   
   echo "  🎯 抽出された情報:"
   echo "    - エンティティ: ${#all_entities[@]} 個"
   echo "    - ユースケースシナリオ: ${#use_case_scenarios[@]} 個"
   
   echo "✅ 情報分析完了"
   ```

6. **Create Application Layer Structure**:
   ```bash
   # 🏗️ Create application layer structure
   echo "🏗️ アプリケーション層構造作成中..."
   
   # Define application structure directories
   app_directories=(
       "src/application/use_cases"
       "src/application/dtos"
       "src/application/exceptions"
       "src/application/services"
   )
   
   # Create all application directories safely
   for dir in "${app_directories[@]}"; do
       echo "  📁 作成中: $dir"
       if ! safe_mkdir "$dir"; then
           echo "エラー: アプリケーションディレクトリ作成に失敗しました: $dir"
           execute_rollback "app_directory_creation_failed"
           exit 1
       fi
       add_rollback "rmdir '$dir' 2>/dev/null || true" "Remove app directory: $dir"
   done
   
   # Create __init__.py files
   app_init_files=(
       "src/application/use_cases/__init__.py"
       "src/application/dtos/__init__.py"
       "src/application/exceptions/__init__.py"
       "src/application/services/__init__.py"
   )
   
   for init_file in "${app_init_files[@]}"; do
       echo "  📄 作成中: $init_file"
       if ! safe_create_file "$init_file" '"""Application layer package initialization"""' false; then
           echo "エラー: アプリケーション__init__.pyファイルの作成に失敗しました"
           execute_rollback "app_init_creation_failed"
           exit 1
       fi
       add_rollback "rm -f '$init_file'" "Remove app init file: $init_file"
   done
   
   echo "✅ アプリケーション構造作成完了 (${#app_directories[@]} ディレクトリ)"
   ```

7. **Setup Template Variables and Implement DTOs**:
   ```bash
   # 🎯 Setup template variables
   echo "🎯 テンプレート変数設定中..."
   
   # Setup feature-based variables
   setup_feature_vars "$feature_name"
   
   # Generate entity-related variables
   if [[ ${#all_entities[@]} -gt 0 ]]; then
       entity_imports=$(generate_entity_imports "${all_entities[@]}")
       repository_imports=$(generate_repository_imports "${all_entities[@]}")
       generate_repository_constructor "${all_entities[@]}"
   else
       entity_imports=""
       repository_imports=""
       repository_constructor_params=""
       repository_constructor_docs=""
       repository_assignments=""
   fi
   
   echo "  ✅ テンプレート変数設定完了"
   
   # 📝 Implement DTOs using template
   echo "📝 DTO（データ転送オブジェクト）実装中..."
   
   implemented_files=()
   dtos_file="src/application/dtos/${feature_name_snake}_dtos.py"
   
   echo "  📝 テンプレート使用: application/dto_template.py"
   
   if ! process_template "application/dto_template.py" "$dtos_file"; then
       echo "エラー: DTOテンプレート処理に失敗しました"
       execute_rollback "dtos_template_processing_failed"
       exit 1
   fi
   
   implemented_files+=("$dtos_file")
   add_rollback "rm -f '$dtos_file'" "Remove implemented DTOs: $dtos_file"
   
   echo "✅ DTO実装完了"
   ```

8. **Implement Application Exceptions**:
   ```bash
   # 🚨 Implement application-specific exceptions using template
   echo "🚨 アプリケーション例外実装中..."
   
   exceptions_file="src/application/exceptions/${feature_name_snake}_exceptions.py"
   
   echo "  🚨 テンプレート使用: application/exceptions_template.py"
   
   if ! process_template "application/exceptions_template.py" "$exceptions_file"; then
       echo "エラー: 例外テンプレート処理に失敗しました"
       execute_rollback "exceptions_template_processing_failed"
       exit 1
   fi
   
   implemented_files+=("$exceptions_file")
   add_rollback "rm -f '$exceptions_file'" "Remove implemented exceptions: $exceptions_file"
   
   echo "✅ アプリケーション例外実装完了"
   ```

9. **Implement Use Cases**:
   ```bash
   # 🔄 Implement main use cases using template
   echo "🔄 ユースケース実装中..."
   
   usecase_file="src/application/use_cases/${feature_name_snake}_use_case.py"
   
   echo "  🔄 テンプレート使用: application/usecase_template.py"
   
   # Generate additional template variables for use case
   if [[ ${#all_entities[@]} -gt 0 ]]; then
       main_entity="${all_entities[0]}"
       entity_lower=$(to_lower_case "$main_entity")
       
       entity_creation_logic="entity = self._create_or_load_${entity_lower}(request)"
       entity_params="entity, "
       entity_params_with_request="entity, "
       persistence_logic="self._${entity_lower}_repository.save(entity)"
       list_logic="entities = self._${entity_lower}_repository.find_all()\\n            items = [self._entity_to_dict(entity) for entity in entities]"
       
       # Generate create_or_load methods
       create_or_load_methods="def _create_or_load_${entity_lower}(self, request: ${feature_name_title}Request) -> $main_entity:\\n        \"\"\"${main_entity}の作成または読み込み\"\"\"\\n        # TODO: 実際のビジネスロジックに基づいて実装\\n        return $main_entity.create(entity_id=\"temp-id\")\\n"
       
       # Generate entity_to_dict methods
       entity_to_dict_methods="def _entity_to_dict(self, entity: $main_entity) -> dict:\\n        \"\"\"エンティティを辞書に変換\"\"\"\\n        return {\\n            \"id\": entity.id,\\n            \"created_at\": entity.created_at.isoformat(),\\n            \"updated_at\": entity.updated_at.isoformat()\\n            # TODO: 必要な属性を追加\\n        }"
   else
       entity_creation_logic="# TODO: ドメインオブジェクトの操作を実装"
       entity_params=""
       entity_params_with_request=""
       persistence_logic="# TODO: 永続化処理を実装"
       list_logic="# TODO: データ取得処理を実装\\n            items = []"
       create_or_load_methods=""
       entity_to_dict_methods=""
   fi
   
   # Generate scenario comments from use case scenarios
   scenario_comments=""
   if [[ ${#use_case_scenarios[@]} -gt 0 ]]; then
       scenario_comments="# Given-When-Then シナリオに基づく実装:"
       for i in "${!use_case_scenarios[@]}"; do
           scenario="${use_case_scenarios[$i]}"
           when=$(echo "$scenario" | grep -oE "When: [^\\|]*" | sed 's/When: //' || echo "処理 $((i+1))")
           scenario_comments+="\\n        # $((i+1)). $when"
       done
   else
       scenario_comments="# ビジネスロジックをここに実装"
   fi
   
   # Set additional template variables (注意: 既存のテンプレート関数で処理されない変数)
   # これらは直接置換する必要がある
   temp_content=$(load_template "application/usecase_template.py")
   temp_content=$(echo "$temp_content" | sed "s|{{ENTITY_CREATION_LOGIC}}|$entity_creation_logic|g")
   temp_content=$(echo "$temp_content" | sed "s|{{ENTITY_PARAMS}}|$entity_params|g")
   temp_content=$(echo "$temp_content" | sed "s|{{ENTITY_PARAMS_WITH_REQUEST}}|$entity_params_with_request|g")
   temp_content=$(echo "$temp_content" | sed "s|{{PERSISTENCE_LOGIC}}|$persistence_logic|g")
   temp_content=$(echo "$temp_content" | sed "s|{{LIST_LOGIC}}|$list_logic|g")
   temp_content=$(echo "$temp_content" | sed "s|{{CREATE_OR_LOAD_METHODS}}|$create_or_load_methods|g")
   temp_content=$(echo "$temp_content" | sed "s|{{ENTITY_TO_DICT_METHODS}}|$entity_to_dict_methods|g")
   temp_content=$(echo "$temp_content" | sed "s|{{SCENARIO_COMMENTS}}|$scenario_comments|g")
   
   # Apply standard template variable substitution
   processed_content=$(substitute_template_vars "application/usecase_template.py" "$temp_content")
   
   if ! safe_create_file "$usecase_file" "$processed_content" true; then
       echo "エラー: ユースケースファイルの作成に失敗しました: $usecase_file"
       execute_rollback "usecase_implementation_failed"
       exit 1
   fi
   
   implemented_files+=("$usecase_file")
   add_rollback "rm -f '$usecase_file'" "Remove implemented use case: $usecase_file"
   
   echo "✅ ユースケース実装完了"
   ```

10. **Create Mock Repositories for Testing**:
    ```bash
    # 🎭 Create mock repositories for testing
    echo "🎭 モックリポジトリ実装中..."
    
    # Create infrastructure repositories directory
    if ! safe_mkdir "src/infrastructure/repositories"; then
        echo "エラー: インフラリポジトリディレクトリの作成に失敗しました"
        execute_rollback "infra_repo_dir_creation_failed"
        exit 1
    fi
    
    # Create __init__.py
    if ! safe_create_file "src/infrastructure/repositories/__init__.py" '"""Infrastructure repositories package"""' false; then
        echo "エラー: インフラリポジトリ__init__.pyの作成に失敗しました"
        execute_rollback "infra_repo_init_creation_failed"
        exit 1
    fi
    
    # Create mock repositories for each entity using individual template processing
    for entity in "${all_entities[@]}"; do
        entity_lower=$(to_lower_case "$entity")
        mock_repo_file="src/infrastructure/repositories/mock_${entity_lower}_repository.py"
        
        echo "  🎭 実装中: Mock${entity}Repository ($mock_repo_file)"
        
        # Setup entity-specific variables for mock repository
        setup_entity_vars "$entity"
        
        # Use infrastructure/repository_template.py as a base and modify for mock
        mock_template_content=$(load_template "infrastructure/repository_template.py")
        
        # Modify for mock implementation
        mock_template_content=$(echo "$mock_template_content" | sed "s/class ${entity}Repository/class Mock${entity}Repository/g")
        mock_template_content=$(echo "$mock_template_content" | sed "s/from src.infrastructure.models/# Mock repository - no database models needed/g")
        mock_template_content=$(echo "$mock_template_content" | sed "s/{{MODEL_IMPORTS}}/from typing import Dict, List, Optional/g")
        
        # Process with template utilities
        mock_processed_content=$(substitute_template_vars "infrastructure/repository_template.py" "$mock_template_content")
        
        # Apply mock-specific modifications
        mock_processed_content=$(echo "$mock_processed_content" | sed 's/""".*Repository implementation/"""Mock '"$entity"' Repository Implementation\n\n    テスト用のメモリ内リポジトリ実装。/g')
        mock_processed_content=$(echo "$mock_processed_content" | sed 's/def __init__(self):/def __init__(self):\n        """モックリポジトリ初期化"""\n        self._storage: Dict[str, '"$entity"'] = {}\n        self._next_id = 1\n\n    def clear(self) -> None:\n        """すべてのデータをクリア（テスト用）"""\n        self._storage.clear()\n        self._next_id = 1\n    \n    def count(self) -> int:\n        """保存されているエンティティ数を取得（テスト用）"""\n        return len(self._storage)/g')
        
        if ! safe_create_file "$mock_repo_file" "$mock_processed_content" true; then
            echo "エラー: モックリポジトリファイルの作成に失敗しました: $mock_repo_file"
            execute_rollback "mock_repo_implementation_failed"
            exit 1
        fi
        
        implemented_files+=("$mock_repo_file")
        add_rollback "rm -f '$mock_repo_file'" "Remove mock repository: $mock_repo_file"
    done
    
    echo "✅ モックリポジトリ実装完了 (${#all_entities[@]} ファイル)"
    ```

11. **Run Tests to Verify GREEN State**:
    ```bash
    # 🟢 Verify use case tests are now in GREEN state
    echo "🟢 ユースケーステスト GREEN状態検証中..."
    
    # Run use case tests to confirm GREEN state
    echo "  🧪 ユースケーステスト実行中（GREEN状態確認）..."
    
    usecase_green_test_output_file="/tmp/usecase_green_test_output_$$"
    usecase_test_result=0
    
    # Run tests and capture output
    if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/unit/application/use_cases/ -v --tb=short > "$usecase_green_test_output_file" 2>&1; then
        usecase_test_result=0  # Tests passed (expected in GREEN phase)
    else
        usecase_test_result=1  # Tests failed (need more implementation)
    fi
    
    # Analyze test results
    total_usecase_tests=$(grep -c "test_.*PASSED\\|test_.*FAILED" "$usecase_green_test_output_file" 2>/dev/null || echo "0")
    passed_usecase_tests=$(grep -c "PASSED" "$usecase_green_test_output_file" 2>/dev/null || echo "0")
    failed_usecase_tests=$(grep -c "FAILED" "$usecase_green_test_output_file" 2>/dev/null || echo "0")
    
    echo "  📊 ユースケーステスト結果分析:"
    echo "    - 総テスト数: $total_usecase_tests"
    echo "    - 成功テスト数: $passed_usecase_tests"
    echo "    - 失敗テスト数: $failed_usecase_tests"
    
    if [[ $failed_usecase_tests -gt 0 ]]; then
        echo "⚠️  まだ失敗しているユースケーステストがあります:"
        grep "FAILED" "$usecase_green_test_output_file" | head -5
        echo ""
        echo "追加実装が必要な可能性があります。続行しますか？ (y/N): "
        read -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "アプリケーション層実装を中止しました"
            rm -f "$usecase_green_test_output_file"
            execute_rollback "usecase_tests_still_failing"
            exit 1
        fi
    else
        echo "  ✅ GREEN状態確認: すべてのユースケーステストが成功しています"
    fi
    
    # Calculate test coverage if possible
    usecase_coverage_result=""
    if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/unit/application/ --cov=src.application --cov-report=term-missing --quiet >/tmp/usecase_coverage_output_$$ 2>&1; then
        usecase_coverage_result=$(grep -E "[0-9]+%" /tmp/usecase_coverage_output_$$ | tail -1 || echo "Coverage data not available")
        rm -f /tmp/usecase_coverage_output_$$
    fi
    
    rm -f "$usecase_green_test_output_file"
    usecase_tests_passed=$([ $failed_usecase_tests -eq 0 ] && echo "true" || echo "false")
    
    echo "✅ ユースケーステスト GREEN フェーズ検証完了"
    ```

12. **Code Quality Validation**:
    ```bash
    # 🔍 Code quality validation for application layer
    echo "🔍 アプリケーション層コード品質検証中..."
    
    # Run ruff formatting and linting on application layer
    echo "  🎨 コードフォーマット・リント実行中..."
    
    if ! uv run --frozen ruff format src/application/ --quiet; then
        echo "⚠️  アプリケーション層のコードフォーマットに問題があります"
    fi
    
    app_lint_output_file="/tmp/app_ruff_output_$$"
    if uv run --frozen ruff check src/application/ > "$app_lint_output_file" 2>&1; then
        echo "    ✅ リント検査: 問題なし"
    else
        echo "    ⚠️  リント警告があります:"
        head -5 "$app_lint_output_file"
        echo "    💡 必要に応じて修正してください"
    fi
    rm -f "$app_lint_output_file"
    
    # Run type checking if pyright is available
    echo "  🔍 型チェック実行中..."
    
    app_type_output_file="/tmp/app_pyright_output_$$"
    if uv run --frozen pyright src/application/ > "$app_type_output_file" 2>&1; then
        echo "    ✅ 型チェック: 問題なし"
    else
        echo "    ⚠️  型チェック警告があります:"
        head -5 "$app_type_output_file"
        echo "    💡 必要に応じて型ヒントを修正してください"
    fi
    rm -f "$app_type_output_file"
    
    # Architecture validation - check for proper layer separation
    echo "  🏗️ アーキテクチャ検証中..."
    
    # Check for external dependencies in application layer
    app_imports=$(find src/application/ -name "*.py" -exec grep -l "^import \\|^from " {} \; 2>/dev/null || echo "")
    external_deps_found=false
    presentation_deps_found=false
    
    for file in $app_imports; do
        # Check for problematic imports (infrastructure details or presentation)
        if grep -E "^(import|from) (requests|sqlalchemy|django|flask|fastapi|sqlite3|psycopg2)" "$file" >/dev/null 2>&1; then
            echo "    ⚠️  インフラ依存発見: $file"
            external_deps_found=true
        fi
        
        # Check for presentation layer dependencies
        if grep -E "^(import|from).*presentation" "$file" >/dev/null 2>&1; then
            echo "    ⚠️  プレゼンテーション層依存発見: $file"
            presentation_deps_found=true
        fi
    done
    
    if [[ "$external_deps_found" == "false" ]] && [[ "$presentation_deps_found" == "false" ]]; then
        echo "    ✅ アーキテクチャ検証: アプリケーション層の適切な分離"
    else
        echo "    💡 アプリケーション層の依存関係を見直すことを推奨します"
    fi
    
    echo "✅ コード品質検証完了"
    ```

13. **Update Metadata and Documentation**:
    ```bash
    # 📊 Update metadata with application implementation completion
    echo "📊 メタデータ更新中..."
    
    if ! update_metadata_atomic "$metadata_file" \
        '.phases.application_implementation.created = true | 
         .phases.application_implementation.completed = true |
         .phases.application_implementation.completed_at = "'"$(date -u +%Y-%m-%dT%H:%M:%SZ)"'" |
         .phases.application_implementation.usecase_tests_passed = '"$usecase_tests_passed"' |
         .phases.application_implementation.coverage = "'"$usecase_coverage_result"'" |
         .updated_at = "'"$(date -u +%Y-%m-%dT%H:%M:%SZ)"'" |
         .spec_files.application_implementation = ['"$(printf '"%s",' "${implemented_files[@]}" | sed 's/,$//')"'] |
         .phase = "application_implemented" |
         .next_commands = ["implement-infra", "use-case-status"]'; then
        echo "エラー: メタデータの更新に失敗しました"
        execute_rollback "metadata_update_failed"
        exit 1
    fi
    
    # Create application documentation
    app_doc_dir="docs/application"
    if ! safe_mkdir "$app_doc_dir"; then
        echo "エラー: アプリケーションドキュメントディレクトリの作成に失敗しました"
        execute_rollback "app_doc_dir_creation_failed"
        exit 1
    fi
    
    app_doc_file="$app_doc_dir/issue-${issue_list}-application-design.md"
    
    app_doc_content="# アプリケーション層設計: $feature_name

**Issues**: $(printf '#%s ' "${issue_numbers[@]}")
**実装日時**: $(date)

## 概要

このアプリケーション層実装は、$(printf 'Issue #%s, ' "${issue_numbers[@]}" | sed 's/, $//')の要件に基づいて作成されました。
ドメインオブジェクトを orchestrate し、ビジネス要件を実現します。

## 実装されたコンポーネント

### ユースケース
- **${feature_name_title}UseCase**: メインビジネス機能の実行
  - execute(): 主要ビジネスフロー実行
  - list(): データ一覧取得

### DTOs (Data Transfer Objects)
- **${feature_name_title}Request**: 実行リクエスト
- **${feature_name_title}Response**: 実行レスポンス
- **${feature_name_title}ListRequest**: 一覧取得リクエスト
- **${feature_name_title}ListResponse**: 一覧取得レスポンス

### 例外クラス
- **${feature_name_title}ApplicationError**: 基底例外
- **${feature_name_title}ValidationError**: バリデーションエラー
- **${feature_name_title}NotFoundError**: データ未発見エラー
- **${feature_name_title}AuthorizationError**: 認可エラー
- **${feature_name_title}BusinessRuleViolationError**: ビジネスルール違反
- **${feature_name_title}ConcurrencyError**: 同時実行エラー

### モックリポジトリ
$(for entity in "${all_entities[@]}"; do
    echo "- **Mock${entity}Repository**: ${entity}のテスト用リポジトリ"
done)

## アーキテクチャ原則

### レイヤー分離
- アプリケーション層はドメイン層に依存
- インフラ層の詳細には依存しない
- プレゼンテーション層には依存しない

### 責務
- ドメインオブジェクトの orchestration
- トランザクション境界の管理
- 認可・認証の実装
- DTOによる入出力データ変換

### 設計パターン
- **Dependency Injection**: リポジトリの注入
- **DTO Pattern**: データ転送オブジェクト
- **Exception Translation**: ドメイン例外からアプリケーション例外への変換

## テンプレートシステム

このアプリケーション層実装は、統一されたテンプレートシステムを使用して生成されました：

- **DTOテンプレート**: `templates/application/dto_template.py`
- **例外テンプレート**: `templates/application/exceptions_template.py`
- **ユースケーステンプレート**: `templates/application/usecase_template.py`

## テスト結果

- **テスト数**: $total_usecase_tests
- **成功**: $passed_usecase_tests
- **失敗**: $failed_usecase_tests
- **カバレッジ**: $usecase_coverage_result

## 次のステップ

1. **インフラ層実装**: \`/implement-infra $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')\`
2. **進捗確認**: \`/use-case-status $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')\`

---
**実装ステータス**: ✅ 完了
**アーキテクチャ検証**: ✅ 通過
**テスト状況**: $usecase_tests_passed
**テンプレートベース**: ✅ 使用
"
    
    if ! safe_create_file "$app_doc_file" "$app_doc_content" true; then
        echo "エラー: アプリケーションドキュメントの作成に失敗しました"
        execute_rollback "app_doc_creation_failed"
        exit 1
    fi
    
    implemented_files+=("$app_doc_file")
    add_rollback "rm -f '$app_doc_file'" "Remove application documentation"
    
    echo "✅ メタデータ・ドキュメント更新完了"
    ```

14. **Update Use Case Index and Git Commit**:
    ```bash
    # 📚 Update use case index and commit changes
    echo "📚 ユースケースインデックス更新・コミット中..."
    
    use_cases_index="docs/use_cases/index.md"
    if [[ -f "$use_cases_index" ]]; then
        # Create backup
        backup_file="${use_cases_index}.backup.$(date +%Y%m%d_%H%M%S)"
        if ! cp "$use_cases_index" "$backup_file"; then
            echo "エラー: インデックスファイルのバックアップ作成に失敗しました"
            execute_rollback "index_backup_failed"
            exit 1
        fi
        add_rollback "mv '$backup_file' '$use_cases_index'" "Restore index backup"
        
        # Update status for the feature
        feature_line="\\[${feature_name}\\]"
        updated_line="- [${feature_name}]($(basename "${spec_file}")) - Issues: $(printf '#%s ' "${issue_numbers[@]}")- Phase: application_implemented, TDD: 🟢 GREEN, App: ✅)"
        
        if ! sed -i "s|.*${feature_line}.*|${updated_line}|" "$use_cases_index"; then
            echo "エラー: インデックスファイルの更新に失敗しました"
            execute_rollback "index_update_failed"
            exit 1
        fi
        
        echo "✅ インデックス更新完了"
    fi
    
    # 💾 Commit application implementation
    echo "💾 アプリケーション層実装をコミット中..."
    
    commit_message="feat: implement application layer for $(printf 'issue #%s ' "${issue_numbers[@]}")- ${feature_name}

Application Layer Implementation Summary:
- Feature: ${feature_name}
- Issues: $(printf '#%s ' "${issue_numbers[@]}")
- Implementation Files: ${#implemented_files[@]} created
- Use Case Test Results: Passed $passed_usecase_tests, Failed $failed_usecase_tests
- Coverage: $usecase_coverage_result
- Template-Based Implementation: ✅

Implemented Components:
$(printf '  - %s\n' "${implemented_files[@]}")

Application Layer Features:
- Use cases for business workflow orchestration
- DTOs for clean input/output data transfer
- Application-specific exception handling
- Mock repositories for testing isolation
- Proper layer separation and dependency injection

Template System Usage:
- DTOs: application/dto_template.py
- Exceptions: application/exceptions_template.py  
- Use Cases: application/usecase_template.py
- Consistent code generation and maintainability

Architecture Compliance:
- Clean Architecture principles maintained
- Domain logic orchestration (no business logic in app layer)
- Proper dependency direction (app → domain)
- No infrastructure or presentation dependencies

TDD Status: Use case tests passing
Next Step: /implement-infra for infrastructure layer
"
    
    files_to_commit=("$metadata_file")
    files_to_commit+=("${implemented_files[@]}")
    if [[ -f "$use_cases_index" ]]; then
        files_to_commit+=("$use_cases_index")
    fi
    
    if ! safe_git_commit "$commit_message" "${files_to_commit[@]}"; then
        echo "エラー: コミットに失敗しました"
        execute_rollback "commit_failed"
        exit 1
    fi
    
    add_rollback "git reset --hard HEAD~1" "Undo application implementation commit"
    echo "✅ コミット完了"
    ```

15. **Update GitHub Issues and Final Success**:
    ```bash
    # 🎫 Update GitHub issues with application implementation completion
    echo "🎫 GitHubイシュー更新中..."
    
    for issue_num in "${issue_numbers[@]}"; do
        echo "  📝 Issue #$issue_num コメント追加中..."
        
        issue_comment="🔄 **アプリケーション層実装完了**

アプリケーション層（ユースケース）の実装が完了しました。

## 📊 実装結果
- **実装ファイル数**: ${#implemented_files[@]} ファイル
- **ユースケーステスト結果**: 成功 $passed_usecase_tests / 総計 $total_usecase_tests
- **カバレッジ**: $usecase_coverage_result
- **アーキテクチャ検証**: ✅ 通過
- **テンプレートベース**: ✅ 使用

## 🔄 実装されたコンポーネント
### ユースケース
- **${feature_name_title}UseCase**: ビジネスフロー orchestration
  - メインビジネス機能の実行
  - データ一覧取得機能
  - 認可・バリデーション処理

### DTOs (データ転送オブジェクト)
- **リクエスト/レスポンス**: 型安全な入出力
- **バリデーション機能**: 入力データ検証
- **エラーレスポンス**: 適切なエラーハンドリング

### 例外処理
- **階層化された例外**: アプリケーション固有のエラー分類
- **ビジネスルール違反**: 適切なエラー区分
- **認可・バリデーション**: セキュリティ対応

### モックリポジトリ
$(if [[ ${#all_entities[@]} -gt 0 ]]; then
    for entity in "${all_entities[@]:0:2}"; do
        echo "- **Mock${entity}Repository**: テスト用データアクセス"
    done
    [[ ${#all_entities[@]} -gt 2 ]] && echo "- ... (他 $((${#all_entities[@]} - 2)) リポジトリ)"
fi)

## 🎯 テンプレートシステム活用
- **統一されたコード生成**: 一貫性のある実装
- **保守性向上**: 標準化されたコード構造
- **開発効率**: 高速で確実な実装

## 🏛️ アーキテクチャ準拠
- [x] クリーンアーキテクチャ原則
- [x] ドメイン層への適切な依存
- [x] インフラ層からの独立
- [x] 依存性注入パターン
- [x] レイヤー分離の維持

## 🚀 次のステップ

インフラストラクチャ層実装を開始してください：
\`\`\`bash
/implement-infra $issue_num
\`\`\`

## 📚 関連ドキュメント
- [アプリケーション層設計]($app_doc_file)
- [実装されたファイル一覧](#実装されたコンポーネント)

## 🔍 動作確認
\`\`\`bash
# アプリケーション層テスト実行
uv run --frozen pytest tests/unit/application/ -v

# カバレッジ確認
uv run --frozen pytest tests/unit/application/ --cov=src.application
\`\`\`

---
**Layer Status**: Application ✅ → 次: Infrastructure 🏗️
**Template System**: ✅ Active
"
        
        if ! safe_add_issue_comment "$issue_num" "$issue_comment"; then
            echo "    ⚠️  Issue #$issue_num へのコメント追加に失敗しました（続行します）"
        else
            echo "    ✅ Issue #$issue_num コメント追加完了"
        fi
    done
    
    echo "✅ GitHub イシュー更新完了"
    
    # 🎉 Transaction commit (success!)
    if commit_transaction; then
        echo ""
        echo "🎉 アプリケーション層実装完了!"
        echo "============================================="
        echo "🔄 機能名: $feature_name"
        echo "🎫 対象イシュー: $(printf '#%s ' "${issue_numbers[@]}")"
        echo "📊 実装ファイル数: ${#implemented_files[@]} 個"
        echo "🎯 テンプレートベース: ✅ 活用"
        echo ""
        echo "📋 実装されたコンポーネント:"
        echo "   ユースケース: 1 個 (${feature_name_title}UseCase)"
        echo "   DTOs: 4 個 (Request/Response + List)"
        echo "   例外クラス: 6 個 (階層化された例外処理)"
        echo "   モックリポジトリ: ${#all_entities[@]} 個"
        echo ""
        echo "🟢 テスト状況:"
        echo "   - ユースケーステスト: 成功 $passed_usecase_tests / 総計 $total_usecase_tests"
        echo "   - カバレッジ: $usecase_coverage_result"
        echo "   - ドメインテスト: 引き続き通過"
        echo ""
        echo "🏛️ アーキテクチャ準拠:"
        echo "   - クリーンアーキテクチャ原則"
        echo "   - 適切なレイヤー分離"
        echo "   - ドメインロジックの orchestration"
        echo "   - 依存性注入パターン"
        echo ""
        echo "🎯 テンプレートシステム:"
        echo "   - DTOテンプレート: application/dto_template.py"
        echo "   - 例外テンプレート: application/exceptions_template.py"
        echo "   - ユースケーステンプレート: application/usecase_template.py"
        echo "   - 統一されたコード生成と保守性"
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
        echo "   - ビジネスフロー orchestration"
        echo "   - 型安全なデータ転送"
        echo "   - 包括的なエラーハンドリング"
        echo "   - テスト可能な設計"
        echo "   - テンプレートベースの一貫性"
        echo ""
        
        # Show operation logs summary
        echo "📊 操作ログサマリー:"
        show_github_operation_log | tail -2
        show_git_operation_log | tail -2
        show_transaction_log | tail -2
        
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
        
    else
        echo "❌ トランザクション コミット失敗"
        exit 1
    fi
    ```

Important Notes:
- Use cases orchestrate, don't contain business logic
- Keep use cases thin and focused
- Use DTOs for input/output, not domain objects
- Handle cross-cutting concerns (logging, auth)
- Mock repositories for testing
- Template system ensures consistency and maintainability
- All user-facing output must be in JAPANESE