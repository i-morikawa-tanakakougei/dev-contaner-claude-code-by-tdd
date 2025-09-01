#!/usr/bin/env python3
"""
Execution History Analyzer - 実行履歴分析ツール
コマンドの実行時間、パフォーマンス、ボトルネックを分析
"""

import json
import sys
import statistics
from datetime import datetime, timedelta
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
    
    json_files = []
    for json_file in use_cases_dir.glob("issue-*.json"):
        json_files.append(str(json_file))
    
    return sorted(json_files)


def collect_execution_data():
    """全ファイルから実行データを収集"""
    
    json_files = find_all_use_case_jsons()
    all_commands = []
    issues_data = {}
    
    for json_file in json_files:
        try:
            use_case_data = load_use_case_json(json_file)
            metadata = use_case_data.get("metadata", {})
            execution_history = use_case_data.get("execution_history", {})
            issue_id = metadata.get("issue_id", "unknown")
            
            # Issue基本情報
            issues_data[issue_id] = {
                "title": metadata.get("title", ""),
                "created_at": metadata.get("created_at", ""),
                "updated_at": metadata.get("updated_at", ""),
                "status": metadata.get("status", "draft"),
                "json_file": json_file,
                "last_command": execution_history.get("last_command", "なし"),
                "tdd_phases": execution_history.get("tdd_phases", {}),
                "commands_executed": execution_history.get("commands_executed", [])
            }
            
            # コマンド実行履歴を収集
            commands = execution_history.get("commands_executed", [])
            for cmd in commands:
                cmd_data = cmd.copy()
                cmd_data["issue_id"] = issue_id
                all_commands.append(cmd_data)
                
        except Exception as e:
            print(f"⚠️ {json_file} の読み込みエラー: {e}")
    
    return all_commands, issues_data


def analyze_command_performance(commands):
    """コマンドのパフォーマンス分析"""
    
    # コマンド別の実行時間を集計
    command_times = defaultdict(list)
    command_success_rates = defaultdict(lambda: {"success": 0, "failed": 0, "partial": 0})
    
    for cmd in commands:
        cmd_name = cmd["command"].split()[0]  # コマンド名のみ抽出
        
        # 実行時間
        if "duration_ms" in cmd:
            command_times[cmd_name].append(cmd["duration_ms"])
        
        # 成功率
        status = cmd.get("status", "unknown")
        if status in command_success_rates[cmd_name]:
            command_success_rates[cmd_name][status] += 1
    
    # 統計計算
    performance_stats = {}
    for cmd_name, times in command_times.items():
        if times:
            performance_stats[cmd_name] = {
                "count": len(times),
                "avg_time": statistics.mean(times),
                "median_time": statistics.median(times),
                "min_time": min(times),
                "max_time": max(times),
                "std_dev": statistics.stdev(times) if len(times) > 1 else 0
            }
    
    # 成功率の計算
    success_rates = {}
    for cmd_name, stats in command_success_rates.items():
        total = sum(stats.values())
        if total > 0:
            success_rates[cmd_name] = {
                "total_executions": total,
                "success_rate": stats["success"] / total * 100,
                "failure_rate": stats["failed"] / total * 100,
                "partial_rate": stats["partial"] / total * 100
            }
    
    return performance_stats, success_rates


def analyze_usage_patterns(commands):
    """使用パターンを分析"""
    
    if not commands:
        return {}
    
    # 時間別使用パターン
    hourly_usage = defaultdict(int)
    daily_usage = defaultdict(int)
    command_sequences = defaultdict(int)
    
    # 実行間隔の分析
    execution_intervals = []
    
    sorted_commands = sorted(commands, key=lambda x: x.get("executed_at", ""))
    
    for i, cmd in enumerate(sorted_commands):
        try:
            executed_at = datetime.fromisoformat(cmd["executed_at"])
            
            # 時間帯別
            hourly_usage[executed_at.hour] += 1
            
            # 曜日別（0=月曜日）
            daily_usage[executed_at.weekday()] += 1
            
            # コマンドシーケンス（前後のコマンドとの関係）
            if i > 0:
                prev_cmd = sorted_commands[i-1]["command"].split()[0]
                curr_cmd = cmd["command"].split()[0]
                command_sequences[f"{prev_cmd} → {curr_cmd}"] += 1
                
                # 実行間隔
                prev_time = datetime.fromisoformat(sorted_commands[i-1]["executed_at"])
                interval = (executed_at - prev_time).total_seconds()
                execution_intervals.append(interval)
                
        except (ValueError, KeyError) as e:
            continue
    
    # 統計計算
    avg_interval = statistics.mean(execution_intervals) if execution_intervals else 0
    
    return {
        "hourly_usage": dict(hourly_usage),
        "daily_usage": dict(daily_usage),
        "command_sequences": dict(sorted(command_sequences.items(), key=lambda x: x[1], reverse=True)[:10]),
        "avg_execution_interval": avg_interval,
        "total_sessions": len(set(cmd.get("issue_id") for cmd in commands))
    }


