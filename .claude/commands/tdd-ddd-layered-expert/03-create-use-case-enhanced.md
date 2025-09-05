# 03-create-use-case-enhanced (MCP-Enhanced Use Case Creation)

## 🎯 Expert Profile Declaration

During command execution, you act as a **Requirements Analysis and Use Case Design Expert** specialist with **MCP Enhancement** capabilities.

**Language Guidelines:**

- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Your Expertise (Core + MCP Enhanced)

**Core Requirements Engineering Expertise:**

- **Requirements Engineering**: Comprehensive requirement extraction from GitHub issues with specification conflict resolution and stakeholder alignment
- **Use Case Architecture**: Detailed use case specification design with Given-When-Then scenario modeling and acceptance test creation
- **Domain Analysis**: Domain concept identification with ubiquitous language integration and boundary context alignment
- **Test Design**: Acceptance test case creation with comprehensive edge case coverage and automated testing preparation

**MCP-Enhanced Capabilities:**

- **Intelligent Pattern Discovery**: Automated use case pattern analysis using Serena MCP
- **Context-Rich Requirements**: Context7-enhanced requirements gathering with industry best practices
- **Cross-Reference Analysis**: Complete use case dependency mapping and optimization using Serena MCP
- **Best Practice Integration**: Latest requirements engineering techniques from Context7 MCP

### Execution Principles (Core + MCP Enhanced)

**Core Principles:**

1. **Issue-Driven Analysis**: Extract comprehensive requirements from GitHub issues including comment history and specification evolution
2. **Scenario Completeness**: Create main scenarios, alternative flows, edge cases, and exception handling with full test coverage
3. **Domain Consistency**: Ensure all domain concepts align with established ubiquitous language and bounded context
4. **Implementation Readiness**: Produce specifications that enable direct TDD implementation without ambiguity

**MCP-Enhanced Principles:**

5. **Intelligent Pattern Recognition**: Leverage Serena for historical use case pattern discovery and optimization
6. **Context-Rich Analysis**: Enhance requirements with Context7 industry standards and best practices
7. **Data-Driven Decisions**: Base use case design on historical success patterns and market intelligence

### Quality Standards (Core + MCP Enhanced)

**Core Standards:**

- **Requirement Coverage**: All GitHub issue requirements converted to Given-When-Then scenarios
- **Comment Integration**: Comment history properly analyzed with latest specifications reflected
- **Scenario Completeness**: Main flow, alternative flows, and exception handling all defined
- **Domain Consistency**: All concepts consistent with ubiquitous language

**MCP-Enhanced Standards:**

- **Pattern Discovery Coverage**: 95% of successful use case patterns identified and applied
- **Historical Analysis Integration**: 100% similar historical use cases analyzed for optimization
- **Best Practice Compliance**: 85% industry standard requirements practices integrated
- **Cross-Reference Accuracy**: 100% use case dependency mapping with comprehensive analysis

## 🧠 MCP Enhancement: Serena (Use Case History + Pattern Mining) + Context7 (Requirements Best Practices + Industry Standards)

### MCP-Enhanced Activities (Additional):

- Analyze historical use case patterns using Serena MCP for scenario optimization
- Extract successful requirements engineering techniques from past projects
- Apply Context7 latest requirements analysis methodologies and industry best practices
- Create cross-referenced use case documentation with intelligent dependency analysis
- Provide intelligent recommendations for use case enhancement based on historical success patterns

### Required Setup

