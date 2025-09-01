#!/usr/bin/env python3
"""
Review Issue Command - 改修版
実装の品質レビューを実行し、実行履歴を更新
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


def ensure_reviews_directory():
    """レビュー結果保存ディレクトリを作成"""
    reviews_dir = Path("docs/reviews")
    reviews_dir.mkdir(parents=True, exist_ok=True)
    return reviews_dir


def analyze_architecture_compliance() -> Dict[str, Any]:
    """アーキテクチャ準拠性を分析"""
    print("🏗️ アーキテクチャ準拠性を分析中...")
    
    compliance_result = {
        "status": "success",
        "overall_compliance": 100,
        "layer_violations": [],
        "dependency_violations": [],
        "pattern_adherence": {},
        "issues": []
    }
    
    # src ディレクトリの存在確認
    if not Path("src").exists():
        compliance_result["status"] = "error"
        compliance_result["issues"].append("src directory not found")
        compliance_result["overall_compliance"] = 0
        return compliance_result
    
    # レイヤー構造の検証
    expected_layers = ["domain", "application", "infrastructure", "presentation"]
    existing_layers = {}
    
    for layer in expected_layers:
        layer_path = Path(f"src/{layer}")
        if layer_path.exists():
            py_files = list(layer_path.glob("**/*.py"))
            existing_layers[layer] = {
                "exists": True,
                "files_count": len([f for f in py_files if f.name != "__init__.py"]),
                "path": str(layer_path)
            }
        else:
            existing_layers[layer] = {"exists": False, "files_count": 0}
    
    compliance_result["layer_structure"] = existing_layers
    
    # 依存関係方向の検証
    dependency_violations = []
    
    # ドメイン層の依存関係チェック（外部層への依存は禁止）
    domain_path = Path("src/domain")
    if domain_path.exists():
        for py_file in domain_path.glob("**/*.py"):
            if py_file.name == "__init__.py":
                continue
                
            try:
                content = py_file.read_text(encoding="utf-8")
                
                # 禁止された依存関係のパターン
                forbidden_imports = [
                    r'from\s+.*application.*import',
                    r'from\s+.*infrastructure.*import', 
                    r'from\s+.*presentation.*import',
                    r'import\s+.*application',
                    r'import\s+.*infrastructure',
                    r'import\s+.*presentation'
                ]
                
                for pattern in forbidden_imports:
                    matches = re.findall(pattern, content, re.IGNORECASE)
                    if matches:
                        dependency_violations.append({
                            "file": str(py_file),
                            "violation": "domain_layer_external_dependency",
                            "details": f"Domain layer imports external layer: {matches[0]}",
                            "severity": "critical"
                        })
            except Exception:
                continue
    
    # アプリケーション層の依存関係チェック（インフラ・プレゼンテーション層への依存は禁止）
    app_path = Path("src/application")
    if app_path.exists():
        for py_file in app_path.glob("**/*.py"):
            if py_file.name == "__init__.py":
                continue
                
            try:
                content = py_file.read_text(encoding="utf-8")
                
                forbidden_imports = [
                    r'from\s+.*infrastructure.*import',
                    r'from\s+.*presentation.*import',
                    r'import\s+.*infrastructure',
                    r'import\s+.*presentation'
                ]
                
                for pattern in forbidden_imports:
                    matches = re.findall(pattern, content, re.IGNORECASE)
                    if matches:
                        dependency_violations.append({
                            "file": str(py_file),
                            "violation": "application_layer_external_dependency",
                            "details": f"Application layer imports external layer: {matches[0]}",
                            "severity": "critical"
                        })
            except Exception:
                continue
    
    compliance_result["dependency_violations"] = dependency_violations
    
    # DDD パターン適用の検証
    ddd_patterns = analyze_ddd_patterns()
    compliance_result["pattern_adherence"] = ddd_patterns
    
    # 全体的なコンプライアンススコアの計算
    penalty = 0
    
    # レイヤー構造の欠損によるペナルティ
    missing_layers = [layer for layer, info in existing_layers.items() if not info["exists"]]
    penalty += len(missing_layers) * 20
    
    # 依存関係違反によるペナルティ
    critical_violations = [v for v in dependency_violations if v["severity"] == "critical"]
    penalty += len(critical_violations) * 15
    
    compliance_result["overall_compliance"] = max(0, 100 - penalty)
    
    if penalty > 0:
        compliance_result["status"] = "violations_found"
    
    return compliance_result


def analyze_ddd_patterns() -> Dict[str, Any]:
    """DDD パターンの適用を分析"""
    
    patterns = {
        "entities": {"found": 0, "files": []},
        "value_objects": {"found": 0, "files": []},
        "aggregates": {"found": 0, "files": []},
        "repositories": {"found": 0, "files": []},
        "domain_services": {"found": 0, "files": []},
        "use_cases": {"found": 0, "files": []}
    }
    
    # エンティティの検出
    domain_entities = Path("src/domain/entities")
    if domain_entities.exists():
        entity_files = list(domain_entities.glob("*.py"))
        patterns["entities"]["found"] = len([f for f in entity_files if f.name != "__init__.py"])
        patterns["entities"]["files"] = [str(f) for f in entity_files if f.name != "__init__.py"]
    
    # 値オブジェクトの検出
    domain_vos = Path("src/domain/value_objects") 
    if domain_vos.exists():
        vo_files = list(domain_vos.glob("*.py"))
        patterns["value_objects"]["found"] = len([f for f in vo_files if f.name != "__init__.py"])
        patterns["value_objects"]["files"] = [str(f) for f in vo_files if f.name != "__init__.py"]
    
    # リポジトリインターフェースの検出
    domain_repos = Path("src/domain/repositories")
    if domain_repos.exists():
        repo_files = list(domain_repos.glob("*.py"))
        patterns["repositories"]["found"] = len([f for f in repo_files if f.name != "__init__.py"])
        patterns["repositories"]["files"] = [str(f) for f in repo_files if f.name != "__init__.py"]
    
    # ユースケースの検出
    app_use_cases = Path("src/application/use_cases")
    if app_use_cases.exists():
        uc_files = list(app_use_cases.glob("*.py"))
        patterns["use_cases"]["found"] = len([f for f in uc_files if f.name != "__init__.py"])
        patterns["use_cases"]["files"] = [str(f) for f in uc_files if f.name != "__init__.py"]
    
    return patterns


def analyze_code_quality() -> Dict[str, Any]:
    """コード品質を分析"""
    print("📊 コード品質を分析中...")
    
    quality_result = {
        "status": "success",
        "overall_score": 100,
        "ruff_issues": [],
        "type_issues": [],
        "metrics": {}
    }
    
    # Ruff による静的解析
    try:
        ruff_cmd = ["uv", "run", "--frozen", "ruff", "check", "src/", "--output-format=json"]
        result = subprocess.run(ruff_cmd, capture_output=True, text=True, timeout=120)
        
        if result.returncode == 0:
            quality_result["ruff_issues"] = []
            quality_result["metrics"]["ruff_score"] = 100
        else:
            try:
                ruff_output = json.loads(result.stdout) if result.stdout else []
                quality_result["ruff_issues"] = ruff_output
                quality_result["metrics"]["ruff_score"] = max(0, 100 - len(ruff_output) * 2)
            except json.JSONDecodeError:
                quality_result["ruff_issues"] = [{"error": "Could not parse ruff output"}]
                quality_result["metrics"]["ruff_score"] = 80
                
    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
        quality_result["ruff_issues"] = [{"error": f"Ruff execution failed: {e}"}]
        quality_result["metrics"]["ruff_score"] = 80
    
    # Pyright による型チェック
    try:
        pyright_cmd = ["uv", "run", "--frozen", "pyright", "src/", "--outputjson"]
        result = subprocess.run(pyright_cmd, capture_output=True, text=True, timeout=120)
        
        try:
            pyright_output = json.loads(result.stdout) if result.stdout else {}
            error_count = pyright_output.get("summary", {}).get("errorCount", 0)
            warning_count = pyright_output.get("summary", {}).get("warningCount", 0)
            
            quality_result["type_issues"] = pyright_output.get("generalDiagnostics", [])
            quality_result["metrics"]["type_score"] = max(0, 100 - error_count * 5 - warning_count * 2)
            
        except json.JSONDecodeError:
            quality_result["type_issues"] = [{"error": "Could not parse pyright output"}]
            quality_result["metrics"]["type_score"] = 80
            
    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
        quality_result["type_issues"] = [{"error": f"Pyright execution failed: {e}"}]
        quality_result["metrics"]["type_score"] = 80
    
    # 全体スコア計算
    ruff_score = quality_result["metrics"].get("ruff_score", 80)
    type_score = quality_result["metrics"].get("type_score", 80)
    quality_result["overall_score"] = int((ruff_score + type_score) / 2)
    
    return quality_result


def analyze_test_quality() -> Dict[str, Any]:
    """テスト品質を分析"""
    print("🧪 テスト品質を分析中...")
    
    test_result = {
        "status": "success",
        "coverage_percentage": 0,
        "test_count": 0,
        "given_when_then_coverage": 0,
        "test_structure": {},
        "coverage_details": {}
    }
    
    # テストディレクトリの存在確認
    if not Path("tests").exists():
        test_result["status"] = "no_tests"
        return test_result
    
    # テスト数のカウント
    test_files = list(Path("tests").glob("**/*test*.py"))
    test_result["test_count"] = len(test_files)
    
    # pytest でカバレッジ実行
    try:
        coverage_cmd = [
            "uv", "run", "--frozen", "pytest",
            "--cov=src",
            "--cov-report=json:coverage.json",
            "-v",
            "--tb=short"
        ]
        
        result = subprocess.run(coverage_cmd, capture_output=True, text=True, timeout=300)
        
        # カバレッジJSONファイルを読み取り
        if Path("coverage.json").exists():
            try:
                with open("coverage.json", "r", encoding="utf-8") as f:
                    coverage_data = json.load(f)
                
                test_result["coverage_percentage"] = coverage_data.get("totals", {}).get("percent_covered", 0)
                test_result["coverage_details"] = coverage_data
                
            except json.JSONDecodeError:
                test_result["status"] = "coverage_error"
        
        # テスト構造の分析
        test_structure = {}
        for test_type in ["unit", "integration", "e2e"]:
            test_dir = Path(f"tests/{test_type}")
            if test_dir.exists():
                test_files_in_dir = list(test_dir.glob("**/*test*.py"))
                test_structure[test_type] = {
                    "files": len(test_files_in_dir),
                    "exists": True
                }
            else:
                test_structure[test_type] = {
                    "files": 0,
                    "exists": False
                }
        
        test_result["test_structure"] = test_structure
        
    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
        test_result["status"] = "execution_error"
        test_result["error"] = str(e)
    
    # Given-When-Then カバレッジの簡易分析
    gwt_coverage = analyze_given_when_then_coverage()
    test_result["given_when_then_coverage"] = gwt_coverage
    
    return test_result


def analyze_given_when_then_coverage() -> int:
    """Given-When-Then シナリオのカバレッジを分析"""
    
    # ユースケースファイルからシナリオ数を取得
    use_case_scenarios = 0
    use_cases_dir = Path("docs/use_cases")
    if use_cases_dir.exists():
        for json_file in use_cases_dir.glob("*.json"):
            try:
                with open(json_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                scenarios = data.get("given_when_then_scenarios", [])
                use_case_scenarios += len(scenarios)
            except Exception:
                continue
    
    # テストファイルからGiven-When-Thenパターンの検出
    test_gwt_count = 0
    if Path("tests").exists():
        for test_file in Path("tests").glob("**/*test*.py"):
            try:
                content = test_file.read_text(encoding="utf-8")
                # Given-When-Then パターンやBDD風のコメント/docstringを検出
                gwt_patterns = [
                    r'#.*given.*when.*then',
                    r'""".*given.*when.*then.*"""',
                    r"'''.*given.*when.*then.*'''",
                    r'def.*given.*when.*then',
                    r'def test.*scenario'
                ]
                
                for pattern in gwt_patterns:
                    matches = re.findall(pattern, content, re.IGNORECASE | re.DOTALL)
                    test_gwt_count += len(matches)
                    
            except Exception:
                continue
    
    if use_case_scenarios == 0:
        return 0
    
    return min(100, int((test_gwt_count / use_case_scenarios) * 100))


def analyze_business_value_delivery(use_case_data: Dict[str, Any]) -> Dict[str, Any]:
    """ビジネス価値実現度を分析"""
    print("💼 ビジネス価値実現度を分析中...")
    
    business_analysis = {
        "acceptance_criteria_coverage": 0,
        "user_story_implementation": "unknown",
        "business_rules_coverage": 0,
        "api_completeness": 0,
        "usability_score": 0
    }
    
    # 受け入れ基準のカバレッジ
    scenarios = use_case_data.get("given_when_then_scenarios", [])
    if scenarios:
        implemented_scenarios = 0
        for scenario in scenarios:
            # 簡易的な実装状況チェック（実際の実装では、より詳細な分析が必要）
            scenario_name = scenario.get("scenario", "")
            if scenario_name:
                # テストファイルでシナリオ名の検索
                if search_scenario_in_tests(scenario_name):
                    implemented_scenarios += 1
        
        business_analysis["acceptance_criteria_coverage"] = int((implemented_scenarios / len(scenarios)) * 100)
    
    # API完全性チェック
    api_completeness = check_api_completeness()
    business_analysis["api_completeness"] = api_completeness
    
    # ユーザビリティスコア（簡易版）
    usability_score = assess_usability()
    business_analysis["usability_score"] = usability_score
    
    return business_analysis


def search_scenario_in_tests(scenario_name: str) -> bool:
    """テストファイル内でシナリオが実装されているかチェック"""
    
    if not Path("tests").exists():
        return False
    
    # シナリオ名から検索キーワードを抽出
    keywords = scenario_name.lower().split()[:3]  # 最初の3単語を使用
    
    for test_file in Path("tests").glob("**/*test*.py"):
        try:
            content = test_file.read_text(encoding="utf-8").lower()
            if all(keyword in content for keyword in keywords):
                return True
        except Exception:
            continue
    
    return False


def check_api_completeness() -> int:
    """API完全性をチェック"""
    
    api_score = 0
    
    # プレゼンテーション層のAPIファイル存在チェック
    api_dir = Path("src/presentation/api")
    if api_dir.exists():
        api_files = list(api_dir.glob("**/*.py"))
        api_score += min(50, len(api_files) * 10)
    
    # CLI コマンド存在チェック
    cli_dir = Path("src/presentation/cli")
    if cli_dir.exists():
        cli_files = list(cli_dir.glob("**/*.py"))
        api_score += min(30, len(cli_files) * 10)
    
    # 認証・認可システム存在チェック
    auth_dir = Path("src/presentation/auth")
    if auth_dir.exists():
        api_score += 20
    
    return min(100, api_score)


def assess_usability() -> int:
    """ユーザビリティを評価"""
    
    usability_score = 50  # ベースライン
    
    # エラーハンドリング存在チェック
    if search_pattern_in_src(r'raise.*Exception|try.*except'):
        usability_score += 20
    
    # バリデーション存在チェック
    if search_pattern_in_src(r'validate|validation'):
        usability_score += 15
    
    # ログ出力存在チェック
    if search_pattern_in_src(r'logger|logging'):
        usability_score += 15
    
    return min(100, usability_score)


def search_pattern_in_src(pattern: str) -> bool:
    """srcディレクトリ内で指定パターンを検索"""
    
    if not Path("src").exists():
        return False
    
    for py_file in Path("src").glob("**/*.py"):
        try:
            content = py_file.read_text(encoding="utf-8")
            if re.search(pattern, content, re.IGNORECASE):
                return True
        except Exception:
            continue
    
    return False


def calculate_overall_quality_score(architecture_result: Dict[str, Any], 
                                  code_quality_result: Dict[str, Any],
                                  test_result: Dict[str, Any],
                                  business_result: Dict[str, Any]) -> Dict[str, Any]:
    """総合品質スコアを計算"""
    
    # 各項目の重み付け
    weights = {
        "architecture": 0.3,
        "code_quality": 0.25,
        "test_quality": 0.25,
        "business_value": 0.2
    }
    
    # 各スコアを取得
    arch_score = architecture_result.get("overall_compliance", 0)
    code_score = code_quality_result.get("overall_score", 0)
    test_score = min(100, test_result.get("coverage_percentage", 0) + 
                    (20 if test_result.get("test_count", 0) > 0 else 0))
    business_score = (
        business_result.get("acceptance_criteria_coverage", 0) * 0.4 +
        business_result.get("api_completeness", 0) * 0.3 +
        business_result.get("usability_score", 0) * 0.3
    )
    
    # 重み付け総合スコア
    overall_score = (
        arch_score * weights["architecture"] +
        code_score * weights["code_quality"] +
        test_score * weights["test_quality"] +
        business_score * weights["business_value"]
    )
    
    # 判定の決定
    if overall_score >= 90:
        judgment = "APPROVED"
        pr_ready = "READY"
    elif overall_score >= 70:
        judgment = "CONDITIONAL_APPROVAL"
        pr_ready = "CONDITIONAL"
    else:
        judgment = "REJECTED"
        pr_ready = "NOT_READY"
    
    return {
        "overall_score": int(overall_score),
        "component_scores": {
            "architecture": arch_score,
            "code_quality": code_score,
            "test_quality": test_score,
            "business_value": business_score
        },
        "judgment": judgment,
        "pr_ready": pr_ready,
        "weights": weights
    }


def generate_improvement_recommendations(architecture_result: Dict[str, Any],
                                       code_quality_result: Dict[str, Any], 
                                       test_result: Dict[str, Any],
                                       business_result: Dict[str, Any],
                                       overall_result: Dict[str, Any]) -> List[str]:
    """改善提案を生成"""
    
    recommendations = []
    
    # アーキテクチャ改善提案
    arch_score = architecture_result.get("overall_compliance", 0)
    if arch_score < 100:
        violations = architecture_result.get("dependency_violations", [])
        if violations:
            recommendations.append(
                f"🏗️ **アーキテクチャ違反**: {len(violations)}件の依存関係違反が見つかりました。"
                "Clean Architectureの原則に従って修正してください。"
            )
        
        missing_layers = [
            layer for layer, info in architecture_result.get("layer_structure", {}).items()
            if not info.get("exists", False)
        ]
        if missing_layers:
            recommendations.append(
                f"📁 **レイヤー不足**: {', '.join(missing_layers)} レイヤーが見つかりません。"
                "完全なレイヤー構造を実装してください。"
            )
    
    # コード品質改善提案
    code_score = code_quality_result.get("overall_score", 0)
    if code_score < 90:
        ruff_issues = len(code_quality_result.get("ruff_issues", []))
        if ruff_issues > 0:
            recommendations.append(
                f"📊 **静的解析**: {ruff_issues}件のコード品質問題が見つかりました。"
                "`uv run ruff check src/ --fix` で修正してください。"
            )
        
        type_issues = len(code_quality_result.get("type_issues", []))
        if type_issues > 0:
            recommendations.append(
                f"🔍 **型安全性**: {type_issues}件の型チェック問題があります。"
                "型ヒントを追加し、pyright の警告を解消してください。"
            )
    
    # テスト品質改善提案
    test_score = overall_result["component_scores"]["test_quality"]
    if test_score < 80:
        coverage = test_result.get("coverage_percentage", 0)
        if coverage < 80:
            recommendations.append(
                f"🧪 **テストカバレッジ**: 現在{coverage:.1f}%です。"
                "80%以上を目標に、不足しているテストを追加してください。"
            )
        
        test_count = test_result.get("test_count", 0)
        if test_count == 0:
            recommendations.append(
                "📝 **テスト不足**: テストファイルが見つかりません。"
                "`/create-tests` コマンドでテストを作成してください。"
            )
    
    # ビジネス価値改善提案
    business_score = overall_result["component_scores"]["business_value"]
    if business_score < 80:
        acceptance_coverage = business_result.get("acceptance_criteria_coverage", 0)
        if acceptance_coverage < 100:
            recommendations.append(
                f"✅ **受け入れ基準**: {acceptance_coverage}%のシナリオが実装されています。"
                "すべてのGiven-When-Thenシナリオを実装してください。"
            )
        
        api_completeness = business_result.get("api_completeness", 0)
        if api_completeness < 80:
            recommendations.append(
                "🌐 **API完全性**: APIエンドポイントが不足している可能性があります。"
                "必要なエンドポイントがすべて実装されているか確認してください。"
            )
    
    # 総合判定に基づく提案
    if overall_result["judgment"] == "REJECTED":
        recommendations.append(
            "❌ **再実装必要**: 品質基準を満たしていません。"
            "上記の改善事項を修正後、再度レビューを実行してください。"
        )
    elif overall_result["judgment"] == "CONDITIONAL_APPROVAL":
        recommendations.append(
            "⚠️ **条件付き承認**: 軽微な改善事項があります。"
            "`/apply-feedback` コマンドで修正後、PRを作成できます。"
        )
    else:
        recommendations.append(
            "✅ **承認完了**: すべての品質基準を満たしています。"
            "`/create-pr` コマンドでプルリクエストを作成できます。"
        )
    
    return recommendations


def generate_review_report(issue_number: str, architecture_result: Dict[str, Any],
                         code_quality_result: Dict[str, Any], test_result: Dict[str, Any],
                         business_result: Dict[str, Any], overall_result: Dict[str, Any],
                         recommendations: List[str]) -> str:
    """レビューレポートのMarkdownを生成"""
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    report = f"""# 実装品質レビューレポート