def identify_bottlenecks(performance_stats, success_rates):
    """ボトルネックを特定"""
    
    bottlenecks = []
    
    # 実行時間が長いコマンド
    slow_commands = []
    for cmd_name, stats in performance_stats.items():
        if stats["avg_time"] > 5000:  # 5秒以上
            slow_commands.append((cmd_name, stats["avg_time"]))
    
    if slow_commands:
        slow_commands.sort(key=lambda x: x[1], reverse=True)
        bottlenecks.append({
            "type": "performance",
            "title": "実行時間が長いコマンド",
            "items": slow_commands[:5]
        })
    
    # 失敗率が高いコマンド
    unreliable_commands = []
    for cmd_name, stats in success_rates.items():
        if stats["failure_rate"] > 20:  # 20%以上の失敗率
            unreliable_commands.append((cmd_name, stats["failure_rate"]))
    
    if unreliable_commands:
        unreliable_commands.sort(key=lambda x: x[1], reverse=True)
        bottlenecks.append({
            "type": "reliability", 
            "title": "失敗率が高いコマンド",
            "items": unreliable_commands[:5]
        })
    
    # 実行回数が異常に多いコマンド（繰り返し実行の可能性）
    frequent_commands = []
    for cmd_name, stats in performance_stats.items():
        if stats["count"] > 10:  # 10回以上実行
            frequent_commands.append((cmd_name, stats["count"]))
    
    if frequent_commands:
        frequent_commands.sort(key=lambda x: x[1], reverse=True)
        bottlenecks.append({
            "type": "frequency",
            "title": "実行回数が多いコマンド",
            "items": frequent_commands[:5]
        })
    
    return bottlenecks


def generate_recommendations(bottlenecks, usage_patterns):
    """改善提案を生成"""
    
    recommendations = []
    
    for bottleneck in bottlenecks:
        if bottleneck["type"] == "performance":
            recommendations.append({
                "category": "パフォーマンス改善",
                "suggestions": [
                    "遅いコマンドの処理ロジック見直し",
                    "並列処理の導入検討",
                    "キャッシュ機能の実装",
                    "不要な処理の削除"
                ]
            })
        
        elif bottleneck["type"] == "reliability":
            recommendations.append({
                "category": "信頼性向上",
                "suggestions": [
                    "エラーハンドリングの強化",
                    "事前条件チェックの追加",
                    "リトライ機構の実装",
                    "ユーザー向けエラーメッセージの改善"
                ]
            })
        
        elif bottleneck["type"] == "frequency":
            recommendations.append({
                "category": "使いやすさ向上",
                "suggestions": [
                    "コマンドの統合検討",
                    "自動化できる処理の特定",
                    "デフォルト値の見直し",
                    "ワークフロー最適化"
                ]
            })
    
    # 使用パターンに基づく提案
    if usage_patterns.get("avg_execution_interval", 0) < 60:  # 1分以内の連続実行
        recommendations.append({
            "category": "ワークフロー最適化", 
            "suggestions": [
                "連続実行されるコマンドのバッチ化",
                "コマンド間の依存関係自動解決",
                "ワンコマンドでの複数処理実行"
            ]
        })
    
    return recommendations


