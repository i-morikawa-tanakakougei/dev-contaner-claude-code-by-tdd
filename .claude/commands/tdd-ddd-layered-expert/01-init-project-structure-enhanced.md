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

## 🔧 Setup Script

Execute this comprehensive setup to initialize MCP-enhanced project structure:

```bash
#!/bin/bash

# MCP availability check
echo "🔍 MCP統合プロジェクト構造初期化システム開始..."
if [[ -f ".serena/sessions/current/session-metadata.json" ]]; then
    echo "✅ Serena MCP detected - Enhanced project structure analysis available"
    echo "🎯 Intelligent architecture optimization enabled"
    MCP_AVAILABLE="true"
else
    echo "ℹ️ MCP session not found - Running in standard mode"
    echo "💡 To enable MCP enhancements, run /context-session-stageup first"
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

# Initialize enhanced project structure environment
echo "🎯 MCP Enhanced Project Structure Initialization"
echo "📊 MCP Intelligence: $MCP_AVAILABLE"
echo "🔗 Existing Project: $EXISTING_PROJECT"

echo "✅ MCP統合プロジェクト構造初期化準備完了"
echo ""
```

---

## 📊 Analysis Phase

**Analyze the following as expert (User interactions in Japanese):**

**Core Analysis Activities:**

1. **Project Context Assessment**

   - Analyze current directory structure and existing files
   - Identify project type and requirements (web API, CLI, library)
   - Assess development team preferences and standards
   - Review existing configuration files and dependencies
   - Determine optimal architecture patterns for project goals
   - Evaluate testing strategy and quality requirements

2. **Architecture Planning**
   - Plan Clean Architecture layer organization
   - Design domain model structure based on project scope
   - Plan application service organization
   - Design infrastructure and presentation layer structure
   - Plan testing strategy across all architectural layers
   - Establish documentation structure and templates

**MCP-Enhanced Analysis (if available):**
3. **Intelligent Architecture Optimization**

- Use mcp__serena__search_for_pattern to analyze existing project patterns
- Use mcp__serena__get_symbols_overview for codebase structure analysis
- Create memory using mcp__serena__write_memory for project setup insights

4. **Best Practice Pattern Integration**
   - Extract industry-standard project structure patterns
   - Identify optimal toolchain configuration
   - Plan scalable and maintainable architecture foundation
   - Document setup strategy in architecture memory

---

## 🎨 Design Phase

**Design the following as expert (Instructions to Claude Code in English):**

**Core Design Activities:**

1. **Directory Structure Design**

   ```
   Design comprehensive project structure:
   - domain/ (entities, value objects, services, repositories, events)
   - application/ (use cases, DTOs, exceptions)
   - infrastructure/ (repositories, persistence, external, config)
   - presentation/ (api, cli, web with controllers, validators, serializers)
   - tests/ (unit, integration, e2e with proper organization)
   - docs/ (use cases, domain, application, architecture)
   ```

2. **Development Environment Configuration**

   ```
   Plan complete toolchain setup:
   - Python virtual environment with uv
   - Testing framework (pytest, pytest-cov, anyio)
   - Code quality tools (ruff, pyright)
   - Pre-commit hooks for automated quality checks
   - CI/CD configuration templates
   ```

3. **Documentation Templates**

   ```
   Create comprehensive documentation foundation:
   - Architecture decision records (ADRs)
   - API documentation templates
   - Development workflow guides
   - Contribution guidelines
   ```

4. **Configuration Management**
   ```
   Design robust configuration system:
   - Environment-specific settings
   - Development vs production configurations
   - Security and secrets management
   - Monitoring and observability setup
   ```

**MCP-Enhanced Design (if available):**
5. **Context7 Project Pattern Integration**

```
Use mcp__context7__resolve-library-id for "project-structure-best-practices"
Use mcp__context7__get-library-docs for Clean Architecture patterns
Use mcp__context7__get-library-docs for TDD/DDD project setup
Integrate latest project structure methodologies
```

6. **Intelligent Template Generation**
   ```
   Apply advanced project patterns:
   - Framework-specific optimizations
   - Industry-standard configurations
   - Scalability-oriented structure
   - Future-proof architecture foundation
   ```

---

## ⚡ Implementation Phase

**Execute the following as expert (Instructions to Claude Code in English):**

**Core Implementation Steps:**

