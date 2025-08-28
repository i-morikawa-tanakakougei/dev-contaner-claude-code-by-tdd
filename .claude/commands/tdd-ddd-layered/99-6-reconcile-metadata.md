Use the 99-6-reconcile-metadata subagent to reconcile and update project metadata after emergency recovery process. This command MUST USE PROACTIVELY the specialized 99-6-reconcile-metadata subagent for optimal metadata reconciliation.

**📖 Required Reading**: Before execution, this command MUST read the following files:
- `/workspace/.claude/context/current-command-context.json` - Current execution context
- `/workspace/.claude/context/project-context.json` - Overall project state and active sprint information
- `/workspace/docs/metadata/project-state.json` - Integrated project status for update

## Metadata
- **Prerequisites**: Emergency fix validated, issue created, documentation synchronized, tests created
- **Input**: 
  - `--scope <project|sprint|issue>` (default: issue) - Scope of metadata reconciliation
- **Output**: 
  - Updated project-state.json with current status
  - Reconciled project-context.json
  - Synchronized metadata consistency
  - Status tracking updates
- **Dependencies**: Completed emergency recovery steps, existing metadata files
- **Execution Timing**: After emergency fix validation (99-5) and before final review

## 🎯 **TDD/DDD/LAYERED PROCESS CONTEXT**

**🚨 Emergency Recovery Workflow**: Recovery(99-1) → Issue Creation(99-2) → Sync Docs(99-3) → Retroactive Tests(99-4) → Validation(99-5) → **Metadata Reconcile(99-6)** → Final Review(99-7)

**🏗️ Metadata Reconciliation Architecture**: Collect→Analyze→Update→Verify  
**📋 Metadata Requirements**: Project state consistency, status tracking accuracy, recovery progress documentation
**🔄 Integration**: Ensures metadata accurately reflects post-emergency recovery state

> 📖 **Emergency Recovery System**: [99-X Series Commands](./README.md)  
> 🗺️ **Current Position**: Metadata Reconciliation (99-6/99-7)  
> 🎯 **Phase Purpose**: Update project metadata to reflect emergency recovery completion  
> ➡️ **Next Stage**: 99-7-review-emergency-recovery (Final Recovery Review)

## 🎯 **PHASE PURPOSE: METADATA RECONCILIATION**

**⚠️ Important Notice:**
- **This step is METADATA UPDATE ONLY** - Reconcile project tracking and status information
- **NO CODE CHANGES** - Focus on updating project state and tracking metadata  
- **Consistency restoration phase** - Ensure all metadata accurately reflects current project state
- **Update tracking files ONLY** - Maintain accurate project status and progress tracking

**What this step does:**
1. `99-5-validate-emergency-fix` ← Validate emergency fix implementation
2. `99-6-reconcile-metadata` ← **【YOU ARE HERE】Update project metadata and status tracking**
3. `99-7-review-emergency-recovery` ← Conduct final recovery review
4. Then emergency recovery process is complete

**RECONCILE METADATA ONLY.**

## Common Errors and Solutions

### ❌ Error Case 1: Metadata files not found
**Cause**: Required metadata files don't exist or are in unexpected locations  
**Solution**: 
- Check metadata structure: `find . -name "*metadata*" -o -name "project-state.json"`
- Initialize metadata if needed: `/init-project-structure`
- Create missing metadata files with default values

### ❌ Error Case 2: Inconsistent metadata state
**Cause**: Multiple metadata files contain conflicting information  
**Solution**: 
```bash
# Check metadata consistency
/use-case-status --validate-metadata
# Reconcile with broader scope
/reconcile-metadata --scope project
```

### ❌ Error Case 3: Metadata corruption
**Cause**: JSON syntax errors or invalid metadata structure  
**Solution**: 
```bash
# Validate JSON syntax
python -m json.tool docs/metadata/project-state.json
# Restore from backup if available
cp docs/metadata/project-state.json.backup docs/metadata/project-state.json
```

## Execution Examples

