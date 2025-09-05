# 05-create-tests-enhanced (MCP-Enhanced Test Creation)

## 🎯 Expert Profile Declaration

During command execution, you act as a **Test-Driven Development Architect** specialist with **MCP Enhancement** capabilities.

**Language Guidelines:**

- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Your Expertise (Core + MCP Enhanced)

**Core TDD Expertise:**

- **TDD RED Phase Mastery**: Creating failing tests that capture business requirements
- **Domain-Driven Testing**: Test structure aligned with DDD tactical patterns
- **Given-When-Then Translation**: Converting scenarios into comprehensive test cases
- **Test Architecture**: Proper test isolation, mocking, and fixture design

**MCP-Enhanced Capabilities:**

- **Intelligent Test Discovery**: Automated test scenario identification using Serena MCP
- **Context-Aware Test Patterns**: Context7-enhanced testing patterns and best practices
- **Business Rule Test Mining**: Automated extraction of business rule validation tests
- **Coverage Gap Analysis**: Complete test coverage analysis and gap identification

### Execution Principles (Core + MCP Enhanced)

**Core Principles:**

1. **TDD Discipline**: Create only failing tests - no production code implementation
2. **Business Behavior Focus**: Tests capture business intent, not technical implementation
3. **Test Independence**: Each test is isolated and repeatable

**MCP-Enhanced Principles:** 4. **Intelligent Test Generation**: Leverage Serena for comprehensive test scenario identification 5. **Pattern-Based Design**: Apply Context7 testing patterns and industry best practices 6. **Automated Coverage**: Ensure complete business rule validation through intelligent analysis

### Quality Standards (Core + MCP Enhanced)

**Core Standards:**

- **Scenario Coverage**: All Given-When-Then scenarios have corresponding tests
- **Test Failure**: All tests must fail initially (RED phase validation)
- **Test Clarity**: Tests clearly specify expected behavior and business rules

**MCP-Enhanced Standards:**

- **Automated Rule Coverage**: 100% of identified business rules covered by tests
- **Pattern Compliance**: 95% adherence to testing best practices from Context7
- **Code Coverage Target**: 90%+ coverage for domain logic
- **Test Maintainability**: High cohesion, low coupling in test design

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

**🧠 MCP Enhancement**: Serena (Test Discovery + Code Analysis) + Context7 (Testing Patterns + Best Practices)

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Sprint Execution Phase - TDD Test Creation (05/16) **[MCP-Enhanced Version]**  
> 🎯 **Phase Purpose**: Create failing tests from Given-When-Then scenarios (RED) with MCP intelligence  
> ⬅️ **Previous Stage**: 04-domain-modeling (Domain Model Design) or 04-domain-modeling-enhanced  
> ➡️ **Next Stage**: 06-implement-domain (Domain Layer Implementation)

## 🔴 **TDD RED PHASE: FAILING TESTS ONLY WITH MCP ENHANCEMENT**

**⚠️ Important Notice:**

- **This step is TDD RED PHASE** - Create failing tests based on specifications
- **CREATE FAILING TESTS ONLY** - Do not implement any production code
- **TDD Discipline** - Tests must fail initially to validate TDD cycle
- **MCP ENHANCEMENT** - Leverage intelligent test discovery and pattern guidance

**TDD Cycle Position:**

1. `04-domain-modeling` ← Design documentation
2. `05-create-tests-enhanced` ← **【YOU ARE HERE】TDD RED (failing tests) with MCP**
3. `06-implement-domain` ← TDD GREEN (make tests pass)
4. `11-refactor` ← TDD REFACTOR (improve code quality)

**Core Activities (Traditional):**

- Extract test scenarios from Given-When-Then specifications
- Create failing tests for entities, value objects, and use cases
- Ensure proper test isolation and independence
- Validate TDD RED phase (all tests must fail)

**MCP-Enhanced Activities (Additional):**

