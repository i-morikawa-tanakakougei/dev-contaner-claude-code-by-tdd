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

**🤖 Agent Integration**: This command uses the specialized `08-implement-infra` agent for optimal infrastructure layer implementation.

1. **Pre-execution Validation**:
   ```bash
   # Validate issue number requirement
   if [[ $# -eq 0 ]]; then
       echo "エラー: 少なくとも1つのイシュー番号を指定してください"
       echo "使用例: /implement-infra 1"
       echo "使用例: /implement-infra 1,7 (複数イシュー)"
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
   
   # Check for application layer implementation
   missing_apps=()
   for issue_num in "${issue_numbers[@]}"; do
       # Look for application implementation files
       if ! find src/application/use_cases/ -name "*${issue_num}*.py" -o -name "*issue*${issue_num}*.py" -type f 2>/dev/null | head -1 >/dev/null; then
           missing_apps+=("$issue_num")
       fi
   done
   
   if [[ ${#missing_apps[@]} -gt 0 ]]; then
       echo "❌ エラー: 以下のIssueのアプリケーション層実装が見つかりません:"
       printf '  - Issue #%s\n' "${missing_apps[@]}"
       echo "💡 先に /implement-usecase を実行してください"
       exit 1
   fi
   
   echo "🏗️ Issues: $(printf '#%s ' "${issue_numbers[@]}")のインフラストラクチャ層実装を開始します"
   ```

2. **Context Preparation and Agent Execution**:
   ```bash
   # 🔄 Prepare context for agent (Pattern B: Hybrid approach)
   echo "🏗️ コンテキスト準備とエージェント起動..."
   
   # Create context file with infrastructure implementation information
   context_file="/workspace/.claude/context/current-command-context.json"
   current_time=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
   
   # Build context JSON for infrastructure implementation
   cat > "$context_file" <<EOF
   {
     "command": "implement-infra",
     "timestamp": "$current_time",
     "issue_numbers": [$(IFS=,; echo "${issue_numbers[*]}")],
     "phase": "infrastructure-layer",
     "context": {
       "expected_outputs": [
         "src/infrastructure/repositories/",
         "src/infrastructure/database/",
         "src/infrastructure/external_services/",
         "src/infrastructure/config/"
       ],
       "architecture_patterns": ["Clean Architecture", "Repository Pattern", "DDD"]
     },
     "additional_instructions": "インフラストラクチャ層を実装してください。ドメイン層のリポジトリインターフェースの具象実装を作成し、データベースアクセスと外部サービス連携を実装してください。Clean Architectureの依存関係ルールを遵守し、インフラの詳細をドメイン層から分離してください。",
     "special_considerations": [
       "ドメインリポジトリインターフェース（src/domain/repositories/）の完全実装",
       "データベース接続とトランザクション管理の設計",
       "外部API連携とエラーハンドリングの実装",
       "インフラテストと統合テストの作成"
     ],
     "custom_context": {
       "database_integration": true,
       "external_service_integration": true,
       "transaction_management": true,
       "infrastructure_testing": true
     }
   }
   EOF
   
   echo "✅ コンテキストファイル作成完了: $context_file"
   
   # 🤖 Call the specialized agent with hybrid context
   echo ""
   echo "🏗️ インフラストラクチャ実装エージェントを起動します..."
   echo "専門エージェントがリポジトリ実装と外部サービス連携を実装します"
   echo ""
   
   # Actual Claude Code Task tool invocation with hybrid approach
   cat <<'AGENT_CALL'
   Task tool will be called with:
   - subagent_type: "08-implement-infra"
   - description: "Implement infrastructure layer with repositories and external services"
   - prompt: |
     インフラストラクチャ層実装タスクを実行してください。
     
     ## コンテキスト情報の取得
     1. 一時コンテキスト（イシュー情報）:
        - /workspace/.claude/context/current-command-context.json を読み込み
     
     2. 既存実装情報の確認:
        - src/domain/repositories/ でリポジトリインターフェースを確認
        - src/application/ でアプリケーション層の依存関係を確認
        - docs/use_cases/issue-X-Y.json で現在のフェーズを確認
     
     ## 実行タスク
     1. リポジトリインターフェースの分析と具象実装の作成
     2. データベースモデルとエンティティマッピングの設計
     3. SQLAlchemyを使用したデータ永続化層の実装
     4. データベース接続とトランザクション管理の設定
     5. 外部サービス統合とAPI連携の実装
     6. 統合テストとインフラテストの作成・実行
     7. パフォーマンス最適化と接続プールの設定
     
     ## 処理完了後
     - 実装したインフラクラスのパス報告
     - 統合テスト実行結果の報告
     - 次のステップ（プレゼンテーション層実装）への案内
   AGENT_CALL
   
   echo "✅ エージェント呼び出し設定完了"
   echo "エージェントが以下の処理を実行します:"
   echo "  - コンテキストファイルからのイシュー情報取得"
   echo "  - リポジトリインターフェースの分析と具象実装の作成"
   echo "  - データベースモデルとエンティティマッピングの設計"
   echo "  - SQLAlchemyを使用したデータ永続化層の実装"
   echo "  - データベース接続とトランザクション管理の設定"
   echo "  - 外部サービス統合とAPI連携の実装"
   echo "  - 統合テストとインフラテストの作成・実行"
   echo "  - パフォーマンス最適化と接続プールの設定"
   ```

