# /review-issue-enhanced [issue-number] - MCP-3統合戦略的実装レビュー

## 🎯 Expert Profile Declaration

**TDD/DDD/Layered Architecture Expert** specializing in strategic implementation review with **MCP-3 Complex Analysis Integration**.

**Core Expertise**: Implementation quality assessment, architectural compliance verification, technical debt analysis, strategic improvement planning
**MCP-3 Enhancement**: Sequential thinking for complex quality analysis, Context7 review patterns, Serena cross-layer analysis  
**Specialized Skills**: Multi-layer quality evaluation, systematic improvement prioritization, strategic technical debt management

## 🎯 Purpose and Scope

Conduct strategic implementation review with **MCP-3 Complex Analysis** for comprehensive quality assessment and improvement planning. This command applies **Sequential MCP for complex strategic analysis** when dealing with multi-layer implementation review requiring systematic decomposition and cross-domain quality evaluation.

### Your Expertise

**Strategic Review Capabilities:**
- Multi-layer implementation quality assessment
- Architectural compliance verification across all layers  
- Technical debt analysis and strategic prioritization
- Cross-domain quality evaluation and improvement planning

**MCP-3 Enhanced Analysis:**
- Sequential thinking for complex quality decomposition
- Context7 latest review methodologies and industry patterns
- Serena comprehensive code analysis and pattern recognition
- Strategic improvement roadmap with intelligent prioritization

---

## 📍 Process Context

### Position in TDD/DDD/Layered Workflow

```
📋 Current Position: /review-issue-enhanced
├── 00-12. [Development cycle] ← Implementation completed with documentation
├── 13. review-issue ← **Current: Strategic implementation review**
├── 14. apply-feedback ← Next: Apply strategic improvement recommendations
├── 15-16. [PR and status] ← Completion and reporting
```

**Previous Phase**: Implementation cycle completion with evolved scenarios
**Current Phase**: Strategic quality assessment and improvement planning  
**Next Phase**: Implementation of strategic improvement recommendations

---

## 🔧 Complexity & MCP Integration Assessment

**Task Complexity Analysis**:
- **Strategic Quality Assessment**: Multi-layer implementation quality evaluation requires strategic analysis
- **Cross-Domain Analysis**: Quality spans Domain, UseCase, Infrastructure, and Presentation layers
- **Systematic Approach Needed**: Complex quality metrics, technical debt analysis, and improvement prioritization  
- **Multi-Component Integration**: Implementation review affects architecture decisions across all layers

**→ Sequential MCP Recommended for Complex Strategic Analysis**

```bash
#!/bin/bash

echo "🚀 Review Issue Enhanced with Intelligent MCP Integration..."

# Issue number validation
if [[ -z "$1" ]]; then
    echo "❌ ERROR: Issue number required. Usage: /review-issue-enhanced <issue-number>"
    exit 1
fi

ISSUE_NUMBER="$1"
echo "📊 Analyzing task complexity and requirements..."
echo "🎯 Target: Issue #$ISSUE_NUMBER strategic implementation review"
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
            echo "$ISSUE_DATA" | jq -r '.comments | sort_by(.updatedAt) | reverse | .[0:3] | .[] | "  💬 [\(.updatedAt)] @\(.author.login): \(.body | split("\n")[0] | .[0:100])..."'
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

# Create review workspace directories
mkdir -p docs/review
mkdir -p docs/quality-reports
mkdir -p tests/coverage-reports

echo "✅ MCP-3 Strategic implementation review environment ready"
echo ""
```

---

## 🧠 Intelligent Execution Flow

**Execute strategic implementation review using MCP-3 integration:**

### Phase 1: Strategic Analysis with Sequential MCP