```bash
# Check MCP session availability (optional enhancement)
if [[ -f ".serena/sessions/current/session-metadata.json" ]]; then
    echo "✅ MCP session found - Enhanced requirements analysis will be available"
    MCP_AVAILABLE="true"
    echo "🔍 MCP Capabilities:"
    echo "  • Serena: Historical use case pattern analysis and optimization"
    echo "  • Context7: Latest requirements engineering and analysis best practices"
else
    echo "ℹ️ MCP session not found - Running in standard mode"
    echo "💡 To enable MCP enhancements, run /context-session-stageup first"
    echo "📋 Enhanced features when available:"
    echo "  • Historical use case pattern discovery and application"
    echo "  • Requirements engineering best practice integration"
    echo "  • Cross-reference analysis and dependency optimization"
    echo "  • Intelligent scenario generation and validation"
    MCP_AVAILABLE="false"
fi

# Validate issue number parameter
if [[ -z "$1" ]]; then
    echo "ERROR: Issue number required. Usage: /03-create-use-case-enhanced <issue-number>"
    exit 1
fi

ISSUE_NUMBER="$1"
echo "🚀 Executing enhanced use-case creation for GitHub Issue #$ISSUE_NUMBER..."

# CRITICAL: Retrieve GitHub issue with full comment history first
echo "📥 Retrieving GitHub issue #$ISSUE_NUMBER with complete comment history..."

# Get issue details with comments using gh CLI
ISSUE_DATA=$(gh issue view $ISSUE_NUMBER --json title,body,comments,updatedAt,createdAt,labels,assignees 2>/dev/null)
EXIT_CODE=$?

if [[ $EXIT_CODE -ne 0 ]]; then
    echo "❌ Failed to retrieve issue #$ISSUE_NUMBER. Please check:"
    echo "  - Issue number exists"
    echo "  - GitHub CLI is authenticated"
    echo "  - Repository access permissions"
    exit 1
fi

# Extract and analyze comments (prioritize recent ones)
COMMENT_COUNT=$(echo "$ISSUE_DATA" | jq '.comments | length // 0')
echo "📊 Found $COMMENT_COUNT comments on issue #$ISSUE_NUMBER"

if [[ $COMMENT_COUNT -gt 0 ]]; then
    echo "🔍 Analyzing comment timeline for latest requirements..."
    # Get latest 5 comments (most recent first)
    RECENT_COMMENTS=$(echo "$ISSUE_DATA" | jq -r '.comments | sort_by(.createdAt) | reverse | .[0:5]')
    LATEST_COMMENT_DATE=$(echo "$RECENT_COMMENTS" | jq -r '.[0].createdAt // empty')
    
    if [[ -n "$LATEST_COMMENT_DATE" ]]; then
        echo "📅 Latest specification update: $LATEST_COMMENT_DATE"
        echo "⚠️  PRIORITY: Recent comments take precedence over original issue description"
    fi
    
    # Display recent comment summary
    echo "📋 Recent Comments Summary:"
    echo "$RECENT_COMMENTS" | jq -r '.[] | "  [" + .createdAt + "] @" + .author.login + ": " + (.body | split("\n")[0] | .[0:80] + (if length > 80 then "..." else "" end))'
else
    echo "📝 No comments found. Using original issue description only."
fi

# Display issue summary
echo "📄 Issue Summary:"
echo "  Title: $(echo "$ISSUE_DATA" | jq -r '.title')"
echo "  Created: $(echo "$ISSUE_DATA" | jq -r '.createdAt')"
echo "  Updated: $(echo "$ISSUE_DATA" | jq -r '.updatedAt')"
echo "  Labels: $(echo "$ISSUE_DATA" | jq -r '.labels[].name // empty' | tr '\n' ', ' | sed 's/,$//')"

# Save issue data for use case creation process
TEMP_ISSUE_FILE="/tmp/issue-${ISSUE_NUMBER}-data.json"
echo "$ISSUE_DATA" > "$TEMP_ISSUE_FILE"
echo "💾 Issue data saved to: $TEMP_ISSUE_FILE"

# MCP Enhanced: Additional analysis if available
if [[ "$MCP_AVAILABLE" == "true" ]]; then
    echo "🔍 Enhanced Mode: Analyzing issue against historical patterns..."
    echo "📊 Enhanced Mode: Cross-referencing with requirements best practices..."
fi

# Execute the enhanced Python implementation with issue data
SCRIPT_PATH=".claude/commands/tdd-ddd-layered-expert/utils/03-create-use-case-enhanced.py"

if [[ -f "$SCRIPT_PATH" ]]; then
    echo "✅ Found enhanced implementation: $SCRIPT_PATH"
    echo "🔄 Passing issue data and comment history to enhanced Python implementation..."
    
    # Pass both issue number and temp file path to Python script
    uv run "$SCRIPT_PATH" "$ISSUE_NUMBER" "$TEMP_ISSUE_FILE"
    EXIT_CODE=$?

    # Cleanup temp file
    rm -f "$TEMP_ISSUE_FILE"

    if [[ $EXIT_CODE -eq 0 ]]; then
        echo "✅ Enhanced use case creation completed successfully"
        if [[ "$MCP_AVAILABLE" == "true" ]]; then
            echo "🎯 GitHub issue was analyzed with MCP enhancements:"
            echo "  📚 Serena: Historical patterns and optimization applied"
            echo "  🧠 Context7: Industry best practices integrated"
        else
            echo "🎯 GitHub issue was analyzed in standard mode"
        fi
    else
        echo "❌ Enhanced use case creation failed with exit code: $EXIT_CODE"
        exit $EXIT_CODE
    fi
else
    echo "❌ Enhanced implementation not found: $SCRIPT_PATH"
    echo "💡 Using direct Claude analysis with retrieved issue data..."
    echo ""
    echo "🚀 Starting enhanced use case creation with comprehensive GitHub issue analysis..."
    echo "📊 Issue Data Available:"
    echo "  - Original Description: ✅"
    echo "  - Comment History: ✅ ($COMMENT_COUNT comments)"
    echo "  - Latest Updates: ✅"
    if [[ "$MCP_AVAILABLE" == "true" ]]; then
        echo "  - MCP Analysis: ✅ (Enhanced mode)"
    else
        echo "  - MCP Analysis: ❌ (Standard mode)"
    fi
    echo ""
    echo "⏰ Ready for enhanced use case specification creation..."
    # Cleanup temp file
    rm -f "$TEMP_ISSUE_FILE"
fi
```

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Enhanced Requirements Analysis - Detailed Use Case Specification (03/16)  
> 🎯 **Phase Purpose**: Convert GitHub issues into comprehensive implementable specifications with MCP intelligence  
> ➡️ **Next Stage**: /04-domain-modeling-enhanced to design enhanced domain model from use cases

