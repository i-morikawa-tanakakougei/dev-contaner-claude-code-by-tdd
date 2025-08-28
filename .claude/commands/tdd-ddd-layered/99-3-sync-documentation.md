Use the 99-3-sync-documentation subagent to synchronize documentation with emergency code changes. This command MUST USE PROACTIVELY the specialized 99-3-sync-documentation subagent for optimal documentation synchronization.

**📖 Required Reading**: Before execution, this command MUST read the following files:
- `/workspace/.claude/context/current-command-context.json` - Current execution context
- `/workspace/.claude/context/project-context.json` - Overall project state and active sprint information
- `/workspace/docs/metadata/project-state.json` - Integrated project status for update

## Metadata
- **Prerequisites**: GitHub issue created for emergency fix, existing project documentation
- **Input**: 
  - `<issue-number>` (required) - GitHub issue number for the emergency fix
  - `--type <use-case|domain|all>` (default: all) - Type of documentation to sync
- **Output**: 
  - Updated Given-When-Then scenarios
  - Synchronized domain model documentation
  - Reconciled documentation-code alignment
  - Updated project metadata
- **Dependencies**: GitHub issue, existing docs structure, emergency fix commits
- **Execution Timing**: After retroactive issue creation (99-2) and before test creation

## 🎯 **TDD/DDD/LAYERED PROCESS CONTEXT**

**🚨 Emergency Recovery Workflow**: Recovery(99-1) → Issue Creation(99-2) → **Sync Docs(99-3)** → Retroactive Tests(99-4) → Validation(99-5) → Metadata Reconcile(99-6) → Final Review(99-7)

**🏗️ Documentation Sync Architecture**: Analyze→Extract→Generate→Merge  
**📋 Documentation Requirements**: Given-When-Then alignment, domain model consistency, code-doc traceability
**🔄 Integration**: Restores documentation integrity after emergency code changes

> 📖 **Emergency Recovery System**: [99-X Series Commands](./README.md)  
> 🗺️ **Current Position**: Documentation Synchronization (99-3/99-7)  
> 🎯 **Phase Purpose**: Align documentation with emergency code changes  
> ➡️ **Next Stage**: 99-4-retroactive-test (Test Creation)

## 🎯 **PHASE PURPOSE: DOCUMENTATION SYNCHRONIZATION**

**⚠️ Important Notice:**
- **This step is DOCUMENTATION SYNC ONLY** - Update docs to match emergency code changes
- **NO CODE CHANGES** - Focus on bringing documentation in line with implemented functionality  
- **Consistency restoration phase** - Eliminate gaps between documentation and code
- **Update documentation artifacts ONLY** - Maintain Given-When-Then and domain model accuracy

**What this step does:**
1. `99-2-create-retroactive-issue` ← GitHub issue creation for emergency fixes
2. `99-3-sync-documentation` ← **【YOU ARE HERE】Synchronize docs with emergency changes**
3. `99-4-retroactive-test` ← Create tests for emergency changes
4. Then continue with validation and finalization cycle

**SYNCHRONIZE DOCUMENTATION ONLY.**

## Common Errors and Solutions

### ❌ Error Case 1: Issue number not found
**Cause**: Provided GitHub issue doesn't exist or is not accessible  
**Solution**: 
- Verify issue exists: `gh issue view <issue-number>`
- Check if issue is in correct repository
- Ensure GitHub CLI is authenticated: `gh auth status`

### ❌ Error Case 2: No documentation changes needed
**Cause**: Emergency fix didn't impact documented functionality  
**Solution**: 
```bash
# Verify with analysis mode
/sync-documentation <issue> --type all --dry-run
# Or focus on specific area
/sync-documentation <issue> --type use-case
```

### ❌ Error Case 3: Conflicting documentation changes
**Cause**: Multiple emergency fixes created conflicting documentation needs  
**Solution**: 
```bash
# Resolve conflicts manually then sync
git status docs/
# Sync after resolving conflicts
/sync-documentation <issue> --type all --force
```

## Execution Examples

