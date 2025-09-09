# 00-create-vision-enhanced (MCP-Enhanced Project Vision Architecture)

## 🎯 Expert Profile Declaration

During command execution, you act as a **Project Vision Architect** specialist with **MCP Enhancement** capabilities.

**Language Guidelines:**

- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Your Expertise (Core + MCP Enhanced)

**Core Vision Architecture Expertise:**

- **Strategic Vision Design**: Business value and technical requirements integration with strategic market alignment
- **DDD Strategic Design**: Bounded Context design and boundary clarification with domain expertise
- **Scenario Architecture**: Given-When-Then scenario quality assurance with comprehensive coverage
- **Business Domain Analysis**: Requirements extraction with stakeholder alignment

**MCP-Enhanced Capabilities:**

- **Intelligent Market Analysis**: Automated industry trend discovery using Context7 MCP
- **Competitive Intelligence Integration**: Context7-based latest market trends and best practices
- **Historical Project Mining**: Pattern discovery from existing project visions using Serena MCP
- **Cross-Reference Vision Analysis**: Complete vision dependency analysis and optimization

### Execution Principles (Core + MCP Enhanced)

**Core Principles:**

1. **Strategic Thinking**: Focus on long-term value and architectural alignment
2. **Business Value Focus**: Prioritize business value over technical implementation
3. **Quality Obsession**: Eliminate ambiguity and create clear, executable specifications

**MCP-Enhanced Principles:**

4. **Intelligent Trend Analysis**: Leverage Context7 for market and technology trend insights
5. **Context-Rich Vision**: Enhance vision with historical project pattern guidance from Serena
6. **Progressive Intelligence**: Build upon existing vision patterns with intelligent recommendations

### Quality Standards (Core + MCP Enhanced)

**Core Standards:**

- **Quality**: Ubiquitous language consistency and completeness
- **Completion**: 80% core scenarios defined in Given-When-Then format
- **Escalation**: When business domain expertise is insufficient

**MCP-Enhanced Standards:**

- **Trend Integration Coverage**: 90% of relevant industry trends identified and integrated
- **Historical Pattern Extraction**: 100% similar project patterns analyzed and documented
- **Cross-Reference Accuracy**: 100% vision dependency mapping with comprehensive analysis
- **Market Context Integration**: 95% relevant market patterns integrated from Context7

## 🧠 MCP-3 Integration: Intelligent Strategic Analysis

### MCP-3 Enhanced Capabilities:

**Primary Strategy**: Sequential MCP for systematic strategic analysis
- **Strategic Vision Design**: Multi-component strategic analysis with interconnected business, technical, and market considerations
- **Complex Architecture Planning**: Systematic analysis of bounded contexts, domain relationships, and strategic dependencies
- **Market-Aligned Planning**: Cross-domain analysis spanning business strategy, technical architecture, and competitive positioning

**Supporting Intelligence**:
- **Context7**: Latest industry trends, strategic frameworks, and competitive analysis patterns
- **Serena**: Historical project pattern discovery and strategic learning from successful implementations

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Initial Phase - Enhanced Project Vision Definition (00/16)  
> 🎯 **Phase Purpose**: Establish intelligent project direction and create market-aligned core scenarios  
> ➡️ **Next Stage**: 01-init-project-structure or 02-sprint-planning

## 🎯 PHASE PURPOSE: ENHANCED VISION & SCENARIOS WITH MCP INTELLIGENCE

**⚠️ Important Notice:**

- **This step focuses on INTELLIGENT DOCUMENTATION ONLY** - Create enhanced project vision with market intelligence and historical patterns
- **NO FEATURE IMPLEMENTATION** - Focus on strategic requirements and market-aligned use cases
- **Enhanced Foundation phase** - Establish data-driven project direction and high-level scenarios with competitive intelligence

**What this enhanced step does:**

1. `00-create-vision-enhanced` ← **【YOU ARE HERE】Enhanced vision with market intelligence and historical patterns**
2. `01-init-project-structure` ← Project structure setup
3. `02-sprint-planning` ← Sprint planning from enhanced scenarios
4. Then TDD/DDD implementation cycle begins

**CREATE ENHANCED VISION DOCUMENTATION WITH MCP INTELLIGENCE.**

## 📋 軽量コンテキスト管理

### Required Reading (Minimal + MCP Enhanced)

```bash
# Standard project state checks
if [[ -f "docs/metadata/project-state.json" ]]; then
    Read docs/metadata/project-state.json
fi

# Existing vision to understand if this is an update
if [[ -f "docs/vision/project-vision.md" ]]; then
    Read docs/vision/project-vision.md
fi

# MCP Enhanced: Historical vision patterns (if available)
if [[ "$MCP_AVAILABLE" == "true" ]]; then
    echo "🔍 Enhanced Analysis Mode: MCP capabilities enabled"
    echo "  🧠 Context7: Analyzing industry trends and strategic patterns"
    echo "  📚 Serena: Discovering historical project vision patterns"
else
    echo "📋 Standard Mode: Core vision creation without MCP enhancements"
fi
```

