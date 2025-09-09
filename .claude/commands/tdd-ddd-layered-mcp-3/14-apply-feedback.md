# 14-apply-feedback-enhanced (MCP-Enhanced Feedback Application)

## 🎯 Expert Profile Declaration

**TDD/DDD/Layered Architecture Expert** specializing in strategic feedback application with **MCP-3 Complex Analysis Integration**.

**Core Expertise**: Strategic feedback analysis, priority-based improvement implementation, quality metrics enhancement, systematic technical debt reduction
**MCP-3 Enhancement**: Sequential thinking for complex improvement analysis, Context7 feedback patterns, Serena comprehensive impact analysis
**Specialized Skills**: Multi-layer improvement prioritization, systematic quality enhancement, strategic feedback implementation planning

**Language Guidelines:**

- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

## 🎯 Purpose and Scope

Conduct strategic feedback application with **MCP-3 Complex Analysis** for systematic quality improvement and technical debt reduction. This command applies **Sequential MCP for complex strategic analysis** when dealing with multi-component feedback implementation requiring systematic prioritization and cross-layer impact assessment.

### Your Expertise

**Strategic Feedback Application Capabilities:**
- Multi-source feedback analysis and strategic prioritization
- Cross-layer impact assessment and improvement planning
- Technical debt reduction with architectural compliance verification
- Quality metrics enhancement with comprehensive validation

**MCP-3 Enhanced Analysis:**
- Sequential thinking for complex improvement decomposition
- Context7 latest feedback application methodologies and patterns
- Serena comprehensive code analysis and change impact evaluation
- Strategic improvement roadmap with intelligent prioritization

---

## 📍 Process Context

### Position in TDD/DDD/Layered Workflow

```
📋 Current Position: /apply-feedback-enhanced
├── 00-13. [Development cycle] ← Implementation completed with review
├── 14. apply-feedback ← **Current: Strategic feedback application**
├── 15. create-pr ← Next: Pull request creation and finalization
├── 16. status-report ← Final: Status reporting and completion
```

**Previous Phase**: Implementation review with strategic improvement recommendations
**Current Phase**: Strategic feedback application and quality enhancement
**Next Phase**: Pull request preparation with comprehensive validation

---

## 🔧 Complexity & MCP Integration Assessment

**Task Complexity Analysis**:
- **Strategic Improvement Planning**: Multi-component feedback requires strategic analysis and prioritization
- **Cross-Layer Impact**: Feedback application affects Domain, UseCase, Infrastructure, and Presentation layers
- **Systematic Approach Needed**: Complex quality metrics, technical debt analysis, and improvement sequencing
- **Multi-Component Validation**: Quality enhancement requires comprehensive testing and validation across layers

**→ Sequential MCP Recommended for Complex Strategic Analysis**

