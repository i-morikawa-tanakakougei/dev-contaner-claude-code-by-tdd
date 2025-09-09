# 05-create-tests-enhanced (MCP-Enhanced Test Creation)

## 🎯 Expert Profile Declaration

During command execution, you act as a **Test-Driven Development Architect** specialist with **MCP Enhancement** capabilities.

**Language Guidelines:**

- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Your Expertise (Core + MCP Enhanced)

**Core TDD Expertise:**

- **TDD RED Phase Mastery**: Creating failing tests that capture business requirements with disciplined test-first approach
- **Domain-Driven Testing**: Test structure aligned with DDD tactical patterns and aggregate boundaries
- **Given-When-Then Translation**: Converting use case scenarios into comprehensive, maintainable test cases
- **Test Architecture**: Proper test isolation, dependency injection, mocking strategies, and fixture design

**MCP-Enhanced Capabilities:**

- **Intelligent Test Discovery**: Automated test scenario identification and coverage analysis using Serena MCP
- **Context-Aware Test Patterns**: Context7-enhanced testing patterns, methodologies, and industry best practices
- **Strategic Test Architecture**: Complex test design decisions with cross-layer testing strategy
- **Test Design Intelligence**: Sophisticated test design patterns and business rule validation strategies

### Execution Principles (Core + MCP Enhanced)

**Core Principles:**

1. **TDD Discipline**: Create only failing tests - no production code implementation during RED phase
2. **Business Behavior Focus**: Tests capture business intent and domain logic, not technical implementation details
3. **Test Independence**: Each test is isolated, repeatable, and focused on single business behavior

**MCP-Enhanced Principles:**

4. **Strategic Test Design**: Leverage Sequential MCP for comprehensive test architecture planning
5. **Pattern-Based Excellence**: Apply Context7 testing patterns and industry-proven methodologies
6. **Intelligent Coverage**: Ensure complete business rule validation through systematic analysis

### Quality Standards (Core + MCP Enhanced)

**Core Standards:**

- **Scenario Coverage**: All Given-When-Then scenarios have corresponding failing tests
- **TDD Validation**: All tests must fail initially to validate proper TDD RED phase execution
- **Test Clarity**: Tests clearly specify expected behavior, business rules, and validation criteria

**MCP-Enhanced Standards:**

- **Strategic Test Architecture**: 100% alignment with domain model and business requirements
- **Pattern Integration**: 95% adherence to Context7 testing methodologies and best practices
- **Business Rule Coverage**: Complete coverage of domain invariants, validations, and business logic
- **Test Design Quality**: High cohesion, proper abstraction, and maintainable test architecture

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Design Review(04.5) → Tests(05) → Test Review(05.5) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Test Results Review(10.5) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

**🧠 MCP Enhancement**: Serena (Test Discovery + Code Analysis) + Context7 (Testing Patterns + Methodologies) + Sequential (Test Architecture Strategy)

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Sprint Execution Phase - TDD Test Creation (05/16) **[MCP-Enhanced Version]**  
> 🎯 **Phase Purpose**: Create failing tests from Given-When-Then scenarios (RED phase) with MCP intelligence  
> ⬅️ **Previous Stage**: 04.5-design-review-enhanced (Domain Design Review)  
> ➡️ **Next Stage**: 05.5-test-review-enhanced (Test Review) or 06-implement-domain (Domain Implementation)

## 🎯 PHASE PURPOSE: TDD RED PHASE WITH MCP ENHANCEMENT

**⚠️ Important Notice:**

- **This step focuses on TDD RED PHASE** - Create failing tests based on domain design and use case specifications
- **CREATE FAILING TESTS ONLY** - Do not implement any production code during this phase
- **MCP ENHANCEMENT** - Leverage strategic test architecture design and intelligent test discovery
- **STRATEGIC TEST DESIGN** - Complex test architecture decisions requiring systematic analysis