### ✅ Success Example - Issue Scope Reconciliation
```bash
$ /reconcile-metadata --scope issue
📊 メタデータ調整を開始します (スコープ: issue)

🔍 現在のプロジェクト状態分析中...
  📄 project-state.json: 最終更新 2時間前
  📄 project-context.json: 最終更新 30分前
  🎫 緊急対応関連Issue: #342

📋 緊急対応進捗状況確認中...
  ✅ Issue作成: #342 完了
  ✅ ドキュメント同期: 完了
  ✅ テスト作成: 完了 (カバレッジ: 82%)
  ✅ 検証: 完了 (適合度: B+)
  ⏳ メタデータ調整: 実行中

🔄 プロジェクト状態更新中...
  📊 project-state.json 更新:
    - emergency_recovery.issue_342.status = "metadata_reconciliation"
    - testing_metrics.emergency_test_coverage = 82
    - code_quality_metrics.last_validation = "2024-08-28T16:30:00Z"
    - workflow_statistics.emergency_recovery_commands.reconcile_metadata += 1

📝 プロジェクトコンテキスト更新中...
  📊 project-context.json 更新:
    - emergency_recovery_status.issue_342 = "reconciling_metadata"
    - documentation_status.last_sync = "2024-08-28T16:00:00Z"
    - current_state.overall_status = "Emergency Recovery - Metadata Reconciliation"

✅ Issue #342 スコープのメタデータ調整完了!

📊 更新されたメタデータ:
  - 緊急対応進捗: 6/7ステップ完了
  - プロジェクト健全性: 85% (良好)
  - 技術的負債: +1ポイント (軽微)
  - テストカバレッジ: 向上 (+15%)

次のステップ: /review-emergency-recovery --issue 342
```

### ✅ Success Example - Project Scope Reconciliation
```bash
$ /reconcile-metadata --scope project
📊 プロジェクト全体のメタデータ調整開始

🔍 全体状況分析中...
  📋 アクティブSprint: Sprint 3
  🎫 緊急対応Issue: 3件
  📈 プロジェクト進捗: 75%

🔄 包括的メタデータ更新中...
  📊 全Issue状況の再同期
  📊 Sprint進捗の正確な反映
  📊 チーム生産性指標の更新
  📊 技術的負債スコアの再計算

✅ プロジェクト全体のメタデータ調整完了!

💡 主要更新ポイント:
  - 緊急対応による品質メトリクス調整
  - Sprint進捗率の正確な反映
  - 技術的負債の現実的な評価
```

## 📋 **METADATA RECONCILIATION TASK CHECKLIST**

**Use this checklist for comprehensive metadata reconciliation:**

### 🔴 Required Tasks

#### **📊 Project State Analysis**
- [ ] **Current state assessment**: Analyze current project-state.json content and last update
- [ ] **Recovery progress verification**: Verify all emergency recovery steps are properly tracked
- [ ] **Inconsistency detection**: Identify discrepancies between different metadata sources

#### **🔄 Metadata Updates**
- [ ] **Project state updates**: Update project-state.json with latest recovery status
- [ ] **Context synchronization**: Update project-context.json with current state
- [ ] **Status consistency**: Ensure all status fields reflect actual project state

#### **📝 Tracking Information Updates**
- [ ] **Command execution tracking**: Update workflow statistics with emergency recovery usage
- [ ] **Progress milestones**: Mark appropriate milestones as completed
- [ ] **Timestamp synchronization**: Update all relevant timestamp fields

### 🟡 Recommended Tasks

#### **🎯 Quality Metrics Updates**
- [ ] **Test coverage metrics**: Update testing metrics with retroactive test results
- [ ] **Code quality scores**: Incorporate validation results into quality metrics
- [ ] **Technical debt tracking**: Update technical debt metrics based on validation findings

#### **📈 Progress and Status Reporting**
- [ ] **Sprint progress updates**: Update sprint-specific progress tracking
- [ ] **Team metrics**: Update relevant team productivity and quality metrics
- [ ] **Health score recalculation**: Recalculate overall project health scores

### 🟢 Optional Tasks

#### **🔍 Advanced Reconciliation Features**
- [ ] **Cross-reference validation**: Verify metadata consistency across all tracking files
- [ ] **Historical tracking**: Maintain historical progression of emergency recovery process
- [ ] **Predictive metrics**: Update predictive project completion estimates

#### **📊 Reporting and Analytics**
- [ ] **Reconciliation summary**: Generate summary of all metadata changes made
- [ ] **Impact analysis**: Document impact of emergency recovery on project metrics
- [ ] **Trend analysis**: Update trend data with emergency recovery effects

