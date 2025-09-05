# /evolve-scenarios-enhanced [feature-name] - MCP統合インテリジェントシナリオ進化

## 🎯 Purpose and Scope

Evolve scenarios based on sprint feedback with MCP-enhanced intelligence for comprehensive scenario analysis and strategic evolution planning. This enhanced command provides automated feedback analysis, pattern recognition, and intelligent scenario evolution recommendations.

### Your Expertise (Core + MCP Enhanced)

**Core Scenario Evolution Expertise:**

- **Feedback Analysis**: Sprint retrospective and review feedback interpretation
- **Scenario Extension**: Adding detail and edge cases to existing scenarios  
- **Requirements Discovery**: Identifying new capabilities from implementation experience
- **Impact Assessment**: Understanding evolution impact on architecture and implementation

**MCP-Enhanced Capabilities:**

- **Intelligent Feedback Mining**: Automated feedback pattern analysis using Serena MCP
- **Context-Rich Evolution**: Context7-enhanced scenario evolution patterns and best practices
- **Cross-Reference Analysis**: Comprehensive impact analysis across all project artifacts
- **Strategic Evolution Planning**: Intelligent prioritization and evolution roadmap generation

### Execution Principles (Core + MCP Enhanced)

**Core Principles:**

1. **Feedback-Driven**: All evolution based on concrete feedback from sprints and reviews
2. **Vision Alignment**: Maintain consistency with overall project vision
3. **Incremental Evolution**: Add scenarios gradually without disrupting existing structure

**MCP-Enhanced Principles:**
4. **Intelligent Analysis**: Leverage Serena for deep feedback pattern analysis
5. **Context-Aware Evolution**: Apply Context7 scenario evolution patterns and industry practices
6. **Predictive Enhancement**: Use MCP intelligence for future scenario need prediction

### Quality Standards (Core + MCP Enhanced)

**Core Standards:**

- **Traceability**: Clear connection between feedback source and scenario evolution
- **Consistency**: All evolved scenarios align with established ubiquitous language
- **Testability**: All new scenarios can be implemented and tested

**MCP-Enhanced Standards:**

- **Feedback Coverage**: 95% of feedback patterns analyzed and addressed
- **Evolution Pattern Compliance**: 90% adherence to proven scenario evolution practices
- **Strategic Alignment**: 100% alignment with long-term product vision
- **Cross-Impact Analysis**: 100% coverage of evolution impact across all layers

---

## 🚀 Commands in Workflow Context

### Position in Development Flow

```
📋 Current Position: /evolve-scenarios-enhanced
├── 00. create-vision ← Vision and core scenarios
├── 02. sprint-planning ← Sprint planning and tickets
├── 03. create-use-case ← Use case specifications
├── [Implementation cycle: 04-11]
├── 12. evolve-scenarios ← **Current: Scenario evolution based on feedback**
├── [Next iteration: 02-11 with evolved scenarios]
```

4. Sprint implementation completion ← Previous: Implementation cycle complete with feedback

**Core Activities (Traditional):**

- Analyze sprint retrospective and review feedback
- Create new Given-When-Then scenarios based on discoveries
- Update existing scenarios with enhanced detail
- Create GitHub issues for evolved scenarios

**MCP-Enhanced Activities (Additional):**

- Analyze feedback patterns using Serena MCP for deeper insights
- Extract evolution opportunities automatically from project artifacts
- Apply Context7 scenario evolution patterns and best practices
- Generate strategic evolution roadmap with intelligent prioritization

---

## 🔧 Setup Script

Execute this comprehensive setup to initialize MCP-enhanced scenario evolution environment:

