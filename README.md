# Dev Container 環境で Claude Code を実行する開発環境のひな型

このプロジェクトは、Claude Code を使用した Python 開発を効率的に行うための Dev Container 環境のひな型です。Visual Studio Code のリモート開発機能と組み合わせて使用することで、一貫性のある開発環境を提供します。

## 主な特徴

- **Claude Code 統合**: Anthropic Claude Code がプリインストール済み
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

## プロジェクト構造

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

プルリクエストを作成する際は：

1. `i-morikawa-tanakakougei`をレビュアーに指定
2. 高レベルの問題説明と解決方法を記載
3. 関連する GitHub イシューがある場合は`Github-Issue:#<number>`トレーラーを追加