**💡 Pro Tip**: Use issue scope for specific emergency fixes, project scope for comprehensive updates!

## Task Details

**🤖 Agent Integration**: This command MUST USE PROACTIVELY the specialized `99-6-reconcile-metadata` subagent for optimal metadata reconciliation. Claude Code should automatically delegate this task to the 99-6-reconcile-metadata subagent based on the command description.

## 📖 Subagent Document Reading Instructions

This command delegates to the specialized `99-6-reconcile-metadata` subagent.

**MANDATORY: The subagent MUST read these files before execution:**

1. `/workspace/docs/metadata/project-state.json` - Current project state metadata
2. `/workspace/.claude/context/project-context.json` - Project context information
3. `/workspace/.claude/context/current-command-context.json` - Current execution context
4. `/workspace/.claude/context/execution-history.jsonl` - Command execution history
5. Any other metadata files in the project structure
6. GitHub issue information for issue-scoped reconciliation

**Command-Specific Reading Focus - Metadata Reconciliation:**
- Read all existing metadata files to understand current project state
- Analyze execution history to track emergency recovery progress
- Review GitHub issues to understand emergency recovery scope
- Check project context to maintain consistency with overall project status

**CRITICAL:** Use the Read tool to actually read file contents, not just reference paths.

## サブエージェント実行指示

このコマンドはサブエージェント `99-6-reconcile-metadata` を呼び出します。

**サブエージェントに対する明示的指示**:
- 実行開始前に以下のファイルを必ず読み込んでください:
  1. 全てのプロジェクトメタデータファイル - 現在の状態確認
  2. 実行履歴ファイル - 緊急対応コマンドの実行状況確認
  3. プロジェクトコンテキスト - 全体的な整合性確保
  4. GitHub Issue情報 - Issue単位での調整の場合
  
**重要**: リンクや参照だけでなく、実際にRead toolを使用してファイル内容を読み込むこと

Follow these steps:

1. **Pre-execution Validation**:
   ```bash
   # Validate and parse parameters
   reconcile_scope="issue"
   
   while [[ $# -gt 0 ]]; do
       case $1 in
           --scope)
               reconcile_scope="$2"
               shift 2
               ;;
           *)
               echo "⚠️ Unknown parameter: $1"
               echo "Usage: /reconcile-metadata [--scope project|sprint|issue]"
               exit 1
               ;;
       esac
   done
   
   # Validate scope parameter
   if [[ "$reconcile_scope" != "project" && "$reconcile_scope" != "sprint" && "$reconcile_scope" != "issue" ]]; then
       echo "❌ Invalid scope: $reconcile_scope. Must be 'project', 'sprint', or 'issue'"
       exit 1
   fi
   
   # Check for required metadata files
   metadata_files=(
       "docs/metadata/project-state.json"
       ".claude/context/project-context.json"
   )
   
   missing_files=()
   for file in "${metadata_files[@]}"; do
       if [[ ! -f "$file" ]]; then
           missing_files+=("$file")
       fi
   done
   
   if [[ ${#missing_files[@]} -gt 0 ]]; then
       echo "⚠️ 一部のメタデータファイルが見つかりません: ${missing_files[*]}"
       echo "💡 プロジェクト構造を確認するか、/init-project-structure を実行してください"
   fi
   
   echo "📊 メタデータ調整を開始します (スコープ: $reconcile_scope)"
   ```

