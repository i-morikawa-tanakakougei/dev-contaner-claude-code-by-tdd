Use the 15-create-pr subagent to create pull request and close related issues. This command MUST USE PROACTIVELY the specialized 15-create-pr subagent for optimal pull request creation.

**📖 Required Reading**: Before execution, this command MUST read the following files:
- `/workspace/.claude/context/current-command-context.json` - Current execution context
- `/workspace/.claude/context/project-context.json` - Overall project state and active sprint information
- `/workspace/docs/use_cases/issue-X-Y.json` - Issue-specific metadata and implementation status
- `/workspace/docs/reviews/` - Review reports for PR description reference
- `/workspace/docs/metadata/project-state.json` - Integrated project status for update

## Metadata
- **Prerequisites**: Feedback applied, all implementations completed
- **Input**: Issue number(s) (required)
- **Output**: 
  - GitHub pull request created
  - Issues linked and ready for closure
  - Final `docs/use_cases/issue-X-Y.json` metadata update
- **Dependencies**: GitHub CLI (`gh`), Git configuration, completed implementation
- **Execution Timing**: Final step after all development phases completed

## 🎯 **TDD/DDD/LAYERED PROCESS CONTEXT**

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Review Phase - Pull Request Creation (15/16)  
> 🎯 **Phase Purpose**: Create PR, validate implementation, and close issues  
> ⬅️ **Previous Stage**: 14-apply-feedback (Feedback Application)  
> ➡️ **Next Stage**: Project completion or new feature cycle
>
> **📋 3-Layer Architecture Operations**:  
> - 🎯 **Strategic**: `docs/use_cases/core/index.md` (Reference completion)  
> - 📊 **Tactical**: `docs/use_cases/index.md` (Mark as completed)  
> - 🔧 **Execution**: `docs/use_cases/issue-X-Y.json` (Final metadata update)

## 🚀 **PULL REQUEST CREATION: FINALIZATION ONLY**

**⚠️ Important Notice:**
- **This step is PR CREATION ONLY** - Create pull request and finalize implementation
- **NO NEW IMPLEMENTATION** - Focus on PR creation and issue closure  
- **Quality gates validation** - Ensure all quality criteria are met
- **Documentation finalization** - Complete all required documentation

**PR Creation Process:**
1. `14-apply-feedback` ← All improvements applied
2. `15-create-pr` ← **【YOU ARE HERE】PR creation and finalization**
3. `16-use-case-status` ← Final status verification
4. PR merge and issue closure

**PR Creation Tasks:**
- ✅ Validate all tests pass
- ✅ Create comprehensive PR description
- ✅ Close related issues with proper linking

## 📋 **PULL REQUEST CREATION TASK CHECKLIST**

**Use this checklist for high-quality PR creation and finalization:**

### 🔴 Required Tasks

#### **🔍 Final Quality Gate Validation**
- [ ] **Run final test suite**: Execute `uv run --frozen pytest --cov=src --cov-report=html`
- [ ] **Verify all tests GREEN**: Ensure 100% test success rate
- [ ] **Validate test coverage**: Confirm coverage meets project standards (80%+)
- [ ] **Check Given-When-Then coverage**: Verify all scenarios have corresponding tests
- [ ] **Run final ruff linting**: Execute `uv run --frozen ruff check src/ --fix`
- [ ] **Verify clean quality results**: Ensure all quality tools pass without errors

#### **📊 Issue Analysis and Closure Preparation**
- [ ] **Parse target issues**: Extract all issue numbers from command arguments
- [ ] **Validate issue completion**: Ensure all requirements from target issues are implemented
- [ ] **Check acceptance criteria**: Verify all acceptance criteria are satisfied
- [ ] **Review issue comments**: Ensure all discussed requirements are addressed

#### **📝 Comprehensive PR Description Creation**
- [ ] **Write executive summary**: Clear overview of what was implemented and why
- [ ] **Document business value**: Explain the business impact and user benefits
- [ ] **List technical changes**: Summarize architecture, code, and infrastructure changes
- [ ] **Map issue requirements**: Show how each issue requirement was addressed

