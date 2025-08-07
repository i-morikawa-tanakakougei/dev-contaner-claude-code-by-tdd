テストを成功させるためにドメイン層を実装します（TDD GREEN フェーズ）。

以下の手順に従ってください：

1. **引数の確認**:

   - `$ARGUMENTS`が提供されていることを確認
   - 提供されていない場合は直ちに終了し、イシュー番号引数を渡すように日本語でユーザーに促す

2. **前提条件の確認**:

   - `tests/unit/domain/`にテストが存在することを確認
   - テストを実行して失敗していることを確認（RED フェーズ）
   - テストが見つからない場合は、まず`/create-tests`を実行するように日本語でユーザーに促す

3. **失敗テストの実行**:

   - 実行: `pytest tests/unit/domain/ -v`
   - 失敗テストの出力をキャプチャ
   - 実装が必要なドメインオブジェクトを特定

4. **エンティティの実装**:

   - `domain/entities/`にエンティティファイルを作成
   - テストを成功させるための最低限のコードのみ実装
   - `docs/domain/`のドメインモデル設計に従う
   - ビジネスルールと不変条件が強制されていることを確認

   例構造:

   ```python
   # domain/entities/<entity_name>.py
   class <EntityName>:
       def __init__(self, id, ...):
           self._validate_invariants()
           self.id = id
           # その他の属性

       def _validate_invariants(self):
           # ビジネスルールの検証
           pass

       # ドメインモデルからのビジネスメソッド
   ```

5. **値オブジェクトの実装**:

   - `domain/value_objects/`に値オブジェクトファイルを作成
   - 不変性を確保
   - 値に基づいた等価性を実装
   - コンストラクタでバリデーションを追加

   例構造:

   ```python
   # domain/value_objects/<vo_name>.py
   @dataclass(frozen=True)
   class <ValueObjectName>:
       value: <type>

       def __post_init__(self):
           # バリデーションロジック
           pass
   ```

6. **ドメインサービスの実装**（必要な場合）:

   - `domain/services/`にサービスファイルを作成
   - ステートレスな操作を実装
   - ドメインオブジェクトのみ使用、インフラストラクチャは使用しない

7. **リポジトリインターフェースの定義**:

   - `domain/repositories/`に抽象インターフェースを作成
   - ドメインが必要とするメソッドのみ定義
   - 実装詳細は含めない

   例:

   ```python
   # domain/repositories/<repository_name>.py
   from abc import ABC, abstractmethod

   class <RepositoryName>(ABC):
       @abstractmethod
       def save(self, entity):
           pass

       @abstractmethod
       def find_by_id(self, id):
           pass
   ```

8. **テストの再実行**:

   - 実行: `pytest tests/unit/domain/ -v`
   - すべてのドメインテストが GREEN になっていることを確認
   - 失敗するテストがある場合は実装を反復

9. **コード品質のチェック**:

   - リンターを実行: `ruff check domain/`
   - タイプチェッカーを実行: `pyright domain/`
   - 発見された問題を修正

10. **実装のドキュメント化**:

- 変更があった場合は`docs/domain/issue-$ARGUMENTS-domain-model.md`を更新
- 設計が進化した場合は実装ノートを追加

11. **イシューの更新**:

    - コメント: `gh issue comment $ARGUMENTS --body "ドメイン層の実装を完了しました（GREEN phase）。すべてのドメインテストが成功しています。"`

12. **次のステップの案内**:
    - 日本語でユースケースの実装（`/implement-usecase`）を推奨
    - または必要に応じてリファクタリングを推奨

重要な注意事項:

- テストを成功させるために必要なことのみ実装する
- 技術的な関心事ではなく、ドメインロジックに焦点を当てる
- エンティティと値オブジェクトを純粋に保つ（I/O なし）
- 不変条件とビジネスルールを強制する
- すべてのコードにタイプヒントを使用する
- すべてのユーザー向け出力は日本語で行う必要があります