```bash
#!/bin/bash

echo "🚀 Apply Feedback Enhanced with Intelligent MCP Integration..."

# Issue number validation
if [[ -z "$1" ]]; then
    echo "❌ ERROR: Issue number required. Usage: /apply-feedback-enhanced <issue-number>"
    exit 1
fi

ISSUE_NUMBER="$1"
echo "📊 Analyzing task complexity and requirements..."
echo "🎯 Target: Issue #$ISSUE_NUMBER strategic feedback application"
echo "🧩 Complex strategic task detected - Using Sequential MCP for systematic analysis"

echo "🔧 Checking MCP availability..."

# MCP availability check (standard pattern)
if command -v mcp__serena__think_about_collected_information &> /dev/null; then
    echo "✅ Serena MCP available"
    MCP_SERENA="available"
else
    echo "ℹ️ Serena MCP not found - standard mode"
    MCP_SERENA="unavailable"
fi

if command -v mcp__context7__resolve-library-id &> /dev/null; then
    echo "✅ Context7 MCP available"
    MCP_CONTEXT7="available"
else
    echo "ℹ️ Context7 MCP not found - standard mode"
    MCP_CONTEXT7="unavailable"
fi

if command -v mcp__sequential-thinking__sequentialthinking &> /dev/null; then
    echo "✅ Sequential MCP available"
    MCP_SEQUENTIAL="available"
else
    echo "ℹ️ Sequential MCP not found - standard logic mode"
    MCP_SEQUENTIAL="unavailable"
fi

# GitHub Issue Requirements Loading (Simple & Comment-Focused)
echo "📋 Loading GitHub issue requirements..."

if command -v gh &> /dev/null; then
    ISSUE_DATA=$(gh issue view $ISSUE_NUMBER --json title,body,comments,updatedAt 2>/dev/null)
    
    if [[ $? -eq 0 ]]; then
        echo "✅ GitHub issue #$ISSUE_NUMBER loaded"
        
        # Simple comment analysis with recency priority
        COMMENT_COUNT=$(echo "$ISSUE_DATA" | jq '.comments | length // 0')
        
        if [[ $COMMENT_COUNT -gt 0 ]]; then
            echo "📊 Found $COMMENT_COUNT comments"
            echo "⚠️ PRIORITY: Recent comments contain the most current requirements"
            echo "📅 Implementation should prioritize latest comment content over original description"
            
            # Display recent comments summary (simple)
            echo "📋 Latest Comments (most recent first):"
            echo "$ISSUE_DATA" | jq -r '.comments | sort_by(.updatedAt) | reverse | .[0:3] | .[] | "  💬 [\(.updatedAt)] @\(.author.login): \(.body | split("\n")[0] | .[0:100])..."
        else
            echo "📝 No comments found - using original issue description"
        fi
        
        # Display issue summary
        echo "📄 Issue: $(echo "$ISSUE_DATA" | jq -r '.title')"
        echo "📅 Last Updated: $(echo "$ISSUE_DATA" | jq -r '.updatedAt')"
        
    else
        echo "⚠️ GitHub CLI failed - falling back to specification files"
    fi
else
    echo "ℹ️ GitHub CLI not available - using specification files"
fi

echo "🎯 Proceeding with implementation based on latest requirements..."

# Create feedback workspace directories
mkdir -p docs/feedback
mkdir -p docs/quality-improvement
mkdir -p tests/feedback-validation

echo "✅ MCP-3 Strategic feedback application environment ready"
echo ""
```

---

## 🧠 Intelligent Execution Flow

**Execute strategic feedback application using MCP-3 integration:**

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

**🧠 MCP Enhancement**: Serena (Code Analysis + Feedback Mining) + Context7 (Improvement Patterns + Best Practices)

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Feedback Application Phase (14/16) **[MCP-Enhanced Version]**  
> 🎯 **Phase Purpose**: Systematic application of review feedback with MCP intelligence  
> ⬅️ **Previous Stage**: 13-review-issue (Implementation Review) or 13-review-issue-enhanced  
> ➡️ **Next Stage**: 15-create-pr (Pull Request Creation)

### Phase 1: Strategic Analysis with Sequential MCP

```bash
# Complex strategic analysis using Sequential MCP
if [[ "$MCP_SEQUENTIAL" == "available" ]]; then
    echo "🧩 Executing complex strategic feedback application analysis..."
    
    # Use Sequential MCP for systematic feedback application analysis
    Use mcp__sequential-thinking__sequentialthinking to systematically analyze:
    "Strategic feedback application for issue #$ISSUE_NUMBER with multi-layer improvement planning:
    
    1. Feedback Pattern Analysis:
       - Analyze collected feedback from review reports and quality assessments
       - Categorize feedback by impact, complexity, and implementation priority
       - Identify cross-layer dependencies and improvement opportunities
    
    2. Strategic Improvement Planning:
       - Prioritize improvements by business value and technical impact
       - Assess architectural compliance and technical debt reduction potential
       - Create systematic implementation sequence with risk mitigation
    
    3. Quality Enhancement Strategy:
       - Design comprehensive quality improvement approach
       - Plan testing and validation strategy for each improvement
       - Establish quality metrics and success criteria
    
    4. Cross-Component Impact Analysis:
       - Analyze improvement impact across Domain, UseCase, Infrastructure, Presentation
       - Identify integration points requiring coordinated changes
       - Plan rollback and recovery strategies for high-risk improvements"
       
else
    echo "📋 Sequential MCP unavailable - using structured manual approach"
    echo "🧩 Complex task requires systematic analysis with step-by-step checklists"
fi
```

### Phase 2: Code Analysis with Serena MCP

