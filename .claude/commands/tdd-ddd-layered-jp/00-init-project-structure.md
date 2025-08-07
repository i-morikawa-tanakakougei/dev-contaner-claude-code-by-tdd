TDD/DDD/レイヤードアーキテクチャ開発のためのプロジェクト構造を初期化します。

以下の手順に従ってください：

1. **ディレクトリ構造の作成**:
   以下のプロジェクト構造を作成します：
   ```
   project_root/
   ├── domain/
   │   ├── entities/
   │   ├── value_objects/
   │   ├── services/
   │   ├── repositories/
   │   └── events/
   ├── application/
   │   ├── use_cases/
   │   ├── dtos/
   │   └── exceptions/
   ├── infrastructure/
   │   ├── repositories/
   │   ├── persistence/
   │   │   ├── models/
   │   │   └── mappers/
   │   ├── external/
   │   └── config/
   ├── presentation/
   │   ├── api/
   │   │   ├── controllers/
   │   │   ├── validators/
   │   │   └── serializers/
   │   ├── cli/
   │   └── web/
   ├── tests/
   │   ├── unit/
   │   │   ├── domain/
   │   │   │   ├── entities/
   │   │   │   └── value_objects/
   │   │   └── application/
   │   │       └── use_cases/
   │   ├── integration/
   │   │   └── repositories/
   │   └── e2e/
   │       └── api/
   └── docs/
       ├── use_cases/
       ├── domain/
       ├── application/
       └── test_plan/
   ```

2. **__init__.pyファイルの作成**:
   - すべてのPythonパッケージディレクトリに`__init__.py`を追加
   - 適切なモジュールインポートを保証します

3. **READMEファイルの作成**:
   - 各層にその目的を説明するREADME.mdを追加
   - ドキュメントには日本語を使用：
   
   domain/README.mdの例：
   ```markdown
   # ドメイン層
   
   ビジネスロジックとビジネスルールを含む層です。
   
   ## ディレクトリ構成
   - entities/: エンティティ（識別子を持つオブジェクト）
   - value_objects/: 値オブジェクト（不変オブジェクト）
   - services/: ドメインサービス
   - repositories/: リポジトリインターフェース
   - events/: ドメインイベント
   ```

4. **開発環境の設定**:
   - `uv add`を使用して依存関係を直接インストール（バージョン解決の問題により手動でpyproject.tomlを編集することは避ける）
   - 必要な依存関係をインストール：
   ```bash
   uv add --dev pytest
   uv add --dev pytest-cov
   uv add --dev ruff
   uv add --dev pyright
   # 必要に応じてフレームワーク固有の依存関係を追加
   # 例: uv add fastapi
   # 例: uv add sqlalchemy
   ```

5. **設定ファイルの作成**:
   - Pythonプロジェクト用の`.gitignore`
   - テスト設定用の`pytest.ini`
   - リンティングルール用の`ruff.toml`
   - プリコミットを使用する場合は`.pre-commit-config.yaml`

6. **Gitリポジトリの初期化**（存在しない場合）:
   ```bash
   git init
   git add .
   git commit -m "Initialize TDD/DDD/Layered Architecture structure"
   ```

7. **初期ドキュメントの作成**:
   - アーキテクチャを説明する`docs/architecture.md`を日本語で作成
   - 役に立つ場合は図も含める

8. **次のステップの提供**:
   - 日本語でメッセージを表示：
   ```
   プロジェクト構造の初期化が完了しました。
   
   次のステップ:
   1. GitHub issueを作成または選択
   2. /create-use-case <issue番号> でユースケース仕様を作成
   3. TDD/DDD/レイヤードアーキテクチャの開発フローに従って実装
   ```

重要な注意事項:
- このコマンドはプロジェクト構造全体を一度に設定します
- 新しいプロジェクトや大規模なリファクタリングに有用です
- 既存のプロジェクトでも安全に実行できます（ファイルを上書きしません）
- すべてのユーザー向け出力は日本語で行う必要があります