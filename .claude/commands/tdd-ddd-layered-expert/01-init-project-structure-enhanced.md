# /init-project-structure-enhanced - MCP統合インテリジェントプロジェクト構造初期化

## 🎯 Purpose and Scope

Initialize comprehensive TDD/DDD/Layered Architecture project structure with MCP-enhanced intelligence for optimal development environment setup and architectural foundation establishment.

### Your Expertise (Core + MCP Enhanced)

**Core Initialization Expertise:**

- **Architecture Foundation**: TDD/DDD/Layered Architecture structure establishment
- **Development Environment**: Complete toolchain and dependency setup
- **Project Scaffolding**: Standard directory structure and file organization
- **Quality Infrastructure**: Testing, linting, and quality assurance setup

**MCP-Enhanced Capabilities:**

- **Intelligent Architecture Analysis**: Project structure optimization using Serena MCP
- **Best Practice Integration**: Context7-enhanced project setup patterns and industry standards
- **Template Enhancement**: Intelligent template generation with proven patterns
- **Configuration Optimization**: Automated development environment optimization

### Execution Principles (Core + MCP Enhanced)

**Core Principles:**

1. **Clean Architecture**: Proper layer separation and dependency management
2. **Test-First Setup**: Complete testing infrastructure from project start
3. **Quality Gates**: Integrated quality assurance and continuous improvement tools

**MCP-Enhanced Principles:**
4. **Intelligence-Driven Setup**: Leverage MCP for optimal configuration patterns
5. **Context-Aware Templates**: Apply Context7 project setup best practices
6. **Predictive Configuration**: Use MCP intelligence for future-ready project structure

### Quality Standards (Core + MCP Enhanced)

**Core Standards:**

- **Architecture Compliance**: 100% adherence to Clean Architecture principles
- **Tool Integration**: Complete development toolchain setup and configuration
- **Documentation Foundation**: Comprehensive documentation structure and templates

**MCP-Enhanced Standards:**

- **Pattern Compliance**: 95% adherence to industry-standard project patterns
- **Configuration Optimization**: 90% optimal configuration for development efficiency
- **Future-Ready Structure**: 100% compatibility with anticipated project evolution
- **Intelligent Templates**: 95% coverage of common development scenarios

---

## 🚀 Commands in Workflow Context

### Position in Development Flow

```
📋 Current Position: /init-project-structure-enhanced
├── 01. init-project-structure ← **Current: Project foundation setup**
├── 00. create-vision ← Next: Vision and core scenarios
├── 02. sprint-planning ← Following: Sprint planning
├── [Full development workflow...]
```

4. New project or major restructuring ← Previous: Project inception decision

**Core Activities (Traditional):**

- Create standard TDD/DDD/Layered Architecture directory structure
- Set up Python development environment with essential tools
- Initialize Git repository and configuration files
- Create basic documentation templates and guidelines

**MCP-Enhanced Activities (Additional):**

- Analyze optimal project structure patterns using Serena MCP
- Apply Context7 project setup best practices automatically
- Generate intelligent configuration templates
- Create future-ready architecture foundation

---

## 🚀 MCP統合プロジェクト構造初期化実行フロー

