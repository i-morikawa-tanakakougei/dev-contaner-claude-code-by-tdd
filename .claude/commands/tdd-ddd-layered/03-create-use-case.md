Use the 03-create-use-case subagent to create a Given-When-Then use case specification from GitHub issues. This command MUST USE the specialized 03-create-use-case subagent for optimal use case specification creation.

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

## 📋 **USE CASE SPECIFICATION TASK CHECKLIST**

**Use this checklist for comprehensive use case specification creation:**

### 🔴 Required Tasks

#### **📖 Issue Analysis**
- [ ] **Fetch issue details**: Retrieve issue from GitHub API
- [ ] **Extract requirements**: Parse issue description and acceptance criteria
- [ ] **Identify stakeholders**: Determine primary and secondary users
- [ ] **Map to domain concepts**: Connect issue to business domain

#### **📝 Specification Creation**
- [ ] **Write Given-When-Then scenarios**: Convert requirements to testable scenarios
- [ ] **Define acceptance criteria**: Clear success and failure conditions
- [ ] **Establish ubiquitous language**: Domain terminology and definitions
- [ ] **Document assumptions**: Explicit assumptions and constraints

#### **📊 Metadata Management**
- [ ] **Create tracking metadata**: Issue metadata in JSON format
- [ ] **Initialize phase tracking**: Set up development phase workflow
- [ ] **Update project index**: Add entry to use cases index
- [ ] **Create feature branch**: Git branch for isolated development

### 🟡 Recommended Tasks

#### **🔄 Vision Alignment**
- [ ] **Reference core scenarios**: Ensure alignment with project vision
- [ ] **Check bounded context**: Verify domain boundary consistency
- [ ] **Validate priority**: Confirm issue priority and dependencies
- [ ] **Review stakeholder needs**: Ensure user value proposition

#### **📚 Documentation Quality**
- [ ] **Use domain language**: Consistent terminology throughout
- [ ] **Include examples**: Concrete examples for clarity
- [ ] **Add cross-references**: Links to related issues and documentation
- [ ] **Review readability**: Clear, unambiguous specification text

## Task Details

**🤖 Agent Integration**: This command MUST USE PROACTIVELY the specialized `03-create-use-case` subagent for optimal use case specification creation. Claude Code should automatically delegate this task to the 03-create-use-case subagent based on the command description.

1. **Pre-execution Validation**:
   ```bash
   # Validate issue number requirement
   if [[ $# -eq 0 ]]; then
       echo "エラー: 少なくとも1つのイシュー番号を指定してください"
       echo "使用例: /create-use-case 1"
       echo "使用例: /create-use-case 1,7 (複数イシュー)"
       echo "使用例: /create-use-case 1 feature-name"
       exit 1
   fi
   
   # Extract issue numbers and feature name
   issue_numbers=()
   feature_name=""
   
   # Parse first argument for issue numbers
   IFS=',' read -ra ISSUE_ARRAY <<< "$1"
   for issue in "${ISSUE_ARRAY[@]}"; do
       if [[ "$issue" =~ ^[0-9]+$ ]]; then
           issue_numbers+=("$issue")
       fi
   done
   
   # Optional feature name from second argument
   if [[ $# -gt 1 ]]; then
       feature_name="$2"
   fi
   
   # Check GitHub CLI availability
   if ! command -v gh >/dev/null 2>&1; then
       echo "❌ エラー: GitHub CLI (gh) が見つかりません"
       echo "💡 GitHub CLIをインストールしてください: https://cli.github.com/"
       exit 1
   fi
   
   echo "📋 Issues: $(printf '#%s ' "${issue_numbers[@]}")のユースケース仕様作成を開始します"
   ```

