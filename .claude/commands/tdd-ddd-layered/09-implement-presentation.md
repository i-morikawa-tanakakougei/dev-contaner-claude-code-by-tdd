Use the 09-implement-presentation subagent to implement presentation layer (API endpoints, CLI, or UI). This command MUST USE PROACTIVELY the specialized 09-implement-presentation subagent for optimal presentation layer implementation.

**📖 Required Reading**: Before execution, this command MUST read the following files:
- `/workspace/.claude/context/current-command-context.json` - Current execution context
- `/workspace/.claude/context/project-context.json` - Overall project state and active sprint information
- `/workspace/docs/use_cases/issue-X-Y.json` - Issue-specific metadata and implementation status
- `/workspace/docs/metadata/project-state.json` - Integrated project status for update

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
> ➡️ **Next Stage**: 10-run-all-tests (All Tests Execution)
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
🖼️ Issues: #15 のプレゼンテーション層実装を開始します
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

**🤖 Agent Integration**: This command MUST USE PROACTIVELY the specialized `09-implement-presentation` subagent for optimal presentation layer implementation.

## 📖 Subagent Document Reading Instructions

This command delegates to the specialized `09-implement-presentation` subagent.

**MANDATORY: The subagent MUST read these files before execution:**

1. `docs/index.md` - Project overview and current status
2. `/workspace/.claude/context/current-command-context.json` - Current execution context (includes issue numbers)
3. `src/application/` - Application layer use cases to integrate with presentation endpoints
4. `docs/use_cases/issue-X-Y.md` - Use case specifications for API endpoint or CLI command design
5. `docs/domain/issue-X-Y-domain-model.md` - Domain model design for input/output model creation
6. `tests/` - Test files to understand presentation layer requirements and e2e scenarios
7. Any existing presentation layer files in `src/presentation/` - For pattern consistency
8. API documentation or CLI specification files for interface consistency

**Command-Specific Reading Focus - Presentation Layer Implementation:**
- Map Given-When-Then scenarios to API endpoints, CLI commands, or UI interactions
- Design request/response models based on application layer DTOs
- Understand user interface requirements from use case specifications
- Review application services to ensure proper integration without bypassing layers
- Design input validation and error response patterns for user-friendly interfaces

**Additional Context for Subagent Execution:**
- API design conventions and REST endpoint patterns
- CLI command design patterns and user experience guidelines
- Input validation strategies and error message formatting
- Authentication and authorization implementation patterns
- IMPORTANT: Use Read tool to access actual file contents, not just references

**CRITICAL:** Use the Read tool to actually read file contents, not just reference paths.

 Claude Code should automatically delegate this task to the 09-implement-presentation subagent based on the command description.

1. **Pre-execution Validation**:
   ```bash
   # Validate issue number requirement
   if [[ $# -eq 0 ]]; then
       echo "エラー: 少なくとも1つのイシュー番号を指定してください"
       echo "使用例: /implement-presentation 1"
       echo "使用例: /implement-presentation 1,7 (複数イシュー)"
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
   
   # Check for infrastructure layer implementation
   missing_infra=()
   for issue_num in "${issue_numbers[@]}"; do
       # Look for infrastructure implementation files
       if ! find src/infrastructure/repositories/ -name "*${issue_num}*.py" -o -name "*issue*${issue_num}*.py" -type f 2>/dev/null | head -1 >/dev/null; then
           missing_infra+=("$issue_num")
       fi
   done
   
   if [[ ${#missing_infra[@]} -gt 0 ]]; then
       echo "❌ エラー: 以下のIssueのインフラストラクチャ層実装が見つかりません:"
       printf '  - Issue #%s\n' "${missing_infra[@]}"
       echo "💡 先に /implement-infra を実行してください"
       exit 1
   fi
   
   echo "🖼️ Issues: $(printf '#%s ' "${issue_numbers[@]}")のプレゼンテーション層実装を開始します"
   ```