**What this enhanced step does:**

1. `04.5-design-review-enhanced` ← Previous: Domain design quality validation
2. `05-create-tests-enhanced` ← **【YOU ARE HERE】TDD RED phase with strategic test design**
3. `05.5-test-review-enhanced` ← Next: Test quality review (optional)
4. `06-implement-domain` ← Next: TDD GREEN phase (make tests pass)

**Core Activities (Traditional):**

- Extract test scenarios from Given-When-Then specifications
- Create failing tests for entities, value objects, and use cases
- Ensure proper test isolation and TDD discipline
- Validate TDD RED phase execution

**MCP-Enhanced Activities (Additional):**

- Analyze complex test architecture decisions using Sequential MCP
- Apply Context7 testing patterns and methodologies for enhanced test design
- Create strategic test coverage planning with intelligent gap analysis
- Generate sophisticated test design documentation and guidance

**CREATE COMPREHENSIVE FAILING TEST ARCHITECTURE WITH STRATEGIC INTELLIGENCE.**

## 📋 Intelligent MCP Integration Setup

### TDD Test Creation with MCP Integration

```bash
#!/bin/bash
# TDD Test Creation with Intelligent MCP Integration

# Validate issue number parameter
if [[ -z "$1" ]]; then
    echo "❌ ERROR: Issue number required. Usage: /create-tests-enhanced <issue-number>"
    exit 1
fi

ISSUE_NUMBER="$1"
echo "🚀 TDD Test Creation with Intelligent MCP Integration for Issue #$ISSUE_NUMBER"

# Step 1: Analyzing task complexity and requirements
echo "📊 Analyzing task complexity and requirements..."
echo "🎯 Task Type: Strategic Test Design (Complex test architecture planning)"
echo "🧩 Components: Test Strategy + Domain Testing + Use Case Testing + Business Rule Testing"

# Step 2: Checking MCP availability  
echo "🔧 Checking MCP availability..."

# Check Serena MCP availability
if command -v mcp__serena__get_symbols_overview &> /dev/null; then
    echo "✅ Serena MCP available"
    MCP_SERENA="available"
else
    echo "ℹ️ Serena MCP not found - standard mode"
    MCP_SERENA="unavailable" 
fi

# Check Context7 MCP availability
if command -v mcp__context7__resolve-library-id &> /dev/null; then
    echo "✅ Context7 MCP available"  
    MCP_CONTEXT7="available"
else
    echo "ℹ️ Context7 MCP not found - standard mode"
    MCP_CONTEXT7="unavailable"
fi

# Check Sequential MCP availability
if command -v mcp__sequential-thinking__sequentialthinking &> /dev/null; then
    echo "✅ Sequential MCP available"
    MCP_SEQUENTIAL="available"
else  
    echo "ℹ️ Sequential MCP not found - standard logic mode"
    MCP_SEQUENTIAL="unavailable"
fi

# Step 3: Complex task detected - Using Sequential MCP for systematic analysis
echo "🧩 Complex task detected - Using Sequential MCP for systematic analysis"
echo "📋 Test architecture design requires systematic analysis of 3+ interconnected components:"
echo "  • Test strategy planning across Domain, Application, and Infrastructure layers"
echo "  • Business rule validation test design with comprehensive coverage"
echo "  • Given-When-Then scenario translation to test architecture"
echo "  • TDD RED phase validation and test design quality assurance"

# Graceful Degradation
if [[ "$MCP_SERENA" == "unavailable" ]]; then
    echo "📋 Running without code analysis - manual test discovery required"
fi

if [[ "$MCP_CONTEXT7" == "unavailable" ]]; then
    echo "📚 Running without latest patterns - using standard TDD approaches"
fi

if [[ "$MCP_SEQUENTIAL" == "unavailable" ]]; then
    echo "🧩 Complex task but Sequential MCP unavailable"
    echo "📋 Using structured manual approach with step-by-step test planning"
fi

# Step 4: Specification Analysis
echo "🔍 Locating and analyzing specifications..."

# Find use case specification file
USE_CASE_FILE=$(find docs/use_cases/ -name "*issue*${ISSUE_NUMBER}*" -name "*.md" -type f | head -1)
if [[ ! -f "$USE_CASE_FILE" ]]; then
    USE_CASE_DIR=$(find docs/use_cases/ -name "*issue*${ISSUE_NUMBER}*" -type d | head -1)
    if [[ -d "$USE_CASE_DIR" ]]; then
        USE_CASE_FILE="$USE_CASE_DIR/use-case-specification.md"
    fi
fi

# Find domain model file
DOMAIN_FILE=$(find docs/domain/ -name "*issue*${ISSUE_NUMBER}*" -name "*.md" -type f | head -1)
if [[ ! -f "$DOMAIN_FILE" ]]; then
    DOMAIN_DIR=$(find docs/domain/ -name "*issue*${ISSUE_NUMBER}*" -type d | head -1)
    if [[ -d "$DOMAIN_DIR" ]]; then
        DOMAIN_FILE="$DOMAIN_DIR/domain-model.md"
    fi
fi

if [[ ! -f "$USE_CASE_FILE" ]]; then
    echo "❌ Error: Use case specification for Issue #${ISSUE_NUMBER} not found"
    echo "💡 Please execute /create-use-case-enhanced ${ISSUE_NUMBER} first"
    exit 1
fi

if [[ ! -f "$DOMAIN_FILE" ]]; then
    echo "❌ Error: Domain model for Issue #${ISSUE_NUMBER} not found"
    echo "💡 Please execute /domain-modeling-enhanced ${ISSUE_NUMBER} first"
    exit 1
fi

echo "📄 Found use case specification: $USE_CASE_FILE"
echo "📄 Found domain model: $DOMAIN_FILE"

echo ""
echo "⏰ Ready for systematic test architecture execution..."
```

