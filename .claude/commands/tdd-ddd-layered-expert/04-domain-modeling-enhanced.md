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

## 📋 MCP-Enhanced Domain Analysis

### Required Setup

```bash
# Validate issue number and MCP session
if [[ -z "$1" ]]; then
    echo "ERROR: Issue number required. Usage: /domain-modeling-enhanced <issue-number>"
    exit 1
fi

ISSUE_NUMBER="$1"
echo "🧠 Executing MCP-enhanced domain modeling with intelligent analysis..."

# Check MCP session availability (optional enhancement)
if [[ -f ".serena/sessions/current/session-metadata.json" ]]; then
    echo "✅ MCP session found - Enhanced analysis will be available"
    MCP_AVAILABLE="true"
else
    echo "ℹ️ MCP session not found - Running in standard mode"
    echo "💡 To enable MCP enhancements, run /context-session-stageup first"
    MCP_AVAILABLE="false"
fi

# Execute the enhanced Python implementation (inherits + extends existing functionality)
SCRIPT_PATH=".claude/commands/tdd-ddd-layered-expert/utils/04-domain-modeling-enhanced.py"

if [[ -f "$SCRIPT_PATH" ]]; then
    echo "✅ Found enhanced implementation: $SCRIPT_PATH"
    uv run "$SCRIPT_PATH" "$ISSUE_NUMBER"
    EXIT_CODE=$?
else
    echo "❌ Enhanced implementation not found: $SCRIPT_PATH"
    echo "💡 Please ensure the Python implementation is available"
    exit 1
fi

if [[ $EXIT_CODE -eq 0 ]]; then
    echo "✅ Domain modeling completed successfully"
else
    echo "❌ Domain modeling failed with exit code: $EXIT_CODE"
    exit $EXIT_CODE
fi
```

## 🚀 Expert Execution Flow

### Phase 1: Analysis and Understanding (Core + MCP Enhanced)

**Analyze the following as expert (User interactions in Japanese):**

**Core Analysis Activities:**

1. **Use Case Specification Analysis**

   - Extract domain concepts from Given-When-Then scenarios using Read tool
   - Identify entities (objects with identity and lifecycle)
   - Identify value objects (immutable, replaceable objects)
   - Extract business rules and invariants

2. **Existing Domain Model Consistency Check**
   - Check existing domain models using Glob tool
   - Ensure consistency with established ubiquitous language
   - Identify reusable domain patterns

**MCP-Enhanced Analysis (if available):** 3. **Automated Domain Pattern Discovery**

- Use mcp**serena**get_symbols_overview to scan entire codebase
- Use mcp**serena**find_symbol to identify potential entities and value objects
- Use mcp**serena**search_for_pattern to find existing business rules
- Create memory using mcp**serena**write_memory for discovered patterns

4. **Intelligent Business Logic Mining**
   - Use mcp**serena**find_symbol with pattern matching for business methods
   - Use mcp**serena**find_referencing_symbols to trace business logic flows
   - Extract validation rules and business invariants automatically
   - Document findings in architecture memory

### Phase 2: Design and Planning (Core + MCP Enhanced)

**Design the following as expert (Instructions to Claude Code in English):**

**Core Design Activities:**

1. **Entity Design**

   ```
   For each identified entity:
   - Define entity identity and lifecycle
   - Specify entity behavior and methods
   - Document business rules and invariants
   - Define relationships with other entities
   ```

2. **Value Object Design**

   ```
   For each identified value object:
   - Define immutable properties
   - Specify validation rules
   - Document equality semantics
   - Design factory methods if needed
   ```

3. **Aggregate Boundary Design**
   ```
   For each aggregate:
   - Identify aggregate root
   - Define consistency boundaries
   - Specify business invariants
   - Design repository interface
   ```

**MCP-Enhanced Design (if available):** 4. **Context7 DDD Pattern Integration**

```
Use mcp__context7__resolve-library-id for "domain-driven-design"
Use mcp__context7__get-library-docs for DDD tactical patterns
Use mcp__context7__get-library-docs for aggregate design patterns
Integrate latest best practices into domain model design
```

5. **Technology-Specific Pattern Enhancement**
   ```
   Identify project tech stack from codebase analysis
   Use mcp__context7__resolve-library-id for framework-specific patterns
   Use mcp__context7__get-library-docs for ORM and persistence patterns
   Apply technology-specific domain modeling guidance
   ```

### Phase 3: Implementation and Execution (Core + MCP Enhanced)

**Execute the following as expert (Instructions to Claude Code in English):**

**Core Implementation Steps:**

1. **Validate issue numbers and prerequisites**

   ```bash
   # Validate issue number requirement
   if [[ $# -eq 0 ]]; then
       echo "Error: At least one issue number must be specified"
       echo "Usage example: /domain-modeling-enhanced 1"
       exit 1
   fi

   # Check for use case specifications
   for issue_num in $(echo $1 | tr ',' ' '); do
       USE_CASE_FILE=$(find docs/use_cases/ -name "*issue*${issue_num}*.md" -type f | head -1)
       if [[ ! -f "$USE_CASE_FILE" ]]; then
           echo "❌ Error: Use case specification for Issue #${issue_num} not found"
           echo "💡 Please execute /create-use-case ${issue_num} first"
           exit 1
       fi
   done
   ```