## 🎯 PHASE PURPOSE: ENHANCED USE CASE SPECIFICATION FROM GITHUB ISSUES

**⚠️ Important Notice:**

- **This step focuses on ENHANCED SPECIFICATION CREATION** - Convert GitHub issues into comprehensive Given-When-Then specifications with historical pattern analysis and industry best practices
- **NO IMPLEMENTATION** - Focus only on intelligent requirements analysis and specification design
- **GITHUB ISSUE INTEGRATION WITH MCP ENHANCEMENT** - Prioritize recent comments, analyze historical patterns, and apply industry standards

**What this enhanced step does:**

1. `/02-sprint-planning-enhanced` ← Sprint tickets with intelligent planning
2. `/create-use-case-enhanced <issue-number>` ← **【YOU ARE HERE】Create enhanced specifications with MCP intelligence**
3. `/04-domain-modeling-enhanced <issue-number>` ← Design enhanced domain model from use cases
4. Then proceed with enhanced TDD implementation workflow

**ANALYZE GITHUB ISSUES AND CREATE ENHANCED SPECIFICATIONS WITH MCP INSIGHTS. DO NOT IMPLEMENT CODE.**

## 📋 軽量コンテキスト管理

### Required Reading (Minimal + MCP Enhanced)

```bash
# Standard project state checks
if [[ -f "docs/metadata/project-state.json" ]]; then
    Read docs/metadata/project-state.json
fi

# Project vision and bounded context for consistency
if [[ -f "docs/vision/vision.md" ]]; then
    Read docs/vision/vision.md
fi

if [[ -f "docs/vision/bounded_context.md" ]]; then
    Read docs/vision/bounded_context.md
fi

# MCP Enhanced: Historical use case patterns (if available)
if [[ "$MCP_AVAILABLE" == "true" ]]; then
    echo "🔍 Enhanced Analysis Mode: MCP capabilities enabled"
    echo "  📚 Serena: Analyzing historical use case patterns and optimizations"
    echo "  🧠 Context7: Integrating latest requirements engineering best practices"
else
    echo "📋 Standard Mode: Basic use case creation without MCP enhancements"
fi
```

### GitHub Issue Integration (Enhanced)

```bash
# Enhanced issue-driven use case creation
echo "📥 Loading GitHub issue #$ISSUE_NUMBER for enhanced analysis..."

# Standard issue data extraction
echo "📋 Issue Title: $(echo "$ISSUE_DATA" | jq -r '.title')"
echo "📋 Issue Body Analysis:"
echo "$(echo "$ISSUE_DATA" | jq -r '.body'))" | head -20
echo "📋 Labels: $(echo "$ISSUE_DATA" | jq -r '.labels[].name' | tr '\n' ', ')"

# Enhanced comment timeline analysis
if [[ $COMMENT_COUNT -gt 0 ]]; then
    echo "📊 Processing enhanced comment timeline..."
    echo "$RECENT_COMMENTS" | jq -r '.[] | "[\\(.createdAt)] \\(.author.login): \\(.body[0:100])..."'
    
    # MCP Enhanced: Pattern analysis
    if [[ "$MCP_AVAILABLE" == "true" ]]; then
        echo "🔍 Enhanced: Cross-referencing comment patterns with historical data..."
        echo "📊 Enhanced: Applying requirements engineering best practices..."
    fi
fi
```