def format_performance_table(performance_stats):
    """パフォーマンス統計をテーブル形式でフォーマット"""
    
    if not performance_stats:
        return "データなし"
    
    lines = []
    lines.append("| コマンド             | 実行回数 | 平均時間  | 中央値    | 最大時間  |")
    lines.append("|---------------------|----------|-----------|-----------|-----------|")
    
    # 平均実行時間でソート
    sorted_stats = sorted(
        performance_stats.items(), 
        key=lambda x: x[1]["avg_time"], 
        reverse=True
    )
    
    for cmd_name, stats in sorted_stats[:10]:  # 上位10件
        lines.append(
            f"| {cmd_name:<19} | {stats['count']:8d} | "
            f"{stats['avg_time']:7.0f}ms | {stats['median_time']:7.0f}ms | {stats['max_time']:7.0f}ms |"
        )
    
    return "\n".join(lines)


def format_success_rate_table(success_rates):
    """成功率をテーブル形式でフォーマット"""
    
    if not success_rates:
        return "データなし"
    
    lines = []
    lines.append("| コマンド             | 実行回数 | 成功率   | 失敗率   |")
    lines.append("|---------------------|----------|----------|----------|")
    
    # 失敗率でソート
    sorted_rates = sorted(
        success_rates.items(),
        key=lambda x: x[1]["failure_rate"],
        reverse=True
    )
    
    for cmd_name, stats in sorted_rates:
        lines.append(
            f"| {cmd_name:<19} | {stats['total_executions']:8d} | "
            f"{stats['success_rate']:6.1f}% | {stats['failure_rate']:6.1f}% |"
        )
    
    return "\n".join(lines)


def format_issue_progress_report(issues_data):
    """Issue毎の進捗レポートを作成"""
    
    if not issues_data:
        return "データなし"
    
    lines = []
    lines.append("| Issue# | タイトル                     | 最終コマンド           | TDD進捗   | ステータス |")
    lines.append("|--------|------------------------------|------------------------|-----------|-----------|")
    
    # TDDフェーズのステータスマッピング
    def get_tdd_progress(tdd_phases):
        phases = ["RED", "GREEN", "REFACTOR"]
        completed = sum(1 for phase in phases if tdd_phases.get(phase, {}).get("status") == "completed")
        in_progress = any(tdd_phases.get(phase, {}).get("status") == "in_progress" for phase in phases)
        
        if completed == 3:
            return "✅完了 (3/3)"
        elif in_progress:
            return f"🔄進行中 ({completed}/3)"
        elif completed > 0:
            return f"⏸️部分 ({completed}/3)"
        else:
            return "⚫未開始 (0/3)"
    
    # Issue番号でソート
    sorted_issues = sorted(issues_data.items(), key=lambda x: int(x[0]) if str(x[0]).isdigit() else 999)
    
    for issue_id, data in sorted_issues:
        title = data["title"][:28] + "..." if len(data["title"]) > 28 else data["title"]
        last_cmd = data["last_command"]
        if len(last_cmd) > 20:
            last_cmd = last_cmd[:17] + "..."
        
        tdd_progress = get_tdd_progress(data["tdd_phases"])
        status = data["status"]
        
        lines.append(
            f"| {str(issue_id):>6} | {title:<28} | {last_cmd:<22} | {tdd_progress:<9} | {status:<9} |"
        )
    
    return "\n".join(lines)


