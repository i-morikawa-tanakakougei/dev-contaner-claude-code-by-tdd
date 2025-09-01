#!/usr/bin/env python3
"""
Use Case Status Command - 改修版
実行履歴から進捗状況を詳細に表示し、次のステップを提案
"""

import json
import sys
from datetime import datetime
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))
from json_format_utils import (
    load_use_case_json,
    get_next_recommended_commands,
    format_execution_status
)


def find_use_case_json(issue_number):
    """Issue番号からJSONファイルを検索"""
    use_cases_dir = Path("docs/use_cases")
    
    if not use_cases_dir.exists():
        return None
    
    # issue-{number}-*.json パターンで検索
    for json_file in use_cases_dir.glob(f"issue-{issue_number}-*.json"):
        return str(json_file)
    
    # 単純なissue-{number}.json も検索
    simple_path = use_cases_dir / f"issue-{issue_number}.json"
    if simple_path.exists():
        return str(simple_path)
    
    return None


def calculate_progress_percentage(use_case_data):
    """進捗率を計算"""
    
    # 基本的なマイルストーン (重み付き)
    milestones = {
        "use_case_created": {"weight": 10, "completed": False},
        "domain_modeled": {"weight": 15, "completed": False},
        "tests_created": {"weight": 20, "completed": False},
        "domain_implemented": {"weight": 25, "completed": False},
        "application_implemented": {"weight": 15, "completed": False},
        "infrastructure_implemented": {"weight": 10, "completed": False},
        "presentation_implemented": {"weight": 5, "completed": False}
    }
    
    # 実行履歴から完了状況を判定
    commands = use_case_data.get("execution_history", {}).get("commands_executed", [])
    successful_commands = [cmd["command"] for cmd in commands if cmd["status"] == "success"]
    
    # マイルストーンの完了判定
    if any("/create-use-case" in cmd for cmd in successful_commands):
        milestones["use_case_created"]["completed"] = True
    
    if any("/domain-modeling" in cmd for cmd in successful_commands):
        milestones["domain_modeled"]["completed"] = True
    
    if any("/create-tests" in cmd for cmd in successful_commands):
        milestones["tests_created"]["completed"] = True
    
    if any("/implement-domain" in cmd for cmd in successful_commands):
        milestones["domain_implemented"]["completed"] = True
    
    if any("/implement-usecase" in cmd for cmd in successful_commands):
        milestones["application_implemented"]["completed"] = True
    
    if any("/implement-infra" in cmd for cmd in successful_commands):
        milestones["infrastructure_implemented"]["completed"] = True
    
    if any("/implement-presentation" in cmd for cmd in successful_commands):
        milestones["presentation_implemented"]["completed"] = True
    
    # 進捗率を計算
    total_weight = sum(milestone["weight"] for milestone in milestones.values())
    completed_weight = sum(
        milestone["weight"] for milestone in milestones.values() 
        if milestone["completed"]
    )
    
    return int((completed_weight / total_weight) * 100)


def get_architecture_status(use_case_data):
    """アーキテクチャ層の実装状況を取得"""
    architecture = use_case_data.get("architecture_alignment", {})
    layers = architecture.get("layers", {})
    
    layer_status = {}
    for layer, implemented in layers.items():
        if implemented:
            layer_status[layer] = "✅ 実装済み"
        else:
            layer_status[layer] = "⏳ 未実装"
    
    return layer_status


def get_test_status(use_case_data):
    """テストの実行状況を取得"""
    testing = use_case_data.get("testing_strategy", {})
    
    unit_tests = testing.get("unit_tests", {})
    integration_tests = testing.get("integration_tests", {})
    
    return {
        "unit": {
            "total": unit_tests.get("total", 0),
            "passed": unit_tests.get("passed", 0),
            "failed": unit_tests.get("failed", 0),
            "coverage": unit_tests.get("coverage", 0.0)
        },
        "integration": {
            "total": integration_tests.get("total", 0),
            "passed": integration_tests.get("passed", 0),
            "failed": integration_tests.get("failed", 0)
        }
    }


def format_command_history(commands):
    """コマンド履歴を見やすくフォーマット"""
    if not commands:
        return "履歴なし"
    
    lines = []
    for cmd in commands[-10:]:  # 最新10件
        executed_at = datetime.fromisoformat(cmd["executed_at"])
        status_icon = {
            "success": "✅",
            "failed": "❌",
            "partial": "⚠️"
        }.get(cmd["status"], "❓")
        
        duration = ""
        if "duration_ms" in cmd:
            duration = f" ({cmd['duration_ms']}ms)"
        
        lines.append(
            f"  {status_icon} {cmd['command']:<25} "
            f"{executed_at.strftime('%m-%d %H:%M')}{duration}"
        )
    
    if len(commands) > 10:
        lines.append(f"  ... 他 {len(commands) - 10} 件")
    
    return "\n".join(lines)


