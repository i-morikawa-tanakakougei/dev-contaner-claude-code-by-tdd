プレゼンテーション層（API エンドポイント、CLI、または UI）を実装します。

以下の手順に従ってください：

1. **引数の確認**:

   - `$ARGUMENTS`が提供されていることを確認
   - 提供されていない場合は直ちに終了し、イシュー番号引数を渡すように日本語でユーザーに促す

2. **前提条件の確認**:

   - すべての他の層が実装されていることを確認
   - 統合テストでユースケースが動作していることを確認
   - プレゼンテーションタイプを決定（REST API: FastApi、GraphQL、CLI、Web: FastHtml など）

3. **プレゼンテーション構造の作成**:

   ```
   presentation/
   ├── api/          # REST/GraphQL用
   │   ├── controllers/
   │   ├── validators/
   │   └── serializers/
   ├── cli/          # コマンドラインインターフェース用
   └── web/          # Web UI用
   ```

4. **REST API 実装の場合**:

   a. **コントローラーの作成**:

   ```python
   # presentation/api/controllers/<feature>_controller.py
   class <Feature>Controller:
       def __init__(self, use_case: <UseCase>):
           self._use_case = use_case

       def handle_post(self, request_data: dict) -> dict:
           # 1. 入力のバリデーション
           # 2. DTOへの変換
           # 3. ユースケースの呼び出し
           # 4. レスポンスのシリアライズ
           # 5. エラー処理
           pass
   ```

   b. **入力バリデーション**:

   ```python
   # presentation/api/validators/<feature>_validator.py
   def validate_<feature>_request(data: dict) -> dict:
       # 必須フィールドのバリデーション
       # データ型のチェック
       # バリデーション済みデータを返すか、ValidationErrorを発生
       pass
   ```

   c. **レスポンスシリアライゼーション**:

   ```python
   # presentation/api/serializers/<feature>_serializer.py
   def serialize_<feature>_response(response: <ResponseDTO>) -> dict:
       # DTOをJSONシリアライズ可能なdictに変換
       pass
   ```

5. **REST API フレームワークの設定**（例：FastAPI）:

   ```python
   # presentation/api/app.py
   from fastapi import FastAPI, HTTPException

   app = FastAPI()

   @app.post("/<resource>")
   async def create_<resource>(request: <RequestModel>):
       try:
           controller = <Feature>Controller(use_case)
           response = controller.handle_post(request.dict())
           return response
       except ValidationError as e:
           raise HTTPException(status_code=400, detail=str(e))
   ```

6. **エラーハンドリング**:

   - ドメイン例外を HTTP ステータスコードにマッピング
   - 一貫したエラーレスポンス形式を作成
   - エラーを適切にログ出力

7. **E2E テストの作成**:

   ```python
   # tests/e2e/api/test_<feature>_api.py
   def test_create_<resource>_success():
       # 成功したAPI呼び出しのテスト
       response = client.post("/<resource>", json={...})
       assert response.status_code == 201

   def test_create_<resource>_validation_error():
       # バリデーションエラーのテスト
       response = client.post("/<resource>", json={})
       assert response.status_code == 400
   ```

8. **API ドキュメント**:

   - OpenAPI/Swagger ドキュメントを生成
   - リクエスト/レスポンススキーマをドキュメント化
   - リクエスト例を含める

9. **CLI 実装の場合**:

   ```python
   # presentation/cli/<feature>_commands.py
   import click

   @click.command()
   @click.option('--param', required=True)
   def <feature>_command(param):
       """コマンドラインから<feature>ユースケースを実行"""
       # APIコントローラーと同様のフロー
       pass
   ```

10. **依存性注入の設定**:

- すべての依存関係を接続
- データベース接続を設定
- ログ設定をセットアップ

11. **フルテストスイートの実行**:

    - ユニットテスト: `pytest tests/unit/`
    - 統合テスト: `pytest tests/integration/`
    - E2E テスト: `pytest tests/e2e/`
    - すべてが成功する必要があります

12. **使用ドキュメントの作成**:

    - API エンドポイントドキュメント
    - curl コマンドの例
    - セットアップ手順

13. **イシューの更新**:

    - コメント: `gh issue comment $ARGUMENTS --body "プレゼンテーション層の実装を完了しました。APIエンドポイントが利用可能です。"`
    - API 呼び出しの例を含める

14. **最終ステップ**:
    - 日本語でフル統合テストの実行を推奨
    - 実装した機能の概要を提供
    - デプロイオプションの案内

重要な注意事項:

- プレゼンテーション層を薄く保つ
- コントローラーにビジネスロジックは含めない
- 適切な HTTP ステータスコードとエラーメッセージ
- API バージョニング戦略を検討
- セキュリティの配慮（認証、CORS、レート制限）
- すべてのユーザー向け出力は日本語で行う必要があります
