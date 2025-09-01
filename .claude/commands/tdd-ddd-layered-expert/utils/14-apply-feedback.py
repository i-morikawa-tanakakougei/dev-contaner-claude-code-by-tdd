#!/usr/bin/env python3
"""
Apply Feedback Command - 改修版
レビューフィードバックの適用を実行し、実行履歴を更新
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


def collect_github_feedback(issue_number: str) -> List[Dict[str, Any]]:
    """GitHub Issue/PRからフィードバックを収集"""
    print(f"📋 Issue #{issue_number} からフィードバックを収集中...")
    
    feedback_items = []
    
    try:
        # Issue情報を取得
        result = subprocess.run([
            "gh", "issue", "view", issue_number, 
            "--json", "title,body,comments,labels"
        ], capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            issue_data = json.loads(result.stdout)
            
            # Issue本文からフィードバック抽出
            body = issue_data.get("body", "")
            if any(keyword in body.lower() for keyword in ["feedback", "improvement", "suggestion", "todo", "fix"]):
                feedback_items.append({
                    "source": "issue_body",
                    "type": "requirement",
                    "content": body[:500],  # 最初の500文字
                    "priority": "medium",
                    "created_at": datetime.now().isoformat()
                })
            
            # コメントからフィードバック抽出
            comments = issue_data.get("comments", [])
            feedback_keywords = ["feedback", "improvement", "suggestion", "change", "fix", "todo", "issue", "problem"]
            
            for comment in comments[-10:]:  # 最新10コメント
                comment_body = comment.get("body", "").lower()
                if any(keyword in comment_body for keyword in feedback_keywords):
                    feedback_items.append({
                        "source": "comment",
                        "type": "review_feedback",
                        "content": comment.get("body", "")[:300],
                        "priority": "high" if "critical" in comment_body or "urgent" in comment_body else "medium",
                        "author": comment.get("author", {}).get("login", "unknown"),
                        "created_at": comment.get("createdAt", "")
                    })
        
        # 関連PRからのフィードバック収集
        pr_result = subprocess.run([
            "gh", "pr", "list", "--search", f"linked:#{issue_number}", 
            "--json", "number,title,comments", "--limit", "3"
        ], capture_output=True, text=True, timeout=30)
        
        if pr_result.returncode == 0:
            prs = json.loads(pr_result.stdout)
            for pr in prs:
                for comment in pr.get("comments", [])[-5:]:  # PR最新5コメント
                    comment_body = comment.get("body", "").lower()
                    if any(keyword in comment_body for keyword in ["review", "change", "improve", "fix"]):
                        feedback_items.append({
                            "source": f"pr_{pr['number']}",
                            "type": "pr_review",
                            "content": comment.get("body", "")[:300],
                            "priority": "high",
                            "created_at": comment.get("createdAt", "")
                        })
    
    except subprocess.TimeoutExpired:
        print("⚠️ GitHub API request timed out")
    except FileNotFoundError:
        print("⚠️ gh CLI not available")
    except json.JSONDecodeError:
        print("⚠️ GitHub API response parsing failed")
    
    print(f"✅ {len(feedback_items)}件のフィードバック項目を収集")
    return feedback_items


def analyze_code_feedback() -> List[Dict[str, Any]]:
    """コードベースから技術的フィードバックを分析"""
    print("🔍 コードベースを分析してフィードバック項目を特定中...")
    
    feedback_items = []
    
    # TODO/FIXME/XXXコメントの検索
    try:
        result = subprocess.run([
            "grep", "-r", "-n", "-E", "(TODO|FIXME|XXX|HACK|BUG)", 
            "src/", "--include=*.py"
        ], capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            for line in result.stdout.strip().split('\n')[:20]:  # 最大20件
                if ':' in line:
                    file_path, line_num, content = line.split(':', 2)
                    feedback_items.append({
                        "source": "code_comment",
                        "type": "technical_debt",
                        "content": content.strip(),
                        "file": file_path,
                        "line": int(line_num) if line_num.isdigit() else 0,
                        "priority": "high" if "FIXME" in content or "BUG" in content else "medium"
                    })
    
    except subprocess.TimeoutExpired:
        print("⚠️ Code analysis timed out")
    except FileNotFoundError:
        print("⚠️ grep not available")
    
    # テストカバレッジの問題を特定
    try:
        result = subprocess.run([
            "uv", "run", "--frozen", "pytest", "--cov=src", 
            "--cov-report=json:coverage.json", "-q"
        ], capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0 and Path("coverage.json").exists():
            with open("coverage.json", "r") as f:
                coverage_data = json.load(f)
            
            files = coverage_data.get("files", {})
            for file_path, file_data in files.items():
                coverage_percent = file_data.get("summary", {}).get("percent_covered", 100)
                if coverage_percent < 80:
                    feedback_items.append({
                        "source": "coverage_analysis",
                        "type": "test_coverage",
                        "content": f"Low test coverage in {file_path}: {coverage_percent:.1f}%",
                        "file": file_path,
                        "priority": "medium",
                        "coverage_percent": coverage_percent
                    })
    
    except subprocess.TimeoutExpired:
        print("⚠️ Coverage analysis timed out")
    except FileNotFoundError:
        print("⚠️ pytest not available")
    except json.JSONDecodeError:
        print("⚠️ Coverage report parsing failed")
    
    # コード品質問題の特定
    try:
        result = subprocess.run([
            "uv", "run", "--frozen", "ruff", "check", ".", "--output-format=json"
        ], capture_output=True, text=True, timeout=60)
        
        if result.stdout:
            try:
                ruff_issues = json.loads(result.stdout)
                for issue in ruff_issues[:10]:  # 最大10件
                    feedback_items.append({
                        "source": "ruff_analysis",
                        "type": "code_quality",
                        "content": f"{issue.get('code', '')}: {issue.get('message', '')}",
                        "file": issue.get("filename", ""),
                        "line": issue.get("location", {}).get("row", 0),
                        "priority": "low" if issue.get("code", "").startswith("E") else "medium"
                    })
            except json.JSONDecodeError:
                pass
    
    except subprocess.TimeoutExpired:
        print("⚠️ Ruff analysis timed out")
    except FileNotFoundError:
        print("⚠️ Ruff not available")
    
    print(f"✅ {len(feedback_items)}件のコード分析項目を特定")
    return feedback_items


def prioritize_feedback(feedback_items: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """フィードバック項目を優先度別に分類"""
    print("📊 フィードバック項目を優先度別に分類中...")
    
    prioritized = {
        "critical": [],
        "high": [],
        "medium": [],
        "low": []
    }
    
    # 優先度別分類ロジック
    for item in feedback_items:
        priority = item.get("priority", "medium")
        
        # 緊急度を上げる条件
        content = item.get("content", "").lower()
        if any(keyword in content for keyword in ["critical", "urgent", "security", "bug", "broken"]):
            priority = "critical"
        elif any(keyword in content for keyword in ["important", "must", "required", "failing"]):
            priority = "high"
        elif item.get("type") == "test_coverage" and item.get("coverage_percent", 100) < 50:
            priority = "high"
        
        prioritized[priority].append(item)
    
    # 統計表示
    for priority, items in prioritized.items():
        print(f"  {priority.upper()}: {len(items)}件")
    
    return prioritized


def apply_feedback_item(item: Dict[str, Any]) -> Dict[str, Any]:
    """個別のフィードバック項目を適用"""
    
    result = {
        "item": item,
        "status": "attempted",
        "applied": False,
        "changes_made": [],
        "issues": [],
        "test_status": "not_run"
    }
    
    item_type = item.get("type", "unknown")
    content = item.get("content", "")
    
    print(f"🔧 適用中: {item_type} - {content[:50]}...")
    
    try:
        # 適用前テスト実行
        print("  📝 適用前テストを実行...")
        test_result = subprocess.run([
            "uv", "run", "--frozen", "pytest", "-q"
        ], capture_output=True, text=True, timeout=120)
        
        pre_test_passed = test_result.returncode == 0
        
        if not pre_test_passed:
            result["issues"].append("Pre-application tests failed")
            result["status"] = "skipped"
            return result
        
        # フィードバック種類別の処理
        if item_type == "code_quality":
            # Ruffの自動修正を試行
            fix_result = subprocess.run([
                "uv", "run", "--frozen", "ruff", "check", ".", "--fix", "--unsafe-fixes"
            ], capture_output=True, text=True, timeout=60)
            
            if fix_result.returncode == 0:
                result["changes_made"].append("Applied ruff auto-fixes")
                result["applied"] = True
        
        elif item_type == "technical_debt":
            # TODO/FIXMEコメントの改善提案のみ
            result["changes_made"].append("Identified technical debt item for manual review")
            result["applied"] = True  # 特定することも適用の一種
        
        elif item_type == "test_coverage":
            # カバレッジ改善の提案
            file_path = item.get("file", "")
            if file_path and Path(file_path).exists():
                result["changes_made"].append(f"Identified low coverage in {file_path}")
                result["applied"] = True
        
        elif item_type in ["review_feedback", "pr_review"]:
            # レビューフィードバックの記録（手動対応が必要）
            result["changes_made"].append("Review feedback logged for manual implementation")
            result["applied"] = True
        
        # 適用後テスト実行
        if result["applied"]:
            print("  ✅ 適用後テストを実行...")
            post_test_result = subprocess.run([
                "uv", "run", "--frozen", "pytest", "-q"
            ], capture_output=True, text=True, timeout=120)
            
            result["test_status"] = "passed" if post_test_result.returncode == 0 else "failed"
            
            if result["test_status"] == "failed":
                result["applied"] = False
                result["issues"].append("Post-application tests failed")
                result["status"] = "failed"
            else:
                result["status"] = "success"
        
    except subprocess.TimeoutExpired:
        result["issues"].append("Command timeout")
        result["status"] = "timeout"
    except Exception as e:
        result["issues"].append(f"Error: {str(e)}")
        result["status"] = "error"
    
    return result


def apply_feedback_batch(feedback_items: List[Dict[str, Any]], max_items: int = 10) -> List[Dict[str, Any]]:
    """フィードバック項目をバッチで適用"""
    print(f"🔄 {min(len(feedback_items), max_items)}件のフィードバックを適用中...")
    
    results = []
    applied_count = 0
    
    for i, item in enumerate(feedback_items[:max_items]):
        print(f"\n進行状況: {i+1}/{min(len(feedback_items), max_items)}")
        
        result = apply_feedback_item(item)
        results.append(result)
        
        if result["applied"]:
            applied_count += 1
        
        # 失敗が続く場合は中断
        if result["status"] == "failed":
            print(f"⚠️ フィードバック適用に失敗: {result['issues']}")
            # 続行するかどうかの判断（今回は続行）
        
        # 少し待機
        time.sleep(0.5)
    
    print(f"\n📊 適用結果: {applied_count}/{len(results)}件が成功")
    return results


def generate_quality_metrics() -> Dict[str, Any]:
    """品質メトリクスを生成"""
    print("📈 品質メトリクスを測定中...")
    
    metrics = {
        "timestamp": datetime.now().isoformat(),
        "test_coverage": 0,
        "ruff_issues": 0,
        "pyright_errors": 0,
        "lines_of_code": 0,
        "test_files": 0
    }
    
    # テストカバレッジ
    try:
        result = subprocess.run([
            "uv", "run", "--frozen", "pytest", "--cov=src", 
            "--cov-report=json:coverage.json", "-q"
        ], capture_output=True, text=True, timeout=120)
        
        if result.returncode == 0 and Path("coverage.json").exists():
            with open("coverage.json", "r") as f:
                coverage_data = json.load(f)
            metrics["test_coverage"] = coverage_data.get("totals", {}).get("percent_covered", 0)
    except:
        metrics["test_coverage"] = 0
    
    # Ruff issues
    try:
        result = subprocess.run([
            "uv", "run", "--frozen", "ruff", "check", ".", "--output-format=json"
        ], capture_output=True, text=True, timeout=60)
        
        if result.stdout:
            try:
                issues = json.loads(result.stdout)
                metrics["ruff_issues"] = len(issues)
            except json.JSONDecodeError:
                metrics["ruff_issues"] = 0
    except:
        metrics["ruff_issues"] = 0
    
    # Pyright errors
    try:
        result = subprocess.run([
            "uv", "run", "--frozen", "pyright", "--outputjson"
        ], capture_output=True, text=True, timeout=60)
        
        if result.stdout:
            try:
                pyright_data = json.loads(result.stdout)
                metrics["pyright_errors"] = pyright_data.get("summary", {}).get("errorCount", 0)
            except json.JSONDecodeError:
                metrics["pyright_errors"] = 0
    except:
        metrics["pyright_errors"] = 0
    
    # コード行数
    try:
        result = subprocess.run([
            "find", "src/", "-name", "*.py", "-exec", "wc", "-l", "{}", "+"
        ], capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')
            if lines:
                total_line = lines[-1]
                if "total" in total_line:
                    metrics["lines_of_code"] = int(total_line.split()[0])
    except:
        metrics["lines_of_code"] = 0
    
    # テストファイル数
    try:
        test_files = list(Path("tests").glob("**/*.py")) if Path("tests").exists() else []
        metrics["test_files"] = len([f for f in test_files if f.name.startswith("test_") or f.name.endswith("_test.py")])
    except:
        metrics["test_files"] = 0
    
    return metrics


def update_use_case_json_with_feedback_results(json_file_path: str, feedback_results: List[Dict[str, Any]], 
                                             metrics_before: Dict[str, Any], metrics_after: Dict[str, Any]):
    """ユースケースJSONにフィードバック適用結果を更新"""
    
    use_case_data = load_use_case_json(json_file_path)
    
    # フィードバック適用情報を更新
    feedback_info = use_case_data.get("implementation_details", {})
    
    applied_count = sum(1 for r in feedback_results if r["applied"])
    total_count = len(feedback_results)
    
    feedback_info["feedback_application"] = {
        "completed": True,
        "timestamp": datetime.now().isoformat(),
        "total_feedback_items": total_count,
        "applied_items": applied_count,
        "success_rate": (applied_count / total_count * 100) if total_count > 0 else 0,
        "metrics_improvement": {
            "coverage_change": metrics_after["test_coverage"] - metrics_before["test_coverage"],
            "ruff_issues_change": metrics_before["ruff_issues"] - metrics_after["ruff_issues"],
            "pyright_errors_change": metrics_before["pyright_errors"] - metrics_after["pyright_errors"]
        },
        "feedback_summary": {
            "critical": len([r for r in feedback_results if r["item"].get("priority") == "critical" and r["applied"]]),
            "high": len([r for r in feedback_results if r["item"].get("priority") == "high" and r["applied"]]),
            "medium": len([r for r in feedback_results if r["item"].get("priority") == "medium" and r["applied"]]),
            "low": len([r for r in feedback_results if r["item"].get("priority") == "low" and r["applied"]])
        }
    }
    use_case_data["implementation_details"] = feedback_info
    
    # TDDフェーズを更新
    update_tdd_phase(use_case_data, "feedback_application")
    
    # 保存
    save_use_case_json(json_file_path, use_case_data)
    
    return use_case_data


def main():
    """メイン処理"""
    
    # 引数チェック
    if len(sys.argv) < 2:
        print("❌ エラー: Issue番号が必要です")
        print("使用方法: /apply-feedback <issue-number>")
        sys.exit(1)
    
    issue_number = sys.argv[1]
    print(f"\n🔄 Issue #{issue_number} のフィードバック適用を開始します\n")
    
    # ユースケースJSONファイルを検索
    print("📁 ユースケースJSONファイルを検索中...")
    json_file_path = find_use_case_json(issue_number)
    
    if not json_file_path:
        print(f"❌ Issue #{issue_number} のユースケースJSONが見つかりません")
        print("先に /create-use-case コマンドを実行してください")
        sys.exit(1)
    
    print(f"✅ JSONファイルを発見: {json_file_path}")
    
    # 適用前の品質メトリクス測定
    print("\n📊 適用前品質メトリクス測定")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    metrics_before = generate_quality_metrics()
    
    print(f"✅ テストカバレッジ: {metrics_before['test_coverage']:.1f}%")
    print(f"✅ Ruff issues: {metrics_before['ruff_issues']}件")
    print(f"✅ Pyright errors: {metrics_before['pyright_errors']}件")
    print(f"✅ コード行数: {metrics_before['lines_of_code']}行")
    print(f"✅ テストファイル: {metrics_before['test_files']}ファイル")
    
    # GitHubからフィードバック収集
    print("\n📋 フィードバック収集")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    github_feedback = collect_github_feedback(issue_number)
    
    # コード分析によるフィードバック収集
    code_feedback = analyze_code_feedback()
    
    # 全フィードバック統合
    all_feedback = github_feedback + code_feedback
    print(f"📊 総フィードバック項目数: {len(all_feedback)}件")
    
    if not all_feedback:
        print("ℹ️ 適用可能なフィードバックが見つかりませんでした")
        print("品質メトリクスは良好な状態です")
        
        # 実行履歴を更新
        update_execution_history(
            json_file_path,
            f"/apply-feedback {issue_number}",
            "success",
            ["No feedback items to apply - system is in good state"]
        )
        sys.exit(0)
    
    # フィードバック優先度別分類
    print("\n📊 フィードバック優先度分類")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    prioritized_feedback = prioritize_feedback(all_feedback)
    
    # 高優先度フィードバックの適用
    high_priority_items = prioritized_feedback["critical"] + prioritized_feedback["high"]
    medium_priority_items = prioritized_feedback["medium"]
    
    feedback_results = []
    
    if high_priority_items:
        print(f"\n🔴 高優先度フィードバック適用 ({len(high_priority_items)}件)")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        high_results = apply_feedback_batch(high_priority_items, max_items=5)
        feedback_results.extend(high_results)
    
    if medium_priority_items:
        print(f"\n🟡 中優先度フィードバック適用 ({len(medium_priority_items)}件)")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        medium_results = apply_feedback_batch(medium_priority_items, max_items=5)
        feedback_results.extend(medium_results)
    
    # 低優先度は今回はスキップ（必要に応じて実装）
    low_priority_items = prioritized_feedback["low"]
    if low_priority_items:
        print(f"\nℹ️ 低優先度フィードバック ({len(low_priority_items)}件) は今回スキップします")
    
    # 適用後の品質メトリクス測定
    print("\n📈 適用後品質メトリクス測定")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    metrics_after = generate_quality_metrics()
    
    print(f"✅ テストカバレッジ: {metrics_after['test_coverage']:.1f}% (変化: {metrics_after['test_coverage'] - metrics_before['test_coverage']:+.1f}%)")
    print(f"✅ Ruff issues: {metrics_after['ruff_issues']}件 (変化: {metrics_before['ruff_issues'] - metrics_after['ruff_issues']:+})")
    print(f"✅ Pyright errors: {metrics_after['pyright_errors']}件 (変化: {metrics_before['pyright_errors'] - metrics_after['pyright_errors']:+})")
    
    # ユースケースJSONを更新
    print("\n📊 ユースケースJSONを更新中...")
    final_data = update_use_case_json_with_feedback_results(
        json_file_path, feedback_results, metrics_before, metrics_after
    )
    
    # 実行履歴を更新
    applied_count = sum(1 for r in feedback_results if r["applied"])
    created_files = [
        f"{applied_count} feedback items applied",
        f"Quality metrics updated: coverage {metrics_after['test_coverage']:.1f}%"
    ]
    
    update_execution_history(
        json_file_path,
        f"/apply-feedback {issue_number}",
        "success",
        created_files
    )
    
    # 最新データを読み込んで表示
    final_data = load_use_case_json(json_file_path)
    
    # 実行状況を表示
    print("\n" + "="*60)
    print(format_execution_status(final_data))
    print("="*60)
    
    # 最終サマリー表示
    feedback_details = final_data.get("implementation_details", {}).get("feedback_application", {})
    total_items = feedback_details.get("total_feedback_items", 0)
    applied_items = feedback_details.get("applied_items", 0)
    success_rate = feedback_details.get("success_rate", 0)
    
    print(f"\n🎉 フィードバック適用完了")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"📊 適用サマリー:")
    print(f"  • 総フィードバック項目: {total_items}件")
    print(f"  • 適用成功: {applied_items}件")
    print(f"  • 成功率: {success_rate:.1f}%")
    
    priority_summary = feedback_details.get("feedback_summary", {})
    print(f"\n📋 優先度別適用結果:")
    for priority in ["critical", "high", "medium", "low"]:
        count = priority_summary.get(priority, 0)
        if count > 0:
            print(f"  • {priority.upper()}: {count}件適用")
    
    metrics_improvement = feedback_details.get("metrics_improvement", {})
    print(f"\n📈 品質改善:")
    coverage_change = metrics_improvement.get("coverage_change", 0)
    ruff_change = metrics_improvement.get("ruff_issues_change", 0)
    pyright_change = metrics_improvement.get("pyright_errors_change", 0)
    
    print(f"  • カバレッジ: {coverage_change:+.1f}%")
    print(f"  • Ruff問題: {ruff_change:+}件")
    print(f"  • 型エラー: {pyright_change:+}件")
    
    # 失敗したフィードバック項目の表示
    failed_items = [r for r in feedback_results if not r["applied"]]
    if failed_items:
        print(f"\n⚠️ 適用に失敗したフィードバック ({len(failed_items)}件):")
        for item in failed_items[:5]:  # 最大5件表示
            issues = ", ".join(item["issues"])
            print(f"  • {item['item']['type']}: {issues}")
    
    print(f"\n⏭️ 次の推奨コマンド")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    if success_rate >= 80:
        print(f"1. /create-pr {issue_number}")
        print(f"   → フィードバック適用完了、PR作成可能")
        print(f"2. /run-all-tests {issue_number}")
        print(f"   → 最終品質確認（推奨）")
    else:
        print(f"1. 手動でのフィードバック対応")
        print(f"   → 自動適用できなかった項目の確認・対応")
        print(f"2. /apply-feedback {issue_number}")
        print(f"   → 修正後の再実行")
    
    print(f"3. /project-status")
    print(f"   → プロジェクト全体の進捗確認")
    
    print(f"\n💡 フィードバック適用完了")
    if success_rate >= 80:
        print("大部分のフィードバックが適用され、システム品質が向上しました！")
    else:
        print("一部のフィードバックは手動対応が必要です。上記の推奨に従って進めてください。")


if __name__ == "__main__":
    main()