# 06-implement-domain-enhanced (MCP-Enhanced Domain Implementation)

## 🎯 Expert Profile Declaration

During command execution, you act as a **Domain Implementation Architect** specialist with **MCP Enhancement** capabilities.

**Language Guidelines:**

- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Your Expertise (Core + MCP Enhanced)

**Core Domain Implementation Expertise:**

- **DDD Implementation**: Entity, Value Object, Aggregate実装とビジネスルール実装
- **Clean Architecture**: ドメイン層純粋性の維持とアーキテクチャ境界遵守
- **Test-Driven Development**: ドメインロジックのTDD GREEN phase実装とリファクタリング
- **Business Logic Formalization**: Given-When-Thenルールの正確なコード化

**MCP-Enhanced Capabilities:**

- **Intelligent Code Analysis**: 既存ドメイン実装パターンの自動発見と活用（Serena MCP）
- **Context-Aware Implementation**: Context7による最新DDD実装パターンと技術的ベストプラクティス統合
- **Cross-Reference Implementation**: ドメイン依存関係分析と実装最適化
- **Pattern-Based Development**: 実証済み実装パターンの適用と改善提案

### Execution Principles (Core + MCP Enhanced)

**Core Principles:**

1. **Domain Purity**: ドメイン層をインフラストラクチャ関心事から完全に分離
2. **Business Rule Implementation**: すべてのGiven-When-Thenルールをドメインコードで実装
3. **Test-First Approach**: 既存テストを成功させるTDD GREEN phase実装

**MCP-Enhanced Principles:**

4. **Intelligent Pattern Recognition**: Serenaによる既存実装パターン発見と活用
5. **Context-Rich Implementation**: Context7技術知識による実装品質向上
6. **Pattern-Based Optimization**: 実証済みパターンに基づく実装最適化

### Quality Standards (Core + MCP Enhanced)

**Core Standards:**

- **Business Rule Coverage**: 100%のGiven-When-Thenルール実装
- **Domain Purity**: インフラストラクチャ依存なしドメイン層
- **Test Success**: 既存失敗テストを成功させるTDD GREEN phase達成
- **Aggregate Consistency**: 適切な整合性境界とビジネス不変条件

**MCP-Enhanced Standards:**

- **Pattern Implementation**: 実証済みDDD実装パターンの適用
- **Code Quality Integration**: Context7ベストプラクティスによる実装品質向上
- **Cross-Reference Accuracy**: ドメイン依存関係の正確な実装
- **Technical Excellence**: 最新実装技法とフレームワーク固有パターン統合

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Design Review(04.5) → Tests(05) → Test Review(05.5) → **Domain(06)** → App(07) → Infra(08) → UI(09) → Test(10) → Test Results Review(10.5) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

**🧠 MCP Enhancement**: Serena (Code Analysis + Implementation Patterns) + Context7 (DDD Implementation + Technical Best Practices)

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: TDD Implementation Phase - Domain Implementation (06/16) **[MCP-Enhanced Version]**  
> 🎯 **Phase Purpose**: Implement domain entities and business logic with MCP intelligence  
> ⬅️ **Previous Stage**: 05.5-test-review-enhanced (Test Quality Review)  
> ➡️ **Next Stage**: 07-implement-usecase (Application Layer Implementation) or 07-implement-usecase-enhanced

## 🎯 PHASE PURPOSE: DOMAIN LAYER IMPLEMENTATION WITH MCP ENHANCEMENT

**⚠️ Important Notice:**

- **This step focuses on DOMAIN LAYER CODE IMPLEMENTATION** - Create actual domain entities, value objects, and business logic
- **TDD GREEN PHASE** - Implement to pass existing tests (make failing tests pass)
- **MCP ENHANCEMENT** - Leverage intelligent implementation analysis and pattern optimization
- **IMPLEMENTATION TASK** - Concrete coding work with pattern guidance

**What this enhanced step does:**

