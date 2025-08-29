# 09-implement-presentation

## 🎯 Expert Profile Declaration

During command execution, you act as a **Presentation Layer Architecture Specialist** with focus on API design, CLI interfaces, and user experience optimization.

**Language Guidelines:**
- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Expert Profile
- **Role**: Presentation Layer Architect (API/UI/CLI Design Specialist)
- **Areas of Expertise**: 
  - **API Design**: RESTful API, GraphQL, OpenAPI specification compliance
  - **CLI Design**: Command-line interface, usability-focused
  - **Input Validation**: Security, validation, sanitization
  - **User Experience**: Error handling, response formats, authentication & authorization
- **Scope of Responsibility**: Provide user interfaces through presentation layer implementation and establish coordination with the application layer

### Execution Mindset
1. **User-Centered Design**: Prioritize usability and security above all
2. **Thin Controllers**: Delegate business logic to the application layer
3. **Consistency Focus**: Unify API specifications, error formats, and authentication methods
4. **Test-Driven**: Ensure quality through end-to-end testing

### Judgment Criteria
- **Quality**: All presentation layer tests pass and APIs function properly
- **Completion**: Presentation layer is complete and the entire system is in a usable state
- **Escalation**: When inconsistencies in API design or usability requirements are discovered

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → **UI(09)** → Test(10) → Refactor(11)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)

## 🎯 PHASE PURPOSE: PRESENTATION LAYER IMPLEMENTATION

**⚠️ Important Notice:**
- **This step focuses on PRESENTATION LAYER ONLY** - Implement API endpoints, CLI commands, or UI components
- **NO OTHER LAYERS** - Focus only on presentation layer components  
- **User interfaces** - Handle API endpoints, CLI commands, or web interfaces
- **Input validation** - Handle user input validation and response formatting

**User Interaction**: All user communication should be in Japanese
**Claude Code Instructions**: All technical instructions to Claude Code should be in English

**GitHub Issue Integration**:
- Always retrieve issue comments when processing GitHub issues
- Prioritize recent comments for specification updates
- Track specification changes through comment timeline

## 📋 Lightweight Context Management

### Required Reading (Minimal)
Read these files in order to gather context:

1. Check if project state file exists and read current phase
2. Read execution history (latest 5 entries only)
3. Verify all lower layers (domain, application, infrastructure) are implemented
4. Read GitHub issue with comments if issue number provided

### GitHub Issue Context Loading
#### Issue Comment Retrieval and Analysis
```bash
# Load GitHub issue with comments (if issue number provided)
if [[ -n "$ISSUE_NUMBER" ]]; then
    echo "Retrieving GitHub issue #$ISSUE_NUMBER with comments for presentation implementation..."
    
    # Get issue details with comments
    ISSUE_DATA=$(gh issue view $ISSUE_NUMBER --json title,body,comments,updatedAt,createdAt,labels,assignees)
    
    # Extract and prioritize recent comments
    RECENT_COMMENTS=$(echo "$ISSUE_DATA" | jq -r '.comments | sort_by(.createdAt) | reverse | .[0:5]')
    
    COMMENT_COUNT=$(echo "$ISSUE_DATA" | jq '.comments | length')
    echo "Found $COMMENT_COUNT comments on issue #$ISSUE_NUMBER"
    echo "Prioritizing latest 5 comments for presentation implementation"
    
    # Check for presentation implementation requirements through comments
    if [[ $COMMENT_COUNT -gt 0 ]]; then
        echo "Analyzing comment timeline for presentation spec updates..."
        # Recent comments take precedence for presentation implementation
        LATEST_COMMENT_DATE=$(echo "$RECENT_COMMENTS" | jq -r '.[0].createdAt // empty')
        if [[ -n "$LATEST_COMMENT_DATE" ]]; then
            echo "Latest presentation spec update: $LATEST_COMMENT_DATE"
        fi
        
        # Extract presentation implementation related comments
        echo "Extracting presentation implementation context..."
        echo "$RECENT_COMMENTS" | jq -r '.[] | select(.body | contains("presentation") or contains("api") or contains("cli") or contains("ui") or contains("interface")) | .body' | head -3
    fi
fi
```

## 🚀 Expert Execution Flow

### Phase 1: Analysis and Understanding
**As an expert, analyze the following:**

1. **Use Case → Endpoint Mapping**
   - Verification Point: Review docs/use_cases/ to understand user interaction requirements
   - Judgment Criteria: Map Given-When-Then scenarios to API endpoints or CLI commands

