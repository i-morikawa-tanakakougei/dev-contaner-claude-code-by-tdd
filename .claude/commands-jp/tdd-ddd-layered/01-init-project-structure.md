TDD/DDD/レイヤードアーキテクチャ開発用のプロジェクト構造を初期化します。

## メタデータ
- **前提条件**: ビジョンドキュメントが存在する必要があります（最初に`/create-vision`を実行）
- **入力**: なし（自動構造生成）
- **出力**: 
  - すべての層の完全なディレクトリ構造
  - Pythonパッケージファイル（`__init__.py`）
  - 設定ファイル（`pyproject.toml`、`.gitignore`など）
  - 初期README.md
- **依存関係**: 開発コマンド実行前に必要
- **実行タイミング**: ビジョン作成後に一度

## 🎯 **TDD/DDD/レイヤードプロセスコンテキスト**

**🔄 コアワークフロー**: Vision(00) → Vision Review(00.5) → Structure(01) → Sprint(02) → Sprint Review(02.5) → Use-Case(03) → Domain(04) → Design Review(04.5) → Tests(05) → Test Review(05.5) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Test Results Review(10.5) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 アーキテクチャ**: クリーンアーキテクチャ（Domain→Application→Infrastructure→Presentation）  
**🧪 開発**: テスト駆動開発（RED→GREEN→REFACTOR）  
**🏗️ 設計**: ドメイン駆動設計（Entity、Value Object、Aggregate、Repository）  
**📋 要件**: Given-When-Thenシナリオによる完全なトレーサビリティ  
**🔄 進化**: /evolve-scenariosコマンドによる継続的シナリオ進化

> 📖 **ドキュメント管理システム**: [README.md](./README.md)  
> 🗺️ **現在位置**: 初期フェーズ - プロジェクト構造初期化（01/16）  
> 🎯 **フェーズ目的**: 基盤ディレクトリ構造とビルドシステムのセットアップ  
> ⬅️ **前のステージ**: 00.5-review-vision（ビジョンレビュー）  
> ➡️ **次のステージ**: 02-sprint-planning（スプリント計画）
>
> **📋 3層アーキテクチャ操作**:  
> - 🎯 **戦略**: `docs/use_cases/core/index.md`（参照）  
> - 📊 **戦術**: `docs/use_cases/index.md`（参照）  
> - 🔧 **実行**: ディレクトリ構造セットアップ（インフラ基盤）

## 🏗️ **フェーズ目的: プロジェクト構造セットアップのみ**

**⚠️ 重要な注意:**
- **このステップはインフラセットアップのみ** - ディレクトリ構造とビルドシステムを作成
- **機能実装は行わない** - 基盤構造とツーリングに焦点を当てる  
- **基盤フェーズ** - ディレクトリ、依存関係、開発ツールをセットアップ
- **プロジェクトスケルトンのみ作成** - ビジネスロジックや機能コードは作成しない

**このステップの内容:**
1. `00-create-vision` ← ビジョンドキュメントとコアシナリオ
2. `01-init-project-structure` ← **【ここにいます】プロジェクト構造とツーリングセットアップ**
3. `02-sprint-planning` ← シナリオからのスプリント計画
4. その後、TDD/DDD実装サイクル開始

**プロジェクトインフラのみ作成してください。**

## よくあるエラーと解決策

### ❌ エラーケース1: プロジェクトが既に初期化済み
**原因**: `src/`、`docs/`、または`tests/`ディレクトリが既に存在  
**解決策**: 
- 既存構造をバックアップ（自動でプロンプト表示）
- 上書きを選択（プロンプトで`y`を入力）
- またはクリーンなディレクトリで実行

### ❌ エラーケース2: ディスク容量不足
**原因**: 100MB未満の利用可能容量  
**解決策**: 実行前にディスク容量を確保

### ❌ エラーケース3: Pythonパッケージインポートエラー
**原因**: 不正なPython環境または依存関係の不足  
**解決策**: 
```bash
# Python 3.9+がインストールされていることを確認
python --version
# uvが利用できない場合はインストール
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## 実行例

### ✅ 成功例
```bash
$ /init-project-structure
🏗️ TDD/DDD/レイヤードアーキテクチャ ディレクトリ構造作成中...
  📁 作成中: src/domain/entities
  📁 作成中: src/application/use_cases
  📁 作成中: src/infrastructure/repositories
  📁 作成中: src/presentation/api/controllers