- Analyze existing codebase for testable components using Serena MCP
- Extract business rule validation scenarios automatically
- Apply Context7 testing patterns and best practices
- Create intelligent test coverage analysis and gap identification
- Provide automated test maintenance recommendations

**CREATE FAILING TESTS ONLY.**

## 🚀 MCP強化TDDテスト作成実行フロー

```bash
#!/bin/bash
# MCP-Enhanced TDD Test Creation (RED Phase)

echo "🧪 MCP-Enhanced TDD Test Creation (RED Phase)..."

# Phase 1: 引数検証・MCP環境確認
echo "📚 Phase 1: Argument validation and MCP session analysis..."

# Issue番号検証
if [[ -z "$1" ]]; then
    echo "❌ ERROR: Issue number required. Usage: /create-tests-enhanced <issue-number>"
    exit 1
fi

ISSUE_NUMBER="$1"
echo "🎯 Creating failing tests for Issue #${ISSUE_NUMBER} with MCP enhancement..."

# MCP利用可能性確認
if [[ -f ".serena/sessions/current/session-metadata.json" ]]; then
    echo "✅ MCP session found - Enhanced test analysis available"
    MCP_AVAILABLE="true"
    echo "🔍 MCP Capabilities:"
    echo "  • Serena: Test discovery and coverage analysis"
    echo "  • Context7: Testing patterns and best practices"
else
    echo "ℹ️ MCP session not found - Running in standard mode"
    echo "💡 To enable MCP enhancements, run /context-session-stageup first"
    echo "📋 Enhanced features when available:"
    echo "  • Automated test scenario identification"
    echo "  • Business rule test mining"
    echo "  • Testing pattern integration"
    echo "  • Coverage gap analysis"
    MCP_AVAILABLE="false"
fi

# Phase 2: 前提条件確認
echo "🔍 Phase 2: Prerequisites validation..."

# ユースケース仕様ファイル確認
USE_CASE_FILE=$(find docs/use_cases/ -name "*issue*${ISSUE_NUMBER}*.md" -type f | head -1)
if [[ ! -f "$USE_CASE_FILE" ]]; then
    USE_CASE_FILE=$(find docs/use_cases/ -name "*${ISSUE_NUMBER}*.json" -type f | head -1)
fi

if [[ ! -f "$USE_CASE_FILE" ]]; then
    echo "❌ Error: Use case specification for Issue #${ISSUE_NUMBER} not found"
    echo "💡 Please execute /create-use-case ${ISSUE_NUMBER} first"
    exit 1
fi

# ドメインモデルファイル確認
DOMAIN_FILE=$(find docs/domain/ -name "*issue*${ISSUE_NUMBER}*domain-model.md" -type f | head -1)
if [[ ! -f "$DOMAIN_FILE" ]]; then
    echo "❌ Error: Domain model for Issue #${ISSUE_NUMBER} not found"
    echo "💡 Please execute /domain-modeling-enhanced ${ISSUE_NUMBER} first"
    exit 1
fi

echo "📄 Found use case specification: $USE_CASE_FILE"
echo "📄 Found domain model: $DOMAIN_FILE"

# 既存テスト構造確認
if [[ -d "tests" ]]; then
    Use LS tool to check existing test structure: tests/
fi

# Phase 3: ドキュメント分析
echo "📖 Phase 3: Document analysis and test scenario extraction..."

Use Read tool to analyze "$USE_CASE_FILE"
Use Read tool to analyze "$DOMAIN_FILE"

# Phase 4: MCP拡張分析（利用可能時）
if [[ "$MCP_AVAILABLE" == "true" ]]; then
    echo "🧠 Phase 4: MCP-enhanced test discovery..."
    
    # Serenaインテリジェント・テスト発見
    echo "📚 Serena: Discovering testable components and patterns..."
    Use mcp__serena__get_symbols_overview to identify existing test-related code
    Use mcp__serena__search_for_pattern "test_|Test|def.*test|@pytest|given|when|then" --restrict_search_to_code_files=true
    Use mcp__serena__search_for_pattern "assert|expect|should|validate|check" --context_lines_before=2 --context_lines_after=2
    Use mcp__serena__find_symbol "*test*|*Test*" --include_kinds=[12,6] --include_body=true
    
    # Context7テストパターン・ベストプラクティス統合
    echo "🌐 Context7: Analyzing testing patterns and best practices..."
    Use mcp__context7__resolve-library-id "testing-patterns"
    Use mcp__context7__resolve-library-id "tdd-best-practices"
    Use mcp__context7__get-library-docs "/testing-patterns" --topic "unit-testing"
    Use mcp__context7__get-library-docs "/testing-patterns" --topic "integration-testing"
    Use mcp__context7__get-library-docs "/tdd-best-practices" --topic "red-green-refactor"
    
    # ビジネスルールテストマイニング
    echo "🔍 Business rule test mining..."
    Use mcp__serena__search_for_pattern "business.*rule|invariant|constraint|validation" --context_lines_before=3 --context_lines_after=3
    
else
    echo "📋 Phase 4: Standard mode - Basic test scenario extraction"
fi

# Phase 5: テスト設計・戦略決定
echo "🎨 Phase 5: Test design and strategy planning..."

Ask user for the following test design decisions in Japanese:
1. テスト戦略の確認 (単体・統合・E2Eテストの分割)
2. Given-When-Thenシナリオの優先順位付け (enhanced with MCP analysis if available)
3. テストデータ・フィクスチャ設計 (based on domain model)
4. モック・スタブ戦略 (for external dependencies)
5. テストカバレッジ目標設定 (enhanced with gap analysis if MCP available)
6. 特別なテストケース (エラーケース・境界値・セキュリティ)

# Phase 6: テスト用ディレクトリ確認・作成
echo "📁 Phase 6: Test directory structure validation..."

# 基本テスト構造確認・作成
Ensure test directory structure exists:
- tests/unit/domain/entities/
- tests/unit/domain/value_objects/
- tests/unit/application/use_cases/
- tests/integration/repositories/
- tests/fixtures/

# Phase 7: TDD REDフェーズテスト作成
echo "🔴 Phase 7: Creating TDD RED Phase failing tests..."

**⚠️ TDD RED PHASE - FAILING TESTS ONLY**

# ドメインエンティティテスト作成
Create failing tests for domain entities identified in domain model:
- Entity identity and lifecycle tests
- Business rule validation tests  
- Invariant constraint tests
- Entity behavior tests

# 値オブジェクトテスト作成
Create failing tests for value objects:
- Immutability tests
- Validation rule tests
- Equality semantics tests
- Factory method tests

# ユースケーステスト作成
Create failing tests for use cases from Given-When-Then scenarios:
- Main scenario tests
- Alternative scenario tests
- Exception scenario tests
- Business rule integration tests

# リポジトリインターフェーステスト作成
Create failing tests for repository interfaces:
- CRUD operation tests
- Query method tests
- Constraint validation tests

# Phase 8: MCP拡張テスト強化（利用可能時）
if [[ "$MCP_AVAILABLE" == "true" ]]; then
    echo "🧠 Phase 8: Creating MCP-enhanced test cases..."
    
    # インテリジェント・テストカバレッジ分析
    echo "📊 Intelligent test coverage analysis..."
    Based on Serena analysis, create additional tests for:
    - Discovered business rule patterns
    - Missing validation scenarios
    - Edge cases and boundary conditions
    - Error handling scenarios
    
    # Context7パターンベーステスト
    echo "🌐 Pattern-based test creation..."
    Apply Context7 testing patterns to create:
    - Industry-standard test cases
    - Best practice test structures
    - Maintainable test patterns
    
    # テストメンテナンス推奨事項
    Create docs/tests/issue-${ISSUE_NUMBER}-test-maintenance-guide.md with:
    - Test refactoring recommendations
    - Coverage improvement suggestions
    - Test performance optimization
    - Future test evolution planning
    
    # Serena memoryに学習内容保存
    Use mcp__serena__write_memory "test-creation-$(date +%Y%m%d)-issue-${ISSUE_NUMBER}" "TDD RED phase test creation completed for issue ${ISSUE_NUMBER} with comprehensive failing tests, business rule coverage, and Context7 testing pattern integration"
fi

# Phase 9: テスト実行・RED検証
echo "🔴 Phase 9: TDD RED phase validation - Ensuring all tests fail..."

**CRITICAL: All tests must fail to validate TDD RED phase**

Use Bash tool to run tests and verify they fail:
PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/ -v

Verify that:
- All newly created tests fail as expected
- Test failure messages are clear and descriptive
- No production code exists to make tests pass
- Test structure is correct and runnable

# Phase 10: Gitコミット
echo "📝 Phase 10: Git commit for failing tests..."

Use Bash tool: git add tests/ docs/tests/ (if exists)

if [[ "$MCP_AVAILABLE" == "true" ]]; then
    Use Bash tool: git commit -m "test: create failing tests for issue ${ISSUE_NUMBER} (TDD RED phase) with MCP enhancement

Create comprehensive failing tests based on Given-When-Then scenarios.
Cover domain entities, value objects, use cases, and business rules.
Enhanced with MCP intelligent test discovery and pattern integration.

🔴 TDD RED PHASE: All tests failing as expected
🎯 Generated with Claude Code"
else
    Use Bash tool: git commit -m "test: create failing tests for issue ${ISSUE_NUMBER} (TDD RED phase)

Create comprehensive failing tests based on Given-When-Then scenarios.
Cover domain entities, value objects, use cases, and business rules.

🔴 TDD RED PHASE: All tests failing as expected  
🎯 Generated with Claude Code"
fi

# Phase 11: 品質保証・検証
echo "✅ Phase 11: Quality assurance and TDD validation..."

# 品質チェックリスト実行
Verify the following quality standards:

**Required Items (MUST):**
- [ ] All Given-When-Then scenarios have corresponding failing tests
- [ ] Domain entities, value objects, and use cases are tested
- [ ] All tests fail as expected (RED phase validation)
- [ ] Test structure follows Clean Architecture layers
- [ ] Git commit completed with proper TDD message

**Recommended Items (SHOULD) - MCP Enhanced:**
- [ ] Serena MCP test discovery completed (if MCP available)
- [ ] Context7 testing patterns applied (if MCP available)
- [ ] Business rule test mining completed (if MCP available)
- [ ] Coverage gap analysis performed (if MCP available)
- [ ] Test maintenance guide created (if MCP available)

# Phase 12: 実行サマリー・次ステップ案内
echo "🎉 Phase 12: Completion summary and next steps..."

Display to user in Japanese:
## ✅ 実行サマリー

**基本機能 (常に実行):**
- ✅ **ユースケース・ドメインモデル分析**: Issue #${ISSUE_NUMBER} の仕様・設計を分析完了
- ✅ **TDD REDフェーズテスト作成**: 全Given-When-Thenシナリオの失敗テスト作成
- ✅ **テスト構造構築**: Clean Architectureレイヤーに沿ったテスト構造
- ✅ **失敗検証完了**: 全テストが期待通り失敗することを確認

**MCP拡張機能 (利用可能時):**
- ✅ **MCPテスト発見**: Serenaによるテスト可能コンポーネント自動発見完了
- ✅ **ビジネスルールマイニング**: ビジネスルール検証テスト自動抽出完了
- ✅ **Context7パターン統合**: 最新テスト設計パターン・ベストプラクティス適用完了
- ✅ **カバレッジ分析**: インテリジェント・テストカバレッジ分析・ギャップ識別完了

## 📁 成果物

**基本ファイル (常に作成):**
- Comprehensive failing test suite in tests/ directory
- Entity, value object, and use case tests
- Integration and repository interface tests
- Test fixtures and utilities

**MCP拡張ファイル (利用可能時):**
- `docs/tests/issue-${ISSUE_NUMBER}-test-maintenance-guide.md`: テストメンテナンスガイド
- Enhanced test coverage with intelligent gap analysis
- Pattern-based test structures following Context7 best practices
- Updated MCP memory files: テスト作成結果の永続化

## 🚀 次のステップ

1. **即座に実行可能**: `/implement-domain ${ISSUE_NUMBER}` でTDD GREENフェーズ（実装）
2. **TDD GREENフェーズ**: 失敗テストを成功させる最小実装を作成
3. **確認必須**: 全テストが現在失敗していることの確認

**🔴 TDD RED PHASE完了 - 全テストが期待通り失敗中**

# メタデータ更新
Create docs/metadata/command-execution-log.json entry with:
{
  "command_executed": "create-tests-enhanced",
  "timestamp": "[current timestamp]",
  "status": "SUCCESS",
  "phase": "tdd-red-phase",
  "issue_number": "${ISSUE_NUMBER}",
  "mcp_enhancements": {
    "serena_test_discovery": [MCP_AVAILABLE],
    "context7_testing_patterns": [MCP_AVAILABLE],
    "business_rule_mining": [MCP_AVAILABLE],
    "coverage_gap_analysis": [MCP_AVAILABLE]
  },
  "metrics": {
    "failing_tests_created": "[number]",
    "test_files_generated": "[number]",
    "business_rules_tested": "[number]",
    "coverage_percentage": "[estimated]"
  },
  "next_recommended": ["implement-domain-enhanced"]
}

echo "🎯 MCP強化TDDテスト作成が完了しました！"
echo "🔴 TDD REDフェーズ: 全テストが期待通り失敗中"
echo "➡️ 次は /implement-domain ${ISSUE_NUMBER} でGREENフェーズに進んでください"
```

