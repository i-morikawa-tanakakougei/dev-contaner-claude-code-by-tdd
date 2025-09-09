# 02-sprint-planning-enhanced (MCP-Enhanced Sprint Planning)

## 🎯 Expert Profile Declaration

During command execution, you act as an **Agile Sprint Planning Expert** specialist with **MCP Enhancement** capabilities.

**Language Guidelines:**

- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Your Expertise (Core + MCP Enhanced)

**Core Sprint Planning Expertise:**

- **Sprint Architecture**: Comprehensive sprint planning with scenario-based ticket decomposition and capacity estimation
- **Backlog Management**: Product backlog prioritization with business value assessment and dependency analysis
- **Ticket Engineering**: Given-When-Then acceptance criteria creation with testable specifications and clear definition of done
- **GitHub Integration**: Issue creation and management with proper labeling, milestone assignment, and team coordination

**MCP-Enhanced Capabilities:**

- **Intelligent Sprint Analysis**: Automated sprint pattern discovery and optimization using Serena MCP
- **Context-Aware Planning**: Context7-enhanced agile patterns and industry sprint planning best practices
- **Historical Sprint Mining**: Pattern discovery from previous sprints using Serena MCP memory
- **Cross-Reference Estimation**: Complete sprint dependency analysis and capacity optimization

### Execution Principles (Core + MCP Enhanced)

**Core Principles:**

1. **Scenario-First Decomposition**: Break down core scenarios into implementable tickets using 1-scenario = 1-ticket baseline
2. **Value-Driven Prioritization**: Prioritize tickets based on business value, technical risk, and dependency constraints  
3. **Testable Specifications**: Ensure every ticket has clear Given-When-Then acceptance criteria that enable TDD implementation
4. **Sprint Capacity Alignment**: Balance sprint scope with team capacity and technical complexity

**MCP-Enhanced Principles:**

5. **Intelligence-Driven Planning**: Leverage Serena for sprint pattern analysis and capacity optimization
6. **Context-Rich Estimation**: Apply Context7 agile best practices for accurate estimation and planning
7. **Predictive Sprint Management**: Use MCP intelligence for sprint risk assessment and success prediction

### Quality Standards (Core + MCP Enhanced)

**Core Standards:**

- **Scenario Coverage**: 100% core scenarios converted to implementable tickets
- **Acceptance Criteria**: All tickets have clear Given-When-Then specifications
- **Sprint Capacity**: 80-120% capacity utilization with risk buffer

**MCP-Enhanced Standards:**

- **Sprint Pattern Compliance**: 95% adherence to proven sprint planning patterns
- **Historical Learning Integration**: 100% previous sprint lessons applied to current planning
- **Capacity Prediction Accuracy**: 90%+ accuracy in sprint capacity estimation based on historical data
- **Risk Assessment Coverage**: 100% potential sprint risks identified and mitigated

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

**🧠 MCP Enhancement**: Serena (Sprint Analysis + Historical Patterns) + Context7 (Agile Best Practices + Planning Patterns)

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Initial Phase - Enhanced Sprint Planning (02/16) **[MCP-Enhanced Version]**  
> 🎯 **Phase Purpose**: Convert core scenarios into implementable sprint tickets with MCP intelligence  
> ⬅️ **Previous Stage**: 01-init-project-structure or 00-create-vision-enhanced  
> ➡️ **Next Stage**: 03-create-use-case or 03-create-use-case-enhanced

## 🎯 PHASE PURPOSE: ENHANCED SPRINT PLANNING WITH MCP INTELLIGENCE

**⚠️ Important Notice:**

- **This step focuses on INTELLIGENT SPRINT PLANNING** - Convert core scenarios into actionable development tickets with MCP-enhanced analysis
- **NO IMPLEMENTATION** - Focus only on planning, estimation, and GitHub issue creation with intelligence
- **1-SCENARIO = 1-TICKET BASELINE with MCP optimization** - Maintain traceability with intelligent split recommendations

**What this enhanced step does:**

1. `00-create-vision-enhanced` or `01-init-project-structure` ← Previous: Vision and core scenarios
2. `02-sprint-planning-enhanced` ← **【YOU ARE HERE】Enhanced sprint planning with MCP intelligence**
3. `03-create-use-case-enhanced` ← Next: Detailed specifications for individual tickets
4. Then proceed with TDD implementation workflow

**Core Activities (Traditional):**