**Issue**: #{issue_number}  
**レビュー日時**: {timestamp}  
**総合判定**: {overall_result['judgment']}  
**総合スコア**: {overall_result['overall_score']}/100

## 📊 評価サマリー

| 評価項目 | スコア | 重み | 詳細 |
|----------|--------|------|------|
| アーキテクチャ準拠 | {overall_result['component_scores']['architecture']:.1f}/100 | {overall_result['weights']['architecture']:.0%} | Clean Architecture & DDD 準拠 |
| コード品質 | {overall_result['component_scores']['code_quality']:.1f}/100 | {overall_result['weights']['code_quality']:.0%} | 静的解析・型安全性 |
| テスト品質 | {overall_result['component_scores']['test_quality']:.1f}/100 | {overall_result['weights']['test_quality']:.0%} | カバレッジ・テスト構造 |
| ビジネス価値 | {overall_result['component_scores']['business_value']:.1f}/100 | {overall_result['weights']['business_value']:.0%} | 要件実現・ユーザビリティ |

## 🏗️ アーキテクチャ準拠性分析

**準拠率**: {architecture_result['overall_compliance']:.1f}%

### レイヤー構造
"""
    
    for layer, info in architecture_result.get("layer_structure", {}).items():
        status = "✅" if info["exists"] else "❌"
        report += f"- **{layer}**: {status} ({info['files_count']}ファイル)\n"
    
    violations = architecture_result.get("dependency_violations", [])
    if violations:
        report += f"\n### ⚠️ 依存関係違反 ({len(violations)}件)\n"
        for violation in violations[:3]:  # 最大3件表示
            report += f"- `{violation['file']}`: {violation['details']}\n"
    
    report += f"""

