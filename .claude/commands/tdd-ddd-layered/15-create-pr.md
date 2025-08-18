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

**💡 Pro Tip: A well-written PR description saves hours of review time and helps ensure smooth merging - invest in quality PR documentation!
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

## Task Details

1. **Setup Safe Environment and Validation**:
   ```bash
   # 🔧 Load all safe operation functions
   source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "15-create-pr" "$ARGUMENTS"
   
   # Validate we have at least one issue number
   if [[ ${#issue_numbers[@]} -eq 0 ]]; then
       echo "エラー: 最低1つのイシュー番号が必要です"
       show_usage_example "create-pr" "1" "イシュー1のPR作成"
       show_usage_example "create-pr" "1,7" "複数イシュー統合PR作成"
       exit 1
   fi
   ```

2. **Begin Transaction and Pre-validation**:
   ```bash
   # 🔄 Start comprehensive transaction
   if ! begin_transaction "create_pr_$(IFS=-; echo "${issue_numbers[*]}")"; then
       echo "エラー: トランザクションの開始に失敗しました"
       exit 1
   fi
   
   # 📝 Determine feature name and metadata file
   if [[ ${#other_args[@]} -gt 0 ]]; then
       feature_name="${other_args[0]}"
   else
       # Find metadata file from existing files
       issue_list=$(IFS=-; echo "${issue_numbers[*]}")
       metadata_file=$(find docs/use_cases -name "issue-${issue_list}-*.json" 2>/dev/null | head -1)
       
       if [[ -z "$metadata_file" ]]; then
           echo "エラー: フィーチャー名が指定されておらず、メタデータファイルも見つかりません"
           echo "使用方法: /create-pr ${issue_numbers[*]} フィーチャー名"
           execute_rollback "metadata_not_found"
           exit 1
       fi
       
       feature_name=$(basename "$metadata_file" .json | sed 's/issue-[0-9-]*-//')
   fi
   
   # Set metadata file path
   issue_list=$(IFS=-; echo "${issue_numbers[*]}")
   metadata_file="docs/use_cases/issue-${issue_list}-${feature_name}.json"
   
   echo "🔍 メタデータファイル: $metadata_file"
   echo "🏷️  フィーチャー名: $feature_name"
   ```

3. **Comprehensive Pre-PR Validation**:
   ```bash
   # 🔍 Validate all prerequisites
   echo "📋 PR作成前の包括的検証実行中..."
   
   # 1. Metadata file validation
   if [[ ! -f "$metadata_file" ]]; then
       echo "エラー: メタデータファイルが存在しません: $metadata_file"
       execute_rollback "metadata_missing"
       exit 1
   fi
   
   if ! validate_metadata_integrity "$metadata_file"; then
       echo "エラー: メタデータファイルの整合性チェックに失敗しました"
       execute_rollback "metadata_invalid"
       exit 1
   fi
   
   # 2. Check all required phases are completed
   echo "📊 開発フェーズ完了状況確認中..."
   
   required_phases=("use_case" "domain_model" "tests" "domain_implementation" "usecase_implementation" "infrastructure_implementation" "presentation_implementation" "all_tests" "refactor")
   
   for phase in "${required_phases[@]}"; do
       phase_completed=$(jq -r ".phases.${phase}.completed // .phases.${phase}.created // false" "$metadata_file")
       if [[ "$phase_completed" != "true" ]]; then
           echo "エラー: 必須フェーズが未完了です: $phase"
           echo "現在の状態: $phase_completed"
           execute_rollback "phase_incomplete"
           exit 1
       fi
       echo "  ✅ $phase: 完了"
   done
   
   # 3. Validate GitHub issues exist and are accessible
   echo "🔍 GitHub イシュー検証中..."
   for issue_num in "${issue_numbers[@]}"; do
       if ! safe_get_issue_info "$issue_num" "json" >/dev/null; then
           echo "エラー: イシュー #$issue_num にアクセスできません"
           execute_rollback "issue_access_failed"
           exit 1
       fi
       echo "  ✅ イシュー #$issue_num: アクセス可能"
   done
   
   # 4. Git repository state validation
   echo "🌳 Git リポジトリ状態確認中..."
   
   current_branch=$(git branch --show-current)
   if [[ -z "$current_branch" ]]; then
       echo "エラー: 現在のブランチ名を取得できません"
       execute_rollback "branch_detection_failed"
       exit 1
   fi
   
   expected_branch="feature/issue-${issue_list}-${feature_name}"
   if [[ "$current_branch" != "$expected_branch" ]]; then
       echo "警告: 期待されるブランチと異なります"
       echo "現在: $current_branch"
       echo "期待: $expected_branch"
   fi
   
   # 5. Check for uncommitted changes
   if ! git diff-index --quiet HEAD --; then
       echo "⚠️  未コミットの変更があります。PR作成前にコミットします。"
       
       # Safe commit of remaining changes
       if ! safe_git_commit "chore: final changes before PR creation

   Final cleanup and preparation for pull request.
   
   Related issues: $(for num in "${issue_numbers[@]}"; do echo "#$num "; done)" "." ; then
           echo "エラー: 最終コミットに失敗しました"
           execute_rollback "final_commit_failed"
           exit 1
       fi
       
       add_rollback "git reset --hard HEAD~1" "Undo final commit"
   fi
   ```