2. **Create standard domain model documents**

   ```bash
   # Create docs/domain directory if not exists
   Bash mkdir -p docs/domain

   # For each issue, create domain model document
   for issue_num in $(echo $1 | tr ',' ' '); do
       DOMAIN_FILE="docs/domain/issue-${issue_num}-domain-model.md"

       # Create comprehensive domain model document
       Write "$DOMAIN_FILE" with domain model content including:
       # - Domain overview and bounded context
       # - Entity definitions with behavior
       # - Value object specifications
       # - Aggregate boundaries and roots
       # - Domain services for complex logic
       # - Repository interfaces
       # - Domain events if applicable
       # - Business rules and invariants
       # - Ubiquitous language definitions
   done
   ```

**MCP-Enhanced Implementation (if available):** 3. **Intelligent Entity Design Enhancement**

```bash
# Enhanced entity models with MCP analysis
For each identified entity from Serena analysis:
- Extract existing behavior patterns from code
- Identify missing business methods using pattern analysis
- Generate complete entity specification with Context7 patterns
- Document entity relationships and dependencies
```

4. **Automated Value Object Discovery**

   ```bash
   # Intelligent value object identification
   Use Serena MCP to identify primitive obsession patterns
   Recommend value object candidates from code analysis
   Apply Context7 value object design patterns
   Generate immutable value object specifications
   ```

5. **Aggregate Boundary Optimization**
   ```bash
   # Automated aggregate boundary analysis
   Use mcp__serena__find_referencing_symbols for dependency mapping
   Analyze transaction boundaries from existing code
   Apply Context7 aggregate design best practices
   Generate optimized aggregate root specifications
   ```

### Phase 4: Documentation and Integration (Core + MCP Enhanced)

**Execute the following as expert (Instructions to Claude Code in English):**

1. **Create core domain documentation (always)**

   ```bash
   # Standard domain model document (always created)
   Write "docs/domain/issue-${ISSUE_NUMBER}-domain-model.md" with:
   # - Domain overview and bounded context
   # - Entity definitions with behavior
   # - Value object specifications
   # - Aggregate boundaries and roots
   # - Domain services for complex logic
   # - Repository interfaces
   # - Domain events if applicable
   # - Business rules and invariants
   # - Ubiquitous language definitions
   ```

2. **Create MCP analysis documents (if available)**

   ```bash
   if [[ "$MCP_AVAILABLE" == "true" ]]; then
       # MCP-enhanced analysis document
       Write "docs/domain/issue-${ISSUE_NUMBER}-mcp-analysis.md" with:
       # - MCP-discovered domain patterns analysis
       # - Automated business rule extraction results
       # - Cross-reference dependency mapping
       # - Context7-enhanced design recommendations
       # - Implementation improvement suggestions

       # MCP detailed reports
       Write "docs/domain/issue-${ISSUE_NUMBER}-mcp-analysis-report.md" with:
       # - Serena MCP codebase analysis summary
       # - Discovered anti-patterns and improvement recommendations
       # - Business logic extraction results
       # - Cross-reference analysis and dependency graph
       # - Context7 pattern integration recommendations

       # Implementation guidance
       Write "docs/domain/issue-${ISSUE_NUMBER}-implementation-guidance.md" with:
       # - Step-by-step implementation plan with MCP insights
       # - Code refactoring recommendations from Serena analysis
       # - Pattern implementation examples from Context7
       # - Testing strategy recommendations
       # - Performance and maintainability considerations

       # Update MCP memory with findings
       Use mcp__serena__write_memory to store:
       # - Domain model analysis results
       # - Business rule extraction outcomes
       # - Architectural improvement recommendations
       # - Pattern discovery summary
   fi
   ```

3. **Update project metadata**

   ```bash
   # Update use case metadata files
   for issue_num in $(echo $1 | tr ',' ' '); do
       METADATA_FILE=$(find docs/use_cases/sprints/ -name "*issue*${issue_num}*.json" -type f | head -1)
       if [[ -f "$METADATA_FILE" ]]; then
           # Update metadata to mark domain modeling as complete
           # Set phases.domain_model.created to true
           # Add domain model file reference
       fi
   done

   # Update use cases index
   if [[ -f "docs/use_cases/index.md" ]]; then
       # Update index to reflect domain modeling completion status
   fi
   ```

4. **Git commit domain models**
   ```bash
   Bash git add docs/domain/
   if [[ "$MCP_AVAILABLE" == "true" ]]; then
       Bash git commit -m "feat: create domain models for issues $(echo $1 | tr ',' ' ') with MCP enhancement

   Design entities, value objects, and aggregates based on DDD principles.
   Extract business rules from Given-When-Then scenarios.
   Enhanced with MCP intelligent analysis and pattern discovery.

   🎯 Generated with Claude Code
       "
   else
       Bash git commit -m "feat: create domain models for issues $(echo $1 | tr ',' ' ')

   Design entities, value objects, and aggregates based on DDD principles.
   Extract business rules from Given-When-Then scenarios.

   🎯 Generated with Claude Code
       "
   fi
   ```

