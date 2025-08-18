Implement presentation layer (API endpoints, CLI, or UI).

## Metadata
- **Prerequisites**: Infrastructure layer implementation completed (08-implement-infra)
- **Input**: Issue number(s) (required)
- **Output**: 
  - Presentation layer implementation in `src/presentation/`
  - Controllers, API endpoints, CLI commands
  - Updated `docs/use_cases/issue-X-Y.json` metadata
- **Dependencies**: All lower layers (domain, application, infrastructure)
- **Execution Timing**: After infrastructure layer, before testing phase

## 🎯 **TDD/DDD/LAYERED PROCESS CONTEXT**

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Sprint Execution Phase - Presentation Layer Implementation (09/16)  
> 🎯 **Phase Purpose**: Implement API endpoints, CLI commands, or UI components  
> ⬅️ **Previous Stage**: 08-implement-infra (Infrastructure Layer Implementation)  
> ➡️ **Next Stage**: 10-refactor (Code Refactoring)
>
> **📋 3-Layer Architecture Operations**:  
> - 🎯 **Strategic**: `docs/use_cases/core/index.md` (Reference user interactions)  
> - 📊 **Tactical**: `docs/use_cases/index.md` (Update presentation layer status)  
> - 🔧 **Execution**: `docs/use_cases/issue-X-Y.json` (Track presentation implementation)

## 🖼️ **PRESENTATION LAYER IMPLEMENTATION ONLY**

**⚠️ Important Notice:**
- **This step is PRESENTATION LAYER ONLY** - Implement API endpoints, CLI, or UI components
- **NO OTHER LAYERS** - Focus only on presentation layer components  
- **User interfaces** - Handle API endpoints, CLI commands, or web interfaces
- **Input validation** - Handle user input validation and response formatting

**Layer Implementation Sequence:**
1. `06-implement-domain` ← Domain layer (completed)
2. `07-implement-usecase` ← Application layer (completed)
3. `08-implement-infra` ← Infrastructure layer (completed)  
4. `09-implement-presentation` ← **【YOU ARE HERE】Presentation layer**

## 🚨 **CRITICAL: PRESENTATION LAYER ONLY - NO OTHER LAYERS**

**❌ ABSOLUTELY FORBIDDEN in this step:**
- **Domain Layer Modifications**: Domain layer is complete - DO NOT modify it
- **Application Layer Modifications**: Application layer is complete - DO NOT modify it  
- **Infrastructure Layer Modifications**: Infrastructure layer is complete - DO NOT modify it
- **Business Logic**: No business rules or domain logic in presentation code

**✅ ONLY ALLOWED in this step:**
- **API Controllers**: REST/GraphQL endpoints and HTTP request handling
- **CLI Commands**: Command-line interface implementations
- **Web UI Components**: Frontend interfaces and user interactions
- **Input Validation**: Request validation, serialization, and response formatting

## 📋 **PRESENTATION LAYER TASK CHECKLIST**

**Use this checklist to implement presentation layer with proper integration:**

### 🔴 Required Tasks

#### **🎯 Use Case to Endpoint Mapping**
- [ ] **Map Given-When-Then to endpoints**: Convert scenarios to API endpoints or CLI commands
- [ ] **🚨 CRITICAL: Replace placeholder assertions**: Check for and fix `assert False, "RED: ... not implemented yet"` statements in presentation tests
- [ ] **Verify test authenticity**: Ensure tests actually test implementation, not just placeholder failures
- [ ] **Define request/response models**: Create input/output models for each endpoint
- [ ] **Plan authentication requirements**: Identify which endpoints need authentication
- [ ] **Design error response format**: Define consistent error response structure

#### **🌐 API Controller Implementation**
- [ ] **Create API controllers**: Implement REST controllers for each use case
- [ ] **Add endpoint routing**: Configure URL routing and HTTP methods
- [ ] **Implement request handling**: Parse and validate incoming requests
- [ ] **Call application services**: Integrate with use cases from application layer
- [ ] **Format responses**: Convert application DTOs to API response format

