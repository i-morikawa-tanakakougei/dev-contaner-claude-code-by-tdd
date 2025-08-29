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

## 📋 軽量コンテキスト管理

### Required Reading (Minimal)
```bash
# Issue numbers from command arguments
ISSUE_NUMBERS="$1"

# Read use case specifications for each issue
for issue_num in $(echo $ISSUE_NUMBERS | tr ',' ' '); do
    USE_CASE_FILE=$(find docs/use_cases/ -name "*issue*${issue_num}*.md" -type f | head -1)
    if [[ -f "$USE_CASE_FILE" ]]; then
        Read "$USE_CASE_FILE"
    fi
    
    # Read corresponding domain model
    DOMAIN_FILE=$(find docs/domain/ -name "*issue*${issue_num}*.md" -type f | head -1)
    if [[ -f "$DOMAIN_FILE" ]]; then
        Read "$DOMAIN_FILE"
    fi
done

# Read existing test patterns for consistency
if [[ -d "tests" ]]; then
    Glob tests/**/*.py
fi
```

### GitHub Issue Integration
```bash
# Load GitHub issue with comments (if issue number provided)
if [[ -n "$ISSUE_NUMBERS" ]]; then
    for issue_num in $(echo $ISSUE_NUMBERS | tr ',' ' '); do
        # Retrieve issue details with recent comments prioritized
        Bash gh issue view $issue_num --json title,body,comments
        Bash gh issue view $issue_num --json comments --jq '.comments | sort_by(.createdAt) | reverse | .[0:3]'
    done
fi
```

## 🚀 専門家実行フロー

### Phase 1: 分析と理解
**専門家として以下を分析 (ユーザーとのやり取りは日本語):**

1. **Given-When-Then シナリオの分析**
   - Extract test scenarios from use case specifications using Read tool
   - Map each Given-When-Then to specific test methods
   - Identify acceptance criteria for testable assertions
   - Parse domain model design for entity and behavior expectations

2. **テスト構造の計画**
   - Plan unit tests for individual entities and value objects
   - Plan integration tests for repository interfaces and application services
   - Plan e2e tests for complete user scenarios
   - Design test organization following src/ directory hierarchy

### Phase 2: 設計と計画
**専門家として以下を設計 (Claude Codeへの指示は英語):**

1. **ドメインレイヤーテスト設計**
   ```
   For each domain entity:
   - Test entity creation and validation
   - Test business behavior and methods
   - Test business rule enforcement
   - Test invariant protection
   ```

2. **アプリケーションレイヤーテスト設計**
   ```
   For each use case:
   - Test use case orchestration
   - Test external dependency mocking
   - Test error handling and validation
   - Test transaction boundaries
   ```

3. **テストデータとモック設計**
   ```
   Design test infrastructure:
   - Test fixtures for domain objects
   - Mock objects for external dependencies
   - Test utilities and helper functions
   - Test database configuration if needed
   ```

### Phase 3: 実装と実行
**専門家として以下を実行 (Claude Codeへの指示は英語):**

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

2. **Create test directory structure**
   ```bash
   # Create comprehensive test directory structure
   Bash mkdir -p tests/unit/domain
   Bash mkdir -p tests/unit/application
   Bash mkdir -p tests/integration
   Bash mkdir -p tests/e2e
   Bash mkdir -p tests/fixtures
   ```

