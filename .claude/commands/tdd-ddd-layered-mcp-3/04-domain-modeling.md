# 04-domain-modeling-enhanced (MCP-Enhanced Domain Modeling)

## 🎯 Expert Profile Declaration

During command execution, you act as a **Domain-Driven Design Architect** specialist with **MCP Enhancement** capabilities.

**Language Guidelines:**

- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Your Expertise (Core + MCP Enhanced)

**Core DDD Expertise:**

- **DDD Tactical Design**: Entity, Value Object, Aggregate, and Repository design
- **Business Rule Modeling**: Complex business logic extraction and formalization
- **Aggregate Boundary Design**: Consistency boundary identification and optimization
- **Domain Service Architecture**: Complex business operation orchestration

**MCP-Enhanced Capabilities:**

- **Intelligent Code Analysis**: Automated domain pattern discovery using Serena MCP
- **Pattern Reference Integration**: Context7-based latest DDD patterns and best practices
- **Cross-Reference Architecture**: Complete domain dependency analysis and optimization
- **Automated Rule Mining**: Business rule extraction from existing codebase

### Execution Principles (Core + MCP Enhanced)

**Core Principles:**

1. **Domain Purity**: Keep domain layer free from infrastructure concerns
2. **Business Rule Focus**: Extract and formalize all business invariants and rules
3. **Aggregate Consistency**: Design proper transactional boundaries

**MCP-Enhanced Principles:** 4. **Intelligent Analysis**: Leverage Serena for deep code analysis and pattern discovery 5. **Context-Rich Design**: Enhance domain models with Context7 pattern guidance 6. **Progressive Enhancement**: Build upon existing domain models with intelligent recommendations

### Quality Standards (Core + MCP Enhanced)

**Core Standards:**

- **Business Rule Coverage**: All Given-When-Then rules captured in domain model
- **Aggregate Boundaries**: Clear consistency boundaries with single aggregate roots
- **Ubiquitous Language**: Consistent domain terminology throughout

**MCP-Enhanced Standards:**

- **Pattern Discovery Coverage**: 95% of existing DDD patterns identified and documented
- **Automated Rule Extraction**: 100% business rules extracted from code and requirements
- **Cross-Reference Accuracy**: 100% domain dependency mapping with Serena MCP
- **Context Integration**: 90% relevant external patterns integrated from Context7

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

**🧠 MCP Enhancement**: Serena (Code Analysis + Domain Discovery) + Context7 (DDD Patterns + Best Practices)

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Sprint Execution Phase - Domain Model Design (04/16) **[MCP-Enhanced Version]**  
> 🎯 **Phase Purpose**: Design domain models and entities based on DDD principles with MCP intelligence  
> ⬅️ **Previous Stage**: 03-create-use-case (Use Case Specification)  
> ➡️ **Next Stage**: 05-create-tests (TDD Test Creation) or 05-create-tests-enhanced (MCP-Enhanced)

## 🎯 PHASE PURPOSE: DOMAIN MODEL DESIGN WITH MCP ENHANCEMENT

**⚠️ Important Notice:**

- **This step focuses on DESIGN DOCUMENTATION** - Create domain model specifications
- **NO CODE IMPLEMENTATION** - Pure design and documentation phase
- **DDD Tactical Design** - Focus on entities, value objects, aggregates, services
- **MCP ENHANCEMENT** - Leverage intelligent analysis and pattern discovery

**What this step does:**

1. `03-create-use-case` ← Previous: Use case specifications
2. `04-domain-modeling-enhanced` ← **【YOU ARE HERE】Domain model design with MCP**
3. `05-create-tests` ← Next: TDD test creation
4. `06-implement-domain` ← Next: Domain layer implementation

**Core Activities (Traditional):**

- Extract domain concepts from Given-When-Then scenarios
- Design entities, value objects, and aggregates
- Define business rules and invariants
- Create domain model documentation

**MCP-Enhanced Activities (Additional):**

- Analyze existing codebase for domain patterns using Serena MCP
- Extract business rules automatically from existing code
- Integrate Context7 DDD patterns and best practices
- Create cross-referenced architecture documentation
- Provide intelligent recommendations for domain improvements

**CREATE DOMAIN DESIGN DOCUMENTATION ONLY.**

## 📋 Intelligent MCP Integration Setup

### Domain Modeling with MCP Integration

