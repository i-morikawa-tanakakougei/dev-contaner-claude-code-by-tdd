Use the 99-1-emergency-recovery subagent to analyze emergency fixes and initiate comprehensive recovery to standard TDD/DDD/Layered Architecture workflow. This command MUST USE PROACTIVELY the specialized 99-1-emergency-recovery subagent for optimal emergency response recovery.

**📖 Required Reading**: Before execution, this command MUST read the following files:
- `/workspace/.claude/context/current-command-context.json` - Current execution context
- `/workspace/.claude/context/project-context.json` - Overall project state and active sprint information
- `/workspace/docs/metadata/project-state.json` - Integrated project status for update

## Metadata
- **Prerequisites**: Git repository with emergency fixes that bypassed standard workflow
- **Input**: 
  - `--issue <issue-number>` (optional) - Specific issue to recover
  - `--branch <branch-name>` (optional) - Branch containing emergency fixes
  - `--mode <full|partial|analysis>` (default: full) - Recovery mode
- **Output**: 
  - Recovery analysis report
  - Prioritized action plan
  - Updated project metadata
- **Dependencies**: Git history, existing project structure
- **Execution Timing**: After emergency fixes that bypassed standard TDD/DDD/Layered process

## 🎯 **TDD/DDD/LAYERED PROCESS CONTEXT**

**🚨 Emergency Recovery Workflow**: Recovery(99-1) → Issue Creation(99-2) → Sync Docs(99-3) → Retroactive Tests(99-4) → Validation(99-5) → Metadata Reconcile(99-6) → Final Review(99-7)

**🏗️ Recovery Architecture**: Analyze→Plan→Execute→Verify  
**📋 Recovery Requirements**: Git analysis, document synchronization, test creation, metadata updates
**🔄 Integration**: Seamless transition back to standard 00-16 workflow after recovery

> 📖 **Emergency Recovery System**: [99-X Series Commands](./README.md)  
> 🗺️ **Current Position**: Emergency Recovery Analysis (99-1/99-7)  
> 🎯 **Phase Purpose**: Analyze emergency changes and create comprehensive recovery plan  
> ➡️ **Next Stage**: 99-2-create-retroactive-issue (Issue Creation) or specific recovery command

## 🎯 **PHASE PURPOSE: EMERGENCY RECOVERY ANALYSIS**

**⚠️ Important Notice:**
- **This step is ANALYSIS AND PLANNING** - Examine emergency fixes and create recovery strategy
- **NO IMMEDIATE FIX IMPLEMENTATION** - Focus on understanding changes and planning restoration  
- **Comprehensive assessment phase** - Identify gaps between current state and standard workflow
- **Create strategic recovery plan ONLY** - No code or document changes yet

**What this step does:**
1. `99-1-emergency-recovery` ← **【YOU ARE HERE】Emergency fix analysis and recovery planning**
2. `99-2-create-retroactive-issue` ← Create missing GitHub issues
3. `99-3-sync-documentation` ← Sync docs with code changes
4. Then continue with test creation and validation cycle

**ANALYZE AND PLAN RECOVERY ONLY.**

## Common Errors and Solutions

### ❌ Error Case 1: No emergency fixes detected
**Cause**: Current branch has no changes that bypassed standard workflow  
**Solution**: 
- Check git log for recent commits outside standard process
- Verify you're on the correct branch with emergency fixes
- Run with `--branch` parameter to specify emergency fix branch

### ❌ Error Case 2: Multiple conflicting emergency fixes
**Cause**: Multiple overlapping emergency changes detected  
**Solution**: 
```bash
# Run analysis mode first to understand scope
/emergency-recovery --mode analysis
# Then process individually with issue-specific recovery
/emergency-recovery --issue <specific-issue> --mode partial
```

### ❌ Error Case 3: Standard workflow files missing
**Cause**: Project structure doesn't match expected TDD/DDD/Layered format  
**Solution**: First run standard initialization:
```bash
/init-project-structure
```

## Execution Examples