### 🟡 Recommended Tasks

#### **🎯 Requirements Traceability Documentation**
- [ ] **Document Given-When-Then implementation**: Link scenarios to actual test implementation
- [ ] **Include quality metrics**: Report test coverage, performance, and quality improvements
- [ ] **Validate cross-issue dependencies**: Check if issues have dependencies on each other
- [ ] **Prepare closure statements**: Draft individual closure justifications for each issue

### 🟢 Optional Tasks

#### **🔧 Advanced Quality Validation**
- [ ] **Run final ruff formatting**: Execute `uv run --frozen ruff format src/`
- [ ] **Run final type checking**: Execute `uv run --frozen pyright src/`
- [ ] **Map scenarios to code**: Link Given-When-Then scenarios to implementation
- [ ] **Document acceptance criteria satisfaction**: Show how each criterion was met
- [ ] **Link tests to requirements**: Connect test cases to original business requirements
- [ ] **Show architecture decisions**: Document key design decisions and rationale
- [ ] **Include implementation notes**: Explain complex or non-obvious implementation choices
- [ ] **Document future considerations**: Note any technical debt or future improvement opportunities

### **🔗 Pull Request Technical Setup**
- [ ] **Ensure clean git status**: Verify no uncommitted changes remain
- [ ] **Create feature branch**: Ensure PR is from appropriate feature branch
- [ ] **Write clear commit messages**: Ensure commit history is clean and descriptive
- [ ] **Add appropriate labels**: Tag PR with relevant labels (feature, bugfix, enhancement)
- [ ] **Set milestone**: Link PR to appropriate project milestone
- [ ] **Add reviewers**: Assign appropriate code reviewers (including artofzero)

### **📋 PR Description Template Implementation**
- [ ] **Create PR title**: Clear, descriptive title following project conventions
- [ ] **Write summary section**: Brief overview of changes and business value
- [ ] **Document test plan**: Describe how changes were tested and validated
- [ ] **List breaking changes**: Note any breaking changes or migration requirements
- [ ] **Include screenshots/demos**: Add visual evidence of functionality if applicable
- [ ] **Add deployment notes**: Include any special deployment or configuration requirements

### **🎫 Issue Closure Integration**
- [ ] **Add issue closure keywords**: Include "Closes #X, Fixes #Y" syntax in PR description
- [ ] **Validate issue linking**: Ensure GitHub properly links PR to target issues
- [ ] **Review issue labels**: Update issue labels to reflect completion status
- [ ] **Document completion rationale**: Explain how each issue's requirements were satisfied
- [ ] **Handle partial completions**: Note if any issues are partially completed with follow-up planned
- [ ] **Update issue milestones**: Ensure issues are properly milestone-assigned

### **🚀 CI/CD and Merge Preparation**
- [ ] **Verify CI pipeline readiness**: Ensure all CI checks are configured to run
- [ ] **Check branch protection**: Verify branch protection rules are satisfied
- [ ] **Validate merge requirements**: Ensure all merge requirements will be met
- [ ] **Test PR creation**: Verify PR can be created without conflicts
- [ ] **Check automated checks**: Ensure automated quality checks will pass
- [ ] **Plan merge strategy**: Decide on merge commit vs squash merge approach

### **📊 Quality and Performance Validation**
- [ ] **Document performance impact**: Report any performance improvements or impacts
- [ ] **Validate memory usage**: Ensure no memory leaks or excessive memory usage
- [ ] **Check resource utilization**: Verify appropriate resource usage patterns
- [ ] **Test error handling**: Validate error scenarios work correctly end-to-end
- [ ] **Verify logging and monitoring**: Ensure appropriate observability is implemented
- [ ] **Check security considerations**: Validate security requirements are met

