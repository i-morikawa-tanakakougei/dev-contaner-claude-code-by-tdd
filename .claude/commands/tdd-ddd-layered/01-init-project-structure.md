Initialize project structure for TDD/DDD/Layered Architecture development.

## Metadata
- **Prerequisites**: Vision document should exist (run `/create-vision` first)
- **Input**: None (automatic structure generation)
- **Output**: 
  - Complete directory structure for all layers
  - Python package files (`__init__.py`)
  - Configuration files (`pyproject.toml`, `.gitignore`, etc.)
  - Initial README.md
- **Dependencies**: Required before any development commands
- **Execution Timing**: Once after vision creation

## 🎯 **TDD/DDD/LAYERED PROCESS CONTEXT**

**🔄 Core Workflow**: Vision(00) → Vision Review(00.5) → Structure(01) → Sprint(02) → Sprint Review(02.5) → Use-Case(03) → Domain(04) → Design Review(04.5) → Tests(05) → Test Review(05.5) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Test Results Review(10.5) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Initial Phase - Project Structure Initialization (01/16)  
> 🎯 **Phase Purpose**: Set up foundational directory structure and build system  
> ⬅️ **Previous Stage**: 00.5-review-vision (Vision Review)  
> ➡️ **Next Stage**: 02-sprint-planning (Sprint Planning)
>
> **📋 3-Layer Architecture Operations**:  
> - 🎯 **Strategic**: `docs/use_cases/core/index.md` (Reference)  
> - 📊 **Tactical**: `docs/use_cases/index.md` (Reference)  
> - 🔧 **Execution**: Directory structure setup (Infrastructure foundation)

## 🏗️ **PHASE PURPOSE: PROJECT STRUCTURE SETUP ONLY**

**⚠️ Important Notice:**
- **This step is INFRASTRUCTURE SETUP ONLY** - Create directory structure and build system
- **NO FEATURE IMPLEMENTATION** - Focus on foundational structure and tooling  
- **Foundation phase** - Set up directories, dependencies, and development tools
- **Create project skeleton ONLY** - No business logic or feature code

**What this step does:**
1. `00-create-vision` ← Vision document and core scenarios
2. `01-init-project-structure` ← **【YOU ARE HERE】Project structure and tooling setup**
3. `02-sprint-planning` ← Sprint planning from scenarios
4. Then TDD/DDD implementation cycle begins

**CREATE PROJECT INFRASTRUCTURE ONLY.**

## Common Errors and Solutions

### ❌ Error Case 1: Project already initialized
**Cause**: `src/`, `docs/`, or `tests/` directories already exist  
**Solution**: 
- Back up existing structure (automatically prompted)
- Choose to overwrite (enter `y` at prompt)
- Or run in clean directory

### ❌ Error Case 2: Insufficient disk space
**Cause**: Less than 100MB available  
**Solution**: Free up disk space before running

### ❌ Error Case 3: Python package import errors
**Cause**: Incorrect Python environment or missing dependencies  
**Solution**: 
```bash
# Ensure Python 3.9+ is installed
python --version
# Install uv if not available
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Execution Examples

### ✅ Success Example
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

### ❌ Failure Example and Fix
```bash
$ /init-project-structure
⚠️  プロジェクト構造が既に存在します
既存の構造を上書きしますか？ (y/N): n
プロジェクト初期化をキャンセルしました

# Fix: Choose 'y' to overwrite, or run in new directory
```

## 📋 **PROJECT STRUCTURE INITIALIZATION TASK CHECKLIST**

**Use this checklist for comprehensive project infrastructure setup:**

### 🔴 Required Tasks

#### **🔧 Environment & Prerequisites**
- [ ] **Validate project directory**: Check for existing project configuration files
- [ ] **Check disk space**: Ensure minimum 100MB available for project structure
- [ ] **Validate permissions**: Ensure write permissions for directory creation

#### **📁 Directory Structure Creation**
- [ ] **Create domain layer directories**: entities, value_objects, services, repositories, events
- [ ] **Create application layer directories**: use_cases, dtos, exceptions
- [ ] **Create infrastructure layer directories**: repositories, persistence, external, config
- [ ] **Create presentation layer directories**: api (controllers/validators/serializers), cli, web
- [ ] **Create test structure directories**: unit, integration, e2e with layer subdivisions

#### **🐍 Python Package Setup**
- [ ] **Create __init__.py files**: All packages and subpackages with proper content
- [ ] **Validate package structure**: Ensure Python can import src package

### 🟡 Recommended Tasks

#### **⚙️ Configuration Files**
- [ ] **Create pyproject.toml**: Project metadata, dependencies, tool configurations
- [ ] **Set up pytest configuration**: Test discovery, coverage, markers
- [ ] **Configure ruff**: Linting and formatting rules
- [ ] **Configure pyright**: Type checking settings
- [ ] **Create .gitignore**: Python, testing, IDE, OS exclusions

#### **📦 Dependency Management**
- [ ] **Install core dependencies**: pydantic, fastapi, uvicorn via uv
- [ ] **Install dev dependencies**: pytest, pytest-asyncio, pytest-cov, ruff, pyright, anyio
- [ ] **Verify installation**: Test that all packages are properly installed

#### **📜 Git Repository Initialization**
- [ ] **Initialize git repository**: Set up version control if not exists
- [ ] **Create initial commit**: Commit entire project structure

### 🟢 Optional Tasks

#### **📚 Documentation Enhancement**
- [ ] **Create README.md**: Project overview, setup instructions, development workflow
- [ ] **Create use cases index**: Track implementation status and next steps
- [ ] **Document architecture**: Basic structure explanation in README
- [ ] **Create development guide**: TDD/DDD workflow instructions

#### **🔍 Advanced Validation**
- [ ] **Backup existing structure**: Safely backup any existing src/docs/tests directories
- [ ] **Set up package hierarchy**: Proper namespace organization
- [ ] **Test package imports**: Verify Python package structure works correctly
- [ ] **Validate uv environment**: Ensure package manager is working correctly
- [ ] **Set up git configuration**: Proper author information
- [ ] **Validate all directories**: Confirm all required directories exist
- [ ] **Test Python setup**: Run basic Python imports and pytest discovery
- [ ] **Verify configuration**: Check all config files are valid
- [ ] **Validate git repository**: Ensure proper git initialization and commit

**💡 Pro Tip**: Copy this checklist for use in actual projects!

## Task Details

1. **Setup Safe Environment and Validation**:
   ```bash
   # 🔧 Load all safe operation functions
   source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "01-init-project-structure" "$ARGUMENTS"
   
   # Check if we're in a valid project directory
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

