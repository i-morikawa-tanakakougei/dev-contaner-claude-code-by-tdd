Use the 99-2-create-retroactive-issue subagent to create GitHub issues for emergency fixes that bypassed standard workflow. This command MUST USE PROACTIVELY the specialized 99-2-create-retroactive-issue subagent for optimal retroactive issue creation.

**📖 Required Reading**: Before execution, this command MUST read the following files:
- `/workspace/.claude/context/current-command-context.json` - Current execution context
- `/workspace/.claude/context/project-context.json` - Overall project state and active sprint information
- `/workspace/docs/metadata/project-state.json` - Integrated project status for update

## Metadata
- **Prerequisites**: Git repository with emergency commits that need corresponding GitHub issues
- **Input**: 
  - **コミット指定** (相互排他、いずれか必須):
    - `--commit <commit-hash>` - 特定のコミット（単一）のみを分析対象とする
    - `--since <commit-hash>` - 指定コミット以降（含まない）の全コミット
    - `--from <commit-hash>` - 指定コミット以降（含む）の全コミット  
    - `--range <start>..<end>` - Git範囲指定（start含まない、end含む）
    - `--last <number>` - 最新N個のコミット
  - `--type <bug|hotfix|emergency>` (default: emergency) - Type of emergency fix
  - `--strategy <individual|consolidated|interactive>` (default: individual) - 複数コミット処理戦略
  - `--update` (optional) - 既存Issueの更新。新規作成の代わりに同一コミットの既存Issue情報を更新
- **Output**: 
  - GitHub issues created/updated (単一または複数) with proper labels and content
  - Issues linked to specific commits and related PRs
  - Updated project tracking metadata
- **Dependencies**: GitHub repository access, git history
- **Execution Timing**: After emergency recovery analysis (99-1) and before documentation sync

## 🎯 **TDD/DDD/LAYERED PROCESS CONTEXT**

**🚨 Emergency Recovery Workflow**: Recovery(99-1) → **Issue Creation(99-2)** → Sync Docs(99-3) → Retroactive Tests(99-4) → Validation(99-5) → Metadata Reconcile(99-6) → Final Review(99-7)

**🏗️ Issue Creation Architecture**: Analyze→Extract→Generate→Link  
**📋 Issue Requirements**: Commit analysis, business context extraction, proper GitHub integration
**🔄 Integration**: Links emergency fixes to standard issue tracking for future workflow compliance

> 📖 **Emergency Recovery System**: [99-X Series Commands](./README.md)  
> 🗺️ **Current Position**: Retroactive Issue Creation (99-2/99-7)  
> 🎯 **Phase Purpose**: Create GitHub issues for emergency fixes to restore traceability  
> ➡️ **Next Stage**: 99-3-sync-documentation (Documentation Sync)

## 🎯 **PHASE PURPOSE: RETROACTIVE ISSUE CREATION**

**⚠️ Important Notice:**
- **This step is ISSUE CREATION ONLY** - Generate GitHub issues for emergency commits
- **NO CODE CHANGES** - Focus on creating proper issue tracking and documentation  
- **Traceability restoration phase** - Link emergency fixes to proper issue management
- **Create GitHub artifacts ONLY** - Establish proper tracking for emergency changes

**What this step does:**
1. `99-1-emergency-recovery` ← Emergency fix analysis and recovery planning
2. `99-2-create-retroactive-issue` ← **【YOU ARE HERE】GitHub issue creation for emergency fixes**
3. `99-3-sync-documentation` ← Documentation synchronization with changes
4. Then continue with test creation and validation cycle

**CREATE GITHUB ISSUES ONLY.**

## Common Errors and Solutions

### ❌ Error Case 1: Commit hash not found
**Cause**: Provided commit hash doesn't exist in current repository  
**Solution**: 
- Verify commit hash: `git show <commit-hash>`
- Check if you're on correct branch: `git log --oneline`
- Use full commit hash instead of abbreviated version

### ❌ Error Case 2: GitHub API access denied
**Cause**: Missing or invalid GitHub authentication  
**Solution**: 
```bash
# Set up GitHub CLI authentication
gh auth login
# Or set GitHub token
export GITHUB_TOKEN=<your-token>
```