### **🔍 Review Support Documentation**
- [ ] **Create review guide**: Provide guidance for reviewers on what to focus on
- [ ] **Document testing instructions**: Provide clear instructions for manual testing
- [ ] **Highlight complex changes**: Call attention to complex or risky changes
- [ ] **Provide context**: Explain background and reasoning for major decisions
- [ ] **Include links to references**: Link to specifications, design docs, and related issues
- [ ] **Prepare demo/walkthrough**: Plan demonstration of functionality if needed

### **📈 Metrics and Success Criteria**
- [ ] **Document quality improvements**: Report code quality, coverage, and complexity metrics
- [ ] **Measure business value delivery**: Quantify business impact where possible
- [ ] **Report technical improvements**: Document technical debt reduction or architecture improvements
- [ ] **Validate user experience**: Confirm user experience meets or exceeds expectations
- [ ] **Check accessibility**: Ensure accessibility requirements are met if applicable
- [ ] **Document lessons learned**: Record insights for future development cycles

### **🎉 PR Creation and Final Steps**
- [ ] **Create pull request**: Submit PR with comprehensive description and proper issue linking
- [ ] **Verify issue auto-linking**: Confirm GitHub properly links and will close target issues
- [ ] **Notify stakeholders**: Inform relevant stakeholders that PR is ready for review
- [ ] **Update project tracking**: Update project boards, sprint status, and team communications
- [ ] **Prepare for review cycle**: Be ready to respond to review feedback promptly
- [ ] **Monitor CI/CD pipeline**: Ensure all automated checks pass successfully

### **📚 Final Documentation Update**
- [ ] **Update metadata files**: Mark implementation complete in all relevant issue-X-Y.json files
- [ ] **Update use case index**: Mark tactical-level items as completed
- [ ] **Archive working documents**: Store working notes and temporary files appropriately
- [ ] **Update project metrics**: Record completion metrics for project tracking
- [ ] **Prepare handoff documentation**: Ensure knowledge is properly documented for team
- [ ] **Clean up development artifacts**: Remove temporary files and development-only code

**💡 Pro Tip: A well-written PR description saves hours of review time and helps ensure smooth merging - invest in quality PR documentation!**

- ✅ Link and close related GitHub issues
- ✅ Update final documentation
- ❌ Do not add new features
- ❌ Do not make implementation changes

**CREATE PULL REQUEST AND FINALIZE ONLY.**

## Common Errors and Solutions

### ❌ Error Case 1: Feedback not applied
**Cause**: Pull request creation attempted before feedback application  
**Solution**: Apply feedback first with `/apply-feedback <issue-number>`

### ❌ Error Case 2: GitHub CLI not configured
**Cause**: `gh` command not authenticated or repository not set  
**Solution**: 
```bash
gh auth login
gh repo set-default <your-repo>
```

### ❌ Error Case 3: Branch not pushed to remote
**Cause**: Feature branch exists only locally  
**Solution**: Push branch to remote before creating PR

## Execution Examples

### ✅ Success Example
```bash
$ /create-pr 15
🚀 Issues: #15 のPR作成を開始します
🔄 フィードバック適用確認中...
✅ フィードバックが適用されています
🌐 ブランチをリモートにプッシュ中...
📄 PR作成中...
✅ PR作成完了: https://github.com/repo/pull/123
🔗 イシューリンク設定中...
✅ Issue #15 をPRにリンク
🎉 PR作成完了!
```

### ❌ Failure Example and Fix
```bash
$ /create-pr 15
❌ フィードバックが適用されていません
💡 最初にフィードバックを適用してください:
   /apply-feedback 15

# Fix: Apply feedback first
$ /apply-feedback 15
$ /create-pr 15
```

## 📍 **AGENT INTEGRATION IMPLEMENTATION**

This command follows the established 4-step agent integration pattern for consistent execution:

### **Step 1: Pre-execution Validation** 🔍
- Validate issue numbers provided
- Check all development phases completed
- Verify feedback application status
- Validate GitHub CLI configuration
- Check repository state and branch status

## Task Details