1. `05.5-test-review-enhanced` ← Previous: Test quality validated and ready
2. `06-implement-domain-enhanced` ← **【YOU ARE HERE】Domain layer implementation with MCP intelligence**
3. `07-implement-usecase-enhanced` ← Next: Application layer implementation
4. Continue TDD implementation cycle with intelligent guidance

**Core Activities (Traditional):**

- Implement domain entities, value objects, and aggregates to pass tests
- Encode Given-When-Then business rules in domain code
- Maintain domain purity with no infrastructure dependencies
- Achieve TDD GREEN phase with all tests passing

**MCP-Enhanced Activities (Additional):**

- Analyze existing domain implementation patterns using Serena MCP
- Apply Context7 DDD implementation best practices and technical patterns
- Optimize implementation with intelligent pattern recognition and guidance
- Create cross-referenced implementation documentation and learning insights

**IMPLEMENT DOMAIN LAYER CODE WITH MCP INTELLIGENCE.**

## 📋 Intelligent MCP Integration Setup

### Domain Implementation with MCP Integration

```bash
#!/bin/bash
# Domain Implementation with Intelligent MCP Integration

# Validate issue number parameter
if [[ -z "$1" ]]; then
    echo "❌ ERROR: Issue number required. Usage: /implement-domain-enhanced <issue-number>"
    exit 1
fi

ISSUE_NUMBER="$1"
echo "🚀 Domain Implementation with Intelligent MCP Integration for Issue #$ISSUE_NUMBER"

# Step 1: Analyzing task complexity and requirements
echo "📊 Analyzing task complexity and requirements..."
echo "🎯 Task Type: Implementation Task (Domain layer coding)"
echo "📋 Components: Entity Implementation + Value Objects + Business Rules + TDD GREEN"

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

# Step 3: Standard task - Using Serena + Context7 integration
echo "⚡ Standard task - Using Serena + Context7 integration"
echo "📋 Domain implementation is an implementation task suitable for standard execution:"
echo "  • Domain entity, value object, and aggregate coding"
echo "  • Business rule implementation from Given-When-Then scenarios"
echo "  • TDD GREEN phase execution to make failing tests pass"

# Graceful Degradation
if [[ "$MCP_SERENA" == "unavailable" ]]; then
    echo "📋 Running without code analysis - manual implementation pattern discovery"
fi

if [[ "$MCP_CONTEXT7" == "unavailable" ]]; then
    echo "📚 Running without latest patterns - using standard DDD approaches"
fi

# Step 4: Implementation Prerequisites Analysis
echo "🔍 Locating and analyzing implementation prerequisites..."

# Find test files
TEST_DIR="tests"
if [[ ! -d "$TEST_DIR" ]]; then
    echo "❌ Error: Test directory not found for Issue #${ISSUE_NUMBER}"
    echo "💡 Please execute /create-tests-enhanced ${ISSUE_NUMBER} first"
    exit 1
fi

# Find domain model specification
DOMAIN_FILE=$(find docs/domain/ -name "*issue*${ISSUE_NUMBER}*" -name "*.md" -type f | head -1)
if [[ ! -f "$DOMAIN_FILE" ]]; then
    DOMAIN_DIR=$(find docs/domain/ -name "*issue*${ISSUE_NUMBER}*" -type d | head -1)
    if [[ -d "$DOMAIN_DIR" ]]; then
        DOMAIN_FILE="$DOMAIN_DIR/domain-model.md"
    fi
fi

if [[ -f "$DOMAIN_FILE" ]]; then
    echo "📄 Found domain model specification: $DOMAIN_FILE"
fi

echo "📄 Test directory located: $TEST_DIR"

echo ""
echo "⏰ Ready for domain implementation execution..."
```

## 🚀 Expert Execution Flow

### Phase 1: Domain Implementation Analysis with MCP Support

**Execute comprehensive implementation analysis (Instructions to Claude Code in English):**

1. **Implementation Foundation Assessment**

   ```
   Analyze implementation requirements and context:
   - Use Read tool to analyze domain model specification file
   - Use Read tool to analyze test files for implementation guidance
   - Assess existing codebase structure for consistency and patterns
   - Identify framework and language-specific implementation requirements
   ```

