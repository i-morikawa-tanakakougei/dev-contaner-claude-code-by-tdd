#!/usr/bin/env python3
"""
Create Retroactive Issue Expert Command - 改修版
緊急復旧分析からGitHub Issueを自動作成し、実行履歴を追跡
"""

import json
import os
import sys
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
import glob
import re

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))
from json_format_utils import (
    load_use_case_json,
    update_execution_history,
    save_use_case_json,
    format_execution_status
)


def find_emergency_recovery_data():
    """緊急復旧分析データを検索"""
    recovery_data = {
        "analysis_found": False,
        "report_files": [],
        "action_plan_files": [],
        "emergency_fixes": [],
        "critical_gaps": 0,
        "recovery_priority": "medium"
    }
    
    # Emergency recovery reports directory
    emergency_dir = Path("docs/emergency")
    if emergency_dir.exists():
        # 最新の分析レポートを検索
        report_files = sorted(emergency_dir.glob("emergency-recovery-report-*.md"), key=lambda f: f.stat().st_mtime, reverse=True)
        action_plan_files = sorted(emergency_dir.glob("recovery-action-plan-*.md"), key=lambda f: f.stat().st_mtime, reverse=True)
        
        if report_files:
            recovery_data["analysis_found"] = True
            recovery_data["report_files"] = [str(f) for f in report_files[:3]]  # 最新3件
            
        if action_plan_files:
            recovery_data["action_plan_files"] = [str(f) for f in action_plan_files[:3]]  # 最新3件
    
    # JSONファイルから緊急復旧データを検索
    use_cases_dir = Path("docs/use_cases")
    if use_cases_dir.exists():
        for json_file in use_cases_dir.glob("*.json"):
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                    if "emergency_recovery" in data:
                        recovery_info = data["emergency_recovery"]
                        recovery_data["analysis_found"] = True
                        recovery_data["critical_gaps"] = recovery_info.get("critical_gaps", 0)
                        recovery_data["recovery_priority"] = recovery_info.get("recovery_priority", "medium")
                        break
            except Exception:
                continue
    
    return recovery_data


def analyze_git_commits(commit_hash=None):
    """Git履歴を分析してIssue作成対象を特定"""
    commit_analysis = {
        "emergency_commits": [],
        "bypassed_commits": [],
        "changed_files": [],
        "potential_issues": []
    }
    
    try:
        if commit_hash:
            # 特定のコミットを分析
            result = subprocess.run(
                ["git", "show", "--name-only", "--format=fuller", commit_hash],
                capture_output=True,
                text=True,
                check=True
            )
            
            if result.returncode == 0:
                lines = result.stdout.split('\n')
                commit_message = ""
                changed_files = []
                
                # コミットメッセージと変更ファイルを分離
                in_files_section = False
                for line in lines:
                    if line.startswith("    "):
                        commit_message += line.strip() + " "
                    elif line and not line.startswith(("commit", "Author", "AuthorDate", "Commit", "CommitDate")) and in_files_section:
                        if not line.startswith(" "):
                            changed_files.append(line.strip())
                    elif line == "" and commit_message:
                        in_files_section = True
                
                commit_analysis["emergency_commits"].append({
                    "hash": commit_hash,
                    "message": commit_message.strip(),
                    "changed_files": changed_files
                })
        
        else:
            # 過去7日間の緊急修正を分析
            since_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
            result = subprocess.run(
                ["git", "log", f"--since={since_date}", "--oneline", "--no-merges"],
                capture_output=True,
                text=True,
                check=True
            )
            
            if result.returncode == 0:
                commits = result.stdout.strip().split('\n') if result.stdout.strip() else []
                
                emergency_keywords = ["hotfix", "emergency", "urgent", "critical", "production", "fix"]
                
                for commit_line in commits:
                    if commit_line:
                        commit_hash_short = commit_line.split(' ')[0]
                        commit_message = ' '.join(commit_line.split(' ')[1:])
                        
                        # 緊急修正の検出
                        if any(keyword in commit_message.lower() for keyword in emergency_keywords):
                            commit_analysis["emergency_commits"].append({
                                "hash": commit_hash_short,
                                "message": commit_message
                            })
    
    except subprocess.CalledProcessError as e:
        print(f"❌ Git分析エラー: {e}")
    
    return commit_analysis