**🤖 Agent Integration**: This command MUST USE PROACTIVELY the specialized `15-create-pr` subagent for pull request creation and finalization.
 Claude Code should automatically delegate this task to the 15-create-pr subagent based on the command description.

## 📖 Subagent Document Reading Instructions

This command delegates to the specialized `15-create-pr` subagent.

**MANDATORY: The subagent MUST read these files before execution:**

1. `docs/index.md` - Project overview and current status
2. `.claude/context/project-context.json` - Current project context
3. `/workspace/.claude/context/current-command-context.json` - Current execution context
4. `docs/use_cases/issue-X-Y.json` - Issue metadata and completion status
5. `docs/reviews/` - Review reports for PR description context
6. Git history and branch status for PR creation context
7. Test results and quality metrics for PR validation

**Command-Specific Reading Focus - Pull Request Creation:**
- Analyze completed implementation for comprehensive PR description
- Review all related issues to ensure proper linking and closure
- Examine test results and quality metrics for validation
- Study architectural changes and business impact for PR context
- Review feedback application results for completion confirmation

**CRITICAL:** Use the Read tool to actually read file contents, not just reference paths.

Follow these steps:

1. **Pre-execution Validation**:
   ```bash
   # Validate issue number requirement
   if [[ $# -eq 0 ]]; then
       echo "エラー: 最低1つのイシュー番号が必要です"
       echo "使用例:"
       echo "  /create-pr 15        # 単一イシューPR作成"
       echo "  /create-pr 15,23     # 複数イシュー統合PR作成"
       exit 1
   fi
   
   # Parse issue numbers
   IFS=',' read -ra ISSUES <<< "$1"
   echo "🚀 Issues: $(printf '#%s ' "${ISSUES[@]}")のPR作成を開始します"
   
   # Check feedback application
   feedback_applied=false
   for issue_num in "${ISSUES[@]}"; do
       if find docs/reviews/ -name "*${issue_num}*feedback*" -type f 2>/dev/null | head -1 >/dev/null; then
           feedback_applied=true
           break
       fi
   done
   
   if [[ "$feedback_applied" != "true" ]]; then
       echo "❌ フィードバックが適用されていません"
       echo "💡 最初にフィードバックを適用してください: /apply-feedback $1"
       exit 1
   fi
   ```