### ✅ Success Example - Full Documentation Sync
```bash
$ /sync-documentation 342 --type all
📚 ドキュメント同期を開始します

🔍 Issue #342 分析中...
  タイトル: "Emergency Fix: Payment validation null pointer exception"
  変更範囲: Payment processing domain
  影響ファイル: src/payment/validator.py

📋 既存ドキュメント状態確認中...
  ❌ use_cases/payment-processing.md - 新しいvalidation logic未反映
  ❌ domain/payment-domain.md - Validator entity更新必要
  ✅ vision/project-vision.md - 変更不要

📝 Given-When-Thenシナリオ更新中...
  📄 use_cases/payment-processing.md 更新:
    + Given: 無効な支払いデータが入力される
    + When: バリデーション処理が実行される  
    + Then: 適切なエラーメッセージが返される（null pointer防止）

🏗️ ドメインモデル更新中...
  📄 domain/payment-domain.md 更新:
    - PaymentValidator entity に null-safe validation追加
    - ValidationRule value object に新しいルール追加

🔄 ドキュメント整合性チェック中...
  ✅ 全Given-When-Thenシナリオ - コード整合性確認
  ✅ ドメインモデル - 実装整合性確認
  ✅ プロジェクトメタデータ - 状況更新完了

🎉 ドキュメント同期完了!
更新されたファイル:
  - docs/use_cases/payment-processing.md
  - docs/domain/payment-domain.md
  - docs/metadata/project-state.json

次のステップ: /retroactive-test 342 --coverage-target 80
```

### ✅ Success Example - Use Case Only Sync
```bash
$ /sync-documentation 343 --type use-case
📚 ユースケースドキュメント同期を開始します

🔍 Issue #343 確認中...
  対象: Database connection timeout hotfix
  同期タイプ: use-case のみ

📋 ユースケースドキュメント分析中...
  📄 use_cases/system-availability.md を更新
    既存シナリオ "システム高負荷時の動作" を拡張:
    
    Given: データベース接続が高負荷状態にある
    When: 接続タイムアウトが発生する
    Then: 適切な再試行とフェイルオーバーが実行される
    And: ユーザーに適切なエラーメッセージが表示される

✅ ユースケース同期完了!
更新: docs/use_cases/system-availability.md

💡 推奨: 完全同期のため /sync-documentation 343 --type all の実行を検討
```

## 📋 **DOCUMENTATION SYNC TASK CHECKLIST**

**Use this checklist for comprehensive documentation synchronization:**

### 🔴 Required Tasks

#### **🔍 Change Impact Analysis**
- [ ] **Issue analysis**: Extract emergency fix details from GitHub issue
- [ ] **Code change review**: Identify modified functionality and business logic
- [ ] **Documentation gap identification**: Find docs that need updates

#### **📝 Given-When-Then Scenario Updates**
- [ ] **Scenario alignment**: Update existing scenarios to match new functionality
- [ ] **New scenario creation**: Add scenarios for new emergency functionality
- [ ] **Scenario validation**: Ensure all scenarios match actual code behavior

#### **🏗️ Domain Model Synchronization**
- [ ] **Entity updates**: Modify domain entities to reflect code changes
- [ ] **Value object alignment**: Update value objects and their validation
- [ ] **Aggregate boundary review**: Verify emergency changes maintain clean boundaries

### 🟡 Recommended Tasks

#### **📊 Cross-Reference Validation**
- [ ] **Traceability maintenance**: Link updated docs to issue and commits
- [ ] **Context preservation**: Maintain connection to overall project vision
- [ ] **Metadata updates**: Update project state and tracking information

#### **🔄 Integration Verification**
- [ ] **Document consistency**: Ensure all updated docs are internally consistent
- [ ] **Style compliance**: Maintain documentation formatting and structure standards
- [ ] **Link validation**: Verify all internal documentation links still work

### 🟢 Optional Tasks

#### **📈 Enhancement Features**
- [ ] **Documentation improvement**: Enhance clarity and completeness beyond minimum sync
- [ ] **Example updates**: Update code examples and usage patterns
- [ ] **Glossary maintenance**: Update ubiquitous language definitions if needed

#### **📊 Quality Assurance**
- [ ] **Peer review preparation**: Prepare documentation changes for review
- [ ] **Version control**: Commit documentation changes with clear messages
- [ ] **Change log update**: Document what was synchronized and why

**💡 Pro Tip**: Focus on high-impact documentation first - scenarios that directly relate to the emergency fix!

## Task Details

