#!/usr/bin/env python3
"""
Review Test Design Expert Command - 改修版
TDD準拠性とテスト品質を評価し、段階的GREEN移行の準備を確認
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


def find_test_files(issue_number):
    """Issue番号に関連するテストファイルを検索"""
    test_files = []
    tests_dir = Path("tests")
    
    if not tests_dir.exists():
        return test_files
    
    # Issue番号を含むテストファイルを検索
    patterns = [
        f"*test*issue*{issue_number}*.py",
        f"test_issue_{issue_number}*.py",
        f"*{issue_number}*test*.py"
    ]
    
    for pattern in patterns:
        for test_file in tests_dir.glob(f"**/{pattern}"):
            test_files.append(str(test_file))
    
    # テストディレクトリ全体でissue番号を含むファイルも検索
    for py_file in tests_dir.glob("**/*.py"):
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if re.search(rf'issue.*{issue_number}|Issue.*{issue_number}', content, re.IGNORECASE):
                    test_files.append(str(py_file))
        except Exception:
            continue
    
    # 重複を除去
    return list(set(test_files))


def run_tests_and_analyze(test_files):
    """テストを実行してRED状態を分析"""
    analysis = {
        "all_tests_fail": False,
        "failure_reasons": [],
        "valid_failures": 0,
        "invalid_failures": 0,
        "passing_tests": 0,
        "total_tests": 0,
        "layer_categorization": {
            "domain": [],
            "use_case": [],
            "infrastructure": [],
            "presentation": []
        }
    }
    
    if not test_files:
        return analysis
    
    try:
        # テストを実行（詳細出力）
        result = subprocess.run(
            ["uv", "run", "--frozen", "pytest"] + test_files + ["-v", "--tb=short", "--no-header"],
            capture_output=True,
            text=True,
            cwd=os.getcwd()
        )
        
        output = result.stdout + result.stderr
        
        # テスト結果を解析
        test_lines = [line for line in output.split('\n') if '::' in line and ('PASSED' in line or 'FAILED' in line)]
        
        for line in test_lines:
            analysis["total_tests"] += 1
            
            if 'PASSED' in line:
                analysis["passing_tests"] += 1
            elif 'FAILED' in line:
                # 失敗理由を分析
                if any(keyword in line.lower() for keyword in ['importerror', 'notimplementederror', 'attributeerror']):
                    analysis["valid_failures"] += 1
                    analysis["failure_reasons"].append("Valid failure (missing implementation)")
                else:
                    analysis["invalid_failures"] += 1
                    analysis["failure_reasons"].append("Invalid failure (possible test bug)")
            
            # レイヤー分類
            line_lower = line.lower()
            if 'domain' in line_lower:
                analysis["layer_categorization"]["domain"].append(line)
            elif 'use_case' in line_lower or 'usecase' in line_lower:
                analysis["layer_categorization"]["use_case"].append(line)
            elif 'infra' in line_lower or 'repository' in line_lower:
                analysis["layer_categorization"]["infrastructure"].append(line)
            elif 'presentation' in line_lower or 'api' in line_lower or 'cli' in line_lower:
                analysis["layer_categorization"]["presentation"].append(line)
        
        # RED状態の判定
        analysis["all_tests_fail"] = (analysis["passing_tests"] == 0 and analysis["total_tests"] > 0)
        
    except Exception as e:
        print(f"❌ テスト実行エラー: {e}")
    
    return analysis


def analyze_test_structure(test_files):
    """テスト構造を分析"""
    structure_analysis = {
        "test_independence": True,
        "layer_isolation": True,
        "scenario_coverage": 0,
        "business_intent_clarity": 0,
        "mock_usage": False,
        "test_categories": {
            "unit": 0,
            "integration": 0,
            "e2e": 0
        },
        "violations": []
    }
    
    for test_file in test_files:
        try:
            with open(test_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Given-When-Thenパターンの検出
            gwt_patterns = len(re.findall(r'given|when|then|should', content, re.IGNORECASE))
            structure_analysis["scenario_coverage"] += gwt_patterns
            
            # ビジネス意図の明確性（テスト名の品質）
            test_names = re.findall(r'def test_[a-zA-Z_]+', content)
            clear_names = [name for name in test_names if len(name.split('_')) > 2]
            structure_analysis["business_intent_clarity"] += len(clear_names)
            
            # モック使用の検出
            if re.search(r'@mock|Mock|patch|unittest\.mock', content):
                structure_analysis["mock_usage"] = True
            
            # レイヤー依存関係の違反を検出
            if 'domain' in test_file.lower():
                if re.search(r'from.*infrastructure|from.*presentation|import.*infrastructure|import.*presentation', content):
                    structure_analysis["layer_isolation"] = False
                    structure_analysis["violations"].append(f"Domain test {test_file} has invalid dependencies")
            
            if 'use_case' in test_file.lower():
                if re.search(r'from.*infrastructure|from.*presentation|import.*infrastructure|import.*presentation', content):
                    structure_analysis["layer_isolation"] = False
                    structure_analysis["violations"].append(f"Use case test {test_file} has invalid dependencies")
            
            # テストカテゴリの分類
            if 'unit' in test_file.lower() or 'domain' in test_file.lower():
                structure_analysis["test_categories"]["unit"] += 1
            elif 'integration' in test_file.lower() or 'infra' in test_file.lower():
                structure_analysis["test_categories"]["integration"] += 1
            elif 'e2e' in test_file.lower() or 'presentation' in test_file.lower():
                structure_analysis["test_categories"]["e2e"] += 1
                
        except Exception as e:
            print(f"❌ テストファイル分析エラー ({test_file}): {e}")
            continue
    
    return structure_analysis


def calculate_quality_score(test_analysis, structure_analysis):
    """品質スコアを計算"""
    score = 0
    max_score = 100
    
    # TDD RED状態（30点）
    if test_analysis["all_tests_fail"] and test_analysis["total_tests"] > 0:
        score += 30
    elif test_analysis["passing_tests"] == 0:
        score += 20  # テストが存在しないが失敗もしていない
    
    # 有効な失敗理由（20点）
    if test_analysis["total_tests"] > 0:
        valid_ratio = test_analysis["valid_failures"] / test_analysis["total_tests"]
        score += int(20 * valid_ratio)
    
    # レイヤー分離（20点）
    if structure_analysis["layer_isolation"]:
        score += 20
    
    # シナリオカバレッジ（15点）
    if structure_analysis["scenario_coverage"] > 0:
        score += min(15, structure_analysis["scenario_coverage"] * 2)
    
    # ビジネス意図の明確性（10点）
    if structure_analysis["business_intent_clarity"] > 0:
        score += min(10, structure_analysis["business_intent_clarity"] * 2)
    
    # 適切なモック使用（5点）
    if structure_analysis["mock_usage"]:
        score += 5
    
    return min(score, max_score)


def determine_status(quality_score, test_analysis, structure_analysis):
    """総合ステータスを決定"""
    if quality_score >= 90 and test_analysis["all_tests_fail"] and structure_analysis["layer_isolation"]:
        return "APPROVED"
    elif quality_score >= 70 and test_analysis["passing_tests"] == 0:
        return "CONDITIONAL_APPROVAL"
    else:
        return "REJECTED"


def determine_staged_readiness(structure_analysis, test_analysis):
    """段階的実装準備度を判定"""
    if not structure_analysis["layer_isolation"]:
        return "LAYER_VIOLATIONS"
    
    layer_categories = structure_analysis["test_categories"]
    if sum(layer_categories.values()) == 0:
        return "NEEDS_CATEGORIZATION"
    
    return "STAGED_READY"


def generate_review_report(issue_number, test_analysis, structure_analysis, quality_score, issue_data, test_files):
    """テスト設計レビューレポートを生成"""
    reports_dir = Path("docs/reviews")
    reports_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = reports_dir / f"test-design-review-issue-{issue_number}-{timestamp}.md"
    
    issue_title = issue_data.get("title", "Unknown") if issue_data else "Unknown"
    status = determine_status(quality_score, test_analysis, structure_analysis)
    staged_readiness = determine_staged_readiness(structure_analysis, test_analysis)
    
    report_content = f"""# テスト設計レビューレポート