#### **🧪 End-to-End Testing**
- [ ] **Run e2e tests**: Execute full end-to-end tests through presentation layer
- [ ] **Test all endpoints**: Verify each API endpoint works correctly
- [ ] **Update metadata**: Mark presentation layer implementation complete in issue-X-Y.json
- [ ] **Commit presentation layer**: Version control presentation layer code

### 🟡 Recommended Tasks

#### **✅ Input Validation & Serialization**
- [ ] **Add request validation**: Validate all incoming requests
- [ ] **Implement field validation**: Check required fields, formats, and constraints
- [ ] **Add sanitization**: Sanitize user input to prevent injection attacks
- [ ] **Handle validation errors**: Return clear validation error messages
- [ ] **Implement request serialization**: Convert requests to application DTOs
- [ ] **Add response serialization**: Convert application DTOs to response format

#### **🔒 Authentication & Authorization**
- [ ] **Implement authentication**: Add login/logout functionality
- [ ] **Add authorization checks**: Implement role-based access control
- [ ] **Handle authentication errors**: Provide clear auth failure messages
- [ ] **Add session management**: Implement session handling if needed
- [ ] **Secure sensitive endpoints**: Ensure proper protection for critical operations

#### **🚫 Architecture Compliance Check**
- [ ] **No business logic**: Verify presentation code contains no business rules
- [ ] **Domain layer unchanged**: Verify domain layer files were not modified
- [ ] **Application layer unchanged**: Verify application layer files were not modified
- [ ] **Infrastructure layer unchanged**: Verify infrastructure layer files were not modified
- [ ] **Presentation directory only**: Confirm only src/presentation/ directory has new files
- [ ] **Proper dependency usage**: Verify only application services are called, not domain directly

### 🟢 Optional Tasks

#### **⚡ CLI Command Implementation**
- [ ] **Create CLI commands**: Implement command-line interface for each use case
- [ ] **Add argument parsing**: Parse command-line arguments and options
- [ ] **Implement command logic**: Connect CLI commands to application services
- [ ] **Add help documentation**: Provide usage help and examples
- [ ] **Handle CLI errors**: Implement user-friendly error messages
- [ ] **Add progress indicators**: Show progress for long-running operations

#### **📱 User Experience & Documentation**
- [ ] **Add API documentation**: Create OpenAPI/Swagger documentation
- [ ] **Write usage examples**: Provide clear usage examples for each endpoint
- [ ] **Add CLI help**: Implement comprehensive help system
- [ ] **Create user guides**: Write user-facing documentation
- [ ] **Add logging**: Implement request/response logging for debugging
- [ ] **Optimize performance**: Ensure responsive user experience

#### **🔧 Production Readiness**
- [ ] **Add health checks**: Implement health check endpoints
- [ ] **Add metrics**: Implement monitoring and metrics collection
- [ ] **Configure CORS**: Set up proper cross-origin resource sharing
- [ ] **Add rate limiting**: Implement API rate limiting if needed
- [ ] **Security headers**: Add appropriate security headers
- [ ] **Environment configuration**: Support different environments (dev/staging/prod)

#### **🔧 Code Quality Validation**
- [ ] **Run ruff linting**: Execute `uv run --frozen ruff check src/ --fix`
- [ ] **Run ruff formatting**: Execute `uv run --frozen ruff format src/`
- [ ] **Run type checking**: Execute `uv run --frozen pyright src/`
- [ ] **Fix quality issues**: Address any linting, formatting, or type errors
- [ ] **Verify clean results**: Ensure all quality tools pass without errors

#### **📊 Advanced Phase Completion**
- [ ] **Plan endpoint organization**: Group related endpoints logically
- [ ] **Add error handling**: Implement proper HTTP error responses
- [ ] **Test error scenarios**: Verify proper error handling and responses
- [ ] **Test authentication flows**: Ensure auth/authz works correctly
- [ ] **Test input validation**: Verify validation catches invalid inputs
- [ ] **Test integration**: Confirm all layers work together properly
- [ ] **Add authentication middleware**: Implement reusable auth components
- [ ] **Document API**: Record all endpoints, commands, and usage patterns
- [ ] **Test full system**: Verify complete end-to-end functionality
- [ ] **Prepare for testing**: Ensure system is ready for comprehensive testing phase