```bash
# Complex strategic analysis using Sequential MCP
if [[ "$MCP_SEQUENTIAL" == "available" ]]; then
    echo "🧩 Executing complex strategic implementation review analysis..."
    
    # Use Sequential MCP for systematic implementation review
    Use mcp__sequential-thinking__sequentialthinking to systematically analyze:
    "Strategic implementation review for issue #$ISSUE_NUMBER with multi-layer quality assessment:
    
    1. Implementation Completeness Assessment:
       - Verify all architectural layers are implemented
       - Check Domain, UseCase, Infrastructure, Presentation layer artifacts
       - Analyze alignment with original specifications
    
    2. Quality Metrics Analysis:
       - Evaluate test coverage across all layers
       - Assess code quality metrics and standards compliance
       - Identify technical debt and improvement opportunities
    
    3. Architectural Compliance Verification:
       - Validate Clean Architecture dependency rules
       - Check TDD/DDD implementation patterns
       - Assess separation of concerns and layer responsibilities
    
    4. Strategic Improvement Planning:
       - Prioritize identified issues by impact and complexity
       - Create systematic improvement roadmap
       - Plan technical debt management strategy"
       
else
    echo "📋 Sequential MCP unavailable - using structured manual approach"
    echo "🧩 Complex task requires systematic analysis with step-by-step checklists"
fi
```

### Phase 2: Code Analysis with Serena MCP

```bash
# Project structure and implementation analysis
if [[ "$MCP_SERENA" == "available" ]]; then
    echo "🔍 Analyzing implementation structure and patterns..."
    
    # Analyze implementation completeness
    Use mcp__serena__get_symbols_overview to understand project implementation structure
    Use mcp__serena__search_for_pattern "class.*Entity|class.*ValueObject|class.*Service|class.*Repository" to find domain patterns
    Use mcp__serena__search_for_pattern "test_|Test|@pytest.mark|def.*test" to analyze test coverage
    Use mcp__serena__search_for_pattern "TODO|FIXME|XXX|BUG|HACK" to identify technical debt
    
    # Issue-specific implementation analysis
    Use mcp__serena__find_symbol "issue-${ISSUE_NUMBER}" to locate issue-specific implementations
    
    # Document findings
    Use mcp__serena__write_memory "implementation-review-${ISSUE_NUMBER}" "{
      \"review_analysis\": \"comprehensive implementation review for issue ${ISSUE_NUMBER}\",
      \"quality_assessment\": \"multi-layer quality evaluation and compliance verification\", 
      \"technical_debt_analysis\": \"systematic technical debt identification and prioritization\",
      \"improvement_strategy\": \"strategic improvement recommendations with implementation roadmap\"
    }"
    
else
    echo "📋 Running without code analysis - manual analysis required"
fi
```

### Phase 3: Quality Assessment with Context7 MCP

```bash
# Latest code review patterns and quality methodologies
if [[ "$MCP_CONTEXT7" == "available" ]]; then
    echo "📚 Applying latest code review and quality assessment patterns..."
    
    # Get latest code review methodologies
    Use mcp__context7__resolve-library-id "code-review-best-practices"
    Use mcp__context7__get-library-docs "/code-review/methodologies" --topic "implementation-review"
    Use mcp__context7__get-library-docs "/quality-assessment/patterns" --topic "technical-debt-analysis"
    Use mcp__context7__get-library-docs "/architecture/compliance" --topic "clean-architecture-verification"
    
else
    echo "📚 Running without latest patterns - using standard approaches"
fi
```

### Phase 4: Implementation Analysis & Quality Assessment

**Execute comprehensive implementation review based on MCP analysis:**

