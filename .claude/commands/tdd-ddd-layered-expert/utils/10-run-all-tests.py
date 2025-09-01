#!/usr/bin/env python3
"""
Run All Tests Command - 改修版
全テストスイートを実行し、品質メトリクスを分析、実行履歴を更新
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


def ensure_test_results_directory():
    """テスト結果保存ディレクトリを作成"""
    test_results_dir = Path("docs/test_results")
    test_results_dir.mkdir(parents=True, exist_ok=True)
    return test_results_dir


def check_test_dependencies():
    """テスト実行に必要な依存関係をチェック"""
    print("🔍 テスト環境を確認中...")
    
    dependencies = []
    
    # pytest の存在確認
    try:
        result = subprocess.run(["uv", "run", "--frozen", "pytest", "--version"], 
                              capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            dependencies.append(("pytest", "✅", result.stdout.strip()))
        else:
            dependencies.append(("pytest", "❌", "Not available"))
    except (subprocess.TimeoutExpired, FileNotFoundError):
        dependencies.append(("pytest", "❌", "Not available"))
    
    # coverage の存在確認
    try:
        result = subprocess.run(["uv", "run", "--frozen", "python", "-m", "coverage", "--version"], 
                              capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            dependencies.append(("coverage", "✅", result.stdout.strip()))
        else:
            dependencies.append(("coverage", "❌", "Not available"))
    except (subprocess.TimeoutExpired, FileNotFoundError):
        dependencies.append(("coverage", "❌", "Not available"))
    
    # テストディレクトリの存在確認
    test_dirs = ["tests", "tests/unit", "tests/integration"]
    for test_dir in test_dirs:
        if Path(test_dir).exists():
            dependencies.append((test_dir, "✅", "Directory exists"))
        else:
            dependencies.append((test_dir, "⚠️", "Directory not found"))
    
    return dependencies


def run_test_suite(test_type: str, test_path: str, extra_args: List[str] = None) -> Dict[str, Any]:
    """テストスイートを実行"""
    
    if extra_args is None:
        extra_args = []
    
    print(f"🧪 {test_type}テストを実行中...")
    
    # テストパスの存在確認
    if not Path(test_path).exists():
        print(f"⚠️ {test_path} が見つかりません。スキップします。")
        return {
            "test_type": test_type,
            "path": test_path,
            "status": "skipped",
            "reason": "Directory not found",
            "tests_run": 0,
            "tests_passed": 0,
            "tests_failed": 0,
            "execution_time": 0
        }
    
    # pytestコマンド構築
    cmd = ["uv", "run", "--frozen", "pytest", test_path, "-v"] + extra_args
    
    start_time = time.time()
    try:
        # テスト実行
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=600  # 10分タイムアウト
        )
        
        execution_time = time.time() - start_time
        
        # 結果をパース
        output = result.stdout + result.stderr
        
        # テスト数を抽出
        tests_run = 0
        tests_passed = 0
        tests_failed = 0
        
        # pytest出力からテスト結果を抽出
        if "short test summary" in output.lower():
            # 失敗があった場合
            failed_match = re.search(r'(\d+) failed', output)
            passed_match = re.search(r'(\d+) passed', output)
            
            if failed_match:
                tests_failed = int(failed_match.group(1))
            if passed_match:
                tests_passed = int(passed_match.group(1))
        else:
            # 全て成功した場合
            passed_match = re.search(r'(\d+) passed', output)
            if passed_match:
                tests_passed = int(passed_match.group(1))
        
        tests_run = tests_passed + tests_failed
        
        # ステータス決定
        if result.returncode == 0:
            status = "success"
        else:
            status = "failed"
        
        return {
            "test_type": test_type,
            "path": test_path,
            "status": status,
            "tests_run": tests_run,
            "tests_passed": tests_passed,
            "tests_failed": tests_failed,
            "execution_time": execution_time,
            "output": output,
            "return_code": result.returncode
        }
        
    except subprocess.TimeoutExpired:
        execution_time = time.time() - start_time
        return {
            "test_type": test_type,
            "path": test_path,
            "status": "timeout",
            "tests_run": 0,
            "tests_passed": 0,
            "tests_failed": 0,
            "execution_time": execution_time,
            "output": "Test execution timed out",
            "return_code": -1
        }
    
    except Exception as e:
        execution_time = time.time() - start_time
        return {
            "test_type": test_type,
            "path": test_path,
            "status": "error",
            "tests_run": 0,
            "tests_passed": 0,
            "tests_failed": 0,
            "execution_time": execution_time,
            "output": f"Error running tests: {e}",
            "return_code": -1
        }


def run_coverage_analysis() -> Dict[str, Any]:
    """カバレッジ分析を実行"""
    print("📊 コードカバレッジ分析を実行中...")
    
    # src ディレクトリの存在確認
    if not Path("src").exists():
        print("⚠️ src ディレクトリが見つかりません。カバレッジ分析をスキップします。")
        return {
            "status": "skipped",
            "reason": "src directory not found",
            "overall_coverage": 0,
            "line_coverage": 0,
            "branch_coverage": 0
        }
    
    try:
        # カバレッジ付きでユニットテストを実行
        cmd = [
            "uv", "run", "--frozen", "pytest", 
            "tests/",
            "--cov=src",
            "--cov-report=term-missing",
            "--cov-report=json:coverage.json",
            "--cov-report=html:htmlcov",
            "-v"
        ]
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=600
        )
        
        # coverage.jsonファイルを読み取り
        coverage_data = {}
        if Path("coverage.json").exists():
            try:
                with open("coverage.json", "r", encoding="utf-8") as f:
                    coverage_json = json.load(f)
                
                overall_coverage = coverage_json.get("totals", {}).get("percent_covered", 0)
                coverage_data = {
                    "status": "success",
                    "overall_coverage": overall_coverage,
                    "line_coverage": coverage_json.get("totals", {}).get("percent_covered_display", "0%"),
                    "num_statements": coverage_json.get("totals", {}).get("num_statements", 0),
                    "missing_lines": coverage_json.get("totals", {}).get("missing_lines", 0),
                    "excluded_lines": coverage_json.get("totals", {}).get("excluded_lines", 0),
                    "files": coverage_json.get("files", {})
                }
                
                # HTMLカバレッジレポートの場所を記録
                if Path("htmlcov/index.html").exists():
                    coverage_data["html_report"] = "htmlcov/index.html"
                
            except json.JSONDecodeError:
                coverage_data = {
                    "status": "error",
                    "reason": "Could not parse coverage.json",
                    "overall_coverage": 0
                }
        else:
            coverage_data = {
                "status": "error", 
                "reason": "coverage.json not generated",
                "overall_coverage": 0
            }
        
        # テスト結果も含める
        output = result.stdout + result.stderr
        coverage_data["test_output"] = output
        coverage_data["return_code"] = result.returncode
        
        return coverage_data
        
    except subprocess.TimeoutExpired:
        return {
            "status": "timeout",
            "reason": "Coverage analysis timed out",
            "overall_coverage": 0
        }
    except Exception as e:
        return {
            "status": "error",
            "reason": f"Error running coverage analysis: {e}",
            "overall_coverage": 0
        }


def analyze_test_structure() -> Dict[str, Any]:
    """テスト構造を分析"""
    print("🔍 テスト構造を分析中...")
    
    analysis = {
        "test_directories": {},
        "test_files_count": 0,
        "total_test_functions": 0,
        "architecture_compliance": True,
        "issues": []
    }
    
    # テストディレクトリ構造を分析
    test_base = Path("tests")
    if test_base.exists():
        for test_dir in ["unit", "integration", "e2e", "performance"]:
            test_path = test_base / test_dir
            if test_path.exists():
                py_files = list(test_path.glob("**/*.py"))
                test_files = [f for f in py_files if f.name.startswith("test_") or f.name.endswith("_test.py")]
                
                analysis["test_directories"][test_dir] = {
                    "exists": True,
                    "test_files": len(test_files),
                    "all_files": len(py_files)
                }
                analysis["test_files_count"] += len(test_files)
                
                # テスト関数数をカウント（簡易版）
                for test_file in test_files:
                    try:
                        content = test_file.read_text(encoding="utf-8")
                        test_functions = re.findall(r'def test_\w+\(', content)
                        analysis["total_test_functions"] += len(test_functions)
                    except Exception:
                        continue
            else:
                analysis["test_directories"][test_dir] = {
                    "exists": False,
                    "test_files": 0,
                    "all_files": 0
                }
    else:
        analysis["issues"].append("tests/ directory not found")
        analysis["architecture_compliance"] = False
    
    # src構造との対応をチェック
    src_base = Path("src")
    if src_base.exists():
        src_modules = []
        for py_file in src_base.glob("**/*.py"):
            if py_file.name != "__init__.py":
                relative_path = py_file.relative_to(src_base)
                module_path = str(relative_path).replace("/", ".").replace("\\", ".").replace(".py", "")
                src_modules.append(module_path)
        
        analysis["source_modules"] = len(src_modules)
        
        # テストカバレッジの簡易チェック（構造的）
        if analysis["test_files_count"] == 0 and len(src_modules) > 0:
            analysis["issues"].append("Source code exists but no test files found")
            analysis["architecture_compliance"] = False
    
    return analysis


def generate_quality_report(test_results: List[Dict[str, Any]], coverage_data: Dict[str, Any], 
                          test_structure: Dict[str, Any], issue_number: str) -> Dict[str, Any]:
    """品質レポートを生成"""
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # 全体的な統計
    total_tests = sum(r.get("tests_run", 0) for r in test_results)
    total_passed = sum(r.get("tests_passed", 0) for r in test_results)
    total_failed = sum(r.get("tests_failed", 0) for r in test_results)
    total_execution_time = sum(r.get("execution_time", 0) for r in test_results)
    
    # 品質スコアの計算
    quality_score = calculate_quality_score(test_results, coverage_data, test_structure)
    
    # ステータス決定
    overall_status = "success"
    if total_failed > 0:
        overall_status = "failed"
    elif any(r.get("status") in ["error", "timeout"] for r in test_results):
        overall_status = "error"
    elif coverage_data.get("overall_coverage", 0) < 80:
        overall_status = "partial"
    
    report = {
        "issue_number": issue_number,
        "timestamp": timestamp,
        "execution_summary": {
            "overall_status": overall_status,
            "total_tests": total_tests,
            "total_passed": total_passed,
            "total_failed": total_failed,
            "execution_time": round(total_execution_time, 2),
            "quality_score": quality_score
        },
        "test_suite_results": test_results,
        "coverage_analysis": coverage_data,
        "test_structure_analysis": test_structure,
        "quality_assessment": {
            "meets_coverage_threshold": coverage_data.get("overall_coverage", 0) >= 80,
            "all_tests_passing": total_failed == 0,
            "architecture_compliant": test_structure.get("architecture_compliance", False),
            "ready_for_refactoring": overall_status == "success" and total_failed == 0
        },
        "recommendations": generate_recommendations(test_results, coverage_data, test_structure)
    }
    
    return report


def calculate_quality_score(test_results: List[Dict[str, Any]], coverage_data: Dict[str, Any], 
                          test_structure: Dict[str, Any]) -> int:
    """品質スコアを計算 (0-100)"""
    
    score = 100
    
    # テスト失敗によるペナルティ
    total_failed = sum(r.get("tests_failed", 0) for r in test_results)
    if total_failed > 0:
        score -= min(50, total_failed * 10)  # 失敗1つにつき10点減点、最大50点まで
    
    # カバレッジによるスコア調整
    coverage = coverage_data.get("overall_coverage", 0)
    if coverage < 80:
        score -= (80 - coverage) * 0.5  # カバレッジ80%未満は0.5点/1%の減点
    
    # テスト構造による調整
    if not test_structure.get("architecture_compliance", True):
        score -= 20
    
    # エラーやタイムアウトによるペナルティ
    for result in test_results:
        if result.get("status") in ["error", "timeout"]:
            score -= 15
    
    return max(0, int(score))


def generate_recommendations(test_results: List[Dict[str, Any]], coverage_data: Dict[str, Any], 
                           test_structure: Dict[str, Any]) -> List[str]:
    """改善提案を生成"""
    
    recommendations = []
    
    # テスト失敗に対する提案
    total_failed = sum(r.get("tests_failed", 0) for r in test_results)
    if total_failed > 0:
        recommendations.append(f"🔴 {total_failed}個のテストが失敗しています。実装を見直してください。")
    
    # カバレッジに対する提案
    coverage = coverage_data.get("overall_coverage", 0)
    if coverage < 80:
        recommendations.append(f"📊 コードカバレッジが{coverage:.1f}%です。80%以上を目指してテストを追加してください。")
    elif coverage < 90:
        recommendations.append(f"📊 コードカバレッジは{coverage:.1f}%です。さらなる品質向上のため90%以上を目指すことをお勧めします。")
    
    # テスト構造に対する提案
    if not test_structure.get("architecture_compliance", True):
        recommendations.append("🏗️ テスト構造がClean Architectureの原則に従っていません。tests/unit, tests/integration ディレクトリの整理を検討してください。")
    
    # テストファイル数に対する提案
    if test_structure.get("test_files_count", 0) == 0:
        recommendations.append("⚠️ テストファイルが見つかりません。/create-tests コマンドでテストを作成してください。")
    elif test_structure.get("total_test_functions", 0) < 10:
        recommendations.append("📝 テスト関数が少ないです。より包括的なテストの作成を検討してください。")
    
    # エラーやタイムアウトに対する提案
    for result in test_results:
        if result.get("status") == "timeout":
            recommendations.append(f"⏱️ {result['test_type']}テストがタイムアウトしました。テストの最適化を検討してください。")
        elif result.get("status") == "error":
            recommendations.append(f"❌ {result['test_type']}テストでエラーが発生しました。環境設定を確認してください。")
    
    # 成功時の提案
    if not recommendations:
        recommendations.append("✅ 全てのテストが成功し、品質基準を満たしています。次は /refactor コマンドでリファクタリングを実行できます。")
    
    return recommendations


def save_quality_report(report: Dict[str, Any], test_results_dir: Path) -> List[str]:
    """品質レポートをファイルに保存"""
    
    created_files = []
    timestamp = report["timestamp"]
    issue_number = report["issue_number"]
    
    # JSONレポート保存
    json_report_path = test_results_dir / f"test-metrics-{issue_number}-{timestamp}.json"
    with open(json_report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False, default=str)
    created_files.append(str(json_report_path))
    
    # Markdownレポート生成
    md_report_path = test_results_dir / f"quality-analysis-{issue_number}-{timestamp}.md"
    md_content = generate_markdown_report(report)
    with open(md_report_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    created_files.append(str(md_report_path))
    
    # HTMLカバレッジレポートがある場合は移動
    if Path("htmlcov").exists():
        coverage_report_dir = test_results_dir / f"coverage-{issue_number}-{timestamp}"
        coverage_report_dir.mkdir(parents=True, exist_ok=True)
        
        # htmlcov内容をコピー
        import shutil
        shutil.copytree("htmlcov", coverage_report_dir, dirs_exist_ok=True)
        created_files.append(str(coverage_report_dir / "index.html"))
    
    return created_files


def generate_markdown_report(report: Dict[str, Any]) -> str:
    """Markdown形式のレポートを生成"""
    
    summary = report["execution_summary"]
    coverage = report["coverage_analysis"]
    structure = report["test_structure_analysis"]
    recommendations = report["recommendations"]
    
    md = f"""# テスト実行品質レポート