### DDD パターン適用状況
"""
    
    patterns = architecture_result.get("pattern_adherence", {})
    for pattern_name, pattern_info in patterns.items():
        count = pattern_info.get("found", 0)
        status = "✅" if count > 0 else "⚠️"
        report += f"- **{pattern_name}**: {status} {count}個\n"
    
    report += f"""

## 📊 コード品質分析

**総合スコア**: {code_quality_result['overall_score']}/100

### 静的解析結果
- **Ruffスコア**: {code_quality_result['metrics'].get('ruff_score', 0):.1f}/100
- **型チェックスコア**: {code_quality_result['metrics'].get('type_score', 0):.1f}/100

"""
    
    ruff_issues = code_quality_result.get("ruff_issues", [])
    if ruff_issues and len(ruff_issues) > 0:
        report += f"### ⚠️ 静的解析問題 ({len(ruff_issues)}件)\n"
        for issue in ruff_issues[:3]:  # 最大3件表示
            if isinstance(issue, dict) and "filename" in issue:
                report += f"- `{issue.get('filename', 'unknown')}`: {issue.get('message', 'unknown issue')}\n"
    
    report += f"""

## 🧪 テスト品質分析

**カバレッジ**: {test_result['coverage_percentage']:.1f}%  
**テストファイル数**: {test_result['test_count']}  
**Given-When-Thenカバレッジ**: {test_result['given_when_then_coverage']}%

