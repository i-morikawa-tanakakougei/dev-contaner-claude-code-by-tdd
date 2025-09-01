#!/usr/bin/env python3
"""
Evolve Scenarios Command - 改修版
シナリオ進化を実行し、実行履歴を更新
"""

import json
import os
import sys
import subprocess
import time
from datetime import datetime
from pathlib import Path
import re
from typing import Dict, Any, List, Optional, Tuple

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))
from json_format_utils import (
    load_use_case_json,
    update_execution_history,
    save_use_case_json,
    format_execution_status,
    update_tdd_phase
)


def find_use_case_json(feature_name):
    """フィーチャー名からJSONファイルを検索"""
    use_cases_dir = Path("docs/use_cases")
    
    if not use_cases_dir.exists():
        return None
    
    # feature-name-*.json パターンで検索
    for json_file in use_cases_dir.glob(f"*{feature_name}*.json"):
        return str(json_file)
    
    # issue番号が含まれる可能性もあるので広範囲検索
    for json_file in use_cases_dir.glob("*.json"):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if feature_name.lower() in content.lower():
                    return str(json_file)
        except:
            continue
    
    return None


def collect_development_insights(feature_name: str) -> List[Dict[str, Any]]:
    """開発フェーズから得られたインサイトを収集"""
    print(f"🔍 フィーチャー '{feature_name}' の開発インサイトを収集中...")
    
    insights = []
    
    # テストファイルから失敗パターンやエッジケースを抽出
    try:
        test_files = list(Path("tests").rglob("*.py")) if Path("tests").exists() else []
        for test_file in test_files:
            if feature_name.lower() in test_file.name.lower():
                try:
                    with open(test_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # エラーケースやエッジケースのテストを特定
                    edge_cases = re.findall(r'def test_.*(?:error|edge|fail|invalid|boundary|limit).*\(', content)
                    for case in edge_cases[:5]:  # 最大5件
                        insights.append({
                            "source": "test_analysis",
                            "type": "edge_case",
                            "content": f"Edge case discovered in tests: {case}",
                            "file": str(test_file),
                            "priority": "medium",
                            "category": "testing_insights"
                        })
                    
                    # TODO/FIXMEコメントから改善点を抽出
                    todos = re.findall(r'#\s*(TODO|FIXME|XXX):\s*(.+)', content)
                    for todo_type, todo_content in todos[:3]:
                        insights.append({
                            "source": "test_analysis",
                            "type": "improvement_opportunity",
                            "content": f"{todo_type}: {todo_content.strip()}",
                            "file": str(test_file),
                            "priority": "low",
                            "category": "technical_debt"
                        })
                
                except Exception:
                    continue
    
    except Exception:
        print("⚠️ テストファイル分析でエラーが発生")
    
    # ドメインファイルから複雑なビジネスルールを抽出
    try:
        src_files = list(Path("src").rglob("*.py")) if Path("src").exists() else []
        for src_file in src_files:
            if feature_name.lower() in str(src_file).lower():
                try:
                    with open(src_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # 複雑な条件分岐やバリデーションを特定
                    complex_conditions = re.findall(r'if\s+.*(?:and|or).*(?:and|or).*:', content)
                    for condition in complex_conditions[:3]:
                        insights.append({
                            "source": "code_analysis",
                            "type": "complex_scenario",
                            "content": f"Complex business rule: {condition.strip()}",
                            "file": str(src_file),
                            "priority": "high",
                            "category": "business_logic"
                        })
                    
                    # 例外処理から潜在的なエラーシナリオを抽出
                    exceptions = re.findall(r'except\s+(\w+Error\w*):', content)
                    for exception in set(exceptions[:5]):
                        insights.append({
                            "source": "code_analysis",
                            "type": "error_scenario",
                            "content": f"Error handling for: {exception}",
                            "file": str(src_file),
                            "priority": "medium",
                            "category": "error_handling"
                        })
                
                except Exception:
                    continue
    
    except Exception:
        print("⚠️ ソースコード分析でエラーが発生")
    
    print(f"✅ {len(insights)}件の開発インサイトを収集")
    return insights


def collect_sprint_feedback(feature_name: str) -> List[Dict[str, Any]]:
    """スプリントフィードバックを収集"""
    print(f"📋 フィーチャー '{feature_name}' のスプリントフィードバックを収集中...")
    
    feedback_items = []
    
    # スプリントレトロスペクティブファイルの検索
    docs_dir = Path("docs")
    feedback_sources = []
    
    if docs_dir.exists():
        # スプリント関連ファイル
        feedback_sources.extend(docs_dir.rglob("*retrospective*.md"))
        feedback_sources.extend(docs_dir.rglob("*feedback*.md"))
        feedback_sources.extend(docs_dir.rglob("*sprint*.md"))
    
    for feedback_file in feedback_sources[:5]:  # 最大5ファイル
        try:
            with open(feedback_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # フィーチャー名に関連する内容を抽出
            if feature_name.lower() in content.lower():
                # 改善提案や要望を抽出
                improvement_sections = re.findall(
                    r'(?:改善|要望|問題|課題|機能拡張)[:：]\s*(.+)', 
                    content, re.IGNORECASE
                )
                
                for improvement in improvement_sections[:3]:
                    feedback_items.append({
                        "source": "sprint_feedback",
                        "type": "improvement_request",
                        "content": improvement.strip(),
                        "file": str(feedback_file),
                        "priority": "medium",
                        "category": "feature_enhancement"
                    })
                
                # ユーザーストーリーや要件を抽出
                user_stories = re.findall(
                    r'(?:ユーザー|利用者|顧客).*(?:したい|希望|要求|必要)', 
                    content, re.IGNORECASE
                )
                
                for story in user_stories[:2]:
                    feedback_items.append({
                        "source": "sprint_feedback",
                        "type": "user_story",
                        "content": story.strip(),
                        "file": str(feedback_file),
                        "priority": "high",
                        "category": "user_requirements"
                    })
        
        except Exception:
            continue
    
    print(f"✅ {len(feedback_items)}件のスプリントフィードバックを収集")
    return feedback_items


def collect_github_feedback(feature_name: str) -> List[Dict[str, Any]]:
    """GitHubからフィーチャー関連のフィードバックを収集"""
    print(f"🐙 GitHub上でフィーチャー '{feature_name}' 関連のフィードバックを収集中...")
    
    feedback_items = []
    
    try:
        # 関連イシューを検索
        result = subprocess.run([
            "gh", "issue", "list", "--search", feature_name, 
            "--json", "number,title,body,comments,labels", "--limit", "5"
        ], capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            issues = json.loads(result.stdout)
            
            for issue in issues:
                # イシュー本文から要件を抽出
                body = issue.get("body", "")
                if any(keyword in body.lower() for keyword in ["requirement", "feature", "enhancement", "scenario"]):
                    feedback_items.append({
                        "source": f"github_issue_{issue['number']}",
                        "type": "feature_requirement",
                        "content": body[:400],  # 最初の400文字
                        "priority": "high",
                        "issue_number": issue['number'],
                        "category": "github_requirements"
                    })
                
                # コメントから要望を抽出
                comments = issue.get("comments", [])
                for comment in comments[-3:]:  # 最新3コメント
                    comment_body = comment.get("body", "").lower()
                    if any(keyword in comment_body for keyword in ["suggest", "improve", "enhance", "add", "need"]):
                        feedback_items.append({
                            "source": f"github_comment_issue_{issue['number']}",
                            "type": "enhancement_suggestion",
                            "content": comment.get("body", "")[:300],
                            "priority": "medium",
                            "author": comment.get("author", {}).get("login", "unknown"),
                            "category": "github_feedback"
                        })
        
        # 関連PRからのフィードバック収集
        pr_result = subprocess.run([
            "gh", "pr", "list", "--search", feature_name, 
            "--json", "number,title,comments", "--limit", "3"
        ], capture_output=True, text=True, timeout=30)
        
        if pr_result.returncode == 0:
            prs = json.loads(pr_result.stdout)
            for pr in prs:
                comments = pr.get("comments", [])
                for comment in comments[-2:]:  # PR最新2コメント
                    comment_body = comment.get("body", "").lower()
                    if any(keyword in comment_body for keyword in ["review", "change", "improve", "consider"]):
                        feedback_items.append({
                            "source": f"github_pr_{pr['number']}",
                            "type": "code_review_feedback",
                            "content": comment.get("body", "")[:300],
                            "priority": "medium",
                            "pr_number": pr['number'],
                            "category": "github_review"
                        })
    
    except subprocess.TimeoutExpired:
        print("⚠️ GitHub API request timed out")
    except FileNotFoundError:
        print("⚠️ gh CLI not available")
    except json.JSONDecodeError:
        print("⚠️ GitHub API response parsing failed")
    
    print(f"✅ {len(feedback_items)}件のGitHubフィードバックを収集")
    return feedback_items


def generate_evolved_scenarios(feedback_items: List[Dict[str, Any]], feature_name: str) -> List[Dict[str, Any]]:
    """収集したフィードバックから進化シナリオを生成"""
    print(f"🌱 フィードバックから進化シナリオを生成中...")
    
    scenarios = []
    
    # カテゴリ別にフィードバックをグループ化
    categories = {}
    for item in feedback_items:
        category = item.get("category", "general")
        if category not in categories:
            categories[category] = []
        categories[category].append(item)
    
    scenario_id = 1
    
    # カテゴリ別にシナリオを生成
    for category, items in categories.items():
        if not items:
            continue
        
        # 高優先度のアイテムからシナリオを作成
        high_priority_items = [item for item in items if item.get("priority") == "high"]
        medium_priority_items = [item for item in items if item.get("priority") == "medium"]
        
        # 高優先度のシナリオ生成
        for item in high_priority_items[:3]:  # 最大3個
            scenario = generate_scenario_from_feedback(item, scenario_id, feature_name)
            if scenario:
                scenarios.append(scenario)
                scenario_id += 1
        
        # 中優先度のシナリオ生成（高優先度が少ない場合）
        if len(high_priority_items) < 2:
            for item in medium_priority_items[:2]:
                scenario = generate_scenario_from_feedback(item, scenario_id, feature_name)
                if scenario:
                    scenarios.append(scenario)
                    scenario_id += 1
    
    print(f"✅ {len(scenarios)}個の進化シナリオを生成")
    return scenarios


def generate_scenario_from_feedback(feedback_item: Dict[str, Any], scenario_id: int, feature_name: str) -> Optional[Dict[str, Any]]:
    """個別のフィードバックからGiven-When-Thenシナリオを生成"""
    
    content = feedback_item.get("content", "")
    item_type = feedback_item.get("type", "unknown")
    category = feedback_item.get("category", "general")
    
    # シナリオテンプレートの選択
    scenario_templates = {
        "edge_case": {
            "given": f"the system is in an edge case condition related to {feature_name}",
            "when": "the user performs an action that triggers boundary conditions",
            "then": "the system should handle the edge case gracefully"
        },
        "error_scenario": {
            "given": f"the {feature_name} feature encounters an error condition",
            "when": "the user attempts an operation that may fail",
            "then": "the system should provide clear error feedback and recovery options"
        },
        "performance_scenario": {
            "given": f"the {feature_name} feature is under high load",
            "when": "multiple users perform operations simultaneously",
            "then": "the system should maintain acceptable response times"
        },
        "security_scenario": {
            "given": f"a user attempts to access {feature_name} functionality",
            "when": "the user has insufficient permissions or malicious intent",
            "then": "the system should enforce proper authorization and log security events"
        },
        "integration_scenario": {
            "given": f"the {feature_name} feature needs to interact with external systems",
            "when": "integration points are used",
            "then": "the system should handle integration failures gracefully"
        }
    }
    
    # フィードバック内容に基づいてシナリオタイプを決定
    scenario_type = "edge_case"  # デフォルト
    
    if any(keyword in content.lower() for keyword in ["error", "fail", "exception", "bug"]):
        scenario_type = "error_scenario"
    elif any(keyword in content.lower() for keyword in ["performance", "speed", "slow", "fast", "load"]):
        scenario_type = "performance_scenario"
    elif any(keyword in content.lower() for keyword in ["security", "auth", "permission", "access"]):
        scenario_type = "security_scenario"
    elif any(keyword in content.lower() for keyword in ["integration", "api", "external", "service"]):
        scenario_type = "integration_scenario"
    
    template = scenario_templates[scenario_type]
    
    # シナリオの詳細化
    scenario = {
        "id": f"evolved_{scenario_id:02d}",
        "title": f"Evolved Scenario: {item_type.replace('_', ' ').title()}",
        "type": scenario_type,
        "priority": feedback_item.get("priority", "medium"),
        "source_feedback": {
            "source": feedback_item.get("source", "unknown"),
            "type": feedback_item.get("type", "unknown"),
            "category": category
        },
        "given": template["given"],
        "when": template["when"],
        "then": template["then"],
        "acceptance_criteria": [
            f"The {feature_name} feature handles the scenario appropriately",
            "Error cases are properly managed",
            "User experience remains smooth",
            "System maintains stability"
        ],
        "discovered_at": datetime.now().isoformat(),
        "implementation_notes": f"Based on feedback: {content[:200]}..."
    }
    
    return scenario


def create_evolved_scenarios_document(feature_name: str, scenarios: List[Dict[str, Any]], 
                                    feedback_summary: Dict[str, Any]) -> str:
    """進化シナリオ文書を作成"""
    print(f"📝 進化シナリオ文書を作成中...")
    
    evolved_dir = Path("docs/use_cases/evolved")
    evolved_dir.mkdir(parents=True, exist_ok=True)
    
    doc_path = evolved_dir / f"{feature_name}-evolved-scenarios.md"
    
    # 文書内容の生成
    content = f"""# {feature_name.title()} - Evolved Scenarios

## 📋 Discovery Summary

**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Feature**: {feature_name}
**Total Scenarios**: {len(scenarios)}

## 🔍 Discovery Sources

### Feedback Collection Results
- **Development Insights**: {feedback_summary.get('development_insights', 0)} items
- **Sprint Feedback**: {feedback_summary.get('sprint_feedback', 0)} items  
- **GitHub Feedback**: {feedback_summary.get('github_feedback', 0)} items
- **Total Feedback Items**: {feedback_summary.get('total_items', 0)} items

### Source Distribution
"""
    
    # ソース別統計
    source_stats = {}
    for scenario in scenarios:
        source = scenario.get("source_feedback", {}).get("source", "unknown")
        source_stats[source] = source_stats.get(source, 0) + 1
    
    for source, count in source_stats.items():
        content += f"- **{source}**: {count} scenarios\n"
    
    content += "\n## 🌱 Evolved Scenarios\n\n"
    
    # シナリオ別詳細
    for i, scenario in enumerate(scenarios, 1):
        content += f"### Scenario {i}: {scenario['title']}\n\n"
        content += f"**Type**: {scenario['type']}\n"
        content += f"**Priority**: {scenario['priority']}\n"
        content += f"**Source**: {scenario['source_feedback']['source']}\n\n"
        
        content += "**Given-When-Then:**\n"
        content += f"- **Given**: {scenario['given']}\n"
        content += f"- **When**: {scenario['when']}\n"
        content += f"- **Then**: {scenario['then']}\n\n"
        
        content += "**Acceptance Criteria:**\n"
        for criteria in scenario['acceptance_criteria']:
            content += f"- {criteria}\n"
        
        content += f"\n**Implementation Notes:**\n{scenario['implementation_notes']}\n\n"
        content += "---\n\n"
    
    # ビジョン整合性チェック
    content += """## 🎯 Vision Consistency Check

### Alignment Verification
- [ ] All scenarios align with project vision
- [ ] No conflicting requirements identified
- [ ] Domain boundaries respected
- [ ] Architecture principles maintained

### Integration Readiness
- [ ] Scenarios are ready for sprint integration
- [ ] Implementation priority defined
- [ ] Resource requirements estimated
- [ ] Dependencies identified

## 🔄 Next Steps

### Sprint Integration
1. **Sprint Planning Update**: Integrate new scenarios into backlog
2. **Issue Creation**: Create GitHub issues for high-priority scenarios
3. **Development Cycle**: Begin implementation using TDD/DDD/Layered approach

### Recommended Commands
```bash
# Integrate scenarios into next sprint
/sprint-planning [next-sprint-number]

# Start implementation of high-priority scenarios  
/create-use-case [new-issue-number]
```

## 📊 Evolution Metrics

"""
    
    # メトリクス
    type_stats = {}
    priority_stats = {}
    
    for scenario in scenarios:
        scenario_type = scenario.get("type", "unknown")
        priority = scenario.get("priority", "unknown")
        
        type_stats[scenario_type] = type_stats.get(scenario_type, 0) + 1
        priority_stats[priority] = priority_stats.get(priority, 0) + 1
    
    content += "### Scenario Type Distribution\n"
    for scenario_type, count in type_stats.items():
        content += f"- **{scenario_type}**: {count} scenarios\n"
    
    content += "\n### Priority Distribution\n"
    for priority, count in priority_stats.items():
        content += f"- **{priority}**: {count} scenarios\n"
    
    content += f"\n**Total Evolution Score**: {len(scenarios) * 10}/100\n"
    
    # ファイルに保存
    with open(doc_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ 進化シナリオ文書を作成: {doc_path}")
    return str(doc_path)


def create_evolution_metadata(feature_name: str, scenarios: List[Dict[str, Any]], 
                            feedback_summary: Dict[str, Any]) -> str:
    """進化メタデータファイルを作成"""
    
    evolved_dir = Path("docs/use_cases/evolved")
    evolved_dir.mkdir(parents=True, exist_ok=True)
    
    metadata_path = evolved_dir / f"{feature_name}-metadata.json"
    
    # タイプ別統計
    type_counts = {}
    priority_counts = {}
    
    for scenario in scenarios:
        scenario_type = scenario.get("type", "unknown")
        priority = scenario.get("priority", "unknown")
        
        type_counts[scenario_type] = type_counts.get(scenario_type, 0) + 1
        priority_counts[priority] = priority_counts.get(priority, 0) + 1
    
    metadata = {
        "feature_name": feature_name,
        "evolution_timestamp": datetime.now().isoformat(),
        "discovered_scenarios": {
            "total": len(scenarios),
            "by_type": type_counts,
            "by_priority": priority_counts
        },
        "discovery_sources": {
            "development_insights": feedback_summary.get("development_insights", 0),
            "sprint_feedback": feedback_summary.get("sprint_feedback", 0),
            "github_feedback": feedback_summary.get("github_feedback", 0)
        },
        "vision_alignment": "confirmed",
        "sprint_integration": "ready",
        "evolution_score": len(scenarios) * 10,
        "next_steps": [
            "Sprint planning integration",
            "Issue creation for high-priority scenarios",
            "Development cycle initiation"
        ]
    }
    
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    
    print(f"✅ 進化メタデータを作成: {metadata_path}")
    return str(metadata_path)


def update_use_case_json_with_evolution(json_file_path: str, scenarios: List[Dict[str, Any]], 
                                      metadata_path: str, feature_name: str):
    """ユースケースJSONに進化情報を更新"""
    
    use_case_data = load_use_case_json(json_file_path)
    
    # 進化情報を更新
    evolution_info = use_case_data.get("implementation_details", {})
    evolution_info["scenario_evolution"] = {
        "completed": True,
        "timestamp": datetime.now().isoformat(),
        "feature_name": feature_name,
        "evolved_scenarios_count": len(scenarios),
        "evolution_document": f"docs/use_cases/evolved/{feature_name}-evolved-scenarios.md",
        "metadata_file": metadata_path,
        "scenario_types": list(set(s.get("type", "unknown") for s in scenarios)),
        "priority_distribution": {
            "high": len([s for s in scenarios if s.get("priority") == "high"]),
            "medium": len([s for s in scenarios if s.get("priority") == "medium"]), 
            "low": len([s for s in scenarios if s.get("priority") == "low"])
        },
        "next_actions": [
            "Sprint planning integration",
            "Issue creation for evolved scenarios",
            "Development cycle planning"
        ]
    }
    use_case_data["implementation_details"] = evolution_info
    
    # TDDフェーズを更新
    update_tdd_phase(use_case_data, "scenario_evolution")
    
    # 保存
    save_use_case_json(json_file_path, use_case_data)
    
    return use_case_data


def main():
    """メイン処理"""
    
    # 引数チェック
    if len(sys.argv) < 2:
        print("❌ エラー: フィーチャー名が必要です")
        print("使用方法: /evolve-scenarios <feature-name>")
        sys.exit(1)
    
    feature_name = sys.argv[1]
    print(f"\n🌱 フィーチャー '{feature_name}' のシナリオ進化を開始します\n")
    
    # ユースケースJSONファイルを検索
    print("📁 関連するユースケースJSONファイルを検索中...")
    json_file_path = find_use_case_json(feature_name)
    
    if not json_file_path:
        print(f"⚠️ フィーチャー '{feature_name}' 関連のユースケースJSONが見つかりません")
        print("進化シナリオは作成しますが、履歴更新はスキップします")
        # 続行する（新しいフィーチャーの場合もある）
    else:
        print(f"✅ JSONファイルを発見: {json_file_path}")
    
    # フィードバック収集
    print("\n📋 フィードバック収集")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    # 開発インサイト収集
    development_insights = collect_development_insights(feature_name)
    
    # スプリントフィードバック収集
    sprint_feedback = collect_sprint_feedback(feature_name)
    
    # GitHubフィードバック収集
    github_feedback = collect_github_feedback(feature_name)
    
    # フィードバック統合
    all_feedback = development_insights + sprint_feedback + github_feedback
    
    feedback_summary = {
        "development_insights": len(development_insights),
        "sprint_feedback": len(sprint_feedback),
        "github_feedback": len(github_feedback),
        "total_items": len(all_feedback)
    }
    
    print(f"\n📊 フィードバック収集結果:")
    print(f"  • 開発インサイト: {feedback_summary['development_insights']}件")
    print(f"  • スプリントフィードバック: {feedback_summary['sprint_feedback']}件")
    print(f"  • GitHubフィードバック: {feedback_summary['github_feedback']}件")
    print(f"  • 総計: {feedback_summary['total_items']}件")
    
    if not all_feedback:
        print("ℹ️ 進化対象のフィードバックが見つかりませんでした")
        print("現在のシナリオは十分に成熟している可能性があります")
        
        # 実行履歴を更新（該当なしとして記録）
        if json_file_path:
            update_execution_history(
                json_file_path,
                f"/evolve-scenarios {feature_name}",
                "success",
                ["No evolution feedback found - scenarios are mature"]
            )
        sys.exit(0)
    
    # 進化シナリオ生成
    print("\n🌱 進化シナリオ生成")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    evolved_scenarios = generate_evolved_scenarios(all_feedback, feature_name)
    
    if not evolved_scenarios:
        print("ℹ️ 具体的な進化シナリオを生成できませんでした")
        print("収集されたフィードバックは一般的すぎるか、既に対応済みの可能性があります")
        
        if json_file_path:
            update_execution_history(
                json_file_path,
                f"/evolve-scenarios {feature_name}",
                "success",
                ["Feedback collected but no specific scenarios evolved"]
            )
        sys.exit(0)
    
    # 進化シナリオ文書作成
    print("\n📝 進化シナリオ文書作成")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    document_path = create_evolved_scenarios_document(feature_name, evolved_scenarios, feedback_summary)
    
    # メタデータ作成
    metadata_path = create_evolution_metadata(feature_name, evolved_scenarios, feedback_summary)
    
    # ユースケースJSONを更新（見つかった場合）
    if json_file_path:
        print("\n📊 ユースケースJSONを更新中...")
        final_data = update_use_case_json_with_evolution(json_file_path, evolved_scenarios, metadata_path, feature_name)
        
        # 実行履歴を更新
        created_files = [
            document_path,
            metadata_path,
            f"{len(evolved_scenarios)} evolved scenarios created"
        ]
        
        update_execution_history(
            json_file_path,
            f"/evolve-scenarios {feature_name}",
            "success",
            created_files
        )
        
        # 実行状況を表示
        print("\n" + "="*60)
        print(format_execution_status(final_data))
        print("="*60)
    
    # 最終サマリー表示
    print(f"\n🎉 シナリオ進化完了")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"📋 進化結果:")
    print(f"  • フィーチャー: {feature_name}")
    print(f"  • 生成シナリオ数: {len(evolved_scenarios)}個")
    print(f"  • 進化文書: {document_path}")
    print(f"  • メタデータ: {metadata_path}")
    
    # シナリオタイプ別統計
    type_stats = {}
    priority_stats = {}
    
    for scenario in evolved_scenarios:
        scenario_type = scenario.get("type", "unknown")
        priority = scenario.get("priority", "unknown")
        
        type_stats[scenario_type] = type_stats.get(scenario_type, 0) + 1
        priority_stats[priority] = priority_stats.get(priority, 0) + 1
    
    print(f"\n📊 シナリオ分析:")
    print(f"  タイプ別:")
    for scenario_type, count in type_stats.items():
        print(f"    • {scenario_type}: {count}個")
    
    print(f"  優先度別:")
    for priority, count in priority_stats.items():
        print(f"    • {priority}: {count}個")
    
    evolution_score = len(evolved_scenarios) * 10
    print(f"\n🏆 進化スコア: {evolution_score}/100")
    
    print(f"\n⏭️ 次の推奨コマンド")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"1. 次回スプリント計画への統合")
    print(f"   → 新しいシナリオをバックログに追加")
    print(f"2. 高優先度シナリオのイシュー作成")
    print(f"   → GitHub上で新しいイシューを作成")
    print(f"3. 開発サイクル開始")
    print(f"   → /create-use-case [新イシュー番号]")
    
    if json_file_path:
        print(f"4. /project-status")
        print(f"   → プロジェクト全体の進捗確認")
    
    print(f"\n💡 シナリオ進化完了")
    if evolution_score >= 50:
        print("十分な数の価値ある進化シナリオが発見されました！")
    elif evolution_score >= 20:
        print("いくつかの有用な進化シナリオが発見されました。")
    else:
        print("現在のシナリオは既に十分に成熟しているようです。")


if __name__ == "__main__":
    main()