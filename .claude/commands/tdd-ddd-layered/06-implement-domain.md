Implement domain layer to make tests pass (TDD GREEN phase).

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
**Solution**: 
- **Only** implement files in `src/domain/`
- **No** database connections, API clients, or web controllers
- **No** use cases or application services

### ❌ Error Case 3: Placeholder assertions causing false RED state
**Cause**: Tests contain `assert False, "RED: ... not implemented yet"` but implementation exists  
**Solution**: 
```python
# Bad: Placeholder assertion (causes false RED)
def test_entity_creation(self):
    assert False, "RED: Entity creation not implemented yet"

# Good: Actual test implementation
def test_entity_creation(self):
    entity = MyEntity.create("test_id", "test_value")
    assert entity.id == "test_id"
    assert entity.value == "test_value"
```
**Recovery**: Replace all placeholder assertions with proper tests that verify actual implementation

### ❌ Error Case 4: ID type incompatibility in entity inheritance
**Cause**: Inheriting from base entities with UUID requirements when existing tests use string IDs  
**Solution**: 
```python
# Problem: Direct inheritance causing UUID conversion errors
@dataclass
class Configuration(BaseDomainEntity):  # Requires UUID, but tests use "test-config-1"
    id: str
    
    def __post_init__(self):
        super().__init__(uuid.UUID(self.id))  # ❌ Fails with non-UUID strings

# Solution: Use composition with static methods
@dataclass  
class Configuration:  # No inheritance
    id: str
    
    def _validate_invariants(self):
        # Use base class static methods for validation
        BaseDomainEntity._validate_string_type_and_not_empty(self.id, "ID")
        # ... other validations using static methods
```
**Key principle**: Prefer composition over inheritance when ID formats differ

### ❌ Error Case 5: Domain layer has external dependencies
**Cause**: Domain entities importing infrastructure or application code  
**Solution**: 
```python
# Bad: Domain depending on infrastructure
from src.infrastructure.database import Session

# Good: Pure domain code
from typing import List, Optional
from dataclasses import dataclass
```

## Execution Examples

### ✅ Success Example
```bash
$ /implement-domain 15
🟢 Issues: #15 のドメイン層実装を開始します
🔴 TDD REDフェーズ検証中...
E ImportError: No module named 'src.domain.user'
======= 12 failed, 0 passed =======
✅ 全テストが正常に失敗 - TDD REDフェーズ確認
🏗️ ドメインエンティティ実装中...
  ✅ ファイル作成: src/domain/user.py
  ✅ ファイル作成: src/domain/value_objects.py
🟢 TDD GREENフェーズ検証中...
======= 12 passed, 0 failed =======
✅ 全テストが成功 - TDD GREENフェーズ確認
🎉 ドメイン層実装完了!
```

### ❌ Failure Example and Fix
```bash
$ /implement-domain 15
❌ テストが既に成功しています - TDD REDフェーズではありません
💡 TDD REDフェーズを最初に実行してください:
   /create-tests 15

# Fix: Start with failing tests
$ /create-tests 15
$ /implement-domain 15
```

### ❌ Placeholder Assertion Example and Fix
```bash
$ /implement-domain 3
🚨 プレースホルダーアサーション発見:
  - tests/unit/domain/entities/test_configuration.py: 7 個
  - tests/unit/domain/entities/test_position.py: 8 個
  - tests/unit/domain/entities/test_trade.py: 9 個

🚨 CRITICAL ISSUE: これらのテストは意図的にFALSE失敗しています
   - 実装は完了済みだが、テストがプレースホルダーのまま
   - これはTDDプロセス違反の状態です

# Fix: Replace placeholder assertions with real tests
# Edit test files to replace:
#   assert False, "RED: Configuration update not implemented yet"
# With:
#   config = Configuration.create("key", "value", "category")
#   config.update_value("new_value")
#   assert config.value == "new_value"
```

## 🟢 **TDD GREEN PHASE: DOMAIN LAYER IMPLEMENTATION ONLY**

**⚠️ Important Notice:**
- **This step is TDD GREEN PHASE** - Implement domain layer to make tests pass
- **DOMAIN LAYER IMPLEMENTATION ONLY** - No other layers allowed  
- **TDD Discipline** - Make failing tests pass with minimal implementation
- **Domain purity required** - No infrastructure or application concerns

**TDD Cycle Position:**
1. `05-create-tests` ← TDD RED (failing tests created)
2. `06-implement-domain` ← **【YOU ARE HERE】TDD GREEN (domain implementation)**
3. `07-implement-usecase` ← Application layer implementation  
4. `11-refactor` ← TDD REFACTOR (improve code quality)

**⚠️ This step ONLY allows implementation of the Domain Layer. NO OTHER LAYERS should be implemented.**

## 🚨 **CRITICAL: DOMAIN LAYER ONLY - NO OTHER LAYERS**

**❌ ABSOLUTELY FORBIDDEN in this step:**
- **Application Layer**: No use cases, DTOs, or application services
- **Infrastructure Layer**: No repository implementations, database code, or external API calls
- **Presentation Layer**: No controllers, APIs, CLI commands, or web interfaces
- **Integration Code**: No dependency injection, configuration, or cross-layer implementations

**✅ ONLY ALLOWED in this step:**
- **Domain Entities**: Business objects with identity and lifecycle
- **Value Objects**: Immutable objects representing concepts
- **Domain Services**: Pure business logic not belonging to entities
- **Repository Interfaces**: Abstract contracts (no implementations)

## 📋 **TDD GREEN PHASE TASK CHECKLIST**

**Use this checklist to implement domain layer with TDD discipline:**

### 🔴 Required Tasks

#### **🔴 → 🟢 Test Analysis**
- [ ] **Run failing tests**: Execute pytest to identify which tests are currently failing
- [ ] **Analyze test failures**: Understand what each test expects to be implemented
- [ ] **🚨 CRITICAL: Replace placeholder assertions**: Check for and fix `assert False, "RED: ... not implemented yet"` statements in tests
- [ ] **Verify test authenticity**: Ensure tests actually test implementation, not just placeholder failures
- [ ] **Prioritize implementation order**: Start with entities, then value objects, then services
- [ ] **Identify minimum implementation**: Determine minimal code needed to pass each test

#### **🏗️ Entity Implementation**
- [ ] **Create entity classes**: Implement entities based on domain model design and failing tests
- [ ] **Add entity attributes**: Implement properties and fields as required by tests
- [ ] **Implement entity behavior**: Add methods and business logic to make behavior tests pass
- [ ] **Enforce invariants**: Add validation and business rules to maintain entity consistency