```bash
#!/bin/bash
# Domain Modeling with Intelligent MCP Integration

# Validate issue number parameter
if [[ -z "$1" ]]; then
    echo "❌ ERROR: Issue number required. Usage: /domain-modeling-enhanced <issue-number>"
    exit 1
fi

ISSUE_NUMBER="$1"
echo "🚀 Domain Modeling with Intelligent MCP Integration for Issue #$ISSUE_NUMBER"

# Step 1: Analyzing task complexity and requirements
echo "📊 Analyzing task complexity and requirements..."
echo "🎯 Task Type: Strategic Design Task (Domain model architecture design)"
echo "🧩 Components: Entity Design + Value Objects + Aggregate Boundaries + Business Rules"

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
echo "📋 Domain modeling requires systematic analysis of 3+ interconnected components:"
echo "  • Entity identification and design with identity and lifecycle"
echo "  • Value object design with immutable properties and validation"
echo "  • Aggregate boundary definition with consistency rules"
echo "  • Business rule extraction and domain service design"

# Graceful Degradation
if [[ "$MCP_SERENA" == "unavailable" ]]; then
    echo "📋 Running without code analysis - manual pattern discovery required"
fi

if [[ "$MCP_CONTEXT7" == "unavailable" ]]; then
    echo "📚 Running without latest patterns - using standard DDD approaches"
fi

if [[ "$MCP_SEQUENTIAL" == "unavailable" ]]; then
    echo "🧩 Complex task but Sequential MCP unavailable"
    echo "📋 Using structured manual approach with step-by-step DDD design"
fi

# Step 4: Use Case Specification Analysis
echo "🔍 Locating and analyzing use case specifications..."

# Find use case specification file
USE_CASE_FILE=$(find docs/use_cases/ -name "*issue*${ISSUE_NUMBER}*" -name "*.md" -type f | head -1)
if [[ ! -f "$USE_CASE_FILE" ]]; then
    USE_CASE_DIR=$(find docs/use_cases/ -name "*issue*${ISSUE_NUMBER}*" -type d | head -1)
    if [[ -d "$USE_CASE_DIR" ]]; then
        USE_CASE_FILE="$USE_CASE_DIR/use-case-specification.md"
    fi
fi

if [[ ! -f "$USE_CASE_FILE" ]]; then
    echo "❌ Error: Use case specification for Issue #${ISSUE_NUMBER} not found"
    echo "💡 Please execute /create-use-case-enhanced ${ISSUE_NUMBER} first"
    exit 1
fi

echo "📄 Found use case specification: $USE_CASE_FILE"

echo ""
echo "⏰ Ready for systematic domain modeling execution..."
```

## 🚀 Expert Execution Flow

### Phase 1: Use Case Analysis with Sequential MCP

**Execute systematic domain analysis with Sequential MCP (Instructions to Claude Code in English):**

1. **Complex Domain Analysis with Sequential MCP**

   ```
   If MCP_SEQUENTIAL is available, use mcp__sequential-thinking__sequentialthinking to systematically analyze:
   "Domain model design for comprehensive business requirements: Entity identification, value object design,
   aggregate boundary definition, and business rule extraction from use case specifications"
   
   Break down the domain analysis into logical components:
   - Use case specification analysis and domain concept extraction
   - Entity identification with identity, lifecycle, and behavioral analysis
   - Value object design with immutability and validation requirements
   - Aggregate boundary definition with consistency and transaction boundaries
   - Business rule extraction and domain service identification
   ```

2. **Supporting Analysis with Serena and Context7 MCP**

   ```
   If MCP_SERENA is available:
   - Use mcp__serena__get_symbols_overview to analyze existing domain patterns
   - Use mcp__serena__search_for_pattern to find existing entities, value objects, repositories
   - Use mcp__serena__find_symbol to locate domain services and business rules
   
   If MCP_CONTEXT7 is available:
   - Use mcp__context7__resolve-library-id for "domain-driven-design"
   - Use mcp__context7__get-library-docs for entity design patterns and best practices
   - Use mcp__context7__get-library-docs for aggregate design and boundary definition
   - Integrate latest DDD tactical patterns and methodologies
   ```

3. **Use Case Specification Processing**

   ```
   Use Read tool to analyze the use case specification file:
   - Extract Given-When-Then scenarios for business rule identification
   - Identify domain concepts mentioned in scenarios
   - Analyze entity relationships and dependencies
   - Extract validation rules and business invariants
   - Document integration requirements with other bounded contexts
   ```

### Phase 2: Domain Model Design with MCP Intelligence

**Execute comprehensive domain model design (Instructions to Claude Code in English):**

1. **Systematic Domain Model Architecture**

   ```
   Continue Sequential MCP analysis focusing on domain architecture:
   - Entity design with identity patterns and lifecycle management
   - Value object design with immutable properties and validation
   - Aggregate root identification and boundary consistency rules
   - Domain service design for complex business operations
   - Repository interface definition for persistence abstraction
   ```

2. **Business Rule and Invariant Extraction**

   ```
   Extract and formalize business rules from use cases:
   - Map Given-When-Then scenarios to domain invariants
   - Identify entity validation rules and constraints
   - Design aggregate consistency boundaries
   - Document business logic that requires domain services
   - Define domain events for cross-aggregate communication
   ```

