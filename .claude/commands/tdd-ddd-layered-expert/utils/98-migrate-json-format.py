#!/usr/bin/env python3
"""
JSON Format Migration Tool - 互換性ツール
既存のJSONファイルを新しい標準フォーマットに変換
"""

import json
import sys
import shutil
from datetime import datetime
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))
from json_format_utils import save_use_case_json


def find_all_use_case_jsons():
    """すべてのユースケースJSONファイルを検索"""
    use_cases_dir = Path("docs/use_cases")
    
    if not use_cases_dir.exists():
        return []
    
    json_files = []
    for json_file in use_cases_dir.glob("*.json"):
        if json_file.name != "standard-use-case-format.json":
            json_files.append(str(json_file))
    
    return sorted(json_files)


def backup_file(file_path):
    """ファイルをバックアップ"""
    backup_path = f"{file_path}.backup-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    shutil.copy2(file_path, backup_path)
    return backup_path


def detect_format_version(data):
    """JSONファイルのフォーマットバージョンを検出"""
    
    # 新フォーマットの特徴
    if "execution_history" in data:
        return "new"
    
    # 旧フォーマットのパターン1 (issue-1.json style)
    if "github_issue" in data and "metadata" in data:
        return "old_v1"
    
    # 旧フォーマットのパターン2 (issue-2.json style)  
    if "use_case_metadata" in data:
        return "old_v2"
    
    # 不明なフォーマット
    return "unknown"


