# 05-create-tests (Expert Mode Integration)

## 🎯 Expert Profile Declaration

During command execution, you act as a **Test-Driven Development Architect** specialist.

**Language Guidelines:**

- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Your Expertise

- **TDD RED Phase Mastery**: Creating failing tests that capture business requirements
- **Domain-Driven Testing**: Test structure aligned with DDD tactical patterns
- **Given-When-Then Translation**: Converting scenarios into comprehensive test cases
- **Test Architecture**: Proper test isolation, mocking, and fixture design

### Execution Principles

1. **TDD Discipline**: Create only failing tests - no production code implementation
2. **Business Behavior Focus**: Tests capture business intent, not technical implementation
3. **Test Independence**: Each test is isolated and repeatable

### Quality Standards

- **Scenario Coverage**: All Given-When-Then scenarios have corresponding tests
- **Test Failure**: All tests must fail initially (RED phase validation)
- **Test Clarity**: Tests clearly specify expected behavior and business rules

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Sprint Execution Phase - TDD Test Creation (05/16)  
> 🎯 **Phase Purpose**: Create failing tests from Given-When-Then scenarios (RED)  
> ⬅️ **Previous Stage**: 04-domain-modeling (Domain Model Design)  
> ➡️ **Next Stage**: 06-implement-domain (Domain Layer Implementation)

## 🔴 **TDD RED PHASE: FAILING TESTS ONLY**

**⚠️ Important Notice:**

- **This step is TDD RED PHASE** - Create failing tests based on specifications
- **CREATE FAILING TESTS ONLY** - Do not implement any production code
- **TDD Discipline** - Tests must fail initially to validate TDD cycle

**TDD Cycle Position:**

1. `04-domain-modeling` ← Design documentation
2. `05-create-tests` ← **【YOU ARE HERE】TDD RED (failing tests)**
3. `06-implement-domain` ← TDD GREEN (make tests pass)
4. `11-refactor` ← TDD REFACTOR (improve code quality)

**CREATE FAILING TESTS ONLY.**

## 📋 Lightweight Context Management

### Required Reading (Minimal)

```bash
# Validate issue number parameter
if [[ -z "$1" ]]; then
    echo "ERROR: Issue number required. Usage: /create-tests <issue-number>"
    exit 1
fi

ISSUE_NUMBER="$1"
echo "🧪 Executing create-tests with automated Python implementation (TDD RED Phase)..."

# Execute the enhanced Python implementation
SCRIPT_PATH=".claude/commands/tdd-ddd-layered-expert/utils/05-create-tests.py"

if [[ -f "$SCRIPT_PATH" ]]; then
    echo "✅ Found enhanced implementation: $SCRIPT_PATH"
    uv run "$SCRIPT_PATH" "$ISSUE_NUMBER"
    EXIT_CODE=$?

    if [[ $EXIT_CODE -eq 0 ]]; then
        echo "✅ Test creation completed successfully (RED Phase)"
        echo "💡 All tests should be FAILING - this is expected in TDD RED phase"
    else
        echo "❌ Test creation failed with exit code: $EXIT_CODE"
        exit $EXIT_CODE
    fi
else
    echo "❌ Enhanced implementation not found: $SCRIPT_PATH"
    echo "💡 Please ensure the Python implementation is available"
    exit 1
fi
```

### GitHub Issue Integration

#### Issue Comment Retrieval and Analysis

```bash
# Load GitHub issue with comments (if issue number provided)
if [[ -n "$ISSUE_NUMBERS" ]]; then
    for issue_num in $(echo $ISSUE_NUMBERS | tr ',' ' '); do
        echo "Retrieving GitHub issue #$issue_num with comments for test creation..."

        # Get issue details with comments
        ISSUE_DATA=$(gh issue view $issue_num --json title,body,comments,updatedAt,createdAt,labels,assignees)

        # Extract and prioritize recent comments
        RECENT_COMMENTS=$(echo "$ISSUE_DATA" | jq -r '.comments | sort_by(.createdAt) | reverse | .[0:5]')

        COMMENT_COUNT=$(echo "$ISSUE_DATA" | jq '.comments | length')
        echo "Found $COMMENT_COUNT comments on issue #$issue_num"
        echo "Prioritizing latest 5 comments for test specification analysis"

        # Check for test requirement evolution through comments
        if [[ $COMMENT_COUNT -gt 0 ]]; then
            echo "Analyzing comment timeline for test requirement changes..."
            # Recent comments take precedence for test creation
            LATEST_COMMENT_DATE=$(echo "$RECENT_COMMENTS" | jq -r '.[0].createdAt // empty')
            if [[ -n "$LATEST_COMMENT_DATE" ]]; then
                echo "Latest test requirement update: $LATEST_COMMENT_DATE"
            fi

            # Extract test-related comments
            echo "Extracting test specification context..."
            echo "$RECENT_COMMENTS" | jq -r '.[] | select(.body | contains("test") or contains("scenario") or contains("given") or contains("when") or contains("then") or contains("expect")) | .body' | head -3
        fi
    done
fi
```