## 🚀 Expert Execution Flow

### Phase 1: Test Architecture Analysis with Sequential MCP

**Execute systematic test architecture design with Sequential MCP (Instructions to Claude Code in English):**

1. **Complex Test Architecture Design with Sequential MCP**

   ```
   If MCP_SEQUENTIAL is available, use mcp__sequential-thinking__sequentialthinking to systematically analyze:
   "TDD test architecture design: Given-When-Then scenario analysis, domain model testing strategy,
   business rule validation planning, and comprehensive test coverage design for strategic TDD implementation"
   
   Break down the test architecture into logical components:
   - Use case specification analysis for test scenario extraction
   - Domain model analysis for entity, value object, and aggregate testing
   - Business rule identification for validation test design
   - Test layer strategy (unit, integration, acceptance) planning
   - TDD RED phase execution strategy and validation approach
   ```

2. **Supporting Analysis with Serena and Context7 MCP**

   ```
   If MCP_SERENA is available:
   - Use mcp__serena__get_symbols_overview to analyze existing test patterns
   - Use mcp__serena__search_for_pattern to find testing infrastructure
   - Use mcp__serena__find_symbol to locate test utilities and frameworks

   If MCP_CONTEXT7 is available:
   - Use mcp__context7__resolve-library-id for "testing-best-practices"
   - Use mcp__context7__get-library-docs for TDD methodologies and patterns
   - Integrate latest testing frameworks and assertion libraries guidance
   ```

3. **Specification Analysis and Test Scenario Extraction**

   ```
   Use Read tool to analyze the use case and domain specifications:
   - Extract Given-When-Then scenarios for test case design
   - Identify domain entities, value objects, and business rules
   - Analyze acceptance criteria for test assertion planning
   - Document test data requirements and fixture strategies
   - Map business rules to validation test scenarios
   ```

### Phase 2: Test Implementation Strategy with MCP Intelligence

