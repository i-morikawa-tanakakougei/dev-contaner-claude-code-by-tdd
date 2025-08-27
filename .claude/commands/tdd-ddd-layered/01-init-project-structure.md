Use the 01-init-project-structure subagent to initialize project structure for TDD/DDD/Layered Architecture development. This command MUST USE the specialized 01-init-project-structure subagent for optimal project structure initialization.

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

**🤖 Agent Integration**: This command MUST USE PROACTIVELY the specialized `01-init-project-structure` subagent for optimal project structure initialization.

## 📖 Subagent Document Reading Instructions

This command delegates to the specialized `01-init-project-structure` subagent.

**MANDATORY: The subagent MUST read these files before execution:**

1. `docs/index.md` - Project overview and current status (if exists)
2. `/workspace/.claude/context/current-command-context.json` - Current execution context
3. `docs/vision/project-vision.md` - Project vision for structure alignment
4. `docs/use_cases/core/index.md` - Core scenarios for directory planning
5. Any existing project structure or configuration files
6. `README.md` - Project overview and setup information (if available)

**Command-Specific Reading Focus - Project Structure Setup:**
- Create TDD/DDD/Layered Architecture compliant directory structure
- Set up proper Python project configuration following clean architecture principles
- Initialize testing framework and quality tools configuration
- Establish project documentation and governance structure

**Additional Context for Subagent Execution:**
- Python project structure best practices and conventions
- TDD/DDD project organization patterns
- Development tool configuration requirements
- IMPORTANT: Use Read tool to access actual file contents, not just references

**CRITICAL:** Use the Read tool to actually read file contents, not just reference paths.

 Claude Code should automatically delegate this task to the 01-init-project-structure subagent based on the command description.

**MANDATORY: The subagent MUST read these files before execution:**

1. `docs/index.md` - Project overview and current status
2. `.claude/context/project-context.json` - Current project context  
3. `/workspace/.claude/context/current-command-context.json` - Current execution context
4. `docs/vision/project-vision.md` - Project vision for understanding requirements
5. `docs/steering/*.md` - Steering documents for technical and structural guidance
6. Any existing `README.md` - To understand current project setup
7. Any existing project structure files (`pyproject.toml`, etc.) - For conflict detection

**Command-Specific Reading Focus - Project Structure:**
- Read vision document to understand project scale and requirements
- Review technical steering documents for architecture decisions
- Check existing project files to avoid conflicts
- Understand team size and development approach from vision
- Review any existing directory structure for preservation needs

**CRITICAL:** Use the Read tool to actually read file contents, not just reference paths.

1. **Pre-execution Validation**:
   ```bash
   # 🔧 Load lightweight structure validation
   source "$(dirname "${BASH_SOURCE[0]}")/_validate_structure.sh"
   
   # Validate project initialization structure and preconditions
   echo "🏗️ プロジェクト構造初期化を開始します"
   
   # Execute structure validation with user interaction
   if ! main "01-init-project-structure"; then
       echo "❌ 構造確認が失敗しました"
       exit 1
   fi
   
   echo "✅ 前提条件確認完了: プロジェクト構造初期化準備完了"
   ```