**Issue**: #{report['issue_number']}  
**実行日時**: {report['timestamp']}  
**総合ステータス**: {summary['overall_status'].upper()}  
**品質スコア**: {summary['quality_score']}/100

## 📊 実行サマリー

- **実行テスト数**: {summary['total_tests']}
- **成功**: {summary['total_passed']}
- **失敗**: {summary['total_failed']}
- **実行時間**: {summary['execution_time']}秒

## 🧪 テストスイート結果

"""
    
    for result in report["test_suite_results"]:
        status_emoji = "✅" if result["status"] == "success" else "❌" if result["status"] == "failed" else "⚠️"
        md += f"### {status_emoji} {result['test_type'].title()}テスト\n\n"
        md += f"- **パス**: {result['path']}\n"
        md += f"- **ステータス**: {result['status']}\n"
        md += f"- **実行数**: {result['tests_run']}\n"
        md += f"- **成功**: {result['tests_passed']}\n"
        md += f"- **失敗**: {result['tests_failed']}\n"
        md += f"- **実行時間**: {result['execution_time']:.2f}秒\n\n"
    
    md += f"""## 📈 カバレッジ分析

- **全体カバレッジ**: {coverage.get('overall_coverage', 0):.1f}%
- **ステータス**: {coverage.get('status', 'unknown')}
"""
    
    if coverage.get('num_statements'):
        md += f"- **総ステートメント数**: {coverage['num_statements']}\n"
        md += f"- **未カバー行数**: {coverage.get('missing_lines', 0)}\n"
    
    if coverage.get('html_report'):
        md += f"- **詳細レポート**: {coverage['html_report']}\n"
    
    md += f"""