```bash
# Project structure and improvement analysis
if [[ "$MCP_SERENA" == "available" ]]; then
    echo "🔍 Analyzing feedback implementation and improvement opportunities..."
    
    # Analyze current state and improvement areas
    Use mcp__serena__get_symbols_overview to understand current implementation status
    Use mcp__serena__search_for_pattern "TODO|FIXME|XXX|BUG|HACK|deprecated|refactor" to identify technical debt
    Use mcp__serena__search_for_pattern "test_|Test|@pytest.mark|def.*test" to analyze test coverage areas
    
    # Issue-specific feedback analysis
    Use mcp__serena__find_symbol "issue-${ISSUE_NUMBER}" to locate issue-specific implementations
    
    # Document findings
    Use mcp__serena__write_memory "feedback-application-${ISSUE_NUMBER}" "{
      \"feedback_analysis\": \"comprehensive feedback application for issue ${ISSUE_NUMBER}\",
      \"improvement_opportunities\": \"systematic quality enhancement and technical debt reduction\", 
      \"implementation_strategy\": \"priority-based improvement with comprehensive validation\",
      \"quality_enhancement\": \"strategic improvement roadmap with cross-layer impact analysis\"
    }"
    
else
    echo "📋 Running without code analysis - manual analysis required"
fi
```

### Phase 3: Quality Enhancement with Context7 MCP

```bash
# Latest feedback application patterns and improvement methodologies
if [[ "$MCP_CONTEXT7" == "available" ]]; then
    echo "📚 Applying latest feedback application and quality improvement patterns..."
    
    # Get latest feedback application methodologies
    Use mcp__context7__resolve-library-id "feedback-driven-development"
    Use mcp__context7__get-library-docs "/feedback-application/patterns" --topic "systematic-improvement"
    Use mcp__context7__get-library-docs "/quality-enhancement/methodologies" --topic "technical-debt-reduction"
    Use mcp__context7__get-library-docs "/code-improvement/strategies" --topic "incremental-enhancement"
    
else
    echo "📚 Running without latest patterns - using standard approaches"
fi
```

---

### Phase 4: Implementation Analysis & Quality Assessment

**Execute comprehensive feedback application based on MCP analysis:**

```bash
echo "🔍 Executing feedback application and quality enhancement..."

# 1. Feedback artifact verification
echo "📄 Verifying feedback and review artifacts..."

# Check for issue-specific review and feedback documentation
REVIEW_REPORT="docs/review/issue-${ISSUE_NUMBER}-review.md"
QUALITY_DASHBOARD="docs/quality-reports/issue-${ISSUE_NUMBER}-quality-dashboard.md"

if [[ -f "$REVIEW_REPORT" ]]; then
    echo "✅ Review report found for Issue #$ISSUE_NUMBER"
    # Use Read tool to analyze review feedback
else
    echo "⚠️ Review report not found: $REVIEW_REPORT"
fi

if [[ -f "$QUALITY_DASHBOARD" ]]; then
    echo "✅ Quality dashboard found"
    # Use Read tool to analyze quality metrics
else
    echo "⚠️ Quality dashboard not found: $QUALITY_DASHBOARD"
fi

# 2. Baseline quality metrics capture
echo "📊 Capturing baseline quality metrics..."

# Test coverage baseline
if command -v uv &> /dev/null; then
    echo "🧪 Running baseline test coverage analysis..."
    Use Bash tool: PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest --cov=src --cov=domain --cov=application --cov=infrastructure --cov=presentation --cov-report=json --cov-report=term-missing > tests/feedback-validation/baseline-coverage-${ISSUE_NUMBER}.txt 2>&1 || echo "Baseline coverage analysis completed"
fi

# Code quality baseline
if command -v ruff &> /dev/null; then
    echo "🔍 Running baseline code quality analysis..."
    Use Bash tool: uv run --frozen ruff check . --output-format=json > tests/feedback-validation/baseline-ruff-${ISSUE_NUMBER}.json 2>&1 || echo "Baseline quality analysis completed"
fi

# Type checking baseline
if command -v pyright &> /dev/null; then
    echo "🔬 Running baseline type checking analysis..."
    Use Bash tool: uv run --frozen pyright --outputformat=json > tests/feedback-validation/baseline-pyright-${ISSUE_NUMBER}.json 2>&1 || echo "Baseline type checking completed"
fi

echo "✅ Quality assessment execution completed"
```

### Phase 5: Report Generation & Documentation