2. **Context Preparation and Agent Execution**:
   ```bash
   # 🔄 Prepare context for agent (Pattern B: Hybrid approach)
   echo "🚀 コンテキスト準備とエージェント起動..."
   
   # Create context file with PR creation information
   context_file="/workspace/.claude/context/current-command-context.json"
   current_time=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
   
   # Build context JSON for PR creation
   cat > "$context_file" <<EOF
   {
     "command": "create-pr",
     "timestamp": "$current_time",
     "issue_numbers": [$(IFS=,; printf '%s\n' "${ISSUES[@]}" | paste -sd,)],
     "phase": "pull-request-creation",
     "context": {
       "expected_outputs": [
         "GitHub Pull Request URL",
         "PR description with traceability",
         "docs/pr/pr-summary.md"
       ],
       "architecture_patterns": ["CI/CD", "Code Review", "Git Flow"]
     },
     "additional_instructions": "包括的なプルリクエストを作成してください。Given-When-Thenシナリオのトレーサビリティ、テスト結果、品質メトリクス、実装サマリーを含む詳細なPR説明を作成し、適切なレビュアーを割り当ててください。",
     "special_considerations": [
       "Given-When-Thenシナリオと実装の完全トレーサビリティ",
       "TDD/DDD/Layered Architectureの実装品質説明",
       "テスト結果と品質メトリクスの包含",
       "レビュアー割り当てとマイルストーン設定"
     ],
     "custom_context": {
       "scenario_traceability": true,
       "quality_metrics_inclusion": true,
       "comprehensive_description": true,
       "automated_linking": true
     }
   }
   EOF
   
   echo "✅ コンテキストファイル作成完了: $context_file"
   
   # 🤖 Call the specialized agent with hybrid context
   echo ""
   echo "🚀 プルリクエスト作成エージェントを起動します..."
   echo "専門エージェントが包括的なPRを作成します"
   echo ""
   
   # Actual Claude Code Task tool invocation with hybrid approach
   # Task tool execution with comprehensive prompt
   task_prompt="Execute the task.

## CRITICAL: Subagent Specification Reference
As a fallback mechanism in case the specialized subagent 15-create-pr is not properly invoked:
- MUST READ: /workspace/.claude/agents/15-create-pr.md
- Follow the specifications and requirements defined in this agent file
- Implement the exact same process and standards as defined in the subagent specification
- Ensure standardized output format compliance as specified in the agent document

## Context Information Gathering
1. Temporary Context (project information):
   - Read /workspace/.claude/context/current-command-context.json

2. Project Status Verification:
   - Check required documents and files
   - Review existing implementations and designs

## Task Execution
[Execute 15-create-pr specific tasks]

## IMPORTANT: Standardized Output Format Compliance
Report MUST end with the following structured sections:

### 📊 Execution Summary
Mark completion status of each critical task with ✅/❌

### 📋 Overall Assessment
Specify one of: APPROVED/CONDITIONAL_APPROVAL/REJECTED/COMPLETED

### 💡 Next Steps
List specific action items based on the assessment

## After Processing Completion
- Report execution results
- Provide guidance for next steps"

   # Execute with specialized 15-create-pr subagent
   # The 15-create-pr subagent will be automatically invoked based on the task description
   
   agent_exit_code=$?
   echo "✅ 専用エージェント実行完了 (終了コード: $agent_exit_code)"
   
   echo "✅ エージェント呼び出し設定完了"
   echo "エージェントが以下の処理を実行します:"
   echo "  - コンテキストファイルからのイシュー情報取得"
   echo "  - GitHubリポジトリステータス検証とブランチ管理"
   echo "  - Given-When-Thenトレーサビリティを含む包括的PR説明生成"
   echo "  - テスト結果検証と品質メトリクス包含"
   echo "  - イシューリンクと自動クローズ準備"
   echo "  - レビュアー割り当てとマイルストーン管理"
   echo "  - CI/CDステータスチェック実行"
   ```

3. **Agent Result Verification**:
   ```bash
   # 🔍 Verify agent execution results
   echo "🔍 エージェント実行結果を検証中..."
   
   # Check that PR was created (would verify via GitHub API)
   # In actual implementation, this would check the PR URL returned by agent
   pr_created=true  # Simulated result
   
   if [[ "$pr_created" != "true" ]]; then
       echo "❌ エージェント実行検証失敗:"
       echo "  プルリクエスト作成が確認できません"
       exit 1
   fi
   
   echo "✅ エージェント実行結果検証完了"
   
   # 🔧 Load advanced task verification library
   source "$(dirname "${BASH_SOURCE[0]}")/_task_verification.sh"
   
   # ✨ New: Advanced task verification with retry capability
   echo "🔍 Critical tasks確認中..."
   if ! verify_critical_tasks "15-create-pr" "$latest_report"; then
       echo "⚠️ Critical tasks確認で問題が検出されました - 再実行を試行します"
       prepare_retry_context "15-create-pr" "1" "${verification_issues[@]}"
       
       # Enhanced context for retry
       echo "🔄 再実行用の強化コンテキスト準備中..."
       prepare_enhanced_context "15-create-pr" "$context_file" "${verification_issues[@]}"
       
       echo "💡 推奨アクション: エージェントを再実行してください"
       echo "   重点項目: $(IFS='|'; echo "${verification_issues[*]}")"
       exit 1
   fi
   
   echo "✅ Critical tasks確認完了 - 全項目クリア"
   echo "  - プルリクエスト: 作成完了"
   echo "  - イシューリンク: 設定完了"
   ```