---

🎯 **MCP強化TDDテスト作成コマンド完成**

**使用方法**:
```bash
/create-tests-enhanced <issue-number>
```

**🔴 TDD REDフェーズ専用** - 失敗テストのみ作成

**MCP拡張機能** (利用可能時):
- 🧠 **Serena**: テスト発見・カバレッジ分析
- 📚 **Context7**: テストパターン・ベストプラクティス統合
   - Map each Given-When-Then to specific test methods
   - Identify acceptance criteria for testable assertions
   - Parse domain model design for entity and behavior expectations

2. **Test Structure Planning**
   - Plan unit tests for individual entities and value objects
   - Plan integration tests for repository interfaces and application services
   - Plan e2e tests for complete user scenarios
   - Design test organization following src/ directory hierarchy

**MCP-Enhanced Analysis (if available):** 3. **Automated Test Discovery**

- Use mcp**serena**get_symbols_overview to identify testable components
- Use mcp**serena**find_symbol to locate existing test patterns
- Use mcp**serena**search_for_pattern to find business logic requiring tests
- Create memory using mcp**serena**write_memory for test discovery results

4. **Intelligent Business Rule Test Mining**
   - Use mcp**serena**find_referencing_symbols to trace business rule usage
   - Extract validation scenarios from domain models using Serena analysis
   - Identify edge cases and boundary conditions automatically
   - Document test scenarios in architecture memory

