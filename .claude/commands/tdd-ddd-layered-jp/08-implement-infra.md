永続化と外部サービスのためのインフラストラクチャ層を実装します。

以下の手順に従ってください：

1. **引数の確認**:

   - `$ARGUMENTS`が提供されていることを確認
   - 提供されていない場合は直ちに終了し、イシュー番号引数を渡すように日本語でユーザーに促す

2. **前提条件の確認**:

   - ドメイン層とアプリケーション層が実装されていることを確認
   - `domain/repositories/`にリポジトリインターフェースがあることを確認
   - 必要な外部依存関係を特定

3. **インフラストラクチャ構造の作成**:

   ```
   infrastructure/
   ├── repositories/
   ├── persistence/
   │   ├── models/
   │   └── mappers/
   ├── external/
   └── config/
   ```

4. **リポジトリ具象クラスの実装**:

   - 永続化技術を選択（例：SQLAlchemy、MongoDB）
   - `infrastructure/repositories/`に具象実装を作成

   SQLAlchemy を使った例:

   ```python
   # infrastructure/repositories/sql_<repository>.py
   class Sql<Repository>(<RepositoryInterface>):
       def __init__(self, session):
           self._session = session

       def save(self, entity):
           model = self._to_model(entity)
           self._session.add(model)
           self._session.commit()

       def find_by_id(self, id):
           model = self._session.query(<Model>).filter_by(id=id).first()
           return self._to_entity(model) if model else None

       def _to_model(self, entity):
           # ドメインエンティティをDBモデルにマッピング
           pass

       def _to_entity(self, model):
           # DBモデルをドメインエンティティにマッピング
           pass
   ```

5. **データベースモデルの作成**:

   - `infrastructure/persistence/models/`に ORM モデルを定義
   - モデルをドメインエンティティと分離した状態で保つ

   例:

   ```python
   # infrastructure/persistence/models/<model>.py
   class <Model>(Base):
       __tablename__ = '<table_name>'

       id = Column(Integer, primary_key=True)
       # その他のカラム
   ```

6. **マッパーの実装**:

   - `infrastructure/persistence/mappers/`にマッパーを作成
   - ドメインオブジェクトと DB モデル間の変換を処理
   - 値オブジェクトの適切な処理を確保

7. **データベースマイグレーション**:

   - マイグレーションツールを設定（例：Alembic）
   - 機能のための初期マイグレーションを作成
   - マイグレーションコマンドをドキュメント化

8. **外部サービスアダプター**（必要な場合）:

   - `infrastructure/external/`にアダプターを実装
   - ドメインを独立した状態に保つためにインターフェースを使用
   - API 呼び出し、メッセージキューなどを処理

9. **設定管理**:

   - `infrastructure/config/`に設定ファイルを作成
   - データベース接続を処理
   - 環境固有の設定

10. **統合テストの作成**:

- リアルデータベースでリポジトリをテスト
- テストデータベースまたはインメモリ DB を使用
- トランザクション処理をテスト

```python
# tests/integration/repositories/test_sql_<repository>.py
def test_save_and_find():
    # リアルデータベース接続でテスト
    pass
```

11. **すべてのテストの実行**:

    - ユニットテスト: `pytest tests/unit/`
    - 統合テスト: `pytest tests/integration/`
    - すべてのテストが成功することを確認

12. **ドキュメントの更新**:

    - インフラストラクチャの選択をドキュメント化
    - データベースのセットアップ手順を追加
    - 接続文字列の例を含める

13. **イシューの更新**:

    - コメント: `gh issue comment $ARGUMENTS --body "インフラストラクチャ層の実装を完了しました。データベース永続化と外部サービス連携が可能になりました。"`

14. **次のステップの案内**:
    - 日本語でプレゼンテーション層の実装（`/implement-presentation`）を推奨
    - またはエンドツーエンドテストを推奨

重要な注意事項:

- インフラストラクチャの詳細をドメインから分離した状態に保つ
- 柔軟性のために依存性注入を使用
- 可能な限りリアルインフラストラクチャでテスト
- コネクションプーリングとトランザクションを適切に処理
- Unit of Work パターンでリポジトリパターンの使用を検討
- すべてのユーザー向け出力は日本語で行う必要があります
