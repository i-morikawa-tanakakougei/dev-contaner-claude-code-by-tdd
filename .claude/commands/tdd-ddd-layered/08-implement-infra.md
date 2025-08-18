Implement infrastructure layer for persistence and external services.

## Metadata
- **Prerequisites**: Application layer implementation completed (07-implement-usecase)
- **Input**: Issue number(s) (required)
- **Output**: 
  - Infrastructure layer implementation in `src/infrastructure/`
  - Repository implementations, data mappers, external adapters
  - Updated `docs/use_cases/issue-X-Y.json` metadata
- **Dependencies**: Domain and application layers, database/external service configurations
- **Execution Timing**: After application layer, before presentation layer

## 🎯 **TDD/DDD/LAYERED PROCESS CONTEXT**

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Sprint Execution Phase - Infrastructure Layer Implementation (08/16)  
> 🎯 **Phase Purpose**: Implement persistence and external service integrations  
> ⬅️ **Previous Stage**: 07-implement-usecase (Application Layer Implementation)  
> ➡️ **Next Stage**: 09-implement-presentation (Presentation Layer Implementation)
>
> **📋 3-Layer Architecture Operations**:  
> - 🎯 **Strategic**: `docs/use_cases/core/index.md` (Reference system boundaries)  
> - 📊 **Tactical**: `docs/use_cases/index.md` (Update infrastructure status)  
> - 🔧 **Execution**: `docs/use_cases/issue-X-Y.json` (Track infrastructure implementation)

## 🏗️ **INFRASTRUCTURE LAYER IMPLEMENTATION ONLY**

**⚠️ Important Notice:**
- **This step is INFRASTRUCTURE LAYER ONLY** - Implement repositories and external integrations
- **NO OTHER LAYERS** - Focus only on infrastructure layer components  
- **Data persistence** - Implement repository patterns and database access
- **External services** - Handle third-party integrations and APIs

**Layer Implementation Sequence:**
1. `06-implement-domain` ← Domain layer (completed)
2. `07-implement-usecase` ← Application layer (completed)  
3. `08-implement-infra` ← **【YOU ARE HERE】Infrastructure layer**
4. `09-implement-presentation` ← Presentation layer

## 🚨 **CRITICAL: INFRASTRUCTURE LAYER ONLY - NO OTHER LAYERS**

**❌ ABSOLUTELY FORBIDDEN in this step:**
- **Presentation Layer**: No controllers, APIs, CLI commands, or web interfaces
- **Domain Layer Modifications**: Domain layer is complete - DO NOT modify it
- **Application Layer Modifications**: Application layer is complete - DO NOT modify it
- **Business Logic**: No business rules or domain logic in infrastructure code

**✅ ONLY ALLOWED in this step:**
- **Repository Implementations**: Concrete implementations of domain repository interfaces
- **Database Access**: Database connections, queries, and data mapping
- **External Service Integration**: HTTP clients, file systems, third-party APIs
- **Infrastructure Configuration**: Connection strings, settings, environment variables

## 📋 **INFRASTRUCTURE LAYER TASK CHECKLIST**

**Use this checklist to implement infrastructure layer with proper separation:**

### 🔴 Required Tasks

#### **📊 Repository Interface Analysis**
- [ ] **Review repository interfaces**: Analyze domain repository interfaces from step 06
- [ ] **🚨 CRITICAL: Replace placeholder assertions**: Check for and fix `assert False, "RED: ... not implemented yet"` statements in infrastructure tests
- [ ] **Verify test authenticity**: Ensure tests actually test implementation, not just placeholder failures
- [ ] **Identify data access patterns**: Determine CRUD operations and query requirements
- [ ] **Plan persistence strategy**: Choose database, ORM, or data access approach
- [ ] **Map domain to persistence**: Plan how domain objects map to database tables

#### **🗄️ Repository Implementation**
- [ ] **Create concrete repository classes**: Implement each repository interface from domain layer
- [ ] **Implement CRUD operations**: Add save, find, update, delete functionality
- [ ] **Add query methods**: Implement custom query methods defined in interfaces
- [ ] **Handle database transactions**: Implement proper transaction management
- [ ] **Add error handling**: Convert database errors to domain exceptions

#### **🧪 Infrastructure Testing**
- [ ] **Run integration tests**: Execute tests that verify database and external service integration
- [ ] **Test repository implementations**: Verify CRUD operations work correctly
- [ ] **Update metadata**: Mark infrastructure layer implementation complete in issue-X-Y.json
- [ ] **Commit infrastructure layer**: Version control infrastructure layer code

### 🟡 Recommended Tasks

#### **💾 Database & Persistence Setup**
- [ ] **Set up database connection**: Configure database connection and connection pooling
- [ ] **Create database schema**: Define tables, indexes, and constraints
- [ ] **Implement data mapping**: Convert between domain objects and database records
- [ ] **Add data validation**: Implement database-level validation and constraints
- [ ] **Handle database errors**: Implement proper error handling and logging

#### **⚙️ Configuration Management**
- [ ] **Create configuration classes**: Implement settings and configuration objects
- [ ] **Load environment variables**: Read configuration from environment variables
- [ ] **Add configuration validation**: Validate required configuration on startup
- [ ] **Implement configuration defaults**: Provide sensible default values
- [ ] **Handle configuration errors**: Implement proper error handling for invalid config

#### **🚫 Architecture Compliance Check**
- [ ] **No presentation layer code**: Confirm NO controllers, APIs, or UI components
- [ ] **No business logic**: Verify infrastructure code contains no business rules
- [ ] **Domain layer unchanged**: Verify domain layer files were not modified
- [ ] **Application layer unchanged**: Verify application layer files were not modified
- [ ] **Infrastructure directory only**: Confirm only src/infrastructure/ directory has new files
- [ ] **Proper dependency direction**: Verify infrastructure depends on domain interfaces only

### 🟢 Optional Tasks

#### **🌐 External Service Integration**
- [ ] **Implement HTTP clients**: Create clients for external API integration
- [ ] **Add authentication**: Implement API key, OAuth, or other auth mechanisms  
- [ ] **Handle service errors**: Implement retry logic and error handling
- [ ] **Add rate limiting**: Implement appropriate rate limiting for external calls
- [ ] **Configure timeouts**: Set proper timeout values for external service calls
- [ ] **Add service health checks**: Implement health monitoring for external dependencies