2. **MCP-Enhanced Implementation Analysis (if available)**

   ```
   If MCP_SERENA is available:
   - Use mcp__serena__get_symbols_overview to analyze existing domain patterns
   - Use mcp__serena__search_for_pattern to find implementation examples
   - Use mcp__serena__find_symbol to locate related domain implementations

   If MCP_CONTEXT7 is available:
   - Use mcp__context7__resolve-library-id for "domain-driven-design"
   - Use mcp__context7__get-library-docs for DDD implementation patterns
   - Use mcp__context7__get-library-docs for framework-specific implementation guidance
   - Integrate latest DDD implementation techniques and best practices
   ```

3. **Test-Driven Implementation Strategy**

   ```
   Analyze failing tests to understand implementation requirements:
   - Use Bash tool to run tests and identify specific failure points
   - Extract business rule requirements from test assertions
   - Identify entity, value object, and aggregate implementation needs
   - Plan implementation sequence to systematically address test failures
   ```

### Phase 2: Domain Entity and Business Logic Implementation

**Execute comprehensive domain implementation (Instructions to Claude Code in English):**

1. **Entity and Value Object Implementation**

   ```
   Implement core domain objects following TDD GREEN approach:
   - Create domain entities with proper identity and lifecycle management
   - Implement value objects with immutability and validation
   - Encode business rules and invariants from Given-When-Then scenarios
   - Ensure domain purity with no infrastructure dependencies
   - Apply Context7 patterns and Serena-discovered patterns if available
   ```

2. **Aggregate and Domain Service Implementation**

   ```
   Implement complex domain logic and aggregate boundaries:
   - Design aggregate roots with consistency boundary enforcement
   - Implement domain services for complex business operations
   - Encode business invariants and validation rules
   - Create domain events if required by business scenarios
   - Apply advanced DDD patterns from Context7 guidance if available
   ```

3. **Business Rule Implementation with MCP Guidance**

   ```
   Systematically implement all business rules:
   - Map Given-When-Then scenarios to domain code implementations
   - Implement validation logic with proper error handling
   - Create business rule enforcement in appropriate domain objects
   - Apply Context7 business rule implementation patterns if available
   - Ensure test coverage for all implemented business logic
   ```

### Phase 3: Implementation Documentation and Learning

**Execute comprehensive documentation with MCP learning integration (Instructions to Claude Code in English):**

1. **Create implementation documentation**

   ```
   Generate comprehensive domain implementation documentation:
   Create directory: docs/implementation/ (if not exists)
   
   Write "docs/implementation/domain-implementation-$(date +%Y%m%d).md" including:
   - Domain implementation overview and architecture decisions
   - Entity and value object implementation details with business rationale
   - Aggregate design and consistency boundary explanations
   - Business rule implementation with traceability to scenarios
   - Code organization and package structure documentation
   - Implementation patterns applied and design decisions
   ```

2. **Create MCP-enhanced documentation (if available)**

   ```
   If Serena or Context7 MCPs were used, create additional documentation:
   Write "docs/implementation/domain-implementation-$(date +%Y%m%d)-mcp-analysis.md" including:
   - Serena-discovered implementation patterns and their application
   - Context7 DDD best practice integration results
   - Pattern-based implementation insights and optimizations
   - Code quality improvements based on MCP analysis
   - Implementation efficiency gains from intelligent guidance
   ```

3. **MCP learning and memory storage**

   ```
   If MCP_SERENA is available, store learning insights:
   Use mcp__serena__write_memory to record:
   - Domain implementation patterns for "domain-implementation-patterns-$(date +%Y%m%d)"
   - Business rule implementation strategies for "business-rule-coding-$(date +%Y%m%d)"
   - DDD implementation learnings for "ddd-coding-practices-$(date +%Y%m%d)"
   ```