1. **Create foundational directory structure**

   ```bash
   # Create main architectural layers
   mkdir -p {domain/{entities,value_objects,services,repositories,events},application/{use_cases,dtos,exceptions},infrastructure/{repositories,persistence/{models,mappers},external,config},presentation/{api/{controllers,validators,serializers},cli,web}}
   
   # Create comprehensive test structure
   mkdir -p tests/{unit/{domain/{entities,value_objects,services},application/use_cases},integration/{repositories,external},e2e/api,fixtures,reports}
   
   # Create documentation structure
   mkdir -p docs/{use_cases,domain,application,architecture,guides,decisions}
   ```

2. **Initialize Python environment and dependencies**

   ```bash
   # Initialize uv project (if not exists)
   if [[ ! -f "pyproject.toml" ]]; then
       uv init
   fi
   
   # Install development dependencies
   uv add --dev pytest pytest-cov pytest-asyncio anyio ruff pyright pre-commit
   
   # Install common framework dependencies (conditional)
   # uv add fastapi uvicorn (for web APIs)
   # uv add sqlalchemy alembic (for database projects)
   # uv add pydantic (for data validation)
   ```

**MCP-Enhanced Implementation (if available):**
3. **Intelligent Configuration Generation**

```bash
# Enhanced project setup with MCP analysis
For each architectural component:
- Apply Serena MCP structure optimization
- Generate Context7-enhanced configuration templates
- Create intelligent development environment setup
- Establish future-ready project foundation
```

4. **Advanced Template Creation**

   ```bash
   # Generate optimized configuration files
   Create enhanced templates using MCP intelligence:
   - Optimal pytest configuration for DDD testing
   - Ruff configuration with architecture-specific rules
   - Pyright settings for Clean Architecture
   - Pre-commit hooks with intelligent quality gates
   ```

---

## 🎯 Output Generation

**Execute the following as expert (Instructions to Claude Code in English):**

1. **Create essential configuration files**

   ```bash
   # pytest.ini
   Write "pytest.ini" with:
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
   ```

2. **Generate quality configuration**

   ```bash
   # ruff.toml
   Write "ruff.toml" with:
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
   ```

3. **Create MCP enhancement documentation (if available)**

   ```bash
   if [[ "$MCP_AVAILABLE" == "true" ]]; then
       # MCP-enhanced project documentation
       Write "docs/architecture/mcp-enhanced-architecture.md" with:
       # - Serena MCP project structure analysis
       # - Context7 pattern integration rationale
       # - Intelligent configuration explanations
       # - Future evolution planning
       
       # MCP setup guide
       Write "docs/guides/mcp-integration-guide.md" with:
       # - MCP tool setup and configuration
       # - Enhanced development workflow
       # - Intelligence-driven development practices
       # - Continuous improvement with MCP
   fi
   ```

4. **Initialize Git and create initial documentation**

   ```bash
   # Initialize git repository (if not exists)
   if [[ "$EXISTING_PROJECT" == "false" ]]; then
       git init
   fi
   
   # Create .gitignore
   Write ".gitignore" with standard Python ignores
   
   # Create README.md
   Write "README.md" with project overview and setup instructions
   
   # Create architecture documentation
   Write "docs/architecture/README.md" with:
   # - Clean Architecture overview
   # - Layer responsibilities
   # - Development workflow
   # - Quality standards
   
   # Create all __init__.py files
   Find all Python package directories and create __init__.py
   
   # Initial commit
   git add .
   if [[ "$MCP_AVAILABLE" == "true" ]]; then
       git commit -m "feat: initialize TDD/DDD/Layered Architecture project with MCP enhancement
       
   Complete project structure setup with:
   - Clean Architecture layers (Domain, Application, Infrastructure, Presentation)
   - Comprehensive testing infrastructure
   - Quality assurance toolchain
   - Enhanced with MCP intelligent configuration
       
   🎯 Generated with Claude Code
       "
   else
       git commit -m "feat: initialize TDD/DDD/Layered Architecture project
       
   Complete project structure setup with:
   - Clean Architecture layers (Domain, Application, Infrastructure, Presentation)
   - Comprehensive testing infrastructure
   - Quality assurance toolchain
       
   🎯 Generated with Claude Code
       "
   fi
   ```

---

## ✅ Built-in Quality Assurance

### Self-Diagnosis Checklist

**Required Items (MUST):**

- [ ] Complete architectural layer structure created
- [ ] Python development environment properly configured
- [ ] Testing infrastructure fully functional
- [ ] Quality assurance tools installed and configured
- [ ] Documentation foundation established
- [ ] Git repository initialized with proper configuration

**Recommended Items (SHOULD):**