```bash
#!/bin/bash

# Feature name validation
if [[ $# -eq 0 ]]; then
    echo "❌ Feature name is required"
    echo "Usage: /evolve-scenarios-enhanced [feature-name]"
    exit 1
fi

# MCP availability check
echo "🔍 MCP統合シナリオ進化システム初期化中..."
if [[ -f ".serena/sessions/current/session-metadata.json" ]]; then
    echo "✅ Serena MCP detected - Enhanced feedback analysis available"
    echo "🎯 Intelligent scenario evolution analysis enabled"
    MCP_AVAILABLE="true"
else
    echo "ℹ️ MCP session not found - Running in standard mode"
    echo "💡 To enable MCP enhancements, run /context-session-stageup first"
    MCP_AVAILABLE="false"
fi

# GitHub integration check
if command -v gh &> /dev/null && gh auth status &> /dev/null; then
    echo "✅ GitHub CLI authenticated - Issue creation and feedback analysis available"
    GITHUB_AVAILABLE="true"
    
    # Fetch recent feedback data
    echo "📊 Collecting feedback data..."
    
    # Get recent sprint-related issues and comments
    gh issue list --state=all --limit=20 --json number,title,body,comments > /tmp/recent_issues.json
    
    # Get recent PR reviews and comments
    gh pr list --state=all --limit=10 --json number,title,body,reviews > /tmp/recent_prs.json
    
else
    echo "ℹ️ GitHub CLI not available - Running without GitHub integration"
    GITHUB_AVAILABLE="false"
fi

# Initialize enhanced scenario evolution environment
FEATURE_NAME="$1"
echo "🎯 Enhanced Scenario Evolution Target: Feature [$FEATURE_NAME]"
echo "📊 MCP Intelligence: $MCP_AVAILABLE"
echo "🔗 GitHub Integration: $GITHUB_AVAILABLE"

# Create evolution workspace
mkdir -p docs/use_cases/evolved
mkdir -p docs/sprints/evolution-reports
mkdir -p docs/feedback/analysis-reports

echo "✅ MCP統合シナリオ進化環境準備完了"
echo ""
```

---

## 📊 Analysis Phase

**Analyze the following as expert (User interactions in Japanese):**

**Core Analysis Activities:**

1. **Sprint Feedback Collection**

   - Read sprint review notes from `docs/sprints/` using Read tool
   - Analyze review reports in `docs/review/issue-*-review.md`
   - Extract recent GitHub issue comments and PR feedback
   - Identify patterns in implementation challenges and discoveries
   - Document feedback sources and classify by type (feature, edge case, error, performance)
   - Analyze user stories completion and gaps

2. **Current Scenario Gap Analysis**
   - Compare implemented functionality with original scenarios
   - Identify scenarios that proved incomplete during implementation
   - Find missing edge cases discovered during testing
   - Analyze domain concept evolution during development
   - Review ubiquitous language changes and additions
   - Assess impact on existing architecture and design decisions

**MCP-Enhanced Analysis (if available):**
3. **Automated Feedback Pattern Mining**

- Use mcp__serena__search_for_pattern to find feedback patterns in documentation
- Use mcp__serena__get_symbols_overview to analyze codebase evolution
- Use mcp__serena__find_symbol to identify implementation gaps and extensions
- Create memory using mcp__serena__write_memory for evolution insights

4. **Intelligent Evolution Opportunity Discovery**
   - Use mcp__serena__find_referencing_symbols to trace requirement evolution
   - Extract strategic evolution opportunities from cross-reference analysis
   - Identify architectural implications automatically
   - Document evolution strategy in architecture memory

---

## 🎨 Design Phase

**Design the following as expert (Instructions to Claude Code in English):**

**Core Design Activities:**

1. **Evolution Strategy Design**

   ```
   For each identified evolution opportunity:
   - Classify evolution type (extension/edge case/error case/new feature)
   - Assess impact on domain model and architecture
   - Determine implementation complexity and effort
   - Plan integration with existing scenarios
   ```

2. **Scenario Evolution Structure**

   ```
   For each evolved scenario:
   - Design Given-When-Then structure with enhanced detail
   - Ensure traceability to feedback source
   - Maintain consistency with ubiquitous language
   - Plan testing and verification approach
   ```