**Execute comprehensive test implementation strategy (Instructions to Claude Code in English):**

1. **Systematic Test Architecture Planning**

   ```
   Continue Sequential MCP analysis focusing on test implementation:
   - Domain layer test design with entity and value object validation
   - Application layer test design with use case orchestration testing
   - Infrastructure layer test planning with repository and external service mocking
   - Test data strategy with fixtures, factories, and test utilities
   - Test isolation strategy with proper dependency injection and mocking
   ```

2. **Business Rule Validation Test Design**

   ```
   Design comprehensive business rule testing strategy:
   - Entity invariant validation tests for business constraints
   - Value object validation tests for domain rules and immutability
   - Aggregate consistency tests for transaction boundary validation
   - Domain service tests for complex business logic orchestration
   - Cross-aggregate business rule tests for domain integrity
   ```

3. **Context7 Integration for Testing Excellence**

   ```
   If MCP_CONTEXT7 is available:
   - Apply industry-standard TDD patterns and methodologies
   - Integrate latest testing frameworks and assertion strategies
   - Use proven test organization and naming conventions
   - Apply testing best practices for maintainable test architecture
   ```

### Phase 3: Test Implementation and Documentation

**Execute comprehensive test implementation with MCP learning integration (Instructions to Claude Code in English):**

1. **Create test architecture and implementation**

   ```
   Generate comprehensive failing test suite:
   Create directory structure: tests/unit/, tests/integration/, tests/fixtures/
   
   Write failing tests following TDD RED phase discipline:
   - Domain entity tests with business behavior validation
   - Value object tests with validation and immutability testing
   - Use case tests with Given-When-Then scenario coverage
   - Repository interface tests with contract validation
   - Business rule validation tests with comprehensive edge cases
   ```

2. **Create test documentation and guidance**

   ```
   Generate comprehensive test documentation:
   Write "tests/issue-${ISSUE_NUMBER}-test-architecture.md" including:
   - Test strategy and architecture overview
   - Test layer organization and responsibilities
   - Business rule coverage mapping and validation strategy
   - Test execution guidance and TDD workflow documentation
   - Test maintenance and evolution planning
   ```

3. **Create MCP-enhanced documentation (if available)**

   ```
   If Sequential MCP, Serena, or Context7 MCPs were used, create additional documentation:
   Write "tests/issue-${ISSUE_NUMBER}-mcp-test-analysis.md" including:
   - Sequential MCP test architecture analysis results
   - Serena-discovered testing patterns and infrastructure analysis
   - Context7 testing best practice integration recommendations
   - Test quality insights and improvement opportunities
   ```

4. **MCP learning and memory storage**

   ```
   If MCP_SERENA is available, store learning insights:
   Use mcp__serena__write_memory to record:
   - Test architecture insights for "test-design-patterns-$(date +%Y%m%d)"
   - Business rule testing strategies for "domain-test-validation-$(date +%Y%m%d)"
   - TDD implementation learnings for "tdd-red-phase-execution-$(date +%Y%m%d)"
   ```

5. **Git commit test architecture**

   ```
   Bash git add tests/
   Bash git commit -m "test: create failing test architecture for issue ${ISSUE_NUMBER} (TDD RED phase)

   Comprehensive test suite with domain, application, and infrastructure testing.
   Business rule validation and Given-When-Then scenario coverage.

   🔴 TDD RED PHASE: All tests failing as expected
   🎯 Generated with Claude Code
   "
   ```

## ✅ Built-in Quality Assurance

### Self-Diagnosis Checklist

**Test Architecture Design Completion (MUST):**

- [ ] Use case and domain specifications analyzed for test scenario extraction
- [ ] Comprehensive failing test suite created following TDD RED phase discipline
- [ ] Domain entities, value objects, and use cases properly tested
- [ ] Business rule validation tests cover all identified domain constraints
- [ ] Test architecture documentation created with implementation guidance
- [ ] All tests fail as expected to validate proper TDD RED phase execution