✅ ディレクトリ構造作成完了 (45 ディレクトリ)

🐍 Pythonパッケージ構造作成中...
✅ Pythonパッケージファイル作成完了 (25 ファイル)

🎉 プロジェクト構造初期化完了!
```

### ❌ 失敗例と修正
```bash
$ /init-project-structure
⚠️  プロジェクト構造が既に存在します
既存の構造を上書きしますか？ (y/N): n
プロジェクト初期化をキャンセルしました

# 修正: 上書きするには'y'を選択、または新しいディレクトリで実行
```

## 📋 **プロジェクト構造初期化タスクチェックリスト**

**包括的なプロジェクトインフラセットアップのためのチェックリストを使用してください:**

### 🔴 必須タスク

#### **🔧 環境と前提条件**
- [ ] **プロジェクトディレクトリ検証**: 既存のプロジェクト設定ファイルをチェック
- [ ] **ディスク容量チェック**: プロジェクト構造用に最低100MB利用可能であることを確認
- [ ] **権限検証**: ディレクトリ作成の書き込み権限を確保

#### **📁 ディレクトリ構造作成**
- [ ] **ドメイン層ディレクトリ作成**: entities、value_objects、services、repositories、events
- [ ] **アプリケーション層ディレクトリ作成**: use_cases、dtos、exceptions
- [ ] **インフラ層ディレクトリ作成**: repositories、persistence、external、config
- [ ] **プレゼンテーション層ディレクトリ作成**: api（controllers/validators/serializers）、cli、web
- [ ] **テスト構造ディレクトリ作成**: unit、integration、e2eと層別サブディビジョン

#### **🐍 Pythonパッケージセットアップ**
- [ ] **__init__.pyファイル作成**: すべてのパッケージとサブパッケージに適切な内容で
- [ ] **パッケージ構造検証**: Pythonがsrcパッケージをインポートできることを確認

### 🟡 推奨タスク

#### **⚙️ 設定ファイル**
- [ ] **pyproject.toml作成**: プロジェクトメタデータ、依存関係、ツール設定
- [ ] **pytest設定セットアップ**: テスト発見、カバレッジ、マーカー
- [ ] **ruff設定**: リントとフォーマットルール
- [ ] **pyright設定**: 型チェック設定
- [ ] **.gitignore作成**: Python、テスト、IDE、OS除外

#### **📦 依存関係管理**
- [ ] **コア依存関係インストール**: pydantic、fastapi、uvicornをuvで
- [ ] **開発依存関係インストール**: pytest、pytest-asyncio、pytest-cov、ruff、pyright、anyio
- [ ] **インストール検証**: すべてのパッケージが正しくインストールされたことをテスト

#### **📜 Gitリポジトリ初期化**
- [ ] **gitリポジトリ初期化**: 存在しない場合はバージョン管理をセットアップ
- [ ] **初期コミット作成**: プロジェクト構造全体をコミット

### 🟢 オプションタスク

#### **📚 ドキュメント強化**
- [ ] **README.md作成**: プロジェクト概要、セットアップ手順、開発ワークフロー
- [ ] **ユースケースインデックス作成**: 実装状況と次のステップを追跡
- [ ] **アーキテクチャ文書化**: READMEでの基本構造説明
- [ ] **開発ガイド作成**: TDD/DDDワークフロー手順

#### **🔍 高度な検証**
- [ ] **既存構造バックアップ**: 既存のsrc/docs/testsディレクトリを安全にバックアップ
- [ ] **パッケージ階層セットアップ**: 適切な名前空間組織
- [ ] **パッケージインポートテスト**: Pythonパッケージ構造が正しく動作することを検証
- [ ] **uv環境検証**: パッケージマネージャーが動作していることを確認
- [ ] **git設定セットアップ**: 適切な作成者情報
- [ ] **すべてのディレクトリ検証**: 必要なディレクトリがすべて存在することを確認
- [ ] **Pythonセットアップテスト**: 基本的なPythonインポートとpytest発見を実行
- [ ] **設定検証**: すべての設定ファイルが有効であることをチェック
- [ ] **gitリポジトリ検証**: 適切なgit初期化とコミットを確認

**💡 プロTip**: このチェックリストを実際のプロジェクトで使用するためにコピーしてください！

## タスク詳細

1. **安全環境セットアップと検証**:
   ```bash
   # 🔧 すべての安全操作関数をロード
   source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "01-init-project-structure" "$ARGUMENTS"
   
   # 有効なプロジェクトディレクトリにいるかチェック
   if [[ ! -f "pyproject.toml" ]] && [[ ! -f "package.json" ]] && [[ ! -f "Cargo.toml" ]]; then
       echo "⚠️  プロジェクト設定ファイルが見つかりません"
       echo "新しいプロジェクトを初期化しますか？ (y/N): "
       read -n 1 -r
       echo
       if [[ ! $REPLY =~ ^[Yy]$ ]]; then
           echo "プロジェクト初期化をキャンセルしました"
           exit 0
       fi
   fi
   ```

2. **トランザクション開始と事前検証**:
   ```bash
   # 🔄 包括的トランザクション開始
   if ! begin_transaction "init_project_structure"; then
       echo "エラー: トランザクションの開始に失敗しました"
       exit 1
   fi
   
   # 📋 ディスク容量チェック（最低100MB必要）
   if ! check_disk_space "." 100; then
       echo "エラー: プロジェクト初期化に十分なディスク容量がありません"
       execute_rollback "insufficient_disk_space"
       exit 1
   fi
   
   # 🔍 プロジェクトが既に初期化されているかチェック
   if [[ -d "src" ]] || [[ -d "docs" ]] || [[ -d "tests" ]]; then
       echo "⚠️  プロジェクト構造が既に存在します"
       echo "既存の構造を上書きしますか？ (y/N): "
       read -n 1 -r
       echo
       if [[ ! $REPLY =~ ^[Yy]$ ]]; then
           echo "プロジェクト初期化をキャンセルしました"
           commit_transaction
           exit 0
       fi
       
       # 既存構造をバックアップ
       backup_dir="backup_$(date +%Y%m%d_%H%M%S)"
       echo "既存構造をバックアップ中: $backup_dir"
       if ! safe_mkdir "$backup_dir"; then
           echo "エラー: バックアップディレクトリの作成に失敗しました"
           execute_rollback "backup_creation_failed"
           exit 1
       fi
       
       for dir in src docs tests; do
           if [[ -d "$dir" ]]; then
               if ! safe_move_file "$dir" "$backup_dir/$dir" false; then
                   echo "エラー: $dir のバックアップに失敗しました"
                   execute_rollback "backup_failed"
                   exit 1
               fi
               add_rollback "mv '$backup_dir/$dir' '$dir'" "Restore $dir from backup"
           fi
       done
   fi
   ```

3. **TDD/DDD/レイヤードアーキテクチャディレクトリ構造作成**:
   ```bash
   # 🏗️ 包括的ディレクトリ構造作成
   echo "🏗️ TDD/DDD/レイヤードアーキテクチャ ディレクトリ構造作成中..."
   
   # 完全なディレクトリ構造を定義
   directories=(
       # ソースコード構造（クリーンアーキテクチャ層）
       "src/domain/entities"
       "src/domain/value_objects"
       "src/domain/services"
       "src/domain/repositories"
       "src/domain/events"
       "src/application/use_cases"
       "src/application/dtos"
       "src/application/exceptions"
       "src/infrastructure/repositories"
       "src/infrastructure/persistence/models"
       "src/infrastructure/persistence/mappers"
       "src/infrastructure/external"
       "src/infrastructure/config"
       "src/presentation/api/controllers"
       "src/presentation/api/validators"
       "src/presentation/api/serializers"
       "src/presentation/cli"
       "src/presentation/web"
       
       # テスト構造（TDDアプローチ）
       "tests/unit/domain/entities"
       "tests/unit/domain/value_objects"
       "tests/unit/domain/services"
       "tests/unit/application/use_cases"
       "tests/integration/repositories"
       "tests/integration/use_cases"
       "tests/e2e/api"
       "tests/e2e/cli"
       "tests/fixtures"
       "tests/mocks"
       
       # ドキュメント構造（DDDアプローチ）
       "docs/vision"
       "docs/use_cases/core"
       "docs/use_cases/evolved"
       "docs/domain"
       "docs/application"
       "docs/infrastructure"
       "docs/presentation"
       "docs/test_plan"
       "docs/test_report"
       "docs/review"
       "docs/implementation-summary"
       "docs/sprints"
       "docs/steering"
   )
   
   # すべてのディレクトリを安全に作成
   for dir in "${directories[@]}"; do
       echo "  📁 作成中: $dir"
       if ! safe_mkdir "$dir"; then
           echo "エラー: ディレクトリ作成に失敗しました: $dir"
           execute_rollback "directory_creation_failed"
           exit 1
       fi
       add_rollback "rmdir '$dir' 2>/dev/null || true" "Remove created directory: $dir"
   done
   
   echo "✅ ディレクトリ構造作成完了 (${#directories[@]} ディレクトリ)"
   ```

4. **安全操作による重要なPythonファイル作成**:
   ```bash
   # 🐍 Pythonパッケージ構造作成
   echo "🐍 Pythonパッケージ構造作成中..."
   
   # 作成する__init__.pyファイルを定義
   init_files=(
       "src/__init__.py"
       "src/domain/__init__.py"
       "src/domain/entities/__init__.py"
       "src/domain/value_objects/__init__.py"
       "src/domain/services/__init__.py"
       "src/domain/repositories/__init__.py"
       "src/domain/events/__init__.py"
       "src/application/__init__.py"
       "src/application/use_cases/__init__.py"
       "src/application/dtos/__init__.py"
       "src/application/exceptions/__init__.py"
       "src/infrastructure/__init__.py"
       "src/infrastructure/repositories/__init__.py"
       "src/infrastructure/persistence/__init__.py"
       "src/infrastructure/persistence/models/__init__.py"
       "src/infrastructure/persistence/mappers/__init__.py"
       "src/infrastructure/external/__init__.py"
       "src/infrastructure/config/__init__.py"
       "src/presentation/__init__.py"
       "src/presentation/api/__init__.py"
       "src/presentation/api/controllers/__init__.py"
       "src/presentation/api/validators/__init__.py"
       "src/presentation/api/serializers/__init__.py"
       "src/presentation/cli/__init__.py"
       "src/presentation/web/__init__.py"
       "tests/__init__.py"
   )
   
   # 適切な内容ですべての__init__.pyファイルを作成
   for init_file in "${init_files[@]}"; do
       echo "  📄 作成中: $init_file"
       
       # パッケージに基づいて適切な内容を生成
       package_name=$(dirname "$init_file" | tr '/' '.')
       init_content="\"\"\"
   $package_name パッケージ
   
   TDD/DDD/レイヤードアーキテクチャ プロジェクト
   作成日時: $(date)
   \"\"\""
       
       if ! safe_create_file "$init_file" "$init_content" false; then
           echo "エラー: __init__.py ファイルの作成に失敗しました: $init_file"
           execute_rollback "init_file_creation_failed"
           exit 1
       fi
       
       add_rollback "rm -f '$init_file'" "Remove created __init__.py: $init_file"
   done
   
   echo "✅ Pythonパッケージファイル作成完了 (${#init_files[@]} ファイル)"
   ```

5. **重要な設定ファイル作成**:
   ```bash
   # ⚙️ 重要な設定ファイル作成
   echo "⚙️ 設定ファイル作成中..."
   
   # pyproject.tomlが存在しない場合は作成
   if [[ ! -f "pyproject.toml" ]]; then
       echo "  📄 作成中: pyproject.toml"
       
       pyproject_content='[build-system]
   requires = ["hatchling"]
   build-backend = "hatchling.build"
   
   [project]
   name = "tdd-ddd-project"
   dynamic = ["version"]
   description = "TDD/DDD/Layered Architecture Project"
   readme = "README.md"
   license = "MIT"
   requires-python = ">=3.9"
   authors = [
       { name = "Development Team", email = "dev@example.com" },
   ]
   classifiers = [
       "Development Status :: 4 - Beta",
       "Intended Audience :: Developers",
       "License :: OSI Approved :: MIT License",
       "Operating System :: OS Independent",
       "Programming Language :: Python :: 3",
       "Programming Language :: Python :: 3.9",
       "Programming Language :: Python :: 3.10",
       "Programming Language :: Python :: 3.11",
       "Programming Language :: Python :: 3.12",
   ]
   dependencies = [
       "pydantic>=2.0.0",
       "fastapi>=0.100.0",
       "uvicorn[standard]>=0.20.0",
   ]
   
   [project.optional-dependencies]
   dev = [
       "pytest>=7.0.0",
       "pytest-asyncio>=0.21.0",
       "pytest-cov>=4.0.0",
       "ruff>=0.1.0",
       "pyright>=1.1.0",
       "anyio>=4.0.0",
   ]
   test = [
       "pytest>=7.0.0",
       "pytest-asyncio>=0.21.0", 
       "pytest-cov>=4.0.0",
       "anyio>=4.0.0",
   ]
   
   [project.urls]
   Homepage = "https://github.com/example/tdd-ddd-project"
   Documentation = "https://github.com/example/tdd-ddd-project#readme"
   Repository = "https://github.com/example/tdd-ddd-project.git"
   Issues = "https://github.com/example/tdd-ddd-project/issues"
   
   [tool.hatch.version]
   path = "src/__init__.py"
   
   [tool.hatch.build.targets.wheel]
   packages = ["src"]
   
   [tool.pytest.ini_options]
   testpaths = ["tests"]
   python_files = ["test_*.py", "*_test.py"]
   python_classes = ["Test*"]
   python_functions = ["test_*"]
   addopts = [
       "--strict-markers",
       "--strict-config",
       "--cov=src",
       "--cov-report=term-missing",
       "--cov-report=html",
       "--cov-report=xml",
   ]
   markers = [
       "unit: Unit tests",
       "integration: Integration tests",
       "e2e: End-to-end tests",
       "slow: Slow tests",
   ]
   
   [tool.ruff]
   target-version = "py39"
   line-length = 120
   select = [
       "E",   # pycodestyle errors
       "W",   # pycodestyle warnings
       "F",   # pyflakes
       "I",   # isort
       "B",   # flake8-bugbear
       "C4",  # flake8-comprehensions
       "UP",  # pyupgrade
   ]
   ignore = [
       "E501",  # line too long, handled by formatter
   ]
   
   [tool.ruff.per-file-ignores]
   "tests/**/*" = ["D"]
   
   [tool.pyright]
   include = ["src", "tests"]
   exclude = ["**/__pycache__"]
   reportMissingImports = true
   reportMissingTypeStubs = false
   pythonVersion = "3.9"
   pythonPlatform = "Linux"
   '
       
       if ! safe_create_file "pyproject.toml" "$pyproject_content" true; then
           echo "エラー: pyproject.toml の作成に失敗しました"
           execute_rollback "pyproject_creation_failed"
           exit 1
       fi
       
       add_rollback "rm -f 'pyproject.toml'" "Remove created pyproject.toml"
       echo "  ✅ pyproject.toml 作成完了"
   fi
   ```

6. **Python環境と依存関係の初期化**:
   ```bash
   # 🔧 Python環境を安全に初期化
   echo "🔧 Python環境初期化中..."
   
   # Python環境を検証
   if ! validate_python_environment; then
       echo "エラー: Python環境の検証に失敗しました"
       execute_rollback "python_env_validation_failed"
       exit 1
   fi
   
   # 開発依存関係を安全にインストール
   echo "📦 開発依存関係インストール中..."
   
   dev_packages=("pytest" "pytest-asyncio" "pytest-cov" "ruff" "pyright" "anyio")
   
   for package in "${dev_packages[@]}"; do
       echo "  📦 インストール中: $package"
       if ! uv add --dev "$package" --quiet; then
           echo "エラー: $package のインストールに失敗しました"
           execute_rollback "package_installation_failed"
           exit 1
       fi
   done
   
   # コア依存関係をインストール
   echo "📦 コア依存関係インストール中..."
   
   core_packages=("pydantic>=2.0.0" "fastapi>=0.100.0" "uvicorn[standard]>=0.20.0")
   
   for package in "${core_packages[@]}"; do
       echo "  📦 インストール中: $package"
       if ! uv add "$package" --quiet; then
           echo "エラー: $package のインストールに失敗しました"
           execute_rollback "core_package_installation_failed"
           exit 1
       fi
   done
   
   echo "✅ 依存関係インストール完了"
   ```

7. **Gitリポジトリ初期化と初期コミット**:
   ```bash
   # 📜 Gitリポジトリを安全に初期化
   echo "📜 Gitリポジトリ初期化中..."
   
   # 既にgitリポジトリかチェック
   if ! git rev-parse --git-dir >/dev/null 2>&1; then
       echo "  🌱 新しいGitリポジトリ初期化中..."
       
       if ! git init; then
           echo "エラー: Gitリポジトリの初期化に失敗しました"
           execute_rollback "git_init_failed"
           exit 1
       fi
       
       add_rollback "rm -rf .git" "Remove git repository"
   else
       echo "  ✅ 既存のGitリポジトリを使用"
   fi
   
   # .gitignoreが存在しない場合は作成
   if [[ ! -f ".gitignore" ]]; then
       echo "  📄 作成中: .gitignore"
       
       gitignore_content='# Python
   __pycache__/
   *.py[cod]
   *$py.class
   *.so
   .Python
   build/
   develop-eggs/
   dist/
   downloads/
   eggs/
   .eggs/
   lib/
   lib64/
   parts/
   sdist/
   var/
   wheels/
   *.egg-info/
   .installed.cfg
   *.egg
   MANIFEST
   
   # Testing
   .pytest_cache/
   .coverage
   htmlcov/
   .tox/
   .nox/
   coverage.xml
   *.cover
   .hypothesis/
   
   # Environment
   .env
   .venv
   env/
   venv/
   ENV/
   env.bak/
   venv.bak/
   
   # IDE
   .vscode/
   .idea/
   *.swp
   *.swo
   *~
   
   # OS
   .DS_Store
   Thumbs.db
   
   # Project specific
   /logs/
   /tmp/
   /.uv/
   
   # Documentation builds
   docs/_build/
   docs/site/
   '
       
       if ! safe_create_file ".gitignore" "$gitignore_content" true; then
           echo "エラー: .gitignore の作成に失敗しました"
           execute_rollback "gitignore_creation_failed"
           exit 1
       fi
       
       add_rollback "rm -f '.gitignore'" "Remove created .gitignore"
   fi
   
   # 作成されたすべての構造で初期コミット
   echo "  💾 初期コミット作成中..."
   
   commit_message="feat: initialize TDD/DDD/Layered Architecture project structure

   Create comprehensive project structure with:
   - Clean Architecture layers (Domain, Application, Infrastructure, Presentation)
   - TDD-ready test structure (unit, integration, e2e)
   - DDD documentation structure
   - Python package configuration
   - Development tooling setup
   
   Structure includes:
   - ${#directories[@]} directories created
   - ${#init_files[@]} Python package files
   - Core dependencies and dev tools
   - Git repository initialization
   
   Ready for TDD/DDD development workflow.
   "
   
   if ! safe_git_commit "$commit_message" "."; then
       echo "エラー: 初期コミットに失敗しました"
       execute_rollback "initial_commit_failed"
       exit 1
   fi
   
   add_rollback "git reset --hard HEAD~1" "Undo initial commit"
   echo "  ✅ 初期コミット完了"
   ```

8. **初期ドキュメント作成**:
   ```bash
   # 📚 初期ドキュメント作成
   echo "📚 初期ドキュメント作成中..."
   
   # README.mdが存在しない場合は作成
   if [[ ! -f "README.md" ]]; then
       echo "  📄 作成中: README.md"
       
       readme_content="# TDD/DDD/レイヤードアーキテクチャ プロジェクト

   ## 概要

   このプロジェクトは、Test-Driven Development (TDD)、Domain-Driven Design (DDD)、およびレイヤードアーキテクチャを採用した高品質なソフトウェア開発プロジェクトです。

   ## アーキテクチャ

   ### レイヤー構造

   \`\`\`
   src/
   ├── domain/          # ドメイン層 (ビジネスロジック)
   ├── application/     # アプリケーション層 (ユースケース)
   ├── infrastructure/  # インフラ層 (データアクセス・外部API)
   └── presentation/    # プレゼンテーション層 (API・UI)
   \`\`\`

   ### テスト構造

   \`\`\`
   tests/
   ├── unit/         # 単体テスト
   ├── integration/  # 統合テスト
   └── e2e/          # E2Eテスト
   \`\`\`

   ## セットアップ

   ### 要件

   - Python 3.9+
   - uv (パッケージマネージャー)

   ### インストール

   \`\`\`bash
   # 依存関係のインストール
   uv sync

   # 開発依存関係のインストール
   uv sync --extra dev
   \`\`\`

   ## 開発ワークフロー

   ### TDD サイクル

   1. **RED**: テストを先に書く (失敗)
   2. **GREEN**: 最小限の実装でテストを通す
   3. **REFACTOR**: コードを改善

   ### DDD アプローチ

   1. **ユビキタス言語**: ドメインエキスパートと開発者が共通の言葉を使用
   2. **ドメインモデル**: ビジネスロジックを中心とした設計
   3. **境界づけられたコンテキスト**: 明確な責任範囲の定義

   ## テスト実行

   \`\`\`bash
   # 全テスト実行
   uv run pytest

   # 単体テストのみ
   uv run pytest tests/unit/

   # カバレッジ付きテスト実行
   uv run pytest --cov=src --cov-report=html
   \`\`\`

   ## コード品質

   \`\`\`bash
   # フォーマット
   uv run ruff format .

   # リント
   uv run ruff check .

   # 型チェック
   uv run pyright
   \`\`\`

   ## ドキュメント

   - [ビジョン](docs/vision/): プロジェクトの方向性
   - [ユースケース](docs/use_cases/): 機能仕様
   - [ドメインモデル](docs/domain/): ビジネスロジック設計
   - [アプリケーション](docs/application/): ユースケース実装
   - [インフラ](docs/infrastructure/): 技術的実装詳細
   - [プレゼンテーション](docs/presentation/): API・UI設計

   ## 貢献

   1. フィーチャーブランチを作成
   2. TDDサイクルに従って開発
   3. テストとコード品質チェックを実行
   4. プルリクエストを作成

   ## ライセンス

   MIT License
   "
       
       if ! safe_create_file "README.md" "$readme_content" true; then
           echo "エラー: README.md の作成に失敗しました"
           execute_rollback "readme_creation_failed"
           exit 1
       fi
       
       add_rollback "rm -f 'README.md'" "Remove created README.md"
   fi
   
   # 初期ユースケースインデックス作成
   index_file="docs/use_cases/index.md"
   if [[ ! -f "$index_file" ]]; then
       echo "  📄 作成中: $index_file"
       
       index_content="# Use Case Implementation Status

   ## プロジェクト初期化完了 ✅

   **初期化日時**: $(date)
   **初期化コマンド**: /init-project-structure

   ## 実装ステータス

   ### Completed ✅
   - プロジェクト構造初期化

   ### In Progress 🚧
   (まだありません)

   ### Planned 📋
   (ビジョン作成後に追加されます)

   ### Evolved Scenarios 🌱
   (開発中に発見された新しい要件)

   ## 次のステップ

   1. プロジェクトビジョンの作成: \`/create-vision\`
   2. スプリント計画の策定: \`/sprint-planning 1\`
   3. 最初のユースケース作成: \`/create-use-case <issue-number>\`

   ## メトリクス

   - **作成されたディレクトリ**: ${#directories[@]}
   - **作成されたファイル**: ${#init_files[@]} + 設定ファイル
   - **インストールされたパッケージ**: ${#dev_packages[@]} 開発 + ${#core_packages[@]} コア
   "
       
       if ! safe_create_file "$index_file" "$index_content" false; then
           echo "エラー: インデックスファイルの作成に失敗しました"
           execute_rollback "index_creation_failed"
           exit 1
       fi
       
       add_rollback "rm -f '$index_file'" "Remove created index file"
   fi
   
   echo "✅ 初期ドキュメント作成完了"
   ```

9. **最終検証と成功**:
   ```bash
   # 🔍 最終包括検証
   echo "🔍 最終検証実行中..."
   
   # ディレクトリ構造を検証
   missing_dirs=()
   for dir in "${directories[@]}"; do
       if [[ ! -d "$dir" ]]; then
           missing_dirs+=("$dir")
       fi
   done
   
   if [[ ${#missing_dirs[@]} -gt 0 ]]; then
       echo "エラー: 以下のディレクトリが作成されていません:"
       printf '  - %s\n' "${missing_dirs[@]}"
       execute_rollback "directory_validation_failed"
       exit 1
   fi
   
   # Pythonパッケージを検証
   if ! uv run python -c "import src" 2>/dev/null; then
       echo "エラー: Pythonパッケージ構造が正しくありません"
       execute_rollback "package_validation_failed"
       exit 1
   fi
   
   # 重要ファイルを検証
   essential_files=("pyproject.toml" ".gitignore" "README.md" "$index_file")
   missing_files=()
   for file in "${essential_files[@]}"; do
       if [[ ! -f "$file" ]]; then
           missing_files+=("$file")
       fi
   done
   
   if [[ ${#missing_files[@]} -gt 0 ]]; then
       echo "エラー: 以下の必須ファイルが作成されていません:"
       printf '  - %s\n' "${missing_files[@]}"
       execute_rollback "file_validation_failed"
       exit 1
   fi
   
   # Gitリポジトリを検証
   if ! git status >/dev/null 2>&1; then
       echo "エラー: Gitリポジトリが正しく初期化されていません"
       execute_rollback "git_validation_failed"
       exit 1
   fi
   
   # セットアップ検証のためのクイックテスト実行
   echo "🧪 セットアップ検証テスト実行中..."
   if ! uv run python -c "
   import sys
   import pytest
   print(f'Python: {sys.version}')
   print('pytest version:', pytest.__version__)
   print('Setup validation: PASSED')
   " 2>/dev/null; then
       echo "警告: Pythonセットアップに問題がある可能性があります"
   fi
   
   # 🎉 トランザクションコミット（成功！）
   if commit_transaction; then
       echo ""
       echo "🎉 プロジェクト構造初期化完了!"
       echo "============================================="
       echo "📁 作成されたディレクトリ: ${#directories[@]}"
       echo "📄 作成されたファイル: $((${#init_files[@]} + ${#essential_files[@]}))"
       echo "📦 インストールされたパッケージ: $((${#dev_packages[@]} + ${#core_packages[@]}))"
       echo ""
       echo "🏗️ アーキテクチャ構造:"
       echo "   - Domain Layer: ビジネスロジック (src/domain/)"
       echo "   - Application Layer: ユースケース (src/application/)"
       echo "   - Infrastructure Layer: データアクセス (src/infrastructure/)"
       echo "   - Presentation Layer: API・UI (src/presentation/)"
       echo ""
       echo "🧪 テスト構造:"
       echo "   - Unit Tests: 単体テスト (tests/unit/)"
       echo "   - Integration Tests: 統合テスト (tests/integration/)"
       echo "   - E2E Tests: E2Eテスト (tests/e2e/)"
       echo ""
       echo "📚 ドキュメント構造:"
       echo "   - Vision: プロジェクト方向性 (docs/vision/)"
       echo "   - Use Cases: 機能仕様 (docs/use_cases/)"
       echo "   - Domain: ビジネスロジック設計 (docs/domain/)"
       echo ""
       echo "📋 次のステップ:"
       echo "   1. ビジョン作成: /create-vision"
       echo "   2. スプリント計画: /sprint-planning 1"
       echo "   3. 最初のユースケース: /create-use-case <issue-number>"
       echo ""
       echo "🛠️ 開発コマンド:"
       echo "   - テスト実行: uv run pytest"
       echo "   - コード品質: uv run ruff check ."
       echo "   - 型チェック: uv run pyright"
       echo ""
       
       # 操作ログサマリーを表示
       echo "📊 操作ログサマリー:"
       show_git_operation_log | tail -3
       show_file_operation_log | tail -3
       show_transaction_log | tail -3
       
       echo ""
       echo "✅ TDD/DDD/レイヤードアーキテクチャ プロジェクト準備完了!"
       
   else
       echo "❌ トランザクション コミット失敗"
       exit 1
   fi
   ```