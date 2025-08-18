Create a Given-When-Then use case specification from GitHub issues.

## Metadata
- **Prerequisites**: GitHub issues created, Git repository initialized
- **Input**: Issue number(s) (required), feature name (optional)
- **Output**: 
  - `docs/use_cases/issue-X-Y.md` - Use case specification document
  - `docs/use_cases/issue-X-Y.json` - Metadata tracking file
  - Updated `docs/use_cases/index.md` with new entry
  - Feature branch `feature/issue-X-Y-feature-name`
- **Dependencies**: GitHub CLI (`gh`), Git configuration, jq
- **Execution Timing**: After sprint planning, before domain modeling

## 🎯 **TDD/DDD/LAYERED PROCESS CONTEXT**

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Sprint Review(02.5) → Use-Case(03) → Domain(04) → Design Review(04.5) → Tests(05) → Test Review(05.5) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Sprint Execution Phase - Use Case Specification Creation (03/16)  
> 🎯 **Phase Purpose**: Create Given-When-Then specifications and metadata from GitHub issues  
> ⬅️ **Previous Stage**: 02.5-review-sprint-plan (Sprint Plan Review)  
> ➡️ **Next Stage**: 04-domain-modeling (Domain Model Design)
>
> **📋 3-Layer Architecture Operations**:  
> - 🎯 **Strategic**: `docs/use_cases/core/index.md` (Reference vision alignment)  
> - 📊 **Tactical**: `docs/use_cases/index.md` (Add new use case entry)  
> - 🔧 **Execution**: `docs/use_cases/issue-X-Y.json` (Create detailed metadata)

## Common Errors and Solutions

### ❌ Error Case 1: Issue not found or inaccessible
**Cause**: Invalid issue number or insufficient GitHub permissions  
**Solution**: 
```bash
# Verify issue exists and is accessible
gh issue view <issue-number>
# Check GitHub authentication
gh auth status
```

### ❌ Error Case 2: Metadata template validation failure
**Cause**: Manual metadata creation or incomplete template  
**Solution**: 
- Always use `create_metadata_if_not_exists()` function
- Never create metadata JSON files manually
- Ensure all required phases are present in template

### ❌ Error Case 3: Feature branch creation failure
**Cause**: Branch name conflicts or Git permission issues  
**Solution**: 
```bash
# Check existing branches
git branch -a
# Ensure clean working directory
git status
```

## Execution Examples

### ✅ Success Example
```bash
$ /create-use-case 15 user-management
📋 イシュー #15 からユースケース仕様作成を開始します
🌿 フィーチャーブランチ作成: feature/issue-15-user-management
📋 全イシューの詳細取得と検証中...
=== Issue #15 ===
タイトル: ユーザー管理機能の実装
状態: open
📊 メタデータファイル作成: docs/use_cases/issue-15-user-management.json
✅ 正式メタデータテンプレート確認完了
📄 ユースケース仕様ファイル作成: docs/use_cases/issue-15-user-management.md
📚 インデックスファイル更新: docs/use_cases/index.md
🎉 ユースケース仕様作成完了!
```

### ❌ Failure Example and Fix
```bash
$ /create-use-case
エラー: 最低1つのイシュー番号が必要です
使用例: /create-use-case 1 (単一イシューからユースケース仕様作成)

# Fix: Provide issue number
$ /create-use-case 15
```

## 📖 **PHASE PURPOSE: SPECIFICATION CREATION ONLY**

**⚠️ Important Notice:**
- **This step is SPECIFICATION ONLY** - Create Given-When-Then use case specifications
- **NO FEATURE IMPLEMENTATION** - Focus on detailed requirements documentation  
- **Requirements phase** - Convert GitHub issues into detailed specifications
- **Create specification documents ONLY** - No code implementation

**TDD/DDD Flow Position:**
1. `02-sprint-planning` ← GitHub issues creation
2. `03-create-use-case` ← **【YOU ARE HERE】Specification creation**
3. `04-domain-modeling` ← Design documentation
4. `05-create-tests` ← TDD RED (failing tests)
5. `06-implement-domain` ← TDD GREEN (implementation)