- Convert core scenarios into implementable tickets with acceptance criteria
- Create GitHub issues with proper labeling and milestone assignment
- Estimate effort and plan sprint capacity
- Prioritize based on business value and technical constraints

**MCP-Enhanced Activities (Additional):**

- Analyze historical sprint patterns using Serena MCP for capacity optimization
- Apply Context7 agile best practices for intelligent planning and estimation
- Extract sprint planning insights from previous project patterns
- Create predictive sprint success analysis based on MCP intelligence
- Generate intelligent risk assessment and mitigation strategies

**PLAN ENHANCED SPRINTS WITH MCP INTELLIGENCE. DO NOT IMPLEMENT CODE.**

## 📋 軽量コンテキスト管理

### Required Reading (Minimal + MCP Enhanced)

```bash
# Standard project state checks
if [[ -f "docs/vision/project-vision.md" ]]; then
    echo "Loading project vision..."
    VISION_EXISTS=true
else
    echo "ERROR: Vision document not found. Run /create-vision-enhanced first."
    exit 1
fi

if [[ -d "docs/use_cases/core" ]]; then
    CORE_SCENARIOS=$(find docs/use_cases/core -name "*.md" | wc -l)
    echo "Found $CORE_SCENARIOS core scenarios for sprint planning"
else
    echo "ERROR: Core scenarios not found. Run /create-vision-enhanced first."
    exit 1
fi

# Sprint number parameter handling
if [[ -n "$1" ]]; then
    SPRINT_NUMBER="$1"
    echo "Planning Sprint $SPRINT_NUMBER"
else
    # Auto-detect next sprint number
    SPRINT_NUMBER=$(ls docs/sprint/ 2>/dev/null | grep -E '^sprint_[0-9]+_plan\.md$' | wc -l || echo "0")
    SPRINT_NUMBER=$((SPRINT_NUMBER + 1))
    echo "Auto-detected next sprint: Sprint $SPRINT_NUMBER"
fi

# MCP Enhanced: Historical sprint patterns (if available)
if [[ -f ".serena/sessions/current/session-metadata.json" ]]; then
    echo "🔍 Enhanced Analysis Mode: MCP capabilities enabled"
    echo "  🧠 Serena: Historical sprint analysis and capacity optimization"
    echo "  📚 Context7: Agile best practices and planning patterns"
    MCP_AVAILABLE="true"
else
    echo "📋 Standard Mode: Core sprint planning without MCP enhancements"
    MCP_AVAILABLE="false"
fi
```

### Optional Reading (As Needed)
- Existing sprint history: `docs/sprint/sprint_*_plan.md`
- Project state: `docs/metadata/project-state.json`
- Previous execution history: `.claude/context/execution-history.jsonl`

## GitHub Issue Integration (Enhanced)

### Enhanced Issue Comment Retrieval and Analysis
```bash
# Enhanced issue analysis with historical pattern context
echo "Retrieving existing GitHub issues with enhanced analysis..."

# Get all issues for context
EXISTING_ISSUES=$(gh issue list --state all --limit 50 --json number,title,body,comments,updatedAt,createdAt,labels,assignees)

# MCP Enhanced: Historical issue pattern analysis
if [[ "$MCP_AVAILABLE" == "true" ]]; then
    echo "🔍 Enhanced: Analyzing issue patterns for sprint planning insights..."
    echo "📊 Enhanced: Cross-referencing sprint velocity and success patterns..."
fi

# Extract and analyze recent comments from existing issues
for issue_data in $(echo "$EXISTING_ISSUES" | jq -r '.[] | @base64'); do
    issue_info=$(echo "$issue_data" | base64 --decode)
    issue_number=$(echo "$issue_info" | jq -r '.number')
    comment_count=$(echo "$issue_info" | jq '.comments | length')
    
    if [[ $comment_count -gt 0 ]]; then
        echo "Analyzing issue #$issue_number with $comment_count comments"
        # Get recent comments (latest 3 for each issue)
        recent_comments=$(echo "$issue_info" | jq -r '.comments | sort_by(.createdAt) | reverse | .[0:3]')
        latest_comment_date=$(echo "$recent_comments" | jq -r '.[0].createdAt // empty')
        
        if [[ -n "$latest_comment_date" ]]; then
            echo "Issue #$issue_number latest update: $latest_comment_date"
        fi
    fi
done
```

GitHub milestone and enhanced issue creation will be handled in Phase 4 execution flow.

## 🚀 MCP強化スプリント計画実行フロー