### ❌ Error Case 3: Issue already exists for commit
**Cause**: GitHub issue already linked to this commit  
**Solution**: 
```bash
# Check existing issues
gh issue list --search "commit:<commit-hash>"
# Update existing issue instead of creating new one
/create-retroactive-issue --commit <hash> --update
```

## Execution Examples

### ✅ Success Example - Bug Fix Issue
```bash
$ /create-retroactive-issue --commit a1b2c3d --type bug
📝 事後Issue作成を開始します

🔍 コミット分析中...
  コミット: a1b2c3d
  メッセージ: "Fix payment validation null pointer exception"
  変更ファイル: src/payment/validator.py (12行追加, 3行削除)
  日時: 2024-08-28 14:30:15

📋 Issue内容生成中...
  タイプ: Bug Fix
  影響範囲: Payment Processing
  優先度: High (本番障害対応)

🎫 GitHub Issue作成中...
  ✅ Issue #342 作成完了: "Emergency Fix: Payment validation null pointer exception"
  📎 ラベル付与: bug, emergency-fix, payment
  🔗 コミット紐づけ: a1b2c3d
  📅 マイルストーン: Current Sprint

📊 プロジェクト追跡情報更新中...
  ✅ project-state.json 更新
  ✅ GitHub issue tracking 更新

🎉 事後Issue作成完了!
作成されたIssue: #342
URL: https://github.com/yourorg/yourrepo/issues/342

次のステップ: /sync-documentation 342 --type all
```

### ✅ Success Example - Hotfix Issue
```bash
$ /create-retroactive-issue --commit b2c3d4e --type hotfix
📝 緊急修正用Issue作成を開始します

🔍 コミット詳細分析中...
  コミット: b2c3d4e
  メッセージ: "Hotfix: Resolve database connection timeout"
  変更範囲: Infrastructure layer (database configuration)
  緊急度: Critical

📝 Issue詳細情報:
  タイトル: "Hotfix: Database connection timeout resolution"
  説明: 本番環境でのデータベース接続タイムアウト問題の緊急修正
  影響: システム全体の可用性
  修正内容: 接続プール設定の調整

🎫 GitHub Issue作成...
  ✅ Issue #343 作成
  🏷️ ラベル: hotfix, infrastructure, critical
  🔗 関連コミット: b2c3d4e
  👥 担当者自動割当済み

✅ 作成完了! 次は文書同期をお勧めします。
```

### ✅ Update Mode Example - 既存Issue更新
```bash
# Step 1: 既存Issueの確認
$ gh issue list --search "commit:a1b2c3d"
#123 Emergency: Payment fix (linked to a1b2c3d)

# Step 2: 既存Issue更新実行
$ /create-retroactive-issue --commit a1b2c3d --update
📝 既存Issue更新を開始します

🔍 既存Issue検出中...
  Issue #123: "Emergency: Payment fix"
  現在のラベル: emergency
  リンクされたコミット: a1b2c3d
  作成日時: 2024-08-28 10:30:00

📝 Issue情報更新中...
  ✅ タイプ更新: emergency → bug (より適切な分類)
  ✅ 詳細説明追加: コミット分析結果を反映
  ✅ ラベル付与: bug, payment, critical
  ✅ マイルストーン設定: Current Sprint

🎫 GitHub Issue更新完了...
  ✅ Issue #123 更新完了
  🏷️ 最新ラベル: bug, payment, critical
  📝 説明文改善済み
  🔗 コミット詳細分析済み

🎉 既存Issue更新完了!
更新されたIssue: #123
URL: https://github.com/yourorg/yourrepo/issues/123

次のステップ: /sync-documentation 123 --type all
```

### ✅ Range Specification Examples - 範囲指定実行例

#### **Example 1: Since指定 - 特定コミット以降**
```bash
# 状況: hotfix-start以降の全コミットに対してIssue作成
$ git log --oneline
def456 Fix database timeout settings
abc123 Add connection retry logic  
hotfix-start Initial hotfix commit
...

$ /create-retroactive-issue --since hotfix-start --strategy individual
📝 範囲指定Issue作成を開始します (since mode)

🔍 対象コミット分析中...
  基準コミット: hotfix-start (含まない)
  対象範囲: hotfix-start..HEAD
  検出コミット数: 2件
  
📋 対象コミット一覧:
  1. abc123: "Add connection retry logic"
  2. def456: "Fix database timeout settings"

🎫 個別Issue作成中...
  ✅ Issue #345 作成: "Add connection retry logic" (abc123)
  ✅ Issue #346 作成: "Fix database timeout settings" (def456)

🎉 範囲指定Issue作成完了!
作成されたIssue: #345, #346
次のステップ: 各Issueに対して /sync-documentation 実行
```