**CREATE SPECIFICATIONS AND METADATA ONLY.**

## 📋 **USE CASE SPECIFICATION TASK CHECKLIST**

**Use this checklist to transform GitHub issues into detailed specifications:**

### 🔴 Required Tasks

#### **🎫 GitHub Issue Analysis**
- [ ] **Fetch issue details**: Retrieve title, description, labels, assignees, milestone from GitHub API
- [ ] **Parse issue requirements**: Extract functional requirements from issue description
- [ ] **Identify acceptance criteria**: Find or infer testable acceptance criteria
- [ ] **Extract business context**: Understand the business value and user motivation

#### **📝 Given-When-Then Specification Creation**
- [ ] **Write main scenario**: Create primary Given-When-Then scenario from issue requirements
- [ ] **Add error scenarios**: Create error handling scenarios based on issue constraints
- [ ] **Define preconditions**: Specify system state requirements before scenario execution
- [ ] **Define postconditions**: Specify expected system state after successful execution

#### **📊 Metadata & Project Integration**
- [ ] **Create issue metadata JSON**: Generate comprehensive tracking file (issue-X-Y.json)
- [ ] **Link to GitHub issue**: Ensure traceability between specification and issue
- [ ] **Update use cases index**: Add entry to tactical-level tracking document
- [ ] **Set implementation readiness**: Mark as ready for domain modeling phase

### 🟡 Recommended Tasks

#### **🔍 Requirements Extraction & Validation**
- [ ] **Validate issue completeness**: Ensure issue has sufficient information for implementation
- [ ] **Identify missing information**: Flag gaps that need clarification (use /evolve-scenarios if major)
- [ ] **Extract user stories**: Convert issue into user story format if not already
- [ ] **Define scope boundaries**: Clearly define what is and isn't included in this issue
- [ ] **Validate against vision**: Ensure alignment with project vision and core scenarios

#### **🏗️ Domain Concepts Identification**
- [ ] **Extract business terms**: Identify domain-specific vocabulary from issue description
- [ ] **Define key concepts**: Document business entities, processes, and rules mentioned
- [ ] **Map to ubiquitous language**: Align terminology with existing project vocabulary
- [ ] **Identify domain relationships**: Note how entities relate to each other
- [ ] **Flag new concepts**: Mark concepts not covered in current domain model

### 🟢 Optional Tasks

#### **📝 Advanced Specification Creation**
- [ ] **Add alternative scenarios**: Define alternate flows and edge cases mentioned in issue
- [ ] **Note technical constraints**: Identify any technical limitations mentioned in issue

#### **✅ Acceptance Criteria & Test Guidelines**
- [ ] **Define testable criteria**: Convert requirements into specific, measurable criteria
- [ ] **Create test scenarios**: Map Given-When-Then to future test implementation
- [ ] **Define validation rules**: Specify input validation and business rule enforcement
- [ ] **Document expected behaviors**: Detail all expected system responses
- [ ] **Prepare for TDD**: Structure criteria to support test-first development
- [ ] **Prepare handoff**: Ensure all information needed for /domain-modeling is available

**💡 Pro Tip**: If you discover major new scenarios not covered by the GitHub issue, use /evolve-scenarios instead of expanding scope!

> ⚠️ **CRITICAL REQUIREMENT - OFFICIAL METADATA TEMPLATE ONLY**:
> - 🚫 **NEVER** manually create metadata JSON files
> - ✅ **ALWAYS** use `create_metadata_if_not_exists()` function from `_metadata_operations.sh`
> - 🔍 **MANDATORY** verification of complete template structure (40+ fields)
> - 📊 Official template includes: scenario_evolution, review, feedback_application, pull_request phases
> - ❌ Simplified or manual metadata files will cause validation failures

## Task Details

