# /review-issue-enhanced [issue-number] - MCP統合インテリジェント実装レビュー

## 🎯 Purpose and Scope

Execute comprehensive TDD/DDD/Layered Architecture implementation review with MCP-enhanced intelligence for thorough code quality assessment and architectural compliance verification. This enhanced command provides automated code analysis, pattern recognition, and intelligent improvement recommendations.

### Your Expertise (Core + MCP Enhanced)

**Core Review Expertise:**

- **Architecture Compliance**: TDD/DDD/Layered Architecture principles verification
- **Code Quality Assessment**: Comprehensive quality metrics and standards validation
- **Implementation Review**: Complete artifact review across all layers
- **Test Coverage Analysis**: Thorough testing completeness verification

**MCP-Enhanced Capabilities:**

- **Intelligent Code Analysis**: Automated architecture compliance assessment using Serena MCP
- **Context-Rich Review**: Context7-enhanced review patterns and industry best practices
- **Cross-Layer Impact Analysis**: Comprehensive dependency and coupling analysis
- **Strategic Improvement Planning**: Intelligent prioritization of improvement recommendations

### Execution Principles (Core + MCP Enhanced)

**Core Principles:**

1. **Architecture First**: Verify adherence to TDD/DDD/Layered Architecture principles
2. **Quality Focus**: Ensure code meets established quality standards and metrics
3. **Completeness**: Verify all expected artifacts and implementations exist

**MCP-Enhanced Principles:**
4. **Intelligent Analysis**: Leverage Serena for deep architectural and quality analysis
5. **Pattern-Based Assessment**: Apply Context7 review patterns and industry standards
6. **Predictive Enhancement**: Use MCP intelligence for proactive improvement identification

### Quality Standards (Core + MCP Enhanced)

**Core Standards:**

- **Test Coverage**: Minimum 80% coverage for all business logic
- **Architecture Compliance**: 100% adherence to layer dependency rules
- **Code Quality**: Zero critical issues in linting and type checking

**MCP-Enhanced Standards:**

- **Pattern Compliance**: 95% adherence to architectural patterns and best practices
- **Cross-Layer Analysis**: 100% coverage of dependency and coupling analysis
- **Predictive Quality**: 90% accuracy in identifying potential improvement areas
- **Strategic Assessment**: 100% alignment with long-term architectural goals

---

## 🚀 Commands in Workflow Context

### Position in Development Flow

```
📋 Current Position: /review-issue-enhanced
├── [Implementation cycle: 03-12]
├── 13. review-issue ← **Current: Comprehensive implementation review**
├── [Feedback loop: apply improvements]
```

4. Implementation completion ← Previous: All implementation phases complete

**Core Activities (Traditional):**

- Review domain, application, infrastructure, and presentation layers
- Analyze test coverage and quality metrics
- Verify architectural compliance and patterns
- Create comprehensive review report with improvement recommendations

**MCP-Enhanced Activities (Additional):**

- Analyze architectural patterns using Serena MCP for deeper insights
- Extract quality issues automatically from codebase
- Apply Context7 review patterns and industry best practices
- Generate strategic improvement roadmap with intelligent prioritization

---

## 🔧 Setup Script

Execute this comprehensive setup to initialize MCP-enhanced review environment:

```bash
#!/bin/bash

# Issue number validation
if [[ $# -eq 0 ]]; then
    echo "❌ Issue number is required"
    echo "Usage: /review-issue-enhanced [issue-number]"
    exit 1
fi

# MCP availability check
echo "🔍 MCP統合実装レビューシステム初期化中..."
if [[ -f ".serena/sessions/current/session-metadata.json" ]]; then
    echo "✅ Serena MCP detected - Enhanced architectural analysis available"
    echo "🎯 Intelligent code quality and architecture compliance analysis enabled"
    MCP_AVAILABLE="true"
else
    echo "ℹ️ MCP session not found - Running in standard mode"
    echo "💡 To enable MCP enhancements, run /context-session-stageup first"
    MCP_AVAILABLE="false"
fi

# GitHub integration check
if command -v gh &> /dev/null && gh auth status &> /dev/null; then
    echo "✅ GitHub CLI authenticated - Issue integration available"
    GITHUB_AVAILABLE="true"
    
    # Fetch issue data for context
    if gh issue view "$1" --json title,body,labels > /tmp/gh_issue_$1.json 2>/dev/null; then
        echo "📋 Issue #$1 data retrieved for review context"
    else
        echo "⚠️ Could not fetch issue #$1 data"
    fi
else
    echo "ℹ️ GitHub CLI not available - Running without GitHub integration"
    GITHUB_AVAILABLE="false"
fi

# Initialize enhanced review environment
ISSUE_NUMBER="$1"
echo "🎯 Enhanced Review Target: Issue #[$ISSUE_NUMBER]"
echo "📊 MCP Intelligence: $MCP_AVAILABLE"
echo "🔗 GitHub Integration: $GITHUB_AVAILABLE"

# Create review workspace
mkdir -p docs/review
mkdir -p docs/quality-reports
mkdir -p tests/coverage-reports

echo "✅ MCP統合実装レビュー環境準備完了"
echo ""
```

