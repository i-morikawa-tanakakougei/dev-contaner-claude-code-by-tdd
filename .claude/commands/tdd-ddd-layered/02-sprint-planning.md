Use the 02-sprint-planning subagent to plan sprint and create tickets from core scenarios. This command MUST USE PROACTIVELY the specialized 02-sprint-planning subagent for optimal sprint planning implementation.

**📖 Required Reading**: Before execution, this command MUST read the following files:
- `/workspace/.claude/context/current-command-context.json` - Current execution context
- `/workspace/.claude/context/project-context.json` - Overall project state and active sprint information
- `/workspace/docs/vision/project-vision.md` - Project vision and core scenarios for sprint planning
- `/workspace/docs/metadata/project-state.json` - Integrated project status for update

## Metadata
- **Prerequisites**: Project vision and core scenarios (00-create-vision)
- **Input**: Sprint number (required argument)
- **Output**: 
  - `docs/sprints/sprint-X-plan.md` - Sprint planning document
  - `docs/sprints/sprint-X-backlog.md` - Sprint backlog with GitHub issues
  - GitHub Issues created for sprint tickets
  - Updated `docs/use_cases/index.md` with sprint status
- **Dependencies**: GitHub CLI (`gh`), Git configuration
- **Execution Timing**: Called for each sprint cycle (iterative)

## 🎯 **TDD/DDD/LAYERED PROCESS CONTEXT**

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Iterative Sprint Planning (02/16) - Called for each sprint cycle  
> 🎯 **Phase Purpose**: Continuous sprint planning with progress analysis and backlog adjustment  
> ⬅️ **Previous Stage**: 01-init-project-structure (Project Structure)  
> ➡️ **Next Stage**: 03-create-use-case (Use Case Specification)
>
> **📋 3-Layer Architecture Operations**:  
> - 🎯 **Strategic**: `docs/use_cases/core/index.md` (Read core scenarios)  
> - 📊 **Tactical**: `docs/use_cases/index.md` (Create implementation roadmap)  
> - 🔧 **Execution**: `docs/sprints/sprint-X-backlog.md` (Sprint backlog creation)

## 📋 **SPRINT PLANNING TASK CHECKLIST**

**Use this checklist for comprehensive sprint planning:**

### 🔴 Required Tasks

#### **📖 Sprint Analysis**
- [ ] **Analyze current progress**: Review completed issues and velocity
- [ ] **Review core scenarios**: Reference existing core scenarios from vision
- [ ] **Assess team capacity**: Consider team size and sprint duration
- [ ] **Identify dependencies**: Map scenario dependencies and priorities

#### **📝 Sprint Planning**
- [ ] **Select scenarios for sprint**: Choose scenarios based on priority and capacity
- [ ] **Break down scenarios**: Convert scenarios into actionable GitHub issues
- [ ] **Define acceptance criteria**: Ensure clear Given-When-Then criteria for each ticket
- [ ] **Estimate effort**: Add story points or time estimates to tickets

#### **🎫 Ticket Creation**
- [ ] **Create GitHub issues**: Generate issues with proper labels and assignments
- [ ] **Set milestone**: Assign all tickets to sprint milestone
- [ ] **Update sprint backlog**: Document all tickets in sprint backlog
- [ ] **Update project index**: Reflect sprint status in use cases index

### 🟡 Recommended Tasks

#### **📊 Sprint Metrics**
- [ ] **Set sprint goals**: Define clear objectives for the sprint
- [ ] **Plan sprint review**: Schedule demo and retrospective
- [ ] **Track velocity**: Calculate and record team velocity
- [ ] **Risk assessment**: Identify potential blockers and mitigation

#### **🔄 Process Optimization**
- [ ] **Review previous sprint**: Learn from previous sprint outcomes
- [ ] **Adjust process**: Fine-tune planning process based on learnings
- [ ] **Team alignment**: Ensure team understanding of sprint goals
- [ ] **Stakeholder communication**: Inform stakeholders of sprint plan

## Task Details

**🤖 Agent Integration**: This command MUST USE PROACTIVELY the specialized `02-sprint-planning` subagent for optimal sprint planning implementation. Claude Code should automatically delegate this task to the 02-sprint-planning subagent based on the command description.