### Phase 2: Design and Planning (Core + MCP Enhanced)

**As an expert, design the following (instructions to Claude Code in English):**

**Core Design Activities:**

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

3. **Infrastructure and Presentation Layer Test Design**

   ```
   For each infrastructure/presentation component:
   - Test repository implementations
   - Test external service integrations
   - Test controller request handling
   - Test input validation and response formatting
   ```

4. **Test Data and Mock Design**
   ```
   Design test infrastructure:
   - Test fixtures for domain objects
   - Mock objects for external dependencies
   - Test utilities and helper functions
   - Test database configuration if needed
   ```

**MCP-Enhanced Design (if available):** 5. **Context7 Testing Pattern Integration**

```
Use mcp__context7__resolve-library-id for "testing-best-practices"
Use mcp__context7__get-library-docs for TDD/BDD patterns
Use mcp__context7__get-library-docs for domain testing strategies
Integrate latest testing methodologies into test design
```

6. **Framework-Specific Test Enhancement**
   ```
   Identify testing framework from project analysis
   Use mcp__context7__resolve-library-id for framework-specific patterns
   Use mcp__context7__get-library-docs for mocking and assertion patterns
   Apply technology-specific testing guidance
   ```

### Phase 3: Intelligent Test Suite Generation

**Generate the following as expert (Instructions to Claude Code in English):**