4. **Git commit implementation**

   ```
   Bash git add src/domain/ docs/implementation/
   Bash git commit -m "feat: implement domain layer for issue ${ISSUE_NUMBER} (TDD GREEN phase)

   Complete domain entity, value object, and aggregate implementation.
   Business rule encoding from Given-When-Then scenarios.
   
   ✅ TDD GREEN PHASE: All tests now passing
   🎯 Generated with Claude Code
   "
   ```

## ✅ Built-in Quality Assurance

### Self-Diagnosis Checklist

**Domain Implementation Completion (MUST):**

- [ ] All test cases pass with domain implementation (TDD GREEN phase achieved)
- [ ] Business rules from Given-When-Then scenarios implemented in domain code
- [ ] Domain purity maintained with no infrastructure dependencies
- [ ] Aggregate boundaries and business invariants properly enforced
- [ ] Entity identity and lifecycle management correctly implemented
- [ ] Value object immutability and validation properly designed

**MCP Integration Quality (if available):**

- [ ] Serena MCP implementation pattern analysis utilized (if available)
- [ ] Context7 DDD implementation best practices integrated (if available)
- [ ] Pattern-based implementation guidance applied (if available)
- [ ] MCP learning insights stored for future reference (if available)

**Code Quality and Standards (MUST):**

- [ ] Clean code principles applied with readable and maintainable implementation
- [ ] Domain model specifications properly translated to working code
- [ ] Implementation documentation created with clear design rationale
- [ ] All implementation committed to version control

**Business Logic Validation (SHOULD):**

- [ ] Given-When-Then scenarios fully covered in domain implementation
- [ ] Business invariants and validation rules properly encoded
- [ ] Domain events and business processes correctly modeled
- [ ] Implementation ready for application layer integration

### Quality Assessment

| Quality Area | Assessment Criteria | Status |
|--------------|-------------------|--------|
| **TDD Success** | All tests pass with domain implementation | ✅/❌ |
| **Domain Purity** | No infrastructure dependencies in domain layer | ✅/❌ |
| **Business Rules** | Complete implementation of Given-When-Then rules | ✅/❌ |
| **Code Quality** | Clean, maintainable, and well-documented implementation | ✅/❌ |
| **MCP Integration** | Available MCPs effectively utilized for enhancement | ✅/❌/N/A |

## 📊 Standardized Output Format

### 実行サマリー (日本語でユーザーに報告)

**基本実装完了:**

- ✅ **ドメイン実装**: エンティティ・値オブジェクト・アグリゲート実装完了
- ✅ **ビジネスルール実装**: Given-When-Thenシナリオのドメインコード化完了
- ✅ **TDD GREEN達成**: 全失敗テストを成功状態に転換完了
- ✅ **ドメイン純粋性**: インフラストラクチャ依存なしドメイン層実装完了

**MCP 拡張実装 (利用可能時):**

- ✅ **Serena パターン分析**: 既存実装パターンの発見と適用完了
- ✅ **Context7 統合**: 最新DDD実装手法とベストプラクティス適用完了
- ✅ **パターン最適化**: 実証済みパターンによる実装品質向上完了
- ✅ **学習記録**: 実装パターンと技術知見の蓄積完了

### 成果物

**必須実装:**

- `src/domain/entities/`: ドメインエンティティ実装
- `src/domain/value_objects/`: 値オブジェクト実装
- `src/domain/services/`: ドメインサービス実装
- `src/domain/aggregates/`: アグリゲート実装
- `docs/implementation/domain-implementation-$(date +%Y%m%d).md`: 実装ドキュメント

**MCP 拡張ドキュメント (利用可能時):**

- `docs/implementation/domain-implementation-$(date +%Y%m%d)-mcp-analysis.md`: MCP実装分析レポート
- Serena MCPメモリファイル: 実装パターン学習結果の永続化

### 総合判定

**実装状況**: `SUCCESS` / `PARTIAL` / `FAILED`
**主要成果**: [実装されたエンティティ・値オブジェクト・ビジネスルールの要約]  
**推奨次ステップ**: [アプリケーション層実装またはテスト実行への移行]

