# 22-recovery-session (MCP Session Recovery)

## 🎯 Expert Profile Declaration

During command execution, you act as a **Session Recovery Specialist** expert.

**Language Guidelines:**

- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Your Expertise

- **State Restoration**: Advanced session state recovery and validation
- **Data Integrity**: Comprehensive checkpoint integrity verification
- **Context Reconstruction**: Complete development context restoration
- **Continuity Assurance**: Seamless development workflow resumption

### Execution Principles

1. **Recovery Completeness**: Restore 100% of checkpointed session state
2. **Integrity Verification**: Validate all restored data integrity
3. **Context Continuity**: Maintain seamless development experience
4. **Rollback Safety**: Support safe recovery rollback if issues occur

### Quality Standards

- **Recovery Success Rate**: 99.9% successful session restoration
- **Data Integrity**: 100% checksum verification success
- **Restoration Speed**: < 30 seconds for complete recovery
- **Context Accuracy**: 100% development context preservation

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🔄 Enhanced Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16) → MCP Init(20) → Checkpoint(21) → **[Session Recovery]**

**🧠 MCP Integration**: Serena (Context Restoration) + Context7 (Documentation Recovery) + Session Management

**📋 Requirements**: Complete session recovery from checkpoint with full integrity validation

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: MCP Session Recovery (22/23)  
> 🎯 **Phase Purpose**: Restore complete development session from checkpoint  
> ⬅️ **Previous Stage**: 21-checkpoint-session (Session Checkpointing)  
> ➡️ **Next Stage**: 23-analytics-dashboard (Advanced Analytics)

## 🎯 PHASE PURPOSE: COMPLETE SESSION RECOVERY

**⚠️ Important Notice:**

- **This step focuses on STATE RESTORATION** - Complete session state recovery
- **INTEGRITY VALIDATION** - Comprehensive data integrity verification
- **CONTEXT RECONSTRUCTION** - Full development context restoration

**What this step does:**

1. Validate checkpoint integrity and completeness
2. Restore MCP integration state and memory
3. Reconstruct project documentation and progress
4. Verify restoration completeness and integrity
5. Resume development session with full context

## 📋 Session Recovery Management

### Required Setup

```bash
# Validate checkpoint parameter
if [[ -z "$1" ]]; then
    echo "ERROR: Checkpoint name required. Usage: /recovery-session <checkpoint-name>"
    echo "Available checkpoints:"
    ls -la .serena/checkpoints/ 2>/dev/null || echo "No checkpoints found"
    exit 1
fi

CHECKPOINT_NAME="$1"
echo "🔄 Starting session recovery from checkpoint: $CHECKPOINT_NAME"

# Execute the recovery process
SCRIPT_PATH=".claude/commands/tdd-ddd-layered-expert/utils/22-recovery-session.py"

if [[ -f "$SCRIPT_PATH" ]]; then
    echo "✅ Found recovery manager: $SCRIPT_PATH"
    uv run "$SCRIPT_PATH" "$CHECKPOINT_NAME"
    EXIT_CODE=$?

    if [[ $EXIT_CODE -eq 0 ]]; then
        echo "✅ Session recovery completed successfully"
    else
        echo "❌ Session recovery failed with exit code: $EXIT_CODE"
        exit $EXIT_CODE
    fi
else
    echo "❌ Recovery manager not found: $SCRIPT_PATH"
    echo "💡 Please ensure the Python implementation is available"
    exit 1
fi
```

## 🚀 Expert Execution Flow

### Phase 1: Checkpoint Validation

**Validate the following as expert (User interactions in Japanese):**

1. **Checkpoint Existence and Integrity**
   - Verify checkpoint directory exists at .serena/checkpoints/
   - Check checkpoint metadata and manifest files
   - Validate integrity checksums for all archived data
   - Assess checkpoint completeness and version compatibility

2. **Current State Assessment**
   - Check for existing active sessions that might conflict
   - Assess current project state and uncommitted changes
   - Identify potential conflicts with restoration
   - Prepare backup of current state if needed

### Phase 2: Pre-Recovery Preparation

**Prepare the following as expert (Instructions to Claude Code in English):**

1. **Conflict Resolution**
   ```
   - Backup current session state if it exists
   - Check for git uncommitted changes and warn user
   - Prepare rollback plan in case recovery fails
   - Clear existing MCP state that might conflict
   ```

2. **Integrity Verification**
   ```
   - Run checkpoint validation script
   - Verify all required files are present
   - Check integrity checksums match archived data
   - Validate metadata consistency
   ```

### Phase 3: Recovery Execution

**Execute the following as expert (Instructions to Claude Code in English):**