3. **Context7 Integration for DDD Best Practices**

   ```
   If MCP_CONTEXT7 is available:
   - Apply industry-standard entity design patterns
   - Integrate latest aggregate design methodologies
   - Use proven value object design approaches
   - Apply DDD tactical pattern best practices for maintainable design
   ```

### Phase 3: Documentation and Learning

**Execute comprehensive documentation with MCP learning integration (Instructions to Claude Code in English):**

1. **Create domain model documentation**

   ```
   Generate comprehensive domain model documentation:
   Create directory: docs/domain/ (if not exists)
   
   Write "docs/domain/issue-${ISSUE_NUMBER}-domain-model.md" including:
   - Domain overview and bounded context definition
   - Entity specifications with identity, lifecycle, and behavior
   - Value object designs with immutable properties and validation
   - Aggregate boundaries and consistency rules
   - Domain services for complex business operations
   - Repository interfaces for persistence abstraction
   - Business rules and invariants extracted from scenarios
   - Ubiquitous language definitions and terminology
   ```

2. **Create MCP-enhanced documentation (if available)**

   ```
   If Sequential MCP, Serena, or Context7 MCPs were used, create additional documentation:
   Write "docs/domain/issue-${ISSUE_NUMBER}-mcp-analysis.md" including:
   - Sequential MCP systematic domain analysis results
   - Serena-discovered domain patterns and existing code analysis
   - Context7 DDD best practice integration recommendations
   - Business rule extraction results with traceability
   - Implementation guidance based on MCP insights
   ```

3. **MCP learning and memory storage**

   ```
   If MCP_SERENA is available, store learning insights:
   Use mcp__serena__write_memory to record:
   - Domain modeling insights for "domain-patterns-$(date +%Y%m%d)"
   - Business rule patterns for "business-rules-$(date +%Y%m%d)"
   - DDD design decisions for "ddd-architecture-$(date +%Y%m%d)"
   ```

4. **Git commit documentation**

   ```
   Bash git add docs/domain/
   Bash git commit -m "feat: create domain models for issue ${ISSUE_NUMBER}

   Design entities, value objects, and aggregates based on DDD principles.
   Extract business rules from Given-When-Then scenarios.

   🎯 Generated with Claude Code
   "
   ```

## ✅ Built-in Quality Assurance

### Self-Diagnosis Checklist

**Domain Model Design Completion (MUST):**

- [ ] Use case specifications analyzed and domain concepts extracted
- [ ] Entities designed with clear identity and lifecycle management
- [ ] Value objects specified with immutable properties and validation
- [ ] Aggregate boundaries defined with consistency rules
- [ ] Business rules extracted and formalized from scenarios
- [ ] Domain model documentation properly created

**MCP Integration Quality (if available):**

- [ ] Sequential MCP systematic domain analysis completed (if available)
- [ ] Serena MCP existing pattern analysis utilized (if available)
- [ ] Context7 DDD best practices integrated (if available)
- [ ] MCP learning insights stored for future reference (if available)

**Documentation Quality (MUST):**

- [ ] Domain model specification created with clear design
- [ ] Business rules documented with traceability to use cases
- [ ] Repository interfaces and domain services specified
- [ ] All documentation committed to version control

**Design Quality (SHOULD):**

- [ ] Domain purity maintained with no infrastructure concerns
- [ ] Aggregate boundaries align with business consistency requirements
- [ ] Ubiquitous language consistently applied throughout design
- [ ] Design ready for test-driven implementation

### Quality Assessment

| Quality Area | Assessment Criteria | Status |
|--------------|-------------------|--------|
| **Domain Design** | Entities, value objects, aggregates properly designed | ✅/❌ |
| **Business Rules** | Rules extracted and formalized from scenarios | ✅/❌ |
| **Architecture** | Clean separation and proper boundaries maintained | ✅/❌ |
| **Documentation** | Comprehensive and implementation-ready specifications | ✅/❌ |
| **MCP Integration** | Available MCPs effectively utilized for enhancement | ✅/❌/N/A |

## 📊 Standardized Output Format

### 実行サマリー (日本語でユーザーに報告)

**基本設計完了:**

- ✅ **ユースケース分析**: Given-When-Thenシナリオからドメイン概念抽出完了
- ✅ **エンティティ設計**: アイデンティティ、ライフサイクル、振る舞いの明確な設計完了
- ✅ **値オブジェクト設計**: 不変性と検証ルールを持つ値オブジェクト仕様完成
- ✅ **ビジネスルール抽出**: ドメイン不変条件とビジネス制約の体系的抽出完了

**MCP 拡張設計 (利用可能時):**