## 🚀 Expert Execution Flow

### Phase 1: Analysis and Understanding

**As an expert, analyze the following (user interactions in Japanese):**

1. **Given-When-Then Scenario Analysis**

   - Extract test scenarios from use case specifications using Read tool
   - Map each Given-When-Then to specific test methods
   - Identify acceptance criteria for testable assertions
   - Parse domain model design for entity and behavior expectations

2. **Test Structure Planning**
   - Plan unit tests for individual entities and value objects
   - Plan integration tests for repository interfaces and application services
   - Plan e2e tests for complete user scenarios
   - Design test organization following src/ directory hierarchy

### Phase 2: Design and Planning

**As an expert, design the following (instructions to Claude Code in English):**

1. **Domain Layer Test Design**

   ```
   For each domain entity:
   - Test entity creation and validation
   - Test business behavior and methods
   - Test business rule enforcement
   - Test invariant protection
   ```

2. **Application Layer Test Design**

   ```
   For each use case:
   - Test use case orchestration
   - Test external dependency mocking
   - Test error handling and validation
   - Test transaction boundaries
   ```

3. **Infrastructure Layer Test Design**

   ```
   For each infrastructure component:
   - Test repository implementations
   - Test external service integrations
   - Test data persistence and retrieval
   - Test configuration and connection management
   ```

4. **Presentation Layer Test Design**

   ```
   For each presentation component:
   - Test controller request handling
   - Test input validation and response formatting
   - Test authentication and authorization
   - Test UI component behavior
   ```

5. **Test Data and Mock Design**
   ```
   Design test infrastructure:
   - Test fixtures for domain objects
   - Mock objects for external dependencies
   - Test utilities and helper functions
   - Test database configuration if needed
   ```

### Phase 3: Implementation and Execution

**As an expert, execute the following (instructions to Claude Code in English):**

1. **Validate issue numbers and prerequisites**

   ```bash
   # Validate issue number requirement
   if [[ $# -eq 0 ]]; then
       echo "エラー: 少なくとも1つのイシュー番号を指定してください"
       echo "使用例: /create-tests 1"
       exit 1
   fi

   # Check for use case specifications and domain models
   for issue_num in $(echo $1 | tr ',' ' '); do
       USE_CASE_FILE=$(find docs/use_cases/ -name "*issue*${issue_num}*.md" -type f | head -1)
       DOMAIN_FILE=$(find docs/domain/ -name "*issue*${issue_num}*.md" -type f | head -1)

       if [[ ! -f "$USE_CASE_FILE" ]]; then
           echo "❌ エラー: Issue #${issue_num} のユースケース仕様が見つかりません"
           exit 1
       fi

       if [[ ! -f "$DOMAIN_FILE" ]]; then
           echo "❌ エラー: Issue #${issue_num} のドメインモデルが見つかりません"
           exit 1
       fi
   done
   ```

2. **Create TDD/DDD/Layered Architecture test directory structure**

   ```bash
   # Create comprehensive layered test directory structure
   # Domain layer tests (GREEN phase: 06-implement-domain)
   Bash mkdir -p tests/unit/domain/entities
   Bash mkdir -p tests/unit/domain/value_objects
   Bash mkdir -p tests/unit/domain/domain_services
   Bash mkdir -p tests/unit/domain/repositories

   # Application layer tests (GREEN phase: 07-implement-usecase)
   Bash mkdir -p tests/unit/application/use_cases
   Bash mkdir -p tests/unit/application/services

   # Infrastructure layer tests (GREEN phase: 08-implement-infra)
   Bash mkdir -p tests/unit/infrastructure/repositories
   Bash mkdir -p tests/unit/infrastructure/external_services

   # Presentation layer tests (GREEN phase: 09-implement-presentation)
   Bash mkdir -p tests/unit/presentation/controllers
   Bash mkdir -p tests/unit/presentation/views

   # Integration and E2E tests
   Bash mkdir -p tests/integration
   Bash mkdir -p tests/e2e
   Bash mkdir -p tests/fixtures
   ```