1. **Setup Safe Environment and Parse Arguments**:
   ```bash
   # 🔧 Load all safe operation functions with automatic argument parsing and validation
   source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "03-create-use-case" "$ARGUMENTS"
   
   # Arguments are already parsed and validated by setup script
   # Additional validation for this specific command
   if [[ ${#issue_numbers[@]} -eq 0 ]]; then
       echo "エラー: 最低1つのイシュー番号が必要です"
       show_usage_example "create-use-case" "1" "単一イシューからユースケース仕様作成"
       show_usage_example "create-use-case" "1,7" "複数イシューからユースケース仕様作成"
       show_usage_example "create-use-case" "1,mt5-data" "イシュー1 + 機能名'mt5-data'を指定"
       exit 1
   fi
   ```

2. **Begin Transaction and Prepare Development Environment**:
   ```bash
   # 🔄 Start transaction for atomic operations
   if ! begin_transaction "create_use_case_$(IFS=-; echo "${issue_numbers[*]}")"; then
       echo "エラー: トランザクションの開始に失敗しました"
       exit 1
   fi
   
   # 📝 Determine feature name safely
   if [[ ${#other_args[@]} -gt 0 ]]; then
       feature_name="${other_args[0]}"
   else
       # 🔍 Derive from primary issue title with error handling
       primary_issue="${issue_numbers[0]}"
       echo "イシュー #$primary_issue からフィーチャー名を取得中..."
       
       if ! issue_info=$(safe_get_issue_info "$primary_issue" "json"); then
           echo "エラー: イシュー #$primary_issue の情報取得に失敗しました"
           execute_rollback "issue_fetch_failed"
           exit 1
       fi
       
       feature_name=$(echo "$issue_info" | jq -r '.title' | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | sed 's/^-\|-$//g')
       
       if [[ -z "$feature_name" ]]; then
           echo "エラー: フィーチャー名の生成に失敗しました"
           execute_rollback "feature_name_generation_failed"
           exit 1
       fi
       
       echo "✅ フィーチャー名生成: $feature_name"
   fi
   
   # 🌿 Create feature branch safely with rollback
   issue_list=$(IFS=-; echo "${issue_numbers[*]}")
   branch_name="feature/issue-${issue_list}-${feature_name}"
   
   echo "フィーチャーブランチ作成: $branch_name"
   if ! safe_create_or_switch_branch "$branch_name"; then
       echo "エラー: ブランチの作成/切り替えに失敗しました"
       execute_rollback "branch_creation_failed"
       exit 1
   fi
   
   # Add rollback operation for branch cleanup
   add_rollback "git checkout main && git branch -D '$branch_name'" "Clean up feature branch"
   ```

3. **Validate Issues and Check Vision Alignment**:
   ```bash
   # 🔍 Fetch and validate all issue details
   echo "📋 全イシューの詳細取得と検証中..."
   
   for issue_num in "${issue_numbers[@]}"; do
       echo "=== Issue #$issue_num ==="
       
       if ! safe_get_issue_info "$issue_num" "plain"; then
           echo "エラー: イシュー #$issue_num へのアクセスに失敗しました"
           execute_rollback "issue_validation_failed"
           exit 1
       fi
       
       # Verify issue is open
       if issue_state=$(safe_get_issue_info "$issue_num" "json" | jq -r '.state'); then
           if [[ "$issue_state" == "closed" ]]; then
               echo "警告: イシュー #$issue_num は既に閉じられています" >&2
           fi
       fi
   done
   
   # 📖 Check vision alignment safely
   echo "📖 ビジョンアライメント確認中..."
   
   if [[ -f "docs/vision/project-vision.md" ]]; then
       if check_file_permissions "docs/vision/project-vision.md" "read"; then
           echo "✅ ビジョンドキュメント確認完了"
           # Here you could add actual alignment checking logic
       else
           echo "警告: ビジョンドキュメントの読み取り権限がありません" >&2
       fi
   else
       echo "⚠️  ビジョンドキュメントが存在しません: docs/vision/project-vision.md"
   fi
   ```