## 🚀 Enhanced Expert Execution Flow

### Phase 1: Enhanced GitHub Issue Analysis

**Analyze the following as an enhanced expert (user interactions in Japanese):**

1. **Enhanced Comprehensive Issue Understanding**

   ```bash
   # Enhanced analysis with MCP insights
   if [[ "$MCP_AVAILABLE" == "true" ]]; then
       echo "🧠 MCP拡張モード: インテリジェント要求分析"
       echo "📊 履歴パターン分析と業界標準を活用して最適化された仕様を作成します"
   fi
   ```

   Enhanced analysis includes:
   - Issue requirements with historical pattern validation (MCP Enhanced)
   - Comment evolution analysis with best practice alignment (MCP Enhanced)
   - Stakeholder intent clarification with industry standard techniques

2. **MCP-Enhanced Specification Evolution Analysis**

   - Historical use case pattern matching using Serena MCP
   - Requirements engineering best practice application using Context7 MCP
   - Cross-reference analysis for dependency identification
   - Intelligent gap detection and specification enhancement

### Phase 2: Enhanced Domain Concept Extraction

**Execute enhanced domain analysis:**

1. **MCP-Enhanced Concept Discovery**

   ```bash
   # Enhanced concept analysis with MCP insights
   if [[ "$MCP_AVAILABLE" == "true" ]]; then
       echo "🔍 Enhanced Concept Discovery:"
       echo "  • Serena: Mining successful domain patterns from historical projects"
       echo "  • Context7: Applying latest domain modeling and requirements techniques"
       echo "  • Integration: Creating optimized concept framework with validation"
   fi
   ```

2. **Intelligent Ubiquitous Language Integration**

   - New concept identification with pattern validation (MCP Enhanced)
   - Consistency verification with historical language patterns (MCP Enhanced)
   - Industry standard terminology integration (Context7 Enhanced)
   - Cross-project concept alignment and optimization

### Phase 3: Enhanced Scenario Design

**Design enhanced scenario structure:**

1. **MCP-Enhanced Given-When-Then Creation**

   - Main scenarios with historical success pattern validation
   - Alternative flows enhanced with industry best practice patterns
   - Exception scenarios optimized with historical failure pattern analysis
   - Cross-reference scenario dependencies with intelligent mapping

2. **Intelligent Acceptance Test Design**

   - Test case generation with historical coverage analysis
   - Edge case identification using pattern recognition
   - Automated test strategy with industry standard practices
   - Quality metrics integration with benchmark standards

### Phase 4: Enhanced Documentation Generation

**Create enhanced use case documentation:**

1. **Enhanced Specification Document**

   - Requirements analysis with historical pattern insights
   - Enhanced scenarios with industry standard validation
   - Cross-reference documentation with dependency analysis
   - Quality metrics with benchmark comparison

2. **Enhanced Test Documentation**

   - Intelligent test case design with coverage optimization
   - Historical failure pattern mitigation strategies
   - Industry standard test practices integration
   - Automated testing preparation with best practice guidance

## ✅ Enhanced Built-in Quality Assurance

### Enhanced Self-Diagnostic Checklist

**Mandatory Items (MUST) - Enhanced:**

- [ ] All GitHub issue requirements converted to Given-When-Then scenarios with pattern validation
- [ ] Comment history analyzed with latest specifications and best practices reflected (MCP Enhanced)
- [ ] Historical use case patterns identified and applied where beneficial (MCP Enhanced)
- [ ] Industry standard requirements techniques integrated (MCP Enhanced)
- [ ] Cross-reference dependencies mapped and documented (MCP Enhanced)

**Recommended Items (SHOULD) - Enhanced:**

- [ ] Historical success patterns applied to scenario design (MCP Enhanced)
- [ ] Requirements engineering best practices integrated (MCP Enhanced)
- [ ] Domain concept optimization based on pattern analysis
- [ ] Test strategy enhanced with industry standards
- [ ] Quality metrics aligned with benchmark standards

### Enhanced Quality Metrics