def migrate_from_old_v1(data):
    """旧フォーマット v1 (issue-1.json style) から新フォーマットに変換"""
    
    # GitHub Issue情報をmetadataに統合
    github_issue = data.get("github_issue", {})
    metadata = data.get("metadata", {})
    
    new_metadata = {
        "issue_id": github_issue.get("number") or metadata.get("issue_id"),
        "title": github_issue.get("title", ""),
        "description": github_issue.get("body", ""),
        "created_at": metadata.get("created_at", datetime.now().isoformat()),
        "updated_at": datetime.now().isoformat(),
        "status": metadata.get("status", "draft"),
        "github_url": github_issue.get("html_url", ""),
        "labels": [label if isinstance(label, str) else label.get("name", "") for label in github_issue.get("labels", [])],
        "assignees": [assignee if isinstance(assignee, str) else assignee.get("login", "") for assignee in github_issue.get("assignees", [])]
    }
    
    # シナリオ構造はそのまま使用
    scenarios = data.get("scenarios", {
        "main_scenarios": [],
        "alternative_scenarios": [],
        "exception_scenarios": []
    })
    
    # 受入基準を移行
    acceptance_criteria = []
    
    # ルートレベルの受入基準
    if "acceptance_criteria" in data:
        for i, criteria in enumerate(data["acceptance_criteria"]):
            acceptance_criteria.append({
                "id": f"ac_{i+1}",
                "description": criteria if isinstance(criteria, str) else str(criteria),
                "status": "pending"
            })
    
    # シナリオ内の受入基準も統合
    scenarios_data = data.get("scenarios", {})
    for scenario_type in ["main_scenarios", "alternative_scenarios", "exception_scenarios"]:
        for scenario in scenarios_data.get(scenario_type, []):
            if isinstance(scenario, dict) and "acceptance_criteria" in scenario:
                for j, sc_criteria in enumerate(scenario["acceptance_criteria"]):
                    acceptance_criteria.append({
                        "id": f"sc_{scenario.get('id', len(acceptance_criteria))}_{j+1}",
                        "description": sc_criteria if isinstance(sc_criteria, str) else str(sc_criteria),
                        "status": "pending"
                    })
    
    # ドメインモデル情報を移行
    domain_model = {
        "entities": [],
        "value_objects": [],
        "domain_services": [],
        "business_rules": [],
        "ubiquitous_language": data.get("ubiquitous_language", {})
    }
    
    # domain_conceptsからエンティティと値オブジェクトを抽出
    if "domain_concepts" in data:
        for concept in data["domain_concepts"]:
            if isinstance(concept, dict):
                concept_type = concept.get("type", "").lower()
                if concept_type in ["entity", "entities"]:
                    domain_model["entities"].append({
                        "name": concept.get("name", ""),
                        "description": concept.get("responsibility", concept.get("description", "")),
                        "properties": concept.get("attributes", concept.get("properties", []))
                    })
                elif concept_type in ["value_object", "valueobject", "value object"]:
                    domain_model["value_objects"].append({
                        "name": concept.get("name", ""),
                        "description": concept.get("responsibility", concept.get("description", ""))
                    })
    
    # business_rulesを移行
    if "business_rules" in data:
        for i, rule in enumerate(data["business_rules"]):
            if isinstance(rule, dict):
                domain_model["business_rules"].append({
                    "id": rule.get("id", f"br_{i+1}"),
                    "name": rule.get("name", ""),
                    "description": rule.get("description", str(rule))
                })
            elif isinstance(rule, str):
                domain_model["business_rules"].append({
                    "id": f"br_{i+1}",
                    "name": "",
                    "description": rule
                })
            else:
                domain_model["business_rules"].append({
                    "id": f"br_{i+1}",
                    "name": "",
                    "description": str(rule)
                })
    
    # 実行履歴を初期化
    execution_history = {
        "tdd_phases": {
            "RED": {"status": "not_started"},
            "GREEN": {"status": "not_started"},
            "REFACTOR": {"status": "not_started"}
        },
        "commands_executed": [{
            "command": f"/migrate-json-format {new_metadata['issue_id']}",
            "executed_at": datetime.now().isoformat(),
            "status": "success",
            "files_affected": ["migration"]
        }],
        "last_command": f"/migrate-json-format {new_metadata['issue_id']}"
    }
    
    # その他のセクションを初期化
    architecture_alignment = {
        "layers": {
            "domain": False,
            "application": False,
            "infrastructure": False,
            "presentation": False
        },
        "patterns_used": []
    }
    
    dependencies = data.get("dependencies", {"technical": [], "functional": []})
    
    testing_strategy = {
        "unit_tests": {"total": 0, "passed": 0, "failed": 0, "coverage": 0.0},
        "integration_tests": {"total": 0, "passed": 0, "failed": 0}
    }
    
    documentation = {
        "vision_doc": None,
        "domain_doc": None,
        "api_doc": None,
        "test_plan": None
    }
    
    review_history = []
    
    return {
        "metadata": new_metadata,
        "scenarios": scenarios,
        "acceptance_criteria": acceptance_criteria,
        "domain_model": domain_model,
        "execution_history": execution_history,
        "architecture_alignment": architecture_alignment,
        "dependencies": dependencies,
        "testing_strategy": testing_strategy,
        "documentation": documentation,
        "review_history": review_history
    }