2. **Context Preparation and Agent Execution**:
   ```bash
   # 🔄 Prepare context for metadata reconciliation agent
   echo "📋 プロジェクト状態分析とメタデータ調整コンテキスト準備..."
   
   # Get current git status
   git_status=$(git status --porcelain 2>/dev/null | wc -l)
   git_branch=$(git branch --show-current 2>/dev/null || echo "unknown")
   
   # Get recent emergency recovery commands from execution history
   emergency_commands=""
   if [[ -f ".claude/context/execution-history.jsonl" ]]; then
       emergency_commands=$(grep -E "99-[1-7]-" ".claude/context/execution-history.jsonl" 2>/dev/null | tail -10 | tr '\n' '|' || echo "")
   fi
   
   # Create context file
   context_file="/workspace/.claude/context/current-command-context.json"
   current_time=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
   
   # Build context JSON for metadata reconciliation
   cat > "$context_file" <<EOF
   {
     "command": "reconcile-metadata",
     "timestamp": "$current_time",
     "reconcile_scope": "$reconcile_scope",
     "phase": "metadata-reconciliation",
     "git_info": {
       "branch": "$git_branch",
       "uncommitted_changes": $git_status
     },
     "emergency_commands": "$emergency_commands",
     "context": {
       "git_repo": "true",
       "metadata_focus": "consistency_and_accuracy",
       "expected_outputs": [
         "updated_project_state",
         "reconciled_context",
         "synchronized_tracking"
       ],
       "reconciliation_areas": ["project_state", "context_info", "progress_tracking", "quality_metrics"]
     },
     "additional_instructions": "緊急対応プロセス完了後のプロジェクトメタデータを包括的に調整し、整合性を確保してください。",
     "special_considerations": [
       "全メタデータファイルの現在状態分析",
       "緊急対応コマンド実行履歴の反映", 
       "プロジェクト状態と実際の状況の整合性確保",
       "品質メトリクスと進捗追跡の正確性向上",
       "指定されたスコープに応じた調整粒度の最適化"
     ],
     "custom_context": {
       "emergency_recovery": true,
       "metadata_validation": "high",
       "consistency_priority": "critical"
     }
   }
   EOF
   
   echo "✅ メタデータ調整コンテキストファイル作成完了: $context_file"
   
   # 🤖 Call the specialized metadata reconciliation agent
   echo ""
   echo "📊 メタデータ調整エージェントを起動します..."
   echo "専門エージェントがプロジェクトメタデータを包括的に調整します"
   echo ""
   
   # Task tool execution with comprehensive prompt
   task_prompt="Execute the task.

## CRITICAL: Subagent Specification Reference
As a fallback mechanism in case the specialized subagent 99-6-reconcile-metadata is not properly invoked:
- MUST READ: /workspace/.claude/agents/99-6-reconcile-metadata.md
- Follow the specifications and requirements defined in this agent file
- Implement the exact same process and standards as defined in the subagent specification
- Ensure standardized output format compliance as specified in the agent document

## Context Information Gathering
1. Emergency Recovery Context:
   - Read /workspace/.claude/context/current-command-context.json

2. Metadata Analysis:
   - Read existing project metadata files
   - Check context files for consistency
   - Analyze project state and health metrics

## Task Execution
1. Metadata inconsistency detection and analysis
2. Cross-system synchronization and validation
3. Project state reconciliation and updates
4. Context file consistency verification
5. Health metrics recalculation and updates
6. Comprehensive metadata integration

## IMPORTANT: Standardized Output Format Compliance
Report MUST end with the following structured sections:

### 📊 Execution Summary
Mark completion status of each critical task with ✅/❌

### 📋 Overall Assessment
Provide comprehensive metadata reconciliation results and consistency status

### 💡 Next Steps
List specific follow-up actions for emergency recovery completion

## Post-Processing
- Update all metadata files with consistent information
- Reconcile project state across all systems
- Verify cross-system data consistency
- Guide final steps in emergency recovery process"

   # Execute with specialized 99-6-reconcile-metadata subagent
   # The 99-6-reconcile-metadata subagent will be automatically invoked based on the task description
   
   agent_exit_code=$?
   echo "✅ 専用エージェント実行完了 (終了コード: $agent_exit_code)"
   ```

3. **Agent Result Verification**:
   ```bash
   # 🔍 Verify metadata reconciliation results
   echo "🔍 メタデータ調整結果を検証中..."
   
   # Check if metadata files were updated
   updated_files=()
   for file in "${metadata_files[@]}"; do
       if [[ -f "$file" ]] && [[ "$file" -nt "$context_file" ]]; then
           updated_files+=("$file")
       fi
   done
   
   if [[ ${#updated_files[@]} -gt 0 ]]; then
       echo "📝 更新されたメタデータファイル:"
       for file in "${updated_files[@]}"; do
           echo "   ✅ $file"
       done
   else
       echo "💡 メタデータファイルの更新が検出されませんでした（既に最新の可能性）"
   fi
   
   # Validate JSON syntax of critical metadata files
   json_validation_passed=true
   for file in "${metadata_files[@]}"; do
       if [[ -f "$file" ]]; then
           if ! python -m json.tool "$file" >/dev/null 2>&1; then
               echo "❌ JSON構文エラー: $file"
               json_validation_passed=false
           fi
       fi
   done
   
   if [[ "$json_validation_passed" = true ]]; then
       echo "✅ 全メタデータファイルのJSON構文検証完了"
   else
       echo "⚠️ 一部のメタデータファイルにJSON構文エラーがあります"
   fi
   
   echo "✅ メタデータ調整結果検証完了"
   
   # Clean up context file after successful execution
   if [[ -f "$context_file" ]]; then
       # Archive context to execution history
       echo "{\"timestamp\":\"$(date -Iseconds)\",\"command\":\"reconcile-metadata\",\"scope\":\"$reconcile_scope\",\"status\":\"completed\"}" >> /workspace/.claude/context/execution-history.jsonl
       rm -f "$context_file"
       echo "📝 コンテキストを実行履歴に記録し、一時ファイルをクリーンアップしました"
   fi
   ```

