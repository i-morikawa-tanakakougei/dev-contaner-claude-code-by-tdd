Create pull request and close related issues.

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

### **Step 2: Execute Specialized Agent** 🤖
```bash
# Parse arguments and setup environment
source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "15-create-pr" "$ARGUMENTS"

# Validate required parameters
if [[ ${#issue_numbers[@]} -eq 0 ]]; then
    echo "エラー: 最低1つのイシュー番号が必要です"
    show_usage_example "create-pr" "1" "イシュー1のPR作成"
    show_usage_example "create-pr" "1,7" "複数イシュー統合PR作成"
    exit 1
fi

# Execute specialized agent with Task tool
echo "🤖 Starting specialized 15-create-pr agent..."
echo "📋 Issues: $(IFS=', '; echo "${issue_numbers[*]}")"

# Set up agent parameters
agent_params="{
    \"command\": \"15-create-pr\",
    \"issue_numbers\": [$(IFS=','; echo "\"${issue_numbers[*]//,/\",\"}\")"],
    \"feature_name\": \"${other_args[0]:-}\",
    \"working_directory\": \"$(pwd)\"
}"

# Execute agent
if ! execute_agent_with_task "15-create-pr" "$agent_params" "Create pull request and finalize implementation for issues: $(IFS=', #'; echo "#${issue_numbers[*]}")

## Agent Tasks:
1. Validate all development phases completed
2. Run comprehensive quality gates (tests, linting, architecture)
3. Generate comprehensive PR description with:
   - Executive summary and business value
   - Technical changes and architecture layers
   - Test plan and quality checklist
   - Issue closure integration
4. Push feature branch to remote
5. Create GitHub pull request with proper issue linking
6. Update metadata files and tactical index
7. Add PR information to related issues
8. Final validation and success reporting

## Success Criteria:
- All tests passing (uv run --frozen pytest)
- All quality checks clean (ruff, pyright)
- PR created with comprehensive description
- Issues properly linked for auto-closure
- Metadata files updated with PR information
- Branch pushed and synchronized
- Transaction committed successfully

## TDD/DDD/Layered Architecture Compliance:
- Validate domain layer purity maintained
- Verify application layer orchestration
- Check infrastructure layer isolation
- Confirm presentation layer separation
- Ensure Given-When-Then scenario coverage"; then
    echo "❌ 15-create-pr agent execution failed"
    exit 1
fi
```

### **Step 3: Agent Result Verification** ✅
```bash
# Verify agent execution results
echo "🔍 Verifying 15-create-pr agent results..."

# Check if metadata file exists and was updated
issue_list=$(IFS=-; echo "${issue_numbers[*]}")
if [[ -n "${other_args[0]:-}" ]]; then
    feature_name="${other_args[0]}"
else
    metadata_file=$(find docs/use_cases -name "issue-${issue_list}-*.json" 2>/dev/null | head -1)
    if [[ -z "$metadata_file" ]]; then
        echo "❌ Cannot determine feature name - metadata file not found"
        exit 1
    fi
    feature_name=$(basename "$metadata_file" .json | sed 's/issue-[0-9-]*-//')
fi

metadata_file="docs/use_cases/issue-${issue_list}-${feature_name}.json"

# Verify PR creation in metadata
if [[ ! -f "$metadata_file" ]]; then
    echo "❌ Metadata file not found: $metadata_file"
    exit 1
fi

pr_created=$(jq -r '.phases.pull_request.created // false' "$metadata_file")
pr_number=$(jq -r '.phases.pull_request.pr_number // empty' "$metadata_file")

if [[ "$pr_created" != "true" ]] || [[ -z "$pr_number" ]]; then
    echo "❌ PR creation not properly recorded in metadata"
    exit 1
fi

# Verify PR exists on GitHub
if ! gh pr view "$pr_number" >/dev/null 2>&1; then
    echo "❌ Created PR #$pr_number not accessible on GitHub"
    exit 1
fi

# Verify branch synchronization
current_branch=$(git branch --show-current)
if ! check_remote_sync "$current_branch" >/dev/null 2>&1; then
    echo "❌ Branch not properly synchronized with remote"
    exit 1
fi

echo "✅ 15-create-pr agent results verified successfully"
echo "   🔀 PR #$pr_number created"
echo "   🌳 Branch $current_branch synchronized"
echo "   📊 Metadata updated: $metadata_file"
```

### **Step 4: Display Success Summary** 🎉
```bash
# Display comprehensive success summary
echo ""
echo "🎉 プルリクエスト作成完了!"
echo "========================================"
echo "🔀 Pull Request: #$pr_number"
echo "🌳 Branch: $current_branch"
echo "🏷️  Feature: $feature_name"
echo "🔢 Issues: $(IFS=', #'; echo "#${issue_numbers[*]}")"
echo "📊 Metadata: $metadata_file"
echo ""

# Show PR URL if available
pr_url=$(gh pr view "$pr_number" --json url --jq '.url' 2>/dev/null || echo 'N/A')
echo "🔗 PR URL: $pr_url"
echo ""

# Display next steps
echo "📋 次のステップ:"
echo "   1. チームメンバーによるコードレビュー"
echo "   2. レビューフィードバック対応 (必要に応じて)"
echo "   3. 承認後のマージ"
echo "   4. 本番デプロイ"
echo ""

# Show quality metrics if available
if [[ -f "pyproject.toml" ]]; then
    echo "📊 品質メトリクス:"
    if command -v uv &> /dev/null; then
        echo "   📋 Tests: $(uv run --frozen pytest --tb=no -q 2>/dev/null | grep -E 'passed|failed|error' || echo 'N/A')"
    fi
    echo "   🏗️  Architecture: TDD/DDD/Layered compliance verified"
    echo ""
fi

# Display development phase completion
phases_completed=$(jq -r '.phases | keys | length' "$metadata_file" 2>/dev/null || echo "N/A")
echo "🏁 開発フェーズ完了: $phases_completed フェーズ"
echo "✅ 全開発フェーズ完了 - レビュー準備完了!"
echo ""

# Critical reminder for scenario evolution
echo "🚨 IMPORTANT: SCENARIO EVOLUTION CHECK"
echo "   PR作成中に新要件・制約・改善案発見時は"
echo "   作業を中断して /evolve-scenarios <feature-name> を実行すること"
echo "   CRITICAL: PR統合は最終チェックと新要件発見の重要な段階です"
echo ""

# Show operation summary
echo "📈 操作サマリー:"
echo "   - 全開発フェーズ検証完了"
echo "   - 品質ゲート全通過"
echo "   - GitHub PR作成・イシューリンク完了"
echo "   - メタデータ・インデックス更新完了"
echo "   - ブランチ同期・コミット完了"
echo ""
echo "🎊 TDD/DDD/レイヤードアーキテクチャによる実装サイクル完了!"
```