1. **Session State Restoration**
   ```bash
   # Restore session metadata and configuration
   Execute automatic recovery script from checkpoint
   Verify session directory structure is restored
   Recreate current session symlink
   ```

2. **Memory and Context Restoration**
   ```bash
   # Restore Serena MCP memory files
   Copy memory files from checkpoint archive
   Verify memory file integrity and format
   Use mcp__serena__list_memories to validate restoration
   ```

3. **Project Documentation Restoration**
   ```bash
   # Restore project documentation and progress
   Restore docs/use_cases from checkpoint
   Restore docs/domain from checkpoint  
   Restore docs/vision from checkpoint
   Restore docs/metadata from checkpoint
   ```

4. **MCP Integration Restoration**
   ```bash
   # Restore MCP integration state
   Restore Context7 cached documentation
   Restore Serena symbol analysis cache
   Verify MCP connections are functional
   ```

### Phase 4: Post-Recovery Validation

**Validate the following as expert (Instructions to Claude Code in English):**

1. **Complete integrity verification**
   ```bash
   # Run comprehensive validation
   Execute checkpoint validation script
   Verify all files restored with correct checksums
   Check session metadata consistency
   Validate MCP integration functionality
   ```

2. **Session functionality testing**
   ```bash
   # Test restored session capabilities
   Use mcp__serena__list_memories to verify memory access
   Check project structure using mcp__serena__list_dir  
   Verify Context7 connection if applicable
   Test basic session operations
   ```

## ✅ Built-in Quality Assurance

### Self-Diagnosis Checklist
**Required Items (MUST):**
- [ ] Checkpoint integrity verified
- [ ] Session metadata restored
- [ ] Memory files recovered
- [ ] Project documentation restored
- [ ] MCP integration functional
- [ ] Recovery validation passed

**Recommended Items (SHOULD):**
- [ ] Current state backed up before recovery
- [ ] Git state preserved or restored
- [ ] All file checksums verified
- [ ] Context continuity maintained

### Quality Metrics
| Metric | Target | Actual | Assessment |
|--------|--------|--------|------------|
| Recovery Completeness | 100% | [Actual Value] | ✅/❌ |
| Integrity Verification | 100% | [Actual Value] | ✅/❌ |
| Session Functionality | 100% | [Actual Value] | ✅/❌ |

## 📊 Standardized Output Format

### 実行サマリー (日本語でユーザーに報告)
- ✅ **セッション回復完了**: [$CHECKPOINT_NAME] から正常に復旧
- ✅ **整合性検証**: 全アーカイブファイルの整合性確認済み
- ✅ **MCP統合復旧**: Serena + Context7機能復旧完了
- ✅ **コンテキスト復元**: 開発コンテキスト完全復元済み

### 成果物
**復元されたデータ:**
- `.serena/sessions/current/`: セッションメタデータとMCP状態
- `.serena/memory/`: 永続化メモリファイル群
- `docs/`: プロジェクトドキュメントと進捗状況
- MCP integration state: Serena + Context7統合状態

### 総合判定
**ステータス**: `RECOVERY_COMPLETE`
**復元データサイズ**: [サイズ]MB
**セッション状態**: `ACTIVE_AND_READY`

### 次のステップ (日本語でユーザーに案内)
1. **開発継続**: 通常のTDD/DDDワークフローを再開
2. **状態確認**: `/analytics-dashboard` でプロジェクト状態確認
3. **進捗確認**: `/project-status` で進捗状況確認

**ユーザーへのメッセージ (日本語)**:

```
🎉 セッション回復完了！

🔄 回復情報:
   📝 チェックポイント: $CHECKPOINT_NAME
   📊 復元データ量: [size]MB
   ⏰ 回復完了時刻: [timestamp]
   🔍 検証済みファイル数: [count]

✅ 復元されたコンポーネント:
   🧠 MCPセッション状態 (Serena + Context7)
   📁 プロジェクトドキュメント構造
   🗃️ ドメインモデル・ユースケース仕様
   📊 テスト設計・実装進捗
   🔗 Git状態・メタデータ

🛡️ 整合性検証結果:
   ✅ 全ファイルチェックサム検証パス
   ✅ MCPメモリ整合性確認済み
   ✅ セッションメタデータ検証済み
   ✅ プロジェクト構造整合性確認済み

🚀 開発環境準備完了:
   💡 MCP強化機能利用可能
   📋 全てのTDD/DDDコマンド実行可能
   🔍 プロジェクト分析機能利用可能

📂 回復されたセッション:
   .serena/sessions/current/ (アクティブセッション)

✅ セッション回復完了 - 開発を再開できます！
```