def get_blocking_issues(use_case_data):
    """ブロッキング課題を特定"""
    issues = []
    
    # 失敗したコマンドがあるか確認
    commands = use_case_data.get("execution_history", {}).get("commands_executed", [])
    failed_commands = [cmd for cmd in commands if cmd["status"] == "failed"]
    
    if failed_commands:
        issues.append("❌ 失敗したコマンドがあります")
        for cmd in failed_commands[-3:]:  # 最新3件
            issues.append(f"  - {cmd['command']}: {cmd.get('error_message', '詳細不明')}")
    
    # TDDフェーズの順序チェック
    tdd_phases = use_case_data.get("execution_history", {}).get("tdd_phases", {})
    
    if tdd_phases.get("GREEN", {}).get("status") == "completed" and tdd_phases.get("RED", {}).get("status") != "completed":
        issues.append("⚠️ RED Phase（テスト作成）をスキップしています")
    
    if tdd_phases.get("REFACTOR", {}).get("status") == "completed" and tdd_phases.get("GREEN", {}).get("status") != "completed":
        issues.append("⚠️ GREEN Phase（実装）をスキップしています")
    
    return issues


def main():
    """メイン処理"""
    
    # 引数チェック
    if len(sys.argv) < 2:
        print("❌ エラー: Issue番号が必要です")
        print("使用方法: /use-case-status <issue-number>")
        sys.exit(1)
    
    issue_number = sys.argv[1]
    
    # ユースケースJSONファイルを検索
    json_file_path = find_use_case_json(issue_number)
    
    if not json_file_path:
        print(f"\n❌ Issue #{issue_number} のユースケースが見つかりません")
        print("\n💡 次のステップ:")
        print(f"1. /create-use-case {issue_number}")
        print("   → ユースケース仕様の作成")
        return
    
    # ユースケースデータを読み込み
    use_case_data = load_use_case_json(json_file_path)
    metadata = use_case_data.get("metadata", {})
    
    # ヘッダー表示
    print(f"\n📊 Issue #{issue_number}: {metadata.get('title', '無題')}")
    print("━" * 60)
    
    # 基本情報
    created_at = datetime.fromisoformat(metadata.get("created_at", datetime.now().isoformat()))
    updated_at = datetime.fromisoformat(metadata.get("updated_at", datetime.now().isoformat()))
    
    print(f"📅 作成日時: {created_at.strftime('%Y-%m-%d %H:%M')}")
    print(f"🔄 更新日時: {updated_at.strftime('%Y-%m-%d %H:%M')}")
    print(f"🏷️ ステータス: {metadata.get('status', 'unknown')}")
    print(f"👥 担当者: {', '.join(metadata.get('assignees', [])) or '未割当'}")
    
    # 進捗率の表示
    progress = calculate_progress_percentage(use_case_data)
    progress_bar = "█" * (progress // 5) + "░" * (20 - progress // 5)
    print(f"\n📈 全体進捗: [{progress_bar}] {progress}%")
    
    # TDD進捗の詳細表示
    print(f"\n{format_execution_status(use_case_data)}")
    
    # アーキテクチャ層の状況
    layer_status = get_architecture_status(use_case_data)
    if layer_status:
        print(f"\n🏗️ アーキテクチャ層:")
        for layer, status in layer_status.items():
            print(f"  {layer.capitalize():<15}: {status}")
    
    # テスト実行状況
    test_status = get_test_status(use_case_data)
    unit = test_status["unit"]
    integration = test_status["integration"]
    
    if unit["total"] > 0 or integration["total"] > 0:
        print(f"\n🧪 テスト実行状況:")
        if unit["total"] > 0:
            print(f"  Unit Tests     : {unit['passed']}/{unit['total']} passed ({unit['coverage']:.1f}% coverage)")
        if integration["total"] > 0:
            print(f"  Integration    : {integration['passed']}/{integration['total']} passed")
    
    # コマンド実行履歴
    commands = use_case_data.get("execution_history", {}).get("commands_executed", [])
    if commands:
        print(f"\n📝 最近のコマンド履歴:")
        print(format_command_history(commands))
    
    # ブロッキング課題
    blocking_issues = get_blocking_issues(use_case_data)
    if blocking_issues:
        print(f"\n⚠️ ブロッキング課題:")
        for issue in blocking_issues:
            print(f"  {issue}")
    
    # 次の推奨コマンド
    recommendations = get_next_recommended_commands(json_file_path)
    if recommendations:
        print(f"\n⏭️ 次の推奨コマンド:")
        for i, cmd in enumerate(recommendations, 1):
            print(f"  {i}. {cmd} {issue_number}")
    else:
        # 全て完了している場合
        if progress >= 100:
            print(f"\n🎉 完了!")
            print(f"  すべての開発フェーズが完了しています。")
            print(f"  /create-pr {issue_number} でプルリクエストを作成できます。")
        else:
            print(f"\n💡 ヒント:")
            print(f"  進捗状況を確認して、必要なコマンドを実行してください。")
    
    # ファイル情報
    print(f"\n📁 関連ファイル:")
    print(f"  ✅ {json_file_path}")
    
    # 関連するテストファイル
    test_dir = Path(f"tests/test_issue_{issue_number}")
    if test_dir.exists():
        test_files = list(test_dir.glob("*.py"))
        for test_file in test_files:
            print(f"  🧪 {test_file}")
    
    # ドメイン層ファイル
    domain_dir = Path("src/domain")
    if domain_dir.exists():
        domain_files = []
        for pattern in ["entities/*.py", "value_objects/*.py", "services/*.py"]:
            domain_files.extend(domain_dir.glob(pattern))
        
        if domain_files:
            print(f"  🏗️ ドメイン層:")
            for domain_file in domain_files[:5]:  # 最大5件表示
                print(f"    {domain_file}")
            if len(domain_files) > 5:
                print(f"    ... 他 {len(domain_files) - 5} 件")
    
    print()


if __name__ == "__main__":
    main()