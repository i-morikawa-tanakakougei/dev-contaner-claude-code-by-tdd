Create a Given-When-Then use case specification from a GitHub issue.

Follow these steps:

1. **Check Arguments**:
   - Verify that `$ARGUMENTS` is provided
   - If not provided, terminate immediately and prompt the user to pass the issue number argument in Japanese

2. **Fetch Issue Details**:
   - Use `gh issue view $ARGUMENTS` to get issue details
   - Review the title, description, and comments
   - Prioritize the most recent comments over older ones and the original issue description
   - If there are conflicts between the issue content and newer comments, prioritize the newer comments

3. **Analyze Use Case**:
   - Understand the problem to be solved from the issue
   - Extract business requirements and user stories
   - Identify relevant domain concepts

4. **Create Given-When-Then Specification**:
   - Create `docs/use_cases/` directory if it doesn't exist
   - Create file `docs/use_cases/issue-$ARGUMENTS-<feature-name>.md`
   - Write the specification in JAPANESE using the following template:

```markdown
# ユースケース: <機能名>

Issue: #$ARGUMENTS

## 概要
<issueから抽出した問題の概要と解決方針>

## ドメイン概念
- <概念1>: <説明>
- <概念2>: <説明>

## シナリオ

### シナリオ1: <シナリオ名>
- **Given**: <前提条件>
- **When**: <実行アクション>
- **Then**: <期待される結果>

### シナリオ2: <エッジケース>
- **Given**: <前提条件>
- **When**: <実行アクション>
- **Then**: <期待される結果>

### シナリオ3: <エラーケース>
- **Given**: <前提条件>
- **When**: <実行アクション>
- **Then**: <エラー処理の期待結果>

## 備考
- <実装上の注意点>
- <非機能要件など>
```

5. **Validate Specification**:
   - Confirm the specification meets issue requirements
   - Ensure ubiquitous language is used consistently
   - Verify each scenario is independently testable

6. **Add Comment to Issue**:
   - Use `gh issue comment $ARGUMENTS --body "Given-When-Then仕様を作成しました: docs/use_cases/issue-$ARGUMENTS-<feature-name>.md"`
   - Include the path to the specification file

7. **Guide Next Steps**:
   - Suggest running domain modeling (`/domain-modeling`) in Japanese
   - Or propose specification review

Important Notes:
- Keep scenarios to 3-5 items
- Each scenario must be independently testable
- Define domain language clearly
- Always include edge cases and error cases
- All user-facing output must be in JAPANESE