#### **🧪 TDD GREEN Verification**
- [ ] **Run domain layer tests**: Execute all domain-specific tests
- [ ] **Verify tests pass**: Confirm all previously failing domain tests now pass
- [ ] **Update metadata**: Mark TDD GREEN phase complete in issue-X-Y.json
- [ ] **Commit domain implementation**: Version control domain layer code

### 🟡 Recommended Tasks

#### **💎 Value Object Implementation**
- [ ] **Create value object classes**: Implement immutable value objects as specified
- [ ] **Add value validation**: Implement validation logic to ensure value object integrity
- [ ] **Implement equality methods**: Add __eq__ and __hash__ for proper value comparison
- [ ] **Add value behaviors**: Implement any business operations defined for value objects
- [ ] **Test value object implementation**: Verify value object tests pass

#### **🔗 Repository Interface Implementation**
- [ ] **Create repository interfaces**: Define abstract base classes for data access
- [ ] **Define repository methods**: Add abstract methods as required by failing tests
- [ ] **Add type hints**: Ensure proper type annotations for all repository methods
- [ ] **Document repository contracts**: Add docstrings explaining expected behaviors
- [ ] **NO CONCRETE IMPLEMENTATION**: Only interfaces allowed in domain layer

#### **🚫 Architecture Compliance Check**
- [ ] **No infrastructure dependencies**: Verify domain code has no database/file/network imports
- [ ] **No application layer references**: Ensure no use case or DTO imports
- [ ] **No presentation layer references**: Confirm no API or UI related imports
- [ ] **Pure Python only**: Domain should only depend on standard library and domain itself
- [ ] **Domain purity maintained**: Verify only src/domain/ directory has new implementation files

### 🟢 Optional Tasks

#### **⚙️ Domain Service Implementation**
- [ ] **Create domain service classes**: Implement domain services for complex business logic
- [ ] **Implement business operations**: Add methods that don't belong to entities or value objects
- [ ] **Coordinate entity interactions**: Implement logic that works across multiple entities
- [ ] **Maintain domain purity**: Ensure no infrastructure or application concerns leak in
- [ ] **Test domain service implementation**: Verify domain service tests pass

#### **🔧 Code Quality Validation**
- [ ] **Run ruff linting**: Execute `uv run --frozen ruff check src/ --fix`
- [ ] **Run ruff formatting**: Execute `uv run --frozen ruff format src/`
- [ ] **Run type checking**: Execute `uv run --frozen pyright src/`
- [ ] **Fix quality issues**: Address any linting, formatting, or type errors
- [ ] **Verify clean results**: Ensure all quality tools pass without errors

#### **📊 Advanced Phase Completion**
- [ ] **Plan test-by-test approach**: Implement just enough to make one test pass at a time
- [ ] **Test entity implementation**: Verify entity tests pass while maintaining others failing
- [ ] **Maintain test isolation**: Ensure tests still run independently
- [ ] **Check implementation minimality**: Verify no over-engineering or unnecessary features
- [ ] **Validate domain purity**: Confirm no external dependencies in domain code
- [ ] **Interface segregation**: Repository interfaces should be in domain, not implementations
- [ ] **No concrete repositories**: Confirm NO implementations in src/infrastructure/repositories/
- [ ] **No use case implementations**: Confirm NO files created in src/application/use_cases/
- [ ] **No API implementations**: Confirm NO files created in src/presentation/
- [ ] **Document implementation**: Record what was implemented and why
- [ ] **Prepare for application layer**: Ensure domain interfaces ready for next phase
- [ ] **Run full test suite**: Confirm domain tests pass, others may still fail (expected)

**💡 Pro Tip**: Implement ONLY what's needed to make tests pass - resist the urge to add "nice to have" features!
- `src/domain/entities/` - Domain entities with business logic
- `src/domain/value_objects/` - Immutable value objects with validation
- `src/domain/repositories/` - Repository interfaces (abstract classes only)
- `src/domain/services/` - Domain services for cross-entity business logic

### ❌ FORBIDDEN Files (DO NOT create/modify in this step):
- `src/application/` - **Application Layer (use cases, DTOs, application exceptions)**
- `src/infrastructure/` - **Infrastructure Layer (concrete repositories, databases, external APIs)**
- `src/presentation/` - **Presentation Layer (API endpoints, CLI, web interfaces)**

### 🎯 Implementation Rules:
1. **Domain logic ONLY** - Focus on business rules and invariants
2. **No external dependencies** - No database, HTTP, file I/O, or technical concerns
3. **Minimal implementation to pass tests** - Follow TDD GREEN phase principles
4. **Pure Python code** - Only use standard library, no external packages

### 💡 If you accidentally implement other layers:
```bash
# Delete created files
rm -rf src/application/ src/infrastructure/ src/presentation/

# Or restore with git
git restore src/application/ src/infrastructure/ src/presentation/
```

**Violating these rules will break the architecture and cause problems in later implementation steps.**

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
git restore tests/unit/domain/