**MCP Integration Quality (if available):**

- [ ] Sequential MCP systematic test architecture analysis completed (if available)
- [ ] Serena MCP testing pattern analysis utilized (if available)
- [ ] Context7 testing best practices integrated (if available)
- [ ] MCP learning insights stored for future reference (if available)

**Test Quality and Standards (MUST):**

- [ ] Test isolation and independence properly implemented
- [ ] Given-When-Then scenarios translated to test cases with clear assertions
- [ ] Test data strategy and fixture design documented
- [ ] All documentation committed to version control

**TDD Discipline Validation (SHOULD):**

- [ ] Tests created before any production code implementation
- [ ] Test failure messages are clear and descriptive
- [ ] Test architecture supports future GREEN and REFACTOR phases
- [ ] Business behavior focus maintained over technical implementation details

### Quality Assessment

| Quality Area | Assessment Criteria | Status |
|--------------|-------------------|--------|
| **Test Architecture** | Comprehensive test design aligned with domain model | ✅/❌ |
| **TDD Discipline** | All tests fail appropriately in RED phase | ✅/❌ |
| **Business Coverage** | Complete coverage of business rules and scenarios | ✅/❌ |
| **Test Quality** | Clear, maintainable, and well-organized tests | ✅/❌ |
| **MCP Integration** | Available MCPs effectively utilized for enhancement | ✅/❌/N/A |

## 📊 Standardized Output Format

### 実行サマリー (日本語でユーザーに報告)

**基本テスト設計完了:**

- ✅ **仕様分析**: ユースケース・ドメインモデルからテストシナリオ抽出完了
- ✅ **テストアーキテクチャ設計**: Clean Architecture層に対応した包括的テスト設計完了
- ✅ **TDD REDフェーズ実行**: すべての失敗テストが期待通り作成・検証完了
- ✅ **ビジネスルール検証**: ドメイン制約・不変条件の網羅的テストカバレッジ完了

**MCP 拡張テスト設計 (利用可能時):**

- ✅ **Sequential MCP分析**: テストアーキテクチャの体系的設計と戦略立案完了
- ✅ **Serena パターン分析**: 既存テストパターンとインフラストラクチャ分析完了
- ✅ **Context7 統合**: 最新TDD手法とテスト設計ベストプラクティス適用完了
- ✅ **学習記録**: テスト設計の知見とパターンをライブラリに蓄積完了

### 成果物

**必須ドキュメント:**

- `tests/unit/`, `tests/integration/`, `tests/fixtures/`: 包括的失敗テストスイート
- `tests/issue-${ISSUE_NUMBER}-test-architecture.md`: テストアーキテクチャ設計書
- エンティティ、値オブジェクト、ユースケーステストの完全カバレッジ

**MCP 拡張ドキュメント (利用可能時):**

- `tests/issue-${ISSUE_NUMBER}-mcp-test-analysis.md`: MCPテスト分析とインサイト
- Serena MCPメモリファイル: テスト設計学習結果の永続化

### 総合判定

**テスト準備状況**: `READY` / `CONDITIONAL` / `ARCHITECTURE_REVISION_REQUIRED`
**主要成果**: [作成されたテスト数とビジネスルールカバレッジの要約]  
**推奨次ステップ**: [TDD GREENフェーズまたはテストレビューへの移行判定]

### 次のステップ (日本語でユーザーに案内)

1. **テスト承認時**: `/implement-domain ${ISSUE_NUMBER}` でTDD GREENフェーズ（実装）開始
2. **テスト品質確認時**: `/test-review-enhanced ${ISSUE_NUMBER}` でテスト品質評価
3. **確認推奨**: 全テストが期待通り失敗していることのTDD RED検証

**ユーザーへのメッセージ (日本語)**:

