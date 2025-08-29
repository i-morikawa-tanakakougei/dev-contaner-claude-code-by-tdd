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

### Phase 1: フィードバック分析と要件発見
**Requirements Discovery Specialist として以下を分析:**

1. **スプリントフィードバック分析**
   - 確認ポイント: レトロスペクティブ、ユーザーフィードバック、ステークホルダーコメント
   - 発見対象: 未カバーの使用パターン、エラーシナリオ、パフォーマンス要件

2. **開発インサイト抽出**
   - 確認ポイント: 実装フェーズ（06-09）で発見された技術制約、統合課題
   - 発見対象: エッジケース、セキュリティ要件、スケーラビリティ考慮事項

### Phase 2: 新シナリオ特定と分類
**Requirements Discovery Specialist として以下を特定:**

1. **エッジケースシナリオ**
   ```
   Given [境界条件やエラー状態]
   When [ユーザーアクションやシステムイベント]
   Then [期待される例外処理や代替フロー]
   ```

2. **パフォーマンスシナリオ**
   ```
   Given [大量データや高負荷状態]
   When [パフォーマンス重要な操作]
   Then [応答時間やスループット要件]
   ```

3. **セキュリティシナリオ**
   ```
   Given [セキュリティ制約や認可状態]
   When [セキュリティ関連操作]
   Then [適切なアクセス制御や監査ログ]
   ```

### Phase 3: シナリオ文書化と統合
**Requirements Discovery Specialist として以下を実行:**

```bash
echo "🌱 フィーチャー '${FEATURE_NAME}' のシナリオ進化を開始します"

# 1. Create evolved scenarios directory
mkdir -p "docs/use_cases/evolved/"

# 2. Document new scenarios with proper structure
cat > "docs/use_cases/evolved/${FEATURE_NAME}-evolved-scenarios.md" <<EOF
# ${FEATURE_NAME} - 進化シナリオ

## 発見源
- スプリントフィードバック: [日付とソース]
- 開発インサイト: [実装フェーズでの発見]
- ユーザーフィードバック: [フィードバック内容]

## 新規シナリオ

### エッジケースシナリオ
[新しいGiven-When-Thenシナリオ]

### パフォーマンスシナリオ  
[パフォーマンス関連シナリオ]

### セキュリティシナリオ
[セキュリティ関連シナリオ]

## 既存ビジョンとの整合性
[ビジョンとの整合性確認]

## 実装優先度と複雑度
[各シナリオの実装優先度評価]
EOF

echo "📝 進化シナリオ文書を作成しました"
```

## ✅ Built-in Quality Assurance

### 自己診断チェックリスト
**必須項目（MUST）:**
- [ ] 新シナリオが既存ビジョンと整合していること
- [ ] 全てのシナリオがGiven-When-Then形式で記述されていること
- [ ] シナリオの発見源が明確に記録されていること
- [ ] 実装優先度と複雑度が評価されていること

**推奨項目（SHOULD）:**
- [ ] ドメインモデルへの影響が分析されていること
- [ ] 関連する既存シナリオとの関係が整理されていること
- [ ] スプリント統合のための準備が整っていること

### 品質メトリクス
| 指標 | 目標値 | 実績値 | 判定 |
|------|--------|--------|------|
| 新規シナリオ数 | ≥3個 | [実績値] | ✅/❌ |
| ビジョン整合性 | 100% | [実績値] | ✅/❌ |
| 発見源の明確性 | 100% | [実績値] | ✅/❌ |

### エラー処理
**想定されるエラーと対処:**
1. **ビジョン不整合**: 既存ビジョンと矛盾するシナリオの検出と調整
2. **シナリオ重複**: 既存シナリオとの重複検出と統合処理
3. **発見源不明**: シナリオの根拠が不明確な場合の再調査

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