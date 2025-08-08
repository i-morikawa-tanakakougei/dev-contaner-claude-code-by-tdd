TDD/DDD/レイヤードアーキテクチャ実装のプルリクエストを作成し、issueをクローズします。

以下の手順に従ってください：

1. **引数の確認**:
   - `$ARGUMENTS`が提供されているかを確認
   - 提供されていない場合は即座に終了し、issue番号引数を渡すようユーザーに日本語でプロンプト

2. **実装完了性の確認**:
   - 必要なドキュメントがすべて存在することを確認:
     - `docs/use_cases/issue-$ARGUMENTS-*.md`
     - `docs/domain/issue-$ARGUMENTS-*.md`
     - `docs/test_plan/issue-$ARGUMENTS-*.md`
     - `docs/test_report/issue-$ARGUMENTS-*.md`
     - `docs/review/issue-$ARGUMENTS-*.md`

3. **最終テストスイートの実行**:
   ```bash
   # カバレッジ付きで全テストを実行
   uv run --frozen pytest --cov=domain --cov=application --cov=infrastructure --cov=presentation \
          --cov-report=term --cov-fail-under=80
   ```
   - すべてのテストがパスすることを確認
   - カバレッジが要件を満たすことを確認
   - 失敗がある場合は、先に進む前に修正

4. **最終品質チェックの実行**:
   ```bash
   # Linting
   uv run --frozen ruff check .
   
   # 型チェック
   uv run --frozen pyright
   
   # フォーマットチェック
   uv run --frozen ruff format --check .
   ```
   - 見つかった問題を修正

5. **Git状態の確認**:
   ```bash
   git status
   ```
   - すべての変更をレビュー
   - 一時的ファイルやデバッグファイルがないことを確認

6. **機能ブランチの作成**（まだ作成していない場合）:
   ```bash
   git checkout -b feature/issue-$ARGUMENTS-<機能名>
   ```

7. **すべての変更をステージング・コミット**:
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

8. **リモートへのプッシュ**:
   ```bash
   git push -u origin feature/issue-$ARGUMENTS-<機能名>
   ```

9. **PR情報の収集**:
   - issue詳細の読み込み: `gh issue view $ARGUMENTS`
   - ユースケース仕様の読み込み
   - テストレポートの読み込み
   - レビューレポートの読み込み

10. **プルリクエストの作成**:
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

11. **PRとissueのリンク**:
    ```bash
    # 作成出力からPR番号を取得
    PR_NUMBER=<created_pr_number>
    
    # issueにコメント追加
    gh issue comment $ARGUMENTS --body "プルリクエストを作成しました: #$PR_NUMBER
    
    実装完了項目:
    - ✅ TDDによる開発（RED-GREEN-REFACTOR）
    - ✅ DDDに基づくドメインモデル設計
    - ✅ レイヤードアーキテクチャの実装
    - ✅ Given-When-Thenシナリオの完全実装
    - ✅ テストカバレッジ X%達成
    
    レビューをお願いします。"
    ```

12. **サマリードキュメントの作成**:
    `docs/implementation-summary/issue-$ARGUMENTS-summary.md`を作成:

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

13. **最終サマリーの表示**:
    日本語で完了メッセージを表示:
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

重要な注意事項:
- PR作成前にすべてのテストがパスすることを確認
- 包括的なPR説明を含める
- 常に i-morikawa-tanakakougei をレビュアーに追加
- 自動クローズのためにPRとissueをリンク
- 実装の全工程を文書化
- すべての出力とドキュメントは日本語で記述
- 絵文字は控えめに使用し、最終のお祝いメッセージでのみ使用