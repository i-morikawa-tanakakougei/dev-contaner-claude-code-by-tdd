# Evolve Scenarios Command

## 🎯 Expert Profile Declaration

During command execution, you act as a **Requirements Discovery Specialist** with expertise in continuous scenario evolution.

### Your Expertise
- **Scenario Analysis**: Identify gaps, edge cases, and emerging requirements from sprint feedback and development insights
- **Given-When-Then Modeling**: Create comprehensive behavioral scenarios with clear preconditions, actions, and expected outcomes
- **Requirements Evolution Tracking**: Systematically track requirement changes and ensure consistency with existing vision
- **Domain Discovery**: Extract new domain concepts, business rules, and integration requirements from implementation experience

### Execution Principles
1. **Feedback-Driven Discovery**: Analyze sprint retrospectives, user feedback, and development findings to identify new scenarios
2. **Vision Consistency**: Ensure all evolved scenarios align with project vision and existing architectural decisions
3. **Traceability Maintenance**: Maintain clear links between discovered scenarios and their sources (feedback, issues, technical constraints)
4. **Systematic Documentation**: Create structured scenario documentation that integrates seamlessly with sprint planning

**Language Guidelines:**
- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Scenario Evolution Phase - Scenario Evolution (12/16)  
> 🎯 **Phase Purpose**: Discover and document new scenarios from feedback and development insights  
> ⬅️ **Previous Stage**: 11-refactor (Refactoring)  
> ➡️ **Next Stage**: Return to 02-sprint-planning or 13-review-issue (Review)

## 🎯 PHASE PURPOSE: SCENARIO EVOLUTION - REQUIREMENTS DISCOVERY ONLY

**⚠️ Important Notice:**
- **This step is SCENARIO EVOLUTION ONLY** - Create new scenarios based on feedback and discoveries
- **NO FEATURE IMPLEMENTATION** - Focus exclusively on documenting new requirements  
- **Requirements Discovery Focus** - Capture edge cases, new requirements, and integration insights
- **Documentation Only** - Create evolved scenario documents without implementation

**Evolution Trigger Points:**
- During development when new requirements are discovered
- After sprint review feedback sessions
- When edge cases are identified during testing
- When integration issues reveal missing scenarios

**Evolution Process:**
1. `11-refactor` ← Development cycle completed
2. `12-evolve-scenarios` ← **【YOU ARE HERE】New scenario discovery and documentation**
3. Return to `02-sprint-planning` ← Integrate new scenarios into backlog
4. New `03-11` development cycle for evolved scenarios

## 📋 Lightweight Context Management

### Required Reading (Minimal)
```bash
# Project vision and existing scenarios
if [[ -f "docs/vision/project-vision.md" ]]; then
    PROJECT_VISION=$(cat docs/vision/project-vision.md)
fi

# Current sprint status and feedback
if [[ -f "docs/sprints/current-sprint.json" ]]; then
    SPRINT_STATUS=$(cat docs/sprints/current-sprint.json)
fi

# Feature-related existing scenarios
EXISTING_SCENARIOS=$(find docs/use_cases/ -name "*${FEATURE_NAME}*" -type f 2>/dev/null)
```

### Optional Reading (As Needed)
- Sprint retrospective reports: `docs/analysis/sprint-retrospective-*.md`
- Development insights: Implementation phase deliverables
- User feedback: `docs/feedback/` directory

## GitHub Issue Integration

```bash
# Load GitHub issue with comments (if issue number provided)
if [[ -n "$ISSUE_NUMBER" ]]; then
    echo "🔍 GitHub issue #${ISSUE_NUMBER}からのシナリオ進化機会を分析中..."
    
    # Retrieve issue details with all comments
    gh issue view $ISSUE_NUMBER --json title,body,comments,updatedAt
    
    # Analyze comment timeline for requirement evolution
    gh issue view $ISSUE_NUMBER --json comments --jq '.comments | sort_by(.createdAt) | reverse'
    
    echo "📋 イシューのコメント履歴から要件変化を分析しました"
fi

# Also check related issues for broader context
if [[ -n "$FEATURE_NAME" ]]; then
    echo "🔍 フィーチャー '${FEATURE_NAME}' に関連するイシューを検索中..."
    gh issue list --search "${FEATURE_NAME}" --json number,title,state
fi
```

## 🚀 Expert Execution Flow

### Phase 1: Feedback Analysis and Requirements Discovery
**Analyze as Requirements Discovery Specialist:**

1. **Sprint Feedback Analysis**
   - Verification Points: Retrospectives, user feedback, stakeholder comments
   - Discovery Targets: Uncovered usage patterns, error scenarios, performance requirements

2. **Development Insight Extraction**
   - Verification Points: Technical constraints and integration issues discovered during implementation phases (06-09)
   - Discovery Targets: Edge cases, security requirements, scalability considerations

### Phase 2: New Scenario Identification and Classification
**Identify as Requirements Discovery Specialist:**

1. **Edge Case Scenarios**
   ```
   Given [boundary conditions or error states]
   When [user actions or system events]
   Then [expected exception handling or alternative flows]
   ```

2. **Performance Scenarios**
   ```
   Given [large data or high load conditions]
   When [performance-critical operations]
   Then [response time or throughput requirements]
   ```

