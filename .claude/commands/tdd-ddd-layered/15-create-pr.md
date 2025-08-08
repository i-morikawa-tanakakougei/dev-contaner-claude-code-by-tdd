Create Pull Request for TDD/DDD/Layered Architecture implementation and close the issue.

Follow these steps:

1. **Check Arguments**:
   - Verify that `$ARGUMENTS` is provided
   - If not provided, terminate immediately and prompt the user to pass the issue number argument in Japanese

2. **Verify Implementation Completeness**:
   - Check all required documents exist:
     - `docs/use_cases/issue-$ARGUMENTS-*.md`
     - `docs/domain/issue-$ARGUMENTS-*.md`
     - `docs/test_plan/issue-$ARGUMENTS-*.md`
     - `docs/test_report/issue-$ARGUMENTS-*.md`
     - `docs/review/issue-$ARGUMENTS-*.md`

3. **Run Final Test Suite**:
   ```bash
   # Run all tests with coverage
   pytest --cov=domain --cov=application --cov=infrastructure --cov=presentation \
          --cov-report=term --cov-fail-under=80
   ```
   - Ensure all tests pass
   - Verify coverage meets requirements
   - If any failures, stop and fix before proceeding

4. **Run Final Quality Checks**:
   ```bash
   # Linting
   ruff check .
   
   # Type checking
   pyright
   
   # Format check
   ruff format --check .
   ```
   - Fix any issues found

5. **Check Git Status**:
   ```bash
   git status
   ```
   - Review all changes
   - Ensure no temporary or debug files

6. **Create Feature Branch** (if not on one):
   ```bash
   git checkout -b feature/issue-$ARGUMENTS-<feature-name>
   ```

7. **Stage and Commit All Changes**:
   ```bash
   git add .
   git commit -m "feat: #$ARGUMENTS <機能名>の実装

   TDD/DDD/レイヤードアーキテクチャによる実装を完了

   実装内容:
   - ドメイン層: エンティティ、値オブジェクト、ドメインサービス
   - アプリケーション層: ユースケース、DTO
   - インフラストラクチャ層: リポジトリ実装、永続化
   - プレゼンテーション層: APIエンドポイント/CLI
   
   テスト:
   - ユニットテスト: X件
   - 統合テスト: Y件
   - E2Eテスト: Z件
   - カバレッジ: X%
   
   ドキュメント:
   - ユースケース仕様
   - ドメインモデル設計
   - テスト計画・レポート
   - レビューレポート"
   ```

8. **Push to Remote**:
   ```bash
   git push -u origin feature/issue-$ARGUMENTS-<feature-name>
   ```

9. **Gather PR Information**:
   - Read issue details: `gh issue view $ARGUMENTS`
   - Read use case specification
   - Read test report
   - Read review report

10. **Create Pull Request**:
    ```bash
    gh pr create \
      --title "feat: #$ARGUMENTS <機能名>の実装 (TDD/DDD/レイヤードアーキテクチャ)" \
      --body "$(cat <<'EOF'
## 概要
Issue #$ARGUMENTS の実装を完了しました。
TDD/DDD/レイヤードアーキテクチャに基づいて開発を行いました。

## 実装内容

### アーキテクチャ
- **開発手法**: TDD (Test-Driven Development)
- **設計手法**: DDD (Domain-Driven Design)  
- **アーキテクチャ**: レイヤードアーキテクチャ

### 各レイヤーの実装

#### ドメイン層
- エンティティ: `<Entity1>`, `<Entity2>`
- 値オブジェクト: `<ValueObject1>`, `<ValueObject2>`
- ドメインサービス: `<DomainService>`
- リポジトリインターフェース: `<Repository>`

#### アプリケーション層
- ユースケース: `<UseCase1>`, `<UseCase2>`
- DTO: Request/Response DTOs
- 例外: カスタム例外クラス

#### インフラストラクチャ層
- リポジトリ実装: `<ConcreteRepository>`
- 永続化: <使用技術>
- 外部サービス連携: <該当する場合>

#### プレゼンテーション層
- <API/CLI/Web>: `<エンドポイント/コマンド>`
- 入力検証: バリデーション実装
- エラーハンドリング: 統一エラーレスポンス

## Given-When-Thenシナリオ

実装したシナリオ:
- ✅ 基本成功ケース
- ✅ エッジケース: <内容>
- ✅ エラーケース: <内容>

詳細: `docs/use_cases/issue-$ARGUMENTS-*.md`

## テスト結果

| テスト種別 | 件数 | 結果 |
|-----------|------|------|
| ユニットテスト | X件 | ✅ All Pass |
| 統合テスト | Y件 | ✅ All Pass |
| E2Eテスト | Z件 | ✅ All Pass |

**テストカバレッジ**: X% (基準: 80%以上)

詳細: `docs/test_report/issue-$ARGUMENTS-*.md`

## 品質メトリクス

| チェック項目 | 結果 |
|------------|------|
| Ruff (Linting) | ✅ エラーなし |
| Pyright (Type Check) | ✅ エラーなし |
| 循環的複雑度 | 最大 X (基準: <10) |

## ドキュメント

- 📝 [ユースケース仕様](docs/use_cases/issue-$ARGUMENTS-*.md)
- 📐 [ドメインモデル設計](docs/domain/issue-$ARGUMENTS-*.md)
- 🧪 [テスト計画](docs/test_plan/issue-$ARGUMENTS-*.md)
- 📊 [テストレポート](docs/test_report/issue-$ARGUMENTS-*.md)
- ✅ [レビューレポート](docs/review/issue-$ARGUMENTS-*.md)

## DDD原則の遵守

- ✅ ユビキタス言語の使用
- ✅ 集約境界の適切な設定
- ✅ ドメインロジックの純粋性維持
- ✅ 値オブジェクトの不変性

## レイヤードアーキテクチャの遵守

- ✅ レイヤー間の依存方向が正しい
- ✅ 各レイヤーの責務が明確
- ✅ 依存性注入の活用
- ✅ インフラ詳細の隔離

## 動作確認方法

### APIの場合
\`\`\`bash
# サーバー起動
python -m presentation.api.app

# テストリクエスト
curl -X POST http://localhost:8000/<endpoint> \
  -H "Content-Type: application/json" \
  -d '{"field": "value"}'
\`\`\`

### CLIの場合
\`\`\`bash
# コマンド実行
python -m presentation.cli.<command> --param value
\`\`\`

## チェックリスト

- [x] すべてのテストがパス
- [x] カバレッジ80%以上
- [x] コード品質チェックパス
- [x] ドキュメント作成完了
- [x] Given-When-Thenシナリオ実装完了
- [x] DDD原則遵守
- [x] レイヤードアーキテクチャ遵守

## 関連Issue
Closes #$ARGUMENTS

## レビュアー
@i-morikawa-tanakakougei

## 備考
TDD/DDD/レイヤードアーキテクチャの実践により、保守性・拡張性の高い実装を実現しました。
EOF
)" \
      --assignee @me \
      --reviewer i-morikawa-tanakakougei
    ```

