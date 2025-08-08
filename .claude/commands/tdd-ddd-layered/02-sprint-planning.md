Plan sprint and create tickets from core scenarios.

Follow these steps:

1. **Check Arguments**:
   - Verify that `$ARGUMENTS` (sprint number) is provided
   - If not provided, terminate and prompt user to pass sprint number

2. **Review Core Scenarios**:
   - Read `docs/use_cases/core/index.md` for scenario priorities
   - Read vision document from `docs/vision/project-vision.md`
   - Identify scenarios for this sprint based on priority

3. **Create Sprint Plan Document**:
   - File: `docs/sprints/sprint-$ARGUMENTS-plan.md`
   - Use the following template (content in Japanese):

```markdown
# スプリント$ARGUMENTS計画

## スプリントゴール
<What value will be delivered in this sprint>

## 選択されたコアシナリオ
1. <Scenario 1 name> - <Reason for selection>
2. <Scenario 2 name> - <Reason for selection>

## チケット一覧

### チケット1: <Scenario 1 name>
- **タイプ**: Feature
- **説明**: <Description from core scenario>
- **受け入れ基準**:
  - Given: <From scenario>
  - When: <From scenario>
  - Then: <From scenario>
- **推定**: <Story points or days>
- **依存関係**: <Dependencies if any>

### チケット2: <Scenario 2 name>
- **タイプ**: Feature
- **説明**: <Description from core scenario>
- **受け入れ基準**:
  - Given: <From scenario>
  - When: <From scenario>
  - Then: <From scenario>
- **推定**: <Story points or days>
- **依存関係**: <Dependencies if any>

## 実装順序
1. <Ticket 1> - <Reason>
2. <Ticket 2> - <Reason>

## リスクと軽減策
- **リスク**: <Identified risk>
  - **軽減策**: <Mitigation strategy>

## 成功指標
- <Measurable success criteria>
- <Measurable success criteria>
```

4. **Create GitHub Issues**:
   - For each ticket in the sprint plan:
   - Use `gh issue create` with appropriate labels
   - Include Given-When-Then as acceptance criteria
   - Link to core scenario document
   - Example command:
   ```bash
   gh issue create \
     --title "<Ticket title>" \
     --body "## 概要\n<Description>\n\n## 受け入れ基準\n- Given: <condition>\n- When: <action>\n- Then: <result>\n\n## 関連ドキュメント\n- [コアシナリオ](docs/use_cases/core/<scenario>.md)\n- [スプリント計画](docs/sprints/sprint-$ARGUMENTS-plan.md)" \
     --label "sprint-$ARGUMENTS,feature"
   ```

5. **Create Sprint Backlog**:
   - File: `docs/sprints/sprint-$ARGUMENTS-backlog.md`
   - Track issue numbers and status (content in Japanese):

```markdown
# スプリント$ARGUMENTS バックログ

## イシュー一覧
| Issue # | タイトル | ステータス | 担当者 | 完了日 |
|---------|----------|------------|--------|--------|
| #X | <Title> | Todo | - | - |
| #Y | <Title> | Todo | - | - |

## 進捗メトリクス
- **計画ポイント**: <Total points>
- **完了ポイント**: 0
- **残ポイント**: <Total points>

## デイリー進捗
### Day 1 (<Date>)
- [ ] Issue #X - <What to accomplish>
- [ ] Issue #Y - <What to accomplish>

### Day 2 (<Date>)
- [ ] Issue #X - <What to accomplish>
- [ ] Issue #Y - <What to accomplish>
```

6. **Validate Sprint Scope**:
   - Ensure sprint goals are achievable
   - Check dependencies between tickets
   - Verify team capacity matches workload
   - Confirm alignment with overall vision

7. **Guide Next Steps**:
   - Display created issue numbers
   - Suggest next commands in Japanese:
     - `/create-use-case <issue-number>` - Start implementing first ticket
     - Review sprint plan with team

Important Notes:
- One scenario = One ticket (as baseline)
- Large scenarios can be split into multiple tickets
- Include technical debt tickets if needed
- Always reference core scenarios
- Keep sprint scope realistic (don't overcommit)
- All user-facing output in Japanese