# Claude Code を使用して TDD・DDD・レイヤードアーキテクチャによる Python 開発 in Dev Container 環境のひな型

このプロジェクトは、**TDD（テスト駆動開発）**、**DDD（ドメイン駆動設計）**、**レイヤードアーキテクチャ** を採用した Python 開発のための Dev Container 環境です。Claude Code と統合されたカスタムコマンドにより、体系的な開発ワークフローを提供します。

## 主な特徴

- **TDD/DDD/レイヤードアーキテクチャ対応**: 体系的な開発ワークフローをサポート
- **Claude Code 統合**: カスタムコマンドによる開発プロセスの自動化
- **Given-When-Then 仕様書**: 日本語による明確な仕様記述
- **Python 開発に最適化**: uv パッケージマネージャーと Pyright 型チェッカーを搭載
- **開発ツール充実**: Docker、GitHub CLI、zsh、fzf、delta などの便利なツールを同梱
- **自動品質管理**: pre-commit フックによるコード品質の自動チェック
- **MCP 対応**: context7 によるドキュメント検索機能

## システム要件

- Docker Desktop
- Visual Studio Code
- VS Code Remote - Containers 拡張機能

## クイックスタート

1. このリポジトリをクローン
2. VS Code でフォルダを開く
3. 「Reopen in Container」を選択（VS Code が提案するはず）
4. コンテナのビルドが完了するまで待つ

## 含まれるツール

### 開発ツール

- **Claude Code** (`@anthropic-ai/claude-code`): AI ペアプログラミングツール
- **Docker**: コンテナ内から Docker を使用可能（Docker in Docker）
- **GitHub CLI** (`gh`): GitHub との連携
- **Git Delta**: 美しい Git diff 表示
- **fzf**: インタラクティブなファジー検索
- **zsh**: 高機能シェル

### Python 開発

- **uv**: 高速な Python パッケージマネージャー
- **Pyright**: 型チェッカー
- **Ruff**: 高速な Python リンター/フォーマッター
- **pytest**: テストフレームワーク

### VSCode 拡張機能（自動インストール）

- ESLint
- Prettier
- GitLens
- Anthropic Claude Code

## プロジェクト構造（Claude Code in Dev Container 環境）

```
.
├── .devcontainer/        # Dev Container設定
│   ├── devcontainer.json # コンテナ設定
│   └── Dockerfile        # マルチステージDocker設定
├── .mcp.json            # MCP設定（context7）
├── .pre-commit-config.yaml # コード品質自動チェック
├── CLAUDE.md            # 開発ガイドライン
├── docs/                # 追加ドキュメント
├── scripts/             # ユーティリティスクリプト
└── reviews/             # コードレビュー用ディレクトリ
```

## 開発ガイドライン

### TDD・DDD・レイヤードアーキテクチャによる開発

このプロジェクトは **TDD（テスト駆動開発）**、**DDD（ドメイン駆動設計）**、**レイヤードアーキテクチャ** を採用した開発アプローチを推奨しています。

#### 開発ワークフロー

1. **ユースケース仕様作成**: `/create-use-case <issue番号>`

   - Given-When-Then 形式で仕様を日本語で記述
   - ドメイン概念とユビキタス言語を定義

2. **ドメインモデル設計**: `/domain-modeling <issue番号>`

   - エンティティ、値オブジェクト、ドメインサービスを設計
   - 集約境界とリポジトリインターフェースを定義

3. **TDD テスト作成**: `/create-tests <issue番号>`

   - RED phase: 仕様に基づいて失敗するテストを作成
   - 全ての Given-When-Then シナリオをカバー

4. **実装フェーズ**:

   - **ドメイン層**: `/implement-domain <issue番号>` (GREEN phase)
   - **アプリケーション層**: `/implement-usecase <issue番号>`
   - **インフラ層**: `/implement-infra <issue番号>`
   - **プレゼンテーション層**: `/implement-presentation <issue番号>`

5. **リファクタリング**: `/refactor <issue番号>` (REFACTOR phase)

6. **テスト検証**: `/run-all-tests <issue番号>`

#### プロジェクト構造(TDD・DDD・レイヤードアーキテクチャ)