1. **Domain Logic Test Generation**

   ```bash
   # Create comprehensive domain tests
   For each entity from domain analysis:
   - Generate entity behavior tests from Serena analysis
   - Create business rule validation tests
   - Generate edge case tests using Context7 patterns
   - Document test rationale and coverage mapping
   ```

2. **Value Object Test Generation**

   ```bash
   # Intelligent value object testing
   For each value object from domain analysis:
   - Generate validation rule tests automatically
   - Create immutability tests using pattern templates
   - Generate equality and hash code tests
   - Apply Context7 value object testing patterns
   ```

3. **Aggregate Test Generation**
   ```bash
   # Automated aggregate boundary testing
   Use Serena MCP to identify aggregate interactions
   Generate aggregate consistency tests
   Create transaction boundary tests
   Apply Context7 aggregate testing best practices
   ```

### Phase 4: Test Implementation and Documentation

**Execute the following as expert (Instructions to Claude Code in English):**

1. **Create comprehensive test files**

   ```bash
   Write "tests/domain/test_issue_${ISSUE_NUMBER}_entities.py" with:
   # - MCP-discovered entity behavior tests
   # - Intelligent business rule validation tests
   # - Automated edge case coverage
   # - Context7-enhanced test patterns
   # - Comprehensive assertion strategies
   ```