2. **Context Preparation and Agent Execution**:
   ```bash
   # 🔄 Prepare context for agent (Pattern B: Hybrid approach)
   echo "📋 コンテキスト準備とエージェント起動..."
   
   # Create context file with command arguments and additional instructions
   context_file="/workspace/.claude/context/current-command-context.json"
   
   # Get current timestamp
   current_time=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
   
   # Build context JSON with flexibility for additional instructions
   cat > "$context_file" <<EOF
   {
     "command": "create-use-case",
     "timestamp": "$current_time",
     "issue_numbers": [$(IFS=,; echo "${issue_numbers[*]}")],
     "feature_name": "$feature_name",
     "phase": "use-case-specification",
     "context": {
       "github_cli_available": $(command -v gh >/dev/null 2>&1 && echo "true" || echo "false"),
       "expected_outputs": [
         "docs/use_cases/issue-X-Y.md",
         "docs/use_cases/issue-X-Y.json"
       ]
     },
     "additional_instructions": "GitHub Issueから要件を抽出し、Given-When-Thenシナリオを作成してください。既存のdocs/use_cases/構造に従い、TDD/DDDプロセスに準拠した仕様を作成してください。",
     "special_considerations": [
       "既存のコアシナリオ（docs/use_cases/core/）との整合性確認",
       "ユビキタス言語の一貫性維持",
       "受け入れ条件の明確化"
     ],
     "custom_context": {
       "github_issue_analysis": true,
       "given_when_then_scenarios": true,
       "use_case_specification": true,
       "ubiquitous_language": true
     }
   }
   EOF
   
   echo "✅ コンテキストファイル作成完了: $context_file"
   
   # 🤖 Call the specialized agent with hybrid context
   echo ""
   echo "📋 ユースケース作成エージェントを起動します..."
   echo "専門エージェントがGitHub IssueからGiven-When-Then仕様を作成します"
   echo ""
   
   # Actual Claude Code Task tool invocation with hybrid approach
   # This will be executed by Claude Code when the command runs
   # Task tool execution with comprehensive prompt
   task_prompt="タスクを実行してください。

## コンテキスト情報の取得
1. 一時コンテキスト（プロジェクト情報）:
   - /workspace/.claude/context/current-command-context.json を読み込み

2. プロジェクト状況の確認:
   - 必要な文書やファイルを確認
   - 既存の実装や設計を参照

## 実行タスク
[03-create-use-case固有のタスクを実行]

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

   # Execute with specialized 03-create-use-case subagent
   # The 03-create-use-case subagent will be automatically invoked based on the task description
   
   agent_exit_code=$?
   echo "✅ 専用エージェント実行完了 (終了コード: $agent_exit_code)"
   
   echo "✅ エージェント呼び出し設定完了"
   echo "エージェントが以下の処理を実行します:"
   echo "  - コンテキストファイルからの引数情報取得"
   echo "  - GitHub Issueの詳細分析と要件抽出"
   echo "  - Given-When-Thenシナリオの作成とドメイン言語の確立"
   echo "  - ユースケース仕様書の生成と受け入れ条件の定義"
   echo "  - メタデータファイルの作成とフェーズ追跡の設定"
   echo "  - フィーチャーブランチの作成とプロジェクトインデックスの更新"
   ```