**💡 Pro Tip**: Presentation layer should be thin - delegate all business logic to application services!

### ✅ ALLOWED Files (Implementation Targets):
- `src/presentation/api/` - REST API endpoints, controllers
- `src/presentation/cli/` - Command-line interface commands
- `src/presentation/web/` - Web UI components, views, templates
- `src/presentation/serializers/` - Input/output serialization
- `src/presentation/validators/` - Request validation
- `src/presentation/middleware/` - HTTP middleware, request processing

### ❌ FORBIDDEN Files (DO NOT create/modify in this step):
- `src/domain/` - **Domain Layer (already implemented, DO NOT MODIFY)**
- `src/application/` - **Application Layer (already implemented, DO NOT MODIFY)**
- `src/infrastructure/` - **Infrastructure Layer (already implemented, DO NOT MODIFY)**

### 🎯 Implementation Rules:
1. **Handle user interfaces ONLY** - API endpoints, CLI commands, web pages
2. **No business logic** - Delegate all business operations to application layer
3. **Input validation and serialization** - Validate input, serialize output
4. **Dependency injection** - Inject application use cases, don't create them
5. **HTTP/CLI concerns only** - Request handling, response formatting, error handling
6. **Thin controllers** - Keep presentation logic minimal

### 💡 If you accidentally implement other layers:
```bash
# Do NOT modify any other layers
# All other layers should already be complete from previous steps

# If you accidentally created files in wrong locations:
# Review the file paths carefully and move them to src/presentation/
```

**Violating these rules will break the clean architecture and create tight coupling.**

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
git restore tests/e2e/api/
git restore tests/unit/presentation/

# Return to proper TDD flow
# 1. Read failing tests (these are specifications)
# 2. Implement presentation code to make tests pass
# 3. Never change test logic to match code
```

**⚠️ CRITICAL: Test modifications break the TDD cycle and invalidate scenario-driven development!**

---

## Common Errors and Solutions

### ❌ Error Case 1: Infrastructure layer not implemented
**Cause**: Presentation layer started before infrastructure completion  
**Solution**: Complete infrastructure layer first with `/implement-infra <issue-number>`

### ❌ Error Case 2: Business logic in controllers
**Cause**: Business logic implemented in API controllers or UI handlers  
**Solution**: Controllers should only handle HTTP/UI concerns - delegate to application layer

### ❌ Error Case 3: Placeholder assertions causing false RED state
**Cause**: Presentation tests contain `assert False, "RED: ... not implemented yet"` but implementation exists  
**Solution**: 
```python
# Bad: Placeholder assertion (causes false RED)
def test_api_endpoint(self):
    assert False, "RED: API endpoint not implemented yet"

# Good: Actual test implementation
def test_api_endpoint(self):
    response = client.post("/api/entities", json={"name": "test"})
    assert response.status_code == 201
    assert response.json()["id"] is not None
    assert response.json()["name"] == "test"
```
**Recovery**: Replace all placeholder assertions with proper tests that verify actual implementation

### ❌ Error Case 4: Direct domain access from presentation
**Cause**: Presentation layer bypassing application layer  
**Solution**: Always use application layer use cases from presentation layer

## Execution Examples

### ✅ Success Example
```bash
$ /implement-presentation 15
🖥️ Issues: #15 のプレゼンテーション層実装を開始します
✅ インフラ層が正常に実装されています
🌐 APIエンドポイント実装中...
  ✅ ファイル作成: src/presentation/api/user_controller.py