3. **Impact Assessment Plan**

   ```
   For each evolution:
   - Analyze domain layer impact (entities, value objects, aggregates)
   - Assess application layer changes (use cases, services)
   - Evaluate infrastructure implications
   - Plan presentation layer adaptations
   ```

4. **Evolution Prioritization Framework**
   ```
   Priority matrix based on:
   - Business value and user impact
   - Implementation complexity
   - Risk and architectural impact
   - Sprint capacity and timeline constraints
   ```

**MCP-Enhanced Design (if available):**
5. **Context7 Evolution Pattern Integration**

```
Use mcp__context7__resolve-library-id for "scenario-evolution"
Use mcp__context7__get-library-docs for evolution patterns
Use mcp__context7__get-library-docs for feedback analysis techniques
Integrate latest scenario evolution methodologies
```

6. **Strategic Evolution Roadmap**
   ```
   Apply intelligent prioritization using:
   - Pattern-based evolution strategies
   - Risk-adjusted implementation planning
   - Capacity-based sprint allocation
   - Long-term architectural alignment
   ```

---

## ⚡ Implementation Phase

**Execute the following as expert (Instructions to Claude Code in English):**

**Core Implementation Steps:**

1. **Validate feature context and feedback sources**

   ```bash
   # Verify feature exists in current documentation
   if [[ ! -d "docs/use_cases" ]]; then
       echo "❌ Use cases directory not found"
       exit 1
   fi
   
   # Check for existing feature documentation
   if [[ ! -f "docs/use_cases/${FEATURE_NAME}.md" && ! -f "docs/use_cases/core/${FEATURE_NAME}.md" ]]; then
       echo "⚠️ Feature ${FEATURE_NAME} not found in existing documentation"
       echo "Creating new evolved scenario documentation..."
   fi
   ```

2. **Create evolved scenario documentation**

   ```bash
   # Create evolved scenario document
   Write "docs/use_cases/evolved/${FEATURE_NAME}-evolution.md" with:
   # - Change reason and feedback source analysis
   # - New/updated Given-When-Then scenarios
   # - Domain impact analysis
   # - Implementation impact assessment
   # - Relationship to core scenarios
   
   # Update scenario index
   Edit "docs/use_cases/index.md" to add:
   # - New evolved scenario entry
   # - Traceability information
   # - Status tracking
   ```

**MCP-Enhanced Implementation (if available):**
3. **Intelligent Scenario Generation**

```bash
# Enhanced scenario creation with MCP analysis
For each Serena-identified evolution opportunity:
- Generate comprehensive scenario variations
- Apply Context7 evolution patterns automatically
- Create intelligent cross-reference documentation
- Generate impact analysis with architectural implications
```

4. **Automated GitHub Integration**

   ```bash
   # Create GitHub issues for evolved scenarios
   For each new scenario:
   - Generate issue with enhanced description from MCP analysis
   - Apply appropriate labels and priority
   - Create cross-references to related scenarios
   - Update sprint planning documents automatically
   ```

---

## 🎯 Output Generation

**Execute the following as expert (Instructions to Claude Code in English):**

1. **Create comprehensive evolution documentation**

   ```bash
   Write "docs/use_cases/evolved/${FEATURE_NAME}-evolution.md" with:
   # - Detailed evolution rationale with feedback traceability
   # - Complete Given-When-Then scenarios with context
   # - Domain model implications and changes
   # - Implementation roadmap and effort estimation
   ```

2. **Generate evolution impact report**

   ```bash
   Write "docs/feedback/analysis-reports/${FEATURE_NAME}-evolution-analysis.md" with:
   # - Feedback source analysis and pattern identification
   # - Evolution opportunity assessment
   # - Risk analysis and mitigation strategies
   # - Sprint planning recommendations
   ```