def migrate_from_old_v2(data):
    """旧フォーマット v2 (issue-2.json style) から新フォーマットに変換"""
    
    # use_case_metadata を metadata にリネーム
    use_case_metadata = data.get("use_case_metadata", {})
    github_issue = use_case_metadata.get("github_issue", {})
    
    new_metadata = {
        "issue_id": github_issue.get("number") or use_case_metadata.get("issue_id"),
        "title": github_issue.get("title", ""),
        "description": github_issue.get("body", ""),
        "created_at": use_case_metadata.get("created_at", datetime.now().isoformat()),
        "updated_at": datetime.now().isoformat(),
        "status": use_case_metadata.get("status", "draft"),
        "github_url": github_issue.get("html_url", ""),
        "labels": [label if isinstance(label, str) else label.get("name", "") for label in github_issue.get("labels", [])],
        "assignees": [assignee if isinstance(assignee, str) else assignee.get("login", "") for assignee in github_issue.get("assignees", [])]
    }
    
    # シナリオ構造を正規化
    old_scenarios = data.get("scenarios", {})
    scenarios = {
        "main_scenarios": old_scenarios.get("main_success", []),
        "alternative_scenarios": old_scenarios.get("alternative_flows", []),
        "exception_scenarios": old_scenarios.get("exception_flows", [])
    }
    
    # 既存のacceptance_criteriaを移行
    old_acceptance_criteria = data.get("acceptance_criteria", [])
    acceptance_criteria = []
    
    # 受入基準の構造を正規化
    if isinstance(old_acceptance_criteria, list):
        for i, criteria in enumerate(old_acceptance_criteria):
            if isinstance(criteria, str):
                acceptance_criteria.append({
                    "id": f"ac_{i+1}",
                    "description": criteria,
                    "status": "pending"
                })
            elif isinstance(criteria, dict):
                acceptance_criteria.append({
                    "id": criteria.get("id", f"ac_{i+1}"),
                    "description": criteria.get("description", str(criteria)),
                    "status": criteria.get("status", "pending")
                })
    
    # シナリオの受入基準も確認
    scenarios_data = data.get("scenarios", {})
    for scenario_type in ["main_scenarios", "alternative_scenarios", "exception_scenarios"]:
        for scenario in scenarios_data.get(scenario_type, []):
            if isinstance(scenario, dict) and "acceptance_criteria" in scenario:
                for j, sc_criteria in enumerate(scenario["acceptance_criteria"]):
                    acceptance_criteria.append({
                        "id": f"sc_{scenario.get('id', len(acceptance_criteria))}_{j+1}",
                        "description": sc_criteria if isinstance(sc_criteria, str) else str(sc_criteria),
                        "status": "pending"
                    })
    
    # ドメインモデルを初期化（v2には詳細なドメインモデル情報がない）
    domain_model = {
        "entities": [],
        "value_objects": [],
        "domain_services": [],
        "business_rules": [],
        "ubiquitous_language": {}
    }
    
    # 実行履歴を初期化
    execution_history = {
        "tdd_phases": {
            "RED": {"status": "not_started"},
            "GREEN": {"status": "not_started"},
            "REFACTOR": {"status": "not_started"}
        },
        "commands_executed": [{
            "command": f"/migrate-json-format {new_metadata['issue_id']}",
            "executed_at": datetime.now().isoformat(),
            "status": "success",
            "files_affected": ["migration"]
        }],
        "last_command": f"/migrate-json-format {new_metadata['issue_id']}"
    }
    
    # 既存のarchitecture_alignmentを使用
    architecture_alignment = data.get("architecture_alignment", {
        "layers": {
            "domain": False,
            "application": False,
            "infrastructure": False,
            "presentation": False
        },
        "patterns_used": []
    })
    
    # 既存の依存関係情報を使用
    dependencies = data.get("dependencies", {"technical": [], "functional": []})
    
    # 既存のtesting_strategyを使用
    testing_strategy = data.get("testing_strategy", {
        "unit_tests": {"total": 0, "passed": 0, "failed": 0, "coverage": 0.0},
        "integration_tests": {"total": 0, "passed": 0, "failed": 0}
    })
    
    # 既存のdocumentationを使用
    documentation = data.get("documentation", {
        "vision_doc": None,
        "domain_doc": None,
        "api_doc": None,
        "test_plan": None
    })
    
    # review_historyを初期化
    review_history = []
    
    return {
        "metadata": new_metadata,
        "scenarios": scenarios,
        "acceptance_criteria": acceptance_criteria,
        "domain_model": domain_model,
        "execution_history": execution_history,
        "architecture_alignment": architecture_alignment,
        "dependencies": dependencies,
        "testing_strategy": testing_strategy,
        "documentation": documentation,
        "review_history": review_history
    }


