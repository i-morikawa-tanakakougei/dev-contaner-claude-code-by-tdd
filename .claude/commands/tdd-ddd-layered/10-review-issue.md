Review TDD/DDD/Layered Architecture implementation for the issue.

Follow these steps:

1. **Check Arguments**:
   - Verify that `$ARGUMENTS` is provided
   - If not provided, terminate immediately and prompt the user to pass the issue number argument in Japanese

2. **Gather Implementation Artifacts**:
   - Check for all expected documents and code:
     - Use case specification: `docs/use_cases/issue-$ARGUMENTS-*.md`
     - Domain model: `docs/domain/issue-$ARGUMENTS-*.md`
     - Test plan: `docs/test_plan/issue-$ARGUMENTS-*.md`
     - Test report: `docs/test_report/issue-$ARGUMENTS-*.md`

3. **Review Domain Layer**:
   - Check entities in `domain/entities/`
   - Review value objects in `domain/value_objects/`
   - Verify domain services follow DDD principles
   - Ensure business rules are properly encapsulated
   - Validate aggregate boundaries

4. **Review Application Layer**:
   - Check use cases in `application/use_cases/`
   - Verify DTOs are properly defined
   - Ensure use cases only orchestrate, not contain business logic
   - Check proper separation of concerns

5. **Review Infrastructure Layer**:
   - Verify repository implementations
   - Check database models and mappers
   - Ensure infrastructure details don't leak to domain
   - Review external service adapters

6. **Review Presentation Layer**:
   - Check API endpoints or CLI commands
   - Verify input validation
   - Review error handling and responses
   - Ensure no business logic in controllers

7. **Test Coverage Analysis**:
   ```bash
   pytest --cov=domain --cov=application --cov=infrastructure --cov=presentation \
          --cov-report=term-missing
   ```
   - Verify coverage is above 80%
   - Check for untested critical paths

8. **Code Quality Checks**:
   ```bash
   # Linting
   ruff check . --statistics
   
   # Type checking
   pyright --stats
   
   # Complexity analysis
   # Check for functions with cyclomatic complexity > 10
   ```

9. **Architecture Compliance Check**:
   - Verify no circular dependencies between layers
   - Check dependency direction: Presentation → Application → Domain
   - Ensure domain has no external dependencies
   - Validate proper use of dependency injection

10. **Given-When-Then Verification**:
    - Verify all scenarios from use case spec are implemented
    - Check test coverage for each scenario
    - Ensure tests follow Given-When-Then structure

11. **Create Review Report**:
    Create `docs/review/issue-$ARGUMENTS-review.md` in Japanese:

```markdown
# レビューレポート: <機能名>

Issue: #$ARGUMENTS
レビュー日時: <timestamp>

## 実装成果物の確認

### ドキュメント
- [x] ユースケース仕様: docs/use_cases/issue-$ARGUMENTS-*.md
- [x] ドメインモデル設計: docs/domain/issue-$ARGUMENTS-*.md
- [x] テスト計画: docs/test_plan/issue-$ARGUMENTS-*.md
- [x] テストレポート: docs/test_report/issue-$ARGUMENTS-*.md

### 実装レイヤー
- [x] ドメイン層
- [x] アプリケーション層
- [x] インフラストラクチャ層
- [x] プレゼンテーション層

## アーキテクチャ準拠性

### DDD原則
- [ ] ユビキタス言語の一貫性
- [ ] 集約境界の適切性
- [ ] ドメインロジックの純粋性
- [ ] 値オブジェクトの不変性

### レイヤードアーキテクチャ
- [ ] レイヤー間の依存方向
- [ ] 関心の分離
- [ ] 依存性注入の活用

### TDD実践
- [ ] RED-GREEN-REFACTORサイクル
- [ ] テストファースト開発
- [ ] テストカバレッジ: X%

## 品質メトリクス

| メトリクス | 結果 | 基準 | 評価 |
|-----------|------|------|------|
| テストカバレッジ | X% | >80% | ✅/❌ |
| 循環的複雑度（最大） | X | <10 | ✅/❌ |
| Ruffエラー数 | X | 0 | ✅/❌ |
| Pyrightエラー数 | X | 0 | ✅/❌ |

## 改善提案

### 必須対応項目
1. <重要度：高の改善点>
2. <重要度：高の改善点>

### 推奨改善項目
1. <重要度：中の改善点>
2. <重要度：中の改善点>

### 将来的な改善案
1. <重要度：低の改善点>
2. <重要度：低の改善点>

## Given-When-Thenシナリオ実装状況

| シナリオ | 実装 | テスト | カバレッジ |
|---------|------|--------|------------|
| 基本成功ケース | ✅ | ✅ | 100% |
| エッジケース1 | ✅ | ✅ | 100% |
| エラーケース1 | ✅ | ✅ | 100% |

## 総評

<全体的な評価と次のステップの推奨事項>

## チェックリスト

### ドメイン層
- [ ] エンティティの不変条件が守られている
- [ ] 値オブジェクトが適切に使用されている
- [ ] ドメインサービスが必要最小限
- [ ] リポジトリインターフェースが適切

### アプリケーション層
- [ ] ユースケースが薄く保たれている
- [ ] DTOが適切に定義されている
- [ ] トランザクション境界が明確
- [ ] エラーハンドリングが一貫している

### インフラストラクチャ層
- [ ] リポジトリ実装が効率的
- [ ] マッパーが正しく動作
- [ ] 外部サービス連携が適切
- [ ] 設定管理が環境依存を吸収

### プレゼンテーション層
- [ ] APIが RESTful/適切な設計
- [ ] 入力検証が十分
- [ ] エラーレスポンスが一貫
- [ ] ドキュメントが整備されている
```

12. **Update Issue with Review**:
    ```bash
    gh issue comment $ARGUMENTS --body "@<作成者> レビューを完了しました。詳細は docs/review/issue-$ARGUMENTS-review.md をご確認ください。

    主な確認ポイント:
    - テストカバレッジ: X%
    - アーキテクチャ準拠: ✅
    - 改善提案: X件
    
    次のステップ: /apply-feedback でフィードバックを反映してください。"
    ```

13. **Display Summary**:
    Show review summary in Japanese:
    ```
    レビュー完了！
    
    Issue: #$ARGUMENTS
    
    結果サマリー:
    - アーキテクチャ準拠性: ✅
    - テストカバレッジ: X%
    - 品質基準達成: X/Y項目
    
    改善提案:
    - 必須: X件
    - 推奨: Y件
    
    詳細: docs/review/issue-$ARGUMENTS-review.md
    
    次のコマンド:
    - /apply-feedback $ARGUMENTS - レビューフィードバックを反映
    ```

Important Notes:
- Focus on TDD/DDD/Layered Architecture principles
- Check both code quality and architectural compliance
- Provide actionable feedback with priorities
- Verify Given-When-Then scenarios are fully implemented
- All output and documentation must be in JAPANESE