4. **Architecture and Quality Validation**:
   ```bash
   # 🏗️ Architecture validation
   echo "🏗️ アーキテクチャ検証実行中..."
   
   if ! validate_architecture; then
       echo "エラー: アーキテクチャ検証に失敗しました"
       echo "PR作成前にアーキテクチャ違反を修正してください"
       execute_rollback "architecture_validation_failed"
       exit 1
   fi
   
   echo "✅ アーキテクチャ検証完了"
   
   # 🧪 Run all tests if available
   echo "🧪 テスト実行中..."
   
   if [[ -f "pyproject.toml" ]] && command -v uv &> /dev/null; then
       echo "Python プロジェクト検出 - テスト実行中..."
       
       if ! uv run --frozen pytest --tb=short; then
           echo "エラー: テストが失敗しました"
           echo "PR作成前にテストを修正してください"
           execute_rollback "tests_failed"
           exit 1
       fi
       
       echo "✅ 全テスト成功"
   else
       echo "⚠️  テスト環境が検出されませんでした"
   fi
   ```

5. **Generate PR Content and Push Branch**:
   ```bash
   # 📝 Generate comprehensive PR content
   echo "📝 PR内容生成中..."
   
   # Extract information from metadata
   creation_date=$(jq -r '.created_at' "$metadata_file")
   phases_completed=$(jq -r '.phases | keys[]' "$metadata_file" | wc -l)
   
   # Generate PR title
   pr_title="feat: implement $feature_name"
   if [[ ${#issue_numbers[@]} -gt 1 ]]; then
       pr_title="$pr_title (multiple issues)"
   fi
   
   # Generate comprehensive PR body
   pr_body="$(cat <<EOF
## 📋 Summary
   
   Implementation of **$feature_name** feature covering the following requirements:
   $(for num in "${issue_numbers[@]}"; do echo "- Closes #$num"; done)
   
## 🎯 What Changed
   
   ### 📊 Implementation Overview
   - **Development Phases Completed**: $phases_completed
   - **Architecture**: TDD/DDD/Layered Architecture
   - **Created**: $creation_date
   - **Branch**: $current_branch
   
   ### 🏗️ Architecture Layers Implemented
   - ✅ **Domain Layer**: Core business logic and entities
   - ✅ **Application Layer**: Use cases and orchestration
   - ✅ **Infrastructure Layer**: Data persistence and external services
   - ✅ **Presentation Layer**: API endpoints and user interfaces
   
   ### 📁 Files Modified/Created
   $(git diff --name-status main..HEAD | sed 's/^/   - /')
   
## 🧪 Test Plan
   
   - [x] Unit tests for domain entities and value objects
   - [x] Integration tests for use cases
   - [x] Architecture compliance validation
   - [x] End-to-end scenario testing
   - [x] Error handling and edge cases
   
## 🔍 Review Checklist
   
   ### Code Quality
   - [x] Follows TDD/DDD principles
   - [x] Proper layer separation maintained
   - [x] No architectural violations
   - [x] Comprehensive error handling
   
   ### Documentation
   - [x] Use case specifications updated
   - [x] API documentation current
   - [x] README updated if needed
   
   ### Testing
   - [x] All tests passing
   - [x] Test coverage adequate
   - [x] Integration tests included
   
## 📊 Metadata
   
   - **Feature**: $feature_name
   - **Issues**: $(IFS=', #'; echo "#${issue_numbers[*]}")
   - **Metadata File**: \`$metadata_file\`
   - **Development Phases**: $(jq -r '.phases | keys | join(", ")' "$metadata_file")
   
## 🚀 Deployment Notes
   
   This feature is ready for deployment and includes:
   - Database migrations (if applicable)
   - Configuration changes documented
   - Backward compatibility maintained
   
   ---
   
   **Generated**: $(date)
   **Branch**: $current_branch
EOF
)"

   # 🚀 Push branch safely
   echo "🚀 ブランチをプッシュ中: $current_branch"
   
   if ! safe_git_push "$current_branch"; then
       echo "エラー: ブランチのプッシュに失敗しました"
       execute_rollback "push_failed"
       exit 1
   fi
   
   add_rollback "git push origin --delete '$current_branch'" "Delete remote branch"
   echo "✅ ブランチプッシュ完了"
   ```