### テスト構造
"""
    
    for test_type, info in test_result.get("test_structure", {}).items():
        status = "✅" if info["exists"] else "❌"
        report += f"- **{test_type}**: {status} ({info['files']}ファイル)\n"
    
    report += f"""

## 💼 ビジネス価値分析

### 実装状況
- **受け入れ基準達成**: {business_result['acceptance_criteria_coverage']}%
- **API完全性**: {business_result['api_completeness']}%
- **ユーザビリティスコア**: {business_result['usability_score']}/100

## 💡 改善提案

"""
    
    for i, recommendation in enumerate(recommendations, 1):
        report += f"{i}. {recommendation}\n\n"
    
    report += f"""

## ✅ 判定結果

**総合判定**: {overall_result['judgment']}  
**プルリクエスト準備**: {overall_result['pr_ready']}

### 次のステップ

"""
    
    if overall_result["judgment"] == "APPROVED":
        report += f"1. `/create-pr {issue_number}` - プルリクエスト作成\n"
    elif overall_result["judgment"] == "CONDITIONAL_APPROVAL":
        report += f"1. `/apply-feedback {issue_number}` - 改善事項の適用\n"
        report += f"2. `/create-pr {issue_number}` - 改善後PR作成\n"
    else:
        report += f"1. 上記改善事項の修正\n"
        report += f"2. `/review-issue {issue_number}` - 再レビュー\n"
    
    report += f"""