2. **Context Preparation and Agent Execution**:
   ```bash
   # 🔄 Prepare context for agent (Pattern B: Hybrid approach)
   echo "🖼️ コンテキスト準備とエージェント起動..."
   
   # Create context file with presentation layer information
   context_file="/workspace/.claude/context/current-command-context.json"
   current_time=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
   
   # Build context JSON for presentation layer implementation
   cat > "$context_file" <<EOF
   {
     "command": "implement-presentation",
     "timestamp": "$current_time",
     "issue_numbers": [$(IFS=,; echo "${issue_numbers[*]}")],
     "phase": "presentation-layer",
     "context": {
       "expected_outputs": [
         "src/presentation/api/controllers/",
         "src/presentation/cli/commands/",
         "src/presentation/ui/components/",
         "src/presentation/middleware/"
       ],
       "architecture_patterns": ["Clean Architecture", "API First", "MVC"]
     },
     "additional_instructions": "プレゼンテーション層を実装してください。アプリケーション層のユースケースをAPIエンドポイント、CLIコマンド、またはUI画面として公開してください。入力検証、エラーハンドリング、認証・認可を適切に実装し、ユーザーにとって使いやすいインターフェースを提供してください。",
     "special_considerations": [
       "アプリケーション層ユースケース（src/application/）との密な連携",
       "RESTful API設計とOpenAPI仕様への準拠",
       "入力検証とセキュリティ対策の実装",
       "エンドツーエンドテストの作成と実行"
     ],
     "custom_context": {
       "api_design": true,
       "input_validation": true,
       "security_implementation": true,
       "e2e_testing": true
     }
   }
   EOF
   
   echo "✅ コンテキストファイル作成完了: $context_file"
   
   # 🤖 Call the specialized agent with hybrid context
   echo ""
   echo "🖼️ プレゼンテーション実装エージェントを起動します..."
   echo "専門エージェントがAPI・CLI・UI層を実装します"
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
[09-implement-presentation固有のタスクを実行]

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

   # Execute with specialized 09-implement-presentation subagent
   # The 09-implement-presentation subagent will be automatically invoked based on the task description
   
   agent_exit_code=$?
   echo "✅ 専用エージェント実行完了 (終了コード: $agent_exit_code)"
   
   echo "✅ エージェント呼び出し設定完了"
   echo "エージェントが以下の処理を実行します:"
   echo "  - コンテキストファイルからのイシュー情報取得"
   echo "  - ユースケースからAPIエンドポイントへのマッピングと設計"
   echo "  - APIコントローラーとHTTPリクエスト処理の実装"
   echo "  - 入力検証とレスポンス形式の標準化"
   echo "  - CLIコマンドとユーザーインターフェースの実装"
   echo "  - エンドツーエンドテストと統合検証の実行"
   echo "  - エラーハンドリングとセキュリティ機能の実装"
   ```

3. **Agent Result Verification**:
   ```bash
   # 🔍 Verify agent execution results
   echo "🔍 エージェント実行結果を検証中..."
   
   # Check that presentation files were created
   echo "  🔍 プレゼンテーション層ファイルの作成確認中..."
   
   created_files=()
   for issue_num in "${issue_numbers[@]}"; do
       # Look for controller implementation files
       controller_pattern="src/presentation/api/controllers/*${issue_num}*controller*.py"
       if ls $controller_pattern 2>/dev/null | head -1 >/dev/null; then
           controller_files=$(ls $controller_pattern 2>/dev/null)
           for file in $controller_files; do
               created_files+=("$file")
               echo "    ✅ Issue #$issue_num のコントローラーを確認: $(basename "$file")"
           done
       else
           echo "    ❌ Issue #$issue_num のコントローラーが見つかりません"
       fi
       
       # Check for API endpoints
       api_pattern="src/presentation/api/*${issue_num}*.py"
       if ls $api_pattern 2>/dev/null | head -1 >/dev/null; then
           api_files=$(ls $api_pattern 2>/dev/null)
           for file in $api_files; do
               created_files+=("$file")
               echo "    ✅ Issue #$issue_num のAPIファイルを確認: $(basename "$file")"
           done
       fi
       
       # Check metadata update
       metadata_pattern="docs/use_cases/*issue*${issue_num}*.json"
       if ls $metadata_pattern 2>/dev/null | head -1 >/dev/null; then
           metadata_file=$(ls $metadata_pattern 2>/dev/null | head -1)
           if command -v jq >/dev/null 2>&1; then
               presentation_status=$(jq -r '.phases.presentation_implementation.completed // false' "$metadata_file" 2>/dev/null)
               if [[ "$presentation_status" == "true" ]]; then
                   echo "    ✅ Issue #$issue_num のメタデータが更新されました"
               else
                   echo "    ⚠️ Issue #$issue_num のメタデータ更新が未確認"
               fi
           fi
       fi
   done
   
   # Check if src/presentation directory exists
   if [[ ! -d "src/presentation" ]]; then
       echo "❌ エラー: src/presentation ディレクトリが作成されていません"
       exit 1
   fi
   
   # Report validation results
   if [[ ${#created_files[@]} -eq 0 ]]; then
       echo "❌ エージェント実行検証失敗: プレゼンテーション層ファイルが作成されていません"
       exit 1
   fi
   
   echo "✅ エージェント実行結果検証完了"
   
   # 🔧 Load advanced task verification library
   source "$(dirname "${BASH_SOURCE[0]}")/_task_verification.sh"
   
   # ✨ New: Advanced task verification with retry capability
   echo "🔍 Critical tasks確認中..."
   if ! verify_critical_tasks "09-implement-presentation" "$latest_report"; then
       echo "⚠️ Critical tasks確認で問題が検出されました - 再実行を試行します"
       prepare_retry_context "09-implement-presentation" "1" "${verification_issues[@]}"
       
       # Enhanced context for retry
       echo "🔄 再実行用の強化コンテキスト準備中..."
       prepare_enhanced_context "09-implement-presentation" "$context_file" "${verification_issues[@]}"
       
       echo "💡 推奨アクション: エージェントを再実行してください"
       echo "   重点項目: $(IFS='|'; echo "${verification_issues[*]}")"
       exit 1
   fi
   
   echo "✅ Critical tasks確認完了 - 全項目クリア"
   ```