| Indicator | Target Value | Enhanced Target | Actual Value | Result |
|-----------|-------------|-----------------|--------------|---------|
| Scenario Completeness Rate | 100% | 100% (Pattern Validated) | [Completion %] | ✅/❌ |
| Historical Pattern Coverage | N/A | 90% (MCP Enhanced) | [Coverage %] | ✅/❌ |
| Best Practice Integration | N/A | 85% (Context7) | [Integration %] | ✅/❌ |
| Cross-Reference Accuracy | 90% | 95% (MCP Enhanced) | [Accuracy %] | ✅/❌ |

## 📊 Enhanced Standardized Output Format

### Enhanced 実行サマリー

- ✅ **Issue分析**: [分析完了したIssue情報とコメント数] (MCP拡張: パターン分析統合)
- ✅ **シナリオ作成**: [作成されたメイン/代替/例外シナリオ数] (履歴パターン検証付き)
- ✅ **受け入れ基準**: [定義された受け入れ基準数とテストケース数] (業界標準準拠)
- ✅ **MCP分析**: [実行された拡張分析項目数]

### Enhanced 成果物

**作成されたファイル (MCP Enhanced):**

- `docs/use_cases/sprints/sprint-*/issue-<number>/specification.md`: パターン分析統合ユースケース仕様書
- `docs/use_cases/sprints/sprint-*/issue-<number>/scenarios.md`: 履歴検証Given-When-Thenシナリオ集
- `docs/use_cases/sprints/sprint-*/issue-<number>/domain_concepts.md`: 最適化ドメイン概念定義
- `docs/use_cases/sprints/sprint-*/issue-<number>/acceptance_tests.md`: 業界標準受け入れテストケース
- `docs/use_cases/sprints/sprint-*/issue-<number>/pattern_analysis.md`: Serenaパターン分析レポート (MCP Enhanced)
- `docs/use_cases/sprints/sprint-*/issue-<number>/best_practices.md`: Context7ベストプラクティス統合 (MCP Enhanced)
- `docs/vision/ubiquitous_language.md`: パターン検証ユビキタス言語辞書

### Enhanced 次のステップ

1. **即座に実行可能**: 
   - `/04-domain-modeling-enhanced <issue-number>` でパターン分析統合ドメインモデル設計
   - `/05-create-tests-enhanced <issue-number>` でインテリジェント・テスト設計
2. **戦略的推奨**: 
   - MCP拡張機能を活用した継続的要求分析最適化の実施
   - 履歴パターン学習システムの構築検討

### Enhanced メタデータ更新

```json
{
  "command_executed": "03-create-use-case-enhanced",
  "timestamp": "[ISO-8601 timestamp]",
  "status": "[SUCCESS|PARTIAL|FAILED]",
  "phase": "enhanced-use-case-specification",
  "issue_number": "[issue-number]",
  "mcp_enhancements": {
    "serena_pattern_analysis": true,
    "context7_best_practices": true,
    "historical_pattern_mining": true,
    "cross_reference_analysis": true
  },
  "deliverables": {
    "specification": "docs/use_cases/sprints/sprint-*/issue-<number>/specification.md",
    "scenarios": "docs/use_cases/sprints/sprint-*/issue-<number>/scenarios.md",
    "domain_concepts": "docs/use_cases/sprints/sprint-*/issue-<number>/domain_concepts.md",
    "acceptance_tests": "docs/use_cases/sprints/sprint-*/issue-<number>/acceptance_tests.md",
    "pattern_analysis": "docs/use_cases/sprints/sprint-*/issue-<number>/pattern_analysis.md",
    "best_practices": "docs/use_cases/sprints/sprint-*/issue-<number>/best_practices.md"
  },
  "metrics": {
    "scenarios_created": "[main/alternative/exception count]",
    "acceptance_criteria": "[number]",
    "test_cases": "[number]",
    "domain_concepts_added": "[number]",
    "historical_patterns_applied": "[number]",
    "best_practices_integrated": "[number]"
  },
  "next_recommended": ["04-domain-modeling-enhanced", "05-create-tests-enhanced"],
  "quality_score": "[score]",
  "pattern_coverage_score": "[score]"
}
```

---

🎯 MCP拡張ユースケース仕様作成を開始します。要求分析エキスパートとして、履歴パターン分析と業界標準を活用した包括的な仕様設計を実施いたします。

**使用方法**:

```bash
/03-create-use-case-enhanced <issue-number>

# 例
/03-create-use-case-enhanced 123
```

**MCP拡張機能** (利用可能時):
- 📚 **Serena**: 履歴ユースケース分析・パターン発見・最適化推奨
- 🧠 **Context7**: 最新要求分析手法・業界標準・ベストプラクティス統合