---

*このレポートは `/review-issue` コマンドによって自動生成されました。*
"""
    
    return report


def save_review_results(issue_number: str, architecture_result: Dict[str, Any],
                       code_quality_result: Dict[str, Any], test_result: Dict[str, Any],
                       business_result: Dict[str, Any], overall_result: Dict[str, Any],
                       recommendations: List[str], reviews_dir: Path) -> List[str]:
    """レビュー結果をファイルに保存"""
    
    created_files = []
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # メインレビューレポート (Markdown)
    report_content = generate_review_report(
        issue_number, architecture_result, code_quality_result,
        test_result, business_result, overall_result, recommendations
    )
    
    report_path = reviews_dir / f"implementation-review-{issue_number}-{timestamp}.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_content)
    created_files.append(str(report_path))
    
    # アーキテクチャ準拠性詳細 (JSON)
    arch_path = reviews_dir / f"architecture-compliance-{issue_number}-{timestamp}.json"
    with open(arch_path, 'w', encoding='utf-8') as f:
        json.dump(architecture_result, f, indent=2, ensure_ascii=False, default=str)
    created_files.append(str(arch_path))
    
    # 品質メトリクス詳細 (JSON)
    metrics_data = {
        "issue_number": issue_number,
        "timestamp": timestamp,
        "overall_result": overall_result,
        "architecture": architecture_result,
        "code_quality": code_quality_result,
        "test_quality": test_result,
        "business_value": business_result,
        "recommendations": recommendations
    }
    
    metrics_path = reviews_dir / f"quality-metrics-{issue_number}-{timestamp}.json"
    with open(metrics_path, 'w', encoding='utf-8') as f:
        json.dump(metrics_data, f, indent=2, ensure_ascii=False, default=str)
    created_files.append(str(metrics_path))
    
    # 改善提案 (Markdown)
    improvements_content = f"""# 改善提案 - Issue #{issue_number}