4. **Create Metadata File with Atomic Operations**:
   ```bash
   # 📊 Create metadata file safely using MANDATORY official template
   metadata_file="docs/use_cases/issue-${issue_list}-${feature_name}.json"
   
   echo "メタデータファイル作成: $metadata_file"
   
   # 🚫 CRITICAL: NEVER create metadata files manually - ALWAYS use create_metadata_if_not_exists()
   # This function ensures the complete official template structure is used
   if ! create_metadata_if_not_exists "$metadata_file" "$feature_name" "${issue_numbers[@]}"; then
       echo "エラー: メタデータファイルの作成に失敗しました"
       execute_rollback "metadata_creation_failed"
       exit 1
   fi
   
   # ✅ Verify the official template was used (must have all required phases)
   if ! jq -e '.phases.scenario_evolution and .phases.review and .phases.feedback_application and .phases.pull_request' "$metadata_file" >/dev/null 2>&1; then
       echo "❌ エラー: 正式テンプレートが使用されていません - 手動作成は禁止されています"
       echo "   必須フィールド: scenario_evolution, review, feedback_application, pull_request"
       execute_rollback "invalid_metadata_template"
       exit 1
   fi
   
   echo "✅ 正式メタデータテンプレート確認完了"
   
   # Add rollback for metadata file
   add_rollback "rm -f '$metadata_file'" "Clean up metadata file"
   
   # 🔄 Update metadata atomically
   echo "メタデータ更新中..."
   if ! update_metadata_atomic "$metadata_file" '
       .phases.use_case.created = true |
       .phases.use_case.approved = false |
       .phase = "use_case_created" |
       .updated_at = "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'"
   '; then
       echo "エラー: メタデータの更新に失敗しました"
       execute_rollback "metadata_update_failed"
       exit 1
   fi
   ```

5. **Create Use Case Specification Files Safely**:
   ```bash
   # 📄 Create specification file with safe operations
   spec_file="docs/use_cases/issue-${issue_list}-${feature_name}.md"
   
   echo "ユースケース仕様ファイル作成: $spec_file"
   
   # 🛡️ Verify safe operation before file creation
   if ! verify_safe_operation "create" "$spec_file" 50; then
       echo "エラー: ファイル作成の安全性チェックに失敗しました"
       execute_rollback "safety_check_failed"
       exit 1
   fi
   
   # 📝 Generate specification content
   spec_content="$(cat <<EOF
# ユースケース仕様: $feature_name

## 概要
$(for num in "${issue_numbers[@]}"; do echo "- [Issue #$num]($(gh issue view $num --json url --jq '.url' 2>/dev/null || echo 'N/A'))"; done)

## Given-When-Then シナリオ

### メインシナリオ
**Given**: <前提条件を記述>
- システムが正常に稼働している
- ユーザーが適切な権限を持っている

**When**: <実行される操作を記述>
- ユーザーが特定のアクションを実行する

**Then**: <期待される結果を記述>
- システムが期待通りに応答する
- 適切な状態変更が発生する

### 代替シナリオ 1: エラーケース
**Given**: <エラー前提条件>
**When**: <エラー操作>
**Then**: <エラー処理結果>

### 代替シナリオ 2: 境界値ケース
**Given**: <境界値前提条件>
**When**: <境界値操作>
**Then**: <境界値処理結果>

## 非機能要件
- **性能**: レスポンス時間 < 2秒
- **セキュリティ**: 適切な認証・認可
- **可用性**: 99.9% アップタイム

## 受け入れ基準
- [ ] メインシナリオが正常に動作する
- [ ] エラーケースが適切に処理される
- [ ] 非機能要件を満たす
- [ ] セキュリティ要件を満たす
- [ ] テストケースが網羅的に作成されている

## 関連情報
- **作成日時**: $(date)
- **作成者**: $(git config user.name || echo "Unknown")
- **関連イシュー**: $(for num in "${issue_numbers[@]}"; do echo "#$num "; done)
- **ブランチ**: $branch_name
- **メタデータ**: $metadata_file

## 次のステップ
1. ドメインモデル設計: \`/domain-modeling ${issue_numbers[*]}\`
2. テスト作成: \`/create-tests ${issue_numbers[*]}\`
EOF
)"

   # 📄 Create file safely with backup
   if ! safe_create_file "$spec_file" "$spec_content" true; then
       echo "エラー: 仕様ファイルの作成に失敗しました"
       execute_rollback "spec_file_creation_failed"
       exit 1
   fi
   
   # Add rollback for spec file
   add_rollback "rm -f '$spec_file'" "Clean up specification file"
   ```