3. **Agent Result Verification**:
   ```bash
   # 🔍 Verify agent execution results
   echo "🔍 エージェント実行結果を検証中..."
   
   # Check that infrastructure files were created
   echo "  🔍 インフラストラクチャファイルの作成確認中..."
   
   created_files=()
   for issue_num in "${issue_numbers[@]}"; do
       # Look for repository implementation files
       repo_pattern="src/infrastructure/repositories/*${issue_num}*repository*.py"
       if ls $repo_pattern 2>/dev/null | head -1 >/dev/null; then
           repo_files=$(ls $repo_pattern 2>/dev/null)
           for file in $repo_files; do
               created_files+=("$file")
               echo "    ✅ Issue #$issue_num のリポジトリ実装を確認: $(basename "$file")"
           done
       else
           echo "    ❌ Issue #$issue_num のリポジトリ実装が見つかりません"
       fi
       
       # Check for database models
       model_pattern="src/infrastructure/models/*${issue_num}*.py"
       if ls $model_pattern 2>/dev/null | head -1 >/dev/null; then
           model_files=$(ls $model_pattern 2>/dev/null)
           for file in $model_files; do
               created_files+=("$file")
               echo "    ✅ Issue #$issue_num のデータベースモデルを確認: $(basename "$file")"
           done
       fi
       
       # Check metadata update
       metadata_pattern="docs/use_cases/*issue*${issue_num}*.json"
       if ls $metadata_pattern 2>/dev/null | head -1 >/dev/null; then
           metadata_file=$(ls $metadata_pattern 2>/dev/null | head -1)
           if command -v jq >/dev/null 2>&1; then
               infra_status=$(jq -r '.phases.infrastructure_implementation.completed // false' "$metadata_file" 2>/dev/null)
               if [[ "$infra_status" == "true" ]]; then
                   echo "    ✅ Issue #$issue_num のメタデータが更新されました"
               else
                   echo "    ⚠️ Issue #$issue_num のメタデータ更新が未確認"
               fi
           fi
       fi
   done
   
   # Check if src/infrastructure directory exists
   if [[ ! -d "src/infrastructure" ]]; then
       echo "❌ エラー: src/infrastructure ディレクトリが作成されていません"
       exit 1
   fi
   
   # Report validation results
   if [[ ${#created_files[@]} -eq 0 ]]; then
       echo "❌ エージェント実行検証失敗: インフラストラクチャファイルが作成されていません"
       exit 1
   fi
   
   echo "✅ エージェント実行結果検証完了"
   ```

4. **Display Infrastructure Implementation Success Summary**:
   ```bash
   # 📊 Display comprehensive infrastructure implementation summary
   echo ""
   echo "🎉 インフラストラクチャ層実装完了!"
   echo "============================================="
   
   # Show created infrastructure files
   echo "📁 作成されたインフラファイル:"
   for file in "${created_files[@]}"; do
       if [[ -f "$file" ]]; then
           echo "   ✅ $file"
       fi
   done
   
   # Show infrastructure components summary
   echo ""
   echo "🏗️ インフラコンポーネント:"
   if [[ ${#created_files[@]} -gt 0 ]]; then
       repo_count=$(printf '%s\n' "${created_files[@]}" | grep -c "repository" || echo "0")
       model_count=$(printf '%s\n' "${created_files[@]}" | grep -c "model" || echo "0")
       config_count=$(printf '%s\n' "${created_files[@]}" | grep -c "config" || echo "0")
       
       echo "   📊 リポジトリ実装: $repo_count 個"
       echo "   📊 データベースモデル: $model_count 個"
       echo "   📊 設定ファイル: $config_count 個"
   fi
   
   # Show next steps
   echo ""
   echo "📋 次のステップ (プレゼンテーション層実装):"
   for issue_num in "${issue_numbers[@]}"; do
       echo "   /implement-presentation $issue_num"
   done
   
   echo ""
   echo "📚 重要ドキュメント:"
   echo "   - インフラ実装: src/infrastructure/"
   echo "   - データベース設定: 環境変数で制御"
   if [[ ${#created_files[@]} -gt 0 ]]; then
       echo "   - 実装されたファイル: ${created_files[0]} 他"
   fi
   
   echo ""
   echo "🔗 関連リソース:"
   for issue_num in "${issue_numbers[@]}"; do
       echo "   - Issue #$issue_num: gh issue view $issue_num"
   done
   
   echo ""
   echo "✅ インフラストラクチャ層実装完了 - プレゼンテーション層実装準備完了!"
   ```


Important Notes:
- Keep infrastructure details isolated from domain
- Use dependency injection for flexibility
- Test with real infrastructure when possible
- Handle connection pooling and transactions properly
- Consider using repository pattern with Unit of Work
- All user-facing output must be in JAPANESE