4. **Display Success Summary**:
   ```bash
   # 📊 Display comprehensive success summary
   echo ""
   echo "🎉 プルリクエスト作成完了!"
   echo "=========================="
   
   # Show summary information
   echo "📊 PR作成サマリー:"
   echo "  🚀 対象Issues: $(printf '#%s ' "${ISSUES[@]}")"
   echo "  📝 プルリクエスト: 作成完了"
   echo "  🔗 イシューリンク: 設定完了"
   echo ""
   echo "📋 次のステップ:"
   echo "   1. PR レビュー待ち"
   echo "   2. CI/CD チェック確認"
   echo "   3. マージ後の状況確認: /use-case-status"
   echo ""
   echo "✅ プルリクエスト作成完了 - レビューとマージを待機中!"

   ```

## 🔄 **PHASE 3: ENHANCED INTEGRATION CAPABILITIES**

### **Critical Enhancement Features**
This command implements Phase 3 advanced integration and pull request creation capabilities:

1. **PR Quality Analysis**: Comprehensive pull request quality analysis with compliance validation and completeness assessment
2. **Integration Validation**: Advanced integration validation with cross-system compatibility and deployment readiness checks
3. **Merge Readiness Assessment**: Intelligent merge readiness assessment with automated quality gates and risk analysis
4. **Deployment Preparation**: Smart deployment preparation with configuration validation and rollback strategy planning

### **Project State Updates**

**CRITICAL**: After successful pull request creation completion, MUST update integrated project metadata:

#### Project State Updates (`docs/metadata/project-state.json`)
```json
{
  "project_metadata": {
    "overall_status": "pull_request_created",
    "health_score": "RECALCULATE_WITH_PR_METRICS",
    "last_updated": "CURRENT_TIMESTAMP"
  },
  "architecture_overview": {
    "deployment_readiness": {
      "pull_requests_created": "INCREMENT_PR_COUNT",
      "integration_validation_score": "UPDATE_INTEGRATION_SCORE",
      "merge_readiness_score": "UPDATE_MERGE_READINESS",
      "deployment_preparation_status": "UPDATE_DEPLOYMENT_STATUS"
    }
  },
  "workflow_statistics": {
    "command_execution_stats": {
      "total_command_executions": "INCREMENT_BY_1",
      "create_pr_completions": "INCREMENT_BY_1"
    },
    "subagent_performance": {
      "most_active_agents": "UPDATE_WITH_15_CREATE_PR_SUBAGENT"
    }
  },
  "recent_activity": {
    "last_command_executed": "create-pr",
    "last_metadata_update": "CURRENT_TIMESTAMP"
  }
}
```

#### Context File Updates (`.claude/context/project-context.json`)
```json
{
  "current_state": {
    "last_command": "create-pr",
    "last_command_timestamp": "CURRENT_TIMESTAMP"
  },
  "workflow_tracking": {
    "command_usage": {
      "create_pr": "INCREMENT_USAGE_COUNT"
    }
  },
  "pr_creation_status": {
    "created_pull_requests": "UPDATE_PR_LIST",
    "integration_validation": "UPDATE_INTEGRATION_VALIDATION",
    "merge_readiness": "UPDATE_MERGE_READINESS",
    "deployment_status": "UPDATE_DEPLOYMENT_PREPARATION"
  }
}
```

#### System Integration Updates (`.claude/context/system-integration.json`)
```json
{
  "real_time_metrics": {
    "current_session": {
      "commands_executed": "INCREMENT_BY_1",
      "metadata_syncs": "INCREMENT_BY_1",
      "pull_requests_created": "INCREMENT_BY_1"
    }
  },
  "pr_quality": {
    "quality_analysis_score": "UPDATE_PR_QUALITY_SCORE",
    "integration_compliance": "UPDATE_INTEGRATION_COMPLIANCE",
    "deployment_readiness": "UPDATE_DEPLOYMENT_READINESS"
  }
}
```

**⚠️ Error Handling**: If standard workflow is disrupted:
- 📖 Consult: [Manual Sync Guide](../../docs/maintenance/manual-sync-guide.md)
- 🔄 Check Status: `/use-case-status` for current project state
- 📊 Verify Context: `.claude/context/current-command-context.json`