def classify_potential_issues(recovery_data, commit_analysis):
    """潜在的な問題をIssueタイプ別に分類"""
    issue_classification = {
        "bug_issues": [],
        "enhancement_issues": [],
        "technical_debt_issues": [],
        "documentation_issues": [],
        "testing_issues": []
    }
    
    # 緊急修正からBugを抽出
    for commit in commit_analysis["emergency_commits"]:
        if any(keyword in commit["message"].lower() for keyword in ["fix", "bug", "error", "crash"]):
            issue_classification["bug_issues"].append({
                "title": f"Bug fix from emergency commit: {commit['message'][:50]}...",
                "description": f"Emergency fix was applied in commit {commit['hash']}:\n\n**Original commit message:** {commit['message']}\n\n**Root cause analysis needed:**\n- Why was this not caught by tests?\n- What process failed to prevent this issue?\n- How can we prevent similar issues?",
                "priority": "high",
                "commit_hash": commit["hash"],
                "labels": ["bug", "emergency-fix", "retrospective"]
            })
    
    # テストカバレッジ不足からTestingを抽出
    if recovery_data["critical_gaps"] > 0:
        issue_classification["testing_issues"].append({
            "title": f"Critical test coverage gaps identified during emergency recovery",
            "description": f"Emergency recovery analysis identified {recovery_data['critical_gaps']} critical gaps in test coverage.\n\n**Acceptance Criteria:**\n- [ ] Identify all uncovered code paths that contributed to emergency situation\n- [ ] Create comprehensive test suite for identified gaps\n- [ ] Achieve minimum 80% test coverage for critical paths\n- [ ] Implement automated coverage reporting",
            "priority": "high",
            "labels": ["testing", "technical-debt", "coverage"]
        })
    
    # ドキュメント不足からDocumentationを抽出
    if recovery_data["analysis_found"]:
        issue_classification["documentation_issues"].append({
            "title": "Update documentation based on emergency recovery findings",
            "description": f"Emergency recovery revealed documentation gaps that contributed to the incident.\n\n**Required updates:**\n- [ ] Update Given-When-Then scenarios to reflect discovered edge cases\n- [ ] Document emergency procedures and runbooks\n- [ ] Update architecture diagrams if needed\n- [ ] Create troubleshooting guides",
            "priority": "medium",
            "labels": ["documentation", "emergency-recovery"]
        })
    
    # プロセス改善からEnhancementを抽出
    if len(commit_analysis["emergency_commits"]) > 1:
        issue_classification["enhancement_issues"].append({
            "title": "Improve development process to prevent emergency fixes",
            "description": f"Multiple emergency fixes ({len(commit_analysis['emergency_commits'])}) were required, indicating process improvement opportunities.\n\n**Proposed enhancements:**\n- [ ] Strengthen pre-commit hooks and CI/CD pipeline\n- [ ] Implement better monitoring and alerting\n- [ ] Add automated regression testing\n- [ ] Improve code review process",
            "priority": "medium",
            "labels": ["enhancement", "process-improvement", "devops"]
        })
    
    # 技術的負債からTechnical Debtを抽出
    if recovery_data["recovery_priority"] in ["critical", "high"]:
        issue_classification["technical_debt_issues"].append({
            "title": f"Address technical debt accumulated during emergency response",
            "description": f"Emergency recovery process with {recovery_data['recovery_priority']} priority indicates accumulated technical debt.\n\n**Debt categories to address:**\n- [ ] Quick fixes that need proper implementation\n- [ ] Temporarily disabled features or safeguards\n- [ ] Code quality issues introduced under time pressure\n- [ ] Architecture compromises made for quick resolution",
            "priority": "medium",
            "labels": ["technical-debt", "refactoring", "code-quality"]
        })
    
    return issue_classification


