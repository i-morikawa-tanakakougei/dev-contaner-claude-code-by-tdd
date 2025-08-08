ドメインロジックを統理するアプリケーション層のユースケースを実装します。

以下の手順に従ってください：

1. **引数の確認**:

   - `$ARGUMENTS`が提供されていることを確認
   - 提供されていない場合は直ちに終了し、イシュー番号引数を渡すように日本語でユーザーに促す

2. **前提条件の確認**:

   - ドメイン実装が存在し、テストが成功していることを確認
   - `tests/unit/application/use_cases/`にユースケーステストが存在することを確認
   - ユースケーステストを実行して失敗していることを確認

3. **アプリケーション層構造の作成**:

   - ディレクトリを作成:

   ```
   application/
   ├── use_cases/
   ├── dtos/
   └── exceptions/
   ```

4. **ユースケースの実装**:

   - `application/use_cases/`にユースケースファイルを作成
   - 各ユースケースはドメインオブジェクトを統理する必要がある
   - アプリケーションレベルの関心事（トランザクション、認証）を処理
   - リポジトリに依存性注入を使用

   例構造:

   ```python
   # application/use_cases/<use_case_name>.py
   class <UseCaseName>:
       def __init__(self, repository: <RepositoryInterface>):
           self._repository = repository

       def execute(self, request: <RequestDTO>) -> <ResponseDTO>:
           # 1. リクエストのバリデーション
           # 2. ドメインオブジェクトの読み込み
           # 3. ドメインロジックの実行
           # 4. 変更の永続化
           # 5. レスポンスの返却
           pass
   ```

5. **DTO（Data Transfer Object）の作成**:

   - `application/dtos/`にリクエスト/レスポンス DTO を作成
   - DTO はシンプルでデータ転送に焦点を当てたものにする
   - リクエスト DTO にバリデーションを含める

   例:

   ```python
   # application/dtos/<feature>_dtos.py
   @dataclass
   class <Feature>Request:
       # リクエストフィールド

       def validate(self):
           # バリデーションロジック
           pass

   @dataclass
   class <Feature>Response:
       # レスポンスフィールド
   ```

6. **アプリケーション例外の定義**:

   - `application/exceptions/`にカスタム例外を作成
   - ビジネスルール違反と技術的エラーを区別

7. **モックリポジトリの実装**:

   - `infrastructure/repositories/`にインメモリ実装を作成
   - データベースなしでテストするために使用

   例:

   ```python
   # infrastructure/repositories/mock_<repository>.py
   class Mock<Repository>(<RepositoryInterface>):
       def __init__(self):
           self._storage = {}

       def save(self, entity):
           self._storage[entity.id] = entity

       def find_by_id(self, id):
           return self._storage.get(id)
   ```

8. **ユースケーステストの実行**:

   - 実行: `pytest tests/unit/application/use_cases/ -v`
   - すべてのユースケーステストが GREEN になっていることを確認
   - 失敗するテストを修正

9. **統合テスト**:

   - ユースケースとモックリポジトリの統合テストを作成
   - トランザクション境界とエラーハンドリングをテスト

10. **コード品質のチェック**:

- 実行: `ruff check application/`
- 実行: `pyright application/`
- 問題を修正

11. **ドキュメントの更新**:

    - `docs/application/`にユースケースのフローをドキュメント化
    - 複雑な場合はシーケンス図を含める

12. **イシューの更新**:

    - コメント: `gh issue comment $ARGUMENTS --body "アプリケーション層（ユースケース）の実装を完了しました。"`

13. **次のステップの案内**:
    - 日本語でインフラストラクチャの実装（`/implement-infra`）を推奨
    - インフラストラクチャがシンプルな場合はプレゼンテーション層

重要な注意事項:

- ユースケースは統理し、ビジネスロジックを含まない
- ユースケースを簡素で焦点を絞ったものに保つ
- 入出力には DTO を使用し、ドメインオブジェクトは使用しない
- 横断的関心事（ログイン、認証）を処理
- テストにはモックリポジトリを使用
- すべてのユーザー向け出力は日本語で行う必要があります