```bash
#!/bin/bash
# MCP-Enhanced Sprint Planning

echo "📋 MCP-Enhanced Sprint Planning..."

# Phase 1: MCP セッション確認・環境準備
echo "📚 Phase 1: MCP session and project context analysis..."

# Sprint番号検証
if [[ -n "$1" ]]; then
    SPRINT_NUMBER="$1"
    echo "🎯 Planning Sprint $SPRINT_NUMBER with MCP enhancement..."
else
    # Auto-detect next sprint number
    SPRINT_NUMBER=$(ls docs/sprint/ 2>/dev/null | grep -E '^sprint_[0-9]+_plan\.md$' | wc -l || echo "0")
    SPRINT_NUMBER=$((SPRINT_NUMBER + 1))
    echo "🎯 Auto-detected Sprint $SPRINT_NUMBER with MCP enhancement..."
fi

# MCP利用可能性確認
if [[ -f ".serena/sessions/current/session-metadata.json" ]]; then
    echo "✅ MCP session found - Enhanced sprint analysis available"
    MCP_AVAILABLE="true"
    echo "🔍 MCP Capabilities:"
    echo "  • Serena: Sprint pattern analysis and capacity optimization"
    echo "  • Context7: Agile best practices and planning patterns"
else
    echo "ℹ️ MCP session not found - Running in standard mode"
    echo "💡 To enable MCP enhancements, run /context-session-stageup first"
    echo "📋 Enhanced features when available:"
    echo "  • Historical sprint pattern analysis"
    echo "  • Intelligent capacity estimation"
    echo "  • Predictive risk assessment"
    echo "  • Agile best practice integration"
    MCP_AVAILABLE="false"
fi

# Phase 2: プロジェクト状態・ビジョン分析
echo "🔍 Phase 2: Vision and scenario analysis..."

# ビジョン文書確認
if [[ ! -f "docs/vision/project-vision.md" ]]; then
    echo "❌ ERROR: Vision document not found. Run /create-vision-enhanced first."
    exit 1
fi

echo "📄 Loading project vision and core scenarios..."
Use Read tool to analyze docs/vision/project-vision.md
Use Read tool to analyze docs/vision/bounded_context.md if exists
Use Read tool to analyze docs/vision/ubiquitous_language.md if exists

# コアシナリオ確認
if [[ ! -d "docs/use_cases/core" ]]; then
    echo "❌ ERROR: Core scenarios not found. Run /create-vision-enhanced first."
    exit 1
fi

CORE_SCENARIOS=$(find docs/use_cases/core -name "*.md" | wc -l)
echo "📊 Found $CORE_SCENARIOS core scenarios for sprint planning"
Use Glob tool to analyze "docs/use_cases/core/*.md"

# 既存スプリント履歴確認
if [[ -d "docs/sprint" ]]; then
    echo "📚 Analyzing existing sprint history..."
    Use LS tool to check docs/sprint/
fi

# Phase 3: MCP拡張分析（利用可能時）
if [[ "$MCP_AVAILABLE" == "true" ]]; then
    echo "🧠 Phase 3: MCP-enhanced sprint planning analysis..."
    
    # Serena履歴スプリントパターン分析
    echo "📚 Serena: Analyzing historical sprint patterns and velocity..."
    Use mcp__serena__search_for_pattern "sprint|velocity|capacity|estimation" --restrict_search_to_code_files=false
    Use mcp__serena__read_memory "sprint-success-patterns" if available
    Use mcp__serena__read_memory "capacity-estimation-history" if available
    Use mcp__serena__list_memories to find sprint-related patterns
    
    # Context7アジャイル・ベストプラクティス統合
    echo "🌐 Context7: Analyzing agile sprint planning best practices..."
    Use mcp__context7__resolve-library-id "agile-methodologies"
    Use mcp__context7__resolve-library-id "scrum-sprint-planning"
    Use mcp__context7__get-library-docs "/agile-methodologies" --topic "sprint-planning"
    Use mcp__context7__get-library-docs "/scrum-sprint-planning" --topic "capacity-estimation"
    Use mcp__context7__get-library-docs "/agile-methodologies" --topic "backlog-prioritization"
    
    # インテリジェント・リスク分析
    echo "🔍 Intelligent sprint risk analysis..."
    Use mcp__serena__search_for_pattern "risk|blocker|dependency|constraint" --context_lines_before=2 --context_lines_after=2
    
else
    echo "📋 Phase 3: Standard mode - Basic sprint analysis"
fi

# Step 7: 戦略的スプリント設計・決定
echo "🎨 Phase 4: Strategic sprint design and planning..."

echo "🎯 Strategic Sprint Planning Mode"
echo "📊 Systematic analysis with intelligent MCP integration for optimized sprint planning"

# ユーザーに日本語で戦略的スプリント計画情報を収集
Ask user for the following strategic sprint planning information in Japanese:
1. スプリント期間と開始日（戦略的タイムライン計画を含む）
2. チーム構成と利用可能工数（スキルマップを含む）
3. 主要な制約条件と依存関係（リスク評価を含む）
4. スプリント目標の優先順位（ビジネス価値分析を含む）
5. 技術的負債対応の割合（技術戦略との整合性を含む）
6. 特別考慮事項（休暇、イベント、リソース制約等）

# Step 8: 戦略的チケット分解・優先順位付け
echo "🎯 Phase 5: Strategic ticket decomposition and prioritization..."

echo "🔍 Strategic Ticket Analysis Framework:"
echo "  • Sequential: Systematic scenario complexity and decomposition analysis"
echo "  • Context7: Industry-standard decomposition patterns (if available)"
echo "  • Serena: Historical scenario complexity intelligence (if available)"

# Context7業界標準パターン取得（利用可能時）
if [[ "$MCP_CONTEXT7" == "available" ]]; then
    Use mcp__context7__get-library-docs "/user-story-splitting" --topic "scenario-decomposition"
    Use mcp__context7__get-library-docs "/agile-estimation" --topic "story-point-estimation"
fi

# Serenaシナリオ分析（利用可能時）
if [[ "$MCP_SERENA" == "available" ]]; then
    Use mcp__serena__search_for_pattern "Given.*When.*Then|complex|integration|dependency" --context_lines_before=3 --context_lines_after=3
fi

# Sequential による体系的分解戦略（利用可能時）
if [[ "$MCP_SEQUENTIAL" == "available" ]]; then
    Use mcp__sequential-thinking__sequentialthinking to systematically design:
    "Strategic Ticket Decomposition Framework:
    1. Scenario Complexity Analysis: Evaluate each core scenario for technical complexity, integration points, and dependencies
    2. Decomposition Strategy Planning: Determine optimal ticket splitting approach balancing business value and technical feasibility
    3. Priority Matrix Development: Create systematic prioritization framework considering business impact, technical risk, and resource requirements
    4. Capacity Allocation Planning: Map ticket complexity to team capacity and skill distribution
    5. Dependency Chain Analysis: Identify and map inter-ticket dependencies and sequencing requirements
    6. Risk Mitigation Integration: Incorporate risk factors into ticket prioritization and sprint planning"
fi

# 1-scenario = 1-ticket baseline with systematic adjustments
Apply the following strategic decomposition strategy:
- Simple scenarios: Keep as single tickets with clear acceptance criteria
- Complex scenarios: Systematic splitting based on strategic analysis and industry patterns
- Cross-cutting concerns: Extract as independent tickets with comprehensive dependency mapping
Enhanced with systematic complexity scoring and strategic capacity optimization

# Step 9: スプリント・ディレクトリ作成
echo "📁 Phase 6: Creating sprint documentation structure..."

# スプリントディレクトリ作成
Create directories: docs/sprint, docs/sprint/tickets if not exists

# Step 10: GitHub統合・Issue作成
echo "🔗 Phase 7: Strategic GitHub integration and issue creation..."

# Setup sprint milestone
MILESTONE_NAME="Sprint $SPRINT_NUMBER"
echo "Creating or checking milestone: $MILESTONE_NAME"

# Create milestone if not exists
Use Bash tool: gh api repos/:owner/:repo/milestones --method POST --field title="$MILESTONE_NAME" --field description="Sprint $SPRINT_NUMBER implementation milestone with MCP enhancement" --field due_on="$(date -d '+2 weeks' --iso-8601)" || echo "Milestone may already exist"

# Get milestone number for issue assignment
MILESTONE_NUMBER=$(gh api repos/:owner/:repo/milestones --jq ".[] | select(.title==\"$MILESTONE_NAME\") | .number")

# Strategic issue creation with MCP-3 integration
For each planned ticket, create GitHub issue with:
- Title: Clear, descriptive ticket name
- Body: Strategic Given-When-Then acceptance criteria
- Labels: sprint-$SPRINT_NUMBER, enhancement, tdd-ddd, mcp3-strategic (if MCP available)
- Milestone: Sprint $SPRINT_NUMBER
- Strategic descriptions with systematic analysis insights

Use Bash tool for each ticket:
gh issue create \
  --title "$ticket_title" \
  --body "$(Strategic ticket template with MCP-3 insights)" \
  --label "sprint-$SPRINT_NUMBER,enhancement,tdd-ddd" \
  --milestone "$MILESTONE_NUMBER" \
  --assignee "@me"

# Step 11: スプリント文書生成
echo "📝 Phase 8: Creating comprehensive sprint documentation..."

# メインスプリント計画書作成
SPRINT_PLAN_FILE="docs/sprint/sprint_${SPRINT_NUMBER}_plan.md"
Create "$SPRINT_PLAN_FILE" with:
- Sprint overview and goals with strategic context
- Ticket list with systematic complexity scoring and dependencies
- Capacity planning with strategic resource allocation
- Risk assessment and mitigation strategies enhanced by systematic analysis
- Success criteria and definition of done

# バックログ文書作成
SPRINT_BACKLOG_FILE="docs/sprint/sprint_${SPRINT_NUMBER}_backlog.md"
Create "$SPRINT_BACKLOG_FILE" with:
- Prioritized ticket list with strategic business value scoring
- Comprehensive dependency mapping and implementation order
- Strategic estimation with systematic analysis insights
- Sprint scope and out-of-scope items

# スプリント目標文書作成
SPRINT_GOALS_FILE="docs/sprint/sprint_${SPRINT_NUMBER}_goals.md"
Create "$SPRINT_GOALS_FILE" with:
- Clear sprint objectives aligned with strategic project vision
- Success metrics and acceptance criteria
- Team commitments and strategic capacity allocation
- Comprehensive risk mitigation strategies

# Step 12: MCP-3統合文書作成（利用可能時）
echo "🧠 Phase 9: Creating MCP-3 strategic analysis documents..."

# MCP-3統合文書作成
if [[ "$MCP_SEQUENTIAL" == "available" || "$MCP_SERENA" == "available" || "$MCP_CONTEXT7" == "available" ]]; then
    # MCP-3戦略分析結果文書
    MCP3_ANALYSIS_FILE="docs/sprint/sprint_${SPRINT_NUMBER}_mcp3_analysis.md"
    Create "$MCP3_ANALYSIS_FILE" with:
    - Sequential MCP systematic multi-component analysis results
    - Serena historical sprint pattern intelligence (if available)
    - Context7 agile best practice integration summary (if available)
    - Strategic capacity optimization recommendations
    - Systematic sprint success analysis and risk assessment
    
    # 戦略的容量分析レポート
    STRATEGIC_ANALYSIS_FILE="docs/sprint/sprint_${SPRINT_NUMBER}_strategic_analysis.md"
    Create "$STRATEGIC_ANALYSIS_FILE" with:
    - Strategic capacity planning with systematic analysis
    - Team optimization recommendations with skill mapping
    - Sprint scope optimization based on systematic evaluation
    - Continuous improvement recommendations for strategic planning
    
    # Serena memory への学習内容保存（利用可能時）
    if [[ "$MCP_SERENA" == "available" ]]; then
        Use mcp__serena__write_memory "sprint-planning-$(date +%Y%m%d)-sprint-${SPRINT_NUMBER}" "Sprint ${SPRINT_NUMBER} strategic planning completed with ${CORE_SCENARIOS} scenarios, systematic analysis, and MCP-3 integration"
    fi
fi

# Step 13: Git戦略的コミット
echo "💾 Recording results and learning insights..."
echo "📝 Phase 10: Git commit for strategic sprint planning..."

Use Bash tool: git add docs/sprint/

# MCP-3統合レベルに応じた戦略的コミットメッセージ
COMMIT_MSG="feat: create sprint ${SPRINT_NUMBER} plan with MCP-3 strategic integration

Strategic sprint planning with systematic multi-component analysis.
Convert ${CORE_SCENARIOS} core scenarios into implementable tickets.
Enhanced with MCP-3 systematic analysis and strategic optimization.

🤖 Generated with Claude Code

Co-Authored-By: Claude <noreply@anthropic.com>"

Use Bash tool: git commit -m "$COMMIT_MSG"

# Step 14: 品質保証・戦略検証
echo "✅ Phase 11: Quality assurance and strategic sprint validation..."

# 戦略品質チェックリスト実行
Verify the following strategic quality standards:

**Required Items (MUST):**
- [ ] All core scenarios converted to implementable tickets
- [ ] Each ticket has clear Given-When-Then acceptance criteria
- [ ] Sprint goals clearly defined and aligned with strategic vision
- [ ] GitHub Issues created with proper labeling and milestones
- [ ] Dependencies and risks identified and documented

**MCP-3 Enhanced Items (SHOULD if available):**
- [ ] Sequential MCP systematic multi-component analysis completed
- [ ] Serena MCP sprint pattern intelligence integrated
- [ ] Context7 agile best practices applied
- [ ] Strategic capacity optimization recommendations generated
- [ ] Systematic risk assessment performed

# Step 15: 実行サマリー・次ステップ案内
echo "🎉 Phase 12: Completion summary and next steps..."

Display to user in Japanese:
## ✅ 戦略的スプリント計画完了サマリー

**基本機能 (常に実行):**
- ✅ **シナリオ分析**: ${CORE_SCENARIOS}個のコアシナリオを戦略的分析・分類完了
- ✅ **チケット分解**: 1-scenario=1-ticket原則での体系的分解・優先順位付け完了
- ✅ **スプリント計画**: Sprint ${SPRINT_NUMBER} の戦略的目標・容量・スコープ策定完了
- ✅ **GitHub統合**: Issue作成・Milestone設定・ラベル付け完了

**MCP-3統合機能 (利用可能時):**
- ✅ **Sequential戦略分析**: 体系的多コンポーネント分析による最適化完了
- ✅ **Serena履歴分析**: 過去スプリントパターン・速度インテリジェンス統合完了
- ✅ **Context7アジャイル統合**: 最新スプリント計画・見積もり手法適用完了
- ✅ **体系的リスク評価**: 戦略的分析に基づく潜在リスク識別・対策立案完了

## 📁 成果物

**基本ファイル (常に作成):**
- `docs/sprint/sprint_${SPRINT_NUMBER}_plan.md`: 総合スプリント計画書
- `docs/sprint/sprint_${SPRINT_NUMBER}_backlog.md`: プロダクトバックログ
- `docs/sprint/sprint_${SPRINT_NUMBER}_goals.md`: スプリント目標定義
- GitHub Issues with sprint-${SPRINT_NUMBER} milestone

**MCP-3統合ファイル (利用可能時):**
- `docs/sprint/sprint_${SPRINT_NUMBER}_mcp3_analysis.md`: MCP-3戦略分析結果レポート
- `docs/sprint/sprint_${SPRINT_NUMBER}_strategic_analysis.md`: 戦略的容量・計画分析レポート
- Strategic GitHub Issues with systematic insights and recommendations
- Updated Serena memory: スプリント戦略計画結果の永続化

## 🚀 次のステップ

1. **即座に実行可能**: `/create-use-case-enhanced <issue-number>` で最優先チケットの詳細仕様作成
2. **推奨**: 最高優先度のGitHub Issueから順次ユースケース仕様作成開始
3. **確認推奨**: 作成されたスプリント計画とチーム容量のレビュー

**📊 Sprint ${SPRINT_NUMBER} 準備完了 - MCP-3戦略統合で最適化済み**

# メタデータ更新
Create docs/metadata/command-execution-log.json entry with:
{
  "command_executed": "sprint-planning-enhanced",
  "timestamp": "[current timestamp]",
  "status": "SUCCESS",
  "phase": "sprint-planning",
  "sprint_number": "${SPRINT_NUMBER}",
  "mcp_integration": {
    "sequential_strategic_analysis": "$MCP_SEQUENTIAL",
    "serena_sprint_intelligence": "$MCP_SERENA",
    "context7_agile_integration": "$MCP_CONTEXT7",
    "systematic_risk_assessment": "applied"
  },
  "metrics": {
    "scenarios_processed": "${CORE_SCENARIOS}",
    "tickets_created": "[number]",
    "github_issues": "[number]",
    "sprint_capacity_utilization": "[percentage]"
  },
  "next_recommended": ["create-use-case-enhanced"]
}

echo "🎯 MCP-3戦略統合スプリント計画が完了しました！"
```

---

🎯 **MCP-3戦略統合スプリント計画コマンド完成**

**使用方法**:
```bash
# スプリント番号を指定する場合
/sprint-planning-enhanced 1

# 自動検出する場合
/sprint-planning-enhanced
```

**MCP-3統合機能**:
- 🧩 **Sequential**: 戦略的複雑性に対する体系的多コンポーネント分析
- 📊 **Serena**: 履歴スプリントパターン分析・容量インテリジェンス
- 🌐 **Context7**: アジャイル・ベストプラクティス・最新計画手法統合