6. **Create Pull Request**:
   ```bash
   # 🔀 Create pull request safely
   echo "🔀 プルリクエスト作成中..."
   
   pr_number=$(safe_create_pull_request "$pr_title" "$pr_body" "main" "$current_branch")
   
   if [[ -z "$pr_number" ]]; then
       echo "エラー: プルリクエストの作成に失敗しました"
       execute_rollback "pr_creation_failed"
       exit 1
   fi
   
   echo "✅ プルリクエスト作成成功: #$pr_number"
   add_rollback "gh pr close '$pr_number' --delete-branch" "Close PR and cleanup"
   ```

7. **Update Metadata and Index Files**:
   ```bash
   # 📊 Update metadata with PR information
   echo "📊 メタデータファイル更新中..."
   
   if ! update_metadata_atomic "$metadata_file" "
       .phases.pull_request.created = true |
       .phases.pull_request.pr_number = $pr_number |
       .phases.pull_request.merged = false |
       .phase = \"pull_request_created\" |
       .updated_at = \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\"
   "; then
       echo "エラー: メタデータの更新に失敗しました"
       execute_rollback "metadata_update_failed"
       exit 1
   fi
   
   # 📚 Update tactical index file
   index_file="docs/use_cases/index.md"
   
   if [[ -f "$index_file" ]]; then
       echo "📚 インデックスファイル更新中..."
       
       # Create backup
       backup_file="${index_file}.backup.$(date +%Y%m%d_%H%M%S)"
       if ! cp "$index_file" "$backup_file"; then
           echo "エラー: インデックスファイルのバックアップ作成に失敗しました"
           execute_rollback "index_backup_failed"
           exit 1
       fi
       
       add_rollback "mv '$backup_file' '$index_file'" "Restore index backup"
       
       # Update status from "In Progress" to "Review"
       temp_file="${index_file}.tmp"
       if ! sed "s/- \[${feature_name}\].*Phase: [^)]*)/- [$feature_name](issue-${issue_list}-${feature_name}.md) - Issues: $(IFS=', #'; echo "#${issue_numbers[*]}") (Phase: pull_request_created, PR: #$pr_number)/" "$index_file" > "$temp_file"; then
           echo "エラー: インデックスファイルの更新に失敗しました"
           execute_rollback "index_update_failed"
           exit 1
       fi
       
       if ! mv "$temp_file" "$index_file"; then
           echo "エラー: インデックスファイルの置換に失敗しました"
           execute_rollback "index_replacement_failed"
           exit 1
       fi
       
       echo "✅ インデックスファイル更新完了"
   fi
   ```

