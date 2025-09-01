#!/usr/bin/env python3
"""
Project Status Command - 改修版
プロジェクト全体の進捗状況を集計表示
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from collections import defaultdict

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))
from json_format_utils import load_use_case_json


def find_all_use_case_jsons():
    """すべてのユースケースJSONファイルを検索"""
    use_cases_dir = Path("docs/use_cases")
    
    if not use_cases_dir.exists():
        return []
    
    # issue-*.json パターンで検索
    json_files = []
    for json_file in use_cases_dir.glob("issue-*.json"):
        json_files.append(str(json_file))
    
    return sorted(json_files)


def calculate_issue_progress(use_case_data):
    """個別Issueの進捗率を計算"""
    
    # 基本的なマイルストーン
    milestones = [
        "use_case_created",
        "domain_modeled", 
        "tests_created",
        "domain_implemented",
        "application_implemented",
        "infrastructure_implemented",
        "presentation_implemented"
    ]
    
    # 実行履歴から完了状況を判定
    commands = use_case_data.get("execution_history", {}).get("commands_executed", [])
    successful_commands = [cmd["command"] for cmd in commands if cmd["status"] == "success"]
    
    completed_milestones = 0
    total_milestones = len(milestones)
    
    # マイルストーンの完了判定
    command_patterns = [
        "/create-use-case",
        "/domain-modeling", 
        "/create-tests",
        "/implement-domain",
        "/implement-usecase",
        "/implement-infra",
        "/implement-presentation"
    ]
    
    for pattern in command_patterns:
        if any(pattern in cmd for cmd in successful_commands):
            completed_milestones += 1
    
    return int((completed_milestones / total_milestones) * 100)


def get_tdd_phase_summary(use_case_data):
    """TDDフェーズのサマリーを取得"""
    tdd_phases = use_case_data.get("execution_history", {}).get("tdd_phases", {})
    
    phase_status = {}
    for phase in ["RED", "GREEN", "REFACTOR"]:
        status = tdd_phases.get(phase, {}).get("status", "not_started")
        phase_status[phase] = status
    
    return phase_status


def calculate_project_stats():
    """プロジェクト全体の統計を計算"""
    json_files = find_all_use_case_jsons()
    
    if not json_files:
        return {
            "total_issues": 0,
            "issues": [],
            "overall_progress": 0,
            "phase_distribution": {"not_started": 0, "in_progress": 0, "completed": 0},
            "command_stats": {},
            "recent_activity": []
        }
    
    issues = []
    all_commands = []
    phase_counts = defaultdict(int)
    
    for json_file in json_files:
        try:
            use_case_data = load_use_case_json(json_file)
            metadata = use_case_data.get("metadata", {})
            
            # Issue番号を抽出
            issue_id = metadata.get("issue_id")
            if not issue_id:
                # ファイル名から抽出
                filename = Path(json_file).stem
                if filename.startswith("issue-"):
                    issue_id = filename.split("-")[1]
            
            progress = calculate_issue_progress(use_case_data)
            tdd_phases = get_tdd_phase_summary(use_case_data)
            
            # フェーズ分布を計算
            if progress == 0:
                phase_counts["not_started"] += 1
            elif progress == 100:
                phase_counts["completed"] += 1
            else:
                phase_counts["in_progress"] += 1
            
            issue_info = {
                "id": issue_id,
                "title": metadata.get("title", "無題"),
                "progress": progress,
                "status": metadata.get("status", "unknown"),
                "tdd_phases": tdd_phases,
                "updated_at": metadata.get("updated_at", ""),
                "json_file": json_file
            }
            
            issues.append(issue_info)
            
            # コマンド履歴を収集
            commands = use_case_data.get("execution_history", {}).get("commands_executed", [])
            for cmd in commands:
                cmd_info = cmd.copy()
                cmd_info["issue_id"] = issue_id
                all_commands.append(cmd_info)
            
        except Exception as e:
            print(f"⚠️ {json_file} の読み込みエラー: {e}")
    
    # 全体進捗を計算
    overall_progress = int(sum(issue["progress"] for issue in issues) / len(issues)) if issues else 0
    
    # 最近のアクティビティ (最新20件)
    recent_activity = sorted(all_commands, key=lambda x: x.get("executed_at", ""), reverse=True)[:20]
    
    # コマンド統計
    command_stats = defaultdict(int)
    for cmd in all_commands:
        # コマンド名を正規化
        cmd_name = cmd["command"].split()[0]
        command_stats[cmd_name] += 1
    
    return {
        "total_issues": len(issues),
        "issues": sorted(issues, key=lambda x: int(x["id"]) if x["id"] and x["id"].isdigit() else 0),
        "overall_progress": overall_progress,
        "phase_distribution": dict(phase_counts),
        "command_stats": dict(command_stats),
        "recent_activity": recent_activity
    }


def format_issue_table(issues):
    """Issue一覧テーブルをフォーマット"""
    if not issues:
        return "Issueが見つかりません"
    
    lines = []
    lines.append("| ID | タイトル                    | 進捗 | TDD進捗        | 更新日時     |")
    lines.append("|----|---------------------------|------|----------------|------------|")
    
    for issue in issues:
        # TDD進捗のアイコン
        tdd = issue["tdd_phases"]
        red_icon = "🔴" if tdd.get("RED") == "completed" else "⚫"
        green_icon = "🟢" if tdd.get("GREEN") == "completed" else "⚫"  
        refactor_icon = "🔵" if tdd.get("REFACTOR") == "completed" else "⚫"
        tdd_status = f"{red_icon}{green_icon}{refactor_icon}"
        
        # 進捗バー
        progress = issue["progress"]
        progress_bar = "█" * (progress // 10) + "░" * (10 - progress // 10)
        progress_text = f"[{progress_bar}] {progress:3d}%"
        
        # 更新日時
        updated_at = issue.get("updated_at", "")
        if updated_at:
            try:
                dt = datetime.fromisoformat(updated_at)
                update_str = dt.strftime("%m-%d %H:%M")
            except:
                update_str = "不明"
        else:
            update_str = "不明"
        
        # タイトルを28文字に切り詰め
        title = issue["title"]
        if len(title) > 25:
            title = title[:22] + "..."
        
        lines.append(f"| {issue['id']:2} | {title:<25} | {progress_text} | {tdd_status}      | {update_str} |")
    
    return "\n".join(lines)


def format_command_stats(command_stats):
    """コマンド統計をフォーマット"""
    if not command_stats:
        return "コマンド実行履歴なし"
    
    # 使用頻度順にソート
    sorted_commands = sorted(command_stats.items(), key=lambda x: x[1], reverse=True)
    
    lines = []
    for cmd, count in sorted_commands[:10]:  # 上位10件
        bar_length = min(count, 20)  # 最大20文字
        bar = "█" * bar_length
        lines.append(f"  {cmd:<20} : {bar} ({count}回)")
    
    return "\n".join(lines)


def format_recent_activity(recent_activity):
    """最近のアクティビティをフォーマット"""
    if not recent_activity:
        return "アクティビティなし"
    
    lines = []
    for activity in recent_activity[:10]:  # 最新10件
        executed_at = activity.get("executed_at", "")
        if executed_at:
            try:
                dt = datetime.fromisoformat(executed_at)
                time_str = dt.strftime("%m-%d %H:%M")
            except:
                time_str = "不明"
        else:
            time_str = "不明"
        
        status_icon = {
            "success": "✅",
            "failed": "❌", 
            "partial": "⚠️"
        }.get(activity.get("status", "unknown"), "❓")
        
        issue_id = activity.get("issue_id", "?")
        command = activity.get("command", "unknown")
        
        lines.append(f"  {status_icon} #{issue_id:<3} {command:<25} {time_str}")
    
    return "\n".join(lines)


def main():
    """メイン処理"""
    
    print(f"\n📊 プロジェクト全体ステータス")
    print("━" * 80)
    
    # プロジェクト統計を計算
    stats = calculate_project_stats()
    
    if stats["total_issues"] == 0:
        print("\n❌ ユースケースが見つかりません")
        print("\n💡 次のステップ:")
        print("1. /create-use-case <issue-number>")
        print("   → 最初のユースケースを作成")
        return
    
    # 基本情報
    print(f"📈 全体進捗: {stats['overall_progress']}% ({stats['total_issues']} Issues)")
    
    # フェーズ分布
    phase_dist = stats["phase_distribution"]
    total = stats["total_issues"]
    print(f"🎯 フェーズ分布:")
    print(f"  未開始    : {phase_dist.get('not_started', 0):2d}個 ({phase_dist.get('not_started', 0)/total*100:4.1f}%)")
    print(f"  進行中    : {phase_dist.get('in_progress', 0):2d}個 ({phase_dist.get('in_progress', 0)/total*100:4.1f}%)")
    print(f"  完了      : {phase_dist.get('completed', 0):2d}個 ({phase_dist.get('completed', 0)/total*100:4.1f}%)")
    
    # Issue一覧テーブル
    print(f"\n📋 Issue一覧:")
    print(format_issue_table(stats["issues"]))
    
    # コマンド使用統計
    print(f"\n📊 コマンド使用統計:")
    print(format_command_stats(stats["command_stats"]))
    
    # 最近のアクティビティ
    print(f"\n🕐 最近のアクティビティ:")
    print(format_recent_activity(stats["recent_activity"]))
    
    # 推奨アクション
    print(f"\n💡 推奨アクション:")
    
    # 未開始のIssueがあるか
    not_started = [issue for issue in stats["issues"] if issue["progress"] == 0]
    if not_started:
        print(f"  📝 未開始Issue:")
        for issue in not_started[:3]:  # 上位3件
            print(f"    - #{issue['id']}: {issue['title']}")
            print(f"      → /create-use-case {issue['id']} または /domain-modeling {issue['id']}")
    
    # 進行中のIssueがあるか
    in_progress = [issue for issue in stats["issues"] if 0 < issue["progress"] < 100]
    if in_progress:
        print(f"  🔄 進行中Issue:")
        for issue in in_progress[:3]:  # 上位3件
            print(f"    - #{issue['id']}: {issue['title']} ({issue['progress']}%)")
            print(f"      → /use-case-status {issue['id']} で詳細確認")
    
    # 完了したIssueがあるか
    completed = [issue for issue in stats["issues"] if issue["progress"] == 100]
    if completed:
        print(f"  🎉 完了Issue:")
        for issue in completed[-3:]:  # 最新3件
            print(f"    - #{issue['id']}: {issue['title']}")
            print(f"      → /create-pr {issue['id']} でPR作成可能")
    
    print(f"\n📁 プロジェクト構成:")
    
    # ディレクトリ構造の確認
    directories = {
        "docs/use_cases": "ユースケース仕様",
        "src/domain": "ドメイン層",
        "tests": "テストコード",
        "docs/vision": "プロジェクトビジョン"
    }
    
    for dir_path, description in directories.items():
        path = Path(dir_path)
        if path.exists():
            file_count = len(list(path.rglob("*.py"))) + len(list(path.rglob("*.json"))) + len(list(path.rglob("*.md")))
            print(f"  ✅ {dir_path:<20}: {description} ({file_count} files)")
        else:
            print(f"  ❌ {dir_path:<20}: {description} (未作成)")
    
    print()


if __name__ == "__main__":
    main()