## 🏗️ テスト構造分析

- **テストファイル数**: {structure['test_files_count']}
- **テスト関数数**: {structure['total_test_functions']}
- **アーキテクチャ準拠**: {'✅' if structure['architecture_compliance'] else '❌'}

### テストディレクトリ構造

"""
    
    for dir_name, dir_info in structure['test_directories'].items():
        exists_emoji = "✅" if dir_info['exists'] else "❌"
        md += f"- **{dir_name}**: {exists_emoji} {dir_info['test_files']}ファイル\n"
    
    md += f"""

## 💡 改善提案

"""
    
    for i, recommendation in enumerate(recommendations, 1):
        md += f"{i}. {recommendation}\n"
    
    md += f"""

## ✅ 品質評価

- **カバレッジ基準達成**: {'✅' if report['quality_assessment']['meets_coverage_threshold'] else '❌'}
- **全テスト成功**: {'✅' if report['quality_assessment']['all_tests_passing'] else '❌'}
- **アーキテクチャ準拠**: {'✅' if report['quality_assessment']['architecture_compliant'] else '❌'}
- **リファクタリング準備完了**: {'✅' if report['quality_assessment']['ready_for_refactoring'] else '❌'}

---

*このレポートは `/run-all-tests` コマンドによって自動生成されました。*
"""
    
    return md


def update_use_case_json_with_test_results(json_file_path: str, quality_report: Dict[str, Any]):
    """ユースケースJSONにテスト結果を更新"""
    
    use_case_data = load_use_case_json(json_file_path)
    
    # テスト実行情報を更新
    test_info = use_case_data.get("implementation_details", {})
    test_info["test_execution"] = {
        "completed": True,
        "timestamp": quality_report["timestamp"],
        "overall_status": quality_report["execution_summary"]["overall_status"],
        "total_tests": quality_report["execution_summary"]["total_tests"],
        "tests_passed": quality_report["execution_summary"]["total_passed"],
        "tests_failed": quality_report["execution_summary"]["total_failed"],
        "coverage_percentage": quality_report["coverage_analysis"].get("overall_coverage", 0),
        "quality_score": quality_report["execution_summary"]["quality_score"],
        "ready_for_refactoring": quality_report["quality_assessment"]["ready_for_refactoring"]
    }
    use_case_data["implementation_details"] = test_info
    
    # TDDフェーズを更新
    update_tdd_phase(use_case_data, "test_execution")
    
    # 保存
    save_use_case_json(json_file_path, use_case_data)
    
    return use_case_data


def main():
    """メイン処理"""
    
    # 引数チェック
    if len(sys.argv) < 2:
        print("❌ エラー: Issue番号が必要です")
        print("使用方法: /run-all-tests <issue-number>")
        sys.exit(1)
    
    issue_number = sys.argv[1]
    print(f"\n🧪 Issue #{issue_number} の全テスト実行を開始します\n")
    
    # ユースケースJSONファイルを検索
    print("📁 ユースケースJSONファイルを検索中...")
    json_file_path = find_use_case_json(issue_number)
    
    if not json_file_path:
        print(f"❌ Issue #{issue_number} のユースケースJSONが見つかりません")
        print("先に /create-use-case コマンドを実行してください")
        sys.exit(1)
    
    print(f"✅ JSONファイルを発見: {json_file_path}")
    
    # テスト結果保存ディレクトリ準備
    test_results_dir = ensure_test_results_directory()
    print(f"📁 テスト結果保存先: {test_results_dir}")
    
    # テスト環境チェック
    print("\n🔍 テスト環境確認")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    dependencies = check_test_dependencies()
    for name, status, info in dependencies:
        print(f"{status} {name}: {info}")
    
    # 必須依存関係チェック
    pytest_available = any(d[0] == "pytest" and d[1] == "✅" for d in dependencies)
    if not pytest_available:
        print("\n❌ pytest が利用できません。テスト実行を中止します。")
        print("uv add pytest pytest-cov を実行してください。")
        sys.exit(1)
    
    # 各テストスイートを実行
    print("\n🧪 テストスイート実行")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    test_results = []
    
    # 1. ユニットテスト
    if Path("tests/unit").exists():
        unit_result = run_test_suite("Unit", "tests/unit/")
        test_results.append(unit_result)
        print(f"✅ ユニットテスト完了: {unit_result['tests_passed']}成功, {unit_result['tests_failed']}失敗")
    else:
        print("⚠️ tests/unit/ ディレクトリが見つかりません")
    
    # 2. 統合テスト
    if Path("tests/integration").exists():
        integration_result = run_test_suite("Integration", "tests/integration/")
        test_results.append(integration_result)
        print(f"✅ 統合テスト完了: {integration_result['tests_passed']}成功, {integration_result['tests_failed']}失敗")
    else:
        print("⚠️ tests/integration/ ディレクトリが見つかりません")
    
    # 3. E2Eテスト（オプション）
    if Path("tests/e2e").exists():
        e2e_result = run_test_suite("E2E", "tests/e2e/")
        test_results.append(e2e_result)
        print(f"✅ E2Eテスト完了: {e2e_result['tests_passed']}成功, {e2e_result['tests_failed']}失敗")
    else:
        print("ℹ️ E2Eテストディレクトリがありません（オプション）")
    
    # 4. パフォーマンステスト（オプション）
    if Path("tests/performance").exists():
        perf_result = run_test_suite("Performance", "tests/performance/")
        test_results.append(perf_result)
        print(f"✅ パフォーマンステスト完了: {perf_result['tests_passed']}成功, {perf_result['tests_failed']}失敗")
    else:
        print("ℹ️ パフォーマンステストディレクトリがありません（オプション）")
    
    # テストが1つも実行されなかった場合
    if not test_results:
        print("❌ 実行可能なテストが見つかりませんでした")
        print("tests/ ディレクトリにテストファイルを作成してください")
        sys.exit(1)
    
    # カバレッジ分析実行
    print("\n📊 カバレッジ分析実行")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    coverage_data = run_coverage_analysis()
    if coverage_data["status"] == "success":
        print(f"✅ カバレッジ分析完了: {coverage_data['overall_coverage']:.1f}%")
    else:
        print(f"⚠️ カバレッジ分析: {coverage_data['status']} - {coverage_data.get('reason', '')}")
    
    # テスト構造分析
    print("\n🔍 テスト構造分析")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    test_structure = analyze_test_structure()
    print(f"✅ 分析完了: {test_structure['test_files_count']}ファイル, {test_structure['total_test_functions']}関数")
    
    # 品質レポート生成
    print("\n📋 品質レポート生成")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    quality_report = generate_quality_report(test_results, coverage_data, test_structure, issue_number)
    
    # レポート保存
    created_files = save_quality_report(quality_report, test_results_dir)
    print(f"✅ 品質レポート保存完了: {len(created_files)}ファイル")
    
    # ユースケースJSONを更新
    print("📊 ユースケースJSONを更新中...")
    update_use_case_json_with_test_results(json_file_path, quality_report)
    
    # 実行履歴を更新
    update_execution_history(
        json_file_path,
        f"/run-all-tests {issue_number}",
        quality_report["execution_summary"]["overall_status"],
        created_files
    )
    
    # 最新データを読み込んで表示
    final_data = load_use_case_json(json_file_path)
    
    # 実行状況を表示
    print("\n" + "="*60)
    print(format_execution_status(final_data))
    print("="*60)
    
    # 最終サマリー表示
    summary = quality_report["execution_summary"]
    print(f"\n🧪 テスト実行サマリー")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"📊 総合ステータス: {summary['overall_status'].upper()}")
    print(f"✅ 実行テスト数: {summary['total_tests']}")
    print(f"✅ 成功: {summary['total_passed']}")
    print(f"❌ 失敗: {summary['total_failed']}")
    print(f"📈 カバレッジ: {coverage_data.get('overall_coverage', 0):.1f}%")
    print(f"🏆 品質スコア: {summary['quality_score']}/100")
    print(f"⏱️ 実行時間: {summary['execution_time']:.2f}秒")
    
    print(f"\n📁 生成ファイル")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    for file_path in created_files:
        print(f"✅ {file_path}")
    
    print(f"\n💡 改善提案")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    for recommendation in quality_report["recommendations"]:
        print(f"{recommendation}")
    
    print(f"\n⏭️ 次の推奨コマンド")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    if quality_report["quality_assessment"]["ready_for_refactoring"]:
        print(f"1. /refactor {issue_number}")
        print(f"   → 全テスト成功、リファクタリング実行可能")
    else:
        if summary["total_failed"] > 0:
            print(f"1. テスト失敗の修正")
            print(f"   → 失敗したテストの原因を調査・修正")
        if coverage_data.get('overall_coverage', 0) < 80:
            print(f"2. テストカバレッジ改善")
            print(f"   → カバレッジ80%以上を目指してテスト追加")
        print(f"3. /run-all-tests {issue_number}")
        print(f"   → 修正後の再テスト実行")
    
    print(f"\n💡 テスト実行完了")
    if summary["overall_status"] == "success":
        print("全てのテストが成功し、品質基準を満たしています！")
    else:
        print("一部のテストで問題が発見されました。上記の提案に従って修正してください。")


if __name__ == "__main__":
    main()