#### **Example 2: Range指定 - Git範囲指定**
```bash
$ /create-retroactive-issue --range hotfix-start..release-branch --strategy consolidated
📝 範囲指定Issue作成を開始します (range mode)

🔍 Git範囲分析中...
  範囲: hotfix-start..release-branch
  対象コミット数: 5件
  変更ファイル数: 12件
  影響レイヤー: Infrastructure, Domain

📝 統合Issue生成中...
  タイトル: "Emergency Database Stability Improvements"
  説明: hotfix-startからrelease-branchまでの包括的な修正
  
🎫 統合Issue作成...
  ✅ Issue #347 作成
  🏷️ ラベル: emergency, infrastructure, database
  🔗 関連コミット: 5件すべてリンク済み
  📊 影響評価: Critical database stability fixes

🎉 統合Issue作成完了!
作成されたIssue: #347 (5コミット統合)
```

#### **Example 3: Last指定 - 最新コミット**
```bash
$ /create-retroactive-issue --last 3 --strategy interactive
📝 最新コミット範囲Issue作成 (interactive mode)

🔍 最新3コミット分析中...
  1. ghi789: "Update error handling in payment service"
  2. def456: "Fix null pointer in validation"  
  3. abc123: "Add logging to database connection"

🎯 インタラクティブ選択:
  
  コミット 1/3: abc123 "Add logging to database connection"
  種別候補: [emergency] (recommended: bug)
  アクション: [c]reate Issue / [s]kip / [u]pdate existing
  選択: c
  ✅ Issue #348 作成予定
  
  コミット 2/3: def456 "Fix null pointer in validation"  
  種別候補: [emergency] (recommended: bug)
  アクション: [c]reate Issue / [s]kip / [u]pdate existing
  選択: c
  ✅ Issue #349 作成予定
  
  コミット 3/3: ghi789 "Update error handling in payment service"
  種別候補: [emergency] (recommended: hotfix)
  アクション: [c]reate Issue / [s]kip / [u]pdate existing  
  選択: s
  ⏭️ スキップ

🎫 選択されたIssue作成実行中...
  ✅ Issue #348 作成完了
  ✅ Issue #349 作成完了

🎉 インタラクティブIssue作成完了!
作成: 2件、スキップ: 1件
```

## 📋 **コミット処理仕様**

### **処理対象の明確化**

#### **単一コミット処理 (`--commit`)**
- **対象**: 指定された`--commit <hash>`の**単一コミットのみ**
- **範囲**: コミットに含まれる全ての変更ファイル
- **分析**: コミットメッセージ、変更差分、影響範囲、ビジネスコンテキスト

#### **範囲指定処理 (`--since`, `--from`, `--range`, `--last`)**
- **対象**: 指定範囲内の**複数コミット**
- **範囲**: 各コミットの変更ファイル + 全体の影響評価
- **分析**: 個別コミット分析 + 範囲全体の一貫性評価

### **範囲指定パラメータ詳細**

| パラメータ | 説明 | Git相当 | 基準コミット含む |
|-----------|------|---------|----------------|
| `--since <hash>` | 指定コミット以降 | `<hash>..HEAD` | ❌ 含まない |
| `--from <hash>` | 指定コミット以降 | `<hash>~1..HEAD` | ✅ 含む |
| `--range <start>..<end>` | Git範囲指定 | `<start>..<end>` | start❌, end✅ |
| `--last <number>` | 最新N個 | `HEAD~<N>..HEAD` | 最新から数える |

### **処理戦略の選択**

#### **individual戦略 (default)**
```bash
# 各コミットに個別Issue作成
/create-retroactive-issue --since hotfix-start --strategy individual
# 結果: コミット数分のIssueが作成される
```

#### **consolidated戦略**
```bash
# 複数コミットを1つのIssueに統合
/create-retroactive-issue --range abc123..def456 --strategy consolidated
# 結果: 1つの包括的なIssueが作成される（全コミットリンク）
```