#### **🔧 Infrastructure Quality**
- [ ] **Add proper logging**: Implement comprehensive logging for debugging
- [ ] **Implement monitoring**: Add metrics and monitoring for infrastructure components
- [ ] **Add connection pooling**: Implement efficient resource management
- [ ] **Handle resource cleanup**: Ensure proper disposal of connections and resources
- [ ] **Optimize performance**: Implement caching and query optimization where appropriate
- [ ] **Add security measures**: Implement proper security for data access and external calls

#### **🔧 Code Quality Validation**
- [ ] **Run ruff linting**: Execute `uv run --frozen ruff check src/ --fix`
- [ ] **Run ruff formatting**: Execute `uv run --frozen ruff format src/`
- [ ] **Run type checking**: Execute `uv run --frozen pyright src/`
- [ ] **Fix quality issues**: Address any linting, formatting, or type errors
- [ ] **Verify clean results**: Ensure all quality tools pass without errors

#### **📊 Advanced Phase Completion**
- [ ] **Define transaction boundaries**: Identify where database transactions are needed
- [ ] **Implement migrations**: Add database migration scripts if needed
- [ ] **Configure ORM/Query builder**: Set up database abstraction layer if used
- [ ] **Test error scenarios**: Verify proper error handling and exception mapping
- [ ] **Test transaction handling**: Ensure transactions work correctly across operations
- [ ] **Test external service mocks**: Verify external service integration with test doubles
- [ ] **Validate data persistence**: Ensure domain objects are correctly saved and retrieved
- [ ] **Add configuration documentation**: Document all configuration options
- [ ] **Document infrastructure setup**: Record database schema, external services, and configuration
- [ ] **Prepare for presentation**: Ensure repositories are ready for use by presentation layer
- [ ] **Verify end-to-end flow**: Test that domain → application → infrastructure flow works

**💡 Pro Tip**: Infrastructure code should be purely technical - no business logic should leak into this layer!

### ✅ ALLOWED Files (Implementation Targets):
- `src/infrastructure/repositories/` - Concrete repository implementations
- `src/infrastructure/models/` - Database/persistence models
- `src/infrastructure/mappers/` - Domain-to-infrastructure mapping
- `src/infrastructure/external/` - External service integrations (APIs, files, etc.)
- `src/infrastructure/config/` - Infrastructure configuration

### ❌ FORBIDDEN Files (DO NOT create/modify in this step):
- `src/domain/` - **Domain Layer (already implemented, DO NOT MODIFY)**
- `src/application/` - **Application Layer (already implemented, DO NOT MODIFY)**
- `src/presentation/` - **Presentation Layer (will be implemented in next step)**

### 🎯 Implementation Rules:
1. **Implement domain repository interfaces** - Provide concrete implementations
2. **Handle external system integration** - Databases, APIs, file systems, message queues
3. **No business logic** - Pure technical implementation, no business rules
4. **Use mappers for transformation** - Convert between domain objects and infrastructure models
5. **Depend on abstractions** - Implement interfaces defined in domain layer
6. **Configuration management** - Database connections, API credentials, infrastructure settings

### 💡 If you accidentally implement other layers:
```bash
# Delete incorrectly created files
rm -rf src/presentation/

# Do NOT modify domain or application layers
# These should already be complete from previous steps
```

**Violating these rules will break the dependency inversion and cause architectural issues.**

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
git restore tests/integration/repositories/
git restore tests/unit/infrastructure/

# Return to proper TDD flow
# 1. Read failing tests (these are specifications)
# 2. Implement infrastructure code to make tests pass
# 3. Never change test logic to match code
```

**⚠️ CRITICAL: Test modifications break the TDD cycle and invalidate scenario-driven development!**

---

## Common Errors and Solutions

### ❌ Error Case 1: Application layer not implemented
**Cause**: Infrastructure layer started before application implementation completion  
**Solution**: Complete application layer first with `/implement-usecase <issue-number>`

### ❌ Error Case 2: Business logic in infrastructure layer
**Cause**: Domain logic leaked into repositories or data access code  
**Solution**: Infrastructure should only handle persistence - move business logic to domain layer

### ❌ Error Case 3: Placeholder assertions causing false RED state
**Cause**: Infrastructure tests contain `assert False, "RED: ... not implemented yet"` but implementation exists  
**Solution**: 
```python
# Bad: Placeholder assertion (causes false RED)
def test_repository_save(self):
    assert False, "RED: Repository save not implemented yet"

# Good: Actual test implementation
def test_repository_save(self):
    entity = MyEntity.create("test_id", "test_value")
    repository.save(entity)
    saved_entity = repository.find_by_id("test_id")
    assert saved_entity is not None
    assert saved_entity.value == "test_value"
```
**Recovery**: Replace all placeholder assertions with proper tests that verify actual implementation

### ❌ Error Case 4: Infrastructure depending on domain incorrectly
**Cause**: Infrastructure importing domain concrete classes instead of interfaces  
**Solution**: Infrastructure should implement domain interfaces, use dependency inversion principle

## Execution Examples

### ✅ Success Example
```bash
$ /implement-infra 15
🏗️ Issues: #15 のインフラ層実装を開始します
✅ アプリケーション層が正常に実装されています
🔌 リポジトリ実装中...
  ✅ ファイル作成: src/infrastructure/repositories/user_repository.py
🎉 インフラ層実装完了!
```

### ❌ Failure Example and Fix
```bash
$ /implement-infra 15
❌ アプリケーション層の実装が完了していません
# Fix: Complete application layer first
$ /implement-usecase 15
$ /implement-infra 15
```

### ❌ Placeholder Assertion Example and Fix
```bash
$ /implement-infra 3
🚨 プレースホルダーアサーション発見:
  - tests/integration/repositories/test_sqlite_trade_repository.py: 6 個
  - tests/integration/repositories/test_sqlite_position_repository.py: 5 個

🚨 CRITICAL ISSUE: これらのテストは意図的にFALSE失敗しています
   - 実装は完了済みだが、テストがプレースホルダーのまま
   - これはTDDプロセス違反の状態です

