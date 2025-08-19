Initialize project structure for TDD/DDD/Layered Architecture development using specialized agent.

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

## Task Details

**Agent Integration Pattern - 4 Steps:**

1. **Pre-execution Validation**:
   ```bash
   # 🔧 Load all safe operation functions
   source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "01-init-project-structure" "$ARGUMENTS"
   
   # Validate initialization preconditions
   echo "🏗️ プロジェクト構造初期化を開始します"
   
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
   
   # Check if project is already initialized
   if [[ -d "src" ]] || [[ -d "docs" ]] || [[ -d "tests" ]]; then
       echo "⚠️  プロジェクト構造が既に存在します"
       echo "既存の構造を上書きしますか？ (y/N): "
       read -n 1 -r
       echo
       if [[ ! $REPLY =~ ^[Yy]$ ]]; then
           echo "プロジェクト初期化をキャンセルしました"
           exit 0
       fi
   fi
   
   echo "✅ 前提条件確認完了: プロジェクト構造初期化準備完了"
   ```

2. **Execute Specialized Agent**:
   ```bash
   # 🤖 Delegate to specialized project structure initialization agent
   echo "🏗️ プロジェクト構造初期化エージェントを起動します..."
   echo "専門エージェントがTDD/DDD/レイヤードアーキテクチャの基盤を構築します"
   
   # Note: Agent integration happens automatically through Task tool with subagent_type="01-init-project-structure"
   
   agent_exit_code=$?
   echo "✅ 専用エージェント実行完了 (終了コード: $agent_exit_code)"
   ```

3. **Agent Result Verification**:
   ```bash
   # 🔍 Verify agent execution results
   echo "🔍 エージェント結果検証中..."
   
   verification_issues=()
   
   # Check that essential directories were created
   essential_dirs=("src/domain" "src/application" "src/infrastructure" "src/presentation" "tests" "docs")
   missing_dirs=()
   
   for dir in "${essential_dirs[@]}"; do
       if [[ ! -d "$dir" ]]; then
           missing_dirs+=("$dir")
       fi
   done
   
   if [[ ${#missing_dirs[@]} -eq 0 ]]; then
       echo "  ✅ 基本ディレクトリ構造確認"
   else
       verification_issues+=("必須ディレクトリが作成されていません: ${missing_dirs[*]}")
   fi
   
   # Check that essential configuration files exist
   essential_files=("pyproject.toml" ".gitignore" "README.md")
   missing_files=()
   
   for file in "${essential_files[@]}"; do
       if [[ ! -f "$file" ]]; then
           missing_files+=("$file")
       fi
   done
   
   if [[ ${#missing_files[@]} -eq 0 ]]; then
       echo "  ✅ 基本設定ファイル確認"
   else
       verification_issues+=("必須設定ファイルが作成されていません: ${missing_files[*]}")
   fi
   
   # Check Python package structure
   if uv run python -c "import src" 2>/dev/null; then
       echo "  ✅ Pythonパッケージ構造確認"
   else
       verification_issues+=("Pythonパッケージ構造が正しくありません")
   fi
   
   # Check Git repository
   if git status >/dev/null 2>&1; then
       echo "  ✅ Gitリポジトリ確認"
   else
       verification_issues+=("Gitリポジトリが正しく初期化されていません")
   fi
   
   # Check agent exit code
   if [[ $agent_exit_code -ne 0 ]]; then
       verification_issues+=("エージェント実行エラー (終了コード: $agent_exit_code)")
   fi
   
   # Report verification results
   if [[ ${#verification_issues[@]} -eq 0 ]]; then
       echo "✅ エージェント結果検証完了"
   else
       echo "❌ エージェント結果検証で問題が発見されました:"
       printf '  - %s\n' "${verification_issues[@]}"
       exit 1
   fi
   ```

4. **Display Success Summary**:
   ```bash
   # 🎉 Display comprehensive success summary
   echo ""
   echo "🎉 プロジェクト構造初期化完了!"
   echo ""
   echo "🏗️ 作成された構造:"
   echo "  📁 Domain Layer: ビジネスロジック (src/domain/)"
   echo "  📁 Application Layer: ユースケース (src/application/)"
   echo "  📁 Infrastructure Layer: データアクセス (src/infrastructure/)"
   echo "  📁 Presentation Layer: API・UI (src/presentation/)"
   echo ""
   echo "🧪 テスト構造:"
   echo "  📁 Unit Tests: 単体テスト (tests/unit/)"
   echo "  📁 Integration Tests: 統合テスト (tests/integration/)"
   echo "  📁 E2E Tests: E2Eテスト (tests/e2e/)"
   echo ""
   echo "📚 ドキュメント構造:"
   echo "  📁 Vision: プロジェクト方向性 (docs/vision/)"
   echo "  📁 Use Cases: 機能仕様 (docs/use_cases/)"
   echo "  📁 Domain: ビジネスロジック設計 (docs/domain/)"
   echo ""
   echo "📋 次のステップ:"
   echo "   💡 /create-vision (ビジョン作成)"
   echo "   💡 /sprint-planning 1 (最初のスプリント計画)"
   echo ""
   echo "🛠️ 開発コマンド:"
   echo "   • テスト実行: uv run pytest"
   echo "   • コード品質: uv run ruff check ."
   echo "   • 型チェック: uv run pyright"
   echo ""
   echo "📁 重要ファイル:"
   echo "  📝 README.md: プロジェクト概要"
   echo "  ⚙️ pyproject.toml: Python設定"
   echo "  📊 docs/use_cases/index.md: 実装状況"
   echo ""
   echo "🎯 プロジェクト基盤構築が正常に完了しました!"
   ```

**💡 Key Benefits of Project Structure Initialization:**
- **Foundation Setup**: Establish comprehensive TDD/DDD/Clean Architecture foundation
- **Tool Integration**: Configure all development tools and dependencies
- **Documentation Structure**: Create documentation framework for entire development lifecycle
- **Version Control**: Initialize Git repository with proper configuration
- **Development Ready**: Immediately ready for TDD/DDD development workflow

**🎯 Critical Success Factors:**
- Create complete Clean Architecture layer structure
- Establish comprehensive test framework (unit, integration, e2e)
- Configure all essential development tools (pytest, ruff, pyright)
- Initialize proper Python package structure
- Set up Git repository with appropriate .gitignore

**🚨 MANDATORY FOR CLAUDE CODE: NO FEATURE IMPLEMENTATION**

プロジェクト構造初期化はインフラ設定のみ
ビジネスロジックや機能実装は含まない
CRITICAL: 基盤構築に集中すること