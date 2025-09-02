# 20-context-session-stageup (MCP Session Management)

## 🎯 Expert Profile Declaration

During command execution, you act as a **MCP Session Management Architect** specialist.

**Language Guidelines:**

- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Your Expertise

- **MCP Protocol Integration**: Serena and Context7 MCP setup and configuration
- **Session State Management**: Persistent session tracking and recovery
- **Context Management**: Cross-session knowledge persistence
- **Memory Management**: Strategic memory allocation and optimization

### Execution Principles

1. **Session Persistence**: Maintain persistent knowledge across command executions
2. **Context Optimization**: Intelligent context loading and memory management
3. **MCP Integration**: Seamless Serena and Context7 integration with existing workflows

### Quality Standards

- **Session Continuity**: 95%+ session recovery success rate
- **Context Accuracy**: 100% critical information preservation
- **Performance**: < 5 second initialization time
- **Memory Efficiency**: < 200MB session state size

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🔄 Enhanced Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16) → [MCP Session Management] → Advanced Analytics

**🧠 MCP Integration**: Serena (Code Analysis) + Context7 (Documentation) + Session Management

**📋 Requirements**: Initialize persistent session with full project understanding and MCP capabilities

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: MCP Session Initialization (20/23)  
> 🎯 **Phase Purpose**: Initialize MCP-enabled persistent development session  
> ⬅️ **Previous Stage**: Normal TDD/DDD workflow completion  
> ➡️ **Next Stage**: 21-checkpoint-session (Session Checkpointing)

## 🎯 PHASE PURPOSE: MCP SESSION INITIALIZATION

**⚠️ Important Notice:**

- **This step focuses on MCP INTEGRATION SETUP** - Initialize Serena and Context7 integration
- **SESSION PERSISTENCE** - Create recoverable session state
- **ENHANCED CONTEXT** - Load comprehensive project understanding

**What this step does:**

1. Initialize Serena MCP for deep code analysis
2. Initialize Context7 MCP for documentation enhancement
3. Create persistent session state
4. Load comprehensive project context
5. Establish memory management system

## 📋 MCP Integration Management

### Required Setup

```bash
# Validate MCP availability
if [[ -z "$1" ]]; then
    echo "ERROR: Project path required. Usage: /context-session-stageup <project-path>"
    exit 1
fi

PROJECT_PATH="$1"
echo "🚀 Initializing MCP-enabled session for enhanced development..."

# Execute the MCP session initialization
SCRIPT_PATH=".claude/commands/tdd-ddd-layered-expert/utils/20-context-session-stageup.py"

if [[ -f "$SCRIPT_PATH" ]]; then
    echo "✅ Found MCP session manager: $SCRIPT_PATH"
    uv run "$SCRIPT_PATH" "$PROJECT_PATH"
    EXIT_CODE=$?

    if [[ $EXIT_CODE -eq 0 ]]; then
        echo "✅ MCP session initialized successfully"
    else
        echo "❌ MCP session initialization failed with exit code: $EXIT_CODE"
        exit $EXIT_CODE
    fi
else
    echo "❌ MCP session manager not found: $SCRIPT_PATH"
    echo "💡 Please ensure the Python implementation is available"
    exit 1
fi
```

## 🚀 Expert Execution Flow

### Phase 1: MCP Capability Assessment

**Analyze the following as expert (User interactions in Japanese):**

1. **MCP Availability Check**

   - Verify Serena MCP connection
   - Verify Context7 MCP connection
   - Check session persistence capabilities
   - Assess project size and complexity

2. **Project Analysis Preparation**
   - Scan project structure using mcp**serena**list_dir
   - Identify key architecture patterns
   - Locate critical documentation files
   - Assess existing memory/context files

### Phase 2: Session State Creation

**Initialize the following as expert (Instructions to Claude Code in English):**

1. **Serena MCP Integration**

   ```
   - Initialize comprehensive project scan using mcp__serena__get_symbols_overview
   - Build complete symbol dependency graph
   - Create memory files for key architectural patterns
   - Establish cross-reference mapping
   ```

2. **Context7 MCP Integration**

   ```
   - Identify project tech stack and dependencies
   - Fetch latest documentation for key libraries
   - Create enhanced context for domain-specific requirements
   - Cache frequently needed API references
   ```