**生成日時**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  
**総合判定**: {overall_result['judgment']}

## 優先度別改善事項

"""
    
    for i, recommendation in enumerate(recommendations, 1):
        improvements_content += f"### {i}. {recommendation}\n\n"
    
    improvements_path = reviews_dir / f"improvement-recommendations-{issue_number}-{timestamp}.md"
    with open(improvements_path, 'w', encoding='utf-8') as f:
        f.write(improvements_content)
    created_files.append(str(improvements_path))
    
    return created_files


def update_use_case_json_with_review_results(json_file_path: str, overall_result: Dict[str, Any],
                                           architecture_result: Dict[str, Any],
                                           test_result: Dict[str, Any]):
    """ユースケースJSONにレビュー結果を更新"""
    
    use_case_data = load_use_case_json(json_file_path)
    
    # レビュー情報を更新
    review_info = use_case_data.get("implementation_details", {})
    review_info["quality_review"] = {
        "completed": True,
        "timestamp": datetime.now().isoformat(),
        "overall_judgment": overall_result["judgment"],
        "overall_score": overall_result["overall_score"],
        "pr_ready": overall_result["pr_ready"],
        "component_scores": overall_result["component_scores"],
        "architecture_compliance": architecture_result.get("overall_compliance", 0),
        "test_coverage": test_result.get("coverage_percentage", 0),
        "review_status": "completed"
    }
    use_case_data["implementation_details"] = review_info
    
    # TDDフェーズを更新
    update_tdd_phase(use_case_data, "quality_review")
    
    # 保存
    save_use_case_json(json_file_path, use_case_data)
    
    return use_case_data


def main():
    """メイン処理"""
    
    # 引数チェック
    if len(sys.argv) < 2:
        print("❌ エラー: Issue番号が必要です")
        print("使用方法: /review-issue <issue-number>")
        sys.exit(1)
    
    issue_number = sys.argv[1]
    print(f"\n🔍 Issue #{issue_number} の実装品質レビューを開始します\n")
    
    # ユースケースJSONファイルを検索
    print("📁 ユースケースJSONファイルを検索中...")
    json_file_path = find_use_case_json(issue_number)
    
    if not json_file_path:
        print(f"❌ Issue #{issue_number} のユースケースJSONが見つかりません")
        print("先に /create-use-case コマンドを実行してください")
        sys.exit(1)
    
    print(f"✅ JSONファイルを発見: {json_file_path}")
    use_case_data = load_use_case_json(json_file_path)
    
    # レビュー結果保存ディレクトリ準備
    reviews_dir = ensure_reviews_directory()
    print(f"📁 レビュー結果保存先: {reviews_dir}")
    
    # 各種分析を実行
    print("\n🔍 品質分析実行")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    # 1. アーキテクチャ準拠性分析
    architecture_result = analyze_architecture_compliance()
    arch_score = architecture_result["overall_compliance"]
    print(f"✅ アーキテクチャ分析完了: {arch_score:.1f}%準拠")
    
    # 2. コード品質分析
    code_quality_result = analyze_code_quality()
    code_score = code_quality_result["overall_score"]
    print(f"✅ コード品質分析完了: {code_score}/100スコア")
    
    # 3. テスト品質分析
    test_result = analyze_test_quality()
    test_coverage = test_result.get("coverage_percentage", 0)
    print(f"✅ テスト分析完了: {test_coverage:.1f}%カバレッジ")
    
    # 4. ビジネス価値分析
    business_result = analyze_business_value_delivery(use_case_data)
    acceptance_coverage = business_result["acceptance_criteria_coverage"]
    print(f"✅ ビジネス価値分析完了: {acceptance_coverage}%受け入れ基準")
    
    # 総合評価計算
    print("\n📊 総合評価計算")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    overall_result = calculate_overall_quality_score(
        architecture_result, code_quality_result, test_result, business_result
    )
    
    print(f"🏆 総合スコア: {overall_result['overall_score']}/100")
    print(f"⚖️ 判定結果: {overall_result['judgment']}")
    print(f"📋 PR準備状況: {overall_result['pr_ready']}")
    
    # 改善提案生成
    print("\n💡 改善提案生成")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    recommendations = generate_improvement_recommendations(
        architecture_result, code_quality_result, test_result, business_result, overall_result
    )
    print(f"✅ {len(recommendations)}件の改善提案を生成")
    
    # レビュー結果保存
    print("\n📋 レビューレポート生成")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    created_files = save_review_results(
        issue_number, architecture_result, code_quality_result,
        test_result, business_result, overall_result, recommendations, reviews_dir
    )
    print(f"✅ レビューレポート保存完了: {len(created_files)}ファイル")
    
    # ユースケースJSONを更新
    print("📊 ユースケースJSONを更新中...")
    update_use_case_json_with_review_results(json_file_path, overall_result, architecture_result, test_result)
    
    # 実行履歴を更新
    update_execution_history(
        json_file_path,
        f"/review-issue {issue_number}",
        "success" if overall_result["judgment"] != "REJECTED" else "conditional",
        created_files
    )
    
    # 最新データを読み込んで表示
    final_data = load_use_case_json(json_file_path)
    
    # 実行状況を表示
    print("\n" + "="*60)
    print(format_execution_status(final_data))
    print("="*60)
    
    # 詳細サマリー表示
    print(f"\n🔍 実装品質レビューサマリー")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"📊 総合判定: {overall_result['judgment']}")
    print(f"🏆 総合スコア: {overall_result['overall_score']}/100")
    
    print(f"\n📈 コンポーネントスコア")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    for component, score in overall_result["component_scores"].items():
        print(f"✅ {component}: {score:.1f}/100")
    
    print(f"\n📁 生成ファイル")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    for file_path in created_files:
        print(f"✅ {file_path}")
    
    print(f"\n💡 改善提案")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    for i, recommendation in enumerate(recommendations, 1):
        print(f"{i}. {recommendation}")
    
    print(f"\n⏭️ 次の推奨コマンド")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    if overall_result["judgment"] == "APPROVED":
        print(f"1. /create-pr {issue_number}")
        print(f"   → 品質基準をすべて満たしているため、即座にPR作成可能")
    elif overall_result["judgment"] == "CONDITIONAL_APPROVAL":
        print(f"1. /apply-feedback {issue_number}")
        print(f"   → 軽微な改善事項を修正")
        print(f"2. /create-pr {issue_number}")
        print(f"   → 修正後にPR作成")
    else:
        print(f"1. 上記の改善事項を修正")
        print(f"2. /review-issue {issue_number}")
        print(f"   → 修正後に再レビュー実行")
    
    print(f"\n💡 実装品質レビュー完了")
    
    if overall_result["judgment"] == "APPROVED":
        print("🎉 すべての品質基準を満たしています！プルリクエストを作成できます。")
    elif overall_result["judgment"] == "CONDITIONAL_APPROVAL":
        print("⚠️ 軽微な改善事項があります。修正後にプルリクエストを作成してください。")
    else:
        print("❌ 品質基準を満たしていません。改善事項を修正後、再度レビューしてください。")


if __name__ == "__main__":
    main()