## 📖 Subagent Document Reading Instructions

This command delegates to the specialized `02-sprint-planning` subagent.

**MANDATORY: The subagent MUST read these files before execution:**

1. `docs/index.md` - Project overview and current status
2. `.claude/context/project-context.json` - Current project context
3. `/workspace/.claude/context/current-command-context.json` - Current execution context
4. `docs/vision/project-vision.md` - Project vision and objectives
5. `docs/use_cases/core/index.md` - Core scenarios for sprint planning
6. `docs/use_cases/index.md` - Current implementation status
7. Any existing `docs/sprints/` folder contents - Previous sprint results and learnings
8. GitHub Issues (via `gh issue list`) - Current issue status and backlog

**Command-Specific Reading Focus - Sprint Planning:**
- Review core scenarios to prioritize features for the sprint
- Check project vision for business priorities and constraints
- Analyze previous sprint results to understand team velocity
- Review current implementation status to understand what's completed
- Examine GitHub issues to understand current backlog and dependencies

**CRITICAL:** Use the Read tool to actually read file contents, not just reference paths.

1. **Pre-execution Validation**:
   ```bash
   # Validate sprint number requirement
   if [[ $# -eq 0 ]]; then
       echo "エラー: スプリント番号を指定してください"
       echo "使用例: /sprint-planning 1"
       echo "使用例: /sprint-planning 2"
       exit 1
   fi
   
   # Extract sprint number
   sprint_number="$1"
   if [[ ! "$sprint_number" =~ ^[0-9]+$ ]]; then
       echo "エラー: スプリント番号は正の整数で指定してください"
       exit 1
   fi
   
   # Check for vision document
   if [[ ! -f "docs/vision/project-vision.md" ]]; then
       echo "❌ エラー: プロジェクトビジョンが見つかりません"
       echo "💡 先に /create-vision を実行してください"
       exit 1
   fi
   
   echo "📋 スプリント $sprint_number の計画を開始します"
   ```

2. **Context Preparation and Agent Execution**:
   ```bash
   # 🔄 Prepare context for agent (Pattern B: Hybrid approach)
   echo "📋 コンテキスト準備とエージェント起動..."
   
   # Create context file with sprint planning information
   context_file="/workspace/.claude/context/current-command-context.json"
   current_time=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
   
   # Build context JSON for sprint planning
   cat > "$context_file" <<EOF
   {
     "command": "sprint-planning",
     "timestamp": "$current_time",
     "sprint_number": $sprint_number,
     "phase": "sprint-planning",
     "context": {
       "github_cli_available": $(command -v gh >/dev/null 2>&1 && echo "true" || echo "false"),
       "git_repo": $(git rev-parse --is-inside-work-tree 2>/dev/null && echo "true" || echo "false"),
       "expected_outputs": [
         "docs/sprints/sprint-$sprint_number.md",
         "docs/sprints/sprint-$sprint_number-backlog.md"
       ],
       "architecture_patterns": ["TDD", "DDD", "Layered Architecture"]
     },
     "additional_instructions": "スプリント $sprint_number の計画を作成してください。コアシナリオを分析し、適切なチケット分割とGitHub Issue作成を行ってください。Given-When-Then形式の受け入れ条件を各チケットに含めてください。",
     "special_considerations": [
       "既存のコアシナリオ（docs/use_cases/core/）との整合性確認",
       "スプリント容量とチーム能力の適切な見積もり",
       "チケット間の依存関係の明確化",
       "GitHub Issueの品質確保（ラベル、マイルストーン設定）"
     ],
     "custom_context": {
       "capacity_planning": true,
       "github_integration": true,
       "milestone_management": true,
       "sprint_goal_definition": true
     }
   }
   EOF
   
   echo "✅ コンテキストファイル作成完了: $context_file"
   
   # 🤖 Call the specialized agent with hybrid context
   echo ""
   echo "📋 スプリント計画エージェントを起動します..."
   echo "専門エージェントがスプリント $sprint_number の計画とチケット作成を行います"
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
[02-sprint-planning固有のタスクを実行]

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

   # Execute with specialized 02-sprint-planning subagent
   # The 02-sprint-planning subagent will be automatically invoked based on the task description
   
   agent_exit_code=$?
   echo "✅ 専用エージェント実行完了 (終了コード: $agent_exit_code)"
   
   echo "✅ エージェント呼び出し設定完了"
   echo "エージェントが以下の処理を実行します:"
   echo "  - コンテキストファイルからのスプリント情報取得"
   echo "  - コアシナリオの分析と優先度付け"
   echo "  - スプリント容量の見積もりとチケット選択"
   echo "  - GitHub Issueの作成とマイルストーン設定"
   echo "  - スプリントバックログとドキュメントの生成"
   echo "  - プロジェクト進捗管理の更新"
   ```