def create_github_issues(issue_classification):
    """GitHub Issueを実際に作成"""
    created_issues = []
    
    try:
        for issue_type, issues in issue_classification.items():
            for issue_data in issues:
                # GitHub CLI を使用してIssueを作成
                labels_str = ",".join(issue_data.get("labels", []))
                
                # Create issue using gh command
                cmd = [
                    "gh", "issue", "create",
                    "--title", issue_data["title"],
                    "--body", issue_data["description"]
                ]
                
                if labels_str:
                    cmd.extend(["--label", labels_str])
                
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True
                )
                
                if result.returncode == 0:
                    # Extract issue URL and number from output
                    issue_url = result.stdout.strip()
                    issue_number = issue_url.split('/')[-1] if '/' in issue_url else "unknown"
                    
                    created_issue = {
                        "issue_number": issue_number,
                        "title": issue_data["title"],
                        "type": issue_type.replace("_issues", ""),
                        "priority": issue_data.get("priority", "medium"),
                        "url": issue_url,
                        "labels": issue_data.get("labels", [])
                    }
                    created_issues.append(created_issue)
                    
                    print(f"✅ Created {issue_type.replace('_issues', '')} issue #{issue_number}: {issue_data['title'][:50]}...")
                
                else:
                    print(f"❌ Failed to create issue: {issue_data['title'][:50]}...")
                    print(f"Error: {result.stderr}")
    
    except Exception as e:
        print(f"❌ GitHub Issue作成エラー: {e}")
    
    return created_issues


def generate_issue_creation_report(created_issues, recovery_data, commit_analysis):
    """Issue作成レポートを生成"""
    issues_dir = Path("docs/issues")
    issues_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = issues_dir / f"retroactive-issues-{timestamp}.md"
    
    # 統計データの計算
    issues_by_type = {}
    issues_by_priority = {}
    
    for issue in created_issues:
        issue_type = issue["type"]
        priority = issue["priority"]
        
        issues_by_type[issue_type] = issues_by_type.get(issue_type, 0) + 1
        issues_by_priority[priority] = issues_by_priority.get(priority, 0) + 1
    
    report_content = f"""# 緊急復旧Issue作成レポート

## 基本情報
- **作成日時**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
- **作成Issue数**: {len(created_issues)}個
- **分析対象**: 緊急復旧分析結果とGit履歴

## 作成Issue統計

### タイプ別分布
"""
    
    for issue_type, count in issues_by_type.items():
        report_content += f"- **{issue_type.title()}**: {count}個\n"
    
    report_content += f"""

### 優先度別分布
"""
    
    for priority, count in issues_by_priority.items():
        report_content += f"- **{priority.title()}**: {count}個\n"
    
    report_content += f"""

## 作成されたIssue一覧

"""
    
    for issue in created_issues:
        report_content += f"""### Issue #{issue['issue_number']}: {issue['title']}
- **タイプ**: {issue['type']}
- **優先度**: {issue['priority']}
- **ラベル**: {', '.join(issue['labels'])}
- **URL**: {issue['url']}

"""
    
    report_content += f"""## 分析サマリー

### 緊急復旧分析結果
- **分析データ発見**: {'Yes' if recovery_data['analysis_found'] else 'No'}
- **Critical Gap数**: {recovery_data['critical_gaps']}
- **復旧優先度**: {recovery_data['recovery_priority']}

### Git履歴分析結果
- **緊急修正コミット**: {len(commit_analysis['emergency_commits'])}個
- **標準プロセス迂回**: {len(commit_analysis['bypassed_commits'])}個

### 緊急修正コミット詳細
"""
    
    for commit in commit_analysis["emergency_commits"]:
        report_content += f"- `{commit['hash']}`: {commit['message']}\n"
    
    report_content += f"""

## 推奨次ステップ

### 即座実行
1. `/sync-documentation` - 文書同期でIssue内容を反映
2. 作成されたIssueのレビューと優先順位の確認

### 短期対応
1. High優先度Issue（{issues_by_priority.get('high', 0)}個）の実装計画策定
2. Bug修正Issue（{issues_by_type.get('bug', 0)}個）の根本原因分析

### 中長期対応
1. Technical DebtとEnhancementIssueの計画的実行
2. プロセス改善の段階的適用

## メタデータ
- **レポートファイル**: {report_file}
- **関連緊急復旧レポート**: {', '.join(recovery_data['report_files'])}
- **関連アクションプラン**: {', '.join(recovery_data['action_plan_files'])}
"""
    
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    return str(report_file)