#### **interactive戦略**
```bash
# コミット毎に作成/スキップ選択
/create-retroactive-issue --last 5 --strategy interactive
# 結果: ユーザー選択に基づいてIssue作成
```

### **従来の複数コミット処理パターン（互換性維持）**
```bash
# 従来方式（個別実行）も継続サポート
/create-retroactive-issue --commit abc123 --type bug
/create-retroactive-issue --commit def456 --type hotfix  
/create-retroactive-issue --commit ghi789 --type emergency
```

### **--updateモードの使用ケース**
1. **重複Issue防止**: 同じコミットに対して既にIssueが存在する場合
2. **情報補完**: 緊急対応時に作成した簡易Issueに詳細情報を追加
3. **分類見直し**: Issue タイプやラベルの再分類が必要な場合
4. **GitHub API制限回避**: 新規Issue作成限度回避のための更新利用

## 📋 **RETROACTIVE ISSUE CREATION TASK CHECKLIST**

**Use this checklist for comprehensive retroactive issue creation:**

### 🔴 Required Tasks

#### **🔍 Commit Analysis**
- [ ] **Commit validation**: Verify commit exists and is accessible
- [ ] **Change analysis**: Extract changed files, lines, and impact scope
- [ ] **Message parsing**: Analyze commit message for business context

#### **📝 Issue Content Generation**
- [ ] **Title creation**: Generate clear, descriptive issue title
- [ ] **Description writing**: Create detailed issue description with context
- [ ] **Business impact assessment**: Document why this emergency fix was necessary

#### **🎫 GitHub Issue Creation**
- [ ] **Issue creation**: Create GitHub issue with generated content
- [ ] **Label application**: Apply appropriate labels (bug, hotfix, emergency-fix, etc.)
- [ ] **Commit linkage**: Link issue to the emergency commit

### 🟡 Recommended Tasks

#### **📊 Project Integration**
- [ ] **Milestone assignment**: Assign to current or appropriate milestone
- [ ] **Assignee setting**: Set appropriate team member as assignee
- [ ] **Project board**: Add to relevant project board if exists

#### **🔗 Cross-Reference Linking**
- [ ] **PR linking**: Link to related pull request if exists
- [ ] **Related issues**: Link to any related existing issues
- [ ] **Documentation references**: Reference relevant documentation

### 🟢 Optional Tasks

#### **📈 Enhancement Features**
- [ ] **Priority assessment**: Set appropriate priority level
- [ ] **Epic linking**: Link to parent epic if applicable
- [ ] **Template application**: Use issue templates if configured

#### **📊 Tracking and Metrics**
- [ ] **Time tracking**: Estimate time spent on emergency fix
- [ ] **Impact metrics**: Document performance or availability impact
- [ ] **Follow-up tasks**: Create tasks for proper implementation in future

**💡 Pro Tip**: Use specific commit hashes and include business context in issue descriptions!

## Task Details

**🤖 Agent Integration**: This command MUST USE PROACTIVELY the specialized `99-2-create-retroactive-issue` subagent for optimal retroactive issue creation. Claude Code should automatically delegate this task to the 99-2-create-retroactive-issue subagent based on the command description.

## 📖 Subagent Document Reading Instructions

This command delegates to the specialized `99-2-create-retroactive-issue` subagent.

**MANDATORY: The subagent MUST read these files before execution:**

1. `.git/log` - Git commit history for commit analysis
2. `docs/vision/project-vision.md` - Project context for business alignment (if exists)
3. `docs/use_cases/` - Current scenario documentation for impact assessment
4. `/workspace/.claude/context/current-command-context.json` - Current execution context
5. `/workspace/docs/metadata/project-state.json` - Project status and issue tracking
6. `.github/ISSUE_TEMPLATE/` - GitHub issue templates (if exists)

**Command-Specific Reading Focus - Retroactive Issue Creation:**
- Read git commit details for comprehensive change analysis
- Review project documentation to understand business context
- Check existing issue templates for consistent formatting
- Analyze current project state for proper milestone and assignee selection

**CRITICAL:** Use the Read tool to actually read file contents, not just reference paths.

## サブエージェント実行指示