**🤖 Agent Integration**: This command MUST USE PROACTIVELY the specialized `99-3-sync-documentation` subagent for optimal documentation synchronization. Claude Code should automatically delegate this task to the 99-3-sync-documentation subagent based on the command description.

## 📖 Subagent Document Reading Instructions

This command delegates to the specialized `99-3-sync-documentation` subagent.

**MANDATORY: The subagent MUST read these files before execution:**

1. `docs/use_cases/` - Current use case scenarios for synchronization
2. `docs/domain/` - Domain model documentation for alignment
3. `docs/vision/project-vision.md` - Project vision for context (if exists)
4. `/workspace/.claude/context/current-command-context.json` - Current execution context
5. `/workspace/docs/metadata/project-state.json` - Project status and documentation state
6. Source code files related to the emergency fix (extracted from issue)

**Command-Specific Reading Focus - Documentation Synchronization:**
- Read GitHub issue details to understand emergency fix scope
- Compare current documentation with implemented code changes
- Review existing Given-When-Then scenarios for alignment needs
- Analyze domain model consistency with new code implementation

**CRITICAL:** Use the Read tool to actually read file contents, not just reference paths.

## サブエージェント実行指示

このコマンドはサブエージェント `99-3-sync-documentation` を呼び出します。

**サブエージェントに対する明示的指示**:
- 実行開始前に以下のファイルを必ず読み込んでください:
  1. GitHub Issue詳細 - 緊急修正の内容確認
  2. 既存ドキュメント (`docs/use_cases/`, `docs/domain/`) - 現状把握
  3. `/workspace/docs/metadata/project-state.json` - プロジェクト状態確認
  4. `/workspace/.claude/context/current-command-context.json` - 実行コンテキスト確認
  
**重要**: リンクや参照だけでなく、実際にRead toolを使用してファイル内容を読み込むこと

Follow these steps:

1. **Pre-execution Validation**:
   ```bash
   # Validate required parameters
   issue_number=""
   sync_type="all"
   dry_run=false
   force_sync=false
   
   # Parse arguments
   if [[ $# -lt 1 ]]; then
       echo "❌ Issue number is required"
       echo "Usage: /sync-documentation <issue-number> [--type use-case|domain|all] [--dry-run] [--force]"
       exit 1
   fi
   
   issue_number="$1"
   shift
   
   while [[ $# -gt 0 ]]; do
       case $1 in
           --type)
               sync_type="$2"
               shift 2
               ;;
           --dry-run)
               dry_run=true
               shift
               ;;
           --force)
               force_sync=true
               shift
               ;;
           *)
               echo "⚠️ Unknown parameter: $1"
               echo "Usage: /sync-documentation <issue-number> [--type use-case|domain|all] [--dry-run] [--force]"
               exit 1
               ;;
       esac
   done
   
   # Validate sync type
   if [[ "$sync_type" != "use-case" && "$sync_type" != "domain" && "$sync_type" != "all" ]]; then
       echo "❌ Invalid sync type: $sync_type. Must be 'use-case', 'domain', or 'all'"
       exit 1
   fi
   
   # Validate GitHub CLI and issue
   if ! command -v gh &> /dev/null; then
       echo "⚠️ GitHub CLI not found. Issue information may be limited."
   else
       if ! gh issue view "$issue_number" >/dev/null 2>&1; then
           echo "❌ GitHub issue #$issue_number not found or not accessible"
           echo "💡 確認: gh issue view $issue_number"
           exit 1
       fi
   fi
   
   echo "📚 ドキュメント同期を開始します (Issue: #$issue_number, Type: $sync_type)"
   ```