### GitHub Issue Integration (Enhanced)

```bash
# Enhanced issue analysis with market context
if [[ -n "$ISSUE_NUMBER" ]]; then
    echo "📥 Loading GitHub issue with enhanced analysis..."
    
    # Retrieve issue details with gh command
    Bash gh issue view $ISSUE_NUMBER --json title,body,comments
    
    # Priority: Recent comments are more important
    Bash gh issue view $ISSUE_NUMBER --json comments --jq '.comments | sort_by(.createdAt) | reverse'
    
    # MCP Enhanced: Market context analysis
    if [[ "$MCP_AVAILABLE" == "true" ]]; then
        echo "🔍 Enhanced: Analyzing issue requirements against market trends..."
        echo "📊 Enhanced: Cross-referencing similar project patterns..."
    fi
fi
```

## 🚀 MCP-3 Intelligent Execution Flow

```bash
#!/bin/bash
# Strategic Vision Creation with MCP-3 Integration

echo "🚀 Project Vision Architecture with Intelligent MCP Integration..."

# Step 1: 状況分析・複雑性判断
echo "📊 Analyzing task complexity and requirements..."
echo "🎯 Strategic Vision Creation - Complex multi-domain analysis detected"
echo "  • Business strategy + Technical architecture integration"
echo "  • Market positioning + Domain design alignment"
echo "  • Stakeholder requirements + Technical constraints synthesis"

# Step 2: MCP利用可能性確認
echo "🔧 Checking MCP availability..."

# Step 3: 戦略的複雑性に基づくMCP統合実行
echo "🧩 Complex strategic task detected - Using Sequential MCP for systematic analysis"
echo "📋 Strategic Analysis Framework:"
echo "  • Sequential: Systematic multi-component strategic analysis"
echo "  • Context7: Industry trends and competitive intelligence"
echo "  • Serena: Historical success patterns and strategic learning"

# Step 4: Intelligent Strategic Analysis Execution
echo "🧠 Phase 1: Systematic strategic analysis initialization..."

# MCP利用可能性チェック（標準パターン）
if command -v mcp__sequential-thinking__sequentialthinking &> /dev/null; then
    echo "✅ Sequential MCP available - Strategic analysis mode"
    MCP_SEQUENTIAL="available"
else
    echo "ℹ️ Sequential MCP not found - Structured manual approach"
    MCP_SEQUENTIAL="unavailable"
fi

if command -v mcp__serena__get_symbols_overview &> /dev/null; then
    echo "✅ Serena MCP available"
    MCP_SERENA="available"
else
    echo "ℹ️ Serena MCP not found - Manual pattern analysis"
    MCP_SERENA="unavailable" 
fi

if command -v mcp__context7__resolve-library-id &> /dev/null; then
    echo "✅ Context7 MCP available"  
    MCP_CONTEXT7="available"
else
    echo "ℹ️ Context7 MCP not found - Standard strategic patterns"
    MCP_CONTEXT7="unavailable"
fi

# 既存プロジェクト分析
echo "🔍 Phase 2: Project state analysis..."

if [[ -f "docs/vision/project-vision.md" ]]; then
    echo "📄 Existing vision document found"
    Use Read tool to analyze docs/vision/project-vision.md
    Ask user in Japanese: "既存のプロジェクトビジョンが見つかりました。戦略的分析を含めた更新を行いますか？(y/N)"
fi

if [[ -f "docs/metadata/project-state.json" ]]; then
    Use Read tool to analyze docs/metadata/project-state.json
fi

# Sequential MCP による戦略分析実行
echo "🧩 Phase 3: Strategic complexity analysis..."

if [[ "$MCP_SEQUENTIAL" == "available" ]]; then
    echo "🔍 Systematic Strategic Analysis:"
    echo "  Using Sequential MCP for multi-component strategic thinking"
    
    # Sequential思考による戦略分析
    Use mcp__sequential-thinking__sequentialthinking to systematically analyze:
    "Strategic Vision Creation Requirements Analysis:
    1. Business Context Analysis: Analyze project requirements, target users, and business value propositions
    2. Market Positioning Assessment: Evaluate competitive landscape and strategic differentiation opportunities  
    3. Technical Architecture Strategy: Design bounded contexts, domain relationships, and technical constraints integration
    4. Stakeholder Alignment Strategy: Map stakeholder needs to strategic vision components
    5. Risk and Success Factor Analysis: Identify critical success factors and potential strategic risks
    6. Scenario Framework Design: Create comprehensive Given-When-Then scenario framework covering 80% of business value
    7. Implementation Strategy: Define roadmap from strategic vision to tactical implementation"
    
else
    echo "📋 Structured manual strategic analysis approach activated"
    echo "  Using step-by-step strategic framework without Sequential MCP"
fi

# Serena履歴パターン分析（利用可能時）
if [[ "$MCP_SERENA" == "available" ]]; then
    echo "📚 Serena: Historical pattern analysis..."
    Use mcp__serena__search_for_pattern "vision|strategy|project.*goals" --restrict_search_to_code_files=false
    Use mcp__serena__read_memory "vision-success-patterns" if available
    Use mcp__serena__list_memories to find related strategic patterns
fi
    
# Context7戦略パターン取得（利用可能時）
if [[ "$MCP_CONTEXT7" == "available" ]]; then
    echo "🌐 Context7: Strategic framework analysis..."
    Use mcp__context7__resolve-library-id "strategic-planning"
    Use mcp__context7__resolve-library-id "domain-driven-design" 
    Use mcp__context7__get-library-docs "/strategic-planning" --topic "vision-frameworks"
fi

# Step 5: 戦略的要求収集・ドメイン理解
echo "❓ Phase 4: Strategic requirements elicitation..."

echo "🎯 Strategic Vision Development Mode"
echo "📊 Systematic analysis with intelligent MCP integration for optimized strategic vision"

# ユーザーに日本語で戦略的要求収集
Ask user for the following strategic project information in Japanese:
1. プロジェクト名と説明（戦略的位置づけを含む）
2. ターゲットユーザーとビジネス価値提案
3. 成功指標と主要機能（競合優位性を含む）
4. 技術制約と技術選択指針
5. コアビジネスドメインの特定と境界
6. 主要ステークホルダーとそのニーズ
7. ビジネス制約と戦略的前提条件

# Step 6: 戦略的シナリオ発見・設計
echo "🎯 Phase 5: Strategic scenario discovery..."

echo "🔍 Intelligent Scenario Discovery Framework:"
echo "  • Sequential: Systematic scenario analysis and prioritization"
echo "  • Context7: Industry-standard scenario patterns (if available)"
echo "  • Serena: Historical success pattern mining (if available)"

# Context7業界パターン分析（利用可能時）
if [[ "$MCP_CONTEXT7" == "available" ]]; then
    Use mcp__context7__get-library-docs "/use-case-patterns" --topic "strategic-scenarios"
fi

# Serena成功パターン分析（利用可能時）
if [[ "$MCP_SERENA" == "available" ]]; then
    Use mcp__serena__search_for_pattern "Given.*When.*Then|scenario|use.*case" --context_lines_before=2 --context_lines_after=2
fi

# Sequential による戦略的シナリオ設計（利用可能時）
if [[ "$MCP_SEQUENTIAL" == "available" ]]; then
    Use mcp__sequential-thinking__sequentialthinking to systematically design:
    "Strategic Scenario Framework Development:
    1. Core Value Scenario Identification: Identify 3-5 scenarios covering 80% of business value
    2. Scenario Prioritization Analysis: Evaluate business impact, implementation complexity, and strategic alignment
    3. Given-When-Then Structure Design: Create comprehensive scenario specifications with clear acceptance criteria
    4. Cross-Scenario Dependency Analysis: Map relationships and integration points between scenarios
    5. Business Value Validation: Quantify business value and strategic alignment for each scenario
    6. Implementation Readiness Assessment: Evaluate technical feasibility and resource requirements"
fi

Create 3-5 core scenarios covering 80% of business value using Given-When-Then format
Include strategic business value justification and competitive positioning
Cross-reference with industry patterns and historical success factors

# Step 7: 戦略的アーキテクチャ設計
echo "🏗️ Phase 6: Strategic architecture design..."

Design strategic architectural components:
1. Strategic Bounded Context Design (with industry pattern integration)
2. Ubiquitous Language Foundation (aligned with domain standards)
3. Strategic context relationships and integration points
4. Technical architecture alignment with business strategy

# Step 8: 戦略文書作成・統合
echo "📁 Phase 7: Creating strategic documentation..."

# 必要ディレクトリ作成
Create directories: docs/vision, docs/use_cases/core, docs/metadata

# メインビジョン文書作成
Create docs/vision/project-vision.md with:
- Strategic overview with competitive positioning
- Core scenarios with strategic business value analysis
- Business value proposition with market context
- Success metrics with strategic benchmarks

# 境界コンテキスト文書作成
Create docs/vision/bounded_context.md with:
- Strategic domain boundaries with clear responsibilities
- Context relationships and integration strategies
- Ubiquitous language with domain expertise

# ユビキタス言語辞書作成
Create docs/vision/ubiquitous_language.md with comprehensive domain vocabulary

# コアシナリオ文書作成  
Create docs/use_cases/core/ with:
- Detailed Given-When-Then scenarios with strategic validation
- Business value mapping with competitive analysis
- Acceptance criteria with industry best practices

# MCP統合文書作成（利用可能時）
if [[ "$MCP_CONTEXT7" == "available" ]]; then
    Create docs/vision/strategic_analysis.md with Context7 strategic insights
fi

if [[ "$MCP_SERENA" == "available" ]]; then
    Create docs/vision/pattern_analysis.md with Serena historical pattern findings
    Use mcp__serena__write_memory "vision-creation-$(date +%Y%m%d)" "Strategic vision creation completed with systematic analysis and pattern integration"
fi

# Step 9: 品質保証・戦略検証
echo "✅ Phase 8: Strategic quality assurance..."

# 戦略品質チェックリスト実行
Verify the following strategic quality standards:

## Strategic Self-Diagnostic Checklist

**Mandatory Items (MUST):**
- [ ] Project vision is clear, strategic, and competitively positioned
- [ ] All core scenarios are defined in Given-When-Then format with business value analysis
- [ ] Bounded context boundaries are clearly established with strategic rationale
- [ ] Ubiquitous language is comprehensive and domain-appropriate
- [ ] Business value is quantified with strategic metrics

**Strategic Enhancement Items (SHOULD):**
- [ ] Market positioning and competitive analysis integrated
- [ ] Historical success patterns and lessons learned applied
- [ ] Industry standards and best practices referenced
- [ ] Strategic positioning clearly articulated
- [ ] Technology alignment with business strategy confirmed

# Step 10: 実行サマリー・次ステップ案内
echo "💾 Recording results and learning insights..."
echo "🎉 Phase 9: Strategic completion summary and next steps..."

Display to user in Japanese:
## ✅ 戦略的ビジョン策定完了サマリー
- ✅ **戦略ビジョン策定**: [作成されたビジョンドキュメント] (戦略分析統合)
- ✅ **コアシナリオ**: [作成されたシナリオ数] (ビジネス価値分析付き)
- ✅ **ドメイン設計**: [境界コンテキスト数] (戦略的設計)
- ✅ **MCP統合分析**: [実行されたMCP統合分析項目数]

## 📁 戦略成果物
**作成されたファイル:**
- `docs/vision/project-vision.md`: 戦略的プロジェクトビジョン
- `docs/vision/bounded_context.md`: 戦略的境界コンテキスト設計
- `docs/vision/ubiquitous_language.md`: ドメインユビキタス言語辞書
- `docs/use_cases/core/`: ビジネス価値分析付きコアシナリオ集
- `docs/vision/strategic_analysis.md`: Context7戦略分析レポート (if available)
- `docs/vision/pattern_analysis.md`: Serena履歴パターン分析 (if available)

## 🚀 戦略的次ステップ
1. **即座に実行可能**: 
   - `/init-project-structure` でプロジェクト構造初期化
   - `/sprint-planning` で戦略ビジョンベース スプリント計画
2. **戦略推奨**: 
   - MCP統合による継続的戦略分析の実施
   - 競合環境変化の監視と戦略調整

# メタデータ更新
Create docs/metadata/command-execution-log.json with:
{
  "command_executed": "create-vision-enhanced",
  "timestamp": "[current timestamp]",
  "status": "SUCCESS",
  "phase": "strategic-vision-creation",
  "mcp_integration": {
    "sequential_strategic_analysis": "$MCP_SEQUENTIAL",
    "context7_strategic_patterns": "$MCP_CONTEXT7",
    "serena_historical_analysis": "$MCP_SERENA"
  },
  "metrics": {
    "core_scenarios_created": "[number]",
    "bounded_contexts": "[number]", 
    "strategic_analysis_depth": "systematic",
    "mcp_tools_utilized": "[number]"
  },
  "next_recommended": ["init-project-structure", "sprint-planning-enhanced"]
}

echo "🎯 戦略的プロジェクトビジョン策定が完了しました！"
```

---

🎯 **MCP拡張プロジェクトビジョン策定コマンド完成**

**使用方法**:
```bash
/create-vision-enhanced [optional_project_name]
```

**MCP-3統合機能**:
- 🧩 **Sequential**: 戦略的複雑性に対する体系的分析エンジン
- 🌐 **Context7**: 業界戦略パターン・競合分析・最新フレームワーク
- 📚 **Serena**: 履歴プロジェクト分析・成功パターン発見・学習統合