Create project vision and core scenarios.

Follow these steps:

1. **Define Project Vision**:
   - Clarify overall project goals
   - Identify main Bounded Contexts
   - Define core business value
   - Identify key stakeholders

2. **Create Directory Structure**:
   - Create `docs/vision/` directory
   - Create `docs/use_cases/core/` directory

3. **Create Vision Document**:
   - File: `docs/vision/project-vision.md`
   - Use the following template (content in Japanese):

```markdown
# プロジェクトビジョン

## 概要
<Overall project goals and value proposition>

## Bounded Context
### <Context Name>
- **責務**: <Responsibilities of this context>
- **主要ユースケース**: 
  - <Use case 1>
  - <Use case 2>
  - <Use case 3>

## コアエンティティとドメイン概念
- **<Entity 1>**: <Description>
- **<Entity 2>**: <Description>
- **値オブジェクト**: 
  - <Value Object 1>: <Description>
  - <Value Object 2>: <Description>

## ユビキタス言語
| 用語 | 定義 | 例 |
|------|------|-----|
| <Term 1> | <Definition> | <Example> |
| <Term 2> | <Definition> | <Example> |

## ステークホルダー
- **<Role 1>**: <Expected value>
- **<Role 2>**: <Expected value>

## 非機能要件
- **パフォーマンス**: <Requirements>
- **セキュリティ**: <Requirements>
- **可用性**: <Requirements>
```

4. **Create Core Scenarios (80% Coverage)**:
   - Create Given-When-Then scenarios for each main use case
   - File: `docs/use_cases/core/<usecase-name>.md`
   - Use the following template (content in Japanese):

```markdown
# コアユースケース: <Feature Name>

## 概要
<Problem this use case solves and value it provides>

## ドメイン概念
- <Concept 1>: <Description>
- <Concept 2>: <Description>

## コアシナリオ

### シナリオ1: <Basic Success Case>
- **Given**: <Preconditions>
- **When**: <Action>
- **Then**: <Expected Result>

### シナリオ2: <Alternative Flow>
- **Given**: <Preconditions>
- **When**: <Action>
- **Then**: <Expected Result>

### シナリオ3: <Main Error Case>
- **Given**: <Preconditions>
- **When**: <Action>
- **Then**: <Expected Error Handling>

## 実装優先度
- **優先度**: High/Medium/Low
- **推定工数**: <Days>
- **依存関係**: <Relationships with other use cases>

## 備考
- <Implementation notes>
- <About extensibility>
```

5. **Create Core Scenarios Index**:
   - File: `docs/use_cases/core/index.md`
   - List all core scenarios with priorities (content in Japanese)

```markdown
# コアシナリオ一覧

## 優先度: 高
1. [<Use Case Name>](./<filename>.md) - <Brief description>
2. [<Use Case Name>](./<filename>.md) - <Brief description>

## 優先度: 中
3. [<Use Case Name>](./<filename>.md) - <Brief description>
4. [<Use Case Name>](./<filename>.md) - <Brief description>

## 優先度: 低
5. [<Use Case Name>](./<filename>.md) - <Brief description>

## 推定スプリント配分
- **スプリント1**: Use cases 1, 2
- **スプリント2**: Use cases 3, 4
- **スプリント3**: Use case 5
```

6. **Validation**:
   - Confirm core scenarios cover 80% of the vision
   - Intentionally exclude edge cases (add in later sprints)
   - Check consistency of ubiquitous language
   - Verify each scenario is independently testable

7. **Guide Next Steps**:
   - Suggest next commands in Japanese:
     - `/sprint-planning 1` - First sprint planning
     - `/init-project-structure` - Initialize project structure

Important Notes:
- Limit core scenarios to 3-7 (covering 80% of the whole)
- Exclude edge cases and special cases (add later)
- Create vision as an evolving document
- Always include ubiquitous language definitions
- All user-facing output should be in Japanese