## ✅ Built-in Quality Assurance

### Self-Diagnosis Checklist

**Required Items (MUST):**

- [ ] Serena MCP codebase analysis completed
- [ ] Context7 pattern integration applied
- [ ] Enhanced domain models generated with intelligence
- [ ] Business rules automatically extracted and documented
- [ ] Cross-reference analysis completed
- [ ] Implementation guidance created

**Recommended Items (SHOULD):**

- [ ] Anti-pattern identification and recommendations provided
- [ ] Performance implications analyzed and documented
- [ ] Refactoring roadmap created with priorities
- [ ] Test strategy aligned with domain model enhancements

### Quality Metrics

| Metric                          | Target | Actual         | Assessment |
| ------------------------------- | ------ | -------------- | ---------- |
| Business Rule Coverage          | 100%   | [Actual Value] | ✅/❌      |
| Aggregate Design Quality        | 90%    | [Actual Value] | ✅/❌      |
| Ubiquitous Language Consistency | 95%    | [Actual Value] | ✅/❌      |

**MCP-Enhanced Metrics (if MCP Available):**
| Metric | Target | Actual | Assessment |
|--------|--------|--------|-----------|
| Pattern Discovery Coverage | 90% | [Actual Value] | ✅/❌ |
| Automated Rule Extraction | 95% | [Actual Value] | ✅/❌ |
| Context7 Integration | 85% | [Actual Value] | ✅/❌ |
| Cross-Reference Accuracy | 100% | [Actual Value] | ✅/❌ |

## 📊 Standardized Output Format

### 実行サマリー (日本語でユーザーに報告)

**基本機能 (常に実行):**

- ✅ **ユースケース仕様分析**: [Issue numbers] の仕様を分析完了
- ✅ **ドメインモデル設計**: エンティティ X 個、値オブジェクト Y 個を設計
- ✅ **アグリゲート境界定義**: Z 個のアグリゲートを定義完了
- ✅ **ドキュメント作成**: docs/domain/issue-X-domain-model.md 作成

**MCP 拡張機能 (利用可能時):**

- ✅ **MCP コードベース分析**: [X]個のファイル、[Y]個のシンボル分析完了
- ✅ **ドメインパターン発見**: エンティティ[A]個、値オブジェクト[B]個を自動発見
- ✅ **ビジネスルール抽出**: [C]個のビジネスルールを自動抽出
- ✅ **Context7 パターン統合**: 最新 DDD 設計パターン適用完了
- ✅ **実装ガイダンス生成**: MCP 分析に基づく実装計画作成

### 成果物

**基本ファイル (常に作成):**

- `docs/domain/issue-X-domain-model.md`: ドメインモデル設計書
- Updated metadata files: 対応する use case metadata の更新

**MCP 拡張ファイル (利用可能時):**

- `docs/domain/issue-X-mcp-analysis.md`: MCP 分析結果
- `docs/domain/issue-X-mcp-analysis-report.md`: 詳細 MCP 分析レポート
- `docs/domain/issue-X-implementation-guidance.md`: 実装ガイダンス
- Updated MCP memory files: ドメイン分析結果の永続化

### 総合判定

**ステータス**: `SUCCESS` (基本) / `MCP_ENHANCED_SUCCESS` (MCP 利用時)
**品質スコア**: [スコア]/100
**MCP インテリジェンス品質**: [スコア]/100 (利用時のみ)
**次フェーズ準備**: `READY`

### 次のステップ (日本語でユーザーに案内)

1. **即座に実行可能**: `/create-tests [issue-numbers]` または `/create-tests-enhanced [issue-numbers]`
2. **推奨**: TDD テスト作成フェーズに進む
3. **確認推奨**: ドメインモデル設計のレビュー

**ユーザーへのメッセージ (日本語)**:

```
🎉 ドメインモデリング完了！

🏗️ ドメイン設計要素:
   📊 エンティティ: [count] 個
   📊 値オブジェクト: [count] 個
   📊 アグリゲート: [count] 個
   📊 ドメインサービス: [count] 個

📁 作成されたファイル:
   ✅ docs/domain/issue-X-domain-model.md

🧠 MCP強化機能 (利用時のみ):
   📊 Serena分析: [X]ファイル、[Y]シンボル分析
   🔍 発見パターン: エンティティ[A]個、値オブジェクト[B]個
   📋 抽出ビジネスルール: [C]個
   🌐 Context7統合: 最新DDD設計パターン適用
   ✅ docs/domain/issue-X-mcp-analysis.md
   ✅ docs/domain/issue-X-mcp-analysis-report.md
   ✅ docs/domain/issue-X-implementation-guidance.md
   ✅ MCP メモリファイル更新

📋 次のステップ (テスト作成):
   /create-tests [issue-numbers] または /create-tests-enhanced [issue-numbers]

✅ ドメインモデリング完了 - TDD テスト作成準備完了！
```