```
project/
├── domain/               # ドメイン層（ビジネスロジック）
│   ├── entities/        # エンティティ
│   ├── value_objects/   # 値オブジェクト
│   ├── services/        # ドメインサービス
│   ├── repositories/    # リポジトリインターフェース
│   └── events/          # ドメインイベント
├── application/         # アプリケーション層（ユースケース）
│   ├── use_cases/       # ユースケース
│   ├── dtos/           # データ転送オブジェクト
│   └── exceptions/      # アプリケーション例外
├── infrastructure/      # インフラ層（永続化・外部サービス）
│   ├── repositories/    # リポジトリ実装
│   ├── persistence/     # データベースモデル
│   ├── external/        # 外部サービス
│   └── config/          # 設定
├── presentation/        # プレゼンテーション層（API・UI）
│   ├── api/            # REST API
│   ├── cli/            # コマンドライン
│   └── web/            # Web UI
├── tests/              # テスト
│   ├── unit/           # 単体テスト
│   ├── integration/    # 統合テスト
│   └── e2e/            # E2Eテスト
└── docs/               # ドキュメント
    ├── use_cases/      # ユースケース仕様
    ├── domain/         # ドメインモデル設計
    ├── test_plan/      # テスト計画
    └── test_report/    # テストレポート
```

### パッケージ管理

```bash
# パッケージのインストール
uv add package-name

# 開発依存関係の追加
uv add --dev package-name

# ツールの実行
uv run tool-name
```

### コード品質

- **フォーマット**: `uv run --frozen ruff format .`
- **リント**: `uv run --frozen ruff check .`
- **型チェック**: `uv run --frozen pyright`
- **テスト**: `uv run --frozen pytest`

### Git 操作

コミット時に pre-commit フックが自動実行され、以下がチェックされます：

- Python コードのフォーマットとリント（Ruff）
- Python 型チェック（Pyright）
- YAML と JSON のフォーマット（Prettier）
- Markdown のリント

## 環境設定

### タイムゾーン

デフォルトで`Asia/Tokyo`に設定されています。変更する場合は`.devcontainer/devcontainer.json`の`TZ`環境変数を編集してください。

### 永続化される設定

- bash ヒストリー
- Claude 設定
- GitHub CLI 設定

## 本番用イメージのビルド

開発環境とは別に、軽量な本番用イメージが必要な場合：

```bash
docker build -t myapp:prod --target prod .
```

## GitHub 認証

GitHub CLI を使用する前に認証が必要です：

```bash
gh auth login
```

## MCP (Model Context Protocol)

このプロジェクトは context7 を使用してドキュメント検索機能を提供しています。設定は`.mcp.json`で管理されています。

## トラブルシューティング

### pytest が anyio マークを認識しない場合

```bash
PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest
```

### 型エラーの解決

1. フォーマットを先に実行: `uv run --frozen ruff format .`
2. 型エラーを確認: `uv run --frozen pyright`
3. Optional 型には明示的な None チェックを追加

## ライセンス

このひな型プロジェクトは MIT ライセンスで提供されています。

## 貢献

### 新機能開発

TDD・DDD・レイヤードアーキテクチャのワークフローに従って開発を行ってください：

1. **Issue 作成**: 機能の要求と受入基準を明確に記載
2. **開発ワークフロー実行**:
   ```bash
   /create-use-case <issue番号>    # Given-When-Then仕様作成
   /domain-modeling <issue番号>    # ドメインモデル設計
   /create-tests <issue番号>       # TDDテスト作成
   /implement-domain <issue番号>   # ドメイン層実装
   /implement-usecase <issue番号>  # アプリケーション層実装
   /implement-infra <issue番号>    # インフラ層実装
   /implement-presentation <issue番号> # プレゼンテーション層実装
   /refactor <issue番号>          # リファクタリング
   /run-all-tests <issue番号>     # テスト検証
   ```

### プルリクエストの作成

プルリクエストを作成する際は：

1. **レビュアー**: `i-morikawa-tanakakougei`を指定
2. **説明**: 高レベルの問題説明と解決方法を記載
3. **テスト**: 全てのテストが通ることを確認
4. **ドキュメント**: 仕様書と設計書が適切に作成されていることを確認
5. **トレーラー**: 関連する GitHub イシューがある場合は`Github-Issue:#<number>`を追加