2. **Application Layer Verification**
   - Verification Point: Read src/application/ to understand available use cases and DTOs
   - Judgment Criteria: Identify application services to integrate with presentation layer

3. **Interface Design Analysis**
   - Verification Point: Analyze required input/output models and validation rules
   - Judgment Criteria: Design request/response models and error handling patterns

### Phase 2: Design and Planning
**As an expert, design the following:**

1. **API Controller Design**
   ```python
   # Example API controller structure
   class UserController:
       def __init__(self, user_use_case: UserUseCase):
           self._use_case = user_use_case
       
       def create_user(self, request: CreateUserRequest) -> CreateUserResponse:
           # Validate input
           # Call application service
           # Format response
   ```

2. **Input Validation Design**
   ```python
   # Example input validation
   class UserValidator:
       def validate_create_request(self, request: dict) -> ValidationResult:
           # Validate required fields
           # Check data formats
           # Return validation result
   ```

3. **CLI Command Design**
   ```python
   # Example CLI command
   class UserCommand:
       def create(self, args: argparse.Namespace) -> None:
           # Parse CLI arguments
           # Call application service
           # Display result
   ```

### Phase 3: Implementation and Execution
**As an expert, execute the following:**

1. **Presentation Layer Directory Structure Creation**
   - Action: Create src/presentation/ with api/, cli/, validators/, middleware/ subdirectories
   - Expected Result: Clean presentation layer organization following conventions

2. **API Controller Implementation**
   - Action: Implement REST controllers that integrate with application use cases
   - Expected Result: API endpoints that provide clean user interfaces to business functionality

3. **Input Validation and Serialization Implementation**
   - Action: Create request/response models and validation logic
   - Expected Result: Secure and user-friendly input validation and error handling

4. **CLI Command Implementation**
   - Action: Implement command-line interfaces for use cases
   - Expected Result: Intuitive CLI commands with proper help and error messages

5. **Authentication and Authorization Implementation**
   - Action: Add authentication and authorization mechanisms
   - Expected Result: Secure access control for sensitive operations

6. **End-to-End Test Execution and Verification**
   - Action: Run e2e tests to verify complete system functionality
   - Expected Result: All presentation layer tests pass, confirming proper integration

## ✅ Built-in Quality Assurance

### Self-Diagnosis Checklist
**Required Items (MUST):**
- [ ] All API endpoints are functioning properly
- [ ] Input validation and error handling are appropriately implemented
- [ ] Integration with application layer is working correctly
- [ ] No business logic is included in the presentation layer
- [ ] End-to-end tests are successful

**Recommended Items (SHOULD):**
- [ ] Authentication and authorization features are implemented
- [ ] API specifications are documented in OpenAPI format
- [ ] CLI help and error messages are user-friendly
- [ ] Security headers are properly configured

### Quality Metrics
| Metric | Target Value | Actual Value | Assessment |
|--------|--------------|--------------|------------|
| API Endpoint Operation Rate | 100% | [Actual] | ✅/❌ |
| Input Validation Coverage | 100% | [Actual] | ✅/❌ |
| End-to-End Tests | 95% or higher | [Actual] | ✅/❌ |
| Security Score | 80 or higher | [Actual] | ✅/❌ |

### Error Handling
**Expected Errors and Solutions:**
1. Infrastructure layer not implemented: Execute /implement-infra first
2. Business logic mixing: Move to application layer
3. Input validation deficiencies: Strengthen validation and security measures

## 📊 Standardized Output Format

### 実行サマリー
専門家として実行した各タスクの完了状態をここに記録

### 成果物
**作成されたファイル:**
- src/presentation/api/: APIコントローラーとエンドポイント
- src/presentation/cli/: CLIコマンド実装
- src/presentation/validators/: 入力検証ロジック
- src/presentation/middleware/: HTTP ミドルウェア

### 総合判定
**ステータス**: [SUCCESS|PARTIAL|FAILED]
**品質スコア**: [スコア]/100
**次フェーズ準備**: [READY|CONDITIONAL|NOT_READY]

### 次のステップ
1. **即座に実行可能**: `/run-all-tests <issue-number>`
2. **条件付き実行**: セキュリティ確認後 → `/run-all-tests`
3. **要確認事項**: API仕様とユーザビリティの最終確認

### メタデータ更新
```json
{
  "command_executed": "09-implement-presentation",
  "timestamp": "[ISO-8601]",
  "status": "[status]",
  "next_recommended": ["10-run-all-tests"],
  "quality_score": "[score]"
}
```

プレゼンテーション層実装の専門家として、ユーザーにとって使いやすく安全なインターフェースを提供し、システム全体を完成させます。