2. **Context Preparation and Agent Execution**:
   ```bash
   # 🔄 Prepare context for agent (Pattern B: Hybrid approach)
   echo "🏗️ コンテキスト準備とエージェント起動..."
   
   # Create context file for project structure initialization
   context_file="/workspace/.claude/context/current-command-context.json"
   current_time=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
   
   # Build context JSON for project structure
   cat > "$context_file" <<EOF
   {
     "command": "init-project-structure",
     "timestamp": "$current_time",
     "phase": "project-initialization",
     "context": {
       "working_directory": "$(pwd)",
       "git_repo": $(git rev-parse --is-inside-work-tree 2>/dev/null && echo "true" || echo "false"),
       "existing_structure": $(ls -la . 2>/dev/null | wc -l),
       "architecture_patterns": ["TDD", "DDD", "Layered Architecture"]
     },
     "additional_instructions": "TDD/DDD/レイヤードアーキテクチャに基づいたプロジェクト構造を作成してください。Clean Architectureの原則に従い、依存関係の方向が適切になるようにディレクトリ構造を設計してください。",
     "special_considerations": [
       "既存ファイルとの競合回避",
       "Python環境の依存関係管理",
       "テストディレクトリの適切な配置",
       "ドキュメント構造の初期化"
     ],
     "custom_context": {
       "create_python_packages": true,
       "setup_development_environment": true,
       "initialize_testing_framework": true
     }
   }
   EOF
   
   echo "✅ コンテキストファイル作成完了: $context_file"
   
   # 🤖 Call the specialized agent with hybrid context
   echo ""
   echo "🏗️ プロジェクト構造初期化エージェントを起動します..."
   echo "専門エージェントがTDD/DDD/レイヤードアーキテクチャの基盤を構築します"
   echo ""
   
   # Actual Claude Code Task tool invocation with hybrid approach
   # Task tool execution with comprehensive prompt
   task_prompt="タスクを実行してください。

## コンテキスト情報の取得
1. 一時コンテキスト（プロジェクト情報）:
   - /workspace/.claude/context/current-command-context.json を読み込み

2. プロジェクト状況の確認:
   - 必要な文書やファイルを確認
   - 既存の実装や設計を参照

## 実行タスク
[01-init-project-structure固有のタスクを実行]

## 重要: 標準化出力形式の遵守
レポートは必ず以下の構造化セクションで終了してください：

### 📊 実行サマリー
各Critical Taskの完了状態を✅/❌で明記

### 📋 総合判定
APPROVED/CONDITIONAL_APPROVAL/REJECTED/COMPLETED のいずれかを明記

### 💡 次のステップ
判定に基づく具体的なアクションアイテムを列挙

## 処理完了後
- 実行結果の報告
- 次のステップへの案内"

   # Execute with specialized 01-init-project-structure subagent
   # The 01-init-project-structure subagent will be automatically invoked based on the task description
   
   agent_exit_code=$?
   echo "✅ 専用エージェント実行完了 (終了コード: $agent_exit_code)"
   
   agent_exit_code=$?
   echo "✅ エージェント呼び出し設定完了 (終了コード: $agent_exit_code)"
   echo "エージェントが以下の処理を実行します:"
   echo "  - コンテキストファイルからの環境情報取得"
   echo "  - TDD/DDD/レイヤードアーキテクチャディレクトリ構造作成"
   echo "  - Pythonパッケージ構造の初期化"
   echo "  - テストフレームワーク設定"
   echo "  - ドキュメント構造初期化"
   echo "  - 開発環境設定"
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
       
       # Clean up context file after successful execution
       if [[ -f "$context_file" ]]; then
           # Archive context to execution history
           echo "{\"timestamp\":\"$(date -Iseconds)\",\"command\":\"init-project-structure\",\"directory\":\"$(pwd)\",\"status\":\"completed\"}" >> /workspace/.claude/context/execution-history.jsonl
           rm -f "$context_file"
           echo "📝 コンテキストを実行履歴に記録し、一時ファイルをクリーンアップしました"
       fi
   else
       echo "❌ エージェント結果検証で問題が発見されました:"
       printf '  - %s\n' "${verification_issues[@]}"
       exit 1
   fi
   ```

4. **Advanced Task Verification**:
   ```bash
   # 🔧 Load advanced task verification library
   source "$(dirname "${BASH_SOURCE[0]}")/_task_verification.sh"
   
   # ✨ New: Advanced task verification with retry capability
   echo "🔍 Critical tasks確認中..."
   if ! verify_critical_tasks "01-init-project-structure" "$latest_report"; then
       echo "⚠️ Critical tasks確認で問題が検出されました - 再実行を試行します"
       prepare_retry_context "01-init-project-structure" "1" "${verification_issues[@]}"
       
       # Enhanced context for retry
       echo "🔄 再実行用の強化コンテキスト準備中..."
       prepare_enhanced_context "01-init-project-structure" "$context_file" "${verification_issues[@]}"
       
       echo "💡 推奨アクション: エージェントを再実行してください"
       echo "   重点項目: $(IFS='|'; echo "${verification_issues[*]}")"
       exit 1
   fi
   
   echo "✅ Critical tasks確認完了 - 全項目クリア"
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