def find_most_recent_json():
    """最新のユースケースJSONファイルを検索"""
    use_cases_dir = Path("docs/use_cases")
    
    if not use_cases_dir.exists():
        return None
    
    # JSONファイルを最新順でソート
    json_files = list(use_cases_dir.glob("issue-*.json"))
    if not json_files:
        return None
    
    # 最新の更新時刻のファイルを返す
    latest_file = max(json_files, key=lambda f: f.stat().st_mtime)
    return str(latest_file)


def main():
    """メイン処理"""
    
    # 引数チェック（コミットハッシュまたは分析モードは任意）
    commit_hash_or_mode = sys.argv[1] if len(sys.argv) > 1 else None
    
    if commit_hash_or_mode:
        print(f"\n📝 特定コンテキストでの緊急復旧Issue作成: {commit_hash_or_mode}\n")
    else:
        print(f"\n📝 自動分析モードでの緊急復旧Issue作成を開始します\n")
    
    # 緊急復旧データを検索
    print("🔍 緊急復旧分析データを検索中...")
    recovery_data = find_emergency_recovery_data()
    
    if recovery_data["analysis_found"]:
        print(f"✅ 緊急復旧分析データを発見")
        print(f"📊 Critical Gap数: {recovery_data['critical_gaps']}")
        print(f"⚡ 復旧優先度: {recovery_data['recovery_priority']}")
    else:
        print("⚠️ 緊急復旧分析データが見つかりません - Git履歴から分析します")
    
    # Git履歴分析
    print("\n📊 Git履歴分析中...")
    commit_analysis = analyze_git_commits(commit_hash_or_mode)
    
    print(f"✅ 緊急修正コミット: {len(commit_analysis['emergency_commits'])}個検出")
    
    # Issue分類
    print("\n🏷️ 潜在的Issue分類中...")
    issue_classification = classify_potential_issues(recovery_data, commit_analysis)
    
    total_potential_issues = sum(len(issues) for issues in issue_classification.values())
    print(f"✅ 潜在的Issue: {total_potential_issues}個特定")
    
    # GitHub Issue作成
    print("\n📝 GitHub Issue作成中...")
    created_issues = create_github_issues(issue_classification)
    
    # レポート生成
    print("\n📊 Issue作成レポート生成中...")
    report_file = generate_issue_creation_report(created_issues, recovery_data, commit_analysis)
    
    # JSON更新（最新のJSONファイルを使用）
    json_file_path = find_most_recent_json()
    if json_file_path:
        print(f"✅ JSONファイル: {json_file_path}")
        
        try:
            use_case_data = load_use_case_json(json_file_path)
            
            # Issue統計の計算
            issues_by_type = {}
            issues_by_priority = {}
            
            for issue in created_issues:
                issue_type = issue["type"]
                priority = issue["priority"]
                issues_by_type[issue_type] = issues_by_type.get(issue_type, 0) + 1
                issues_by_priority[priority] = issues_by_priority.get(priority, 0) + 1
            
            # 緊急復旧Issue情報を更新
            retroactive_issues = {
                "creation_completed_at": datetime.now().isoformat(),
                "status": "SUCCESS" if created_issues else "PARTIAL",
                "total_issues_created": len(created_issues),
                "issues_by_type": issues_by_type,
                "issues_by_priority": issues_by_priority,
                "created_issues": created_issues,
                "report_file": report_file,
                "next_actions": ["/sync-documentation", "/create-tests"]
            }
            
            use_case_data["retroactive_issues"] = retroactive_issues
            save_use_case_json(json_file_path, use_case_data)
            
            # 実行履歴を更新
            command = f"/create-retroactive-issue {commit_hash_or_mode}" if commit_hash_or_mode else "/create-retroactive-issue"
            affected_files = [report_file] + [issue["url"] for issue in created_issues]
            
            update_execution_history(
                json_file_path,
                command,
                "success",
                affected_files
            )
            
            # 更新されたデータを読み込み
            updated_data = load_use_case_json(json_file_path)
            
            # 実行状況を表示
            print("\n" + "="*60)
            print(format_execution_status(updated_data))
            print("="*60)
        
        except Exception as e:
            print(f"⚠️ JSON更新エラー: {e}")
    else:
        print("⚠️ JSONファイルが見つかりません（Issue作成は継続）")
    
    # 結果サマリー表示
    print(f"\n📝 緊急復旧Issue作成結果")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"🎯 ステータス: {'SUCCESS' if created_issues else 'PARTIAL'}")
    print(f"📊 作成Issue総数: {len(created_issues)}個")
    print(f"🔍 分析ソース: {'緊急復旧データ + Git履歴' if recovery_data['analysis_found'] else 'Git履歴のみ'}")
    
    if created_issues:
        print(f"\n📁 成果物")
        print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"✅ {report_file}")
        for issue in created_issues[:5]:  # 最大5件表示
            print(f"✅ Issue #{issue['issue_number']}: {issue['title'][:50]}...")
    
    if len(created_issues) > 0:
        # Issue種別分布
        issues_by_type = {}
        issues_by_priority = {}
        for issue in created_issues:
            issue_type = issue["type"]
            priority = issue["priority"]
            issues_by_type[issue_type] = issues_by_type.get(issue_type, 0) + 1
            issues_by_priority[priority] = issues_by_priority.get(priority, 0) + 1
        
        print(f"\n📋 Issue分布")
        print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"🐛 Bug: {issues_by_type.get('bug', 0)}個")
        print(f"🔧 Enhancement: {issues_by_type.get('enhancement', 0)}個")
        print(f"⚙️ Technical Debt: {issues_by_type.get('technical_debt', 0)}個")
        print(f"📚 Documentation: {issues_by_type.get('documentation', 0)}個")
        print(f"🧪 Testing: {issues_by_type.get('testing', 0)}個")
        
        print(f"\n⚡ 優先度分布")
        print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"🔴 High: {issues_by_priority.get('high', 0)}個")
        print(f"🟡 Medium: {issues_by_priority.get('medium', 0)}個")
        print(f"🟢 Low: {issues_by_priority.get('low', 0)}個")
    
    print(f"\n⏭️ 次の推奨コマンド")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    if created_issues:
        high_priority_count = sum(1 for issue in created_issues if issue["priority"] == "high")
        if high_priority_count > 0:
            print(f"🔴 High優先度Issue {high_priority_count}個が作成されました:")
            print(f"   /sync-documentation")
            print(f"   → ドキュメント同期でIssue内容を反映")
            print(f"   /create-use-case [issue-number]")
            print(f"   → High優先度Issueの仕様作成開始")
        else:
            print(f"✅ Issue作成完了 - 次の標準ステップ:")
            print(f"   /sync-documentation")
            print(f"   → ドキュメント同期")
            print(f"   /review-issue")
            print(f"   → 作成されたIssueのレビュー")
    else:
        print(f"⚠️ Issue作成がスキップされました:")
        print(f"   /emergency-recovery")
        print(f"   → 緊急復旧分析の再実行")
        print(f"   または手動でのIssue作成を検討")
    
    # 最終メッセージ
    status_emoji = {"SUCCESS": "✅", "PARTIAL": "⚠️", "FAILED": "❌"}
    emoji = status_emoji.get("SUCCESS" if created_issues else "PARTIAL", "❓")
    
    print(f"\n{emoji} 緊急復旧Issue作成完了")
    print(f"詳細なレポートは {report_file} に記録されました。")


if __name__ == "__main__":
    main()