---

## 📊 Analysis Phase

**Analyze the following as expert (User interactions in Japanese):**

**Core Analysis Activities:**

1. **Implementation Artifacts Verification**

   - Check use case specification: `docs/use_cases/issue-${ISSUE_NUMBER}-*.md`
   - Verify domain model documentation: `docs/domain/issue-${ISSUE_NUMBER}-*.md`
   - Validate test plan existence: `docs/test_plan/issue-${ISSUE_NUMBER}-*.md`
   - Confirm test report completeness: `docs/test_report/issue-${ISSUE_NUMBER}-*.md`
   - Review implementation files across all layers (domain, application, infrastructure, presentation)
   - Analyze test files and coverage reports

2. **Architecture Compliance Assessment**
   - Verify layer dependency directions (Presentation → Application → Domain)
   - Check for circular dependencies between components
   - Validate proper separation of concerns across layers
   - Assess domain purity (no external dependencies)
   - Review dependency injection patterns and implementations
   - Analyze aggregate boundaries and consistency rules

**MCP-Enhanced Analysis (if available):**
3. **Automated Architectural Pattern Discovery**

- Use mcp__serena__get_symbols_overview to analyze complete codebase structure
- Use mcp__serena__find_symbol to identify architectural components and patterns
- Use mcp__serena__search_for_pattern to find architectural violations and anti-patterns
- Create memory using mcp__serena__write_memory for architectural insights

4. **Intelligent Quality Assessment**
   - Use mcp__serena__find_referencing_symbols to analyze component coupling
   - Extract code quality issues using pattern analysis
   - Identify performance and maintainability concerns automatically
   - Document quality assessment in architecture memory

---

## 🎨 Design Phase

**Design the following as expert (Instructions to Claude Code in English):**

**Core Design Activities:**

1. **Review Strategy Design**

   ```
   For comprehensive implementation review:
   - Plan systematic review of all architectural layers
   - Design quality metrics assessment framework
   - Establish compliance verification checklist
   - Plan improvement recommendation prioritization
   ```

2. **Quality Assessment Framework**

   ```
   For code quality evaluation:
   - Define measurable quality criteria
   - Establish testing coverage standards
   - Plan architectural compliance verification
   - Design improvement impact analysis
   ```

3. **Review Reporting Structure**

   ```
   For comprehensive review documentation:
   - Plan detailed architectural analysis report
   - Design quality metrics dashboard
   - Structure improvement recommendations by priority
   - Plan actionable next steps and timelines
   ```

4. **Improvement Prioritization Framework**
   ```
   Priority matrix based on:
   - Architectural impact and compliance
   - Code quality and maintainability
   - Business risk and technical debt
   - Implementation complexity and effort
   ```

**MCP-Enhanced Design (if available):**
5. **Context7 Review Pattern Integration**

```
Use mcp__context7__resolve-library-id for "code-review-best-practices"
Use mcp__context7__get-library-docs for architectural review patterns
Use mcp__context7__get-library-docs for quality assessment methodologies
Integrate latest review methodologies and industry standards
```

6. **Strategic Assessment Enhancement**
   ```
   Apply intelligent review analysis using:
   - Pattern-based architectural assessment
   - Automated quality metric collection
   - Predictive improvement identification
   - Long-term architectural health evaluation
   ```

---

## ⚡ Implementation Phase

**Execute the following as expert (Instructions to Claude Code in English):**

**Core Implementation Steps:**

1. **Validate issue context and gather artifacts**

   ```bash
   # Verify issue-specific documentation exists
   if [[ ! -d "docs/use_cases" || ! -d "docs/domain" ]]; then
       echo "❌ Required documentation directories not found"
       exit 1
   fi
   
   # Check for issue-specific artifacts
   use_case_files=$(find docs/use_cases -name "*issue-${ISSUE_NUMBER}*" -o -name "*${ISSUE_NUMBER}*")
   domain_files=$(find docs/domain -name "*issue-${ISSUE_NUMBER}*" -o -name "*${ISSUE_NUMBER}*")
   
   if [[ -z "$use_case_files" || -z "$domain_files" ]]; then
       echo "⚠️ Some expected documentation files may be missing for Issue #${ISSUE_NUMBER}"
   fi
   ```