### ✅ Success Example - Full Recovery
```bash
$ /emergency-recovery --mode full --branch hotfix/critical-bug
🚨 緊急対応復旧分析を開始します

📊 Git差分分析中...
  - 検出された緊急修正: 3件のコミット
  - 変更ファイル: src/payment.py, src/validation.py
  - 標準プロセス未実施箇所を特定

📋 ドキュメント整合性チェック中...
  ❌ Given-When-Thenシナリオ: payment-processing.md (未更新)
  ❌ ドメインモデル: domain-model.md (決済部分が未反映)
  ✅ メタデータ: project-state.json (最新)

🧪 テストカバレッジ分析中...
  ❌ 変更コードのテスト網羅率: 45% (標準: 80%以上)
  📝 不足テストケース: 12件特定

✅ 復旧計画生成完了!

📋 復旧アクションプラン (推定時間: 2.5時間)
==========================================
🔴 Critical (必須):
  1. Issue #234作成 - 決済処理緊急修正の文書化
  2. Given-When-Thenシナリオ更新 - payment-processing.md
  3. 不足テスト12件の作成と実行

🟡 High (推奨):
  4. ドメインモデル図の更新
  5. メタデータの整合性確認

🟢 Medium (任意):
  6. リファクタリング提案の検討

次のステップ: /create-retroactive-issue --commit a1b2c3d
```

### ✅ Success Example - Analysis Only
```bash
$ /emergency-recovery --mode analysis
🚨 緊急対応状況分析モード

📊 分析結果サマリー
================
🔍 検出された問題:
  - 未文書化コミット: 5件
  - 不整合ドキュメント: 3ファイル  
  - 不足テスト: 18ケース
  - メタデータ不整合: 2箇所

💡 推奨復旧順序:
  1. /create-retroactive-issue (5件のIssue作成)
  2. /sync-documentation --type all
  3. /retroactive-test --coverage-target 80
  4. /reconcile-metadata --scope project

📈 復旧完了予想: 3-4時間
```

## 📋 **EMERGENCY RECOVERY TASK CHECKLIST**

**Use this checklist for comprehensive emergency recovery analysis:**

### 🔴 Required Tasks

#### **🔍 Emergency Fix Analysis**
- [ ] **Git history analysis**: Identify commits that bypassed standard workflow
- [ ] **Change scope assessment**: Analyze affected files, functions, and business logic
- [ ] **Impact evaluation**: Determine scope of emergency changes vs. standard process

#### **📊 Document-Code Gap Analysis**
- [ ] **Given-When-Then scenario gaps**: Compare current scenarios vs. implemented functionality
- [ ] **Domain model inconsistencies**: Identify domain documentation that doesn't match code
- [ ] **Metadata synchronization**: Check project-state.json, context files alignment

#### **🧪 Test Coverage Analysis**
- [ ] **Coverage gap identification**: Determine untested emergency changes
- [ ] **Test quality assessment**: Evaluate existing test relevance to new changes
- [ ] **Risk assessment**: Identify critical paths without adequate testing

### 🟡 Recommended Tasks

#### **📋 Recovery Planning**
- [ ] **Priority classification**: Categorize recovery tasks by business impact (Critical/High/Medium/Low)
- [ ] **Time estimation**: Calculate realistic timeframes for each recovery activity
- [ ] **Resource allocation**: Determine team effort required for complete recovery

#### **🔄 Integration Strategy**
- [ ] **Workflow transition plan**: Strategy to return to standard 00-16 command sequence
- [ ] **Quality gate definition**: Set criteria for "recovery complete" status
- [ ] **Rollback planning**: Define contingency if recovery efforts need reversal

### 🟢 Optional Tasks

#### **📈 Advanced Analysis**
- [ ] **Technical debt assessment**: Evaluate if emergency fixes introduced technical debt
- [ ] **Architecture compliance**: Check if changes maintain DDD and layered architecture principles
- [ ] **Performance impact**: Assess if emergency changes affected system performance

#### **📊 Metrics and Reporting**
- [ ] **Recovery metrics definition**: Define success metrics for recovery process
- [ ] **Progress tracking setup**: Establish monitoring for recovery activities
- [ ] **Team communication plan**: Define how to communicate recovery status to stakeholders

**💡 Pro Tip**: Use analysis mode first for complex emergency situations before full recovery!

## Task Details

**🤖 Agent Integration**: This command MUST USE PROACTIVELY the specialized `99-1-emergency-recovery` subagent for optimal emergency recovery analysis. Claude Code should automatically delegate this task to the 99-1-emergency-recovery subagent based on the command description.

## 📖 Subagent Document Reading Instructions

This command delegates to the specialized `99-1-emergency-recovery` subagent.

**MANDATORY: The subagent MUST read these files before execution:**

