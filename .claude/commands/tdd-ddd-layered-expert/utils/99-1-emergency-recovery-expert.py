#!/usr/bin/env python3
"""
Emergency Recovery Expert Command - 改修版
緊急修正の分析と復旧計画を作成し、実行履歴を追跡
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


def get_github_issue(issue_number):
    """GitHub Issueの情報を取得"""
    try:
        result = subprocess.run(
            ["gh", "issue", "view", str(issue_number), "--json", 
             "title,body,comments,updatedAt,createdAt,labels,assignees,url"],
            capture_output=True,
            text=True,
            check=True
        )
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"❌ GitHub Issue取得エラー: {e}")
        return None


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


def analyze_git_history():
    """Git履歴を分析して緊急修正を検出"""
    analysis_results = {
        "emergency_fixes": [],
        "recent_commits": [],
        "bypassed_workflow_commits": [],
        "changed_files": [],
        "total_commits_analyzed": 0
    }
    
    try:
        # 過去7日間のコミット履歴を取得
        since_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
        
        result = subprocess.run(
            ["git", "log", f"--since={since_date}", "--oneline", "--no-merges"],
            capture_output=True,
            text=True,
            check=True
        )
        
        commits = result.stdout.strip().split('\n') if result.stdout.strip() else []
        analysis_results["total_commits_analyzed"] = len(commits)
        
        # 緊急修正のキーワードでフィルタリング
        emergency_keywords = ["hotfix", "emergency", "urgent", "critical", "production", "fix"]
        
        for commit_line in commits:
            if commit_line:
                commit_hash = commit_line.split(' ')[0]
                commit_message = ' '.join(commit_line.split(' ')[1:])
                analysis_results["recent_commits"].append({
                    "hash": commit_hash,
                    "message": commit_message
                })
                
                # 緊急修正の検出
                if any(keyword in commit_message.lower() for keyword in emergency_keywords):
                    analysis_results["emergency_fixes"].append({
                        "hash": commit_hash,
                        "message": commit_message,
                        "type": "emergency_fix"
                    })
        
        # 標準ワークフロー迂回の検出（テストファイルが同時にコミットされていない）
        for commit in analysis_results["recent_commits"]:
            files_result = subprocess.run(
                ["git", "show", "--name-only", "--format=", commit["hash"]],
                capture_output=True,
                text=True
            )
            
            if files_result.returncode == 0:
                changed_files = files_result.stdout.strip().split('\n') if files_result.stdout.strip() else []
                analysis_results["changed_files"].extend(changed_files)
                
                # ソースコードが変更されているが、テストファイルが含まれていない
                has_source_changes = any(
                    f.endswith(('.py', '.js', '.java', '.ts', '.cpp')) and 
                    not any(test_pattern in f.lower() for test_pattern in ['test_', '_test.', '/test/', 'test/'])
                    for f in changed_files
                )
                has_test_changes = any(
                    any(test_pattern in f.lower() for test_pattern in ['test_', '_test.', '/test/', 'test/'])
                    for f in changed_files
                )
                
                if has_source_changes and not has_test_changes:
                    analysis_results["bypassed_workflow_commits"].append({
                        "hash": commit["hash"],
                        "message": commit["message"],
                        "changed_files": changed_files,
                        "reason": "No test files in source code changes"
                    })
    
    except subprocess.CalledProcessError as e:
        print(f"❌ Git履歴分析エラー: {e}")
    except Exception as e:
        print(f"❌ 予期しないエラー: {e}")
    
    return analysis_results


def analyze_documentation_gaps():
    """ドキュメントとコードの不整合を分析"""
    gap_analysis = {
        "outdated_documents": [],
        "missing_use_cases": [],
        "domain_model_gaps": [],
        "scenario_coverage_gaps": [],
        "total_gaps": 0
    }
    
    try:
        # ドキュメントディレクトリの存在確認
        docs_dirs = {
            "use_cases": Path("docs/use_cases"),
            "domain": Path("docs/domain"),
            "reviews": Path("docs/reviews")
        }
        
        # 最近の変更と比較して古いドキュメントを特定
        for doc_type, doc_dir in docs_dirs.items():
            if doc_dir.exists():
                for doc_file in doc_dir.glob("*.md"):
                    # ファイルの最終更新時刻をチェック
                    file_mtime = datetime.fromtimestamp(doc_file.stat().st_mtime)
                    days_old = (datetime.now() - file_mtime).days
                    
                    if days_old > 7:  # 7日以上古い
                        gap_analysis["outdated_documents"].append({
                            "file": str(doc_file),
                            "days_old": days_old,
                            "type": doc_type
                        })
        
        # ソースコードファイルに対応するユースケースドキュメントの存在確認
        src_dir = Path("src")
        if src_dir.exists():
            for src_file in src_dir.rglob("*.py"):
                # 対応するユースケースドキュメントが存在するかチェック
                base_name = src_file.stem
                corresponding_use_case = docs_dirs["use_cases"] / f"{base_name}-use-case.md"
                
                if not corresponding_use_case.exists():
                    gap_analysis["missing_use_cases"].append({
                        "source_file": str(src_file),
                        "expected_doc": str(corresponding_use_case)
                    })
        
        gap_analysis["total_gaps"] = (
            len(gap_analysis["outdated_documents"]) +
            len(gap_analysis["missing_use_cases"]) +
            len(gap_analysis["domain_model_gaps"]) +
            len(gap_analysis["scenario_coverage_gaps"])
        )
        
    except Exception as e:
        print(f"❌ ドキュメントギャップ分析エラー: {e}")
    
    return gap_analysis


def analyze_test_coverage():
    """テストカバレッジを分析"""
    coverage_analysis = {
        "overall_coverage": 0.0,
        "uncovered_files": [],
        "missing_test_files": [],
        "test_quality_score": 0,
        "recommendations": []
    }
    
    try:
        # pytestでカバレッジを実行
        result = subprocess.run(
            ["uv", "run", "--frozen", "pytest", "--cov=src", "--cov-report=json", "--cov-report=term", "-q"],
            capture_output=True,
            text=True,
            cwd=os.getcwd()
        )
        
        # カバレッジ結果を解析
        coverage_file = Path("coverage.json")
        if coverage_file.exists():
            with open(coverage_file, 'r') as f:
                coverage_data = json.load(f)
                coverage_analysis["overall_coverage"] = coverage_data.get("totals", {}).get("percent_covered", 0)
                
                # 低カバレッジファイルの特定
                files_data = coverage_data.get("files", {})
                for file_path, file_data in files_data.items():
                    file_coverage = file_data.get("summary", {}).get("percent_covered", 0)
                    if file_coverage < 80:  # 80%未満
                        coverage_analysis["uncovered_files"].append({
                            "file": file_path,
                            "coverage": file_coverage,
                            "missing_lines": file_data.get("summary", {}).get("missing_lines", 0)
                        })
        
        # テストファイルの存在確認
        src_dir = Path("src")
        tests_dir = Path("tests")
        
        if src_dir.exists() and tests_dir.exists():
            for src_file in src_dir.rglob("*.py"):
                # 対応するテストファイルが存在するかチェック
                relative_path = src_file.relative_to(src_dir)
                test_file = tests_dir / f"test_{relative_path}"
                
                if not test_file.exists():
                    # 別のパターンもチェック
                    alt_test_file = tests_dir / relative_path.parent / f"{relative_path.stem}_test.py"
                    if not alt_test_file.exists():
                        coverage_analysis["missing_test_files"].append({
                            "source_file": str(src_file),
                            "expected_test": str(test_file)
                        })
        
        # テスト品質スコアの計算
        coverage_score = coverage_analysis["overall_coverage"]
        missing_files_penalty = len(coverage_analysis["missing_test_files"]) * 10
        coverage_analysis["test_quality_score"] = max(0, coverage_score - missing_files_penalty)
        
        # 推奨事項の生成
        if coverage_analysis["overall_coverage"] < 80:
            coverage_analysis["recommendations"].append(f"全体カバレッジが{coverage_analysis['overall_coverage']:.1f}%です。80%以上を目標にテストを追加してください。")
        
        if coverage_analysis["missing_test_files"]:
            coverage_analysis["recommendations"].append(f"{len(coverage_analysis['missing_test_files'])}個のソースファイルにテストが不足しています。")
        
        if coverage_analysis["uncovered_files"]:
            coverage_analysis["recommendations"].append(f"{len(coverage_analysis['uncovered_files'])}個のファイルでカバレッジが不十分です。")
    
    except Exception as e:
        print(f"❌ テストカバレッジ分析エラー: {e}")
    
    return coverage_analysis


def create_recovery_plan(git_analysis, doc_gaps, coverage_analysis):
    """復旧計画を作成"""
    recovery_plan = {
        "critical_tasks": [],
        "high_priority_tasks": [],
        "medium_priority_tasks": [],
        "low_priority_tasks": [],
        "estimated_hours": 0,
        "priority_level": "medium"
    }
    
    # Critical tasks (業務影響度が高い)
    if git_analysis["emergency_fixes"]:
        for fix in git_analysis["emergency_fixes"]:
            recovery_plan["critical_tasks"].append({
                "task": f"緊急修正 {fix['hash'][:7]} の文書化",
                "description": f"コミット「{fix['message']}」のIssue作成と仕様書更新",
                "estimated_hours": 1.0,
                "action": "/create-retroactive-issue"
            })
    
    if coverage_analysis["overall_coverage"] < 50:
        recovery_plan["critical_tasks"].append({
            "task": "クリティカルテストカバレッジ不足の解消",
            "description": f"カバレッジが{coverage_analysis['overall_coverage']:.1f}%と危険水準",
            "estimated_hours": 4.0,
            "action": "/create-tests"
        })
    
    # High priority tasks (品質影響度が高い)
    if git_analysis["bypassed_workflow_commits"]:
        for commit in git_analysis["bypassed_workflow_commits"]:
            recovery_plan["high_priority_tasks"].append({
                "task": f"標準プロセス迂回修正 {commit['hash'][:7]}",
                "description": f"「{commit['message']}」のテスト追加とドキュメント更新",
                "estimated_hours": 2.0,
                "action": "/create-tests"
            })
    
    if len(coverage_analysis["missing_test_files"]) > 0:
        recovery_plan["high_priority_tasks"].append({
            "task": f"{len(coverage_analysis['missing_test_files'])}個の不足テストファイル作成",
            "description": "ソースコードに対応するテストファイルの作成",
            "estimated_hours": len(coverage_analysis["missing_test_files"]) * 0.5,
            "action": "/create-tests"
        })
    
    # Medium priority tasks (技術的負債)
    if doc_gaps["outdated_documents"]:
        recovery_plan["medium_priority_tasks"].append({
            "task": f"{len(doc_gaps['outdated_documents'])}個の古いドキュメント更新",
            "description": "7日以上更新されていないドキュメントの見直し",
            "estimated_hours": len(doc_gaps["outdated_documents"]) * 0.3,
            "action": "/sync-documentation"
        })
    
    # Low priority tasks (nice-to-have)
    if coverage_analysis["uncovered_files"]:
        low_coverage_files = [f for f in coverage_analysis["uncovered_files"] if f["coverage"] > 50]
        if low_coverage_files:
            recovery_plan["low_priority_tasks"].append({
                "task": f"{len(low_coverage_files)}個のファイルのカバレッジ向上",
                "description": "50-80%のカバレッジファイルの改善",
                "estimated_hours": len(low_coverage_files) * 0.5,
                "action": "/create-tests"
            })
    
    # 総推定時間の計算
    all_tasks = (
        recovery_plan["critical_tasks"] +
        recovery_plan["high_priority_tasks"] +
        recovery_plan["medium_priority_tasks"] +
        recovery_plan["low_priority_tasks"]
    )
    recovery_plan["estimated_hours"] = sum(task.get("estimated_hours", 0) for task in all_tasks)
    
    # 優先度レベルの決定
    if recovery_plan["critical_tasks"]:
        recovery_plan["priority_level"] = "critical"
    elif len(recovery_plan["high_priority_tasks"]) > 3:
        recovery_plan["priority_level"] = "high"
    else:
        recovery_plan["priority_level"] = "medium"
    
    return recovery_plan


def generate_recovery_reports(git_analysis, doc_gaps, coverage_analysis, recovery_plan, issue_data):
    """復旧レポートとアクションプランを生成"""
    emergency_dir = Path("docs/emergency")
    emergency_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # 緊急復旧分析レポート
    report_file = emergency_dir / f"emergency-recovery-report-{timestamp}.md"
    
    report_content = f"""# 緊急復旧分析レポート