8. **Final Commit and Issue Updates**:
   ```bash
   # 💾 Commit metadata updates
   echo "💾 メタデータ変更をコミット中..."
   
   if ! safe_git_commit "chore: update metadata for PR #$pr_number

   Update metadata and index files to reflect PR creation.
   
   - PR #$pr_number created for $feature_name
   - Status updated to pull_request_created
   - Index file updated with PR reference
   
   Related issues: $(for num in "${issue_numbers[@]}"; do echo "#$num "; done)" "$metadata_file" "$index_file"; then
       echo "エラー: メタデータコミットに失敗しました"
       execute_rollback "metadata_commit_failed"
       exit 1
   fi
   
   add_rollback "git reset --hard HEAD~1" "Undo metadata commit"
   
   # 🚀 Push final changes
   if ! safe_git_push "$current_branch"; then
       echo "エラー: 最終プッシュに失敗しました"
       execute_rollback "final_push_failed"
       exit 1
   fi
   
   # 📢 Update GitHub issues with PR information
   echo "📢 GitHub イシュー更新中..."
   
   for issue_num in "${issue_numbers[@]}"; do
       comment_body="🎉 **プルリクエスト作成完了**

   **Pull Request**: [#$pr_number]($(gh pr view $pr_number --json url --jq '.url' 2>/dev/null || echo 'N/A'))
   **Branch**: \`$current_branch\`
   **Feature**: $feature_name

   **🔍 Review Ready:**
   - ✅ All development phases completed
   - ✅ Architecture validation passed
   - ✅ All tests passing
   - ✅ Code ready for review

   **📊 Implementation Summary:**
   - Domain layer: Business logic implemented
   - Application layer: Use cases orchestrated  
   - Infrastructure layer: Persistence implemented
   - Presentation layer: API endpoints created

   **Next Steps:**
   1. Code review by team members
   2. Address any review feedback
   3. Merge when approved
   4. Deploy to staging/production

   This issue will be automatically closed when the PR is merged.
   "
       
       if ! safe_add_issue_comment "$issue_num" "$comment_body"; then
           echo "警告: イシュー #$issue_num へのコメント追加に失敗しました (続行します)" >&2
       else
           echo "✅ イシュー #$issue_num にPR情報コメント追加完了"
       fi
   done
   ```

9. **Final Validation and Success**:
   ```bash
   # 🔍 Final comprehensive validation
   echo "🔍 最終検証実行中..."
   
   # Verify PR was created successfully
   if ! gh pr view "$pr_number" >/dev/null 2>&1; then
       echo "エラー: 作成されたPRにアクセスできません: #$pr_number"
       execute_rollback "pr_verification_failed"
       exit 1
   fi
   
   # Verify metadata was updated
   pr_created_status=$(jq -r '.phases.pull_request.created' "$metadata_file")
   if [[ "$pr_created_status" != "true" ]]; then
       echo "エラー: メタデータのPR作成状態が正しく更新されていません"
       execute_rollback "metadata_verification_failed"
       exit 1
   fi
   
   # Verify branch is pushed and up-to-date
   if ! check_remote_sync "$current_branch" >/dev/null; then
       echo "エラー: ブランチがリモートと同期されていません"
       execute_rollback "sync_verification_failed"
       exit 1
   fi
   
   # 🎉 Transaction commit (success!)
   if commit_transaction; then
       echo ""
       echo "🎉 プルリクエスト作成完了!"
       echo "========================================="
       echo "🔀 Pull Request: #$pr_number"
       echo "🌳 Branch: $current_branch"
       echo "🏷️  Feature: $feature_name"
       echo "🔢 Issues: $(IFS=', #'; echo "#${issue_numbers[*]}")"
       echo "📊 Metadata: $metadata_file"
       echo ""
       echo "🔗 PR URL: $(gh pr view $pr_number --json url --jq '.url' 2>/dev/null || echo 'N/A')"
       echo ""
       echo "📋 次のステップ:"
       echo "   1. チームメンバーによるコードレビュー"
       echo "   2. レビューフィードバック対応 (必要に応じて)"
       echo "   3. 承認後のマージ"
       echo "   4. 本番デプロイ"
       echo ""
       
       # Show comprehensive operation logs
       echo "📊 操作ログサマリー:"
       show_git_operation_log | tail -5
       show_github_operation_log | tail -3
       show_transaction_log | tail -3
       
       echo ""
       echo "✅ 全開発フェーズ完了 - レビュー準備完了!"
       echo ""
       echo "🚨 MANDATORY FOR CLAUDE CODE: SCENARIO EVOLUTION CHECK"
       echo "   PR作成中に新要件・制約・改善案発見時は"
       echo "   作業を中断して /evolve-scenarios <feature-name> を実行すること"
       echo "   CRITICAL: PR統合は最終チェックと新要件発見の重要な段階です"
       
   else
       echo "❌ トランザクション コミット失敗"
       exit 1
   fi
   ```