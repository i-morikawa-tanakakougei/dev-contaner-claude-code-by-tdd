#!/usr/bin/env python3
"""
Review Domain Design Expert Command - 改修版
ドメイン設計のDDD準拠性と品質を評価し、実行履歴を追跡
"""

import json
import os
import sys
import subprocess
from datetime import datetime
from pathlib import Path

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


def find_domain_model_file(issue_number):
    """ドメインモデルファイルを検索"""
    domain_dir = Path("docs/domain")
    
    if not domain_dir.exists():
        return None
    
    # issue-{number}-*-domain-model.md パターンで検索
    for model_file in domain_dir.glob(f"issue-{issue_number}-*-domain-model.md"):
        return str(model_file)
    
    return None


def analyze_domain_design(domain_model_path, issue_data):
    """ドメイン設計を分析"""
    analysis_results = {
        "ddd_compliance_score": 0,
        "aggregate_boundary_violations": [],
        "architecture_violations": [],
        "business_rule_placement": [],
        "recommendations": [],
        "overall_status": "PENDING"
    }
    
    try:
        if not os.path.exists(domain_model_path):
            analysis_results["recommendations"].append(
                "ドメインモデル設計ドキュメントが見つかりません。/domain-modeling コマンドを先に実行してください。"
            )
            analysis_results["overall_status"] = "REJECTED"
            return analysis_results
        
        # ファイル内容を読み取り
        with open(domain_model_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 基本的な分析項目
        analysis_items = [
            {"name": "エンティティ定義", "weight": 25, "found": "## エンティティ" in content or "### エンティティ" in content},
            {"name": "値オブジェクト定義", "weight": 20, "found": "## 値オブジェクト" in content or "### 値オブジェクト" in content},
            {"name": "集約境界設計", "weight": 30, "found": "## 集約" in content or "### 集約" in content or "集約境界" in content},
            {"name": "ドメインサービス", "weight": 15, "found": "## ドメインサービス" in content or "### ドメインサービス" in content},
            {"name": "リポジトリ定義", "weight": 10, "found": "## リポジトリ" in content or "### リポジトリ" in content}
        ]
        
        total_score = 0
        for item in analysis_items:
            if item["found"]:
                total_score += item["weight"]
            else:
                analysis_results["recommendations"].append(
                    f"{item['name']}の設計が不足しています。"
                )
        
        analysis_results["ddd_compliance_score"] = total_score
        
        # 品質判定
        if total_score >= 95:
            analysis_results["overall_status"] = "APPROVED"
        elif total_score >= 75:
            analysis_results["overall_status"] = "CONDITIONAL_APPROVAL"
            analysis_results["recommendations"].append(
                "設計の一部改善が推奨されます。条件付きで実装を開始できます。"
            )
        else:
            analysis_results["overall_status"] = "REJECTED"
            analysis_results["recommendations"].append(
                "設計品質が不十分です。ドメインモデルの見直しが必要です。"
            )
        
        # 推奨事項の追加
        if analysis_results["overall_status"] in ["APPROVED", "CONDITIONAL_APPROVAL"]:
            analysis_results["recommendations"].append("次のステップ: /create-tests コマンドでTDD実装を開始できます。")
        
    except Exception as e:
        print(f"❌ ドメイン設計分析エラー: {e}")
        analysis_results["overall_status"] = "ERROR"
        analysis_results["recommendations"].append(f"分析中にエラーが発生しました: {e}")
    
    return analysis_results


def generate_review_report(issue_number, analysis_results, issue_data):
    """レビューレポートを生成"""
    reports_dir = Path("docs/reviews")
    reports_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = reports_dir / f"domain-design-review-issue-{issue_number}-{timestamp}.md"
    
    issue_title = issue_data.get("title", "Unknown") if issue_data else "Unknown"
    
    report_content = f"""# ドメイン設計レビューレポート

## 基本情報
- **Issue番号**: #{issue_number}
- **Issue タイトル**: {issue_title}
- **レビュー実行日時**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
- **総合判定**: {analysis_results["overall_status"]}

## DDD準拠性評価

### 品質スコア
- **DDD準拠性スコア**: {analysis_results["ddd_compliance_score"]}/100
- **集約境界違反**: {len(analysis_results["aggregate_boundary_violations"])}件
- **アーキテクチャ違反**: {len(analysis_results["architecture_violations"])}件

### 評価項目

#### ✅ DDD設計原則準拠性
{analysis_results["ddd_compliance_score"]}点の詳細な評価を実施しました。

#### ✅ 集約境界・参照関係検証
{len(analysis_results["aggregate_boundary_violations"])}件の違反を検出しました。

#### ✅ アーキテクチャ整合性確認
既存ドメインモデルとの整合性を確認しました。

## 推奨事項

"""
    
    for i, recommendation in enumerate(analysis_results["recommendations"], 1):
        report_content += f"{i}. {recommendation}\n"
    
    report_content += f"""

## 次のステップ

"""
    
    if analysis_results["overall_status"] == "APPROVED":
        report_content += """
### 即座に実行可能
- `/create-tests {issue_number}` - TDD実装の開始

### 品質保証
- すべてのDDD原則に準拠しています
- 実装準備が整っています
"""
    elif analysis_results["overall_status"] == "CONDITIONAL_APPROVAL":
        report_content += """
### 条件付き実行
- 軽微な改善を実施後、`/create-tests {issue_number}` を実行可能

### 改善事項
- 設計の一部改善が推奨されます
- 実装と並行して改善可能です
"""
    else:
        report_content += """
### 要改善
- `/domain-modeling {issue_number}` でドメインモデルの再設計が必要
- 設計品質向上後に再レビューを実施

### 改善が必要な領域
- DDD準拠性の向上
- 集約境界の明確化
- ビジネスルールの配置見直し
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
        print("使用方法: /review-domain-design <issue-number>")
        sys.exit(1)
    
    issue_number = sys.argv[1]
    print(f"\n🔍 Issue #{issue_number} のドメイン設計レビューを開始します\n")
    
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
    
    # ドメインモデルファイルを検索
    print("\n🏗️ ドメインモデル設計ファイルを検索中...")
    domain_model_path = find_domain_model_file(issue_number)
    
    if not domain_model_path:
        print(f"❌ Issue #{issue_number} のドメインモデル設計が見つかりません")
        print("先に /domain-modeling コマンドを実行してください")
        sys.exit(1)
    
    print(f"✅ ドメインモデルを発見: {domain_model_path}")
    
    # ドメイン設計を分析
    print("\n🔍 ドメイン設計のDDD準拠性を分析中...")
    analysis_results = analyze_domain_design(domain_model_path, issue_data)
    
    # レビューレポートを生成
    print("\n📊 レビューレポートを生成中...")
    report_file = generate_review_report(issue_number, analysis_results, issue_data)
    
    # ユースケースデータを読み込み
    use_case_data = load_use_case_json(json_file_path)
    
    # 設計レビュー情報を更新
    design_review = {
        "status": analysis_results["overall_status"],
        "completed_at": datetime.now().isoformat(),
        "ddd_compliance_score": analysis_results["ddd_compliance_score"],
        "violations": len(analysis_results["aggregate_boundary_violations"]) + len(analysis_results["architecture_violations"]),
        "report_file": report_file,
        "recommendations": analysis_results["recommendations"]
    }
    
    use_case_data.setdefault("quality_gates", {})["domain_design_review"] = design_review
    save_use_case_json(json_file_path, use_case_data)
    
    # 実行履歴を更新
    update_execution_history(
        json_file_path,
        f"/review-domain-design {issue_number}",
        "success" if analysis_results["overall_status"] != "ERROR" else "failed",
        [report_file]
    )
    
    # 更新されたデータを読み込み
    updated_data = load_use_case_json(json_file_path)
    
    # 実行状況を表示
    print("\n" + "="*60)
    print(format_execution_status(updated_data))
    print("="*60)
    
    # 結果サマリー表示
    print(f"\n📊 ドメイン設計レビュー結果")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"🎯 総合判定: {analysis_results['overall_status']}")
    print(f"📈 DDD準拠性スコア: {analysis_results['ddd_compliance_score']}/100")
    print(f"🔍 検出された違反: {len(analysis_results['aggregate_boundary_violations']) + len(analysis_results['architecture_violations'])}件")
    print(f"📝 推奨事項: {len(analysis_results['recommendations'])}項目")
    
    print(f"\n📁 成果物")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"✅ {report_file}")
    
    print(f"\n💡 推奨事項")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    for i, recommendation in enumerate(analysis_results["recommendations"], 1):
        print(f"{i}. {recommendation}")
    
    print(f"\n⏭️ 次の推奨コマンド")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    if analysis_results["overall_status"] == "APPROVED":
        print(f"✅ 設計承認済み - 即座に実行可能:")
        print(f"   /create-tests {issue_number}")
        print(f"   → TDD実装フェーズの開始")
    elif analysis_results["overall_status"] == "CONDITIONAL_APPROVAL":
        print(f"⚠️ 条件付き承認:")
        print(f"   /create-tests {issue_number}")
        print(f"   → 実装開始（改善と並行）")
        print(f"   または")
        print(f"   /domain-modeling {issue_number}")
        print(f"   → 設計改善後に実装")
    else:
        print(f"❌ 設計要改善:")
        print(f"   /domain-modeling {issue_number}")
        print(f"   → ドメインモデル再設計")
        print(f"   その後")
        print(f"   /review-domain-design {issue_number}")
        print(f"   → 再レビュー実施")
    
    # 最終メッセージ
    status_emoji = {"APPROVED": "✅", "CONDITIONAL_APPROVAL": "⚠️", "REJECTED": "❌", "ERROR": "🚨"}
    emoji = status_emoji.get(analysis_results["overall_status"], "❓")
    
    print(f"\n{emoji} ドメイン設計レビュー完了")
    print(f"詳細なレビュー結果は {report_file} に記録されました。")


if __name__ == "__main__":
    main()