2. **Begin Transaction and Pre-validation**:
   ```bash
   # 🔄 Start comprehensive transaction
   if ! begin_transaction "init_project_structure"; then
       echo "エラー: トランザクションの開始に失敗しました"
       exit 1
   fi
   
   # 📋 Check disk space (minimum 100MB required)
   if ! check_disk_space "." 100; then
       echo "エラー: プロジェクト初期化に十分なディスク容量がありません"
       execute_rollback "insufficient_disk_space"
       exit 1
   fi
   
   # 🔍 Check if project is already initialized
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
       
       # Backup existing structure
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

3. **Create TDD/DDD/Layered Architecture Directory Structure**:
   ```bash
   # 🏗️ Create comprehensive directory structure
   echo "🏗️ TDD/DDD/レイヤードアーキテクチャ ディレクトリ構造作成中..."
   
   # Define the complete directory structure
   directories=(
       # Source code structure (Clean Architecture layers)
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
       
       # Test structure (TDD approach)
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
       
       # Documentation structure (DDD approach)
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
   
   # Create all directories safely
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

4. **Create Essential Python Files with Safe Operations**:
   ```bash
   # 🐍 Create Python package structure
   echo "🐍 Pythonパッケージ構造作成中..."
   
   # Define __init__.py files to create
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
   
   # Create all __init__.py files with appropriate content
   for init_file in "${init_files[@]}"; do
       echo "  📄 作成中: $init_file"
       
       # Generate appropriate content based on the package
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

5. **Create Essential Configuration Files**:
   ```bash
   # ⚙️ Create essential configuration files
   echo "⚙️ 設定ファイル作成中..."
   
   # Create pyproject.toml if it doesn't exist
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

6. **Initialize Python Environment and Dependencies**:
   ```bash
   # 🔧 Initialize Python environment safely
   echo "🔧 Python環境初期化中..."
   
   # Validate Python environment
   if ! validate_python_environment; then
       echo "エラー: Python環境の検証に失敗しました"
       execute_rollback "python_env_validation_failed"
       exit 1
   fi
   
   # Install development dependencies safely
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
   
   # Install core dependencies
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

7. **Initialize Git Repository and Initial Commit**:
   ```bash
   # 📜 Initialize Git repository safely
   echo "📜 Gitリポジトリ初期化中..."
   
   # Check if already a git repository
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
   
   # Create .gitignore if it doesn't exist
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
   
   # Initial commit with all created structure
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

8. **Create Initial Documentation**:
   ```bash
   # 📚 Create initial documentation
   echo "📚 初期ドキュメント作成中..."
   
   # Create README.md if it doesn't exist
   if [[ ! -f "README.md" ]]; then
       echo "  📄 作成中: README.md"
       
       readme_content="# TDD/DDD/Layered Architecture Project

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
   
   # Create initial use cases index
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

9. **Final Validation and Success**:
   ```bash
   # 🔍 Final comprehensive validation
   echo "🔍 最終検証実行中..."
   
   # Validate directory structure
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
   
   # Validate Python packages
   if ! uv run python -c "import src" 2>/dev/null; then
       echo "エラー: Pythonパッケージ構造が正しくありません"
       execute_rollback "package_validation_failed"
       exit 1
   fi
   
   # Validate essential files
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
   
   # Validate Git repository
   if ! git status >/dev/null 2>&1; then
       echo "エラー: Gitリポジトリが正しく初期化されていません"
       execute_rollback "git_validation_failed"
       exit 1
   fi
   
   # Quick test run to validate setup
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
   
   # 🎉 Transaction commit (success!)
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
       
       # Show operation logs summary
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