2. **Context Preparation and Agent Execution**:
   ```bash
   # 🔄 Prepare context for documentation sync agent
   echo "📋 Issue分析とドキュメント同期コンテキスト準備..."
   
   # Extract issue information if GitHub CLI is available
   issue_title=""
   issue_body=""
   if command -v gh &> /dev/null; then
       issue_title=$(gh issue view "$issue_number" --json title -q '.title' 2>/dev/null || echo "")
       issue_body=$(gh issue view "$issue_number" --json body -q '.body' 2>/dev/null || echo "")
   fi
   
   # Create context file
   context_file="/workspace/.claude/context/current-command-context.json"
   current_time=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
   
   # Build context JSON for documentation synchronization
   cat > "$context_file" <<EOF
   {
     "command": "sync-documentation",
     "timestamp": "$current_time",
     "issue_number": "$issue_number",
     "sync_type": "$sync_type",
     "dry_run": $dry_run,
     "force_sync": $force_sync,
     "phase": "documentation-synchronization",
     "issue_info": {
       "title": "$issue_title",
       "body": "$issue_body"
     },
     "context": {
       "git_repo": "true",
       "docs_structure": "TDD/DDD/Layered",
       "expected_outputs": [
         "updated_use_cases",
         "updated_domain_docs",
         "metadata_updates"
       ],
       "sync_targets": ["use_cases", "domain", "metadata"]
     },
     "additional_instructions": "緊急修正によるコード変更を分析し、対応するドキュメント（Given-When-Thenシナリオ、ドメインモデル）を同期してください。",
     "special_considerations": [
       "Issue内容からのコード変更範囲特定",
       "既存ドキュメントとの整合性確認", 
       "Given-When-Thenシナリオの正確性保証",
       "ドメインモデルの一貫性維持",
       "プロジェクトメタデータの更新"
     ],
     "custom_context": {
       "emergency_recovery": true,
       "documentation_focus": "high",
       "consistency_validation": true
     }
   }
   EOF
   
   echo "✅ ドキュメント同期コンテキストファイル作成完了: $context_file"
   
   # 🤖 Call the specialized documentation sync agent
   echo ""
   echo "📚 ドキュメント同期エージェントを起動します..."
   echo "専門エージェントがIssue内容を分析してドキュメントを同期します"
   echo ""
   
   # Task tool execution with comprehensive prompt
   task_prompt="Execute the task.

## CRITICAL: Subagent Specification Reference
As a fallback mechanism in case the specialized subagent 99-3-sync-documentation is not properly invoked:
- MUST READ: /workspace/.claude/agents/99-3-sync-documentation.md
- Follow the specifications and requirements defined in this agent file
- Implement the exact same process and standards as defined in the subagent specification
- Ensure standardized output format compliance as specified in the agent document

## Context Information Gathering
1. Emergency Recovery Context:
   - Read /workspace/.claude/context/current-command-context.json

2. Documentation Analysis:
   - Read existing use case scenarios in docs/use_cases/
   - Read domain model documentation in docs/domain/
   - Check project vision in docs/vision/ (if exists)

## Task Execution
1. Issue analysis and emergency fix scope identification
2. Documentation gap identification and impact assessment
3. Given-When-Then scenario updates and alignment
4. Domain model synchronization with code changes
5. Cross-reference validation and traceability maintenance
6. Documentation consistency verification and updates

## IMPORTANT: Standardized Output Format Compliance
Report MUST end with the following structured sections:

### 📊 Execution Summary
Mark completion status of each critical task with ✅/❌

### 📋 Overall Assessment
Provide comprehensive documentation synchronization results

### 💡 Next Steps
List specific follow-up actions for emergency recovery workflow

## Post-Processing
- Update Given-When-Then scenarios to match code changes
- Synchronize domain model documentation
- Maintain documentation consistency and style compliance
- Guide next steps in emergency recovery process"

   # Execute with specialized 99-3-sync-documentation subagent
   # The 99-3-sync-documentation subagent will be automatically invoked based on the task description
   
   agent_exit_code=$?
   echo "✅ 専用エージェント実行完了 (終了コード: $agent_exit_code)"
   ```

3. **Agent Result Verification**:
   ```bash
   # 🔍 Verify documentation sync results
   echo "🔍 ドキュメント同期結果を検証中..."
   
   # Check for expected documentation directories
   doc_dirs=("docs/use_cases" "docs/domain" "docs/metadata")
   missing_dirs=()
   
   for dir in "${doc_dirs[@]}"; do
       if [[ ! -d "$dir" ]]; then
           missing_dirs+=("$dir")
       fi
   done
   
   if [[ ${#missing_dirs[@]} -gt 0 ]]; then
       echo "⚠️ 一部のドキュメントディレクトリが見つかりません: ${missing_dirs[*]}"
       echo "💡 プロジェクト構造を確認してください"
   else
       echo "✅ ドキュメント構造確認完了"
   fi
   
   # Check git status for documentation changes
   if git diff --quiet docs/; then
       echo "💡 ドキュメントに変更はありませんでした（既に同期済みの可能性）"
   else
       echo "📝 ドキュメントの変更を検出しました:"
       git diff --name-only docs/ | head -10
   fi
   
   echo "✅ ドキュメント同期結果検証完了"
   
   # Clean up context file after successful execution
   if [[ -f "$context_file" ]]; then
       # Archive context to execution history
       echo "{\"timestamp\":\"$(date -Iseconds)\",\"command\":\"sync-documentation\",\"issue\":\"$issue_number\",\"type\":\"$sync_type\",\"status\":\"completed\"}" >> /workspace/.claude/context/execution-history.jsonl
       rm -f "$context_file"
       echo "📝 コンテキストを実行履歴に記録し、一時ファイルをクリーンアップしました"
   fi
   ```