3. **Create failing tests for each issue (TDD/DDD/Layered Architecture)**

   ```bash
   for issue_num in $(echo $1 | tr ',' ' '); do
       # Domain layer tests (GREEN phase: 06-implement-domain)
       # Entity tests
       Write "tests/unit/domain/entities/test_issue_${issue_num}_entities.py" with:
       # - Entity creation and validation tests (must fail)
       # - Business invariant enforcement tests (must fail)
       # - Entity behavior and method tests (must fail)

       # Value object tests
       Write "tests/unit/domain/value_objects/test_issue_${issue_num}_value_objects.py" with:
       # - Value object creation and immutability tests (must fail)
       # - Value object equality and validation tests (must fail)
       # - Value object business logic tests (must fail)

       # Domain service tests
       Write "tests/unit/domain/domain_services/test_issue_${issue_num}_domain_services.py" with:
       # - Domain service orchestration tests (must fail)
       # - Cross-entity business rule tests (must fail)
       # - Domain service behavior tests (must fail)

       # Repository interface tests
       Write "tests/unit/domain/repositories/test_issue_${issue_num}_repository_interfaces.py" with:
       # - Repository interface contract tests (must fail)
       # - Repository query specification tests (must fail)

       # Application layer tests (GREEN phase: 07-implement-usecase)
       # Use case tests
       Write "tests/unit/application/use_cases/test_issue_${issue_num}_use_cases.py" with:
       # - Use case orchestration and workflow tests (must fail)
       # - Use case input validation and error handling tests (must fail)
       # - Use case transaction boundary tests (must fail)

       # Application service tests
       Write "tests/unit/application/services/test_issue_${issue_num}_app_services.py" with:
       # - Application service coordination tests (must fail)
       # - External dependency mocking tests (must fail)
       # - Application service validation tests (must fail)

       # Infrastructure layer tests (GREEN phase: 08-implement-infra)
       # Repository implementation tests
       Write "tests/unit/infrastructure/repositories/test_issue_${issue_num}_repo_impl.py" with:
       # - Repository implementation tests (must fail)
       # - Data persistence and retrieval tests (must fail)
       # - Database operation tests (must fail)

       # External service tests
       Write "tests/unit/infrastructure/external_services/test_issue_${issue_num}_external.py" with:
       # - External service integration tests (must fail)
       # - API communication tests (must fail)
       # - External dependency handling tests (must fail)

       # Presentation layer tests (GREEN phase: 09-implement-presentation)
       # Controller tests
       Write "tests/unit/presentation/controllers/test_issue_${issue_num}_controllers.py" with:
       # - HTTP request handling tests (must fail)
       # - Input validation and response formatting tests (must fail)
       # - Authentication and authorization tests (must fail)

       # Integration tests
       Write "tests/integration/test_issue_${issue_num}_integration.py" with:
       # - End-to-end workflow integration tests (must fail)
       # - Cross-layer integration tests (must fail)
       # - Database integration tests (must fail)

       # Test fixtures
       Write "tests/fixtures/issue_${issue_num}_fixtures.py" with:
       # - Test data factories for all layers
       # - Mock object configurations
       # - Test utilities and helper functions
   done
   ```

4. **Create test configuration**

   ```bash
   # Create pytest configuration
   Write "pytest.ini" with pytest configuration settings
   Write "conftest.py" with shared test fixtures and setup
   ```

5. **Verify RED phase - all tests must fail**

   ```bash
   # Run all tests to verify RED phase
   echo "🔴 TDD RED フェーズ検証: すべてのテストが失敗することを確認中..."

   # Run pytest and expect failures
   if Bash pytest tests/ --tb=short; then
       echo "⚠️ 警告: テストが成功しています。TDD REDフェーズではすべてのテストが失敗すべきです。"
       echo "実装コードが含まれていないか確認してください。"
   else
       echo "✅ TDD REDフェーズ確認完了: すべてのテストが期待通り失敗しています"
   fi
   ```

6. **Update metadata and commit**

   ```bash
   # Update use case metadata files
   for issue_num in $(echo $1 | tr ',' ' '); do
       METADATA_FILE=$(find docs/use_cases/sprints/ -name "*issue*${issue_num}*.json" -type f | head -1)
       if [[ -f "$METADATA_FILE" ]]; then
           # Update metadata to mark TDD RED phase as complete
           # Set phases.tdd_tests.created to true
           # Add test file references
       fi
   done

   # Git commit all test files
   Bash git add tests/
   Bash git commit -m "feat: create TDD RED phase tests for issues $(echo $1 | tr ',' ' ')
   ```

Create comprehensive failing tests based on Given-When-Then scenarios.
All tests fail as expected in TDD RED phase - ready for implementation.

🎯 Generated with Claude Code
"

````

## ✅ Built-in Quality Assurance

### Self-Diagnostic Checklist
**Required Items (MUST):**
- [ ] All Given-When-Then scenarios are converted to test cases
- [ ] Domain entity and value object tests are created
- [ ] Application use case tests are created
- [ ] All tests are failing (TDD RED confirmation)
- [ ] External dependencies are properly mocked
- [ ] Tests maintain independence

**Recommended Items (SHOULD):**
- [ ] Integration tests are created
- [ ] End-to-end tests are planned
- [ ] Test fixtures are appropriately designed
- [ ] Test coverage is properly configured