3. **Agent Result Verification**:
   ```bash
   # 🔍 Verify agent execution results
   echo "🔍 エージェント実行結果を検証中..."
   
   # Check that sprint documents were created
   echo "  🔍 スプリント文書の作成確認中..."
   
   # Check for sprint directory and files
   sprint_files=(
       "docs/sprints/sprint-${sprint_number}-plan.md"
       "docs/sprints/sprint-${sprint_number}-backlog.md"
   )
   
   missing_sprint_files=()
   for file in "${sprint_files[@]}"; do
       if [[ ! -f "$file" ]]; then
           missing_sprint_files+=("$file")
       fi
   done
   
   # Check for GitHub issues (if gh is available)
   issues_created=false
   if command -v gh >/dev/null 2>&1; then
       # Check if issues were created for this sprint
       if gh issue list --milestone "Sprint $sprint_number" --limit 1 >/dev/null 2>&1; then
           issues_created=true
           echo "    ✅ GitHub Issues が作成されました"
       else
           echo "    ⚠️ GitHub Issues が見つかりません"
       fi
   else
       echo "    ⚠️ GitHub CLI が見つかりません"
   fi
   
   # Check if use cases index was updated
   use_cases_updated=false
   if [[ -f "docs/use_cases/index.md" ]] && grep -q "Sprint $sprint_number" "docs/use_cases/index.md"; then
       use_cases_updated=true
       echo "    ✅ ユースケースインデックスが更新されました"
   fi
   
   # Report validation results
   if [[ ${#missing_sprint_files[@]} -gt 0 ]]; then
       echo "❌ エージェント実行検証失敗:"
       echo "  未作成スプリント文書: ${missing_sprint_files[*]}"
       exit 1
   fi
   
   echo "✅ エージェント実行結果検証完了"
   
   # 🔧 Load advanced task verification library
   source "$(dirname "${BASH_SOURCE[0]}")/_task_verification.sh"
   
   # ✨ New: Advanced task verification with retry capability
   echo "🔍 Critical tasks確認中..."
   if ! verify_critical_tasks "02-sprint-planning" "$latest_report"; then
       echo "⚠️ Critical tasks確認で問題が検出されました - 再実行を試行します"
       prepare_retry_context "02-sprint-planning" "1" "${verification_issues[@]}"
       
       # Enhanced context for retry
       echo "🔄 再実行用の強化コンテキスト準備中..."
       prepare_enhanced_context "02-sprint-planning" "$context_file" "${verification_issues[@]}"
       
       echo "💡 推奨アクション: エージェントを再実行してください"
       echo "   重点項目: $(IFS='|'; echo "${verification_issues[*]}")"
       exit 1
   fi
   
   echo "✅ Critical tasks確認完了 - 全項目クリア"
   
   # Clean up context file after successful execution
   if [[ -f "$context_file" ]]; then
       # Archive context to execution history
       echo "{\"timestamp\":\"$(date -Iseconds)\",\"command\":\"sprint-planning\",\"sprint_number\":$sprint_number,\"status\":\"completed\"}" >> /workspace/.claude/context/execution-history.jsonl
       rm -f "$context_file"
       echo "📝 コンテキストを実行履歴に記録し、一時ファイルをクリーンアップしました"
   fi
   ```