```bash
echo "📝 Creating comprehensive feedback application reports..."

# Main feedback application report
FEEDBACK_REPORT_FILE="docs/feedback/issue-${ISSUE_NUMBER}-feedback-application.md"
Write "$FEEDBACK_REPORT_FILE" with:
# - Strategic analysis results from Sequential MCP
# - Feedback categorization and prioritization with impact analysis
# - Implementation approach and systematic methodology
# - Quality metrics improvement tracking with before/after comparison
# - Risk assessment and mitigation strategies with lessons learned
# - Cross-layer architectural impact analysis with dependency mapping

# Quality improvement metrics report
QUALITY_METRICS_FILE="docs/feedback/issue-${ISSUE_NUMBER}-quality-metrics.md"
Write "$QUALITY_METRICS_FILE" with:
# - Comprehensive quality metrics comparison with trend analysis
# - Test coverage improvement tracking with detailed breakdown
# - Code quality scores with improvement measurement
# - Performance and maintainability enhancement results
# - Technical debt reduction achievements with strategic planning

echo "✅ Strategic feedback application documentation completed"
```

### Phase 6: GitHub Integration & Project Updates

```bash
echo "🔗 Updating GitHub issue and project documentation..."

# GitHub issue comment with feedback application results
if command -v gh &> /dev/null; then
    FEEDBACK_SUMMARY="✅ 戦略的フィードバック適用完了 - Issue #${ISSUE_NUMBER}

📊 **品質改善結果**:
- 🧪 テストカバレッジ: [改善前]% → [改善後]% (+[改善度]%)
- 🔍 コード品質スコア: [改善前] → [改善後] (-[改善件数]件)
- 🔬 型安全性: [改善前] → [改善後] (+[改善度]%)
- ⚡ パフォーマンス: [最適化項目数]件の最適化適用

📁 **詳細レポート**:
- [フィードバック適用レポート](docs/feedback/issue-${ISSUE_NUMBER}-feedback-application.md)
- [品質改善メトリクス](docs/feedback/issue-${ISSUE_NUMBER}-quality-metrics.md)"
    
    if [[ "$MCP_SEQUENTIAL" == "available" ]]; then
        FEEDBACK_SUMMARY="$FEEDBACK_SUMMARY

🧠 **MCP-3戦略的分析**:
- Sequential MCP: 複合戦略分析で包括的改善計画生成
- Serena MCP: 実装パターン解析と改善機会発見
- Context7 MCP: 最新フィードバック適用手法適用"
    fi
    
    FEEDBACK_SUMMARY="$FEEDBACK_SUMMARY

🚀 **次のステップ**:
プルリクエスト作成準備完了。"
    
    Use Bash tool: gh issue comment "${ISSUE_NUMBER}" --body "$FEEDBACK_SUMMARY"
fi

echo "💾 Recording results and learning insights..."

# Commit feedback application documentation
Use Bash tool: git add docs/feedback/ tests/feedback-validation/

if [[ "$MCP_SEQUENTIAL" == "available" ]]; then
    Use Bash tool: git commit -m "feat: apply comprehensive feedback for issue ${ISSUE_NUMBER} with MCP-3 strategic analysis

Systematic feedback application with Sequential MCP strategic planning.
Quality metrics enhancement with comprehensive validation and testing.
MCP-3 enhanced analysis with pattern recognition and intelligent optimization.

🎯 Generated with Claude Code"
else
    Use Bash tool: git commit -m "feat: apply comprehensive feedback for issue ${ISSUE_NUMBER}

Systematic feedback application with priority-based improvement implementation.
Quality metrics enhancement with comprehensive validation and testing.

🎯 Generated with Claude Code"
fi

echo "✅ Strategic feedback application completed with MCP-3 intelligence"
```

---

## ✅ Quality Assurance & Learning

### Execution Validation

```bash
echo "🔍 Validating feedback application quality..."

# MCP Integration Quality Check
if [[ "$MCP_SEQUENTIAL" == "available" ]]; then
    echo "✅ Sequential MCP strategic analysis completed"
    Use mcp__serena__think_about_collected_information
else
    echo "ℹ️ Manual strategic analysis completed with structured approach"
fi

if [[ "$MCP_SERENA" == "available" ]]; then
    echo "✅ Serena MCP code analysis completed"
fi

if [[ "$MCP_CONTEXT7" == "available" ]]; then
    echo "✅ Context7 MCP pattern integration completed"
fi

echo "📊 Quality validation completed"
```

### Learning & Improvement