6. **Update Index Files Safely**:
   ```bash
   # 📚 Update tactical level index file safely
   index_file="docs/use_cases/index.md"
   
   echo "インデックスファイル更新: $index_file"
   
   # 🔍 Create index file if it doesn't exist
   if [[ ! -f "$index_file" ]]; then
       index_content="# Use Case Implementation Status

## In Progress 🚧
- [$feature_name]($spec_file) - Issues: $(IFS=', #'; echo "#${issue_numbers[*]}") (Phase: use_case_created)

## Completed ✅
(None yet)

## Evolved Scenarios
(None yet)
"
       
       if ! safe_create_file "$index_file" "$index_content" true; then
           echo "エラー: インデックスファイルの作成に失敗しました"
           execute_rollback "index_creation_failed"
           exit 1
       fi
   else
       # 🔄 Update existing index file safely
       # Create backup before modification
       backup_file="${index_file}.backup.$(date +%Y%m%d_%H%M%S)"
       if ! cp "$index_file" "$backup_file"; then
           echo "エラー: インデックスファイルのバックアップ作成に失敗しました"
           execute_rollback "index_backup_failed"
           exit 1
       fi
       
       add_rollback "mv '$backup_file' '$index_file'" "Restore index file backup"
       
       # Safe update using temporary file
       temp_file="${index_file}.tmp"
       if ! sed "/## In Progress 🚧/a\\
   - [$feature_name]($spec_file) - Issues: $(IFS=', #'; echo "#${issue_numbers[*]}") (Phase: use_case_created)" "$index_file" > "$temp_file"; then
           echo "エラー: インデックスファイルの更新に失敗しました"
           execute_rollback "index_update_failed"
           exit 1
       fi
       
       if ! mv "$temp_file" "$index_file"; then
           echo "エラー: インデックスファイルの置換に失敗しました"
           execute_rollback "index_replacement_failed"
           exit 1
       fi
   fi
   ```

7. **Commit Changes Safely**:
   ```bash
   # 💾 Commit with safe git operations
   commit_message="feat: add use case specification for $feature_name

   Create Given-When-Then scenarios and metadata tracking for:
   $(for num in "${issue_numbers[@]}"; do echo "- Issue #$num"; done)
   
   Files created:
   - $spec_file (use case specification)
   - $metadata_file (metadata tracking)
   - $index_file (updated index)
   
   Related issues: $(for num in "${issue_numbers[@]}"; do echo "Closes #$num"; done | tr '\n' ' ')
   "
   
   echo "変更をコミット中..."
   if ! safe_git_commit "$commit_message" "$spec_file" "$metadata_file" "$index_file"; then
       echo "エラー: コミットに失敗しました"
       execute_rollback "commit_failed"
       exit 1
   fi
   
   # Update rollback to include commit cleanup
   add_rollback "git reset --hard HEAD~1" "Undo commit"
   ```