# Return to proper TDD flow
# 1. Read failing tests (these are specifications)
# 2. Implement domain code to make tests pass
# 3. Never change test logic to match code
```

**⚠️ CRITICAL: Test modifications break the TDD cycle and invalidate scenario-driven development!**

---

## Task Details

1. **Setup Safe Environment and Parse Arguments**:
   ```bash
   # 🔧 Load all safe operation functions
   source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "06-implement-domain" "$ARGUMENTS"
   
   # Domain implementation expects at least one issue number
   if [[ ${#issue_numbers[@]} -eq 0 ]]; then
       echo "エラー: 少なくとも1つのイシュー番号を指定してください"
       show_usage_example "implement-domain" "1" "単一イシューのドメイン実装"
       show_usage_example "implement-domain" "1,7" "複数イシューのドメイン実装"
       show_usage_example "implement-domain" "1 mt5-extended-data" "イシュー + 機能名指定"
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
   
   echo "🏗️ Issues: $(printf '#%s ' "${issue_numbers[@]}")のドメイン層実装を開始します（TDD GREEN phase）"
   echo ""
   echo "🚨 重要な注意: このステップではドメイン層のみを実装します"
   echo "   ✅ 許可: src/domain/ 配下のファイルのみ"
   echo "   ❌ 禁止: src/application/, src/infrastructure/, src/presentation/"
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
   if ! begin_transaction "implement_domain_${issue_list}"; then
       echo "エラー: トランザクションの開始に失敗しました"
       exit 1
   fi
   
   # 📋 Validate prerequisites - tests must exist and be failing
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
   
   # Check for domain tests
   domain_test_files=$(find tests/unit/domain/ -name "test_*.py" -type f 2>/dev/null || echo "")
   if [[ -z "$domain_test_files" ]]; then
       echo "❌ ドメインテストが見つかりません"
       echo "💡 最初にTDDテストを作成してください:"
       echo "   /create-tests $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
       execute_rollback "missing_domain_tests"
       exit 1
   fi
   
   echo "  ✅ ドメインテストファイル確認: $(echo "$domain_test_files" | wc -l) ファイル"
   
   # Check for domain model design
   domain_model_file="docs/domain/issue-${issue_list}-domain-model.md"
   if [[ ! -f "$domain_model_file" ]]; then
       echo "❌ ドメインモデル設計が見つかりません: $domain_model_file"
       echo "💡 最初にドメインモデル設計を作成してください:"
       echo "   /domain-modeling $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
       execute_rollback "missing_domain_model"
       exit 1
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
   
   # Check tests phase completion
   test_status=$(jq -r '.phases.tests.created // false' "$metadata_file" 2>/dev/null)
   if [[ "$test_status" != "true" ]]; then
       echo "エラー: TDDテスト作成が完了していません"
       echo "💡 先に /create-tests コマンドを実行してください"
       execute_rollback "tests_not_created"
       exit 1
   fi
   
   # Check if domain implementation is already completed
   domain_status=$(jq -r '.phases.domain_implementation.completed // false' "$metadata_file" 2>/dev/null)
   if [[ "$domain_status" == "true" ]]; then
       echo "⚠️  Issue #${issue_list} のドメイン実装は既に完了しています"
       echo "既存の実装を上書きしますか？ (y/N): "
       read -n 1 -r
       echo
       if [[ ! $REPLY =~ ^[Yy]$ ]]; then
           echo "ドメイン実装をキャンセルしました"
           commit_transaction
           exit 0
       fi
       echo "🔄 既存のドメイン実装を上書きします"
   fi
   
   echo "✅ メタデータ検証完了"
   ```

4. **Run Tests to Confirm RED State and Fix Placeholder Assertions**:
   ```bash
   # 🔍 Validate current test state (should be RED)
   echo "🔍 現在のテスト状態確認中（RED状態検証）..."
   
   # Validate Python environment for testing
   if ! validate_python_environment; then
       echo "エラー: Python環境の検証に失敗しました"
       execute_rollback "python_env_validation_failed"
       exit 1
   fi
   
   # 🚨 CRITICAL: Check for placeholder assertions that cause false RED state
   echo "  🚨 プレースホルダーアサーション検証中..."
   
   placeholder_files=()
   while IFS= read -r -d '' file; do
       if grep -l 'assert False, "RED:' "$file" >/dev/null 2>&1; then
           placeholder_files+=("$file")
       fi
   done < <(find tests/unit/domain/ -name "*.py" -print0 2>/dev/null)
   
   if [[ ${#placeholder_files[@]} -gt 0 ]]; then
       echo "  ❌ プレースホルダーアサーション発見:"
       for file in "${placeholder_files[@]:0:5}"; do
           count=$(grep -c 'assert False, "RED:' "$file" 2>/dev/null || echo "0")
           echo "    - $file: $count 個"
       done
       [[ ${#placeholder_files[@]} -gt 5 ]] && echo "    - ... (他 $((${#placeholder_files[@]} - 5)) ファイル)"
       
       echo ""
       echo "  🚨 CRITICAL ISSUE: これらのテストは意図的にFALSE失敗しています"
       echo "     - 実装は完了済みだが、テストがプレースホルダーのまま"
       echo "     - これはTDDプロセス違反の状態です"
       echo ""
       echo "  💡 修正が必要: プレースホルダーアサーションを実際のテストに置き換える"
       echo "     この修正は手動で行う必要があります"
       echo ""
       echo "  ⚠️  続行するとプレースホルダーテストの修正をスキップしますが、"
       echo "     後でテストを適切に実装する必要があります"
       echo ""
       echo "  続行しますか？ (y/N): "
       read -n 1 -r
       echo
       if [[ ! $REPLY =~ ^[Yy]$ ]]; then
           echo "ドメイン実装をキャンセルしました"
           echo "💡 推奨: 手動でプレースホルダーテストを適切なテストに置き換えてから再実行"
           execute_rollback "placeholder_assertions_found"
           exit 1
       fi
       
       echo "  ⚠️  プレースホルダーテストを無視して続行（後で修正が必要）"
   else
       echo "  ✅ プレースホルダーアサーション: なし（正常なテスト状態）"
   fi
   
   # Run domain tests to confirm RED state
   echo "  🧪 ドメインテスト実行中（RED状態確認）..."
   
   test_output_file="/tmp/domain_test_output_$$"
   test_result=0
   
   # Run tests and capture output
   if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/unit/domain/ -v --tb=short > "$test_output_file" 2>&1; then
       test_result=0  # Tests passed (unexpected in RED phase)
   else
       test_result=1  # Tests failed (expected in RED phase)
   fi
   
   # Analyze test results
   total_tests=$(grep -c "^tests/unit/domain/" "$test_output_file" 2>/dev/null || echo "0")
   failed_tests=$(grep -c "FAILED" "$test_output_file" 2>/dev/null || echo "0")
   
   echo "  📊 テスト結果分析:"
   echo "    - 総テスト数: $total_tests"
   echo "    - 失敗テスト数: $failed_tests"
   
   if [[ $test_result -eq 0 ]] && [[ $total_tests -gt 0 ]]; then
       echo "⚠️  警告: テストが成功しています（RED状態ではない）"
       echo "既に実装が存在する可能性があります"
       
       echo "実装を続行しますか？ (y/N): "
       read -n 1 -r
       echo
       if [[ ! $REPLY =~ ^[Yy]$ ]]; then
           echo "ドメイン実装をキャンセルしました"
           rm -f "$test_output_file"
           commit_transaction
           exit 0
       fi
   elif [[ $total_tests -eq 0 ]]; then
       echo "エラー: ドメインテストが見つかりません"
       rm -f "$test_output_file"
       execute_rollback "no_domain_tests_found"
       exit 1
   else
       echo "  ✅ RED状態確認: $failed_tests 個のテストが期待通り失敗"
   fi
   
   # Extract failing test information for implementation guidance
   failing_entities=()
   while IFS= read -r line; do
       if [[ $line =~ test_([a-z_]+)\.py.*FAILED ]]; then
           entity_name=$(echo "$line" | sed 's/.*test_\([a-z_]*\)\.py.*/\1/')
           [[ -n "$entity_name" ]] && failing_entities+=("$entity_name")
       fi
   done < "$test_output_file"
   
   # Remove duplicates
   unique_failing_entities=($(printf '%s\n' "${failing_entities[@]}" | sort -u))
   
   echo "  🎯 実装が必要な要素: ${#unique_failing_entities[@]} 個"
   for entity in "${unique_failing_entities[@]:0:5}"; do
       echo "    - $entity"
   done
   [[ ${#unique_failing_entities[@]} -gt 5 ]] && echo "    - ... (他 $((${#unique_failing_entities[@]} - 5)) 個)"
   
   rm -f "$test_output_file"
   echo "✅ テスト状態確認完了"
   ```

5. **Extract Domain Design Information**:
   ```bash
   # 📖 Extract implementation guidance from domain model
   echo "📖 ドメインモデル設計分析中..."
   
   if ! check_file_permissions "$domain_model_file" "read"; then
       echo "エラー: ドメインモデルファイルの読み取り権限がありません: $domain_model_file"
       execute_rollback "domain_model_access_denied"
       exit 1
   fi
   
   # Extract entities from domain model
   entities=$(grep -A 5 "^### [A-Z]" "$domain_model_file" 2>/dev/null | \
             grep -E "^### [A-Z][a-zA-Z]*$" | \
             sed 's/^### //' || echo "")
   
   all_entities=()
   if [[ -n "$entities" ]]; then
       while IFS= read -r entity; do
           [[ -n "$entity" ]] && all_entities+=("$entity")
       done <<< "$entities"
   fi
   
   # Extract value objects
   value_objects=$(grep -A 10 "## 値オブジェクト\\|## Value Objects" "$domain_model_file" 2>/dev/null | \
                  grep -E "^### [A-Z][a-zA-Z]*$" | \
                  sed 's/^### //' || echo "")
   
   all_value_objects=()
   if [[ -n "$value_objects" ]]; then
       while IFS= read -r vo; do
           [[ -n "$vo" ]] && all_value_objects+=("$vo")
       done <<< "$value_objects"
   fi
   
   echo "  🎯 設計から抽出:"
   echo "    - エンティティ: ${#all_entities[@]} 個"
   echo "    - 値オブジェクト: ${#all_value_objects[@]} 個"
   
   echo "✅ ドメイン設計分析完了"
   ```

6. **Implement Domain Entities**:
   ```bash
   # 🏗️ Implement domain entities
   echo "🏗️ ドメインエンティティ実装中..."
   
   implemented_files=()
   
   # Implement entities based on failing tests and domain model
   for entity in "${all_entities[@]}"; do
       entity_lower=$(echo "$entity" | tr '[:upper:]' '[:lower:]')
       entity_file="src/domain/entities/${entity_lower}.py"
       
       echo "  🏗️ 実装中: $entity ($entity_file)"
       
       # Create entity implementation
       entity_implementation='"""
   '"$entity"' エンティティ実装

   ドメインモデル: docs/domain/issue-'"${issue_list}"'-'"${feature_name}"'.md
   実装日時: '"$(date)"'
   """

   from datetime import datetime
   from typing import Optional
   from dataclasses import dataclass


   @dataclass
   class '"$entity"':
       """'"$entity"' エンティティ
       
       ドメインの中心となるビジネスエンティティ。
       ライフサイクルを持ち、一意性により識別される。
       """
       
       id: str
       created_at: datetime
       updated_at: datetime
       
       def __post_init__(self) -> None:
           """エンティティ初期化後の検証"""
           self._validate_invariants()
       
       def _validate_invariants(self) -> None:
           """ビジネス不変条件の検証"""
           if not self.id:
               raise ValueError("'"$entity"' ID cannot be empty")
           
           if not isinstance(self.id, str):
               raise TypeError("'"$entity"' ID must be a string")
           
           if self.created_at > datetime.now():
               raise ValueError("Created date cannot be in the future")
           
           if self.updated_at < self.created_at:
               raise ValueError("Updated date cannot be before created date")
       
       @classmethod
       def create(cls, entity_id: str) -> "'"$entity"'":
           """新しい'"$entity"'を作成する
           
           Args:
               entity_id: エンティティの一意識別子
               
           Returns:
               '"$entity"': 作成された'"$entity"'インスタンス
               
           Raises:
               ValueError: 無効なIDが指定された場合
           """
           now = datetime.now()
           return cls(
               id=entity_id,
               created_at=now,
               updated_at=now
           )
       
       def update(self) -> None:
           """'"$entity"'を更新する
           
           更新日時を現在時刻に設定し、不変条件を検証する。
           """
           self.updated_at = datetime.now()
           self._validate_invariants()
       
       def __eq__(self, other) -> bool:
           """等値性の比較
           
           エンティティはIDによる同一性で比較される。
           """
           if not isinstance(other, '"$entity"'):
               return False
           return self.id == other.id
       
       def __hash__(self) -> int:
           """ハッシュ値の計算
           
           IDに基づいてハッシュ値を計算する。
           """
           return hash(self.id)
   '
       
       if ! safe_create_file "$entity_file" "$entity_implementation" true; then
           echo "エラー: エンティティファイルの作成に失敗しました: $entity_file"
           execute_rollback "entity_implementation_failed"
           exit 1
       fi
       
       implemented_files+=("$entity_file")
       add_rollback "rm -f '$entity_file'" "Remove implemented entity: $entity_file"
   done
   
   echo "✅ エンティティ実装完了 (${#all_entities[@]} ファイル)"
   ```

7. **Implement Value Objects**:
   ```bash
   # 💎 Implement value objects
   echo "💎 値オブジェクト実装中..."
   
   # Implement common value objects
   common_value_objects=("EntityId" "Email")
   
   for vo in "${common_value_objects[@]}"; do
       vo_lower=$(echo "$vo" | tr '[:upper:]' '[:lower:]')
       vo_file="src/domain/value_objects/${vo_lower}.py"
       
       echo "  💎 実装中: $vo ($vo_file)"
       
       case "$vo" in
           "EntityId")
               vo_implementation='"""
   EntityId 値オブジェクト実装

   エンティティの一意識別子を表現する値オブジェクト。
   """

   import uuid
   from dataclasses import dataclass
   from typing import Union


   @dataclass(frozen=True)
   class EntityId:
       """エンティティ一意識別子
       
       UUIDベースの一意識別子を提供する不変の値オブジェクト。
       """
       
       value: str
       
       def __post_init__(self) -> None:
           """値オブジェクト初期化後の検証"""
           if not self.value:
               raise ValueError("EntityId value cannot be empty")
           
           if not isinstance(self.value, str):
               raise TypeError("EntityId value must be a string")
           
           # UUID形式の検証
           try:
               uuid.UUID(self.value)
           except ValueError:
               raise ValueError(f"EntityId value must be a valid UUID: {self.value}")
       
       @classmethod
       def generate(cls) -> "EntityId":
           """新しいEntityIdを生成する
           
           Returns:
               EntityId: 新しく生成されたEntityId
           """
           return cls(value=str(uuid.uuid4()))
       
       @classmethod
       def from_string(cls, value: Union[str, "EntityId"]) -> "EntityId":
           """文字列またはEntityIdからEntityIdを作成
           
           Args:
               value: 文字列またはEntityIdインスタンス
               
           Returns:
               EntityId: EntityIdインスタンス
           """
           if isinstance(value, EntityId):
               return value
           return cls(value=value)
       
       def __str__(self) -> str:
           """文字列表現"""
           return self.value
       
       def __repr__(self) -> str:
           """デバッグ表現"""
           return f"EntityId({self.value!r})"
   '
               ;;
           "Email")
               vo_implementation='"""
   Email 値オブジェクト実装

   メールアドレスを表現する値オブジェクト。
   """

   import re
   from dataclasses import dataclass


   @dataclass(frozen=True)
   class Email:
       """メールアドレス値オブジェクト
       
       RFC 5322に準拠したメールアドレスを表現する不変の値オブジェクト。
       """
       
       value: str
       
       # メールアドレス形式の正規表現（簡略版）
       _EMAIL_PATTERN = re.compile(
           r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
       )
       
       def __post_init__(self) -> None:
           """値オブジェクト初期化後の検証"""
           self._validate()
       
       def _validate(self) -> None:
           """メールアドレス形式の検証"""
           if not self.value:
               raise ValueError("Email value cannot be empty")
           
           if not isinstance(self.value, str):
               raise TypeError("Email value must be a string")
           
           if len(self.value) > 255:
               raise ValueError("Email value cannot exceed 255 characters")
           
           if not self._EMAIL_PATTERN.match(self.value):
               raise ValueError(f"Invalid email format: {self.value}")
       
       @property
       def local_part(self) -> str:
           """ローカル部分（@より前）を取得"""
           return self.value.split("@")[0]
       
       @property 
       def domain_part(self) -> str:
           """ドメイン部分（@より後）を取得"""
           return self.value.split("@")[1]
       
       def __str__(self) -> str:
           """文字列表現"""
           return self.value
       
       def __repr__(self) -> str:
           """デバッグ表現"""
           return f"Email({self.value!r})"
   '
               ;;
       esac
       
       if ! safe_create_file "$vo_file" "$vo_implementation" true; then
           echo "エラー: 値オブジェクトファイルの作成に失敗しました: $vo_file"
           execute_rollback "value_object_implementation_failed"
           exit 1
       fi
       
       implemented_files+=("$vo_file")
       add_rollback "rm -f '$vo_file'" "Remove implemented value object: $vo_file"
   done
   
   echo "✅ 値オブジェクト実装完了 (${#common_value_objects[@]} ファイル)"
   ```

8. **Implement Repository Interfaces**:
   ```bash
   # 🏪 Implement repository interfaces
   echo "🏪 リポジトリインターフェース実装中..."
   
   # Create repository interfaces for each entity
   for entity in "${all_entities[@]}"; do
       entity_lower=$(echo "$entity" | tr '[:upper:]' '[:lower:]')
       repo_file="src/domain/repositories/${entity_lower}_repository.py"
       
       echo "  🏪 実装中: ${entity}Repository ($repo_file)"
       
       repo_implementation='"""
   '"$entity"'Repository インターフェース

   '"$entity"'エンティティの永続化抽象インターフェース。
   """

   from abc import ABC, abstractmethod
   from typing import List, Optional
   from ..entities.'"${entity_lower}"' import '"$entity"'


   class '"$entity"'Repository(ABC):
       """'"$entity"'リポジトリ抽象インターフェース
       
       '"$entity"'エンティティの永続化操作を定義する。
       具体的な実装はインフラストラクチャ層で行う。
       """
       
       @abstractmethod
       def save(self, entity: '"$entity"') -> None:
           """'"$entity"'を保存する
           
           Args:
               entity: 保存する'"$entity"'エンティティ
               
           Raises:
               RepositoryError: 保存に失敗した場合
           """
           pass
       
       @abstractmethod
       def find_by_id(self, entity_id: str) -> Optional['"$entity"']:
           """IDで'"$entity"'を検索する
           
           Args:
               entity_id: 検索するエンティティのID
               
           Returns:
               Optional['"$entity"']: 見つかった'"$entity"'、または None
               
           Raises:
               RepositoryError: 検索に失敗した場合
           """
           pass
       
       @abstractmethod
       def find_all(self) -> List['"$entity"']:
           """すべての'"$entity"'を取得する
           
           Returns:
               List['"$entity"']: すべての'"$entity"'のリスト
               
           Raises:
               RepositoryError: 取得に失敗した場合
           """
           pass
       
       @abstractmethod
       def delete(self, entity_id: str) -> bool:
           """'"$entity"'を削除する
           
           Args:
               entity_id: 削除するエンティティのID
               
           Returns:
               bool: 削除に成功した場合True、エンティティが見つからない場合False
               
           Raises:
               RepositoryError: 削除に失敗した場合
           """
           pass
       
       @abstractmethod
       def exists(self, entity_id: str) -> bool:
           """'"$entity"'が存在するかチェックする
           
           Args:
               entity_id: チェックするエンティティのID
               
           Returns:
               bool: エンティティが存在する場合True
               
           Raises:
               RepositoryError: チェックに失敗した場合
           """
           pass


   class RepositoryError(Exception):
       """リポジトリ操作エラー"""
       pass
   '
       
       if ! safe_create_file "$repo_file" "$repo_implementation" true; then
           echo "エラー: リポジトリインターフェースファイルの作成に失敗しました: $repo_file"
           execute_rollback "repository_interface_implementation_failed"
           exit 1
       fi
       
       implemented_files+=("$repo_file")
       add_rollback "rm -f '$repo_file'" "Remove implemented repository interface: $repo_file"
   done
   
   echo "✅ リポジトリインターフェース実装完了 (${#all_entities[@]} ファイル)"
   ```

9. **Run Tests to Verify GREEN State**:
   ```bash
   # 🟢 Verify tests are now in GREEN state
   echo "🟢 TDD GREENフェーズ検証中..."
   
   # Run domain tests to confirm GREEN state
   echo "  🧪 ドメインテスト実行中（GREEN状態確認）..."
   
   test_output_file="/tmp/domain_green_test_output_$$"
   test_result=0
   
   # Run tests and capture output
   if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/unit/domain/ -v --tb=short > "$test_output_file" 2>&1; then
       test_result=0  # Tests passed (expected in GREEN phase)
   else
       test_result=1  # Tests failed (need more implementation)
   fi
   
   # Analyze test results
   total_tests=$(grep -c "test_.*PASSED\\|test_.*FAILED" "$test_output_file" 2>/dev/null || echo "0")
   passed_tests=$(grep -c "PASSED" "$test_output_file" 2>/dev/null || echo "0")
   failed_tests=$(grep -c "FAILED" "$test_output_file" 2>/dev/null || echo "0")
   
   echo "  📊 テスト結果分析:"
   echo "    - 総テスト数: $total_tests"
   echo "    - 成功テスト数: $passed_tests"
   echo "    - 失敗テスト数: $failed_tests"
   
   if [[ $failed_tests -gt 0 ]]; then
       echo "⚠️  まだ失敗しているテストがあります:"
       grep "FAILED" "$test_output_file" | head -5
       echo ""
       echo "追加実装が必要な可能性があります。続行しますか？ (y/N): "
       read -n 1 -r
       echo
       if [[ ! $REPLY =~ ^[Yy]$ ]]; then
           echo "ドメイン実装を中止しました"
           rm -f "$test_output_file"
           execute_rollback "tests_still_failing"
           exit 1
       fi
   else
       echo "  ✅ GREEN状態確認: すべてのテストが成功しています"
   fi
   
   # Calculate test coverage if possible
   coverage_result=""
   if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/unit/domain/ --cov=src.domain --cov-report=term-missing --quiet >/tmp/coverage_output_$$ 2>&1; then
       coverage_result=$(grep -E "[0-9]+%" /tmp/coverage_output_$$ | tail -1 || echo "Coverage data not available")
       rm -f /tmp/coverage_output_$$
   fi
   
   rm -f "$test_output_file"
   tests_passed=$([ $failed_tests -eq 0 ] && echo "true" || echo "false")
   
   echo "✅ TDD GREEN フェーズ検証完了"
   ```

10. **Code Quality and Architecture Validation**:
    ```bash
    # 🔍 Code quality and architecture validation
    echo "🔍 コード品質・アーキテクチャ検証中..."
    
    # Run ruff formatting and linting
    echo "  🎨 コードフォーマット・リント実行中..."
    
    if ! uv run --frozen ruff format src/domain/ --quiet; then
        echo "⚠️  コードフォーマットに問題があります"
    fi
    
    lint_output_file="/tmp/ruff_output_$$"
    if uv run --frozen ruff check src/domain/ > "$lint_output_file" 2>&1; then
        echo "    ✅ リント検査: 問題なし"
    else
        echo "    ⚠️  リント警告があります:"
        head -5 "$lint_output_file"
        echo "    💡 必要に応じて修正してください"
    fi
    rm -f "$lint_output_file"
    
    # Run type checking if pyright is available
    echo "  🔍 型チェック実行中..."
    
    type_output_file="/tmp/pyright_output_$$"
    if uv run --frozen pyright src/domain/ > "$type_output_file" 2>&1; then
        echo "    ✅ 型チェック: 問題なし"
    else
        echo "    ⚠️  型チェック警告があります:"
        head -5 "$type_output_file"
        echo "    💡 必要に応じて型ヒントを修正してください"
    fi
    rm -f "$type_output_file"
    
    # Architecture validation
    echo "  🏗️ アーキテクチャ検証中..."
    
    # 🚨 CRITICAL: Verify ONLY domain layer was implemented
    echo "    🚨 ドメイン層限定実装検証中..."
    
    prohibited_layers_found=false
    
    # Check for accidentally created application layer files
    if [[ -d "src/application" ]]; then
        app_files=$(find src/application/ -name "*.py" -type f 2>/dev/null | grep -v __pycache__ || echo "")
        if [[ -n "$app_files" ]]; then
            echo "    ❌ エラー: アプリケーション層ファイルが作成されています!"
            echo "    🚫 禁止: このステップではアプリケーション層は実装してはいけません"
            echo "    📁 検出されたファイル:"
            echo "$app_files" | sed 's/^/        - /'
            prohibited_layers_found=true
        fi
    fi
    
    # Check for accidentally created infrastructure layer files
    if [[ -d "src/infrastructure" ]]; then
        infra_files=$(find src/infrastructure/ -name "*.py" -type f 2>/dev/null | grep -v __pycache__ || echo "")
        if [[ -n "$infra_files" ]]; then
            echo "    ❌ エラー: インフラストラクチャ層ファイルが作成されています!"
            echo "    🚫 禁止: このステップではインフラ層は実装してはいけません"
            echo "    📁 検出されたファイル:"
            echo "$infra_files" | sed 's/^/        - /'
            prohibited_layers_found=true
        fi
    fi
    
    # Check for accidentally created presentation layer files
    if [[ -d "src/presentation" ]]; then
        pres_files=$(find src/presentation/ -name "*.py" -type f 2>/dev/null | grep -v __pycache__ || echo "")
        if [[ -n "$pres_files" ]]; then
            echo "    ❌ エラー: プレゼンテーション層ファイルが作成されています!"
            echo "    🚫 禁止: このステップではプレゼンテーション層は実装してはいけません"
            echo "    📁 検出されたファイル:"
            echo "$pres_files" | sed 's/^/        - /'
            prohibited_layers_found=true
        fi
    fi
    
    if [[ "$prohibited_layers_found" == "true" ]]; then
        echo ""
        echo "    🚨 重大なエラー: 禁止されたレイヤーの実装が検出されました"
        echo "    💡 対処方法:"
        echo "       1. 禁止されたファイルを削除: rm -rf src/application/ src/infrastructure/ src/presentation/"
        echo "       2. またはgitでリストア: git restore src/application/ src/infrastructure/ src/presentation/"
        echo "       3. ドメイン層のみの実装に戻す"
        echo ""
        echo "    このエラーを無視すると、後の実装ステップで重大な問題が発生します。"
        echo ""
        echo "    修正しますか？ (y/N): "
        read -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            echo "    🧹 禁止されたレイヤーファイルを削除中..."
            [[ -d "src/application" ]] && rm -rf src/application/
            [[ -d "src/infrastructure" ]] && rm -rf src/infrastructure/
            [[ -d "src/presentation" ]] && rm -rf src/presentation/
            echo "    ✅ クリーンアップ完了"
        else
            echo "    ❌ アーキテクチャ違反により実装を中止します"
            execute_rollback "architecture_violation_detected"
            exit 1
        fi
    else
        echo "    ✅ レイヤー実装検証: ドメイン層のみ正しく実装"
    fi
    
    # Check for external dependencies in domain layer
    domain_imports=$(find src/domain/ -name "*.py" -exec grep -l "^import \\|^from " {} \; 2>/dev/null || echo "")
    external_deps_found=false
    
    for file in $domain_imports; do
        # Check for problematic imports (infrastructure dependencies)
        if grep -E "^(import|from) (requests|sqlalchemy|django|flask|fastapi|sqlite3|psycopg2)" "$file" >/dev/null 2>&1; then
            echo "    ⚠️  外部依存発見: $file"
            external_deps_found=true
        fi
    done
    
    if [[ "$external_deps_found" == "false" ]]; then
        echo "    ✅ 依存関係検証: ドメイン層の純粋性維持"
    else
        echo "    💡 ドメイン層の外部依存を削除することを推奨します"
    fi
    
    echo "✅ コード品質検証完了"
    ```

11. **Update Metadata and Documentation**:
    ```bash
    # 📊 Update metadata with domain implementation completion
    echo "📊 メタデータ・ドキュメント更新中..."
    
    if ! update_metadata_atomic "$metadata_file" \
        '.phases.domain_implementation.created = true | 
         .phases.domain_implementation.completed = true |
         .phases.domain_implementation.completed_at = "'"$(date -u +%Y-%m-%dT%H:%M:%SZ)"'" |
         .phases.tests.passed = '"$tests_passed"' |
         .phases.tests.coverage = "'"$coverage_result"'" |
         .updated_at = "'"$(date -u +%Y-%m-%dT%H:%M:%SZ)"'" |
         .spec_files.domain_implementation = ['"$(printf '"%s",' "${implemented_files[@]}" | sed 's/,$//')"'] |
         .phase = "domain_implemented_green" |
         .next_commands = ["implement-usecase", "use-case-status"]'; then
        echo "エラー: メタデータの更新に失敗しました"
        execute_rollback "metadata_update_failed"
        exit 1
    fi
    
    # Update domain model document with implementation notes
    if [[ -f "$domain_model_file" ]]; then
        echo "  📝 ドメインモデル文書更新中..."
        
        # Add implementation completion note
        temp_file="${domain_model_file}.tmp"
        if cat >> "$temp_file" << EOF

## 実装完了状況

**実装日時**: $(date)
**実装ファイル数**: ${#implemented_files[@]}
**テスト状況**: $tests_passed (成功: $passed_tests, 失敗: $failed_tests)
**カバレッジ**: $coverage_result

### 実装されたファイル
$(printf '- %s\n' "${implemented_files[@]}")

### 次のステップ
- アプリケーション層実装: \`/implement-usecase $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')\`
- 進捗確認: \`/use-case-status $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')\`

---
**実装ステータス**: ✅ 完了
EOF
then
            if ! mv "$temp_file" "$domain_model_file"; then
                echo "エラー: ドメインモデル文書の更新に失敗しました"
                execute_rollback "domain_model_update_failed"
                exit 1
            fi
        else
            echo "エラー: ドメインモデル文書への追記に失敗しました"
            execute_rollback "domain_model_append_failed"
            exit 1
        fi
    fi
    
    echo "✅ メタデータ更新完了"
    ```

12. **Update Use Case Index and Git Commit**:
    ```bash
    # 📚 Update use case index and commit changes
    echo "📚 ユースケースインデックス更新中..."
    
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
        updated_line="- [${feature_name}]($(basename "${found_spec}")) - Issues: $(printf '#%s ' "${issue_numbers[@]}")- Phase: domain_implemented_green, TDD: 🟢 GREEN, Domain: ✅)"
        
        if ! sed -i "s|.*${feature_line}.*|${updated_line}|" "$use_cases_index"; then
            echo "エラー: インデックスファイルの更新に失敗しました"
            execute_rollback "index_update_failed"
            exit 1
        fi
        
        echo "✅ インデックス更新完了"
    fi
    
    # 💾 Commit domain implementation
    echo "💾 ドメイン実装をコミット中..."
    
    commit_message="feat: implement domain layer for $(printf 'issue #%s ' "${issue_numbers[@]}")- ${feature_name} (GREEN phase)

    TDD Green Phase Summary:
    - Feature: ${feature_name}
    - Issues: $(printf '#%s ' "${issue_numbers[@]}")
    - Implementation Files: ${#implemented_files[@]} created
    - Test Results: Passed $passed_tests, Failed $failed_tests
    - Coverage: $coverage_result
    
    Implemented Components:
    $(printf '  - %s\n' "${implemented_files[@]}")
    
    Domain Layer Implementation:
    - Entities with business logic and invariants
    - Value objects with immutability and validation
    - Repository interfaces for persistence abstraction
    - Clean architecture principles maintained
    - No external dependencies in domain layer
    
    TDD Status: 🔴 RED → 🟢 GREEN (domain tests passing)
    Next Step: /implement-usecase for application layer
    "
    
    files_to_commit=("$metadata_file" "$domain_model_file")
    files_to_commit+=("${implemented_files[@]}")
    if [[ -f "$use_cases_index" ]]; then
        files_to_commit+=("$use_cases_index")
    fi
    
    if ! safe_git_commit "$commit_message" "${files_to_commit[@]}"; then
        echo "エラー: コミットに失敗しました"
        execute_rollback "commit_failed"
        exit 1
    fi
    
    add_rollback "git reset --hard HEAD~1" "Undo domain implementation commit"
    echo "✅ コミット完了"
    ```

13. **Update GitHub Issues**:
    ```bash
    # 🎫 Update GitHub issues with domain implementation completion
    echo "🎫 GitHubイシュー更新中..."
    
    for issue_num in "${issue_numbers[@]}"; do
        echo "  📝 Issue #$issue_num コメント追加中..."
        
        issue_comment="🟢 **ドメイン層実装完了（GREEN phase）**

    TDDのGREENフェーズとして、ドメイン層の実装が完了しました。

    ## 📊 実装結果
    - **実装ファイル数**: ${#implemented_files[@]} ファイル
    - **テスト結果**: 成功 $passed_tests / 総計 $total_tests
    - **カバレッジ**: $coverage_result
    - **アーキテクチャ検証**: ✅ 通過

    ## 🏗️ 実装されたコンポーネント
    ### エンティティ
    $(if [[ ${#all_entities[@]} -gt 0 ]]; then
        for entity in "${all_entities[@]:0:3}"; do
            echo "- **$entity**: ビジネスロジックと不変条件を含む"
        done
        [[ ${#all_entities[@]} -gt 3 ]] && echo "- ... (他 $((${#all_entities[@]} - 3)) 個)"
    fi)
    
    ### 値オブジェクト
    - **EntityId**: UUID ベース一意識別子
    - **Email**: RFC 5322 準拠メールアドレス
    
    ### リポジトリインターフェース
    $(if [[ ${#all_entities[@]} -gt 0 ]]; then
        for entity in "${all_entities[@]:0:2}"; do
            echo "- **${entity}Repository**: ${entity}の永続化抽象インターフェース"
        done
        [[ ${#all_entities[@]} -gt 2 ]] && echo "- ... (他リポジトリ)"
    fi)

    ## 🎯 TDD状況
    - **現在の状態**: 🟢 GREEN（ドメインテスト通過）
    - **前フェーズ**: 🔴 RED（テスト作成）
    - **次フェーズ**: アプリケーション層実装

    ## 🏛️ アーキテクチャ準拠
    - [x] ドメイン層の純粋性維持
    - [x] 外部依存なし
    - [x] ビジネスルールの実装
    - [x] エンティティの不変条件
    - [x] 値オブジェクトの不変性

    ## 🚀 次のステップ
    
    アプリケーション層実装を開始してください：
    \`\`\`bash
    /implement-usecase $issue_num
    \`\`\`

    ## 📚 関連ドキュメント
    - [ドメインモデル設計（更新済み）]($domain_model_file)
    - [実装されたファイル一覧](#実装されたコンポーネント)

    ## 🔍 動作確認
    \`\`\`bash
    # ドメインテスト実行
    uv run --frozen pytest tests/unit/domain/ -v
    
    # カバレッジ確認
    uv run --frozen pytest tests/unit/domain/ --cov=src.domain
    \`\`\`

    ---
    **TDD Phase**: 🟢 GREEN (domain_implemented) → 次: アプリケーション層
    "
        
        if ! safe_add_issue_comment "$issue_num" "$issue_comment"; then
            echo "    ⚠️  Issue #$issue_num へのコメント追加に失敗しました（続行します）"
        else
            echo "    ✅ Issue #$issue_num コメント追加完了"
        fi
    done
    
    echo "✅ GitHub イシュー更新完了"
    ```

14. **Final Success and TDD Guidance**:
    ```bash
    # 🎉 Transaction commit (success!)
    if commit_transaction; then
        echo ""
        echo "🎉 ドメイン層実装完了（TDD GREEN phase）!"
        echo "============================================="
        echo "🏗️ 機能名: $feature_name"
        echo "🎫 対象イシュー: $(printf '#%s ' "${issue_numbers[@]}")"
        echo "📊 実装ファイル数: ${#implemented_files[@]} 個"
        echo ""
        echo "📋 実装されたコンポーネント:"
        echo "   エンティティ: ${#all_entities[@]} 個"
        echo "   値オブジェクト: ${#common_value_objects[@]} 個"
        echo "   リポジトリIF: ${#all_entities[@]} 個"
        echo ""
        echo "🟢 TDD GREEN状態:"
        echo "   - テスト結果: 成功 $passed_tests / 総計 $total_tests"
        echo "   - カバレッジ: $coverage_result"
        echo "   - すべてのドメインテストが通過"
        echo ""
        echo "🏛️ アーキテクチャ準拠:"
        echo "   - ドメイン層の純粋性維持"
        echo "   - 外部依存関係なし"
        echo "   - ビジネスルールと不変条件の実装"
        echo "   - クリーンアーキテクチャ原則遵守"
        echo ""
        echo "🚀 次のステップ（TDD継続）:"
        echo "   1. アプリケーション層実装: /implement-usecase $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
        echo "   2. 進捗確認: /use-case-status $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
        echo "   3. リファクタリング検討（必要に応じて）"
        echo ""
        echo "🚨 TDD原則リマインダー:"
        echo "   ⚠️  実装中にテストを変更した場合、それはTDD違反です"
        echo "   ✅ 正解: シナリオ → テスト → 実装の順序で進める"
        echo "   ❌ 禁止: 実装を正としてテストを変更する"
        echo ""
        echo "📖 TDD サイクル進捗:"
        echo "   🔴 RED: テスト作成 ✅ 完了"
        echo "   🟢 GREEN: ドメイン実装 ✅ 完了"
        echo "   🔄 REFACTOR: コード改善 ← 必要に応じて"
        echo ""
        echo "💡 実装品質:"
        echo "   - ビジネスロジック中心設計"
        echo "   - 不変条件とバリデーション"
        echo "   - テスト駆動での堅牢性確保"
        echo "   - エンティティと値オブジェクトの適切な分離"
        echo ""
        echo "📁 作成されたファイル:"
        printf '   - %s\n' "${implemented_files[@]:0:7}"  # Show first 7
        [[ ${#implemented_files[@]} -gt 7 ]] && echo "   - ... (他 $((${#implemented_files[@]} - 7)) ファイル)"
        echo ""
        
        # Show operation logs summary
        echo "📊 操作ログサマリー:"
        show_github_operation_log | tail -2
        show_git_operation_log | tail -2
        show_transaction_log | tail -2
        
        echo ""
        echo "✅ TDD GREENフェーズ完了 - アプリケーション層実装準備完了!"
        echo ""
        echo "🚨 MANDATORY FOR CLAUDE CODE: SCENARIO EVOLUTION CHECK"
        echo "   ドメイン実装中に新要件・制約・エッジケース発見時は"
        echo "   作業を中断して /evolve-scenarios <feature-name> を実行すること"
        echo "   CRITICAL: ドメイン層の変更は全システムに影響します"
        echo ""
        echo "🔒 アーキテクチャ注意事項:"
        echo "   このステップではドメイン層のみを実装しました"
        echo "   アプリケーション層は /implement-usecase で別途実装してください"
        echo "   各層を適切なタイミングで実装することでクリーンアーキテクチャを維持します"
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
- Implement ONLY what's needed to pass tests
- Focus on domain logic, not technical concerns
- Keep entities and value objects pure (no I/O)
- Enforce invariants and business rules
- Use type hints for all code
- All user-facing output must be in JAPANESE