#!/usr/bin/env python3
"""
Review Test Results Expert Command - 改修版
包括的テスト結果分析と品質メトリクス評価を実行
"""

import json
import os
import sys
import subprocess
from datetime import datetime
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


def run_comprehensive_tests():
    """包括的テスト実行とカバレッジ分析"""
    test_results = {
        "total_tests": 0,
        "passed_tests": 0,
        "failed_tests": 0,
        "success_rate": 0.0,
        "coverage_data": {},
        "execution_time": 0.0,
        "test_files": []
    }
    
    tests_dir = Path("tests")
    if not tests_dir.exists():
        print("⚠️ testsディレクトリが存在しません")
        return test_results
    
    try:
        # テストファイルを収集
        test_files = list(tests_dir.glob("**/*.py"))
        test_results["test_files"] = [str(f) for f in test_files]
        
        # カバレッジ付きテスト実行
        cmd = [
            "uv", "run", "--frozen", "pytest", 
            "tests/", 
            "--cov=src",
            "--cov-report=json",
            "--cov-report=html",
            "--cov-report=term",
            "-v",
            "--tb=short"
        ]
        
        start_time = datetime.now()
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=os.getcwd()
        )
        end_time = datetime.now()
        
        test_results["execution_time"] = (end_time - start_time).total_seconds()
        
        # テスト結果を解析
        output = result.stdout + result.stderr
        
        # テスト数をカウント
        test_lines = [line for line in output.split('\n') if '::' in line and ('PASSED' in line or 'FAILED' in line)]
        
        test_results["total_tests"] = len(test_lines)
        test_results["passed_tests"] = len([line for line in test_lines if 'PASSED' in line])
        test_results["failed_tests"] = len([line for line in test_lines if 'FAILED' in line])
        
        if test_results["total_tests"] > 0:
            test_results["success_rate"] = (test_results["passed_tests"] / test_results["total_tests"]) * 100
        
        # カバレッジデータを読み込み
        coverage_file = Path("coverage.json")
        if coverage_file.exists():
            with open(coverage_file, 'r') as f:
                coverage_data = json.load(f)
                test_results["coverage_data"] = {
                    "percent_covered": coverage_data.get("totals", {}).get("percent_covered", 0),
                    "num_statements": coverage_data.get("totals", {}).get("num_statements", 0),
                    "missing_lines": coverage_data.get("totals", {}).get("missing_lines", 0),
                    "covered_lines": coverage_data.get("totals", {}).get("covered_lines", 0)
                }
        
    except Exception as e:
        print(f"❌ テスト実行エラー: {e}")
    
    return test_results