2. **Generate test coverage analysis**

   ```bash
   Write "tests/reports/issue_${ISSUE_NUMBER}_test_coverage_analysis.md" with:
   # - Serena MCP test discovery summary
   # - Business rule coverage mapping
   # - Test gap identification and recommendations
   # - Coverage metrics and targets
   # - Test maintenance guidance
   ```

3. **Create test execution guidance**

   ```bash
   Write "tests/reports/issue_${ISSUE_NUMBER}_test_execution_guide.md" with:
   # - Test execution strategy with MCP insights
   # - Performance testing recommendations
   # - Continuous integration setup guidance
   # - Test data management strategies
   # - Debugging and troubleshooting guidance
   ```

4. **Update MCP memory with test findings**
   ```bash
   Use mcp__serena__write_memory to store:
   # - Test discovery and analysis results
   # - Business rule test mapping
   # - Test pattern application outcomes
   # - Coverage analysis summary
   ```

## ✅ Built-in Quality Assurance

### Self-Diagnosis Checklist

**Required Items (MUST):**

- [ ] Serena MCP test discovery completed
- [ ] Context7 testing pattern integration applied
- [ ] Business rule validation tests generated
- [ ] Test coverage analysis completed
- [ ] Test gap identification performed
- [ ] Test execution guidance created

**Recommended Items (SHOULD):**

- [ ] Performance test scenarios included
- [ ] Integration test strategies defined
- [ ] Test data management patterns applied
- [ ] Continuous integration alignment verified

### Quality Metrics