4. **Display Presentation Implementation Success Summary**:
   ```bash
   # 📊 Display comprehensive presentation implementation summary
   echo ""
   echo "🎉 プレゼンテーション層実装完了!"
   echo "============================================="
   
   # Show created presentation files
   echo "📁 作成されたプレゼンテーションファイル:"
   for file in "${created_files[@]}"; do
       if [[ -f "$file" ]]; then
           echo "   ✅ $file"
       fi
   done
   
   # Show presentation components summary
   echo ""
   echo "🎨 プレゼンテーション層コンポーネント:"
   if [[ ${#created_files[@]} -gt 0 ]]; then
       controller_count=$(printf '%s\n' "${created_files[@]}" | grep -c "controller" || echo "0")
       api_count=$(printf '%s\n' "${created_files[@]}" | grep -c "api" || echo "0")
       cli_count=$(printf '%s\n' "${created_files[@]}" | grep -c "cli" || echo "0")
       
       echo "   📊 APIコントローラー: $controller_count 個"
       echo "   📊 APIエンドポイント: $api_count 個"
       echo "   📊 CLIコマンド: $cli_count 個"
   fi
   
   # Show next steps
   echo ""
   echo "📋 次のステップ (全テスト実行・リファクタリング):"
   for issue_num in "${issue_numbers[@]}"; do
       echo "   /run-all-tests $issue_num"
       echo "   /refactor $issue_num"
   done
   
   echo ""
   echo "📚 重要ドキュメント:"
   echo "   - プレゼンテーション実装: src/presentation/"
   echo "   - API仕様: OpenAPI/Swagger ドキュメント"
   if [[ ${#created_files[@]} -gt 0 ]]; then
       echo "   - 実装されたファイル: ${created_files[0]} 他"
   fi
   
   echo ""
   echo "🔗 関連リソース:"
   for issue_num in "${issue_numbers[@]}"; do
       echo "   - Issue #$issue_num: gh issue view $issue_num"
   done
   
   echo ""
   echo "✅ プレゼンテーション層実装完了 - システム完成準備完了!"
   ```

Important Notes:
- Keep presentation layer lightweight and focused
- Delegate all business logic to application layer
- Use proper input validation and error handling
- Ensure consistent API response formats
- All user-facing output must be in JAPANESE

## 🔄 Metadata Update Requirements

**CRITICAL**: After successful presentation implementation completion, you MUST update the following files:

1. **Project State Update**:
   ```bash
   # Update docs/metadata/project-state.json
   # - Increment presentation_layer.api_endpoints count
   # - Update architecture_overview.presentation_layer.completion_rate
   # - Add to recent_activity.last_command_executed
   # - Update workflow_statistics.command_execution_stats
   ```

2. **Project Context Update**:
   ```bash
   # Update .claude/context/project-context.json  
   # - Update architecture_status.presentation_layer.api_endpoints array
   # - Increment workflow_tracking.command_usage.implement_presentation
   # - Set current_state.last_command and last_command_timestamp
   ```

3. **Issue-Specific Metadata**:
   ```bash
   # Update docs/use_cases/issue-X-Y.json
   # - Set presentation_layer.status to "completed"
   # - Add implementation_files array with created presentation files
   # - Update completion timestamp
   ```

**⚠️ Error Handling**: If standard workflow is disrupted:
- 📖 Consult: [Manual Sync Guide](../../docs/maintenance/manual-sync-guide.md)
- 🔄 Check Status: `/use-case-status` for current project state
- 📊 Verify Context: `.claude/context/current-command-context.json`