このコマンドはサブエージェント `99-2-create-retroactive-issue` を呼び出します。

**サブエージェントに対する明示的指示**:
- 実行開始前に以下のファイルを必ず読み込んでください:
  1. Gitログと指定コミットの詳細情報
  2. プロジェクトドキュメント - ビジネスコンテキストの理解
  3. `/workspace/docs/metadata/project-state.json` - プロジェクト状態確認
  4. `/workspace/.claude/context/current-command-context.json` - 実行コンテキスト確認
  
**重要**: リンクや参照だけでなく、実際にRead toolを使用してファイル内容を読み込むこと

Follow these steps:

1. **Pre-execution Validation**:
   ```bash
   # Validate required parameters
   commit_hash=""
   issue_type="emergency"
   update_mode=false
   
   while [[ $# -gt 0 ]]; do
       case $1 in
           --commit)
               commit_hash="$2"
               shift 2
               ;;
           --type)
               issue_type="$2"
               shift 2
               ;;
           --update)
               update_mode=true
               shift
               ;;
           *)
               echo "⚠️ Unknown parameter: $1"
               echo "Usage: /create-retroactive-issue --commit <hash> [--type bug|hotfix|emergency] [--update]"
               exit 1
               ;;
       esac
   done
   
   # Validate required commit hash
   if [[ -z "$commit_hash" ]]; then
       echo "❌ Commit hash is required"
       echo "Usage: /create-retroactive-issue --commit <hash> [--type bug|hotfix|emergency]"
       exit 1
   fi
   
   # Validate git repository and commit
   if ! git rev-parse --git-dir >/dev/null 2>&1; then
       echo "❌ Git repository not found"
       exit 1
   fi
   
   if ! git cat-file -e "$commit_hash" 2>/dev/null; then
       echo "❌ Commit hash not found: $commit_hash"
       echo "💡 利用可能な最近のコミット:"
       git log --oneline -5
       exit 1
   fi
   
   # Validate issue type
   if [[ "$issue_type" != "bug" && "$issue_type" != "hotfix" && "$issue_type" != "emergency" ]]; then
       echo "❌ Invalid issue type: $issue_type. Must be 'bug', 'hotfix', or 'emergency'"
       exit 1
   fi
   
   echo "📝 事後Issue作成を開始します (タイプ: $issue_type)"
   ```

2. **Context Preparation and Agent Execution**:
   ```bash
   # 🔄 Prepare context for retroactive issue creation agent
   echo "🔍 コミット分析とIssue作成コンテキスト準備..."
   
   # Extract commit information
   commit_subject=$(git log -1 --pretty=format:"%s" "$commit_hash")
   commit_body=$(git log -1 --pretty=format:"%b" "$commit_hash")
   commit_author=$(git log -1 --pretty=format:"%an" "$commit_hash")
   commit_date=$(git log -1 --pretty=format:"%ci" "$commit_hash")
   
   # Get changed files
   changed_files=$(git diff-tree --no-commit-id --name-only -r "$commit_hash" | head -10)
   
   # Create context file
   context_file="/workspace/.claude/context/current-command-context.json"
   current_time=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
   
   # Build context JSON for retroactive issue creation
   cat > "$context_file" <<EOF
   {
     "command": "create-retroactive-issue",
     "timestamp": "$current_time",
     "commit_hash": "$commit_hash",
     "issue_type": "$issue_type",
     "update_mode": $update_mode,
     "phase": "retroactive-issue-creation",
     "commit_info": {
       "subject": "$commit_subject",
       "body": "$commit_body",
       "author": "$commit_author",
       "date": "$commit_date",
       "changed_files": "$changed_files"
     },
     "context": {
       "git_repo": "true",
       "github_integration": "required",
       "expected_outputs": [
         "github_issue_created",
         "project_metadata_updated"
       ]
     },
     "additional_instructions": "緊急修正コミットの内容を分析し、適切なGitHub Issueを作成してトレーサビリティを回復してください。",
     "special_considerations": [
       "コミット内容の詳細分析",
       "ビジネスコンテキストの抽出", 
       "適切なラベリングとマイルストーン設定",
       "関連PRとの紐づけ",
       "プロジェクト追跡情報の更新"
     ],
     "custom_context": {
       "emergency_recovery": true,
       "github_integration": "required",
       "traceability_focus": "high"
     }
   }
   EOF
   
   echo "✅ 事後Issue作成コンテキストファイル作成完了: $context_file"
   
   # 🤖 Call the specialized retroactive issue creation agent
   echo ""
   echo "🎫 事後Issue作成エージェントを起動します..."
   echo "専門エージェントがコミットを分析してGitHub Issueを作成します"
   echo ""
   ```