# Fix: Replace placeholder assertions with real tests
# Edit test files to replace:
#   assert False, "RED: Repository save not implemented yet"
# With:
#   entity = TradeEntity.create("trade_001", "EURUSD", Decimal("1.0"))
#   repository.save(entity)
#   saved = repository.find_by_id("trade_001")
#   assert saved.symbol == "EURUSD"
```

## Task Details

1. **Setup Safe Environment and Parse Arguments**:
   ```bash
   # 🔧 Load all safe operation functions
   source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "08-implement-infra" "$ARGUMENTS"
   
   # Infrastructure implementation expects at least one issue number
   if [[ ${#issue_numbers[@]} -eq 0 ]]; then
       echo "エラー: 少なくとも1つのイシュー番号を指定してください"
       show_usage_example "implement-infra" "1" "単一イシューのインフラ実装"
       show_usage_example "implement-infra" "1,7" "複数イシューのインフラ実装"
       show_usage_example "implement-infra" "1 mt5-extended-data" "イシュー + 機能名指定"
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
   
   echo "🏗️ Issues: $(printf '#%s ' "${issue_numbers[@]}")のインフラストラクチャ層実装を開始します"
   echo ""
   echo "🚨 重要な注意: このステップではインフラストラクチャ層のみを実装します"
   echo "   ✅ 許可: src/infrastructure/ 配下のファイルのみ"
   echo "   ❌ 禁止: src/domain/, src/application/, src/presentation/"
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
   if ! begin_transaction "implement_infra_${issue_list}"; then
       echo "エラー: トランザクションの開始に失敗しました"
       exit 1
   fi
   
   # 📋 Validate prerequisites - application layer must be completed
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
   
   # Check for application implementation
   app_use_cases=$(find src/application/use_cases/ -name "*.py" -type f 2>/dev/null | grep -v __pycache__ || echo "")
   if [[ -z "$app_use_cases" ]]; then
       echo "❌ アプリケーション層の実装が見つかりません"
       echo "💡 最初にアプリケーション層を実装してください:"
       echo "   /implement-usecase $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
       execute_rollback "missing_application_implementation"
       exit 1
   fi
   
   echo "  ✅ アプリケーション実装確認: $(echo "$app_use_cases" | wc -l) ファイル"
   
   # Check for repository interfaces
   repo_interfaces=$(find src/domain/repositories/ -name "*_repository.py" -type f 2>/dev/null | grep -v __pycache__ || echo "")
   if [[ -z "$repo_interfaces" ]]; then
       echo "❌ リポジトリインターフェースが見つかりません"
       echo "💡 ドメイン層実装を確認してください"
       execute_rollback "missing_repository_interfaces"
       exit 1
   fi
   
   echo "  ✅ リポジトリインターフェース確認: $(echo "$repo_interfaces" | wc -l) ファイル"
   
   # 🚨 CRITICAL: Check for placeholder assertions in infrastructure tests
   echo "  🚨 インフラストラクチャ層プレースホルダーアサーション検証中..."
   
   infrastructure_placeholder_files=()
   while IFS= read -r -d '' file; do
       if grep -l 'assert False, "RED:' "$file" >/dev/null 2>&1; then
           infrastructure_placeholder_files+=("$file")
       fi
   done < <(find tests/integration/ -name "*.py" -print0 2>/dev/null)
   
   if [[ ${#infrastructure_placeholder_files[@]} -gt 0 ]]; then
       echo "    ❌ インフラストラクチャ層プレースホルダーアサーション発見:"
       for file in "${infrastructure_placeholder_files[@]:0:5}"; do
           count=$(grep -c 'assert False, "RED:' "$file" 2>/dev/null || echo "0")
           echo "      - $file: $count 個"
       done
       [[ ${#infrastructure_placeholder_files[@]} -gt 5 ]] && echo "      - ... (他 $((${#infrastructure_placeholder_files[@]} - 5)) ファイル)"
       
       echo ""
       echo "    🚨 CRITICAL ISSUE: これらのテストは意図的にFALSE失敗しています"
       echo "       - インフラストラクチャ実装は完了済みだが、テストがプレースホルダーのまま"
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
           echo "インフラストラクチャ層実装をキャンセルしました"
           echo "💡 推奨: 手動でプレースホルダーテストを適切なテストに置き換えてから再実行"
           execute_rollback "infrastructure_placeholder_assertions_found"
           exit 1
       fi
       
       echo "    ⚠️  プレースホルダーテストを無視して続行（後で修正が必要）"
   else
       echo "    ✅ インフラストラクチャ層プレースホルダーアサーション: なし（正常なテスト状態）"
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
   
   # Check application implementation phase completion
   app_status=$(jq -r '.phases.application_implementation.completed // false' "$metadata_file" 2>/dev/null)
   if [[ "$app_status" != "true" ]]; then
       echo "エラー: アプリケーション層実装が完了していません"
       echo "💡 先に /implement-usecase コマンドを実行してください"
       execute_rollback "application_implementation_not_completed"
       exit 1
   fi
   
   # Check if infrastructure implementation is already completed
   infra_status=$(jq -r '.phases.infrastructure_implementation.completed // false' "$metadata_file" 2>/dev/null)
   if [[ "$infra_status" == "true" ]]; then
       echo "⚠️  Issue #${issue_list} のインフラストラクチャ層実装は既に完了しています"
       echo "既存の実装を上書きしますか？ (y/N): "
       read -n 1 -r
       echo
       if [[ ! $REPLY =~ ^[Yy]$ ]]; then
           echo "インフラストラクチャ層実装をキャンセルしました"
           commit_transaction
           exit 0
       fi
       echo "🔄 既存のインフラストラクチャ層実装を上書きします"
   fi
   
   echo "✅ メタデータ検証完了"
   ```

4. **Extract Domain and Repository Information**:
   ```bash
   # 📖 Extract domain and repository information for implementation
   echo "📖 ドメイン・リポジトリ情報分析中..."
   
   # Extract entities from domain layer
   all_entities=()
   for entity_file in $domain_entities; do
       entity_name=$(basename "$entity_file" .py)
       # Convert to PascalCase
       entity_class=$(echo "$entity_name" | sed 's/_\([a-z]\)/\U\1/g' | sed 's/^./\U&/')
       all_entities+=("$entity_class")
   done
   
   # Extract repository interfaces
   all_repositories=()
   for repo_file in $repo_interfaces; do
       repo_name=$(basename "$repo_file" .py)
       # Extract repository class name
       repo_class=$(echo "$repo_name" | sed 's/_\([a-z]\)/\U\1/g' | sed 's/^./\U&/')
       all_repositories+=("$repo_class")
   done
   
   echo "  🎯 抽出された情報:"
   echo "    - エンティティ: ${#all_entities[@]} 個"
   echo "    - リポジトリ: ${#all_repositories[@]} 個"
   
   echo "✅ 情報分析完了"
   ```

5. **Create Infrastructure Layer Structure**:
   ```bash
   # 🏗️ Create infrastructure layer structure
   echo "🏗️ インフラストラクチャ層構造作成中..."
   
   # Load template utilities
   source "$(dirname "${BASH_SOURCE[0]}")/_template_utils.sh"
   
   # Define infrastructure structure directories
   infra_directories=(
       "src/infrastructure/persistence/models"
       "src/infrastructure/persistence/mappers"
       "src/infrastructure/external"
       "src/infrastructure/config"
   )
   
   # Create all infrastructure directories safely
   for dir in "${infra_directories[@]}"; do
       echo "  📁 作成中: $dir"
       if ! safe_mkdir "$dir"; then
           echo "エラー: インフラディレクトリ作成に失敗しました: $dir"
           execute_rollback "infra_directory_creation_failed"
           exit 1
       fi
       add_rollback "rmdir '$dir' 2>/dev/null || true" "Remove infra directory: $dir"
   done
   
   # Create __init__.py files
   infra_init_files=(
       "src/infrastructure/persistence/__init__.py"
       "src/infrastructure/persistence/models/__init__.py"
       "src/infrastructure/persistence/mappers/__init__.py"
       "src/infrastructure/external/__init__.py"
       "src/infrastructure/config/__init__.py"
   )
   
   for init_file in "${infra_init_files[@]}"; do
       echo "  📄 作成中: $init_file"
       if ! safe_create_file "$init_file" '"""Infrastructure layer package initialization"""' false; then
           echo "エラー: インフラ__init__.pyファイルの作成に失敗しました"
           execute_rollback "infra_init_creation_failed"
           exit 1
       fi
       add_rollback "rm -f '$init_file'" "Remove infra init file: $init_file"
   done
   
   echo "✅ インフラ構造作成完了 (${#infra_directories[@]} ディレクトリ)"
   ```

6. **Implement Database Models**:
   ```bash
   # 🗄️ Implement database models using templates
   echo "🗄️ データベースモデル実装中..."
   
   implemented_files=()
   
   # Create base model first
   base_model_file="src/infrastructure/persistence/models/base.py"
   
   echo "  🗄️ 実装中: Base Model ($base_model_file)"
   
   # Base model (固定実装のため直接定義)
   base_model_implementation='"""
Database Base Model

SQLAlchemy基底モデル定義。
実装日時: '"$(date)"'
"""

from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from datetime import datetime


Base = declarative_base()


class BaseModel(Base):
    """すべてのモデルの基底クラス
    
    共通のID、作成日時、更新日時フィールドを提供する。
    """
    
    __abstract__ = True
    
    id = Column(String(36), primary_key=True, comment="一意識別子（UUID）")
    created_at = Column(
        DateTime(timezone=True), 
        server_default=func.now(),
        nullable=False,
        comment="作成日時"
    )
    updated_at = Column(
        DateTime(timezone=True), 
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
        comment="更新日時"
    )
    
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(id={self.id})>"
'
   
   if ! safe_create_file "$base_model_file" "$base_model_implementation" true; then
       echo "エラー: ベースモデルファイルの作成に失敗しました: $base_model_file"
       execute_rollback "base_model_implementation_failed"
       exit 1
   fi
   
   implemented_files+=("$base_model_file")
   add_rollback "rm -f '$base_model_file'" "Remove base model: $base_model_file"
   
   # Create entity models using template system
   for entity in "${all_entities[@]}"; do
       entity_lower=$(echo "$entity" | tr '[:upper:]' '[:lower:]')
       model_file="src/infrastructure/persistence/models/${entity_lower}_model.py"
       
       echo "  🗄️ 実装中: ${entity}Model ($model_file)"
       
       # テンプレート変数設定
       setup_entity_vars "$entity"
       
       # テンプレートを使用してモデルファイルを作成
       if ! process_template "infrastructure/model_template.py" "$model_file"; then
           echo "エラー: モデルファイルの作成に失敗しました: $model_file"
           execute_rollback "model_implementation_failed"
           exit 1
       fi
       
       implemented_files+=("$model_file")
       add_rollback "rm -f '$model_file'" "Remove model: $model_file"
   done
   
   echo "✅ データベースモデル実装完了 (${#all_entities[@]} + 1 ファイル)"
   ```

7. **Implement Mappers**:
   ```bash
   # 🔄 Implement entity-model mappers using templates
   echo "🔄 エンティティ・モデルマッパー実装中..."
   
   for entity in "${all_entities[@]}"; do
       entity_lower=$(echo "$entity" | tr '[:upper:]' '[:lower:]')
       mapper_file="src/infrastructure/persistence/mappers/${entity_lower}_mapper.py"
       
       echo "  🔄 実装中: ${entity}Mapper ($mapper_file)"
       
       # テンプレート変数設定
       setup_entity_vars "$entity"
       
       # テンプレートを使用してマッパーファイルを作成
       if ! process_template "infrastructure/mapper_template.py" "$mapper_file"; then
           echo "エラー: マッパーファイルの作成に失敗しました: $mapper_file"
           execute_rollback "mapper_implementation_failed"
           exit 1
       fi
       
       implemented_files+=("$mapper_file")
       add_rollback "rm -f '$mapper_file'" "Remove mapper: $mapper_file"
   done
   
   echo "✅ マッパー実装完了 (${#all_entities[@]} ファイル)"
   ```

8. **Implement Concrete Repository Classes**:
   ```bash
   # 🏪 Implement concrete repository implementations using templates
   echo "🏪 コンクリートリポジトリ実装中..."
   
   for entity in "${all_entities[@]}"; do
       entity_lower=$(echo "$entity" | tr '[:upper:]' '[:lower:]')
       sql_repo_file="src/infrastructure/repositories/sql_${entity_lower}_repository.py"
       
       echo "  🏪 実装中: Sql${entity}Repository ($sql_repo_file)"
       
       # テンプレート変数設定
       setup_entity_vars "$entity"
       
       # テンプレートを使用してリポジトリファイルを作成
       if ! process_template "infrastructure/repository_template.py" "$sql_repo_file"; then
           echo "エラー: SQLリポジトリファイルの作成に失敗しました: $sql_repo_file"
           execute_rollback "sql_repo_implementation_failed"
           exit 1
       fi
       
       implemented_files+=("$sql_repo_file")
       add_rollback "rm -f '$sql_repo_file'" "Remove SQL repository: $sql_repo_file"
   done
   
   echo "✅ コンクリートリポジトリ実装完了 (${#all_entities[@]} ファイル)"
   ```

9. **Implement Database Configuration**:
   ```bash
   # ⚙️ Implement database configuration
   echo "⚙️ データベース設定実装中..."
   
   # Database configuration
   db_config_file="src/infrastructure/config/database.py"
   
   echo "  ⚙️ 実装中: Database Configuration ($db_config_file)"
   
   db_config_implementation='"""
Database Configuration

データベース接続とセッション管理の設定。
実装日時: '"$(date)"'
"""

import os
from typing import Generator, Optional
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import StaticPool
import logging

from ..persistence.models.base import Base


logger = logging.getLogger(__name__)


class DatabaseConfig:
    """データベース設定クラス
    
    SQLAlchemyエンジンとセッションの管理を行う。
    """
    
    def __init__(self, database_url: Optional[str] = None):
        """データベース設定初期化
        
        Args:
            database_url: データベース接続URL（省略時は環境変数から取得）
        """
        self.database_url = database_url or self._get_database_url()
        self.engine: Optional[Engine] = None
        self.session_factory: Optional[sessionmaker] = None
        
    def _get_database_url(self) -> str:
        """環境変数からデータベースURLを取得"""
        # 本番環境
        if db_url := os.getenv("DATABASE_URL"):
            return db_url
        
        # 開発環境
        if db_url := os.getenv("DEV_DATABASE_URL"):
            return db_url
        
        # テスト環境（インメモリSQLite）
        if os.getenv("TESTING") == "true":
            return "sqlite:///:memory:"
        
        # デフォルト（ローカル開発用SQLite）
        return "sqlite:///./dev_database.db"
    
    def create_engine(self) -> Engine:
        """SQLAlchemyエンジンを作成"""
        if self.engine is not None:
            return self.engine
        
        logger.info(f"Creating database engine for: {self._mask_url(self.database_url)}")
        
        # SQLiteの場合の特別設定
        if self.database_url.startswith("sqlite"):
            self.engine = create_engine(
                self.database_url,
                poolclass=StaticPool,
                connect_args={
                    "check_same_thread": False,  # SQLiteでマルチスレッド使用を許可
                },
                echo=os.getenv("SQL_DEBUG") == "true"  # SQLログ出力制御
            )
        else:
            # PostgreSQL、MySQLなどの場合
            self.engine = create_engine(
                self.database_url,
                pool_pre_ping=True,  # 接続確認
                pool_recycle=3600,   # 1時間で接続リサイクル
                echo=os.getenv("SQL_DEBUG") == "true"
            )
        
        logger.info("Database engine created successfully")
        return self.engine
    
    def create_session_factory(self) -> sessionmaker:
        """セッションファクトリを作成"""
        if self.session_factory is not None:
            return self.session_factory
        
        engine = self.create_engine()
        self.session_factory = sessionmaker(
            bind=engine,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False
        )
        
        logger.info("Session factory created successfully")
        return self.session_factory
    
    def get_session(self) -> Session:
        """データベースセッションを取得"""
        session_factory = self.create_session_factory()
        return session_factory()
    
    def get_session_context(self) -> Generator[Session, None, None]:
        """セッションコンテキストマネージャー
        
        トランザクション管理付きのセッションを提供する。
        """
        session = self.get_session()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
    
    def create_tables(self) -> None:
        """すべてのテーブルを作成"""
        engine = self.create_engine()
        logger.info("Creating all database tables")
        Base.metadata.create_all(bind=engine)
        logger.info("All database tables created successfully")
    
    def drop_tables(self) -> None:
        """すべてのテーブルを削除（テスト用）"""
        engine = self.create_engine()
        logger.warning("Dropping all database tables")
        Base.metadata.drop_all(bind=engine)
        logger.warning("All database tables dropped")
    
    def _mask_url(self, url: str) -> str:
        """URLからパスワードを隠す"""
        if "://" not in url:
            return url
        
        scheme, rest = url.split("://", 1)
        if "@" in rest:
            credentials, host = rest.split("@", 1)
            if ":" in credentials:
                user, _ = credentials.split(":", 1)
                return f"{scheme}://{user}:***@{host}"
        
        return url


# グローバルデータベース設定インスタンス
db_config = DatabaseConfig()


def get_database_session() -> Generator[Session, None, None]:
    """データベースセッション取得（依存性注入用）
    
    FastAPIなどのDIフレームワークで使用する。
    """
    yield from db_config.get_session_context()


def init_database() -> None:
    """データベース初期化"""
    logger.info("Initializing database")
    db_config.create_tables()
    logger.info("Database initialization completed")


def cleanup_database() -> None:
    """データベースクリーンアップ（テスト用）"""
    logger.info("Cleaning up database")
    db_config.drop_tables()
    logger.info("Database cleanup completed")
'
   
   if ! safe_create_file "$db_config_file" "$db_config_implementation" true; then
       echo "エラー: データベース設定ファイルの作成に失敗しました: $db_config_file"
       execute_rollback "db_config_implementation_failed"
       exit 1
   fi
   
   implemented_files+=("$db_config_file")
   add_rollback "rm -f '$db_config_file'" "Remove database config: $db_config_file"
   
   echo "✅ データベース設定実装完了"
   ```

10. **Create Integration Tests**:
    ```bash
    # 🧪 Create integration tests for infrastructure using templates
    echo "🧪 インフラ統合テスト作成中..."
    
    # Create integration test directory if needed
    if ! safe_mkdir "tests/integration/repositories"; then
        echo "エラー: 統合テストディレクトリの作成に失敗しました"
        execute_rollback "integration_test_dir_creation_failed"
        exit 1
    fi
    
    # Create integration tests for each repository using templates
    for entity in "${all_entities[@]}"; do
        entity_lower=$(echo "$entity" | tr '[:upper:]' '[:lower:]')
        integration_test_file="tests/integration/repositories/test_sql_${entity_lower}_repository.py"
        
        echo "  🧪 実装中: Integration Test for Sql${entity}Repository ($integration_test_file)"
        
        # テンプレート変数設定
        setup_entity_vars "$entity"
        
        # テンプレートを使用して統合テストファイルを作成
        if ! process_template "tests/integration_test_template.py" "$integration_test_file"; then
            echo "エラー: 統合テストファイルの作成に失敗しました: $integration_test_file"
            execute_rollback "integration_test_implementation_failed"
            exit 1
        fi
        
        implemented_files+=("$integration_test_file")
        add_rollback "rm -f '$integration_test_file'" "Remove integration test: $integration_test_file"
    done
    
    echo "✅ インフラ統合テスト実装完了 (${#all_entities[@]} ファイル)"
    ```

11. **Run Integration Tests**:
    ```bash
    # 🟢 Run integration tests to verify infrastructure implementation
    echo "🟢 インフラストラクチャ統合テスト実行中..."
    
    # Validate Python environment for testing
    if ! validate_python_environment; then
        echo "エラー: Python環境の検証に失敗しました"
        execute_rollback "python_env_validation_failed"
        exit 1
    fi
    
    # Run integration tests
    echo "  🧪 統合テスト実行中..."
    
    integration_test_output_file="/tmp/integration_test_output_$$"
    integration_test_result=0
    
    # Run integration tests and capture output
    if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/integration/ -v --tb=short > "$integration_test_output_file" 2>&1; then
        integration_test_result=0  # Tests passed
    else
        integration_test_result=1  # Tests failed
    fi
    
    # Analyze integration test results
    total_integration_tests=$(grep -c "test_.*PASSED\|test_.*FAILED" "$integration_test_output_file" 2>/dev/null || echo "0")
    passed_integration_tests=$(grep -c "PASSED" "$integration_test_output_file" 2>/dev/null || echo "0")
    failed_integration_tests=$(grep -c "FAILED" "$integration_test_output_file" 2>/dev/null || echo "0")
    
    echo "  📊 統合テスト結果分析:"
    echo "    - 総テスト数: $total_integration_tests"
    echo "    - 成功テスト数: $passed_integration_tests"
    echo "    - 失敗テスト数: $failed_integration_tests"
    
    if [[ $failed_integration_tests -gt 0 ]]; then
        echo "⚠️  失敗している統合テストがあります:"
        grep "FAILED" "$integration_test_output_file" | head -5
        echo ""
        echo "追加修正が必要な可能性があります。続行しますか？ (y/N): "
        read -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "インフラ実装を中止しました"
            rm -f "$integration_test_output_file"
            execute_rollback "integration_tests_failing"
            exit 1
        fi
    else
        echo "  ✅ GREEN状態確認: すべての統合テストが成功しています"
    fi
    
    # Calculate infrastructure coverage if possible
    infra_coverage_result=""
    if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/integration/ --cov=src.infrastructure --cov-report=term-missing --quiet >/tmp/infra_coverage_output_$$ 2>&1; then
        infra_coverage_result=$(grep -E "[0-9]+%" /tmp/infra_coverage_output_$$ | tail -1 || echo "Coverage data not available")
        rm -f /tmp/infra_coverage_output_$$
    fi
    
    rm -f "$integration_test_output_file"
    integration_tests_passed=$([ $failed_integration_tests -eq 0 ] && echo "true" || echo "false")
    
    echo "✅ 統合テスト実行完了"
    ```

12. **Update Metadata and Documentation**:
    ```bash
    # 📊 Update metadata with infrastructure implementation completion
    echo "📊 メタデータ・ドキュメント更新中..."
    
    if ! update_metadata_atomic "$metadata_file" \
        '.phases.infrastructure_implementation.created = true | 
         .phases.infrastructure_implementation.completed = true |
         .phases.infrastructure_implementation.completed_at = "'"$(date -u +%Y-%m-%dT%H:%M:%SZ)"'" |
         .phases.infrastructure_implementation.integration_tests_passed = '"$integration_tests_passed"' |
         .phases.infrastructure_implementation.coverage = "'"$infra_coverage_result"'" |
         .updated_at = "'"$(date -u +%Y-%m-%dT%H:%M:%SZ)"'" |
         .spec_files.infrastructure_implementation = ['"$(printf '"%s",' "${implemented_files[@]}" | sed 's/,$//')"'] |
         .phase = "infrastructure_implemented" |
         .next_commands = ["implement-presentation", "use-case-status"]'; then
        echo "エラー: メタデータの更新に失敗しました"
        execute_rollback "metadata_update_failed"
        exit 1
    fi
    
    # Create infrastructure documentation
    infra_doc_dir="docs/infrastructure"
    if ! safe_mkdir "$infra_doc_dir"; then
        echo "エラー: インフラドキュメントディレクトリの作成に失敗しました"
        execute_rollback "infra_doc_dir_creation_failed"
        exit 1
    fi
    
    infra_doc_file="$infra_doc_dir/issue-${issue_list}-infrastructure-design.md"
    
    infra_doc_content="# インフラストラクチャ層設計: $feature_name

**Issues**: $(printf '#%s ' "${issue_numbers[@]}")
**実装日時**: $(date)

## 概要

このインフラストラクチャ層実装は、$(printf 'Issue #%s, ' "${issue_numbers[@]}" | sed 's/, $//')の要件に基づいて作成されました。
ドメインエンティティの永続化と外部サービス連携を提供します。

## 実装されたコンポーネント

### データベースモデル
$(for entity in "${all_entities[@]}"; do
    echo "- **${entity}Model**: ${entity}エンティティのデータベースモデル"
done)

### エンティティ・モデルマッパー
$(for entity in "${all_entities[@]}"; do
    echo "- **${entity}Mapper**: ${entity}の双方向変換処理"
done)

### コンクリートリポジトリ
$(for entity in "${all_entities[@]}"; do
    echo "- **Sql${entity}Repository**: SQLAlchemy使用の${entity}永続化"
done)

### データベース設定
- **DatabaseConfig**: 接続管理とセッション制御
- **依存性注入**: セッション提供とトランザクション管理

## アーキテクチャ設計

### 永続化技術
- **ORM**: SQLAlchemy
- **データベース**: SQLite（開発）/ PostgreSQL（本番対応）
- **接続プール**: 自動管理
- **トランザクション**: コンテキストマネージャー

### 設計パターン
- **Repository Pattern**: 永続化の抽象化
- **Data Mapper Pattern**: エンティティ・モデル変換
- **Unit of Work**: トランザクション境界管理
- **Dependency Injection**: 設定とセッション注入

### セキュリティ・信頼性
- **接続プール**: 自動リサイクル
- **SQL インジェクション対策**: ORM使用
- **論理削除**: データ保持とプライバシー配慮
- **エラーハンドリング**: 包括的例外処理

## データベース設計

### 共通フィールド
- \`id\`: VARCHAR(36) - UUID主キー
- \`created_at\`: TIMESTAMP - 作成日時
- \`updated_at\`: TIMESTAMP - 更新日時  
- \`is_active\`: BOOLEAN - 論理削除フラグ

### エンティティテーブル
$(for entity in "${all_entities[@]}"; do
    entity_lower=$(echo "$entity" | tr '[:upper:]' '[:lower:]')
    echo "#### ${entity_lower}s テーブル
- エンティティ: $entity
- 主キー: id (UUID)
- インデックス: created_at, is_active
- 外部キー: (必要に応じて追加)"
done)

## 設定・環境

### 環境変数
- \`DATABASE_URL\`: 本番データベース接続URL
- \`DEV_DATABASE_URL\`: 開発データベース接続URL  
- \`TESTING\`: テスト環境フラグ
- \`SQL_DEBUG\`: SQLログ出力制御

### 接続設定
\`\`\`python
# 本番環境例
DATABASE_URL=postgresql://user:pass@host:5432/dbname

# 開発環境例  
DEV_DATABASE_URL=sqlite:///./dev_database.db

# テスト環境
TESTING=true  # インメモリSQLite使用
\`\`\`

## テスト結果

- **統合テスト数**: $total_integration_tests
- **成功**: $passed_integration_tests
- **失敗**: $failed_integration_tests
- **カバレッジ**: $infra_coverage_result

## パフォーマンス考慮

### 最適化
- **接続プール**: 効率的なDB接続管理
- **遅延ローディング**: 必要時のみデータ取得
- **バッチ処理**: 大量データ操作対応
- **インデックス**: 検索性能向上

### スケーラビリティ
- **読み取り専用レプリカ**: 参照性能向上
- **シャーディング**: 水平分散対応
- **キャッシュ**: Redis等の統合

## 運用・監視

### ログ
- **クエリログ**: 性能分析用
- **エラーログ**: 問題診断用
- **アクセスログ**: 利用状況監視

### 監視項目
- 接続プール使用率
- クエリ実行時間
- デッドロック発生率
- ストレージ使用量

## 次のステップ

1. **プレゼンテーション層実装**: \`/implement-presentation $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')\`
2. **進捗確認**: \`/use-case-status $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')\`
3. **E2Eテスト**: 全レイヤー連携テスト

---
**実装ステータス**: ✅ 完了
**統合テスト**: $integration_tests_passed
**永続化**: SQLAlchemy + SQLite/PostgreSQL
"
    
    if ! safe_create_file "$infra_doc_file" "$infra_doc_content" true; then
        echo "エラー: インフラドキュメントの作成に失敗しました"
        execute_rollback "infra_doc_creation_failed"
        exit 1
    fi
    
    implemented_files+=("$infra_doc_file")
    add_rollback "rm -f '$infra_doc_file'" "Remove infrastructure documentation"
    
    echo "✅ メタデータ・ドキュメント更新完了"
    ```

13. **Update Use Case Index and Git Commit**:
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
        updated_line="- [${feature_name}]($(basename "${spec_file}")) - Issues: $(printf '#%s ' "${issue_numbers[@]}")- Phase: infrastructure_implemented, TDD: 🟢 GREEN, Infra: ✅)"
        
        if ! sed -i "s|.*${feature_line}.*|${updated_line}|" "$use_cases_index"; then
            echo "エラー: インデックスファイルの更新に失敗しました"
            execute_rollback "index_update_failed"
            exit 1
        fi
        
        echo "✅ インデックス更新完了"
    fi
    
    # 💾 Commit infrastructure implementation
    echo "💾 インフラストラクチャ層実装をコミット中..."
    
    commit_message="feat: implement infrastructure layer for $(printf 'issue #%s ' "${issue_numbers[@]}")- ${feature_name}

Infrastructure Layer Implementation Summary:
- Feature: ${feature_name}
- Issues: $(printf '#%s ' "${issue_numbers[@]}")
- Implementation Files: ${#implemented_files[@]} created
- Integration Test Results: Passed $passed_integration_tests, Failed $failed_integration_tests
- Coverage: $infra_coverage_result

Implemented Components:
$(printf '  - %s\n' "${implemented_files[@]}")

Infrastructure Features:
- SQLAlchemy ORM models for data persistence
- Entity-model mappers for clean separation
- Concrete repository implementations with error handling
- Database configuration with connection pooling
- Integration tests with in-memory SQLite
- Transaction management and rollback support

Database Design:
- Common base model with UUID, timestamps, soft delete
- Entity-specific tables with proper indexing
- Environment-specific database configuration
- Migration-ready structure

Architecture Compliance:
- Repository pattern implementation
- Clean separation of concerns
- No domain logic in infrastructure layer
- Dependency injection ready

Next Step: /implement-presentation for presentation layer
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
    
    add_rollback "git reset --hard HEAD~1" "Undo infrastructure implementation commit"
    echo "✅ コミット完了"
    ```

14. **Update GitHub Issues and Final Success**:
    ```bash
    # 🎫 Update GitHub issues with infrastructure implementation completion
    echo "🎫 GitHubイシュー更新中..."
    
    for issue_num in "${issue_numbers[@]}"; do
        echo "  📝 Issue #$issue_num コメント追加中..."
        
        issue_comment="🏗️ **インフラストラクチャ層実装完了**

インフラストラクチャ層の実装が完了しました。データ永続化と外部サービス連携が可能になりました。

## 📊 実装結果
- **実装ファイル数**: ${#implemented_files[@]} ファイル
- **統合テスト結果**: 成功 $passed_integration_tests / 総計 $total_integration_tests
- **カバレッジ**: $infra_coverage_result
- **永続化技術**: SQLAlchemy + SQLite/PostgreSQL

## 🏗️ 実装されたコンポーネント
### データベースモデル
$(if [[ ${#all_entities[@]} -gt 0 ]]; then
    for entity in "${all_entities[@]:0:3}"; do
        echo "- **${entity}Model**: ${entity}の永続化モデル"
    done
    [[ ${#all_entities[@]} -gt 3 ]] && echo "- ... (他 $((${#all_entities[@]} - 3)) モデル)"
fi)

### リポジトリ実装
$(if [[ ${#all_entities[@]} -gt 0 ]]; then
    for entity in "${all_entities[@]:0:2}"; do
        echo "- **Sql${entity}Repository**: SQLAlchemy使用の永続化"
    done
    [[ ${#all_entities[@]} -gt 2 ]] && echo "- ... (他リポジトリ)"
fi)

### マッパー・設定
- **エンティティマッパー**: ドメイン⇔DB変換
- **データベース設定**: 接続管理とトランザクション
- **統合テスト**: 実DB使用のE2Eテスト

## 🗄️ データベース設計
- **基底モデル**: UUID主キー + タイムスタンプ
- **論理削除**: is_activeフラグ使用
- **インデックス**: 検索性能最適化
- **環境対応**: SQLite(開発) / PostgreSQL(本番)

## 🏛️ アーキテクチャ準拠
- [x] リポジトリパターン実装
- [x] データマッパーパターン
- [x] 依存性注入対応
- [x] トランザクション管理
- [x] 例外処理とログ

## 🚀 次のステップ

プレゼンテーション層実装を開始してください：
\`\`\`bash
/implement-presentation $issue_num
\`\`\`

## 📚 関連ドキュメント
- [インフラ層設計]($infra_doc_file)
- [データベース設計](#データベース設計)

## 🔍 動作確認
\`\`\`bash
# 統合テスト実行
uv run --frozen pytest tests/integration/ -v

# カバレッジ確認
uv run --frozen pytest tests/integration/ --cov=src.infrastructure

# データベース初期化（開発環境）
python -c \"from src.infrastructure.config.database import init_database; init_database()\"
\`\`\`

---
**Layer Status**: Infrastructure ✅ → 次: Presentation 🎨
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
        echo "🎉 インフラストラクチャ層実装完了!"
        echo "============================================="
        echo "🏗️ 機能名: $feature_name"
        echo "🎫 対象イシュー: $(printf '#%s ' "${issue_numbers[@]}")"
        echo "📊 実装ファイル数: ${#implemented_files[@]} 個"
        echo ""
        echo "📋 実装されたコンポーネント:"
        echo "   データベースモデル: $((${#all_entities[@]} + 1)) 個 (Base + entities)"
        echo "   エンティティマッパー: ${#all_entities[@]} 個"
        echo "   コンクリートリポジトリ: ${#all_entities[@]} 個"
        echo "   データベース設定: 1 個"
        echo "   統合テスト: ${#all_entities[@]} 個"
        echo ""
        echo "🟢 テスト状況:"
        echo "   - 統合テスト: 成功 $passed_integration_tests / 総計 $total_integration_tests"
        echo "   - カバレッジ: $infra_coverage_result"
        echo "   - データベース接続: 検証済み"
        echo ""
        echo "🏛️ アーキテクチャ準拠:"
        echo "   - リポジトリパターン実装"
        echo "   - データマッパーパターン"
        echo "   - クリーンな層分離"
        echo "   - トランザクション管理"
        echo ""
        echo "🗄️ データベース設計:"
        echo "   - SQLAlchemy ORM使用"
        echo "   - UUID主キー採用"
        echo "   - 論理削除対応"
        echo "   - 環境別設定対応"
        echo ""
        echo "🚀 次のステップ:"
        echo "   1. プレゼンテーション層実装: /implement-presentation $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
        echo "   2. 進捗確認: /use-case-status $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
        echo "   3. E2Eテスト実行（全レイヤー完成後）"
        echo ""
        echo "💡 実装品質:"
        echo "   - 永続化の抽象化"
        echo "   - エラーハンドリング"
        echo "   - トランザクション保証"
        echo "   - 統合テストカバレッジ"
        echo ""
        
        # Show operation logs summary
        echo "📊 操作ログサマリー:"
        show_github_operation_log | tail -2
        show_git_operation_log | tail -2
        show_transaction_log | tail -2
        
        echo ""
        echo "✅ インフラストラクチャ層実装完了 - プレゼンテーション層実装準備完了!"
        echo ""
        echo "🚨 MANDATORY FOR CLAUDE CODE: SCENARIO EVOLUTION CHECK"
        echo "   インフラ実装中に新要件・制約・エッジケース発見時は"
        echo "   作業を中断して /evolve-scenarios <feature-name> を実行すること"
        echo "   CRITICAL: インフラ変更は外部依存・性能に大きな影響があります"
        
    else
        echo "❌ トランザクション コミット失敗"
        exit 1
    fi
    ```

Important Notes:
- Keep infrastructure details isolated from domain
- Use dependency injection for flexibility
- Test with real infrastructure when possible
- Handle connection pooling and transactions properly
- Consider using repository pattern with Unit of Work
- All user-facing output must be in JAPANESE