🎉 プレゼンテーション層実装完了!
```

### ❌ Failure Example and Fix
```bash
$ /implement-presentation 15
❌ インフラ層の実装が完了していません
# Fix: Complete infrastructure layer first
$ /implement-infra 15
$ /implement-presentation 15
```

### ❌ Placeholder Assertion Example and Fix
```bash
$ /implement-presentation 3
🚨 プレースホルダーアサーション発見:
  - tests/e2e/api/test_data_persistence_api.py: 8 個
  - tests/e2e/api/test_connections_api.py: 6 個

🚨 CRITICAL ISSUE: これらのテストは意図的にFALSE失敗しています
   - 実装は完了済みだが、テストがプレースホルダーのまま
   - これはTDDプロセス違反の状態です

# Fix: Replace placeholder assertions with real tests
# Edit test files to replace:
#   assert False, "RED: API endpoint not implemented yet"
# With:
#   response = client.post("/api/trades", json={"symbol": "EURUSD", "quantity": "1.0"})
#   assert response.status_code == 201
#   assert response.json()["trade_id"] is not None
```

## Task Details

1. **Setup Safe Environment and Parse Arguments**:
   ```bash
   # 🔧 Load all safe operation functions and template utilities
   source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "09-implement-presentation" "$ARGUMENTS"
   source "$(dirname "${BASH_SOURCE[0]}")/templates/_template_utils.sh"
   
   # Presentation implementation expects at least one issue number
   if [[ ${#issue_numbers[@]} -eq 0 ]]; then
       echo "エラー: 少なくとも1つのイシュー番号を指定してください"
       show_usage_example "implement-presentation" "1" "単一イシューのプレゼンテーション実装"
       show_usage_example "implement-presentation" "1,7" "複数イシューのプレゼンテーション実装"
       show_usage_example "implement-presentation" "1 api" "イシュー + API指定"
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
   
   echo "🎨 Issues: $(printf '#%s ' "${issue_numbers[@]}")のプレゼンテーション層実装を開始します"
   echo ""
   echo "🚨 重要な注意: このステップではプレゼンテーション層のみを実装します"
   echo "   ✅ 許可: src/presentation/ 配下のファイルのみ"
   echo "   ❌ 禁止: src/domain/, src/application/, src/infrastructure/"
   echo "   💡 他の層を間違って実装した場合は即座に削除してください"
   echo ""
   echo "🔴→🟢 TDD原則: テストを実装に合わせて変更してはいけません!"
   echo "   📖 シナリオ → 🔴 テスト → 🟢 実装 の順序を厳守"
   echo "   ✅ 実装をテストに合わせる（正しい）"
   echo "   ❌ テストを実装に合わせる（禁止）"
   echo ""
   ```

2. **Begin Transaction and Prerequisites Validation**:
   ```bash
   # 🔄 Start comprehensive transaction
   if ! begin_transaction "implement_presentation_${issue_list}"; then
       echo "エラー: トランザクションの開始に失敗しました"
       exit 1
   fi
   
   # 📋 Validate prerequisites - all other layers must be completed
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
   
   # Validate all required layers are implemented
   validate_layer_implementations() {
       local domain_entities=$(find src/domain/entities/ -name "*.py" -type f 2>/dev/null | grep -v __pycache__ | wc -l)
       local app_use_cases=$(find src/application/use_cases/ -name "*.py" -type f 2>/dev/null | grep -v __pycache__ | wc -l)
       local infra_repos=$(find src/infrastructure/repositories/ -name "sql_*.py" -type f 2>/dev/null | grep -v __pycache__ | wc -l)
       
       if [[ $domain_entities -eq 0 ]]; then
           echo "❌ ドメイン層の実装が見つかりません"
           echo "💡 先に /implement-domain を実行してください"
           return 1
       fi
       
       if [[ $app_use_cases -eq 0 ]]; then
           echo "❌ アプリケーション層の実装が見つかりません"
           echo "💡 先に /implement-usecase を実行してください"
           return 1
       fi
       
       if [[ $infra_repos -eq 0 ]]; then
           echo "❌ インフラストラクチャ層の実装が見つかりません"
           echo "💡 先に /implement-infra を実行してください"
           return 1
       fi
       
       echo "  ✅ すべてのレイヤー実装確認完了"
       return 0
   }
   
   if ! validate_layer_implementations; then
       execute_rollback "missing_layer_implementations"
       exit 1
   fi
   
   # 🚨 CRITICAL: Check for placeholder assertions in presentation tests
   echo "  🚨 プレゼンテーション層プレースホルダーアサーション検証中..."
   
   presentation_placeholder_files=()
   while IFS= read -r -d '' file; do
       if grep -l 'assert False, "RED:' "$file" >/dev/null 2>&1; then
           presentation_placeholder_files+=("$file")
       fi
   done < <(find tests/e2e/ -name "*.py" -print0 2>/dev/null)
   
   if [[ ${#presentation_placeholder_files[@]} -gt 0 ]]; then
       echo "    ❌ プレゼンテーション層プレースホルダーアサーション発見:"
       for file in "${presentation_placeholder_files[@]:0:5}"; do
           count=$(grep -c 'assert False, "RED:' "$file" 2>/dev/null || echo "0")
           echo "      - $file: $count 個"
       done
       [[ ${#presentation_placeholder_files[@]} -gt 5 ]] && echo "      - ... (他 $((${#presentation_placeholder_files[@]} - 5)) ファイル)"
       
       echo ""
       echo "    🚨 CRITICAL ISSUE: これらのテストは意図的にFALSE失敗しています"
       echo "       - プレゼンテーション実装は完了済みだが、テストがプレースホルダーのまま"
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
           echo "プレゼンテーション層実装をキャンセルしました"
           echo "💡 推奨: 手動でプレースホルダーテストを適切なテストに置き換えてから再実行"
           execute_rollback "presentation_placeholder_assertions_found"
           exit 1
       fi
       
       echo "    ⚠️  プレースホルダーテストを無視して続行（後で修正が必要）"
   else
       echo "    ✅ プレゼンテーション層プレースホルダーアサーション: なし（正常なテスト状態）"
   fi
   
   echo "✅ 前提条件検証完了"
   ```

3. **Setup Template Variables**:
   ```bash
   # 📝 Setup template variables for code generation
   echo "📝 テンプレート変数設定中..."
   
   # Setup feature-based variables
   setup_feature_vars "$feature_name"
   
   # Extract entities from domain layer
   all_entities=()
   for entity_file in $(find src/domain/entities/ -name "*.py" -type f 2>/dev/null | grep -v __pycache__); do
       entity_name=$(basename "$entity_file" .py)
       entity_class=$(to_title_case "$entity_name")
       all_entities+=("$entity_class")
   done
   
   echo "  🎯 テンプレート変数設定:"
   echo "    - 機能名: $feature_name"
   echo "    - エンティティ: ${#all_entities[@]} 個"
   
   echo "✅ テンプレート変数設定完了"
   ```

4. **Create Presentation Layer Structure**:
   ```bash
   # 🎨 Create presentation layer structure
   echo "🎨 プレゼンテーション層構造作成中..."
   
   # Define presentation structure directories
   presentation_directories=(
       "src/presentation/api/controllers"
       "src/presentation/api/validators"
       "src/presentation/api/serializers"
       "src/presentation/api/middleware"
       "src/presentation/cli"
       "src/presentation/web"
   )
   
   # Create all presentation directories safely
   for dir in "${presentation_directories[@]}"; do
       echo "  📁 作成中: $dir"
       if ! safe_mkdir "$dir"; then
           echo "エラー: プレゼンテーションディレクトリ作成に失敗しました: $dir"
           execute_rollback "presentation_directory_creation_failed"
           exit 1
       fi
       add_rollback "rmdir '$dir' 2>/dev/null || true" "Remove presentation directory: $dir"
   done
   
   echo "✅ プレゼンテーション構造作成完了"
   ```

5. **Generate API Components Using Templates**:
   ```bash
   # ✅ Generate API components using templates
   echo "✅ APIコンポーネント生成中..."
   
   implemented_files=()
   
   # Generate API Validator
   validator_file="src/presentation/api/validators/${feature_name_snake}_validator.py"
   echo "  ✅ 生成中: API Validator ($validator_file)"
   
   if ! process_template "presentation/validator_template.py" "$validator_file"; then
       echo "エラー: バリデーターテンプレート処理に失敗しました"
       execute_rollback "validator_template_failed"
       exit 1
   fi
   
   implemented_files+=("$validator_file")
   add_rollback "rm -f '$validator_file'" "Remove generated validator"
   
   # Generate API Serializer
   serializer_file="src/presentation/api/serializers/${feature_name_snake}_serializer.py"
   echo "  📄 生成中: API Serializer ($serializer_file)"
   
   if ! process_template "presentation/serializer_template.py" "$serializer_file"; then
       echo "エラー: シリアライザーテンプレート処理に失敗しました"
       execute_rollback "serializer_template_failed"
       exit 1
   fi
   
   implemented_files+=("$serializer_file")
   add_rollback "rm -f '$serializer_file'" "Remove generated serializer"
   
   # Generate API Controller
   controller_file="src/presentation/api/controllers/${feature_name_snake}_controller.py"
   echo "  🎮 生成中: API Controller ($controller_file)"
   
   if ! process_template "presentation/controller_template.py" "$controller_file"; then
       echo "エラー: コントローラーテンプレート処理に失敗しました"
       execute_rollback "controller_template_failed"
       exit 1
   fi
   
   implemented_files+=("$controller_file")
   add_rollback "rm -f '$controller_file'" "Remove generated controller"
   
   echo "✅ APIコンポーネント生成完了"
   ```

6. **Generate FastAPI Application**:
   ```bash
   # 🚀 Generate FastAPI application
   echo "🚀 FastAPI アプリケーション生成中..."
   
   app_file="src/presentation/api/app.py"
   echo "  🚀 生成中: FastAPI Application ($app_file)"
   
   # Create custom FastAPI app template content (inline for now)
   app_template_content='"""
   '"$feature_name"' FastAPI Application

   '"$feature_name"' 機能のREST API サーバー。
   実装日時: '"$(date)"'
   """

   from fastapi import FastAPI, HTTPException, Depends, Query, Path
   from fastapi.middleware.cors import CORSMiddleware
   from fastapi.responses import JSONResponse
   from pydantic import BaseModel, Field
   from typing import Dict, Any, Optional
   import logging
   import os

   from src.application.use_cases.'"${feature_name_snake}"'_use_case import '"${feature_name_title}"'UseCase
   from src.infrastructure.config.database import get_database_session
   from .controllers.'"${feature_name_snake}"'_controller import '"${feature_name_title}"'Controller

   # FastAPI アプリケーション初期化
   app = FastAPI(
       title="'"$feature_name"' API",
       description="'"$feature_name"' 機能のREST API",
       version="1.0.0"
   )

   # CORS設定
   app.add_middleware(
       CORSMiddleware,
       allow_origins=["*"],
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
   )

   # ヘルスチェックエンドポイント
   @app.get("/health")
   async def health_check():
       return {"status": "healthy", "service": "'"$feature_name"'"}

   # TODO: Add actual API endpoints using controller
   '
   
   if ! safe_create_file "$app_file" "$app_template_content" true; then
       echo "エラー: FastAPIアプリケーションファイルの作成に失敗しました"
       execute_rollback "app_creation_failed"
       exit 1
   fi
   
   implemented_files+=("$app_file")
   add_rollback "rm -f '$app_file'" "Remove FastAPI app"
   
   echo "✅ FastAPI アプリケーション生成完了"
   ```

7. **Generate E2E Tests**:
   ```bash
   # 🧪 Generate E2E tests for presentation layer
   echo "🧪 E2Eテスト生成中..."
   
   # Create E2E test directory if needed
   if ! safe_mkdir "tests/e2e/api"; then
       echo "エラー: E2Eテストディレクトリの作成に失敗しました"
       execute_rollback "e2e_test_dir_creation_failed"
       exit 1
   fi
   
   e2e_test_file="tests/e2e/api/test_${feature_name_snake}_api.py"
   echo "  🧪 生成中: E2E API Test ($e2e_test_file)"
   
   if ! process_template "tests/e2e_test_template.py" "$e2e_test_file"; then
       echo "エラー: E2Eテストテンプレート処理に失敗しました"
       execute_rollback "e2e_test_template_failed"
       exit 1
   fi
   
   implemented_files+=("$e2e_test_file")
   add_rollback "rm -f '$e2e_test_file'" "Remove generated E2E test"
   
   echo "✅ E2Eテスト生成完了"
   ```

8. **Run E2E Tests and Update Metadata**:
   ```bash
   # 🟢 Run E2E tests to verify presentation layer
   echo "🟢 E2Eテスト実行中..."
   
   # Validate Python environment for testing
   if ! validate_python_environment; then
       echo "エラー: Python環境の検証に失敗しました"
       execute_rollback "python_env_validation_failed"
       exit 1
   fi
   
   # Run E2E tests
   e2e_test_output_file="/tmp/e2e_test_output_$$"
   e2e_test_result=0
   
   if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/e2e/ -v --tb=short > "$e2e_test_output_file" 2>&1; then
       e2e_test_result=0
   else
       e2e_test_result=1
   fi
   
   # Analyze test results
   total_e2e_tests=$(grep -c "test_.*PASSED\\|test_.*FAILED" "$e2e_test_output_file" 2>/dev/null || echo "0")
   passed_e2e_tests=$(grep -c "PASSED" "$e2e_test_output_file" 2>/dev/null || echo "0")
   failed_e2e_tests=$(grep -c "FAILED" "$e2e_test_output_file" 2>/dev/null || echo "0")
   
   echo "  📊 E2Eテスト結果:"
   echo "    - 総テスト数: $total_e2e_tests"
   echo "    - 成功: $passed_e2e_tests"
   echo "    - 失敗: $failed_e2e_tests"
   
   rm -f "$e2e_test_output_file"
   e2e_tests_passed=$([ $failed_e2e_tests -eq 0 ] && echo "true" || echo "false")
   
   # 📊 Update metadata with presentation implementation completion
   metadata_file="docs/use_cases/issue-${issue_list}-${feature_name}.json"
   
   if ! update_metadata_atomic "$metadata_file" \
       '.phases.presentation_implementation.completed = true |
        .phases.presentation_implementation.completed_at = "'"$(date -u +%Y-%m-%dT%H:%M:%SZ)"'" |
        .phases.presentation_implementation.e2e_tests_passed = '"$e2e_tests_passed"' |
        .updated_at = "'"$(date -u +%Y-%m-%dT%H:%M:%SZ)"'" |
        .spec_files.presentation_implementation = ['"$(printf '"%s",' "${implemented_files[@]}" | sed 's/,$//')"'] |
        .phase = "presentation_implemented" |
        .next_commands = ["refactor", "run-all-tests", "use-case-status"]'; then
       echo "エラー: メタデータの更新に失敗しました"
       execute_rollback "metadata_update_failed"
       exit 1
   fi
   
   echo "✅ E2Eテスト実行・メタデータ更新完了"
   ```

9. **Commit Changes and Update GitHub Issues**:
   ```bash
   # 📚 Commit changes and update GitHub issues
   echo "📚 変更のコミットとGitHubイシュー更新中..."
   
   # Create commit message
   commit_message="feat: implement presentation layer for $(printf 'issue #%s ' "${issue_numbers[@]}")- ${feature_name}

   Presentation Layer Implementation Summary:
   - Feature: ${feature_name}
   - Issues: $(printf '#%s ' "${issue_numbers[@]}")
   - Generated Files: ${#implemented_files[@]} files using templates
   - E2E Test Results: Passed $passed_e2e_tests, Failed $failed_e2e_tests
   
   Generated Components:
   $(printf '  - %s\n' "${implemented_files[@]}")
   
   Template-based Implementation:
   - API validators with comprehensive input validation
   - Response serializers with consistent output format
   - Controllers with proper error handling
   - FastAPI application with OpenAPI documentation
   - E2E tests for complete API coverage
   
   Next Step: /refactor or /run-all-tests
   "
   
   files_to_commit=("$metadata_file")
   files_to_commit+=("${implemented_files[@]}")
   
   if ! safe_git_commit "$commit_message" "${files_to_commit[@]}"; then
       echo "エラー: コミットに失敗しました"
       execute_rollback "commit_failed"
       exit 1
   fi
   
   # Update GitHub issues
   for issue_num in "${issue_numbers[@]}"; do
       issue_comment="🎨 **プレゼンテーション層実装完了**

   プレゼンテーション層の実装が完了しました。テンプレートベースの自動生成により、一貫性のあるREST APIが構築されました。

   ## 📊 実装結果
   - **生成ファイル数**: ${#implemented_files[@]} ファイル
   - **E2Eテスト結果**: 成功 $passed_e2e_tests / 総計 $total_e2e_tests
   - **実装方式**: テンプレートベース自動生成

   ## 🎨 生成されたコンポーネント
   - **APIバリデーター**: 入力データの検証とサニタイゼーション
   - **APIシリアライザー**: レスポンス形式の統一化
   - **APIコントローラー**: HTTP リクエスト処理
   - **FastAPIアプリ**: REST APIサーバー
   - **E2Eテスト**: API動作検証

   ## 🚀 次のステップ
   \`\`\`bash
   /refactor $issue_num      # コード品質向上
   /run-all-tests $issue_num # 全テスト実行
   \`\`\`

   ---
   **Phase**: presentation_implemented ✅ → 次: refactor 🔧"
       
       safe_add_issue_comment "$issue_num" "$issue_comment" || true
   done
   
   echo "✅ コミット・GitHub更新完了"
   ```

10. **Final Success**:
    ```bash
    # 🎉 Transaction commit and final success message
    if commit_transaction; then
        echo ""
        echo "🎉 プレゼンテーション層実装完了!"
        echo "============================================="
        echo "🎨 機能名: $feature_name"
        echo "🎫 対象イシュー: $(printf '#%s ' "${issue_numbers[@]}")"
        echo "📊 生成ファイル数: ${#implemented_files[@]} 個"
        echo ""
        echo "📋 生成されたコンポーネント:"
        echo "   - APIバリデーター: 入力検証"
        echo "   - APIシリアライザー: レスポンス変換"
        echo "   - APIコントローラー: HTTP処理"
        echo "   - FastAPIアプリ: REST APIサーバー"
        echo "   - E2Eテスト: API検証"
        echo ""
        echo "🟢 テンプレートベース実装の利点:"
        echo "   - 一貫性のあるコード構造"
        echo "   - 保守性の向上"
        echo "   - 開発速度の向上"
        echo "   - エラーの削減"
        echo ""
        echo "🚀 次のステップ:"
        echo "   1. リファクタリング: /refactor $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
        echo "   2. 全テスト実行: /run-all-tests $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
        echo "   3. 進捗確認: /use-case-status $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
        echo ""
        echo "✅ テンプレートベース・プレゼンテーション層実装完了!"
        echo ""
        echo "🚨 MANDATORY FOR CLAUDE CODE: SCENARIO EVOLUTION CHECK"
        echo "   プレゼンテーション実装中に新要件・UI変更・エッジケース発見時は"
        echo "   作業を中断して /evolve-scenarios <feature-name> を実行すること"
        echo "   CRITICAL: UI変更はユーザー体験に直接影響します"
        
    else
        echo "❌ トランザクション コミット失敗"
        exit 1
    fi
    ```

Important Notes:
- Template-based implementation ensures consistency and maintainability
- All code templates are stored separately and can be reused
- Variable substitution allows customization for different features
- Reduced code duplication and improved development speed
- All user-facing output must be in JAPANESE