```
🎉 TDDテストアーキテクチャ設計完了！

📊 TDDテスト設計結果:
   ✅ 設計状況: [READY/CONDITIONAL/ARCHITECTURE_REVISION_REQUIRED]
   🧪 テスト設計: [エンティティ・値オブジェクト・ユースケーステストの要約]
   📋 ビジネスルール: [検証テスト数とカバレッジ状況]
   🔴 RED検証: すべてのテストが期待通り失敗中

💡 テスト設計分析結果:
   🎯 強み: [テストアーキテクチャの優位性]
   ⚡ 注意点: [実装時の重要な留意事項]
   🔄 カバレッジ: [ビジネスルール検証の完全性]

🧠 MCP拡張テスト設計 (利用時):
   📊 Sequential分析: テストアーキテクチャの体系的設計完了
   🔍 Serena インサイト: テストパターンとインフラ分析
   🌐 Context7 統合: 最新TDD手法を設計に適用

📁 生成テストスイート:
   ✅ tests/unit/domain/: ドメインレイヤーテスト
   ✅ tests/unit/application/: アプリケーションレイヤーテスト
   ✅ tests/integration/: 統合テストスイート
   ✅ tests/issue-${ISSUE_NUMBER}-test-architecture.md

🚀 次のアクション:
   📋 `/implement-domain ${ISSUE_NUMBER}` でTDD GREENフェーズ開始

✅ TDDテストアーキテクチャ設計完了 - 実装準備完了！
```

## Common Errors and Solutions

### ❌ Error Case 1: Use case or domain specification not found
**Cause**: Missing prerequisite documentation  
**Solution**: 
- Verify use case specification exists: `find docs/use_cases/ -name "*issue*${ISSUE_NUMBER}*"`
- Run `/create-use-case-enhanced ${ISSUE_NUMBER}` and `/domain-modeling-enhanced ${ISSUE_NUMBER}` first
- Check issue number parameter accuracy

### ❌ Error Case 2: Test architecture design conflicts
**Cause**: Complex test design decisions requiring domain expertise  
**Solution**: 
- Use Sequential MCP for systematic test architecture analysis
- Focus on business behavior over technical implementation
- Align test design with domain model boundaries

### ❌ Error Case 3: TDD discipline violations
**Cause**: Temptation to implement production code during RED phase  
**Solution**: 
```bash
# Strict TDD RED phase validation
# Ensure all tests fail before any implementation
# Focus on test design and business behavior specification
```

## Execution Examples

### ✅ Success Example - Full Test Architecture with Sequential MCP
```bash
$ /create-tests-enhanced 456

🚀 TDD Test Creation with Intelligent MCP Integration for Issue #456

📊 テストアーキテクチャ分析:
  🎯 ユースケース: "Order management with inventory validation"
  📋 複雑性: 戦略・設計タスク（Sequential MCP使用）
  🧩 テスト設計コンポーネント: Entity + Value Object + Use Case + Business Rules

🧩 Sequential MCP分析結果:
  📊 体系的分析: テストアーキテクチャの戦略的設計完了
  🔍 Serena発見: 既存テストパターンとインフラ分析
  🌐 Context7統合: 最新TDD手法とテスト設計パターン適用

✅ TDDテストアーキテクチャ設計完了:
  🧪 エンティティテスト: Order, Customer, InventoryItem テスト
  💎 値オブジェクトテスト: OrderId, Money, Quantity バリデーション
  📋 ユースケーステスト: Given-When-Thenシナリオ完全カバレッジ
  ✅ ビジネスルールテスト: 在庫検証、注文制約、支払い検証

🔴 TDD RED検証: 全48テストが期待通り失敗中

📁 成果物:
  ✅ tests/unit/domain/: ドメインテストスイート
  ✅ tests/integration/: 統合テスト
  ✅ tests/issue-456-test-architecture.md

🚀 次のステップ: `/implement-domain 456` でGREENフェーズ開始
```