3. **Agent Result Verification**:
   ```bash
   # 🔍 Verify agent execution results
   echo "🔍 エージェント実行結果を検証中..."
   
   # Check that use case files were created
   echo "  🔍 ユースケース文書の作成確認中..."
   
   # Build expected file paths
   issue_list=$(IFS=-; echo "${issue_numbers[*]}")
   expected_files=()
   
   for issue_num in "${issue_numbers[@]}"; do
       # Look for use case specification files
       spec_pattern="docs/use_cases/*issue*${issue_num}*.md"
       if ls $spec_pattern 2>/dev/null | head -1 >/dev/null; then
           spec_file=$(ls $spec_pattern 2>/dev/null | head -1)
           expected_files+=("$spec_file")
           echo "    ✅ Issue #$issue_num の仕様ファイルを確認: $(basename "$spec_file")"
       else
           echo "    ❌ Issue #$issue_num の仕様ファイルが見つかりません"
       fi
       
       # Look for metadata files
       metadata_pattern="docs/use_cases/*issue*${issue_num}*.json"
       if ls $metadata_pattern 2>/dev/null | head -1 >/dev/null; then
           metadata_file=$(ls $metadata_pattern 2>/dev/null | head -1)
           expected_files+=("$metadata_file")
           echo "    ✅ Issue #$issue_num のメタデータを確認: $(basename "$metadata_file")"
       else
           echo "    ❌ Issue #$issue_num のメタデータが見つかりません"
       fi
   done
   
   # Check if use cases index was updated
   index_updated=false
   if [[ -f "docs/use_cases/index.md" ]]; then
       for issue_num in "${issue_numbers[@]}"; do
           if grep -q "#$issue_num" "docs/use_cases/index.md"; then
               index_updated=true
               break
           fi
       done
   fi
   
   # Check for feature branch (if Git is available)
   branch_created=false
   if command -v git >/dev/null 2>&1; then
       current_branch=$(git branch --show-current)
       if [[ "$current_branch" =~ feature/issue-.*-.*|issue.*feature ]]; then
           branch_created=true
           echo "    ✅ フィーチャーブランチを確認: $current_branch"
       fi
   fi
   
   # Report validation results
   if [[ ${#expected_files[@]} -eq 0 ]]; then
       echo "❌ エージェント実行検証失敗: ユースケース文書が作成されていません"
       exit 1
   fi
   
   echo "✅ エージェント実行結果検証完了"
   
   # 🔧 Load advanced task verification library
   source "$(dirname "${BASH_SOURCE[0]}")/_task_verification.sh"
   
   # ✨ New: Advanced task verification with retry capability
   echo "🔍 Critical tasks確認中..."
   if ! verify_critical_tasks "03-create-use-case" "$latest_report"; then
       echo "⚠️ Critical tasks確認で問題が検出されました - 再実行を試行します"
       prepare_retry_context "03-create-use-case" "1" "${verification_issues[@]}"
       
       # Enhanced context for retry
       echo "🔄 再実行用の強化コンテキスト準備中..."
       prepare_enhanced_context "03-create-use-case" "$context_file" "${verification_issues[@]}"
       
       echo "💡 推奨アクション: エージェントを再実行してください"
       echo "   重点項目: $(IFS='|'; echo "${verification_issues[*]}")"
       exit 1
   fi
   
   echo "✅ Critical tasks確認完了 - 全項目クリア"
   
   # Clean up context file after successful execution
   if [[ -f "$context_file" ]]; then
       # Archive context to execution history
       if [[ -f "$context_file" ]]; then
           echo "{\"timestamp\":\"$(date -Iseconds)\",\"command\":\"create-use-case\",\"issues\":\"${issue_numbers[*]}\",\"status\":\"completed\"}" >> /workspace/.claude/context/execution-history.jsonl
           rm -f "$context_file"
           echo "📝 コンテキストを実行履歴に記録し、一時ファイルをクリーンアップしました"
       fi
   fi
   ```

4. **Display Use Case Creation Success Summary**:
   ```bash
   # 📊 Display comprehensive use case creation summary
   echo ""
   echo "🎉 ユースケース仕様作成完了!"
   echo "============================================="
   
   # Show created files
   echo "📁 作成されたファイル:"
   for file in "${expected_files[@]}"; do
       if [[ -f "$file" ]]; then
           echo "   ✅ $file"
       fi
   done
   
   # Show Git integration status
   echo ""
   echo "🔗 Git統合:"
   if [[ "$branch_created" == true ]]; then
       echo "   ✅ フィーチャーブランチ: $(git branch --show-current)"
   else
       echo "   ⚠️ フィーチャーブランチ: 未確認"
   fi
   
   # Show project integration
   echo ""
   echo "📚 プロジェクト統合:"
   if [[ "$index_updated" == true ]]; then
       echo "   ✅ ユースケースインデックス: 更新済み"
   else
       echo "   ⚠️ ユースケースインデックス: 未更新"
   fi
   
   # Show next steps
   echo ""
   echo "📋 次のステップ (ドメインモデリング):"
   for issue_num in "${issue_numbers[@]}"; do
       echo "   /domain-modeling $issue_num"
   done
   
   echo ""
   echo "📚 重要ドキュメント:"
   echo "   - ユースケース仕様: docs/use_cases/"
   echo "   - プロジェクト進捗: docs/use_cases/index.md"
   if [[ ${#expected_files[@]} -gt 0 ]]; then
       echo "   - 作成された仕様: ${expected_files[0]}"
   fi
   
   echo ""
   echo "🔗 GitHub連携:"
   for issue_num in "${issue_numbers[@]}"; do
       echo "   - Issue #$issue_num: gh issue view $issue_num"
   done
   
   echo ""
   echo "✅ ユースケース仕様作成完了 - ドメインモデリング準備完了!"
   ```

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
- Always use automated metadata creation through the agent
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
$ /create-use-case 15
📋 Issues: #15 のユースケース仕様作成を開始します
📋 ユースケース作成エージェントを起動します...
✅ エージェント実行結果検証完了
🎉 ユースケース仕様作成完了!
```

### ❌ Failure Example and Fix
```bash
$ /create-use-case 999
❌ エラー: Issue #999 が見つかりません

# Fix: Use valid issue number
$ gh issue list
$ /create-use-case 15
```