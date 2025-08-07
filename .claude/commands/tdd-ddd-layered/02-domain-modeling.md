Design domain models based on the Given-When-Then specification.

Follow these steps:

1. **Check Arguments**:
   - Verify that `$ARGUMENTS` is provided
   - If not provided, terminate immediately and prompt the user to pass the issue number argument in Japanese

2. **Check Prerequisites**:
   - Verify that use case specification exists in `docs/use_cases/`
   - If `$ARGUMENTS` is provided, look for `docs/use_cases/issue-$ARGUMENTS-*.md`
   - If no specification found, prompt user in Japanese to run `/create-use-case` first

3. **Read Use Case Specification**:
   - Load the Given-When-Then specification file
   - Extract domain concepts and relationships
   - Identify entities, value objects, and domain services

4. **Create Domain Model Design**:
   - Create `docs/domain/` directory if it doesn't exist
   - Create design document `docs/domain/issue-$ARGUMENTS-domain-model.md`
   - Write the design in JAPANESE using the following template:

```markdown
# ドメインモデル設計: <機能名>

Issue: #$ARGUMENTS
仕様: docs/use_cases/issue-$ARGUMENTS-<feature-name>.md

## エンティティ

### <EntityName>
- **責務**: <エンティティの責務>
- **属性**:
  - id: <型>
  - <属性名>: <型>
- **振る舞い**:
  - <メソッド名>(): <説明>
- **不変条件**:
  - <ビジネスルール>

## 値オブジェクト

### <ValueObjectName>
- **責務**: <値オブジェクトの責務>
- **属性**:
  - <属性名>: <型>
- **振る舞い**:
  - <メソッド名>(): <説明>
- **不変条件**:
  - <制約条件>

## ドメインサービス

### <DomainServiceName>
- **責務**: <サービスの責務>
- **メソッド**:
  - <メソッド名>(<引数>): <戻り値> - <説明>

## リポジトリインターフェース

### <RepositoryName>
- **責務**: <リポジトリの責務>
- **メソッド**:
  - save(<Entity>): void
  - findById(id): <Entity>
  - <その他のメソッド>

## 集約境界
- **集約ルート**: <EntityName>
- **集約内エンティティ**: [<Entity1>, <Entity2>]
- **トランザクション境界**: <説明>

## ドメインイベント（必要な場合）
### <EventName>
- **発生タイミング**: <いつ発生するか>
- **含まれる情報**: <イベントデータ>
```

5. **Create Initial Folder Structure**:
   - Create the following directory structure:
   ```
   domain/
   ├── entities/
   ├── value_objects/
   ├── services/
   ├── repositories/
   └── events/
   ```

6. **Validate Domain Model**:
   - Ensure all scenarios from use case can be implemented
   - Check that business rules are enforced
   - Verify aggregate boundaries are correct

7. **Document Design Decisions**:
   - Add rationale for key design choices
   - Note any assumptions or constraints
   - List questions for stakeholder review if needed

8. **Update Issue**:
   - Comment on issue: `gh issue comment $ARGUMENTS --body "ドメインモデル設計を完了しました: docs/domain/issue-$ARGUMENTS-domain-model.md"`

9. **Guide Next Steps**:
   - Suggest creating tests (`/create-tests`) in Japanese
   - Remind to review the model before implementation

Important Notes:
- Focus on domain logic, not technical implementation
- Use ubiquitous language from the specification
- Keep aggregates small and cohesive
- Define clear boundaries and invariants
- All user-facing output must be in JAPANESE