```bash
echo "🔍 Executing implementation analysis and quality assessment..."

# 1. Implementation artifact verification
echo "📄 Verifying implementation artifacts..."

# Check for issue-specific documentation
USE_CASE_FILES=$(find docs/use_cases -name "*issue-${ISSUE_NUMBER}*" -o -name "*${ISSUE_NUMBER}*" 2>/dev/null || echo "")
DOMAIN_FILES=$(find docs/domain -name "*issue-${ISSUE_NUMBER}*" -o -name "*${ISSUE_NUMBER}*" 2>/dev/null || echo "")
TEST_FILES=$(find docs/test_plan docs/test_report -name "*issue-${ISSUE_NUMBER}*" -o -name "*${ISSUE_NUMBER}*" 2>/dev/null || echo "")

if [[ -n "$USE_CASE_FILES" ]]; then
    echo "✅ Use case documentation found for Issue #$ISSUE_NUMBER"
    # Use Read tool to analyze specifications
else
    echo "⚠️ Use case documentation not found for Issue #$ISSUE_NUMBER"
fi

if [[ -n "$DOMAIN_FILES" ]]; then
    echo "✅ Domain model documentation found"
    # Use Read tool to analyze domain documentation
else
    echo "⚠️ Domain model documentation not found"
fi

if [[ -n "$TEST_FILES" ]]; then
    echo "✅ Test documentation found"  
    # Use Read tool to analyze test documentation
else
    echo "⚠️ Test documentation not found"
fi

# 2. Quality metrics execution
echo "📊 Executing quality metrics analysis..."

# Test coverage analysis
if command -v uv &> /dev/null; then
    echo "🧪 Running comprehensive test coverage analysis..."
    Use Bash tool: PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest --cov=src --cov=domain --cov=application --cov=infrastructure --cov=presentation --cov-report=json --cov-report=term-missing > tests/coverage-reports/issue-${ISSUE_NUMBER}-coverage.txt 2>&1 || echo "Test analysis completed"
fi

# Code quality analysis
if command -v ruff &> /dev/null; then
    echo "🔍 Running code quality analysis..."
    Use Bash tool: uv run --frozen ruff check . --output-format=json > docs/quality-reports/issue-${ISSUE_NUMBER}-ruff.json 2>&1 || echo "Code quality analysis completed"
fi

# Type checking analysis
if command -v pyright &> /dev/null; then
    echo "🔬 Running type checking analysis..."
    Use Bash tool: uv run --frozen pyright --outputformat=json > docs/quality-reports/issue-${ISSUE_NUMBER}-pyright.json 2>&1 || echo "Type checking completed"
fi

echo "✅ Quality assessment execution completed"
### Phase 5: Report Generation & Documentation

```bash
echo "📝 Creating comprehensive review reports..."

# Main implementation review report
REVIEW_REPORT_FILE="docs/review/issue-${ISSUE_NUMBER}-review.md"
Write "$REVIEW_REPORT_FILE" with:
# - Strategic analysis results from Sequential MCP
# - Implementation completeness assessment with artifact verification
# - Architectural compliance analysis with Clean Architecture validation
# - Quality metrics analysis with comprehensive coverage reporting
# - Technical debt identification with strategic prioritization
# - Improvement recommendations with implementation roadmap

# Quality dashboard
QUALITY_DASHBOARD_FILE="docs/quality-reports/issue-${ISSUE_NUMBER}-quality-dashboard.md"
Write "$QUALITY_DASHBOARD_FILE" with:
# - Quality metrics overview with trend analysis
# - Test coverage analysis with strategic insights
# - Code quality scores with improvement targets
# - Architecture compliance scoring with remediation plans
# - Technical debt analysis with prioritized action items

echo "✅ Strategic review documentation completed"
```

### Phase 6: GitHub Integration & Project Updates

```bash
echo "🔗 Updating GitHub issue and project documentation..."

# GitHub issue comment with review results
if command -v gh &> /dev/null; then
    REVIEW_SUMMARY="✅ 戦略的実装レビュー完了 - Issue #${ISSUE_NUMBER}

📊 **品質評価結果**:
- 🏗️ アーキテクチャ準拠性: [評価結果]
- 🧪 テストカバレッジ: [カバレッジ%]%
- 🔍 コード品質スコア: [品質スコア]/100
- ⚠️ 技術的負債: [識別件数]件
- 🎯 改善提案: [提案件数]件

📁 **詳細レポート**:
- [戦略的レビューレポート](docs/review/issue-${ISSUE_NUMBER}-review.md)
- [品質ダッシュボード](docs/quality-reports/issue-${ISSUE_NUMBER}-quality-dashboard.md)

🚀 **次のアクション**:
戦略的改善提案の確認と実装計画策定を推奨します。"
    
    Use Bash tool: gh issue comment "${ISSUE_NUMBER}" --body "$REVIEW_SUMMARY"
fi

echo "📦 Recording results and learning insights..."

# Commit review documentation
Use Bash tool: git add docs/review/ docs/quality-reports/ tests/coverage-reports/
Use Bash tool: git commit -m "feat: complete strategic implementation review for issue ${ISSUE_NUMBER} with MCP-3 analysis

Comprehensive quality assessment with Sequential MCP strategic analysis.
Multi-layer implementation verification and architectural compliance validation.
Strategic improvement roadmap with intelligent prioritization.

🎯 Generated with Claude Code"