## 基本情報
- **Issue番号**: #{issue_number}
- **Issue タイトル**: {issue_title}
- **レビュー実行日時**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
- **総合判定**: {status}
- **段階的実装準備度**: {staged_readiness}

## TDD準拠性評価

### 品質スコア: {quality_score}/100

### TDD RED段階検証
- **全テスト失敗**: {"✅ Yes" if test_analysis["all_tests_fail"] else "❌ No"}
- **総テスト数**: {test_analysis["total_tests"]}
- **失敗テスト数**: {test_analysis["valid_failures"] + test_analysis["invalid_failures"]}
- **成功テスト数**: {test_analysis["passing_tests"]}
- **有効な失敗**: {test_analysis["valid_failures"]}件
- **無効な失敗**: {test_analysis["invalid_failures"]}件

### レイヤー分離検証
- **レイヤー分離**: {"✅ Pass" if structure_analysis["layer_isolation"] else "❌ Fail"}
- **検出された違反**: {len(structure_analysis["violations"])}件

### テストカテゴリ分布
- **ユニットテスト**: {structure_analysis["test_categories"]["unit"]}個
- **統合テスト**: {structure_analysis["test_categories"]["integration"]}個
- **E2Eテスト**: {structure_analysis["test_categories"]["e2e"]}個