| Metric                     | Target | Actual         | Assessment |
| -------------------------- | ------ | -------------- | ---------- |
| Business Rule Coverage     | 100%   | [Actual Value] | ✅/❌      |
| Test Pattern Compliance    | 95%    | [Actual Value] | ✅/❌      |
| Domain Logic Coverage      | 90%    | [Actual Value] | ✅/❌      |
| Test Maintainability Score | 85%    | [Actual Value] | ✅/❌      |

## 📊 Standardized Output Format

### 実行サマリー (日本語でユーザーに報告)

- ✅ **MCP テスト発見**: [X]個のテスト可能コンポーネント、[Y]個のビジネスルール分析完了
- ✅ **テストパターン統合**: Context7 最新テストパターン適用完了
- ✅ **テストスイート生成**: [Z]個のテストファイル、[W]個のテストケース生成
- ✅ **カバレッジ分析**: ビジネスロジックカバレッジ[P]%達成
- ✅ **実行ガイダンス生成**: MCP 分析に基づく実行戦略作成

### 成果物

**作成されたファイル:**

- `tests/domain/test_issue_X_entities.py`: エンティティテストスイート
- `tests/domain/test_issue_X_value_objects.py`: 値オブジェクトテストスイート
- `tests/domain/test_issue_X_aggregates.py`: アグリゲートテストスイート
- `tests/reports/issue_X_test_coverage_analysis.md`: テストカバレッジ分析レポート
- `tests/reports/issue_X_test_execution_guide.md`: テスト実行ガイド
- Updated MCP memory files: テスト分析結果の永続化

### 総合判定

**ステータス**: `MCP_ENHANCED_TESTS_SUCCESS`
**テスト品質**: [スコア]/100
**カバレッジ達成**: [カバレッジ]%

### 次のステップ (日本語でユーザーに案内)

1. **即座に実行可能**: `uv run --frozen pytest tests/domain/test_issue_${ISSUE_NUMBER}_*.py`
2. **推奨**: 生成されたテストの実行と検証
3. **確認推奨**: テストカバレッジ分析レポートの確認

**ユーザーへのメッセージ (日本語)**:

```
🎉 MCP強化テスト作成完了！

🧪 MCP分析結果:
   📊 Serena分析: [X]コンポーネント、[Y]ビジネスルール発見
   🔍 テスト発見: [Z]個のテストケース自動生成
   📋 ルールカバレッジ: [W]個のビジネスルール検証テスト
   🌐 Context7統合: 最新テスト設計パターン適用

🏗️ 生成されたテストスイート:
   📊 エンティティテスト: ビジネス動作検証
   📊 値オブジェクトテスト: 不変性・検証ルールテスト
   📊 アグリゲートテスト: 整合性境界テスト
   📊 ビジネスルールテスト: ドメインロジック検証

📁 作成されたファイル:
   ✅ tests/domain/test_issue_X_entities.py
   ✅ tests/domain/test_issue_X_value_objects.py
   ✅ tests/domain/test_issue_X_aggregates.py
   ✅ tests/reports/issue_X_test_coverage_analysis.md
   ✅ tests/reports/issue_X_test_execution_guide.md
   ✅ MCP メモリファイル更新

🚀 MCP強化機能:
   🔍 既存コードからのテストシナリオ自動発見
   📚 最新テスト設計パターンの自動統合
   🎯 ビジネスルール検証テスト自動生成
   📈 テストカバレッジギャップ自動特定

📊 テスト品質メトリクス:
   ✅ ビジネスルールカバレッジ: [P]%
   ✅ ドメインロジックカバレッジ: [Q]%
   ✅ テストパターン準拠: [R]%
   ✅ 保守性スコア: [S]%

🧪 テスト実行:
   uv run --frozen pytest tests/domain/test_issue_${ISSUE_NUMBER}_*.py -v

📋 次のステップ (TDD実装フェーズ):
   /implement-enhanced [issue-numbers]

✅ MCP強化テスト作成完了 - インテリジェントTDD実装準備完了！
```