1. `.git/log` - Git commit history for emergency fix identification
2. `docs/vision/project-vision.md` - Project vision for alignment check (if exists)
3. `docs/use_cases/` - Current scenario documentation for gap analysis
4. `/workspace/.claude/context/current-command-context.json` - Current execution context
5. `/workspace/docs/metadata/project-state.json` - Project status and metadata
6. Any existing documentation in `docs/` hierarchy for consistency assessment

**Command-Specific Reading Focus - Emergency Recovery:**
- Read git commit history to identify changes that bypassed standard workflow
- Compare current documentation state vs. actual implemented functionality
- Review project metadata to understand expected vs. actual project state
- Analyze test coverage and identify gaps from emergency changes

**CRITICAL:** Use the Read tool to actually read file contents, not just reference paths.

## サブエージェント実行指示

このコマンドはサブエージェント `99-1-emergency-recovery` を呼び出します。

**サブエージェントに対する明示的指示**:
- 実行開始前に以下のファイルを必ず読み込んでください:
  1. Gitログ - 緊急修正コミットの特定
  2. `docs/` - 現在のドキュメント状態確認
  3. `/workspace/docs/metadata/project-state.json` - プロジェクト状態確認
  4. `/workspace/.claude/context/current-command-context.json` - 実行コンテキスト確認
  
**重要**: リンクや参照だけでなく、実際にRead toolを使用してファイル内容を読み込むこと

Follow these steps:

1. **Pre-execution Validation**:
   ```bash
   # Validate git repository exists
   if ! git rev-parse --git-dir >/dev/null 2>&1; then
       echo "❌ Git repository not found. Emergency recovery requires git history."
       exit 1
   fi
   
   # Validate arguments
   mode="full"
   branch=""
   issue=""
   
   while [[ $# -gt 0 ]]; do
       case $1 in
           --mode)
               mode="$2"
               shift 2
               ;;
           --branch)
               branch="$2"
               shift 2
               ;;
           --issue)
               issue="$2"
               shift 2
               ;;
           *)
               echo "⚠️ Unknown parameter: $1"
               echo "Usage: /emergency-recovery [--mode full|partial|analysis] [--branch <branch>] [--issue <issue>]"
               exit 1
               ;;
       esac
   done
   
   # Validate mode parameter
   if [[ "$mode" != "full" && "$mode" != "partial" && "$mode" != "analysis" ]]; then
       echo "❌ Invalid mode: $mode. Must be 'full', 'partial', or 'analysis'"
       exit 1
   fi
   
   echo "🚨 緊急対応復旧分析を開始します (モード: $mode)"
   ```

2. **Context Preparation and Agent Execution**:
   ```bash
   # 🔄 Prepare context for emergency recovery agent
   echo "🔍 緊急修正分析とコンテキスト準備..."
   
   # Create context file with emergency recovery information
   context_file="/workspace/.claude/context/current-command-context.json"
   current_time=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
   
   # Build context JSON for emergency recovery
   cat > "$context_file" <<EOF
   {
     "command": "emergency-recovery",
     "timestamp": "$current_time",
     "mode": "$mode",
     "branch": "$branch",
     "issue": "$issue",
     "phase": "emergency-recovery-analysis",
     "context": {
       "git_repo": "true",
       "recovery_scope": "$mode",
       "expected_outputs": [
         "emergency-recovery-report.md",
         "recovery-action-plan.md"
       ],
       "analysis_focus": ["git_diff", "document_gaps", "test_coverage", "metadata_sync"]
     },
     "additional_instructions": "緊急修正によって発生したTDD/DDD/レイヤードアーキテクチャプロセスからの乖離を分析し、標準ワークフローへの復旧計画を作成してください。",
     "special_considerations": [
       "Gitコミット履歴の詳細分析",
       "ドキュメント-コード間の整合性チェック", 
       "テストカバレッジギャップの特定",
       "メタデータ同期状態の確認",
       "復旧優先度の設定"
     ],
     "custom_context": {
       "emergency_mode": true,
       "recovery_focus": "high",
       "workflow_restoration": true
     }
   }
   EOF
   
   echo "✅ 緊急復旧コンテキストファイル作成完了: $context_file"
   
   # 🤖 Call the specialized emergency recovery agent
   echo ""
   echo "🚨 緊急対応復旧エージェントを起動します..."
   echo "専門エージェントが緊急修正を分析し復旧計画を作成します"
   echo ""
   ```