### シナリオカバレッジ
- **Given-When-Thenパターン**: {structure_analysis["scenario_coverage"]}個検出
- **明確なテスト名**: {structure_analysis["business_intent_clarity"]}個
- **モック使用**: {"✅ Yes" if structure_analysis["mock_usage"] else "❌ No"}

## 検出されたテストファイル
"""
    
    for test_file in test_files:
        report_content += f"- {test_file}\n"
    
    report_content += f"""

## レイヤー別テスト分類
### ドメイン層テスト
{len(test_analysis["layer_categorization"]["domain"])}個のテストを検出

### ユースケース層テスト
{len(test_analysis["layer_categorization"]["use_case"])}個のテストを検出

### インフラストラクチャ層テスト
{len(test_analysis["layer_categorization"]["infrastructure"])}個のテストを検出

### プレゼンテーション層テスト
{len(test_analysis["layer_categorization"]["presentation"])}個のテストを検出

## 段階的GREEN移行計画

### 実装段階順序
1. **Phase 6: ドメイン実装**
   - コマンド: `uv run --frozen pytest tests/ -k "domain" -v`
   - 期待結果: ドメインテストのみGREEN

2. **Phase 7: ユースケース実装**
   - コマンド: `uv run --frozen pytest tests/ -k "domain or use_case" -v`
   - 期待結果: ドメイン+ユースケーステストGREEN

3. **Phase 8: インフラストラクチャ実装**
   - コマンド: `uv run --frozen pytest tests/ -k "domain or use_case or infra" -v`
   - 期待結果: プレゼンテーション層以外GREEN

4. **Phase 9: プレゼンテーション実装**
   - コマンド: `uv run --frozen pytest tests/ -v`
   - 期待結果: 全テストGREEN

## 推奨事項
"""
    
    recommendations = []
    
    if not test_analysis["all_tests_fail"]:
        recommendations.append("全テストが適切に失敗するよう、実装コードを削除または修正してください")
    
    if test_analysis["passing_tests"] > 0:
        recommendations.append(f"{test_analysis['passing_tests']}個の成功テストを修正し、RED状態を確立してください")
    
    if test_analysis["invalid_failures"] > 0:
        recommendations.append(f"{test_analysis['invalid_failures']}個のテストでロジックエラーが検出されました。テスト実装を確認してください")
    
    if not structure_analysis["layer_isolation"]:
        recommendations.append("レイヤー間の依存関係違反を修正してください")
        for violation in structure_analysis["violations"]:
            recommendations.append(f"  - {violation}")
    
    if structure_analysis["scenario_coverage"] < 3:
        recommendations.append("Given-When-Thenシナリオのカバレッジを向上させてください")
    
    if not structure_analysis["mock_usage"]:
        recommendations.append("インフラストラクチャテストでの適切なモック使用を検討してください")
    
    if not recommendations:
        recommendations.append("テスト設計は良好です。ドメイン実装を開始できます。")
    
    for i, recommendation in enumerate(recommendations, 1):
        report_content += f"{i}. {recommendation}\n"
    
    report_content += f"""

## 次のステップ

"""
    
    if status == "APPROVED" and staged_readiness == "STAGED_READY":
        report_content += """
### 即座に実行可能
- `/implement-domain {issue_number}` - ドメイン層実装の開始

### 品質保証
- TDD RED状態が確立されています
- レイヤー分離が適切です
- 段階的実装の準備が整っています
"""
    elif status == "CONDITIONAL_APPROVAL":
        report_content += """
### 条件付き実行
- 軽微な改善後、`/implement-domain {issue_number}` を実行可能

### 改善事項
- テスト品質の一部改善が推奨されます
- 実装と並行して改善可能です
"""
    else:
        report_content += """
### 要改善
- `/create-tests {issue_number}` でテストの再作成が必要
- テスト品質向上後に再レビューを実施