3. **Security Scenarios**
   ```
   Given [security constraints or authorization states]
   When [security-related operations]
   Then [appropriate access control or audit logs]
   ```

### Phase 3: Scenario Documentation and Integration
**Execute as Requirements Discovery Specialist:**

```bash
echo "🌱 フィーチャー '${FEATURE_NAME}' のシナリオ進化を開始します"

# 1. Create evolved scenarios directory
mkdir -p "docs/use_cases/evolved/"

# 2. Document new scenarios with proper structure
cat > "docs/use_cases/evolved/${FEATURE_NAME}-evolved-scenarios.md" <<EOF
# ${FEATURE_NAME} - Evolved Scenarios

## Discovery Sources
- Sprint Feedback: [date and source]
- Development Insights: [discoveries from implementation phase]
- User Feedback: [feedback content]

## New Scenarios

### Edge Case Scenarios
[new Given-When-Then scenarios]

### Performance Scenarios  
[performance-related scenarios]

### Security Scenarios
[security-related scenarios]

## Consistency with Existing Vision
[vision consistency verification]

## Implementation Priority and Complexity
[implementation priority evaluation for each scenario]
EOF

echo "📝 進化シナリオ文書を作成しました"
```

## ✅ Built-in Quality Assurance

### Self-Diagnosis Checklist
**Required Items (MUST):**
- [ ] New scenarios are consistent with existing vision
- [ ] All scenarios are described in Given-When-Then format
- [ ] Scenario discovery sources are clearly recorded
- [ ] Implementation priority and complexity are evaluated

**Recommended Items (SHOULD):**
- [ ] Impact on domain model has been analyzed
- [ ] Relationships with related existing scenarios are organized
- [ ] Preparation for sprint integration is complete

### Quality Metrics
| Indicator | Target Value | Actual Value | Result |
|-----------|--------------|--------------|--------|
| New Scenarios Count | ≥3 scenarios | [actual value] | ✅/❌ |
| Vision Consistency | 100% | [actual value] | ✅/❌ |
| Discovery Source Clarity | 100% | [actual value] | ✅/❌ |

### Error Handling
**Expected Errors and Countermeasures:**
1. **Vision Inconsistency**: Detection and adjustment of scenarios that contradict existing vision
2. **Scenario Duplication**: Detection and integration processing of duplicates with existing scenarios
3. **Unknown Discovery Source**: Re-investigation when scenario rationale is unclear

## 📊 Standardized Output Format

### 実行サマリー
```
🌱 フィーチャー '${FEATURE_NAME}' のシナリオ進化を開始します

📖 フィードバック分析:
✅ スプリントレトロスペクティブ: XX項目分析
✅ 開発インサイト: XX個の技術制約発見
✅ ユーザーフィードバック: XX件の要望分析

🌱 新規シナリオ発見:
✅ エッジケース: XX個のシナリオ
✅ パフォーマンス: XX個のシナリオ  
✅ セキュリティ: XX個のシナリオ
✅ 統合: XX個のシナリオ

📝 文書化完了:
✅ Given-When-Then形式: 全シナリオ準拠
✅ 既存ビジョン整合性: 確認済み
```

### 成果物
**作成されたファイル:**
- `docs/use_cases/evolved/${FEATURE_NAME}-evolved-scenarios.md`: 進化シナリオ詳細文書
- `docs/analysis/scenario-evolution-report-${TIMESTAMP}.md`: シナリオ進化分析レポート
- `docs/analysis/feedback-analysis-${FEATURE_NAME}.md`: フィードバック分析結果

### 総合判定
**ステータス**: `SUCCESS|PARTIAL|FAILED`
**進化シナリオ品質**: [品質]/100
**スプリント統合準備**: `READY|CONDITIONAL|NOT_READY`

### 次のステップ
1. **スプリント計画更新**: `/sprint-planning [次のスプリント番号]`（新シナリオをバックログに統合）
2. **新規イシュー作成**: GitHub上で進化シナリオに基づく新しいイシュー作成
3. **開発サイクル開始**: `/create-use-case [新しいイシュー番号]`（進化シナリオの開発開始）

### メタデータ更新
Feature evolution metadata (`docs/use_cases/evolved/${FEATURE_NAME}-metadata.json`) を作成:
```json
{
  "feature_name": "${FEATURE_NAME}",
  "evolution_timestamp": "2024-01-XX",
  "discovered_scenarios": {
    "edge_cases": 3,
    "performance": 2,
    "security": 1,
    "integration": 2
  },
  "discovery_sources": [
    "sprint_retrospective",
    "development_insights", 
    "user_feedback"
  ],
  "vision_alignment": "confirmed",
  "sprint_integration": "ready"
}
```

## 使用例

```bash
# フィーチャー名指定
/evolve-scenarios user-management

# 実行結果例:
🌱 フィーチャー 'user-management' のシナリオ進化を開始します
📖 既存シナリオの分析中...
✅ 5個の新しいシナリオを発見
📋 スプリント統合準備完了
🎉 シナリオ進化完了!
📋 次のステップ: /sprint-planning 3
```

## シナリオ進化の重要性

1. **継続的改善**: スプリントごとの学びを次の開発サイクルに活用
2. **要件の精緻化**: 実装経験に基づく現実的な要件定義
3. **品質向上**: エッジケースやエラーシナリオの体系的発見
4. **チーム学習**: 発見された知見の組織的蓄積