3. **Create MCP enhancement report (if available)**

   ```bash
   if [[ "$MCP_AVAILABLE" == "true" ]]; then
       # MCP-enhanced evolution analysis
       Write "docs/feedback/analysis-reports/${FEATURE_NAME}-mcp-analysis.md" with:
       # - Serena MCP feedback pattern analysis
       # - Context7 evolution pattern application
       # - Intelligent prioritization recommendations
       # - Strategic evolution roadmap
       
       # Detailed MCP insights
       Write "docs/feedback/analysis-reports/${FEATURE_NAME}-mcp-detailed-report.md" with:
       # - Complete feedback mining results
       # - Applied evolution patterns and rationale
       # - Cross-impact analysis findings
       # - Future evolution predictions
   fi
   ```

4. **Update project evolution metadata and create GitHub issues**

   ```bash
   # Create GitHub issues for each evolved scenario
   for scenario in evolved_scenarios; do
       if [[ "$GITHUB_AVAILABLE" == "true" ]]; then
           gh issue create \
             --title "実装: ${scenario}" \
             --body "## 概要
   ${scenario_description}
   
   ## シナリオ
   - Given: ${given_condition}
   - When: ${when_action} 
   - Then: ${then_result}
   
   ## 発見経緯
   ${discovery_context}
   
   ## 関連ドキュメント
   - [進化シナリオ](docs/use_cases/evolved/${FEATURE_NAME}-evolution.md)" \
             --label "enhancement,evolved-scenario"
       fi
   done
   
   # Update sprint evolution tracking
   current_sprint=$(find docs/sprints -name "sprint-*-backlog.md" | sort -r | head -1 | grep -o 'sprint-[0-9]*')
   if [[ -n "$current_sprint" ]]; then
       Write "docs/sprints/evolution-reports/${current_sprint}-evolution.md" with:
       # - Evolution summary for this sprint
       # - Impact on sprint goals and capacity
       # - Learning outcomes and insights
   fi
   
   # Commit evolution documentation
   git add docs/use_cases/evolved/ docs/feedback/analysis-reports/ docs/sprints/evolution-reports/
   if [[ "$MCP_AVAILABLE" == "true" ]]; then
       git commit -m "feat: evolve scenarios for ${FEATURE_NAME} with MCP enhancement
       
   Add evolved scenarios based on sprint feedback and implementation learnings.
   Enhanced with MCP intelligent analysis and strategic evolution planning.
       
   🎯 Generated with Claude Code
       "
   else
       git commit -m "feat: evolve scenarios for ${FEATURE_NAME}
       
   Add evolved scenarios based on sprint feedback and implementation learnings.
       
   🎯 Generated with Claude Code
       "
   fi
   ```

---

## ✅ Built-in Quality Assurance

### Self-Diagnosis Checklist

**Required Items (MUST):**

- [ ] Feedback sources analyzed and documented comprehensively
- [ ] Evolved scenarios maintain consistency with ubiquitous language
- [ ] GitHub issues created for each new scenario
- [ ] Impact analysis completed for all architecture layers
- [ ] Traceability maintained between feedback and evolution
- [ ] Evolution documentation comprehensive and actionable

**Recommended Items (SHOULD):**

- [ ] Serena MCP feedback pattern analysis utilized effectively
- [ ] Context7 evolution patterns applied appropriately
- [ ] Strategic evolution roadmap created with priorities
- [ ] Cross-reference analysis completed for impact assessment

### Quality Metrics

| Metric | Target | Actual | Assessment |
|--------|--------|--------|------------|
| Feedback Coverage | 100% | [Actual Value] | ✅/❌ |
| Scenario Quality | 95% | [Actual Value] | ✅/❌ |
| Traceability Score | 100% | [Actual Value] | ✅/❌ |
| Evolution Completeness | 90% | [Actual Value] | ✅/❌ |

