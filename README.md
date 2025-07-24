# Dev Container 環境で Claude Code を実行する開発環境のひな型

このプロジェクトは、Claude Codeを使用したPython開発を効率的に行うためのDev Container環境のひな型です。Visual Studio Codeのリモート開発機能と組み合わせて使用することで、一貫性のある開発環境を提供します。

## 主な特徴

- **Claude Code統合**: Anthropic Claude Codeがプリインストール済み
- **Python開発に最適化**: uvパッケージマネージャーとPyright型チェッカーを搭載
- **開発ツール充実**: Docker、GitHub CLI、zsh、fzf、deltaなどの便利なツールを同梱
- **自動品質管理**: pre-commitフックによるコード品質の自動チェック
- **MCP対応**: context7によるドキュメント検索機能

## システム要件

- Docker Desktop
- Visual Studio Code
- VS Code Remote - Containers拡張機能

## クイックスタート

1. このリポジトリをクローン
2. VS Codeでフォルダを開く
3. 「Reopen in Container」を選択（VS Codeが提案するはず）
4. コンテナのビルドが完了するまで待つ

## 含まれるツール

### 開発ツール
- **Claude Code** (`@anthropic-ai/claude-code`): AIペアプログラミングツール
- **Docker**: コンテナ内からDockerを使用可能（Docker in Docker）
- **GitHub CLI** (`gh`): GitHubとの連携
- **Git Delta**: 美しいGit diff表示
- **fzf**: インタラクティブなファジー検索
- **zsh**: 高機能シェル

### Python開発
- **uv**: 高速なPythonパッケージマネージャー
- **Pyright**: 型チェッカー
- **Ruff**: 高速なPythonリンター/フォーマッター
- **pytest**: テストフレームワーク

### VSCode拡張機能（自動インストール）
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

### Git操作
コミット時にpre-commitフックが自動実行され、以下がチェックされます：
- Pythonコードのフォーマットとリント（Ruff）
- Python型チェック（Pyright）
- YAMLとJSONのフォーマット（Prettier）
- Markdownのリント

## 環境設定

### タイムゾーン
デフォルトで`Asia/Tokyo`に設定されています。変更する場合は`.devcontainer/devcontainer.json`の`TZ`環境変数を編集してください。

### 永続化される設定
- bashヒストリー
- Claude設定
- GitHub CLI設定

## 本番用イメージのビルド

開発環境とは別に、軽量な本番用イメージが必要な場合：

```bash
docker build -t myapp:prod --target prod .
```

## GitHub認証

GitHub CLIを使用する前に認証が必要です：

```bash
gh auth login
```

## MCP (Model Context Protocol)

このプロジェクトはcontext7を使用してドキュメント検索機能を提供しています。設定は`.mcp.json`で管理されています。

## トラブルシューティング

### pytestがanyioマークを認識しない場合
```bash
PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest
```

### 型エラーの解決
1. フォーマットを先に実行: `uv run --frozen ruff format .`
2. 型エラーを確認: `uv run --frozen pyright`
3. Optional型には明示的なNoneチェックを追加

## ライセンス

このひな型プロジェクトはMITライセンスで提供されています。

## 貢献

プルリクエストを作成する際は：
1. `artofzero`をレビュアーに指定
2. 高レベルの問題説明と解決方法を記載
3. 関連するGitHubイシューがある場合は`Github-Issue:#<number>`トレーラーを追加