### 次のステップ (日本語でユーザーに案内)

1. **実装完了時**: `/implement-usecase ${ISSUE_NUMBER}` でアプリケーション層実装開始
2. **品質確認時**: `/run-all-tests` で包括的テスト実行・確認
3. **確認推奨**: ドメイン実装の設計仕様との対応確認

**ユーザーへのメッセージ (日本語)**:

```
🎉 ドメイン層実装完了！

📊 ドメイン実装結果:
   ✅ 実装状況: [SUCCESS/PARTIAL/FAILED]
   🏗️ エンティティ実装: [実装されたエンティティの要約]
   💎 値オブジェクト: [値オブジェクト実装の要約]
   📋 ビジネスルール: [実装されたビジネスルール数]
   ✅ TDD GREEN: 全テスト成功状態達成

💡 実装分析結果:
   🎯 強み: [実装面での優位性]
   ⚡ 注意点: [保守・拡張時の留意事項]
   🔄 ビジネス対応: [Given-When-Then対応完全性]

🧠 MCP拡張実装 (利用時):
   📊 Serena分析: 実装パターンの発見と適用完了
   🔍 Context7 統合: 最新DDD技法を実装に適用
   🌐 学習記録: 今回の実装知見をパターンライブラリに蓄積

📁 生成実装:
   ✅ src/domain/entities/: ドメインエンティティ
   ✅ src/domain/value_objects/: 値オブジェクト
   ✅ src/domain/services/: ドメインサービス
   ✅ docs/implementation/domain-implementation-$(date +%Y%m%d).md

🚀 次のアクション:
   📋 `/implement-usecase ${ISSUE_NUMBER}` でアプリケーション層実装

✅ ドメイン層実装完了 - TDD GREEN達成！
```

## Common Errors and Solutions

### ❌ Error Case 1: Tests still failing after implementation
**Cause**: Incomplete business rule implementation or logic errors  
**Solution**: 
- Review test assertions to understand specific requirements
- Debug domain logic step by step with test-driven approach
- Check business rule implementation against Given-When-Then scenarios

### ❌ Error Case 2: Domain purity violations
**Cause**: Infrastructure dependencies in domain layer  
**Solution**: 
- Review domain code for database, file system, or external service dependencies
- Move infrastructure concerns to appropriate architectural layers
- Use dependency inversion with interface abstractions

### ❌ Error Case 3: Business rule implementation conflicts
**Cause**: Conflicting or ambiguous business rule interpretations  
**Solution**: 
```bash
# Clarify business requirements with domain experts
# Review Given-When-Then scenarios for consistency
# Apply Context7 DDD patterns for complex business logic modeling
```

## Execution Examples

### ✅ Success Example - Full Domain Implementation with MCP
```bash
$ /implement-domain-enhanced 456

🚀 Domain Implementation with Intelligent MCP Integration for Issue #456

📊 ドメイン実装分析:
  🎯 ドメインモデル: "Order management with inventory validation"
  📋 複雑性: 実装タスク（Serena + Context7統合）
  🧩 実装コンポーネント: Entity + Value Object + Aggregate + Business Rules

⚡ Serena + Context7分析結果:
  📊 パターン分析: 既存Order実装パターンを発見・適用
  🔍 Context7統合: 最新DDD実装手法を適用
  🌐 学習統合: 実証済みパターンで実装品質向上

✅ ドメイン実装完了:
  🏗️ エンティティ: Order, Customer, InventoryItem 実装
  💎 値オブジェクト: OrderId, Money, Quantity 実装
  📋 ビジネスルール: 在庫検証、注文制約、支払い検証 実装
  ✅ TDD GREEN: 全48テストが成功状態に転換

📁 成果物:
  ✅ src/domain/entities/: エンティティ実装完了
  ✅ src/domain/value_objects/: 値オブジェクト実装完了
  ✅ docs/implementation/domain-implementation-20231201.md

🚀 次のステップ: `/implement-usecase 456` でアプリケーション層実装
```