4. **Display Reconciliation Summary**:
   ```bash
   # 📊 Display comprehensive reconciliation summary
   echo ""
   echo "🎉 メタデータ調整完了!"
   echo "======================"
   
   echo "📋 調整情報:"
   echo "   🎯 調整スコープ: $reconcile_scope"
   echo "   📅 実行時刻: $(date '+%Y-%m-%d %H:%M:%S')"
   echo "   🌿 Gitブランチ: $git_branch"
   echo "   📝 未コミット変更: $git_status 件"
   
   # Show updated metadata files
   if [[ ${#updated_files[@]} -gt 0 ]]; then
       echo ""
       echo "📊 更新されたメタデータ:"
       for file in "${updated_files[@]}"; do
           echo "   📄 $file"
       done
   fi
   
   echo ""
   echo "📋 推奨次のステップ:"
   case $reconcile_scope in
       "issue")
           echo "   1. 最終レビュー: /review-emergency-recovery --issue <issue-number>"
           echo "   2. 状況確認: /use-case-status"
           ;;
       "sprint")
           echo "   1. Sprint状況確認: /use-case-status"
           echo "   2. 全体レビュー: /review-emergency-recovery --detail-level full"
           ;;
       "project")
           echo "   1. プロジェクト状況確認: /project-status"
           echo "   2. 包括的レビュー: /review-emergency-recovery --detail-level full"
           echo "   3. チーム共有: 更新されたプロジェクト状況をチームに共有"
           ;;
   esac
   
   echo ""
   echo "💡 補足情報:"
   echo "   - 更新されたメタデータをGitコミットすることを検討してください"
   echo "   - プロジェクト状況が正確に反映されているか確認してください"
   echo "   - 異常な値がある場合は手動で調整を検討してください"
   echo ""
   echo "✅ メタデータ調整完了 - プロジェクト状況が正確に反映されました!"
   ```

## 🔄 **PHASE 3: ENHANCED INTEGRATION CAPABILITIES**

### **Critical Enhancement Features**
This command implements Phase 3 advanced metadata reconciliation capabilities:

1. **Intelligent Project State Analysis with Multi-source Data Integration**
2. **Automated Consistency Validation with Conflict Resolution** 
3. **Smart Scope-based Reconciliation with Granular Updates**
4. **Enhanced Tracking Synchronization with Historical Preservation**

### **Project State Updates**

**CRITICAL**: After successful metadata reconciliation, MUST update integrated project metadata:

1. **Project State Update**:
   ```bash
   # Update docs/metadata/project-state.json
   # - Set metadata_status.last_reconciliation_timestamp
   # - Update project_metadata.overall_status to reflect current state
   # - Increment workflow_statistics.metadata_reconciliation_count
   # - Update project_metadata.health_score based on reconciliation results
   ```

2. **Project Context Update**:
   ```bash
   # Update .claude/context/project-context.json  
   # - Set current_state.last_metadata_reconciliation
   # - Update current_state.last_command and last_command_timestamp
   # - Increment workflow_tracking.command_usage.reconcile_metadata
   # - Update metadata_consistency_status
   ```

**⚠️ Error Handling**: If metadata reconciliation fails:
- 📖 Consult: [Manual Sync Guide](../../docs/maintenance/manual-sync-guide.md)
- 🔄 Check Status: `/use-case-status` for current project state  
- 📊 Manual Update: Update metadata files manually and validate JSON syntax