## 基本情報
- **分析実行日時**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
- **分析対象期間**: 過去7日間
- **総合優先度**: {recovery_plan["priority_level"].upper()}

## Git履歴分析結果

### ✅ 緊急修正検出
- **検出された緊急修正**: {len(git_analysis["emergency_fixes"])}件
- **標準プロセス迂回コミット**: {len(git_analysis["bypassed_workflow_commits"])}件
- **分析対象コミット総数**: {git_analysis["total_commits_analyzed"]}件

### 緊急修正一覧
"""
    
    for fix in git_analysis["emergency_fixes"][:5]:
        report_content += f"- `{fix['hash'][:7]}` {fix['message']}\n"
    
    report_content += f"""

### 標準プロセス迂回コミット
"""
    
    for commit in git_analysis["bypassed_workflow_commits"][:5]:
        report_content += f"- `{commit['hash'][:7]}` {commit['message']}\n"
        report_content += f"  理由: {commit['reason']}\n"
    
    report_content += f"""

## ドキュメントギャップ分析

### ✅ ドキュメント整合性
- **古いドキュメント**: {len(doc_gaps["outdated_documents"])}件
- **不足ユースケース**: {len(doc_gaps["missing_use_cases"])}件
- **総ギャップ数**: {doc_gaps["total_gaps"]}件