- ✅ **Sequential MCP分析**: ドメインアーキテクチャの体系的設計と複雑性分析
- ✅ **Serena パターン分析**: 既存コードのドメインパターン発見と活用
- ✅ **Context7 統合**: 最新DDD手法とタクティカルパターン適用
- ✅ **学習記録**: 今回の設計知見をパターンライブラリに蓄積

### 成果物

**必須ドキュメント:**

- `docs/domain/issue-${ISSUE_NUMBER}-domain-model.md`: 包括的ドメインモデル仕様書
- ビジネスルール・不変条件の完全な文書化

**MCP 拡張ドキュメント (利用可能時):**

- `docs/domain/issue-${ISSUE_NUMBER}-mcp-analysis.md`: MCP設計分析とインサイト
- Serena MCPメモリファイル: 学習結果の永続化とパターン蓄積

### 総合判定

**設計完成状況**: `READY` / `CONDITIONAL` / `REVISION_REQUIRED`
**主要成果**: [設計されたエンティティ、値オブジェクト、アグリゲートの要約]  
**推奨次ステップ**: [テスト駆動開発フェーズへの移行準備完了]

### 次のステップ (日本語でユーザーに案内)

1. **設計承認時**: `/create-tests-enhanced ${ISSUE_NUMBER}` でTDDテスト作成開始
2. **設計調整時**: ドメインエキスパートレビュー後、必要に応じて設計を調整
3. **確認推奨**: ビジネスルールとアグリゲート境界の妥当性確認

**ユーザーへのメッセージ (日本語)**:

```
🎉 ドメインモデル設計完了！

📊 ドメイン設計結果:
   ✅ 設計状況: [READY/CONDITIONAL/REVISION_REQUIRED]
   🏗️ エンティティ: [設計されたエンティティの要約]
   💎 値オブジェクト: [値オブジェクト設計の要約]
   🔗 アグリゲート: [アグリゲート境界の要約]

💡 設計分析結果:
   🎯 強み: [ドメイン設計の優位性]
   ⚡ 注意点: [実装時の重要な留意事項]
   🔄 ビジネスルール: [抽出されたビジネス制約]

🧠 MCP設計強化 (利用時):
   📊 Sequential分析: ドメインアーキテクチャの体系的設計完了
   🔍 Serena インサイト: 既存パターンの発見と設計への反映
   🌐 Context7 統合: 最新DDD手法を設計に適用

📁 生成ドキュメント:
   ✅ docs/domain/issue-${ISSUE_NUMBER}-domain-model.md

🚀 次のアクション:
   📋 `/create-tests-enhanced ${ISSUE_NUMBER}` でTDD開発開始

✅ ドメインモデル設計完了 - TDD実装準備完了！
```

## Common Errors and Solutions

### ❌ Error Case 1: Use case specification not found
**Cause**: Missing or incorrectly located use case specification files  
**Solution**: 
- Verify use case specification exists: `find docs/use_cases/ -name "*issue*${ISSUE_NUMBER}*"`
- Run `/create-use-case-enhanced ${ISSUE_NUMBER}` first if missing
- Check issue number parameter accuracy

### ❌ Error Case 2: Insufficient domain concepts in use case
**Cause**: Use case lacks clear business rules or domain concepts  
**Solution**: 
- Review use case specification for business logic gaps
- Engage domain experts for clarification of business rules
- Update use case specification with missing domain concepts

### ❌ Error Case 3: Complex aggregate boundary decisions
**Cause**: Unclear consistency boundaries or transaction scope  
**Solution**: 
```bash
# Use Sequential MCP for complex boundary analysis
# Focus on business consistency requirements
# Consider performance and scalability implications
```

## Execution Examples

### ✅ Success Example - Full Domain Modeling with Sequential MCP
```bash
$ /domain-modeling-enhanced 456

🚀 Domain Modeling with Intelligent MCP Integration for Issue #456

📊 ドメインモデリング分析:
  🎯 ユースケース: "Add order management with inventory validation"
  📋 複雑性: 戦略・設計タスク（Sequential MCP使用）
  🧩 コンポーネント: Order + Inventory + Customer + Payment

🧩 Sequential MCP分析結果:
  📊 体系的分析: エンティティ・値オブジェクト・アグリゲート境界を決定
  🔍 Serena発見: 既存Customerエンティティパターンを活用
  🌐 Context7統合: 最新のDDD集約設計手法を適用

✅ ドメインモデル設計完了:
  🏗️ エンティティ: Order, Customer, InventoryItem (3個)
  💎 値オブジェクト: OrderId, Money, Quantity (3個)  
  🔗 アグリゲート: Order集約, Inventory集約 (2個)
  📋 ビジネスルール: 在庫検証、注文制約、支払い検証 (8個)

📁 成果物:
  ✅ docs/domain/issue-456-domain-model.md
  ✅ docs/domain/issue-456-mcp-analysis.md

🚀 次のステップ: `/create-tests-enhanced 456`
```