2. **Execute comprehensive quality analysis**

   ```bash
   # Test coverage analysis
   echo "📊 Analyzing test coverage..."
   uv run --frozen pytest --cov=domain --cov=application --cov=infrastructure --cov=presentation \
       --cov-report=json --cov-report=term-missing > /tmp/coverage_report.txt
   
   # Code quality analysis
   echo "🔍 Running code quality checks..."
   uv run --frozen ruff check . --output-format=json > /tmp/ruff_report.json
   uv run --frozen pyright --outputformat=json > /tmp/pyright_report.json
   
   # Architecture dependency analysis
   echo "🏗️ Analyzing architecture dependencies..."
   # Custom dependency analysis would go here
   ```

**MCP-Enhanced Implementation (if available):**
3. **Intelligent Architectural Assessment**

```bash
# Enhanced architectural analysis with MCP
For each architectural layer:
- Apply Serena MCP comprehensive analysis
- Use Context7 patterns for compliance verification
- Generate intelligent improvement recommendations
- Create strategic enhancement roadmap
```

4. **Automated Quality Enhancement Discovery**

   ```bash
   # Comprehensive quality discovery
   Use MCP intelligence for:
   - Automated code smell detection
   - Performance bottleneck identification
   - Maintainability improvement opportunities
   - Security and robustness assessment
   ```

---

## 🎯 Output Generation

**Execute the following as expert (Instructions to Claude Code in English):**

1. **Create comprehensive review report**

   ```bash
   Write "docs/review/issue-${ISSUE_NUMBER}-review.md" with:
   # - Complete implementation artifacts verification
   # - Detailed architectural compliance assessment
   # - Quality metrics analysis and recommendations
   # - Prioritized improvement action plan
   ```

2. **Generate quality metrics dashboard**

   ```bash
   Write "docs/quality-reports/issue-${ISSUE_NUMBER}-quality-dashboard.md" with:
   # - Test coverage analysis and trends
   # - Code quality metrics and benchmarks
   # - Architecture compliance scoring
   # - Performance and maintainability assessment
   ```

3. **Create MCP enhancement report (if available)**

   ```bash
   if [[ "$MCP_AVAILABLE" == "true" ]]; then
       # MCP-enhanced review analysis
       Write "docs/review/issue-${ISSUE_NUMBER}-mcp-analysis.md" with:
       # - Serena MCP architectural pattern analysis
       # - Context7 best practices compliance assessment
       # - Intelligent improvement recommendations
       # - Strategic enhancement roadmap
       
       # Detailed MCP insights
       Write "docs/review/issue-${ISSUE_NUMBER}-mcp-detailed-report.md" with:
       # - Complete architectural analysis findings
       # - Applied review patterns and methodologies
       # - Cross-layer dependency analysis results
       # - Future enhancement predictions
   fi
   ```

4. **Update GitHub issue with review results**

   ```bash
   if [[ "$GITHUB_AVAILABLE" == "true" ]]; then
       # Post review summary to GitHub issue
       gh issue comment "${ISSUE_NUMBER}" --body "✅ 実装レビュー完了
       
   📊 レビュー結果サマリー:
   - アーキテクチャ準拠性: [スコア]
   - テストカバレッジ: [カバレッジ]%
   - コード品質スコア: [品質スコア]
   - 改善提案: [提案数]件
   
   📁 詳細レポート:
   - docs/review/issue-${ISSUE_NUMBER}-review.md
   - docs/quality-reports/issue-${ISSUE_NUMBER}-quality-dashboard.md
   
   🎯 次のアクション:
   改善提案の実装および品質向上作業
       "
   fi
   
   # Commit all review documentation
   git add docs/review/ docs/quality-reports/
   if [[ "$MCP_AVAILABLE" == "true" ]]; then
       git commit -m "feat: complete comprehensive review for issue ${ISSUE_NUMBER} with MCP enhancement
       
   Execute thorough architectural compliance and quality assessment.
   Generate strategic improvement recommendations with MCP intelligence.
       
   🎯 Generated with Claude Code
       "
   else
       git commit -m "feat: complete comprehensive review for issue ${ISSUE_NUMBER}
       
   Execute thorough architectural compliance and quality assessment.
   Generate improvement recommendations and quality metrics.
       
   🎯 Generated with Claude Code
       "
   fi
   ```

---

## ✅ Built-in Quality Assurance

### Self-Diagnosis Checklist

**Required Items (MUST):**

- [ ] All expected implementation artifacts verified and documented
- [ ] Architectural compliance assessment completed across all layers
- [ ] Test coverage analysis executed with detailed reporting
- [ ] Code quality metrics collected and analyzed
- [ ] Improvement recommendations prioritized and actionable
- [ ] Review report comprehensive and well-structured

