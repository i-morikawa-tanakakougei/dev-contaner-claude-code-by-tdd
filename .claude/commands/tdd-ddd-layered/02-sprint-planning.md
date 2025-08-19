Plan sprint and create tickets from core scenarios.

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

**🤖 Agent Integration**: This command uses the specialized `02-sprint-planning` agent for optimal sprint planning implementation.

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

2. **Execute Sprint Planning Agent**:
   ```bash
   # 🤖 Delegate to specialized sprint planning agent
   echo "📋 スプリント計画エージェントを起動します..."
   echo "専門エージェントがスプリント計画とチケット作成を行います"
   echo ""
   
   # Call the specialized agent using Claude Code's Task tool
   # The agent will handle:
   # - Core scenario analysis
   # - Sprint capacity planning
   # - Ticket breakdown and creation
   # - GitHub issue generation
   # - Sprint backlog documentation
   # - Milestone and label management
   # - Progress tracking setup
   
   # Note: In actual implementation, this would be handled by the Claude Code system
   # when the /sprint-planning command is executed. The agent integration happens
   # automatically through the Task tool with subagent_type="02-sprint-planning"
   
   echo "✅ スプリント計画エージェント呼び出し完了"
   echo "エージェントが以下の処理を実行しました:"
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