### 古いドキュメント一覧
"""
    
    for doc in doc_gaps["outdated_documents"][:5]:
        report_content += f"- {doc['file']} ({doc['days_old']}日前更新)\n"
    
    report_content += f"""

## テストカバレッジ分析

### ✅ カバレッジ状況
- **全体カバレッジ**: {coverage_analysis["overall_coverage"]:.1f}% (目標: 80%以上)
- **不足テストファイル**: {len(coverage_analysis["missing_test_files"])}個
- **低カバレッジファイル**: {len(coverage_analysis["uncovered_files"])}個
- **テスト品質スコア**: {coverage_analysis["test_quality_score"]:.1f}/100

### 推奨事項
"""
    
    for rec in coverage_analysis["recommendations"]:
        report_content += f"- {rec}\n"
    
    report_content += f"""

## 総合評価

### 復旧必要性: {"HIGH" if recovery_plan["priority_level"] in ["critical", "high"] else "MEDIUM"}
### 推定復旧時間: {recovery_plan["estimated_hours"]:.1f}時間

## 次のステップ
1. Critical タスクから順次実行
2. `/create-retroactive-issue` で未作成Issue対応
3. `/create-tests` でテストカバレッジ改善
4. `/sync-documentation` でドキュメント同期
"""
    
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    # 復旧アクションプラン
    action_plan_file = emergency_dir / f"recovery-action-plan-{timestamp}.md"
    
    action_plan_content = f"""# 復旧アクションプラン