def main():
    """メイン処理"""
    
    print(f"\n📊 コマンド実行履歴分析レポート")
    print("━" * 80)
    
    # データ収集
    print("📁 実行データを収集中...")
    commands, issues_data = collect_execution_data()
    
    if not commands and not issues_data:
        print("❌ 実行履歴が見つかりません")
        return
    
    print(f"✅ {len(commands)}個のコマンド実行履歴を収集")
    print(f"✅ {len(issues_data)}個のIssueを分析")
    
    # Issue毎の進捗表示
    print(f"\n🎯 Issue別進捗状況")
    print("━" * 80)
    issue_progress = format_issue_progress_report(issues_data)
    print(issue_progress)
    
    # 分析実行
    print("\n🔍 パフォーマンス分析中...")
    performance_stats, success_rates = analyze_command_performance(commands)
    
    print("🔍 使用パターン分析中...")
    usage_patterns = analyze_usage_patterns(commands)
    
    print("🔍 ボトルネック特定中...")
    bottlenecks = identify_bottlenecks(performance_stats, success_rates)
    
    print("🔍 改善提案生成中...")
    recommendations = generate_recommendations(bottlenecks, usage_patterns)
    
    # レポート出力
    print(f"\n📈 全体サマリー")
    print("━" * 40)
    print(f"総コマンド実行数    : {len(commands):,}回")
    print(f"ユニークコマンド数  : {len(performance_stats)}種類")
    print(f"対象Issue数        : {len(issues_data)}件")
    print(f"平均実行間隔       : {usage_patterns.get('avg_execution_interval', 0):.1f}秒")
    
    # パフォーマンス統計
    if performance_stats:
        print(f"\n⚡ パフォーマンス統計")
        print("━" * 40)
        print(format_performance_table(performance_stats))
    
    # 成功率統計
    if success_rates:
        print(f"\n✅ 成功率統計")
        print("━" * 40) 
        print(format_success_rate_table(success_rates))
    
    # 使用パターン
    hourly = usage_patterns.get("hourly_usage", {})
    if hourly:
        print(f"\n🕐 時間帯別使用パターン")
        print("━" * 40)
        for hour in range(24):
            count = hourly.get(hour, 0)
            if count > 0:
                bar = "█" * min(count, 20)
                print(f"  {hour:2d}時: {bar:<20} ({count}回)")
    
    # コマンドシーケンス
    sequences = usage_patterns.get("command_sequences", {})
    if sequences:
        print(f"\n🔄 よく使用されるコマンドシーケンス")
        print("━" * 40)
        for sequence, count in list(sequences.items())[:5]:
            print(f"  {sequence:<30} ({count}回)")
    
    # ボトルネック
    if bottlenecks:
        print(f"\n⚠️ 特定されたボトルネック")
        print("━" * 40)
        for bottleneck in bottlenecks:
            print(f"\n{bottleneck['title']}:")
            for item_name, value in bottleneck["items"][:3]:
                if bottleneck["type"] == "performance":
                    print(f"  - {item_name}: {value:.0f}ms")
                elif bottleneck["type"] == "reliability":
                    print(f"  - {item_name}: {value:.1f}% 失敗率")
                elif bottleneck["type"] == "frequency":
                    print(f"  - {item_name}: {value}回実行")
    
    # 改善提案
    if recommendations:
        print(f"\n💡 改善提案")
        print("━" * 40)
        for rec in recommendations:
            print(f"\n{rec['category']}:")
            for suggestion in rec["suggestions"]:
                print(f"  • {suggestion}")
    
    # レポートファイル生成
    report_dir = Path("docs/analysis_reports")
    report_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = report_dir / f"execution_analysis_{timestamp}.md"
    
    # Markdownレポート作成
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(f"# コマンド実行履歴分析レポート\n\n")
        f.write(f"生成日時: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write(f"## 全体サマリー\n\n")
        f.write(f"- 総コマンド実行数: {len(commands):,}回\n")
        f.write(f"- ユニークコマンド数: {len(performance_stats)}種類\n")
        f.write(f"- 対象Issue数: {len(issues_data)}件\n\n")
        
        if bottlenecks:
            f.write(f"## 特定されたボトルネック\n\n")
            for bottleneck in bottlenecks:
                f.write(f"### {bottleneck['title']}\n\n")
                for item_name, value in bottleneck["items"]:
                    f.write(f"- {item_name}: {value}\n")
                f.write("\n")
        
        if recommendations:
            f.write(f"## 改善提案\n\n")
            for rec in recommendations:
                f.write(f"### {rec['category']}\n\n")
                for suggestion in rec["suggestions"]:
                    f.write(f"- {suggestion}\n")
                f.write("\n")
    
    print(f"\n📄 詳細レポートを生成しました:")
    print(f"  {report_file}")
    
    print(f"\n🎯 次のステップ:")
    print(f"  1. ボトルネックとなっているコマンドの最適化")
    print(f"  2. 失敗率の高いコマンドのエラーハンドリング改善")
    print(f"  3. 頻繁に使用されるコマンドシーケンスの自動化検討")


if __name__ == "__main__":
    main()