4. **Display Sprint Planning Success Summary**:
   ```bash
   # 📊 Display comprehensive sprint planning summary
   echo ""
   echo "🎉 スプリント $sprint_number 計画完了!"
   echo "============================================="
   
   # Show created sprint files
   echo "📁 作成されたスプリント文書:"
   for file in "${sprint_files[@]}"; do
       if [[ -f "$file" ]]; then
           echo "   ✅ $file"
       fi
   done
   
   # Show GitHub integration status
   echo ""
   echo "🎫 GitHub Issues統合:"
   if [[ "$issues_created" == true ]]; then
       echo "   ✅ Issues作成: 完了"
       if command -v gh >/dev/null 2>&1; then
           issue_count=$(gh issue list --milestone "Sprint $sprint_number" --limit 100 | wc -l)
           echo "   📊 作成Issues: $issue_count 個"
       fi
   else
       echo "   ⚠️ Issues作成: 未確認"
   fi
   
   # Show next steps
   echo ""
   echo "📋 次のステップ (各Issue実装):"
   echo "   1. 各Issueに対して /create-use-case <issue-number>"
   echo "   2. ドメインモデリング: /domain-modeling <issue-number>"
   echo "   3. TDD開発サイクル開始"
   
   echo ""
   echo "📚 重要ドキュメント:"
   echo "   - スプリント計画: docs/sprints/sprint-${sprint_number}-plan.md"
   echo "   - スプリントバックログ: docs/sprints/sprint-${sprint_number}-backlog.md"
   echo "   - プロジェクト進捗: docs/use_cases/index.md"
   
   echo ""
   echo "🔗 GitHub連携:"
   if command -v gh >/dev/null 2>&1; then
       echo "   - Milestone: Sprint $sprint_number"
       echo "   - Issues確認: gh issue list --milestone 'Sprint $sprint_number'"
   else
       echo "   - GitHub CLI未導入（手動でIssue確認）"
   fi
   
   echo ""
   echo "✅ スプリント計画完了 - 開発開始準備完了!"
   ```

## Common Errors and Solutions

### ❌ Error Case 1: No core scenarios found
**Cause**: `docs/use_cases/core/index.md` file doesn't exist or is empty  
**Solution**: 
- Run `/create-vision` command first to establish project vision
- Ensure core scenarios are properly formatted with numbered scenarios

### ❌ Error Case 2: GitHub CLI not configured
**Cause**: `gh` command not authenticated or repository not linked  
**Solution**: 
```bash
gh auth login
gh repo set-default <your-repo>
```

### ❌ Error Case 3: Sprint directory not accessible
**Cause**: No write permissions for `docs/sprints/` directory  
**Solution**: Check directory permissions and create if necessary

## Execution Examples

### ✅ Success Example
```bash
$ /sprint-planning 1
📋 スプリント 1 の計画を開始します
📋 スプリント計画エージェントを起動します...
✅ エージェント実行結果検証完了
🎉 スプリント 1 計画完了!
```

### ❌ Failure Example and Fix
```bash
$ /sprint-planning 1
❌ エラー: プロジェクトビジョンが見つかりません

# Fix: Create vision first
$ /create-vision
$ /sprint-planning 1
```

## 🔄 Metadata Update Requirements

**CRITICAL**: After successful sprint planning completion, you MUST update the following files:

1. **Project State Update**:
   ```bash
   # Update docs/metadata/project-state.json
   # - Update sprint_summary.current_sprint to new sprint number
   # - Set sprint_summary.total_issues to created issues count
   # - Update recent_activity.last_command_executed
   # - Update workflow_statistics.command_execution_stats
   ```

2. **Project Context Update**:
   ```bash
   # Update .claude/context/project-context.json  
   # - Update current_state.active_sprint to new sprint number
   # - Update sprint_management.active_sprint_number
   # - Set sprint dates and goal
   # - Increment workflow_tracking.command_usage.sprint_planning
   ```

3. **Sprint Documentation**:
   ```bash
   # Create/Update sprint-specific files
   # - docs/sprints/sprint-X-plan.md (sprint planning document)
   # - docs/sprints/sprint-X-backlog.md (sprint backlog with GitHub issues)
   # - Update docs/use_cases/index.md with sprint status
   ```

**⚠️ Error Handling**: If standard workflow is disrupted:
- 📖 Consult: [Manual Sync Guide](../../docs/maintenance/manual-sync-guide.md)
- 🔄 Check Status: `/use-case-status` for current project state
- 📊 Verify Context: `.claude/context/current-command-context.json`