- [ ] Serena MCP project structure analysis utilized
- [ ] Context7 setup patterns applied effectively
- [ ] Advanced configuration templates generated
- [ ] Future-ready architecture foundation established

### Quality Metrics

| Metric | Target | Actual | Assessment |
|--------|--------|--------|------------|
| Directory Structure Completeness | 100% | [Actual Value] | ✅/❌ |
| Tool Configuration Completeness | 100% | [Actual Value] | ✅/❌ |
| Documentation Coverage | 90% | [Actual Value] | ✅/❌ |
| Quality Gate Functionality | 100% | [Actual Value] | ✅/❌ |

**MCP-Enhanced Metrics (if MCP Available):**
| Metric | Target | Actual | Assessment |
|--------|--------|--------|------------|
| Pattern Compliance | 95% | [Actual Value] | ✅/❌ |
| Configuration Optimization | 90% | [Actual Value] | ✅/❌ |
| Future-Ready Score | 85% | [Actual Value] | ✅/❌ |

---

## 📊 Standardized Output Format

### 実行サマリー (日本語でユーザーに報告)

**基本機能 (常に実行):**

- ✅ **プロジェクト構造作成**: Clean Architecture準拠の完全なディレクトリ構造
- ✅ **開発環境構築**: Python + uv + テスト + 品質ツール完全セットアップ  
- ✅ **品質インフラ**: pytest, ruff, pyright, pre-commit統合環境
- ✅ **文書化基盤**: docs/architecture/, docs/guides/等の包括的文書構造

**MCP拡張機能 (利用可能時):**

- ✅ **MCPプロジェクト解析**: Serenaによる最適プロジェクト構造分析完了
- ✅ **インテリジェント設定**: Context7最新セットアップパターン適用完了
- ✅ **将来対応基盤**: [X]年分の進化を考慮した拡張可能アーキテクチャ
- ✅ **テンプレート強化**: [Y]個の業界標準テンプレート自動生成

### 成果物

**基本ファイル (常に作成):**

- Complete directory structure (domain/, application/, infrastructure/, presentation/, tests/, docs/)
- Configuration files (pytest.ini, ruff.toml, .gitignore, pyproject.toml)
- Documentation templates (README.md, docs/architecture/README.md)
- All necessary __init__.py files

**MCP拡張ファイル (利用可能時):**

- `docs/architecture/mcp-enhanced-architecture.md`: MCP強化アーキテクチャ設計
- `docs/guides/mcp-integration-guide.md`: MCP統合開発ガイド
- Enhanced configuration files with intelligent optimization

### 総合判定

**ステータス**: `SUCCESS` (基本) / `MCP_ENHANCED_SUCCESS` (MCP利用時)
**構造完成度**: [完成度]/100
**MCPインテリジェンス活用**: [活用度]/100 (利用時のみ)
**次フェーズ準備**: `READY`

### 次のステップ (日本語でユーザーに案内)

1. **即座に実行可能**: `/create-vision-enhanced` でビジョンとコアシナリオ策定
2. **推奨**: プロジェクトビジョン定義とGiven-When-Thenシナリオ作成
3. **確認推奨**: 作成された構造とツール設定の動作確認

**ユーザーへのメッセージ (日本語)**:

```
🎉 インテリジェントプロジェクト構造初期化完了！

🏗️ 基本プロジェクト構造:
   ✅ Clean Architectureレイヤー: 4層完全分離
   ✅ テスト基盤: ユニット/統合/E2E完備
   ✅ 品質ツール: pytest + ruff + pyright統合
   ✅ 開発環境: uv + Git完全セットアップ

🤖 MCP強化構造 (利用時):
   🧠 Serena最適化: プロジェクト構造インテリジェント分析
   📊 Context7統合: 業界標準セットアップパターン適用
   🎯 将来対応: 拡張性・保守性最適化設計
   ✅ docs/architecture/mcp-enhanced-architecture.md
   ✅ docs/guides/mcp-integration-guide.md

📁 作成された構造:
   ✅ domain/ (エンティティ、値オブジェクト、サービス)
   ✅ application/ (ユースケース、DTO、例外)
   ✅ infrastructure/ (リポジトリ、永続化、外部連携)
   ✅ presentation/ (API、CLI、Web)
   ✅ tests/ (全層テスト + フィクスチャ)
   ✅ docs/ (アーキテクチャ + ガイド文書)

🎯 次のアクション:
   /create-vision-enhanced でプロジェクトビジョン策定

✅ プロジェクト構造初期化完了 - TDD/DDD/Layered開発準備完了！
```