## 実行概要
- **作成日時**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
- **優先度レベル**: {recovery_plan["priority_level"].upper()}
- **推定総時間**: {recovery_plan["estimated_hours"]:.1f}時間

## 🔴 Critical Tasks (即座実行必須)

"""
    
    for i, task in enumerate(recovery_plan["critical_tasks"], 1):
        action_plan_content += f"""### {i}. {task["task"]}
- **説明**: {task["description"]}
- **推定時間**: {task["estimated_hours"]:.1f}時間
- **実行コマンド**: `{task["action"]}`

"""
    
    action_plan_content += f"""## 🟡 High Priority Tasks (24時間以内)

"""
    
    for i, task in enumerate(recovery_plan["high_priority_tasks"], 1):
        action_plan_content += f"""### {i}. {task["task"]}
- **説明**: {task["description"]}
- **推定時間**: {task["estimated_hours"]:.1f}時間
- **実行コマンド**: `{task["action"]}`

"""
    
    action_plan_content += f"""## 🟢 Medium Priority Tasks (1週間以内)

"""
    
    for i, task in enumerate(recovery_plan["medium_priority_tasks"], 1):
        action_plan_content += f"""### {i}. {task["task"]}
- **説明**: {task["description"]}
- **推定時間**: {task["estimated_hours"]:.1f}時間
- **実行コマンド**: `{task["action"]}`