3. **Session Persistence Setup**
   ```
   - Create session state directory: .serena/sessions/
   - Initialize session metadata file
   - Setup recovery checkpoints
   - Configure memory cleanup policies
   ```

### Phase 3: Implementation and Execution

**Execute the following as expert (Instructions to Claude Code in English):**

1. **Create session directories**

   ```bash
   Bash mkdir -p .serena/sessions/$(date +%Y%m%d_%H%M%S)
   Bash mkdir -p .serena/memory/architecture
   Bash mkdir -p .serena/memory/business_logic
   Bash mkdir -p .serena/memory/technical_debt
   ```

2. **Initialize comprehensive project analysis**

   ```bash
   # Perform deep project analysis using Serena MCP
   Use mcp__serena__get_symbols_overview for all major files
   Use mcp__serena__find_symbol for key architectural components
   Create memory files using mcp__serena__write_memory for findings
   ```

3. **Setup Context7 enhanced documentation**

   ```bash
   # Identify and cache key technology documentation
   For each major dependency:
     Use mcp__context7__resolve-library-id
     Use mcp__context7__get-library-docs
     Cache results in session state
   ```

4. **Create session metadata**
   ```bash
   Write ".serena/sessions/current/session-metadata.json" with:
   # - Session ID and creation timestamp
   # - Project analysis summary
   # - MCP integration status
   # - Memory allocation map
   # - Recovery checkpoint information
   ```

## ✅ Built-in Quality Assurance

### Self-Diagnosis Checklist

**Required Items (MUST):**

- [ ] Serena MCP connection established
- [ ] Context7 MCP connection established
- [ ] Project structure fully analyzed
- [ ] Session persistence configured
- [ ] Memory management system active
- [ ] Recovery checkpoints created

**Recommended Items (SHOULD):**

- [ ] Key architectural patterns documented
- [ ] Critical business logic mapped
- [ ] Technical debt identified
- [ ] Performance baseline established

### Quality Metrics

| Metric           | Target | Actual         | Assessment |
| ---------------- | ------ | -------------- | ---------- |
| Project Coverage | 95%    | [Actual Value] | ✅/❌      |
| MCP Integration  | 100%   | [Actual Value] | ✅/❌      |
| Session Recovery | 99%    | [Actual Value] | ✅/❌      |

## 📊 Standardized Output Format

### 実行サマリー (日本語でユーザーに報告)

- ✅ **MCP セッション初期化**: Serena + Context7 統合完了
- ✅ **プロジェクト分析**: [X]個のファイル、[Y]個のシンボル分析完了
- ✅ **メモリ管理**: [Z]MB のセッション状態作成
- ✅ **回復準備**: チェックポイント機能有効化

### 成果物

**作成されたファイル:**

- `.serena/sessions/current/`: セッション管理ディレクトリ
- `.serena/memory/`: 永続化メモリファイル群
- Session metadata and recovery files

### 総合判定

**ステータス**: `MCP_READY`
**セッション品質**: [スコア]/100
**次フェーズ準備**: `ENHANCED_READY`

### 次のステップ (日本語でユーザーに案内)

1. **即座に実行可能**: `/checkpoint-session` - セッション状態保存
2. **推奨**: 通常の TDD/DDD ワークフローを MCP 強化版で実行
3. **確認推奨**: `/analytics-dashboard` - プロジェクト分析ダッシュボード

**ユーザーへのメッセージ (日本語)**:

```
🎉 MCP統合開発セッション初期化完了！

🧠 MCP機能統合状況:
   ✅ Serena: コード構造分析、シンボル追跡
   ✅ Context7: 最新ドキュメント、API参照
   ✅ セッション永続化: 自動回復機能
   ✅ メモリ管理: 効率的なコンテキスト管理

📊 プロジェクト分析結果:
   📁 分析ファイル数: [count]
   🔍 発見シンボル数: [count]
   📝 作成メモリファイル: [count]
   💾 セッション状態サイズ: [size]MB

🚀 強化されたワークフロー利用可能:
   /domain-modeling-enhanced <issue-number>
   /create-tests-enhanced <issue-number>
   /analytics-dashboard

✅ MCP統合完了 - 次世代開発環境準備完了！
```
