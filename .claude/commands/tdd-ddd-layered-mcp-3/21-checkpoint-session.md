# 21-checkpoint-session (MCP Session Checkpointing)

## 🎯 Expert Profile Declaration

During command execution, you act as a **Session State Management Expert** specialist.

**Language Guidelines:**

- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Your Expertise

- **State Persistence**: Advanced session state serialization and storage
- **Recovery Planning**: Comprehensive checkpoint creation and validation
- **Memory Optimization**: Efficient context compression and storage
- **Continuity Assurance**: Guaranteed session restoration capabilities

### Execution Principles

1. **State Completeness**: Capture complete development context and progress
2. **Recovery Reliability**: Ensure 100% session restoration success
3. **Storage Efficiency**: Optimize checkpoint size while maintaining completeness
4. **Progressive Snapshots**: Support incremental checkpoint updates

### Quality Standards

- **Checkpoint Completeness**: 100% critical state preservation
- **Recovery Success Rate**: 99.9% session restoration reliability
- **Storage Efficiency**: < 50MB per checkpoint
- **Creation Speed**: < 10 seconds checkpoint creation time

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🔄 Enhanced Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16) → MCP Init(20) → **[Checkpoint Session]** → Recovery(22)

**🧠 MCP Integration**: Serena (State Analysis) + Context7 (Documentation State) + Checkpoint Management

**📋 Requirements**: Create comprehensive session checkpoint for reliable recovery

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: MCP Session Checkpointing (21/23)  
> 🎯 **Phase Purpose**: Create persistent checkpoint of current development state  
> ⬅️ **Previous Stage**: 20-context-session-stageup (MCP Session Initialization)  
> ➡️ **Next Stage**: 22-recovery-session (Session Recovery)

## 🎯 PHASE PURPOSE: SESSION STATE CHECKPOINTING

**⚠️ Important Notice:**

- **This step focuses on STATE PRESERVATION** - Capture complete session state
- **INCREMENTAL CHECKPOINTS** - Support progressive state updates
- **RECOVERY PREPARATION** - Prepare comprehensive recovery data

**What this step does:**

1. Analyze current session state and progress
2. Capture MCP integration status and memory
3. Create compressed checkpoint archives
4. Validate checkpoint integrity
5. Update recovery metadata

## 📋 Session Checkpointing Management

### Required Setup

```bash
# Validate checkpoint parameters
if [[ -z "$1" ]]; then
    echo "INFO: Using automatic checkpoint naming"
    CHECKPOINT_NAME="auto_$(date +%Y%m%d_%H%M%S)"
else
    CHECKPOINT_NAME="$1"
fi

echo "💾 Creating session checkpoint: $CHECKPOINT_NAME"

# Execute the checkpoint creation
SCRIPT_PATH=".claude/commands/tdd-ddd-layered-expert/utils/21-checkpoint-session.py"

if [[ -f "$SCRIPT_PATH" ]]; then
    echo "✅ Found checkpoint manager: $SCRIPT_PATH"
    uv run "$SCRIPT_PATH" "$CHECKPOINT_NAME"
    EXIT_CODE=$?

    if [[ $EXIT_CODE -eq 0 ]]; then
        echo "✅ Session checkpoint created successfully"
    else
        echo "❌ Session checkpoint failed with exit code: $EXIT_CODE"
        exit $EXIT_CODE
    fi
else
    echo "❌ Checkpoint manager not found: $SCRIPT_PATH"
    echo "💡 Please ensure the Python implementation is available"
    exit 1
fi
```

## 🚀 Expert Execution Flow

### Phase 1: Session State Analysis

**Analyze the following as expert (User interactions in Japanese):**

1. **Current Session Assessment**

   - Check active MCP integrations using mcp**serena**list_memories
   - Analyze session progression and current phase
   - Identify critical state that needs preservation
   - Assess memory usage and optimization needs

2. **Progress Tracking Analysis**
   - Scan completed TDD/DDD phases
   - Check issue status and metadata
   - Identify work in progress
   - Assess test coverage and implementation status

### Phase 2: Checkpoint Data Collection

**Collect the following as expert (Instructions to Claude Code in English):**

1. **MCP State Capture**

   ```
   - Export Serena memory files using mcp__serena__read_memory
   - Capture symbol analysis state and cross-references
   - Save Context7 cached documentation and API data
   - Archive current session metadata
   ```

2. **Project State Capture**

   ```
   - Capture current git status and branch information
   - Archive all use case specifications and domain models
   - Save test results and coverage reports
   - Capture implementation progress metadata
   ```