"""
    
    action_plan_content += f"""## ⚪ Low Priority Tasks (時間があるとき)

"""
    
    for i, task in enumerate(recovery_plan["low_priority_tasks"], 1):
        action_plan_content += f"""### {i}. {task["task"]}
- **説明**: {task["description"]}
- **推定時間**: {task["estimated_hours"]:.1f}時間
- **実行コマンド**: `{task["action"]}`

"""
    
    action_plan_content += f"""## 推奨実行順序

1. **即座実行**: Critical タスクをすべて完了
2. **短期対応**: High Priority タスクを優先度順に実行
3. **中期対応**: Medium Priority タスクを計画的に実行
4. **長期対応**: Low Priority タスクを空き時間で実行

## 進捗管理
- [ ] Critical タスク完了 (推定: {sum(t.get("estimated_hours", 0) for t in recovery_plan["critical_tasks"]):.1f}時間)
- [ ] High Priority タスク完了 (推定: {sum(t.get("estimated_hours", 0) for t in recovery_plan["high_priority_tasks"]):.1f}時間)
- [ ] Medium Priority タスク完了 (推定: {sum(t.get("estimated_hours", 0) for t in recovery_plan["medium_priority_tasks"]):.1f}時間)
- [ ] Low Priority タスク完了 (推定: {sum(t.get("estimated_hours", 0) for t in recovery_plan["low_priority_tasks"]):.1f}時間)
"""
    
    with open(action_plan_file, 'w', encoding='utf-8') as f:
        f.write(action_plan_content)
    
    return str(report_file), str(action_plan_file)


def main():
    """メイン処理"""
    
    # 引数チェック（Issue番号は任意）
    issue_number = sys.argv[1] if len(sys.argv) > 1 else None
    
    if issue_number:
        print(f"\n🚨 Issue #{issue_number} の緊急復旧分析を開始します\n")
    else:
        print(f"\n🚨 プロジェクト全体の緊急復旧分析を開始します\n")
    
    # GitHub Issue情報を取得（Issue番号が指定されている場合）
    issue_data = None
    if issue_number:
        print("📋 GitHub Issue情報を取得中...")
        issue_data = get_github_issue(issue_number)
        
        if issue_data:
            print(f"✅ Issue情報を取得: {issue_data.get('title', 'Unknown')}")
            comment_count = len(issue_data.get('comments', []))
            print(f"📝 コメント数: {comment_count}件")
        else:
            print("⚠️ GitHub Issue情報の取得に失敗しましたが、分析を続行します")
    
    # Git履歴分析
    print("\n📊 Git履歴分析中...")
    git_analysis = analyze_git_history()
    
    # ドキュメントギャップ分析
    print("\n📋 ドキュメント整合性チェック中...")
    doc_gaps = analyze_documentation_gaps()
    
    # テストカバレッジ分析
    print("\n🧪 テストカバレッジ分析中...")
    coverage_analysis = analyze_test_coverage()
    
    # 復旧計画作成
    print("\n📝 復旧計画作成中...")
    recovery_plan = create_recovery_plan(git_analysis, doc_gaps, coverage_analysis)
    
    # レポート生成
    print("\n📊 復旧レポート生成中...")
    report_file, action_plan_file = generate_recovery_reports(
        git_analysis, doc_gaps, coverage_analysis, recovery_plan, issue_data
    )
    
    # JSONファイルの処理（最新のJSONファイルを使用）
    json_file_path = None
    if issue_number:
        # 特定のIssue番号のJSONファイルを検索
        use_cases_dir = Path("docs/use_cases")
        if use_cases_dir.exists():
            for json_file in use_cases_dir.glob(f"issue-{issue_number}-*.json"):
                json_file_path = str(json_file)
                break
            
            if not json_file_path:
                simple_path = use_cases_dir / f"issue-{issue_number}.json"
                if simple_path.exists():
                    json_file_path = str(simple_path)
    else:
        # 最新のJSONファイルを使用
        json_file_path = find_most_recent_json()
    
    if json_file_path:
        print(f"✅ JSONファイル: {json_file_path}")
        
        # 緊急復旧情報を更新
        try:
            use_case_data = load_use_case_json(json_file_path)
            
            emergency_recovery = {
                "analysis_completed_at": datetime.now().isoformat(),
                "status": "SUCCESS" if recovery_plan["critical_tasks"] or recovery_plan["high_priority_tasks"] else "PARTIAL_SUCCESS",
                "emergency_fixes_detected": len(git_analysis["emergency_fixes"]),
                "critical_gaps": len(recovery_plan["critical_tasks"]),
                "recovery_priority": recovery_plan["priority_level"],
                "estimated_recovery_hours": recovery_plan["estimated_hours"],
                "report_file": report_file,
                "action_plan_file": action_plan_file,
                "next_actions": {
                    "immediate": ["/create-retroactive-issue", "/sync-documentation"],
                    "short_term": ["/create-tests", "/run-all-tests"],
                    "medium_term": ["/refactor", "/review-issue"]
                }
            }
            
            use_case_data["emergency_recovery"] = emergency_recovery
            save_use_case_json(json_file_path, use_case_data)
            
            # 実行履歴を更新
            command = f"/emergency-recovery {issue_number}" if issue_number else "/emergency-recovery"
            update_execution_history(
                json_file_path,
                command,
                "success",
                [report_file, action_plan_file]
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
        print("⚠️ JSONファイルが見つかりません（分析は継続）")
    
    # 結果サマリー表示
    print(f"\n🚨 緊急復旧分析結果")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"🎯 復旧優先度: {recovery_plan['priority_level'].upper()}")
    print(f"⚡ 緊急修正検出: {len(git_analysis['emergency_fixes'])}件")
    print(f"🔄 標準プロセス迂回: {len(git_analysis['bypassed_workflow_commits'])}件")
    print(f"📊 テストカバレッジ: {coverage_analysis['overall_coverage']:.1f}%")
    print(f"⏱️ 推定復旧時間: {recovery_plan['estimated_hours']:.1f}時間")
    
    print(f"\n📁 成果物")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"✅ {report_file}")
    print(f"✅ {action_plan_file}")
    
    print(f"\n📋 復旧タスク分布")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"🔴 Critical: {len(recovery_plan['critical_tasks'])}個")
    print(f"🟡 High: {len(recovery_plan['high_priority_tasks'])}個")
    print(f"🟢 Medium: {len(recovery_plan['medium_priority_tasks'])}個")
    print(f"⚪ Low: {len(recovery_plan['low_priority_tasks'])}個")
    
    print(f"\n⏭️ 次の推奨コマンド")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    if recovery_plan["critical_tasks"]:
        print(f"🔴 Critical タスクが存在 - 即座実行必須:")
        print(f"   /create-retroactive-issue")
        print(f"   → 緊急修正のIssue作成・文書化")
        if coverage_analysis["overall_coverage"] < 50:
            print(f"   /create-tests")
            print(f"   → 危険水準のテストカバレッジ改善")
    elif recovery_plan["high_priority_tasks"]:
        print(f"🟡 High Priority タスクが存在:")
        print(f"   /create-tests")
        print(f"   → 不足テストの作成")
        print(f"   /sync-documentation") 
        print(f"   → ドキュメント同期")
    elif recovery_plan["medium_priority_tasks"]:
        print(f"🟢 Medium Priority タスクのみ:")
        print(f"   /sync-documentation")
        print(f"   → 古いドキュメントの更新")
    else:
        print(f"✅ 緊急復旧が必要な問題は検出されませんでした")
        print(f"   プロジェクトは良好な状態です")
    
    # 最終メッセージ
    priority_emoji = {"critical": "🚨", "high": "⚠️", "medium": "🔧", "low": "✅"}
    emoji = priority_emoji.get(recovery_plan["priority_level"], "❓")
    
    print(f"\n{emoji} 緊急復旧分析完了")
    print(f"詳細な分析結果は {report_file} に記録されました。")
    print(f"復旧アクションプランは {action_plan_file} をご確認ください。")


if __name__ == "__main__":
    main()