3. **Create failing tests for each issue**
   ```bash
   for issue_num in $(echo $1 | tr ',' ' '); do
       # Create domain layer tests
       Write "tests/unit/domain/test_issue_${issue_num}_domain.py" with:
       # - Entity creation and validation tests (must fail)
       # - Value object tests (must fail)
       # - Business rule enforcement tests (must fail)
       # - Domain service tests (must fail)
       
       # Create application layer tests  
       Write "tests/unit/application/test_issue_${issue_num}_usecase.py" with:
       # - Use case orchestration tests (must fail)
       # - Application service tests (must fail)
       # - Input validation tests (must fail)
       
       # Create integration tests
       Write "tests/integration/test_issue_${issue_num}_integration.py" with:
       # - Repository interface tests (must fail)
       # - External service integration tests (must fail)
       
       # Create test fixtures
       Write "tests/fixtures/issue_${issue_num}_fixtures.py" with:
       # - Test data factories
       # - Mock object configurations
       # - Test utilities
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
       METADATA_FILE=$(find docs/use_cases/ -name "*issue*${issue_num}*.json" -type f | head -1)
       if [[ -f "$METADATA_FILE" ]]; then
           # Update metadata to mark TDD RED phase as complete
           # Set phases.tdd_tests.created to true
           # Add test file references
       fi
   done
   
   # Git commit all test files
   Bash git add tests/
   Bash git commit -m "feat: create TDD RED phase tests for issues $(echo $1 | tr ',' ' ')

Create comprehensive failing tests based on Given-When-Then scenarios.
All tests fail as expected in TDD RED phase - ready for implementation.

🎯 Generated with Claude Code
"
   ```

## ✅ 内蔵品質保証

### 自己診断チェックリスト
**必須項目（MUST）:**
- [ ] すべてのGiven-When-Thenシナリオがテストケースに変換されている
- [ ] ドメインエンティティと値オブジェクトのテストが作成されている
- [ ] アプリケーションユースケースのテストが作成されている
- [ ] すべてのテストが失敗している（TDD RED確認）
- [ ] 外部依存関係が適切にモック化されている
- [ ] テストが独立性を保っている

**推奨項目（SHOULD）:**
- [ ] 統合テストが作成されている
- [ ] エンドツーエンドテストが計画されている
- [ ] テストフィクスチャが適切に設計されている
- [ ] テストカバレッジが適切に設定されている

### 品質メトリクス
| 指標 | 目標値 | 実績値 | 判定 |
|------|--------|--------|------|
| シナリオテストカバレッジ | 100% | [実績値] | ✅/❌ |
| TDD RED確認 | 100% | [実績値] | ✅/❌ |
| テスト独立性 | 100% | [実績値] | ✅/❌ |

### エラー処理
**想定されるエラーと対処:**
1. **前提条件不足**: ユースケース仕様またはドメインモデルが未作成の場合の案内
2. **テストが成功してしまう**: 実装コードの混入チェックと修正
3. **テスト依存性**: テスト間の依存関係検出と修正

## 📊 標準化出力フォーマット

### 実行サマリー (日本語でユーザーに報告)
- ✅ **Given-When-Then分析**: [Issue numbers] のシナリオを分析完了
- ✅ **テスト構造作成**: ドメイン・アプリケーション・統合テスト作成
- ✅ **TDD RED確認**: すべてのテストが期待通り失敗
- ✅ **テストファイル作成**: tests/ 配下に [count] ファイル作成

### 成果物
**作成されたファイル:**
- `tests/unit/domain/test_issue_X_domain.py`: ドメインレイヤーテスト
- `tests/unit/application/test_issue_X_usecase.py`: アプリケーションレイヤーテスト  
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
```

**ユーザーへのメッセージ (日本語)**:
```
🎉 TDDテスト作成完了（RED phase）！

🔴 TDD RED状態確認:
   ✅ すべてのテストが失敗（実装前のため正常）
   ✅ Given-When-Thenシナリオからテスト自動生成
   ✅ ドメインモデルに基づくエンティティテスト
   ✅ アプリケーションユースケーステスト

📁 作成されたテストファイル:
   ✅ テストファイル: [count] 個
   - tests/unit/domain/
   - tests/unit/application/
   - tests/integration/
   - tests/fixtures/

📋 次のステップ (TDD GREEN phase):
   /implement-domain [issue-numbers]

✅ TDD RED段階完了 - 実装準備完了！
```