3. **Development Context Capture**
   ```
   - Save current issue assignments and priorities
   - Capture sprint planning state and progress
   - Archive review feedback and applied changes
   - Save refactoring history and technical debt items
   ```

### Phase 3: Checkpoint Creation and Validation

**Execute the following as expert (Instructions to Claude Code in English):**

1. **Create checkpoint archive**

   ```bash
   # Create checkpoint directory structure
   Bash mkdir -p .serena/checkpoints/$CHECKPOINT_NAME

   # Archive session state
   Use mcp__serena__read_memory for all memory files
   Copy session metadata and MCP integration data
   Archive project documentation and progress files
   ```

2. **Validate checkpoint integrity**

   ```bash
   # Verify checkpoint completeness
   Check all required files are archived
   Validate JSON metadata integrity
   Verify MCP state consistency
   Create checkpoint manifest file
   ```

3. **Update recovery metadata**

   ```bash
   Write ".serena/checkpoints/$CHECKPOINT_NAME/checkpoint-metadata.json" with:
   # - Checkpoint ID and creation timestamp
   # - Complete file manifest and checksums
   # - MCP integration state summary
   # - Recovery instructions and commands
   # - Progress tracking information
   ```

4. **Create recovery scripts**
   ```bash
   Write ".serena/checkpoints/$CHECKPOINT_NAME/recovery-script.sh" with:
   # - Automated recovery command sequence
   # - MCP re-initialization commands
   # - Session state restoration commands
   # - Validation and verification steps
   ```

## ✅ Built-in Quality Assurance

### Self-Diagnosis Checklist

**Required Items (MUST):**

- [ ] All session metadata archived
- [ ] MCP integration state captured
- [ ] Project progress preserved
- [ ] Checkpoint integrity validated
- [ ] Recovery scripts generated
- [ ] Checkpoint manifest complete

**Recommended Items (SHOULD):**

- [ ] Git state synchronized
- [ ] Test results archived
- [ ] Memory files optimized
- [ ] Documentation state captured

### Quality Metrics

| Metric              | Target | Actual         | Assessment |
| ------------------- | ------ | -------------- | ---------- |
| State Completeness  | 100%   | [Actual Value] | ✅/❌      |
| Archive Compression | 70%    | [Actual Value] | ✅/❌      |
| Recovery Validation | 100%   | [Actual Value] | ✅/❌      |

## 📊 Standardized Output Format

### 実行サマリー (日本語でユーザーに報告)

- ✅ **セッションチェックポイント作成**: [$CHECKPOINT_NAME] 作成完了
- ✅ **状態アーカイブ**: [X]MB のセッション状態を保存
- ✅ **整合性検証**: チェックポイント整合性確認済み
- ✅ **回復スクリプト作成**: 自動回復コマンド生成完了

### 成果物

**作成されたファイル:**

- `.serena/checkpoints/$CHECKPOINT_NAME/`: チェックポイントアーカイブ
- `checkpoint-metadata.json`: チェックポイントメタデータ
- `recovery-script.sh`: 自動回復スクリプト
- `checkpoint-manifest.json`: ファイルマニフェストと整合性データ

### 総合判定

**ステータス**: `CHECKPOINT_CREATED`
**アーカイブサイズ**: [サイズ]MB
**回復準備**: `RECOVERY_READY`

### 次のステップ (日本語でユーザーに案内)

1. **継続開発**: 通常の TDD/DDD ワークフローを継続
2. **回復テスト**: `/recovery-session $CHECKPOINT_NAME` で回復テスト
3. **チェックポイント管理**: 定期的なチェックポイント作成を推奨

**ユーザーへのメッセージ (日本語)**:

```
🎉 セッションチェックポイント作成完了！

💾 チェックポイント情報:
   📝 名前: $CHECKPOINT_NAME
   📊 アーカイブサイズ: [size]MB
   ⏰ 作成時刻: [timestamp]
   🔍 含まれるファイル数: [count]

🛡️ 保護されたデータ:
   ✅ MCPセッション状態 (Serena + Context7)
   ✅ プロジェクト進捗状況
   ✅ ドメインモデル・テスト設計
   ✅ 実装状況・メタデータ
   ✅ Git状態・ブランチ情報

🚀 回復機能:
   📋 自動回復スクリプト生成済み
   🔄 完全状態復元サポート
   ✅ 整合性検証パス済み

📂 チェックポイント場所:
   .serena/checkpoints/$CHECKPOINT_NAME/

✅ チェックポイント作成完了 - 安心して開発を継続できます！
```