3. **Agent Result Verification**:
   ```bash
   # 🔍 Verify retroactive issue creation results
   echo "🔍 Issue作成結果を検証中..."
   
   # Check GitHub CLI is available
   if ! command -v gh &> /dev/null; then
       echo "⚠️ GitHub CLI (gh) が見つかりません。手動でのIssue確認が必要です。"
   else
       echo "✅ GitHub CLI利用可能"
   fi
   
   echo "✅ 事後Issue作成結果検証完了"
   
   # Clean up context file after successful execution
   if [[ -f "$context_file" ]]; then
       # Archive context to execution history
       echo "{\"timestamp\":\"$(date -Iseconds)\",\"command\":\"create-retroactive-issue\",\"commit\":\"$commit_hash\",\"type\":\"$issue_type\",\"status\":\"completed\"}" >> /workspace/.claude/context/execution-history.jsonl
       rm -f "$context_file"
       echo "📝 コンテキストを実行履歴に記録し、一時ファイルをクリーンアップしました"
   fi
   ```

4. **Display Issue Creation Summary**:
   ```bash
   # 📊 Display comprehensive issue creation summary
   echo ""
   echo "🎉 事後Issue作成完了!"
   echo "========================="
   
   echo "📋 作成したIssue情報:"
   echo "   🎫 コミット: $commit_hash"
   echo "   📝 件名: $commit_subject"
   echo "   🏷️ タイプ: $issue_type"
   echo "   👤 作成者: $commit_author"
   echo "   📅 日付: $commit_date"
   
   if [[ -n "$changed_files" ]]; then
       echo ""
       echo "📁 変更ファイル:"
       echo "$changed_files" | while read -r file; do
           echo "   📄 $file"
       done
   fi
   
   echo ""
   echo "📋 推奨次のステップ:"
   echo "   1. ドキュメント同期: /sync-documentation <issue-number> --type all"
   echo "   2. テスト作成: /retroactive-test <issue-number>"
   echo "   3. Issue確認: GitHub上で作成されたIssueを確認"
   
   echo ""
   echo "💡 補足情報:"
   echo "   - GitHub上でIssueの詳細を確認してください"
   echo "   - 必要に応じてIssue説明やラベルを追加編集してください"
   echo "   - 関連するPRがある場合は手動でリンクしてください"
   echo ""
   echo "✅ 事後Issue作成完了 - GitHub Issueが作成されました!"
   ```

## 🔄 **PHASE 3: ENHANCED INTEGRATION CAPABILITIES**

### **Critical Enhancement Features**
This command implements Phase 3 advanced retroactive issue creation capabilities:

1. **Intelligent Commit Analysis with Business Context Extraction**
2. **Automated Issue Content Generation with Template Integration** 
3. **Smart Label and Milestone Assignment based on Change Impact**
4. **Enhanced GitHub Integration with Cross-Reference Linking**

### **Project State Updates**

**CRITICAL**: After successful retroactive issue creation, MUST update integrated project metadata:

1. **Project State Update**:
   ```bash
   # Update docs/metadata/project-state.json
   # - Add created issue to issue_tracking.emergency_issues
   # - Update project_metadata.github_integration stats
   # - Increment workflow_statistics.retroactive_issues_created
   # - Add to recent_activity.last_command_executed
   ```

2. **Project Context Update**:
   ```bash
   # Update .claude/context/project-context.json  
   # - Add issue_tracking.emergency_recovery_issues entry
   # - Update current_state.last_command and last_command_timestamp
   # - Increment workflow_tracking.command_usage.create_retroactive_issue
   ```

**⚠️ Error Handling**: If retroactive issue creation fails:
- 📖 Consult: [Manual Sync Guide](../../docs/maintenance/manual-sync-guide.md)
- 🔄 Check Status: `/use-case-status` for current project state  
- 🎫 Manual Creation: Create GitHub issue manually and update project metadata