### 改善が必要な領域
- TDD RED状態の確立
- レイヤー分離の改善
- テスト構造の最適化
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
        print("使用方法: /review-test-design <issue-number>")
        sys.exit(1)
    
    issue_number = sys.argv[1]
    print(f"\n🧪 Issue #{issue_number} のテスト設計レビューを開始します\n")
    
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
    
    # テストファイルを検索
    print("\n🧪 テストファイルを検索中...")
    test_files = find_test_files(issue_number)
    
    if not test_files:
        print(f"❌ Issue #{issue_number} に関連するテストファイルが見つかりません")
        print("先に /create-tests コマンドを実行してください")
        sys.exit(1)
    
    print(f"✅ テストファイルを発見: {len(test_files)}個")
    for test_file in test_files:
        print(f"  - {test_file}")
    
    # TDD RED状態を検証
    print("\n🔍 TDD RED状態を検証中...")
    test_analysis = run_tests_and_analyze(test_files)
    
    # テスト構造を分析
    print("\n🏗️ テスト構造を分析中...")
    structure_analysis = analyze_test_structure(test_files)
    
    # 品質スコアを計算
    quality_score = calculate_quality_score(test_analysis, structure_analysis)
    
    # ステータスを決定
    status = determine_status(quality_score, test_analysis, structure_analysis)
    staged_readiness = determine_staged_readiness(structure_analysis, test_analysis)
    
    # レビューレポートを生成
    print("\n📊 テスト設計レビューレポートを生成中...")
    report_file = generate_review_report(issue_number, test_analysis, structure_analysis, quality_score, issue_data, test_files)
    
    # ユースケースデータを読み込み
    use_case_data = load_use_case_json(json_file_path)
    
    # テスト設計レビュー情報を更新
    test_review = {
        "status": status,
        "staged_readiness": staged_readiness,
        "completed_at": datetime.now().isoformat(),
        "test_quality_score": quality_score,
        "red_phase_compliance": (test_analysis["valid_failures"] / max(test_analysis["total_tests"], 1)) * 100,
        "layer_isolation_score": 100 if structure_analysis["layer_isolation"] else 0,
        "total_tests": test_analysis["total_tests"],
        "report_file": report_file,
        "implementation_phases": {
            "domain_ready": len(test_analysis["layer_categorization"]["domain"]) > 0,
            "use_case_ready": len(test_analysis["layer_categorization"]["use_case"]) > 0,
            "infrastructure_ready": len(test_analysis["layer_categorization"]["infrastructure"]) > 0,
            "presentation_ready": len(test_analysis["layer_categorization"]["presentation"]) > 0
        }
    }
    
    use_case_data.setdefault("quality_gates", {})["test_design_review"] = test_review
    save_use_case_json(json_file_path, use_case_data)
    
    # 実行履歴を更新
    update_execution_history(
        json_file_path,
        f"/review-test-design {issue_number}",
        "success" if status != "ERROR" else "failed",
        [report_file] + test_files
    )
    
    # 更新されたデータを読み込み
    updated_data = load_use_case_json(json_file_path)
    
    # 実行状況を表示
    print("\n" + "="*60)
    print(format_execution_status(updated_data))
    print("="*60)
    
    # 結果サマリー表示
    print(f"\n📊 テスト設計レビュー結果")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"🎯 総合判定: {status}")
    print(f"🏗️ 段階的実装準備度: {staged_readiness}")
    print(f"📈 品質スコア: {quality_score}/100")
    print(f"🧪 総テスト数: {test_analysis['total_tests']}個")
    print(f"🔴 RED状態: {'✅ Yes' if test_analysis['all_tests_fail'] else '❌ No'}")
    print(f"🏢 レイヤー分離: {'✅ Pass' if structure_analysis['layer_isolation'] else '❌ Fail'}")
    
    print(f"\n📁 成果物")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"✅ {report_file}")
    
    print(f"\n🏗️ レイヤー別テスト分布")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"📦 ドメイン: {len(test_analysis['layer_categorization']['domain'])}個")
    print(f"🎯 ユースケース: {len(test_analysis['layer_categorization']['use_case'])}個")
    print(f"🏗️ インフラ: {len(test_analysis['layer_categorization']['infrastructure'])}個")
    print(f"🎨 プレゼンテーション: {len(test_analysis['layer_categorization']['presentation'])}個")
    
    print(f"\n⏭️ 次の推奨コマンド")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    if status == "APPROVED" and staged_readiness == "STAGED_READY":
        print(f"✅ テスト設計承認済み - 即座に実行可能:")
        print(f"   /implement-domain {issue_number}")
        print(f"   → ドメイン層実装の開始")
        print(f"\n🧪 段階的テスト実行コマンド:")
        print(f"   uv run --frozen pytest tests/ -k \"domain\" -v")
        print(f"   → ドメイン実装後のテスト確認")
    elif status == "CONDITIONAL_APPROVAL":
        print(f"⚠️ 条件付き承認:")
        print(f"   /implement-domain {issue_number}")
        print(f"   → 実装開始（改善と並行）")
        print(f"   または")
        print(f"   /create-tests {issue_number}")
        print(f"   → テスト改善後に実装")
    else:
        print(f"❌ テスト設計要改善:")
        print(f"   /create-tests {issue_number}")
        print(f"   → テストの再作成")
        print(f"   その後")
        print(f"   /review-test-design {issue_number}")
        print(f"   → 再レビュー実施")
    
    # 最終メッセージ
    status_emoji = {"APPROVED": "✅", "CONDITIONAL_APPROVAL": "⚠️", "REJECTED": "❌"}
    emoji = status_emoji.get(status, "❓")
    
    print(f"\n{emoji} テスト設計レビュー完了")
    print(f"詳細なレビュー結果は {report_file} に記録されました。")


if __name__ == "__main__":
    main()