4. **Display Synchronization Summary**:
   ```bash
   # 📊 Display comprehensive synchronization summary
   echo ""
   echo "🎉 ドキュメント同期完了!"
   echo "========================"
   
   echo "📋 同期情報:"
   echo "   🎫 Issue: #$issue_number"
   if [[ -n "$issue_title" ]]; then
       echo "   📝 タイトル: $issue_title"
   fi
   echo "   🔧 同期タイプ: $sync_type"
   echo "   ⚡ モード: $([ "$dry_run" = true ] && echo "Dry Run" || echo "実行")"
   
   # Show changed files if any
   changed_files=$(git diff --name-only docs/ 2>/dev/null | head -10)
   if [[ -n "$changed_files" ]]; then
       echo ""
       echo "📁 更新されたドキュメント:"
       echo "$changed_files" | while read -r file; do
           echo "   📄 $file"
       done
   else
       echo ""
       echo "📄 ドキュメント: 変更なし（既に同期済み）"
   fi
   
   echo ""
   echo "📋 推奨次のステップ:"
   case $sync_type in
       "use-case")
           echo "   1. ドメインモデル同期: /sync-documentation $issue_number --type domain"
           echo "   2. テスト作成: /retroactive-test $issue_number"
           ;;
       "domain")
           echo "   1. ユースケース同期確認: /sync-documentation $issue_number --type use-case"
           echo "   2. テスト作成: /retroactive-test $issue_number"
           ;;
       "all")
           echo "   1. テスト作成: /retroactive-test $issue_number --coverage-target 80"
           echo "   2. 変更検証: /validate-emergency-fix $issue_number"
           ;;
   esac
   
   echo ""
   echo "💡 補足情報:"
   echo "   - 変更されたドキュメントを手動で確認してください"
   echo "   - 必要に応じて追加の編集を行ってください"
   echo "   - 変更をコミットする前にレビューを実施してください"
   echo ""
   echo "✅ ドキュメント同期完了 - ドキュメントとコードの整合性が回復しました!"
   ```

## 🔄 **PHASE 3: ENHANCED INTEGRATION CAPABILITIES**

### **Critical Enhancement Features**
This command implements Phase 3 advanced documentation synchronization capabilities:

1. **Intelligent Code-Documentation Gap Analysis with AI-driven Impact Assessment**
2. **Automated Given-When-Then Scenario Generation from Code Changes** 
3. **Smart Domain Model Synchronization with Consistency Validation**
4. **Enhanced Documentation Quality Assurance with Cross-Reference Validation**

### **Project State Updates**

**CRITICAL**: After successful documentation synchronization, MUST update integrated project metadata:

1. **Project State Update**:
   ```bash
   # Update docs/metadata/project-state.json
   # - Update documentation_metrics.last_sync_timestamp
   # - Increment documentation_metrics.emergency_sync_count
   # - Set documentation_status.consistency_score
   # - Add to recent_activity.last_command_executed
   ```

2. **Project Context Update**:
   ```bash
   # Update .claude/context/project-context.json  
   # - Update documentation_status with sync results
   # - Set current_state.last_command and last_command_timestamp
   # - Increment workflow_tracking.command_usage.sync_documentation
   ```

**⚠️ Error Handling**: If documentation synchronization fails:
- 📖 Consult: [Manual Sync Guide](../../docs/maintenance/manual-sync-guide.md)
- 🔄 Check Status: `/use-case-status` for current project state  
- 📝 Manual Sync: Update documentation manually and run validation