8. **Update GitHub Issues**:
   ```bash
   # 📢 Update issues with safe GitHub operations
   echo "GitHub イシューの更新中..."
   
   for issue_num in "${issue_numbers[@]}"; do
       comment_body="✅ **ユースケース仕様作成完了**

   **作成ファイル:**
   - 📋 仕様書: \`$spec_file\`
   - 📊 メタデータ: \`$metadata_file\`
   - 🌳 ブランチ: \`$branch_name\`

   **次のステップ:**
   \`\`\`bash
   /domain-modeling ${issue_numbers[*]}
   \`\`\`

   **進捗状況:** TDD フェーズ 1/3 (RED-GREEN-REFACTOR)
   "
       
       if ! safe_add_issue_comment "$issue_num" "$comment_body"; then
           echo "警告: イシュー #$issue_num へのコメント追加に失敗しました (続行します)" >&2
           # GitHub API エラーは警告のみで処理続行
       else
           echo "✅ イシュー #$issue_num にコメント追加完了"
       fi
   done
   ```

9. **Final Validation and Commit Transaction**:
   ```bash
   # 🔍 Final validation
   echo "最終検証実行中..."
   
   # Metadata integrity check
   if ! validate_metadata_integrity "$metadata_file"; then
       echo "エラー: メタデータの整合性チェックに失敗しました"
       execute_rollback "final_validation_failed"
       exit 1
   fi
   
   # 🚨 CRITICAL: Double-check official template compliance
   echo "正式テンプレート完全性チェック..."
   required_phases=("scenario_evolution" "review" "feedback_application" "pull_request" "all_tests" "refactor")
   for phase in "${required_phases[@]}"; do
       if ! jq -e ".phases.$phase" "$metadata_file" >/dev/null 2>&1; then
           echo "❌ エラー: 必須フェーズが不足: $phase"
           echo "   正式テンプレートではありません。create_metadata_if_not_exists()を使用してください"
           execute_rollback "incomplete_metadata_template"
           exit 1
       fi
   done
   echo "✅ 正式テンプレート完全性確認完了"
   
   # File existence verification
   for file in "$spec_file" "$metadata_file" "$index_file"; do
       if [[ ! -f "$file" ]]; then
           echo "エラー: 必要なファイルが存在しません: $file"
           execute_rollback "file_missing"
           exit 1
       fi
   done
   
   # Git status verification
   if ! git diff --quiet HEAD~1 HEAD; then
       echo "✅ 変更が正常にコミットされています"
   else
       echo "エラー: 期待される変更がコミットされていません"
       execute_rollback "commit_verification_failed"
       exit 1
   fi
   
   # 🎉 Commit transaction (success!)
   if commit_transaction; then
       echo ""
       echo "🎉 ユースケース仕様作成完了!"
       echo "================================="
       echo "📁 仕様ファイル: $spec_file"
       echo "📊 メタデータ: $metadata_file"
       echo "📚 インデックス: $index_file"
       echo "🌳 ブランチ: $branch_name"
       echo "🔢 関連イシュー: $(IFS=', #'; echo "#${issue_numbers[*]}")"
       echo ""
       echo "📋 次のコマンド実行:"
       echo "   /domain-modeling ${issue_numbers[*]}"
       echo ""
       echo "🚨 MANDATORY FOR CLAUDE CODE: SCENARIO EVOLUTION CHECK"
       echo "   Claude Code: 新しい要件・エラー・エッジケースを発見時は"
       echo "   必ず /evolve-scenarios <feature-name> を実行すること"
       echo "   ユーザー: 上記と同様の対応をお願いします"
       echo "   警告: このルール違反は重大な実装漏れを引き起こします"
       echo ""
       
       # 🔍 Show metadata template verification
       echo "📊 メタデータテンプレート情報:"
       echo "   フェーズ数: $(jq '.phases | length' "$metadata_file")"
       echo "   テンプレート版: 正式版 ($(jq -r '.created_at' "$metadata_file"))"
       echo "   必須フィールド: ✅ 全て含まれています"
       echo ""
       
       # Show operation logs
       echo "📊 操作ログ:"
       show_git_operation_log
       show_file_operation_log
       show_github_operation_log
       show_transaction_log
       
   else
       echo "❌ トランザクション コミット失敗"
       exit 1
   fi
   ```