**Recommended Items (SHOULD):**

- [ ] Serena MCP architectural analysis utilized for deeper insights
- [ ] Context7 review patterns applied for industry-standard assessment
- [ ] Strategic improvement roadmap created with priorities
- [ ] Cross-layer dependency analysis completed thoroughly

### Quality Metrics

| Metric | Target | Actual | Assessment |
|--------|--------|--------|------------|
| Architecture Compliance | 100% | [Actual Value] | ✅/❌ |
| Test Coverage | 80%+ | [Actual Value] | ✅/❌ |
| Code Quality Score | 90%+ | [Actual Value] | ✅/❌ |
| Review Completeness | 100% | [Actual Value] | ✅/❌ |

**MCP-Enhanced Metrics (if MCP Available):**
| Metric | Target | Actual | Assessment |
|--------|--------|--------|------------|
| Pattern Compliance | 95% | [Actual Value] | ✅/❌ |
| Architectural Health | 90% | [Actual Value] | ✅/❌ |
| Predictive Accuracy | 85% | [Actual Value] | ✅/❌ |

---

## 📊 Standardized Output Format

### 実行サマリー (日本語でユーザーに報告)

**基本機能 (常に実行):**

- ✅ **実装成果物確認**: ユースケース、ドメイン、テスト計画・レポート検証完了
- ✅ **アーキテクチャ準拠性**: TDD/DDD/レイヤード原則[スコア]%達成
- ✅ **テストカバレッジ**: [カバレッジ]%（目標80%以上）
- ✅ **レビューレポート**: docs/review/issue-[N]-review.md 作成

**MCP拡張機能 (利用可能時):**

- ✅ **MCPアーキテクチャ解析**: [X]個のパターン発見、[Y]個の改善機会特定
- ✅ **インテリジェント品質評価**: Context7最新レビューパターン適用完了
- ✅ **戦略的改善計画**: [Z]個の優先順位付き改善提案生成
- ✅ **横断分析**: [W]層での依存関係・結合度完全分析

### 成果物

**基本ファイル (常に作成):**

- `docs/review/issue-[N]-review.md`: 包括的レビューレポート
- `docs/quality-reports/issue-[N]-quality-dashboard.md`: 品質メトリクスダッシュボード
- Test coverage reports: テストカバレッジ詳細レポート
- Quality analysis results: 品質分析結果

**MCP拡張ファイル (利用可能時):**

- `docs/review/issue-[N]-mcp-analysis.md`: MCP分析結果
- `docs/review/issue-[N]-mcp-detailed-report.md`: 詳細MCP分析レポート
- Updated MCP memory files: レビュー知見の永続化

### 総合判定

**ステータス**: `SUCCESS` (基本) / `MCP_ENHANCED_SUCCESS` (MCP利用時)
**アーキテクチャ準拠スコア**: [スコア]/100
**品質総合評価**: [スコア]/100
**MCPインテリジェンス活用**: [スコア]/100 (利用時のみ)
**改善要否判定**: `READY` / `IMPROVEMENTS_NEEDED`

### 次のステップ (日本語でユーザーに案内)

1. **即座に実行可能**: 特定された改善項目の実装
2. **推奨**: レビューフィードバックの適用と品質向上作業
3. **確認推奨**: 改善提案の優先順位確認と実装計画策定

**ユーザーへのメッセージ (日本語)**:

```
🎉 インテリジェント実装レビュー完了！

🔍 基本レビュー結果:
   ✅ アーキテクチャ準拠性: [スコア]%
   ✅ テストカバレッジ: [カバレッジ]%
   ✅ コード品質評価: [品質スコア]/100
   ✅ 改善提案: 必須[X]件、推奨[Y]件

🤖 MCP強化レビュー (利用時):
   🧠 Serenaアーキテクチャ解析: [X]パターン分析
   📊 品質改善発見: [Y]改善機会特定
   🎯 Context7パターン適用: 最新レビュー手法導入
   ✅ docs/review/issue-[N]-mcp-analysis.md
   ✅ docs/review/issue-[N]-mcp-detailed-report.md

📁 生成レポート:
   ✅ docs/review/issue-[N]-review.md
   ✅ docs/quality-reports/issue-[N]-quality-dashboard.md

📊 品質メトリクス:
   - アーキテクチャ健全性: [健全性スコア]%
   - 技術的負債レベル: [負債レベル]
   - 保守性指標: [保守性スコア]%

🎯 改善優先度:
   🔴 必須対応: [X]件 - 即座に対応が必要
   🟡 推奨改善: [Y]件 - 次回スプリントで対応
   🟢 将来改善: [Z]件 - 長期計画で検討

✅ 実装レビュー完了 - 高品質コード実現に向けた改善指針提供完了！
```