3. **Agent Result Verification**:
   ```bash
   # 🔍 Verify emergency recovery analysis results
   echo "🔍 緊急復旧分析結果を検証中..."
   
   # Check that essential analysis files were created
   expected_outputs=(
       "emergency-recovery-report.md"
       "recovery-action-plan.md"
   )
   
   # Validate analysis outputs
   missing_outputs=()
   for output in "${expected_outputs[@]}"; do
       if [[ ! -f "$output" ]]; then
           missing_outputs+=("$output")
       fi
   done
   
   # Report validation results
   if [[ ${#missing_outputs[@]} -gt 0 ]]; then
       echo "❌ 緊急復旧分析検証失敗:"
       echo "  未作成ファイル: ${missing_outputs[*]}"
       exit 1
   fi
   
   echo "✅ 緊急復旧分析結果検証完了"
   
   # Clean up context file after successful execution
   if [[ -f "$context_file" ]]; then
       # Archive context to execution history
       echo "{\"timestamp\":\"$(date -Iseconds)\",\"command\":\"emergency-recovery\",\"mode\":\"$mode\",\"status\":\"completed\"}" >> /workspace/.claude/context/execution-history.jsonl
       rm -f "$context_file"
       echo "📝 コンテキストを実行履歴に記録し、一時ファイルをクリーンアップしました"
   fi
   ```

4. **Display Recovery Summary**:
   ```bash
   # 📊 Display comprehensive recovery analysis summary
   echo ""
   echo "🎉 緊急対応復旧分析完了!"
   echo "================================="
   
   # Show analysis results
   echo "📁 生成されたファイル:"
   if [[ -f "emergency-recovery-report.md" ]]; then
       echo "   ✅ emergency-recovery-report.md (分析レポート)"
   fi
   if [[ -f "recovery-action-plan.md" ]]; then
       echo "   ✅ recovery-action-plan.md (復旧アクションプラン)"
   fi
   
   echo ""
   echo "📋 推奨次のステップ ($mode モード):"
   case $mode in
       "analysis")
           echo "   1. 分析結果の確認: emergency-recovery-report.md"
           echo "   2. フル復旧実行: /emergency-recovery --mode full"
           ;;
       "partial")
           echo "   1. 個別復旧実行: /create-retroactive-issue --issue $issue"
           echo "   2. ドキュメント同期: /sync-documentation $issue"
           ;;
       "full")
           echo "   1. Issue作成: /create-retroactive-issue"
           echo "   2. ドキュメント同期: /sync-documentation --type all"
           echo "   3. テスト作成: /retroactive-test --coverage-target 80"
           echo "   4. 検証実行: /validate-emergency-fix --strict"
           ;;
   esac
   
   echo ""
   echo "📚 重要ドキュメント:"
   echo "   - 分析レポート: emergency-recovery-report.md"
   echo "   - 復旧計画: recovery-action-plan.md"
   echo ""
   echo "✅ 緊急対応復旧分析完了 - 次のアクションを実行してください!"
   ```

## 🔄 **PHASE 3: ENHANCED INTEGRATION CAPABILITIES**

### **Critical Enhancement Features**
This command implements Phase 3 advanced emergency recovery capabilities:

1. **Intelligent Emergency Fix Detection with AI-driven Impact Analysis**
2. **Automated Document-Code Gap Detection and Prioritization** 
3. **Strategic Recovery Planning with Resource Optimization**
4. **Predictive Quality Assessment based on Recovery Plan Execution**

### **Project State Updates**

**CRITICAL**: After successful emergency recovery analysis, MUST update integrated project metadata:

1. **Project State Update**:
   ```bash
   # Update docs/metadata/project-state.json
   # - Add emergency_recovery section with analysis results
   # - Update project_metadata.overall_status to include recovery status
   # - Set technical_debt_metrics based on emergency fix analysis
   # - Add to recent_activity.last_command_executed
   ```

2. **Project Context Update**:
   ```bash
   # Update .claude/context/project-context.json  
   # - Add emergency_recovery_status to current_state
   # - Update documentation_status with gap analysis
   # - Set current_state.last_command and last_command_timestamp
   ```

**⚠️ Error Handling**: If emergency recovery analysis fails:
- 📖 Consult: [Manual Sync Guide](../../docs/maintenance/manual-sync-guide.md)
- 🔄 Check Status: `/use-case-status` for current project state
- 📊 Verify Context: `.claude/context/current-command-context.json`