#!/usr/bin/env python3
"""
Create Use Case Command - 改修版
GitHub IssueからユースケースJSONを新フォーマットで作成し、実行履歴を追跡
"""

import json
import os
import sys
import subprocess
from datetime import datetime
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))
from utils.json_format_utils import (
    update_execution_history,
    save_use_case_json,
    format_execution_status
)


def get_git_branch():
    """現在のGitブランチを取得"""
    try:
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None


def create_feature_branch(issue_number, issue_title=None):
    """フィーチャーブランチを作成"""
    current_branch = get_git_branch()
    
    if current_branch in ["main", "master"]:
        if issue_title:
            # タイトルをブランチ名用にフォーマット
            feature_name = issue_title.lower()
            feature_name = ''.join(c if c.isalnum() else '-' for c in feature_name)
            feature_name = '-'.join(filter(None, feature_name.split('-')))
        else:
            feature_name = "feature"
        
        branch_name = f"feature/issue-{issue_number}-{feature_name}"
        
        try:
            subprocess.run(
                ["git", "checkout", "-b", branch_name],
                check=True
            )
            print(f"✅ フィーチャーブランチを作成しました: {branch_name}")
            return branch_name
        except subprocess.CalledProcessError as e:
            print(f"❌ ブランチ作成エラー: {e}")
            return None
    else:
        print(f"既存のフィーチャーブランチを使用: {current_branch}")
        return current_branch


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


def analyze_issue_comments(issue_data):
    """コメントを分析して最新の仕様を抽出"""
    comments = issue_data.get("comments", [])
    
    if comments:
        # 新しい順にソート
        sorted_comments = sorted(
            comments, 
            key=lambda x: x.get("createdAt", ""), 
            reverse=True
        )
        
        print(f"📝 {len(comments)}件のコメントを分析中...")
        
        # 最新5件のコメントを重点的に分析
        recent_comments = sorted_comments[:5]
        
        for i, comment in enumerate(recent_comments):
            author = comment.get("author", {}).get("login", "Unknown")
            created_at = comment.get("createdAt", "")
            body_preview = comment.get("body", "")[:100]
            print(f"  [{i+1}] {author} ({created_at}): {body_preview}...")
        
        return recent_comments
    
    return []


def create_use_case_json(issue_number, issue_data):
    """新フォーマットでユースケースJSONを作成"""
    
    # 基本メタデータ
    metadata = {
        "issue_id": issue_number,
        "title": issue_data.get("title", ""),
        "description": issue_data.get("body", ""),
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
        "status": "draft",
        "github_url": issue_data.get("url", ""),
        "labels": [label.get("name", "") for label in issue_data.get("labels", [])],
        "assignees": [assignee.get("login", "") for assignee in issue_data.get("assignees", [])]
    }
    
    # シナリオの初期構造
    scenarios = {
        "main_scenarios": [],
        "alternative_scenarios": [],
        "exception_scenarios": []
    }
    
    # 受入基準の初期構造
    acceptance_criteria = []
    
    # ドメインモデルの初期構造
    domain_model = {
        "entities": [],
        "value_objects": [],
        "domain_services": [],
        "business_rules": [],
        "ubiquitous_language": {}
    }
    
    # 実行履歴の初期化
    execution_history = {
        "tdd_phases": {
            "RED": {"status": "not_started"},
            "GREEN": {"status": "not_started"},
            "REFACTOR": {"status": "not_started"}
        },
        "commands_executed": [{
            "command": f"/create-use-case {issue_number}",
            "executed_at": datetime.now().isoformat(),
            "status": "success",
            "files_affected": [f"docs/use_cases/issue-{issue_number}-*.json"]
        }],
        "last_command": f"/create-use-case {issue_number}"
    }
    
    # アーキテクチャ整合性
    architecture_alignment = {
        "layers": {
            "domain": False,
            "application": False,
            "infrastructure": False,
            "presentation": False
        },
        "patterns_used": []
    }
    
    # 依存関係
    dependencies = {
        "technical": [],
        "functional": []
    }
    
    # テスト戦略
    testing_strategy = {
        "unit_tests": {
            "total": 0,
            "passed": 0,
            "failed": 0,
            "coverage": 0.0
        },
        "integration_tests": {
            "total": 0,
            "passed": 0,
            "failed": 0
        }
    }
    
    # ドキュメント参照
    documentation = {
        "vision_doc": None,
        "domain_doc": None,
        "api_doc": None,
        "test_plan": None
    }
    
    # レビュー履歴
    review_history = []
    
    # 完全なユースケース構造
    use_case = {
        "metadata": metadata,
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
    
    return use_case


def main():
    """メイン処理"""
    
    # 引数チェック
    if len(sys.argv) < 2:
        print("❌ エラー: Issue番号が必要です")
        print("使用方法: /create-use-case <issue-number>")
        sys.exit(1)
    
    issue_number = sys.argv[1]
    print(f"\n🚀 Issue #{issue_number} のユースケース仕様を作成します\n")
    
    # GitHub Issueを取得
    print("📥 GitHub Issueを取得中...")
    issue_data = get_github_issue(issue_number)
    
    if not issue_data:
        print("❌ Issueの取得に失敗しました")
        sys.exit(1)
    
    # フィーチャーブランチを作成/確認
    issue_title = issue_data.get("title", "")
    create_feature_branch(issue_number, issue_title)
    
    # コメント分析
    recent_comments = analyze_issue_comments(issue_data)
    
    # ユースケースJSONを作成
    print("\n📝 ユースケースJSONを作成中...")
    use_case = create_use_case_json(issue_number, issue_data)
    
    # ファイル名を決定（タイトルから生成）
    feature_name = issue_title.lower()
    feature_name = ''.join(c if c.isalnum() else '-' for c in feature_name)
    feature_name = '-'.join(filter(None, feature_name.split('-')))
    
    # 保存先ディレクトリを作成
    os.makedirs("docs/use_cases", exist_ok=True)
    
    # JSONファイルを保存
    json_filename = f"docs/use_cases/issue-{issue_number}-{feature_name}.json"
    save_use_case_json(json_filename, use_case)
    
    print(f"✅ ユースケースJSONを作成しました: {json_filename}")
    
    # 実行状況を表示
    print("\n" + "="*60)
    print(format_execution_status(use_case))
    print("="*60)
    
    # サマリー表示
    print(f"\n📊 実行サマリー")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"✅ Issue分析: Issue #{issue_number} - {issue_title}")
    print(f"✅ コメント数: {len(issue_data.get('comments', []))}件")
    print(f"✅ ラベル: {', '.join(use_case['metadata']['labels']) or 'なし'}")
    print(f"✅ 担当者: {', '.join(use_case['metadata']['assignees']) or '未割当'}")
    
    print(f"\n📁 成果物")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"✅ {json_filename}")
    
    print(f"\n⏭️ 次の推奨コマンド")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"1. /domain-modeling {issue_number} - ドメインモデルの設計")
    print(f"2. /evolve-scenarios {issue_number} - シナリオの詳細化")
    
    print(f"\n💡 ヒント: JSONファイルを編集してシナリオやドメイン概念を追加してください")


if __name__ == "__main__":
    main()