```bash
# Record execution insights for continuous improvement
if [[ "$MCP_SERENA" == "available" ]]; then
    Use mcp__serena__write_memory "feedback-application-insights-$(date +%Y%m%d)" "{
      \"approach_effectiveness\": \"MCP-3 strategic feedback application approach\",
      \"sequential_integration_results\": \"systematic analysis outcomes\", 
      \"improvement_opportunities\": [\"enhanced feedback pattern mining\", \"deeper quality impact analysis\"],
      \"user_feedback\": \"feedback application execution feedback\"
    }"
fi

echo "💾 Learning insights recorded for continuous improvement"
```

### Self-Diagnosis Checklist

**Core Quality Standards (MUST):**
- [ ] Feedback systematically applied based on priority and impact analysis
- [ ] Quality metrics improvement achieved and documented comprehensively
- [ ] Test coverage maintained or improved after feedback application
- [ ] All changes properly validated with comprehensive testing
- [ ] Documentation updated to reflect applied improvements and lessons learned
- [ ] GitHub issue updated with improvement results (if GitHub integration available)

**MCP-3 Enhancement Standards (SHOULD when available):**
- [ ] Sequential MCP applied for strategic analysis
- [ ] Serena MCP utilized for code pattern analysis
- [ ] Context7 MCP consulted for feedback best practices
- [ ] Systematic decomposition and impact assessment completed

---

## 📊 Standardized Output

### 実行サマリー (日本語でユーザーに報告)

**基本フィードバック適用 (常に実行):**
- ✅ **フィードバック分析**: Issue #${ISSUE_NUMBER} の包括的フィードバック収集・分析完了
- ✅ **品質改善実装**: 優先度ベース改善実装・品質メトリクス向上完了
- ✅ **検証・文書化**: 包括的検証・詳細文書化・GitHub Issue更新完了
- ✅ **改善レポート**: フィードバック適用結果と品質改善メトリクスレポート作成完了

**MCP-3戦略的強化 (利用可能時):**
- ✅ **Sequential MCP戦略分析**: 複合分析で戦略的改善計画生成
- ✅ **Serena MCP 品質解析**: 包括的品質分析と改善機会発見
- ✅ **Context7最新パターン**: 最新フィードバック適用手法適用
- ✅ **戦略改善ロードマップ**: 長期品質改善計画生成

### 生成ファイル

**基本ファイル:**
- `docs/feedback/issue-${ISSUE_NUMBER}-feedback-application.md`: 戦略的フィードバック適用詳細レポート
- `docs/feedback/issue-${ISSUE_NUMBER}-quality-metrics.md`: 包括的品質改善メトリクスレポート
- `tests/feedback-validation/baseline-*-${ISSUE_NUMBER}.*`: ベースライン品質メトリクス
- `tests/feedback-validation/final-*-${ISSUE_NUMBER}.*`: 最終品質メトリクス

**MCP-3拡張 (利用時):**
- Enhanced analysis with Sequential MCP strategic insights
- Serena MCP memory updates for continuous learning
- Context7 pattern-enhanced documentation

### 総合判定

**ステータス**: `SUCCESS` (基本) / `MCP3_STRATEGIC_SUCCESS` (MCP-3利用時)
**フィードバック適用品質**: [スコア]/100
**MCP-3統合効果**: [スコア]/100 (利用時のみ)
**次フェーズ準備**: `READY`

### 次のステップ案内

1. **即座実行可能**: `/create-pr-enhanced` でプルリクエスト作成開始
2. **推奨**: フィードバック適用結果の詳細確認と最終調整
3. **確認推奨**: 品質改善メトリクスレポートでの改善効果確認

**完了メッセージ:**

```
🎉 MCP-3戦略的フィードバック適用完了！

🔄 基本フィードバック適用:
   ✅ フィードバック分析: Issue #${ISSUE_NUMBER}包括分析
   ✅ 品質改善実装: 優先度ベース改善・検証完了
   ✅ 文書化・報告: 詳細レポート・GitHub Issue更新
   ✅ 品質向上: メトリクス改善・包括的検証完了

🧠 MCP-3戦略強化 (利用時):
   🧩 Sequential MCP: 複合戦略分析完了
   🔍 Serena MCP: 品質解析・改善機会発見
   📚 Context7 MCP: 最新適用手法適用完了
   📈 戦略ロードマップ: 長期品質改善計画生成

📁 成果物:
   ✅ docs/feedback/issue-${ISSUE_NUMBER}-feedback-application.md
   ✅ docs/feedback/issue-${ISSUE_NUMBER}-quality-metrics.md

🎯 次のアクション:
   /create-pr-enhanced

✅ 戦略的フィードバック適用完了 - プルリクエスト準備万全！
```

