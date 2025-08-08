Evolve scenarios based on sprint feedback.

Follow these steps:

1. **Check Arguments**:
   - Verify that `$ARGUMENTS` (feature name) is provided
   - If not provided, terminate and prompt user to pass feature name

2. **Analyze Feedback Source**:
   - Check for sprint review notes in `docs/sprints/`
   - Check for review reports in `docs/review/issue-*-review.md`
   - Review recent GitHub issue comments
   - Identify new requirements or edge cases discovered from:
     - Sprint retrospectives
     - Code review feedback
     - Test results and edge cases found during implementation

3. **Determine Scenario Type**:
   - **Extension**: Adding detail to existing scenario
   - **Edge Case**: Handling special conditions
   - **Error Case**: New error handling requirement
   - **New Feature**: Entirely new capability discovered

4. **Create or Update Scenario Document**:
   - For existing features: Update `docs/use_cases/<feature>.md`
   - For new aspects: Create `docs/use_cases/evolved/<feature>-<aspect>.md`
   - Use the following template (content in Japanese):

```markdown
# 進化したユースケース: <Feature Name>

## 変更理由
- **発見時期**: Sprint <number>
- **フィードバック源**: <Sprint review/User feedback/Testing>
- **重要度**: <High/Medium/Low>

## 新規/更新シナリオ

### シナリオ<N>: <New Scenario Name>
- **Given**: <Preconditions>
- **When**: <Action>
- **Then**: <Expected Result>
- **追加理由**: <Why this scenario was added>

### シナリオ<N+1>: <Edge Case>
- **Given**: <Preconditions>
- **When**: <Action>
- **Then**: <Expected Result>
- **発見経緯**: <How this case was discovered>

## ドメインへの影響
- **新規概念**: <New domain concepts if any>
- **既存概念の変更**: <Changes to existing concepts>
- **ユビキタス言語の追加**:
  - <New term>: <Definition>

## 実装への影響
- **影響を受けるレイヤー**: <Domain/Application/Infrastructure/Presentation>
- **必要な変更**:
  - <Change 1>
  - <Change 2>
- **推定工数**: <Days>

## 関連するコアシナリオ
- [<Core scenario name>](../core/<filename>.md)
- 関係性: <How it relates>
```

5. **Create GitHub Issue for New Scenario**:
   - Create issue immediately when adding scenario
   - Ensure consistency between scenario and ticket
   - Use command:
   ```bash
   gh issue create \
     --title "実装: <Scenario name>" \
     --body "## 概要\n<Description>\n\n## シナリオ\n- Given: <condition>\n- When: <action>\n- Then: <result>\n\n## 発見経緯\n<Discovery context>\n\n## 関連ドキュメント\n- [進化シナリオ](docs/use_cases/evolved/<filename>.md)" \
     --label "enhancement,evolved-scenario"
   ```

6. **Update Scenario Index**:
   - Update `docs/use_cases/index.md` with new scenarios
   - Maintain traceability (content in Japanese):

```markdown
## 進化したシナリオ (Sprint <number>)
- [<Scenario name>](evolved/<filename>.md) - Issue #<number>
  - 追加理由: <Brief reason>
  - ステータス: <Pending/In Progress/Completed>
```

7. **Validate Consistency**:
   - Check alignment with overall vision
   - Ensure no conflicts with existing scenarios
   - Verify ubiquitous language consistency
   - Confirm testability of new scenarios

8. **Update Sprint Documentation**:
   - Determine which sprint the new scenario belongs to:
     - Current sprint if capacity allows and aligns with sprint goal
     - Next sprint if current sprint is full or scenario is lower priority
   - Update appropriate sprint documents:
     
   a. **For Current Sprint**:
      - Update `docs/sprints/sprint-<current>-backlog.md` with new issue
      - Add to active sprint tracking
   
   b. **For Future Sprint**:
      - Create/update `docs/sprints/sprint-<next>-backlog.md`
      - Mark as "ready for sprint planning"
   
   c. **Create Evolution Report**:
      - File: `docs/sprints/sprint-<number>-evolution.md`

```markdown
# スプリント<number> シナリオ進化

## 追加されたシナリオ
1. <Scenario name> - Issue #<number>
   - 優先度: <Priority>
   - 実装タイミング: <This sprint/Next sprint>

## ビジョンへの影響
<Impact on overall vision if any>

## 学習事項
<What we learned that led to these additions>
```

9. **Guide Next Steps**:
   - Display created issue number
   - Suggest next commands in Japanese:
     - `/create-tests <issue-number>` - Create tests for new scenario
     - `/sprint-planning <next-sprint>` - Plan next sprint with new scenarios

Important Notes:
- Always create issue and scenario documentation together
- Maintain traceability between feedback and changes
- Keep evolved scenarios separate from core for clarity
- Don't modify core scenarios directly (unless fundamental change)
- Consider impact on existing implementation
- All user-facing output in Japanese