11. **Link PR to Issue**:
    ```bash
    # Get PR number from creation output
    PR_NUMBER=<created_pr_number>
    
    # Add comment to issue
    gh issue comment $ARGUMENTS --body "プルリクエストを作成しました: #$PR_NUMBER
    
    実装完了項目:
    - ✅ TDDによる開発（RED-GREEN-REFACTOR）
    - ✅ DDDに基づくドメインモデル設計
    - ✅ レイヤードアーキテクチャの実装
    - ✅ Given-When-Thenシナリオの完全実装
    - ✅ テストカバレッジ X%達成
    
    レビューをお願いします。"
    ```

12. **Create Summary Document**:
    Create `docs/implementation-summary/issue-$ARGUMENTS-summary.md`:

```markdown
# 実装サマリー: <機能名>

Issue: #$ARGUMENTS
PR: #<PR_NUMBER>
実装期間: <開始日> - <終了日>

## 実装プロセス

1. ✅ ビジョン確認・ユースケース作成
2. ✅ ドメインモデル設計
3. ✅ TDDテスト作成（RED）
4. ✅ ドメイン層実装（GREEN）
5. ✅ アプリケーション層実装
6. ✅ インフラストラクチャ層実装
7. ✅ プレゼンテーション層実装
8. ✅ リファクタリング（REFACTOR）
9. ✅ 全テスト実行
10. ✅ レビュー実施
11. ✅ フィードバック反映
12. ✅ プルリクエスト作成

## 成果物

### コード
- ドメイン層: X ファイル
- アプリケーション層: Y ファイル
- インフラストラクチャ層: Z ファイル
- プレゼンテーション層: W ファイル

### テスト
- 総テスト数: X件
- カバレッジ: Y%

### ドキュメント
- 設計ドキュメント: X件
- テストドキュメント: Y件
- レビュードキュメント: Z件

## 学習と改善点

### うまくいった点
- <良かった点1>
- <良かった点2>

### 改善が必要な点
- <改善点1>
- <改善点2>

### 次回への提案
- <提案1>
- <提案2>
```

13. **Display Final Summary**:
    Show completion message in Japanese:
    ```
    プルリクエスト作成完了！
    
    Issue: #$ARGUMENTS
    PR: #<PR_NUMBER>
    
    実装成果:
    - アーキテクチャ: TDD/DDD/レイヤード ✅
    - テストカバレッジ: X% ✅
    - 品質チェック: すべてパス ✅
    
    次のアクション:
    - レビュアーからのフィードバック待ち
    - 必要に応じて修正対応
    - マージ後、issueは自動的にクローズされます
    
    お疲れ様でした！🎉
    ```

Important Notes:
- Ensure all tests pass before creating PR
- Include comprehensive PR description
- Always add i-morikawa-tanakakougei as reviewer
- Link PR to issue for automatic closing
- Document the entire implementation journey
- All output and documentation must be in JAPANESE
- Use emojis sparingly and only in final celebration message