def migrate_json_file(file_path, dry_run=False):
    """個別JSONファイルを移行"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    format_version = detect_format_version(data)
    
    if format_version == "new":
        return {"status": "skipped", "reason": "既に新フォーマットです"}
    
    if format_version == "unknown":
        return {"status": "failed", "reason": "不明なフォーマットです"}
    
    # バックアップを作成
    if not dry_run:
        backup_path = backup_file(file_path)
    else:
        backup_path = "dry_run"
    
    # 移行処理
    try:
        if format_version == "old_v1":
            migrated_data = migrate_from_old_v1(data)
        elif format_version == "old_v2":
            migrated_data = migrate_from_old_v2(data)
        else:
            return {"status": "failed", "reason": f"未対応フォーマット: {format_version}"}
        
        # 新フォーマットで保存
        if not dry_run:
            save_use_case_json(file_path, migrated_data)
        
        return {
            "status": "success",
            "old_format": format_version,
            "backup_path": backup_path,
            "migrated_data": migrated_data if dry_run else None
        }
        
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print(f"📋 詳細エラー情報 ({file_path}):")
        print(f"   フォーマット: {format_version}")
        print(f"   エラー: {str(e)}")
        print(f"   スタックトレース:")
        for line in error_details.split('\n')[-10:]:
            if line.strip():
                print(f"     {line}")
        return {"status": "failed", "reason": f"移行エラー: {str(e)}"}


def main():
    """メイン処理"""
    
    # 引数処理
    dry_run = "--dry-run" in sys.argv
    specific_file = None
    
    if len(sys.argv) >= 2 and not sys.argv[1].startswith("--"):
        specific_file = sys.argv[1]
    
    print(f"\n🔄 JSONフォーマット移行ツール")
    if dry_run:
        print("   （ドライランモード - ファイルは変更されません）")
    print("━" * 60)
    
    # 対象ファイルを決定
    if specific_file:
        if Path(specific_file).exists():
            target_files = [specific_file]
        else:
            print(f"❌ ファイルが見つかりません: {specific_file}")
            return
    else:
        target_files = find_all_use_case_jsons()
    
    if not target_files:
        print("❌ 対象ファイルが見つかりません")
        return
    
    print(f"📁 対象ファイル数: {len(target_files)}件")
    print()
    
    # 移行実行
    results = {
        "success": [],
        "skipped": [],
        "failed": []
    }
    
    for file_path in target_files:
        print(f"🔍 {file_path}")
        result = migrate_json_file(file_path, dry_run)
        
        status = result["status"]
        results[status].append({
            "file": file_path,
            "result": result
        })
        
        if status == "success":
            print(f"  ✅ 移行成功 ({result['old_format']} → new)")
            if not dry_run:
                print(f"  📦 バックアップ: {result['backup_path']}")
        elif status == "skipped":
            print(f"  ⏭️ スキップ: {result['reason']}")
        elif status == "failed":
            print(f"  ❌ 移行失敗: {result['reason']}")
        
        print()
    
    # サマリー表示
    print("📊 移行結果サマリー")
    print("━" * 40)
    print(f"✅ 成功: {len(results['success'])}件")
    print(f"⏭️ スキップ: {len(results['skipped'])}件") 
    print(f"❌ 失敗: {len(results['failed'])}件")
    
    if results["failed"]:
        print(f"\n❌ 失敗したファイル:")
        for item in results["failed"]:
            print(f"  - {item['file']}: {item['result']['reason']}")
    
    if results["success"]:
        print(f"\n✅ 移行成功したファイル:")
        for item in results["success"]:
            print(f"  - {item['file']}")
            if not dry_run:
                print(f"    バックアップ: {item['result']['backup_path']}")
    
    # 次のステップ
    if not dry_run and results["success"]:
        print(f"\n⏭️ 次の推奨ステップ:")
        print(f"1. 移行結果の確認:")
        print(f"   新しいフォーマットが正しく適用されているか確認してください")
        print(f"2. テスト実行:")
        print(f"   uv run --frozen pytest tests/ -v")
        print(f"3. バックアップの管理:")
        print(f"   移行が正常に完了したら、バックアップファイルを削除できます")
    
    if dry_run:
        print(f"\n💡 実際の移行を実行するには:")
        print(f"   python3 98-migrate-json-format.py")
        print(f"   （--dry-runオプションを外して実行）")


if __name__ == "__main__":
    main()