```bash
#!/bin/bash
# MCP-Enhanced Project Structure Initialization

echo "🏗️ MCP-Enhanced Project Structure Initialization..."

# Phase 1: MCP セッション確認・環境準備
echo "📚 Phase 1: MCP session and environment analysis..."

# MCP利用可能性確認
if [[ -f ".serena/sessions/current/session-metadata.json" ]]; then
    echo "✅ Serena MCP detected - Enhanced project structure analysis available"
    echo "🎯 Intelligent architecture optimization enabled"
    MCP_AVAILABLE="true"
    echo "🔍 MCP Capabilities:"
    echo "  • Serena: Project structure optimization and pattern analysis"
    echo "  • Context7: Industry-standard setup patterns"
else
    echo "ℹ️ MCP session not found - Running in standard mode"
    echo "💡 To enable MCP enhancements, run /context-session-stageup first"
    echo "📋 Enhanced features when available:"
    echo "  • Intelligent project structure analysis"
    echo "  • Industry-standard pattern integration"
    echo "  • Future-ready architecture foundation"
    MCP_AVAILABLE="false"
fi

# Git repository check
if [[ -d ".git" ]]; then
    echo "✅ Git repository detected - Adding to existing project"
    EXISTING_PROJECT="true"
else
    echo "🆕 New project - Initializing complete structure"
    EXISTING_PROJECT="false"
fi

echo "📊 Environment Status:"
echo "  • MCP Intelligence: $MCP_AVAILABLE"
echo "  • Existing Project: $EXISTING_PROJECT"

# Phase 2: 既存プロジェクト分析
echo "🔍 Phase 2: Project context assessment..."

# 現在のディレクトリ構造確認
Use LS tool to analyze current directory structure
if [[ -f "pyproject.toml" ]]; then
    Use Read tool to analyze pyproject.toml
    echo "📄 Existing Python project configuration found"
fi

# プロジェクト状態確認
if [[ -f "docs/metadata/project-state.json" ]]; then
    Use Read tool to analyze docs/metadata/project-state.json
fi

# Phase 3: MCP拡張分析（利用可能時）
if [[ "$MCP_AVAILABLE" == "true" ]]; then
    echo "🧠 Phase 3: MCP-enhanced project structure analysis..."
    
    # Serenaプロジェクト構造最適化分析
    echo "📚 Serena: Analyzing optimal project structure patterns..."
    Use mcp__serena__list_dir "." --recursive=true to understand current structure
    Use mcp__serena__search_for_pattern "class.*Repository|class.*Service|class.*Entity" --restrict_search_to_code_files=true
    Use mcp__serena__get_symbols_overview for current code organization if files exist
    
    # Context7業界標準パターン分析
    echo "🌐 Context7: Analyzing industry-standard project patterns..."
    Use mcp__context7__resolve-library-id "project-structure-best-practices"
    Use mcp__context7__resolve-library-id "clean-architecture" 
    Use mcp__context7__get-library-docs "/clean-architecture" --topic "project-structure"
    Use mcp__context7__get-library-docs "/python-project-structure" --topic "tdd-ddd-patterns"
    
else
    echo "📋 Phase 3: Standard mode - Basic project analysis"
fi

# Phase 4: アーキテクチャ設計計画
echo "🎨 Phase 4: Architecture design planning..."

Ask user for the following project information in Japanese:
1. プロジェクトタイプ (Web API, CLI, ライブラリ等)
2. 主要な技術スタック選好 (FastAPI, SQLAlchemy等)
3. テスト戦略の選好 (pytest構成、カバレッジ要件等)
4. 開発チーム規模と開発スタイル
5. 特別な品質要件や制約

# Phase 5: ディレクトリ構造作成
echo "📁 Phase 5: Creating comprehensive directory structure..."

# Clean Architecture準拠ディレクトリ作成
Create the following directory structure:

# メイン アーキテクチャレイヤー
mkdir -p domain/entities
mkdir -p domain/value_objects  
mkdir -p domain/services
mkdir -p domain/repositories
mkdir -p domain/events

mkdir -p application/use_cases
mkdir -p application/dtos
mkdir -p application/exceptions

mkdir -p infrastructure/repositories
mkdir -p infrastructure/persistence/models
mkdir -p infrastructure/persistence/mappers
mkdir -p infrastructure/external
mkdir -p infrastructure/config

mkdir -p presentation/api/controllers
mkdir -p presentation/api/validators
mkdir -p presentation/api/serializers
mkdir -p presentation/cli
mkdir -p presentation/web

# 包括的テスト構造
mkdir -p tests/unit/domain/entities
mkdir -p tests/unit/domain/value_objects
mkdir -p tests/unit/domain/services
mkdir -p tests/unit/application/use_cases
mkdir -p tests/integration/repositories
mkdir -p tests/integration/external
mkdir -p tests/e2e/api
mkdir -p tests/fixtures
mkdir -p tests/reports

# 文書化構造
mkdir -p docs/use_cases
mkdir -p docs/domain
mkdir -p docs/application
mkdir -p docs/architecture
mkdir -p docs/guides
mkdir -p docs/decisions

# Phase 6: Python環境・依存関係セットアップ
echo "🐍 Phase 6: Python environment and dependency setup..."

# uv プロジェクト初期化（存在しない場合）
if [[ ! -f "pyproject.toml" ]]; then
    echo "🆕 Initializing new uv project..."
    Use Bash tool: uv init
fi

# 開発依存関係インストール
echo "📦 Installing development dependencies..."
Use Bash tool: uv add --dev pytest pytest-cov pytest-asyncio anyio ruff pyright pre-commit

# 条件付き依存関係（ユーザー要求に基づく）
Based on user project type selection:
- For Web API: uv add fastapi uvicorn
- For Database projects: uv add sqlalchemy alembic
- For Data validation: uv add pydantic
- For CLI projects: uv add click or typer

# Phase 7: 設定ファイル生成
echo "⚙️ Phase 7: Generating configuration files..."

# pytest設定
Create pytest.ini with:
[pytest]
testpaths = tests
python_files = test_*.py *_test.py
python_functions = test_*
python_classes = Test*
addopts = 
    --strict-markers
    --disable-warnings
    --cov=domain
    --cov=application
    --cov=infrastructure
    --cov=presentation
    --cov-report=term-missing
    --cov-report=html:htmlcov
asyncio_mode = auto
markers =
    unit: Unit tests
    integration: Integration tests
    e2e: End-to-end tests
    slow: Slow running tests

# ruff設定
Create ruff.toml with:
[tool.ruff]
line-length = 120
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "W", "I", "N", "UP", "ANN", "S", "B", "A", "COM", "DTZ", "EM", "G", "PIE", "T20", "SIM", "ARG", "PTH", "PD", "PGH", "PL", "TRY", "NPY", "RUF"]
ignore = ["ANN101", "ANN102", "S101"]

[tool.ruff.lint.per-file-ignores]
"tests/*" = ["S101", "ARG"]

[tool.ruff.lint.isort]
known-first-party = ["domain", "application", "infrastructure", "presentation"]

# .gitignore作成
Create .gitignore with standard Python ignores and project-specific patterns

# Phase 8: 文書テンプレート作成
echo "📚 Phase 8: Creating documentation templates..."

# README.md作成
Create README.md with:
- Project overview and purpose
- Architecture overview (Clean Architecture)
- Development setup instructions
- Testing strategy
- Quality standards
- Contribution guidelines

# Architecture documentation
Create docs/architecture/README.md with:
- Clean Architecture layer descriptions
- Dependency rules and flow
- Development workflow
- Quality standards and practices

# Phase 9: __init__.py ファイル作成
echo "🐍 Phase 9: Creating Python package files..."

# 全Python パッケージディレクトリに __init__.py 作成
Find all Python package directories and create __init__.py files

# Phase 10: MCP拡張文書作成（利用可能時）
if [[ "$MCP_AVAILABLE" == "true" ]]; then
    echo "🧠 Phase 10: Creating MCP-enhanced documentation..."
    
    # MCP強化アーキテクチャ文書
    Create docs/architecture/mcp-enhanced-architecture.md with:
    - Serena MCP project structure analysis results
    - Context7 pattern integration rationale
    - Intelligent configuration explanations
    - Future evolution planning based on MCP insights
    
    # MCP統合ガイド
    Create docs/guides/mcp-integration-guide.md with:
    - MCP tool setup and configuration
    - Enhanced development workflow with MCP
    - Intelligence-driven development practices
    - Continuous improvement strategies with MCP
    
    # Serena memory への学習内容保存
    Use mcp__serena__write_memory "project-structure-$(date +%Y%m%d)" "Project structure initialization completed with Clean Architecture layers, comprehensive testing setup, and MCP enhancements applied"
fi

# Phase 11: Git初期化・初回コミット
echo "📝 Phase 11: Git initialization and initial commit..."

# Git初期化（新規プロジェクトの場合）
if [[ "$EXISTING_PROJECT" == "false" ]]; then
    Use Bash tool: git init
fi

# 初回コミット
Use Bash tool: git add .

if [[ "$MCP_AVAILABLE" == "true" ]]; then
    Use Bash tool: git commit -m "feat: initialize TDD/DDD/Layered Architecture project with MCP enhancement

Complete project structure setup with:
- Clean Architecture layers (Domain, Application, Infrastructure, Presentation)  
- Comprehensive testing infrastructure
- Quality assurance toolchain (pytest, ruff, pyright)
- Enhanced with MCP intelligent configuration and optimization

🎯 Generated with Claude Code"
else
    Use Bash tool: git commit -m "feat: initialize TDD/DDD/Layered Architecture project

Complete project structure setup with:
- Clean Architecture layers (Domain, Application, Infrastructure, Presentation)
- Comprehensive testing infrastructure  
- Quality assurance toolchain (pytest, ruff, pyright)

🎯 Generated with Claude Code"
fi

# Phase 12: 品質保証・検証
echo "✅ Phase 12: Quality assurance and verification..."

# 品質チェックリスト実行
Verify the following quality standards:

**Required Items (MUST):**
- [ ] Complete architectural layer structure created
- [ ] Python development environment properly configured  
- [ ] Testing infrastructure fully functional
- [ ] Quality assurance tools installed and configured
- [ ] Documentation foundation established
- [ ] Git repository initialized with proper configuration

**Recommended Items (SHOULD) - MCP Enhanced:**
- [ ] Serena MCP project structure analysis utilized (if MCP available)
- [ ] Context7 setup patterns applied effectively (if MCP available)
- [ ] Advanced configuration templates generated (if MCP available) 
- [ ] Future-ready architecture foundation established (if MCP available)

# Phase 13: 実行サマリー・次ステップ案内
echo "🎉 Phase 13: Completion summary and next steps..."

Display to user in Japanese:
## ✅ 実行サマリー

**基本機能 (常に実行):**
- ✅ **プロジェクト構造作成**: Clean Architecture準拠の完全なディレクトリ構造
- ✅ **開発環境構築**: Python + uv + テスト + 品質ツール完全セットアップ  
- ✅ **品質インフラ**: pytest, ruff, pyright, pre-commit統合環境
- ✅ **文書化基盤**: docs/architecture/, docs/guides/等の包括的文書構造

**MCP拡張機能 (利用可能時):**
- ✅ **MCPプロジェクト解析**: Serenaによる最適プロジェクト構造分析完了
- ✅ **インテリジェント設定**: Context7最新セットアップパターン適用完了
- ✅ **将来対応基盤**: 拡張性・保守性を考慮した最適化アーキテクチャ
- ✅ **拡張文書**: MCP統合ガイドとアーキテクチャ文書生成完了

## 📁 成果物

**基本ファイル (常に作成):**
- Complete directory structure (domain/, application/, infrastructure/, presentation/, tests/, docs/)
- Configuration files (pytest.ini, ruff.toml, .gitignore, pyproject.toml)
- Documentation templates (README.md, docs/architecture/README.md)
- All necessary __init__.py files

**MCP拡張ファイル (利用可能時):**
- `docs/architecture/mcp-enhanced-architecture.md`: MCP強化アーキテクチャ設計
- `docs/guides/mcp-integration-guide.md`: MCP統合開発ガイド
- Enhanced configuration files with intelligent optimization

## 🚀 次のステップ

1. **即座に実行可能**: `/create-vision-enhanced` でビジョンとコアシナリオ策定
2. **推奨**: プロジェクトビジョン定義とGiven-When-Thenシナリオ作成
3. **確認推奨**: 作成された構造とツール設定の動作確認

# メタデータ更新
Create docs/metadata/command-execution-log.json with:
{
  "command_executed": "init-project-structure-enhanced",
  "timestamp": "[current timestamp]",
  "status": "SUCCESS", 
  "phase": "project-structure-initialization",
  "mcp_enhancements": {
    "serena_structure_analysis": [MCP_AVAILABLE],
    "context7_pattern_integration": [MCP_AVAILABLE],
    "intelligent_configuration": [MCP_AVAILABLE],
    "future_ready_architecture": [MCP_AVAILABLE]
  },
  "metrics": {
    "directories_created": "[number]",
    "config_files_generated": "[number]", 
    "dependencies_installed": "[number]",
    "documentation_files": "[number]"
  },
  "next_recommended": ["create-vision-enhanced", "sprint-planning-enhanced"]
}

echo "🎯 MCP統合プロジェクト構造初期化が完了しました！"
```

---

🎯 **MCP統合プロジェクト構造初期化コマンド完成**

**使用方法**:
```bash
/init-project-structure-enhanced
```

**MCP拡張機能** (利用可能時):
- 🧠 **Serena**: プロジェクト構造最適化・パターン分析
- 📚 **Context7**: 業界標準セットアップパターン・最新手法統合