def analyze_quality_metrics():
    """品質メトリクス分析"""
    quality_metrics = {
        "cyclomatic_complexity": {"average": 0, "max": 0, "violations": []},
        "maintainability_index": {"average": 0, "min": 100, "violations": []},
        "code_duplication": {"ratio": 0, "instances": 0},
        "technical_debt": {"hours": 0, "ratio": 0},
        "overall_score": 0
    }
    
    src_dir = Path("src")
    if not src_dir.exists():
        print("⚠️ srcディレクトリが存在しません")
        return quality_metrics
    
    try:
        # Cyclomatic Complexityの計算
        try:
            result = subprocess.run(
                ["radon", "cc", "src/", "--json"],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                cc_data = json.loads(result.stdout)
                complexities = []
                violations = []
                
                for file_path, functions in cc_data.items():
                    for func in functions:
                        complexity = func.get("complexity", 0)
                        complexities.append(complexity)
                        
                        if complexity > 10:  # 高複雑度の閾値
                            violations.append({
                                "file": file_path,
                                "function": func.get("name", "unknown"),
                                "complexity": complexity
                            })
                
                if complexities:
                    quality_metrics["cyclomatic_complexity"]["average"] = sum(complexities) / len(complexities)
                    quality_metrics["cyclomatic_complexity"]["max"] = max(complexities)
                    quality_metrics["cyclomatic_complexity"]["violations"] = violations
        
        except Exception as e:
            print(f"⚠️ Cyclomatic complexity計算エラー: {e}")
        
        # Maintainability Indexの計算
        try:
            result = subprocess.run(
                ["radon", "mi", "src/", "--json"],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                mi_data = json.loads(result.stdout)
                scores = []
                violations = []
                
                for file_path, score in mi_data.items():
                    if isinstance(score, (int, float)):
                        scores.append(score)
                        
                        if score < 60:  # 低保守性の閾値
                            violations.append({
                                "file": file_path,
                                "score": score
                            })
                
                if scores:
                    quality_metrics["maintainability_index"]["average"] = sum(scores) / len(scores)
                    quality_metrics["maintainability_index"]["min"] = min(scores)
                    quality_metrics["maintainability_index"]["violations"] = violations
        
        except Exception as e:
            print(f"⚠️ Maintainability index計算エラー: {e}")
        
        # 総合品質スコア計算
        complexity_score = max(0, 100 - (quality_metrics["cyclomatic_complexity"]["average"] * 10))
        maintainability_score = quality_metrics["maintainability_index"]["average"]
        
        quality_metrics["overall_score"] = (complexity_score + maintainability_score) / 2
        
    except Exception as e:
        print(f"❌ 品質メトリクス分析エラー: {e}")
    
    return quality_metrics


def analyze_performance_metrics(test_results):
    """パフォーマンス分析"""
    performance_metrics = {
        "execution_time": test_results["execution_time"],
        "time_per_test": 0.0,
        "slow_tests": [],
        "performance_score": 0,
        "bottlenecks": []
    }
    
    try:
        if test_results["total_tests"] > 0:
            performance_metrics["time_per_test"] = test_results["execution_time"] / test_results["total_tests"]
        
        # パフォーマンススコアの計算（実行時間に基づく）
        if performance_metrics["time_per_test"] < 0.1:  # 0.1秒未満なら満点
            performance_metrics["performance_score"] = 100
        elif performance_metrics["time_per_test"] < 1.0:  # 1秒未満なら良好
            performance_metrics["performance_score"] = 80
        elif performance_metrics["time_per_test"] < 5.0:  # 5秒未満なら普通
            performance_metrics["performance_score"] = 60
        else:  # 5秒以上は要改善
            performance_metrics["performance_score"] = 40
            performance_metrics["bottlenecks"].append("テスト実行時間が長すぎます")
        
        # 遅いテストの特定（実際のテスト時間があれば）
        if test_results["execution_time"] > 30:  # 30秒以上
            performance_metrics["slow_tests"].append({
                "issue": "全体的な実行時間の長さ",
                "time": test_results["execution_time"],
                "recommendation": "並列実行やテストの最適化を検討"
            })
    
    except Exception as e:
        print(f"❌ パフォーマンス分析エラー: {e}")
    
    return performance_metrics


def calculate_overall_quality_score(test_results, quality_metrics, performance_metrics):
    """総合品質スコアを計算"""
    # 各スコアの重み
    weights = {
        "test_success": 0.35,      # テスト成功率
        "coverage": 0.25,          # カバレッジ
        "quality": 0.25,           # 品質メトリクス
        "performance": 0.15        # パフォーマンス
    }
    
    # 各スコアを計算
    test_success_score = test_results["success_rate"]
    coverage_score = test_results["coverage_data"].get("percent_covered", 0)
    quality_score = quality_metrics["overall_score"]
    performance_score = performance_metrics["performance_score"]
    
    # 重み付き平均を計算
    overall_score = (
        test_success_score * weights["test_success"] +
        coverage_score * weights["coverage"] +
        quality_score * weights["quality"] +
        performance_score * weights["performance"]
    )
    
    return min(100, max(0, overall_score))


def determine_status(overall_score, test_results, quality_metrics):
    """総合ステータスを決定"""
    # 必須条件のチェック
    success_rate = test_results["success_rate"]
    coverage = test_results["coverage_data"].get("percent_covered", 0)
    
    # クリティカルな問題があるかチェック
    critical_issues = 0
    if success_rate < 95:
        critical_issues += 1
    if coverage < 80:
        critical_issues += 1
    if len(quality_metrics["cyclomatic_complexity"]["violations"]) > 5:
        critical_issues += 1
    if len(quality_metrics["maintainability_index"]["violations"]) > 3:
        critical_issues += 1
    
    # ステータス判定
    if overall_score >= 90 and critical_issues == 0:
        return "APPROVED", "READY"
    elif overall_score >= 75 and critical_issues <= 1:
        return "CONDITIONAL_APPROVAL", "CONDITIONAL"
    else:
        return "REJECTED", "NOT_READY"


def generate_comprehensive_report(issue_number, test_results, quality_metrics, performance_metrics, overall_score, issue_data):
    """包括的レビューレポートを生成"""
    reports_dir = Path("docs/reviews")
    reports_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = reports_dir / f"test-results-review-issue-{issue_number}-{timestamp}.md"
    
    issue_title = issue_data.get("title", "Unknown") if issue_data else "Unknown"
    status, readiness = determine_status(overall_score, test_results, quality_metrics)
    
    report_content = f"""# テスト結果レビューレポート

## 基本情報
- **Issue番号**: #{issue_number}
- **Issue タイトル**: {issue_title}
- **レビュー実行日時**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
- **総合判定**: {status}
- **リファクタリング準備度**: {readiness}

## 総合品質評価

### 品質スコア: {overall_score:.1f}/100

## テスト実行結果

### ✅ テスト成功率
- **総テスト数**: {test_results["total_tests"]}個
- **成功テスト数**: {test_results["passed_tests"]}個
- **失敗テスト数**: {test_results["failed_tests"]}個
- **成功率**: {test_results["success_rate"]:.1f}% (目標: 95%以上)
- **実行時間**: {test_results["execution_time"]:.2f}秒

### ✅ カバレッジ分析
- **ラインカバレッジ**: {test_results["coverage_data"].get("percent_covered", 0):.1f}% (目標: 80%以上)
- **総ステートメント数**: {test_results["coverage_data"].get("num_statements", 0)}行
- **カバー済み行数**: {test_results["coverage_data"].get("covered_lines", 0)}行
- **未カバー行数**: {test_results["coverage_data"].get("missing_lines", 0)}行

## 品質メトリクス評価

### ✅ 循環的複雑度
- **平均複雑度**: {quality_metrics["cyclomatic_complexity"]["average"]:.1f} (目標: 5以下)
- **最大複雑度**: {quality_metrics["cyclomatic_complexity"]["max"]}
- **違反関数数**: {len(quality_metrics["cyclomatic_complexity"]["violations"])}個

### ✅ 保守性指数
- **平均保守性指数**: {quality_metrics["maintainability_index"]["average"]:.1f} (目標: 70以上)
- **最低保守性指数**: {quality_metrics["maintainability_index"]["min"]:.1f}
- **低保守性ファイル数**: {len(quality_metrics["maintainability_index"]["violations"])}個

## パフォーマンス分析

### ✅ 実行効率
- **テスト当たり実行時間**: {performance_metrics["time_per_test"]:.3f}秒
- **パフォーマンススコア**: {performance_metrics["performance_score"]}/100
- **検出されたボトルネック**: {len(performance_metrics["bottlenecks"])}個

## 詳細分析結果

### 高複雑度関数
"""
    
    for violation in quality_metrics["cyclomatic_complexity"]["violations"][:5]:
        report_content += f"- {violation['file']}:{violation['function']} (複雑度: {violation['complexity']})\n"
    
    report_content += f"""

### 低保守性ファイル
"""
    
    for violation in quality_metrics["maintainability_index"]["violations"][:5]:
        report_content += f"- {violation['file']} (保守性指数: {violation['score']:.1f})\n"
    
    report_content += f"""

### 検出されたテストファイル
"""
    
    for test_file in test_results["test_files"][:10]:
        report_content += f"- {test_file}\n"
    
    # 推奨事項
    recommendations = []
    
    if test_results["success_rate"] < 95:
        recommendations.append(f"テスト成功率が{test_results['success_rate']:.1f}%です。失敗テストの原因を調査し修正してください。")
    
    if test_results["coverage_data"].get("percent_covered", 0) < 80:
        recommendations.append(f"カバレッジが{test_results['coverage_data'].get('percent_covered', 0):.1f}%です。未カバー部分のテストを追加してください。")
    
    if quality_metrics["cyclomatic_complexity"]["average"] > 5:
        recommendations.append(f"平均循環的複雑度が{quality_metrics['cyclomatic_complexity']['average']:.1f}です。複雑な関数のリファクタリングを検討してください。")
    
    if quality_metrics["maintainability_index"]["average"] < 70:
        recommendations.append(f"保守性指数が{quality_metrics['maintainability_index']['average']:.1f}です。コード品質の改善が必要です。")
    
    if performance_metrics["performance_score"] < 80:
        recommendations.append("テスト実行時間が長すぎます。並列実行や最適化を検討してください。")
    
    if not recommendations:
        recommendations.append("品質メトリクスは良好です。リファクタリングを開始できます。")
    
    report_content += f"""

## 推奨事項

"""
    
    for i, recommendation in enumerate(recommendations, 1):
        report_content += f"{i}. {recommendation}\n"
    
    report_content += f"""

## 次のステップ

"""
    
    if status == "APPROVED" and readiness == "READY":
        report_content += f"""
### 即座に実行可能
- `/refactor {issue_number}` - リファクタリングの開始

### 品質保証
- 全ての品質基準を満たしています
- リファクタリング準備が整っています
"""
    elif status == "CONDITIONAL_APPROVAL":
        report_content += f"""
### 条件付き実行
- 軽微な改善後、`/refactor {issue_number}` を実行可能

### 改善事項
- 品質の一部改善が推奨されます
- リファクタリングと並行して改善可能です
"""
    else:
        report_content += f"""
### 要改善
- `/run-all-tests {issue_number}` でテストの再実行・修正が必要
- 品質向上後に再レビューを実施

### 改善が必要な領域
- テスト成功率の向上
- カバレッジの改善
- コード品質の最適化
"""
    
    report_content = report_content.format(issue_number=issue_number)
    
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    return str(report_file)


def main():
    """メイン処理"""
    
    # 引数チェック
    if len(sys.argv) < 2:
        print("❌ エラー: Issue番号が必要です")
        print("使用方法: /review-test-results <issue-number>")
        sys.exit(1)
    
    issue_number = sys.argv[1]
    print(f"\n🔍 Issue #{issue_number} のテスト結果レビューを開始します\n")
    
    # GitHub Issue情報を取得
    print("📋 GitHub Issue情報を取得中...")
    issue_data = get_github_issue(issue_number)
    
    if issue_data:
        print(f"✅ Issue情報を取得: {issue_data.get('title', 'Unknown')}")
        comment_count = len(issue_data.get('comments', []))
        print(f"📝 コメント数: {comment_count}件")
    else:
        print("⚠️ GitHub Issue情報の取得に失敗しましたが、レビューを続行します")
    
    # ユースケースJSONファイルを検索
    print("\n📁 ユースケースJSONファイルを検索中...")
    json_file_path = find_use_case_json(issue_number)
    
    if not json_file_path:
        print(f"❌ Issue #{issue_number} のユースケースJSONが見つかりません")
        print("先に /create-use-case コマンドを実行してください")
        sys.exit(1)
    
    print(f"✅ JSONファイルを発見: {json_file_path}")
    
    # 包括的テスト実行
    print("\n🧪 包括的テスト実行とカバレッジ分析中...")
    test_results = run_comprehensive_tests()
    
    # 品質メトリクス分析
    print("\n📊 品質メトリクス分析中...")
    quality_metrics = analyze_quality_metrics()
    
    # パフォーマンス分析
    print("\n⚡ パフォーマンス分析中...")
    performance_metrics = analyze_performance_metrics(test_results)
    
    # 総合品質スコア計算
    overall_score = calculate_overall_quality_score(test_results, quality_metrics, performance_metrics)
    
    # ステータス決定
    status, readiness = determine_status(overall_score, test_results, quality_metrics)
    
    # 包括的レポート生成
    print("\n📊 包括的レビューレポートを生成中...")
    report_file = generate_comprehensive_report(issue_number, test_results, quality_metrics, performance_metrics, overall_score, issue_data)
    
    # ユースケースデータを読み込み
    use_case_data = load_use_case_json(json_file_path)
    
    # テスト結果レビュー情報を更新
    test_results_review = {
        "status": status,
        "completed_at": datetime.now().isoformat(),
        "test_success_rate": test_results["success_rate"],
        "coverage_score": test_results["coverage_data"].get("percent_covered", 0),
        "quality_score": overall_score,
        "performance_score": performance_metrics["performance_score"],
        "maintainability_index": quality_metrics["maintainability_index"]["average"],
        "technical_debt_score": 100 - len(quality_metrics["cyclomatic_complexity"]["violations"]) * 5,
        "report_file": report_file,
        "refactoring_readiness": readiness,
        "critical_issues": len(quality_metrics["cyclomatic_complexity"]["violations"]) + len(quality_metrics["maintainability_index"]["violations"]),
        "recommendations": [
            f"テスト成功率: {test_results['success_rate']:.1f}%",
            f"カバレッジ: {test_results['coverage_data'].get('percent_covered', 0):.1f}%",
            f"品質スコア: {overall_score:.1f}/100"
        ]
    }
    
    use_case_data.setdefault("quality_gates", {})["test_results_review"] = test_results_review
    save_use_case_json(json_file_path, use_case_data)
    
    # 実行履歴を更新
    update_execution_history(
        json_file_path,
        f"/review-test-results {issue_number}",
        "success" if status != "ERROR" else "failed",
        [report_file, "coverage.json", "htmlcov/index.html"]
    )
    
    # 更新されたデータを読み込み
    updated_data = load_use_case_json(json_file_path)
    
    # 実行状況を表示
    print("\n" + "="*60)
    print(format_execution_status(updated_data))
    print("="*60)
    
    # 結果サマリー表示
    print(f"\n📊 テスト結果レビュー結果")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"🎯 総合判定: {status}")
    print(f"🏗️ リファクタリング準備度: {readiness}")
    print(f"📈 総合品質スコア: {overall_score:.1f}/100")
    print(f"🧪 テスト成功率: {test_results['success_rate']:.1f}%")
    print(f"📊 カバレッジ: {test_results['coverage_data'].get('percent_covered', 0):.1f}%")
    print(f"⚡ パフォーマンススコア: {performance_metrics['performance_score']}/100")
    
    print(f"\n📁 成果物")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"✅ {report_file}")
    if Path("htmlcov/index.html").exists():
        print(f"✅ htmlcov/index.html (カバレッジレポート)")
    if Path("coverage.json").exists():
        print(f"✅ coverage.json (詳細カバレッジデータ)")
    
    print(f"\n📈 品質メトリクス詳細")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"🔄 平均循環的複雑度: {quality_metrics['cyclomatic_complexity']['average']:.1f}")
    print(f"🏗️ 平均保守性指数: {quality_metrics['maintainability_index']['average']:.1f}")
    print(f"⚠️ 高複雑度関数: {len(quality_metrics['cyclomatic_complexity']['violations'])}個")
    print(f"🔧 低保守性ファイル: {len(quality_metrics['maintainability_index']['violations'])}個")
    
    print(f"\n⏭️ 次の推奨コマンド")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    if status == "APPROVED" and readiness == "READY":
        print(f"✅ 品質基準達成 - 即座に実行可能:")
        print(f"   /refactor {issue_number}")
        print(f"   → リファクタリング段階の開始")
        print(f"\n🧹 推奨リファクタリング項目:")
        if quality_metrics["cyclomatic_complexity"]["violations"]:
            print(f"   - 高複雑度関数の簡素化")
        if quality_metrics["maintainability_index"]["violations"]:
            print(f"   - 低保守性ファイルの改善")
        print(f"   - パフォーマンス最適化")
    elif status == "CONDITIONAL_APPROVAL":
        print(f"⚠️ 条件付き承認:")
        print(f"   /refactor {issue_number}")
        print(f"   → リファクタリング開始（品質改善と並行）")
        print(f"   または")
        print(f"   /run-all-tests {issue_number}")
        print(f"   → テスト改善後にリファクタリング")
    else:
        print(f"❌ 品質基準未達成:")
        print(f"   /run-all-tests {issue_number}")
        print(f"   → テストの再実行・修正")
        print(f"   その後")
        print(f"   /review-test-results {issue_number}")
        print(f"   → 再レビュー実施")
    
    # 最終メッセージ
    status_emoji = {"APPROVED": "✅", "CONDITIONAL_APPROVAL": "⚠️", "REJECTED": "❌"}
    emoji = status_emoji.get(status, "❓")
    
    print(f"\n{emoji} テスト結果レビュー完了")
    print(f"詳細な分析結果は {report_file} に記録されました。")


if __name__ == "__main__":
    main()