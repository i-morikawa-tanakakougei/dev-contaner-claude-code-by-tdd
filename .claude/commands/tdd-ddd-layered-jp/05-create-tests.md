Given-When-Then 仕様とドメインモデルに基づいて TDD テストを作成します。

以下の手順に従ってください：

1. **引数の確認**:

   - `$ARGUMENTS`が提供されていることを確認
   - 提供されていない場合は直ちに終了し、イシュー番号引数を渡すように日本語でユーザーに促す

2. **前提条件の確認**:

   - `docs/use_cases/`にユースケース仕様が存在することを確認
   - `docs/domain/`にドメインモデルが存在することを確認
   - 欠けている場合は、前のステップを完了するように日本語でユーザーに促す

3. **仕様の分析**:

   - Given-When-Then シナリオを読み込み
   - ドメインモデル設計を読み込み
   - シナリオをテストケースにマッピング

4. **テスト構造の作成**:

   - テストディレクトリが存在しない場合は作成:

   ```
   tests/
   ├── unit/
   │   ├── domain/
   │   │   ├── entities/
   │   │   └── value_objects/
   │   └── application/
   │       └── use_cases/
   ├── integration/
   │   └── repositories/
   └── e2e/
       └── api/
   ```

5. **ユニットテストの作成（RED フェーズ）**:

   - ドメインエンティティテストから開始
   - 各 Given-When-Then シナリオに対応するテストを作成
   - テストは初期状態では失敗する必要がある（まだ実装がないため）
   - シナリオを反映する明確なテスト名を使用
   - 仕様へのリンクをコメントで含める

   例構造:

   ```python
   def test_<scenario_description>():
       # Given: <前提条件>
       # When: <実行アクション>
       # Then: <期待される結果>
       assert False  # RED: まだ実装されていない
   ```

6. **テストファイルの作成**:

   - ドメインエンティティテスト: `tests/unit/domain/entities/test_<entity_name>.py`
   - 値オブジェクトテスト: `tests/unit/domain/value_objects/test_<vo_name>.py`
   - ユースケーステスト: `tests/unit/application/use_cases/test_<use_case>.py`

7. **テストデータビルダーの定義**:

   - 一貫したテストデータのためのテストフィクスチャとビルダーを作成
   - `tests/fixtures/`または`tests/builders/`に配置

8. **テスト計画のドキュメント化**:

   - 日本語で`docs/test_plan/issue-$ARGUMENTS-test-plan.md`を作成:

   ```markdown
   # テスト計画: <機能名>

   Issue: #$ARGUMENTS

   ## テストカバレッジ

   ### ユニットテスト

   - [ ] <Entity>: <テスト内容>
   - [ ] <ValueObject>: <テスト内容>
   - [ ] <UseCase>: <テスト内容>

   ### 統合テスト

   - [ ] <Repository>: <テスト内容>

   ### E2E テスト

   - [ ] <API Endpoint>: <テスト内容>

   ## テスト実行方法
   ```

   # すべてのテストを実行

   pytest

   # 特定のテストファイルを実行

   pytest tests/unit/domain/entities/test\_<entity>.py

   # カバレッジ付きで実行

   pytest --cov=domain --cov=application

   ```

   ```

9. **テストセットアップの検証**:

   - テストを実行して失敗することを確認（RED フェーズ）
   - すべてのシナリオがカバーされていることを確認
   - テスト名が説明的であることを確認

10. **イシューの更新**:

- コメント: `gh issue comment $ARGUMENTS --body "TDDテストを作成しました（RED phase）。実装前のため、すべてのテストは失敗します。"`

11. **次のステップの案内**:
    - 日本語でドメイン層の実装（`/implement-domain`）を促す
    - RED-GREEN-REFACTOR サイクルを思い出させる

重要な注意事項:

- テストは初期状態で失敗しなければならない（TDD RED フェーズ）
- 各テストは 1 つのことだけをテストする
- snake_case で説明的なテスト名を使用
- テスト内に Given-When-Then コメントを含める
- 外部依存関係を適切にモック化
- すべてのユーザー向け出力は日本語で行う必要があります