echo "✅ Strategic implementation review completed with MCP-3 intelligence"
```

---

## ✅ Quality Assurance & Learning

### Execution Validation

```bash
echo "🔍 Validating implementation review quality..."

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
    Use mcp__serena__write_memory "review-issue-insights-$(date +%Y%m%d)" "{
      \"approach_effectiveness\": \"MCP-3 strategic implementation review approach\",
      \"sequential_integration_results\": \"systematic analysis outcomes\", 
      \"improvement_opportunities\": [\"enhanced technical debt prioritization\", \"deeper architectural compliance analysis\"],
      \"user_feedback\": \"implementation review execution feedback\"
    }"
fi

echo "📦 Learning insights recorded for continuous improvement"
```

### Self-Diagnosis Checklist

**Core Quality Standards (MUST):**
- [ ] Implementation artifacts verified across all architectural layers
- [ ] Architectural compliance assessment completed with detailed analysis
- [ ] Quality metrics collected and analyzed with improvement recommendations
- [ ] Comprehensive review report created with actionable insights
- [ ] GitHub issue updated with review results

**MCP-3 Enhancement Standards (SHOULD when available):**
- [ ] Sequential MCP applied for strategic analysis
- [ ] Serena MCP utilized for code pattern analysis
- [ ] Context7 MCP consulted for review best practices
- [ ] Systematic decomposition and impact assessment completed

---

## 📊 Standardized Output

### 実行サマリー (日本語でユーザーに報告)

**基本実装レビュー (常に実行):**
- ✅ **実装成果物確認**: Issue #${ISSUE_NUMBER} の全レイヤー実装検証・文書確認完了
- ✅ **アーキテクチャ準拠性**: TDD/DDD/Clean Architecture原則準拠性評価完了
- ✅ **品質評価**: テストカバレッジ・コード品質・技術的負債評価完了
- ✅ **改善提案**: 優先度付き改善推奨事項と実装ロードマップ作成完了

**MCP-3戦略的強化 (利用可能時):**
- ✅ **Sequential MCP戦略分析**: 体系的な複合分析で戦略的洞察を生成
- ✅ **Serena MCP コード解析**: 包括的実装パターン分析と改善機会発見
- ✅ **Context7最新パターン**: 最新のレビュー手法とベストプラクティス適用
- ✅ **戦略的改善計画**: 複数レイヤーにわたる改善ロードマップ生成

### 生成ファイル

**基本ファイル:**
- `docs/review/issue-${ISSUE_NUMBER}-review.md`: 戦略的実装レビューレポート
- `docs/quality-reports/issue-${ISSUE_NUMBER}-quality-dashboard.md`: 総合品質ダッシュボード
- `tests/coverage-reports/issue-${ISSUE_NUMBER}-coverage.txt`: テストカバレッジ詳細

**MCP-3拡張 (利用時):**
- Enhanced analysis with Sequential MCP strategic insights
- Serena MCP memory updates for continuous learning
- Context7 pattern-enhanced documentation

### 総合判定

**ステータス**: `SUCCESS` (基本) / `MCP3_STRATEGIC_SUCCESS` (MCP-3利用時)
**戦略レビュー品質**: [スコア]/100
**MCP-3統合効果**: [スコア]/100 (利用時のみ)
**次フェーズ準備**: `READY`

### 次のステップ案内

1. **即座実行可能**: `/apply-feedback-enhanced ${ISSUE_NUMBER}` で戦略的改善提案の実装開始
2. **推奨**: 戦略的レビューレポートの詳細確認と優先度調整
3. **確認推奨**: 品質ダッシュボードでの継続的品質監視

**完了メッセージ:**

```
🎉 MCP-3戦略的実装レビュー完了！

🔍 基本実装レビュー:
   ✅ 実装成果物検証: 全アーキテクチャレイヤー
   ✅ 品質評価: テスト・コード品質・技術的負債
   ✅ GitHub Issue: #${ISSUE_NUMBER}更新完了

🧠 MCP-3戦略強化 (利用時):
   🧩 Sequential MCP: 体系的戦略分析完了
   🔍 Serena MCP: 実装パターン解析完了
   📚 Context7 MCP: 最新レビュー手法適用完了
   📊 戦略ロードマップ: 優先度付き改善計画生成

📁 成果物:
   ✅ docs/review/issue-${ISSUE_NUMBER}-review.md
   ✅ docs/quality-reports/issue-${ISSUE_NUMBER}-quality-dashboard.md

🎯 次のアクション:
   /apply-feedback-enhanced ${ISSUE_NUMBER}

✅ 戦略的実装レビュー完了 - 品質向上準備万全！
```