**MCP-Enhanced Metrics (if MCP Available):**
| Metric | Target | Actual | Assessment |
|--------|--------|--------|------------|
| Pattern Analysis Coverage | 95% | [Actual Value] | ✅/❌ |
| Evolution Strategy Quality | 90% | [Actual Value] | ✅/❌ |
| Predictive Accuracy | 85% | [Actual Value] | ✅/❌ |

---

## 📊 Standardized Output Format

### 実行サマリー (日本語でユーザーに報告)

**基本機能 (常に実行):**

- ✅ **フィードバック分析**: [X]個のフィードバック源から[Y]個の進化機会を特定
- ✅ **シナリオ進化**: [Z]個の新規/更新シナリオを作成
- ✅ **GitHub連携**: Issue #[N1], #[N2], #[N3] を自動作成
- ✅ **文書化完了**: docs/use_cases/evolved/[feature]-evolution.md 作成

**MCP拡張機能 (利用可能時):**

- ✅ **MCPフィードバック解析**: [X]個のパターン発見、[Y]個の戦略的機会特定
- ✅ **インテリジェント進化**: Context7最新進化パターン適用完了
- ✅ **戦略ロードマップ**: [Z]スプリント分の進化計画自動生成
- ✅ **横断影響分析**: [W]個のアーキテクチャ影響を自動分析

### 成果物

**基本ファイル (常に作成):**

- `docs/use_cases/evolved/[feature]-evolution.md`: 進化シナリオ詳細
- `docs/feedback/analysis-reports/[feature]-evolution-analysis.md`: 進化分析レポート
- `docs/sprints/evolution-reports/sprint-X-evolution.md`: スプリント進化記録
- Updated `docs/use_cases/index.md`: シナリオインデックス更新

**MCP拡張ファイル (利用可能時):**

- `docs/feedback/analysis-reports/[feature]-mcp-analysis.md`: MCP分析結果
- `docs/feedback/analysis-reports/[feature]-mcp-detailed-report.md`: 詳細MCP分析
- Updated MCP memory files: 進化知見の永続化

### 総合判定

**ステータス**: `SUCCESS` (基本) / `MCP_ENHANCED_SUCCESS` (MCP利用時)
**進化品質スコア**: [スコア]/100
**MCPインテリジェンス活用**: [スコア]/100 (利用時のみ)
**次フェーズ準備**: `READY`

### 次のステップ (日本語でユーザーに案内)

1. **即座に実行可能**: `/create-tests-enhanced [新規issue番号]` または `/sprint-planning-enhanced [次スプリント番号]`
2. **推奨**: 進化したシナリオのテスト作成フェーズ
3. **確認推奨**: 進化分析レポートとアーキテクチャ影響の確認

**ユーザーへのメッセージ (日本語)**:

```
🎉 インテリジェントシナリオ進化完了！

🔄 基本シナリオ進化:
   ✅ フィードバック分析: [X]ソース解析
   ✅ 進化機会特定: [Y]個の新規要求発見
   ✅ シナリオ作成: [Z]個のGiven-When-Then追加
   ✅ GitHub Issue作成: #[N1], #[N2], #[N3]

🤖 MCP強化進化 (利用時):
   🧠 Serenaパターン解析: [X]個のフィードバックパターン発見
   📊 進化戦略策定: [Y]スプリント分のロードマップ生成
   🎯 Context7パターン適用: 最新進化手法導入
   ✅ docs/feedback/analysis-reports/[feature]-mcp-analysis.md
   ✅ docs/feedback/analysis-reports/[feature]-mcp-detailed-report.md

📁 生成ファイル:
   ✅ docs/use_cases/evolved/[feature]-evolution.md
   ✅ docs/feedback/analysis-reports/[feature]-evolution-analysis.md
   ✅ docs/sprints/evolution-reports/sprint-X-evolution.md

🎯 次のアクション:
   /create-tests-enhanced [issue-numbers] または /sprint-planning-enhanced [sprint-number]

✅ シナリオ進化完了 - 次世代要求対応準備完了！
```