### Quality Metrics
| Metric | Target Value | Actual Value | Assessment |
|--------|--------------|--------------|------------|
| Scenario Test Coverage | 100% | [Actual Value] | ✅/❌ |
| TDD RED Confirmation | 100% | [Actual Value] | ✅/❌ |
| Test Independence | 100% | [Actual Value] | ✅/❌ |

### Error Handling
**Expected Errors and Countermeasures:**
1. **Prerequisite Shortage**: Guidance when use case specifications or domain models are not created
2. **Tests Succeed**: Check and fix for implementation code contamination
3. **Test Dependencies**: Detection and correction of inter-test dependencies

## 📊 Standardized Output Format

### 実行サマリー (日本語でユーザーに報告)
- ✅ **Given-When-Then分析**: [Issue numbers] のシナリオを分析完了
- ✅ **テスト構造作成**: ドメイン・アプリケーション・統合テスト作成
- ✅ **TDD RED確認**: すべてのテストが期待通り失敗
- ✅ **テストファイル作成**: tests/ 配下に [count] ファイル作成

### 成果物 (TDD/DDD/Layered Architecture準拠)
**作成されたテストファイル (レイヤー別):**

**ドメインレイヤーテスト (GREEN: 06-implement-domain):**
- `tests/unit/domain/entities/test_issue_X_entities.py`: エンティティテスト
- `tests/unit/domain/value_objects/test_issue_X_value_objects.py`: 値オブジェクトテスト
- `tests/unit/domain/domain_services/test_issue_X_domain_services.py`: ドメインサービステスト
- `tests/unit/domain/repositories/test_issue_X_repository_interfaces.py`: リポジトリインターフェーステスト

**アプリケーションレイヤーテスト (GREEN: 07-implement-usecase):**
- `tests/unit/application/use_cases/test_issue_X_use_cases.py`: ユースケーステスト
- `tests/unit/application/services/test_issue_X_app_services.py`: アプリケーションサービステスト

**インフラレイヤーテスト (GREEN: 08-implement-infra):**
- `tests/unit/infrastructure/repositories/test_issue_X_repo_impl.py`: リポジトリ実装テスト
- `tests/unit/infrastructure/external_services/test_issue_X_external.py`: 外部サービステスト

**プレゼンテーションレイヤーテスト (GREEN: 09-implement-presentation):**
- `tests/unit/presentation/controllers/test_issue_X_controllers.py`: コントローラーテスト

**統合・フィクスチャ:**
- `tests/integration/test_issue_X_integration.py`: 統合テスト
- `tests/fixtures/issue_X_fixtures.py`: テストフィクスチャ
- `pytest.ini`, `conftest.py`: テスト設定

### 総合判定
**ステータス**: `SUCCESS`
**品質スコア**: [スコア]/100
**次フェーズ準備**: `READY`

### 次のステップ (日本語でユーザーに案内)
1. **即座に実行可能**: `/implement-domain [issue-numbers]`
2. **推奨**: TDD GREENフェーズ（ドメイン実装）に進む
3. **確認推奨**: 作成されたテストケースのレビュー

### メタデータ更新
```bash
# Update project state metadata
if [[ -f "docs/metadata/project-state.json" ]]; then
 # Update overall_status to "tdd_red_phase_completed"
 # Update test layer metrics
 # Increment create_tests completions
fi
````

**ユーザーへのメッセージ (日本語)**:

```
🎉 TDD/DDD/Layered Architectureテスト作成完了（RED phase）！

🔴 TDD RED状態確認:
   ✅ すべてのテストが失敗（実装前のため正常）
   ✅ Given-When-Thenシナリオからテスト自動生成
   ✅ レイヤー別テスト構造完全準拠

📁 作成されたテストファイル (レイヤー別):
   🏗️ ドメインレイヤー: [count] ファイル
   - tests/unit/domain/entities/
   - tests/unit/domain/value_objects/
   - tests/unit/domain/domain_services/
   - tests/unit/domain/repositories/

   ⚙️ アプリケーションレイヤー: [count] ファイル
   - tests/unit/application/use_cases/
   - tests/unit/application/services/

   🔧 インフラ・プレゼンテーションレイヤー: [count] ファイル
   - tests/unit/infrastructure/
   - tests/unit/presentation/

   🔄 統合テスト: [count] ファイル
   - tests/integration/
   - tests/fixtures/

📋 次のステップ (TDD GREEN phases):
   1. /implement-domain [issue-numbers] (ドメインレイヤー実装)
   2. /implement-usecase [issue-numbers] (アプリケーションレイヤー実装)
   3. /implement-infra [issue-numbers] (インフラレイヤー実装)
   4. /implement-presentation [issue-numbers] (プレゼンテーションレイヤー実装)

✅ TDD RED段階完了 - レイヤー別実装準備完了！
```
