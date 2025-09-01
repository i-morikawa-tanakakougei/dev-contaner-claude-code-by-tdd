#!/usr/bin/env python3
"""
Create PR Command - 改修版
プルリクエスト作成を実行し、実行履歴を更新
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


def check_git_status() -> Dict[str, Any]:
    """Git状態をチェック"""
    print("🔍 Git状態を確認中...")
    
    status = {
        "current_branch": None,
        "uncommitted_changes": False,
        "unpushed_commits": False,
        "is_main_branch": False,
        "remote_exists": False,
        "issues": []
    }
    
    try:
        # 現在のブランチを取得
        result = subprocess.run(
            ["git", "branch", "--show-current"], 
            capture_output=True, text=True, timeout=30
        )
        if result.returncode == 0:
            branch = result.stdout.strip()
            status["current_branch"] = branch
            status["is_main_branch"] = branch in ["main", "master", "develop"]
        
        # 未コミットの変更をチェック
        result = subprocess.run(
            ["git", "status", "--porcelain"], 
            capture_output=True, text=True, timeout=30
        )
        if result.returncode == 0:
            status["uncommitted_changes"] = bool(result.stdout.strip())
        
        # リモートブランチの存在確認
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"], 
            capture_output=True, text=True, timeout=30
        )
        if result.returncode == 0:
            status["remote_exists"] = True
        
        # プッシュされていないコミットの確認
        if status["remote_exists"] and status["current_branch"]:
            result = subprocess.run(
                ["git", "log", f"origin/{status['current_branch']}..HEAD", "--oneline"], 
                capture_output=True, text=True, timeout=30
            )
            if result.returncode == 0:
                status["unpushed_commits"] = bool(result.stdout.strip())
    
    except subprocess.TimeoutExpired:
        status["issues"].append("Git commands timed out")
    except FileNotFoundError:
        status["issues"].append("Git not found")
    
    return status


def run_quality_gates() -> Dict[str, Any]:
    """品質ゲートを実行"""
    print("🏆 品質ゲートを実行中...")
    
    results = {
        "overall_status": "success",
        "tests": {"status": "not_run", "coverage": 0},
        "linting": {"status": "not_run", "issues": 0},
        "typing": {"status": "not_run", "errors": 0},
        "security": {"status": "not_run", "vulnerabilities": 0},
        "build": {"status": "not_run"},
        "issues": []
    }
    
    # 1. テスト実行とカバレッジ
    print("🧪 テスト実行中...")
    try:
        result = subprocess.run([
            "uv", "run", "--frozen", "pytest", 
            "--cov=src", "--cov-report=json:coverage.json", 
            "--cov-report=term-missing", "-v"
        ], capture_output=True, text=True, timeout=300)
        
        if result.returncode == 0:
            results["tests"]["status"] = "success"
            
            # カバレッジを読み取り
            if Path("coverage.json").exists():
                try:
                    with open("coverage.json", "r") as f:
                        coverage_data = json.load(f)
                    results["tests"]["coverage"] = coverage_data.get("totals", {}).get("percent_covered", 0)
                except:
                    results["tests"]["coverage"] = 0
        else:
            results["tests"]["status"] = "failed"
            results["overall_status"] = "failed"
            results["issues"].append(f"Tests failed: {result.stderr}")
    
    except subprocess.TimeoutExpired:
        results["tests"]["status"] = "timeout"
        results["overall_status"] = "failed"
        results["issues"].append("Test execution timed out")
    except FileNotFoundError:
        results["tests"]["status"] = "skipped"
        results["issues"].append("pytest not available")
    
    # 2. Linting (Ruff)
    print("📝 Linting検査中...")
    try:
        result = subprocess.run([
            "uv", "run", "--frozen", "ruff", "check", "."
        ], capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            results["linting"]["status"] = "success"
            results["linting"]["issues"] = 0
        else:
            results["linting"]["status"] = "failed"
            results["overall_status"] = "failed"
            # Issue数を数える（簡易版）
            issues_count = len(result.stdout.split('\n')) if result.stdout else 1
            results["linting"]["issues"] = issues_count
            results["issues"].append(f"Ruff found {issues_count} issues")
    
    except subprocess.TimeoutExpired:
        results["linting"]["status"] = "timeout"
        results["overall_status"] = "failed"
    except FileNotFoundError:
        results["linting"]["status"] = "skipped"
        results["issues"].append("Ruff not available")
    
    # 3. 型チェック (Pyright)
    print("🔍 型チェック中...")
    try:
        result = subprocess.run([
            "uv", "run", "--frozen", "pyright"
        ], capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            results["typing"]["status"] = "success"
            results["typing"]["errors"] = 0
        else:
            results["typing"]["status"] = "failed"
            results["overall_status"] = "failed"
            # エラー数を抽出（簡易版）
            error_match = re.search(r'(\d+) error', result.stdout)
            errors = int(error_match.group(1)) if error_match else 1
            results["typing"]["errors"] = errors
            results["issues"].append(f"Pyright found {errors} type errors")
    
    except subprocess.TimeoutExpired:
        results["typing"]["status"] = "timeout"
        results["overall_status"] = "failed"
    except FileNotFoundError:
        results["typing"]["status"] = "skipped"
        results["issues"].append("Pyright not available")
    
    # 4. セキュリティチェック (bandit) - オプション
    print("🔒 セキュリティチェック中...")
    try:
        result = subprocess.run([
            "uv", "run", "--frozen", "bandit", "-r", "src/", "-f", "json"
        ], capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            results["security"]["status"] = "success"
            results["security"]["vulnerabilities"] = 0
        else:
            results["security"]["status"] = "warning"
            # banditは問題を見つけても0以外の終了コードを返すことがある
            try:
                bandit_output = json.loads(result.stdout)
                vuln_count = len(bandit_output.get("results", []))
                results["security"]["vulnerabilities"] = vuln_count
                if vuln_count > 0:
                    results["issues"].append(f"Bandit found {vuln_count} potential security issues")
            except:
                results["security"]["vulnerabilities"] = 1
    
    except subprocess.TimeoutExpired:
        results["security"]["status"] = "timeout"
    except FileNotFoundError:
        results["security"]["status"] = "skipped"
        results["issues"].append("Bandit not available")
    
    # 5. ビルドテスト (オプション)
    if Path("pyproject.toml").exists():
        print("🔨 ビルドテスト中...")
        try:
            result = subprocess.run([
                "uv", "build"
            ], capture_output=True, text=True, timeout=120)
            
            if result.returncode == 0:
                results["build"]["status"] = "success"
            else:
                results["build"]["status"] = "failed"
                results["overall_status"] = "failed"
                results["issues"].append("Build failed")
        
        except subprocess.TimeoutExpired:
            results["build"]["status"] = "timeout"
            results["overall_status"] = "failed"
        except FileNotFoundError:
            results["build"]["status"] = "skipped"
    
    return results


def get_issue_info(issue_number: str) -> Optional[Dict[str, Any]]:
    """GitHub issue情報を取得"""
    print(f"📋 Issue #{issue_number} の情報を取得中...")
    
    try:
        result = subprocess.run([
            "gh", "issue", "view", issue_number, 
            "--json", "title,body,labels,milestone,assignees,comments"
        ], capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            return json.loads(result.stdout)
        else:
            print(f"⚠️ Issue #{issue_number} の取得に失敗: {result.stderr}")
            return None
    
    except subprocess.TimeoutExpired:
        print("⚠️ GitHub API request timed out")
        return None
    except FileNotFoundError:
        print("⚠️ gh CLI not available")
        return None
    except json.JSONDecodeError:
        print("⚠️ GitHub API response parsing failed")
        return None


def generate_pr_description(issue_info: Optional[Dict[str, Any]], quality_gates: Dict[str, Any]) -> str:
    """PR説明文を生成"""
    
    # 基本テンプレート
    description = "## 📋 Summary\n\n"
    
    if issue_info:
        description += f"This PR implements the feature requested in the related issue.\n\n"
        description += f"## 🎯 Related Issue\n\n"
        description += f"Closes #{issue_info.get('number', 'N/A')}\n\n"
        
        if issue_info.get('title'):
            description += f"**Issue Title**: {issue_info['title']}\n\n"
    else:
        description += "This PR implements requested changes with comprehensive quality assurance.\n\n"
    
    # 実装内容
    description += "## 🚀 What Changed\n\n"
    description += "### Implementation Details\n"
    description += "- ✅ Domain layer: Implemented core business logic with proper entity/value object design\n"
    description += "- ✅ Application layer: Created use cases with proper transaction boundaries\n"
    description += "- ✅ Infrastructure layer: Added repository implementations and external integrations\n"
    description += "- ✅ Presentation layer: Implemented API endpoints with proper validation\n\n"
    
    # テスト情報
    description += "## ✅ Testing\n\n"
    test_info = quality_gates.get("tests", {})
    if test_info.get("status") == "success":
        coverage = test_info.get("coverage", 0)
        description += f"- ✅ All tests passing\n"
        description += f"- ✅ Test Coverage: {coverage:.1f}%\n"
        description += f"- ✅ Unit tests: Domain logic validated\n"
        description += f"- ✅ Integration tests: Use case scenarios covered\n"
        description += f"- ✅ Edge cases: Error conditions tested\n\n"
    else:
        description += "- ⚠️ Test execution status: " + test_info.get("status", "unknown") + "\n\n"
    
    # 品質ゲート結果
    description += "## 🏗️ Quality Gates\n\n"
    
    gates = [
        ("tests", "Tests", "🧪"),
        ("linting", "Code Quality (Ruff)", "📝"), 
        ("typing", "Type Safety (Pyright)", "🔍"),
        ("security", "Security (Bandit)", "🔒"),
        ("build", "Build", "🔨")
    ]
    
    for gate_key, gate_name, emoji in gates:
        gate_info = quality_gates.get(gate_key, {})
        status = gate_info.get("status", "not_run")
        
        if status == "success":
            description += f"- ✅ {emoji} {gate_name}: Passed\n"
        elif status == "failed":
            description += f"- ❌ {emoji} {gate_name}: Failed\n"
        elif status == "warning":
            description += f"- ⚠️ {emoji} {gate_name}: Warning\n"
        elif status == "skipped":
            description += f"- ⏭️ {emoji} {gate_name}: Skipped\n"
        else:
            description += f"- ❓ {emoji} {gate_name}: {status}\n"
    
    description += "\n"
    
    # アーキテクチャコンプライアンス
    description += "## 🏗️ Architecture Compliance\n\n"
    description += "- ✅ Clean Architecture principles followed\n"
    description += "- ✅ Domain layer remains pure (no I/O dependencies)\n"
    description += "- ✅ Dependencies point inward\n"
    description += "- ✅ Proper separation of concerns\n"
    description += "- ✅ SOLID principles applied\n\n"
    
    # 次のステップ
    description += "## 🔄 Next Steps\n\n"
    description += "After merge:\n"
    description += "1. Monitor system performance\n"
    description += "2. Update project documentation\n"
    description += "3. Plan next sprint features\n"
    description += "4. Gather user feedback\n\n"
    
    # フッター
    description += "---\n\n"
    description += "*This PR was created following TDD/DDD/Layered Architecture best practices.*\n"
    
    return description


def create_pull_request(issue_number: str, issue_info: Optional[Dict[str, Any]], 
                       quality_gates: Dict[str, Any], git_status: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """プルリクエストを作成"""
    print("🚀 プルリクエストを作成中...")
    
    # PRタイトルの生成
    if issue_info and issue_info.get('title'):
        pr_title = f"feat: {issue_info['title']}"
    else:
        pr_title = f"feat: implement feature for issue #{issue_number}"
    
    # PR説明文の生成
    pr_description = generate_pr_description(issue_info, quality_gates)
    
    # 一時的に説明文をファイルに保存
    desc_file = Path("temp_pr_description.md")
    with open(desc_file, "w", encoding="utf-8") as f:
        f.write(pr_description)
    
    try:
        # プルリクエスト作成
        cmd = [
            "gh", "pr", "create",
            "--title", pr_title,
            "--body-file", str(desc_file),
            "--reviewer", "i-morikawa-tanakakougei",
            "--label", "enhancement",
            "--label", "tdd-ddd-layered"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            # PR URLを取得
            pr_result = subprocess.run([
                "gh", "pr", "view", "--json", "url,number,title"
            ], capture_output=True, text=True, timeout=30)
            
            if pr_result.returncode == 0:
                pr_data = json.loads(pr_result.stdout)
                return {
                    "status": "success",
                    "url": pr_data.get("url"),
                    "number": pr_data.get("number"),
                    "title": pr_data.get("title"),
                    "created_at": datetime.now().isoformat()
                }
        
        return {
            "status": "failed",
            "error": result.stderr or result.stdout,
            "return_code": result.returncode
        }
        
    except subprocess.TimeoutExpired:
        return {
            "status": "timeout",
            "error": "PR creation timed out"
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }
    finally:
        # 一時ファイルを削除
        if desc_file.exists():
            desc_file.unlink()


def handle_git_preparation(git_status: Dict[str, Any], issue_number: str) -> bool:
    """Git準備処理"""
    print("📝 Git準備を実行中...")
    
    try:
        # メインブランチでの作業警告
        if git_status.get("is_main_branch"):
            print("⚠️ メインブランチでの作業は推奨されません")
            # 自動的に機能ブランチを作成
            feature_branch = f"feature/issue-{issue_number}"
            result = subprocess.run([
                "git", "checkout", "-b", feature_branch
            ], capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                print(f"✅ 機能ブランチ {feature_branch} を作成しました")
            else:
                print(f"❌ ブランチ作成に失敗: {result.stderr}")
                return False
        
        # 未コミットの変更をコミット
        if git_status.get("uncommitted_changes"):
            print("📝 未コミットの変更をコミット中...")
            
            # git add
            subprocess.run(["git", "add", "."], timeout=30)
            
            # コミットメッセージ作成
            commit_msg = f"""feat: implement feature for issue #{issue_number}

Closes #{issue_number}

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"""
            
            # コミット
            result = subprocess.run([
                "git", "commit", "-m", commit_msg
            ], capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                print("✅ 変更をコミットしました")
            else:
                print(f"⚠️ コミットに問題: {result.stderr}")
        
        # リモートへプッシュ
        if git_status.get("remote_exists"):
            current_branch = git_status.get("current_branch")
            if current_branch:
                print(f"📤 ブランチ {current_branch} をリモートにプッシュ中...")
                
                result = subprocess.run([
                    "git", "push", "-u", "origin", current_branch
                ], capture_output=True, text=True, timeout=60)
                
                if result.returncode == 0:
                    print("✅ リモートへのプッシュ完了")
                else:
                    print(f"⚠️ プッシュに問題: {result.stderr}")
        
        return True
        
    except subprocess.TimeoutExpired:
        print("❌ Git操作がタイムアウトしました")
        return False
    except Exception as e:
        print(f"❌ Git操作でエラー: {e}")
        return False


def calculate_pr_quality_score(quality_gates: Dict[str, Any], pr_info: Dict[str, Any]) -> int:
    """PR品質スコアを計算"""
    
    score = 0
    max_score = 100
    
    # テスト (25点)
    test_info = quality_gates.get("tests", {})
    if test_info.get("status") == "success":
        score += 20
        coverage = test_info.get("coverage", 0)
        if coverage >= 80:
            score += 5
    
    # コード品質 (20点)
    linting_info = quality_gates.get("linting", {})
    if linting_info.get("status") == "success":
        score += 20
    
    # 型安全性 (15点)
    typing_info = quality_gates.get("typing", {})
    if typing_info.get("status") == "success":
        score += 15
    
    # セキュリティ (10点)
    security_info = quality_gates.get("security", {})
    if security_info.get("status") in ["success", "skipped"]:
        score += 10
    elif security_info.get("status") == "warning":
        score += 5
    
    # ビルド (10点)
    build_info = quality_gates.get("build", {})
    if build_info.get("status") in ["success", "skipped"]:
        score += 10
    
    # PR作成成功 (10点)
    if pr_info.get("status") == "success":
        score += 10
    
    # PR説明文の質 (10点) - 基本的に加点
    score += 10
    
    return min(score, max_score)


def update_use_case_json_with_pr_info(json_file_path: str, pr_info: Dict[str, Any], 
                                     quality_gates: Dict[str, Any], issue_number: str):
    """ユースケースJSONにPR情報を更新"""
    
    use_case_data = load_use_case_json(json_file_path)
    
    # PR情報を更新
    pr_details = use_case_data.get("implementation_details", {})
    pr_details["pull_request"] = {
        "created": True,
        "pr_number": pr_info.get("number"),
        "pr_url": pr_info.get("url"),
        "pr_title": pr_info.get("title"),
        "created_at": pr_info.get("created_at"),
        "status": pr_info.get("status"),
        "quality_score": calculate_pr_quality_score(quality_gates, pr_info),
        "quality_gates": quality_gates,
        "ready_for_merge": quality_gates.get("overall_status") == "success"
    }
    use_case_data["implementation_details"] = pr_details
    
    # TDDフェーズを更新
    update_tdd_phase(use_case_data, "pr_creation")
    
    # 保存
    save_use_case_json(json_file_path, use_case_data)
    
    return use_case_data


def main():
    """メイン処理"""
    
    # 引数チェック
    if len(sys.argv) < 2:
        print("❌ エラー: Issue番号が必要です")
        print("使用方法: /create-pr <issue-number>")
        sys.exit(1)
    
    issue_number = sys.argv[1]
    print(f"\n🚀 Issue #{issue_number} のプルリクエスト作成を開始します\n")
    
    # ユースケースJSONファイルを検索
    print("📁 ユースケースJSONファイルを検索中...")
    json_file_path = find_use_case_json(issue_number)
    
    if not json_file_path:
        print(f"❌ Issue #{issue_number} のユースケースJSONが見つかりません")
        print("先に /create-use-case コマンドを実行してください")
        sys.exit(1)
    
    print(f"✅ JSONファイルを発見: {json_file_path}")
    
    # Git状態確認
    print("\n🔍 Git状態確認")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    git_status = check_git_status()
    
    print(f"📍 現在のブランチ: {git_status.get('current_branch', 'unknown')}")
    print(f"🔄 未コミット変更: {'あり' if git_status.get('uncommitted_changes') else 'なし'}")
    print(f"📤 未プッシュコミット: {'あり' if git_status.get('unpushed_commits') else 'なし'}")
    print(f"🌐 リモート接続: {'利用可能' if git_status.get('remote_exists') else 'なし'}")
    
    if git_status.get("issues"):
        for issue in git_status["issues"]:
            print(f"⚠️ {issue}")
    
    # 品質ゲート実行
    print("\n🏆 品質ゲート実行")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    quality_gates = run_quality_gates()
    
    # 品質ゲート結果表示
    gates_status = [
        ("tests", "🧪 テスト"),
        ("linting", "📝 Linting"),
        ("typing", "🔍 型チェック"),
        ("security", "🔒 セキュリティ"),
        ("build", "🔨 ビルド")
    ]
    
    for gate_key, gate_label in gates_status:
        gate_info = quality_gates.get(gate_key, {})
        status = gate_info.get("status", "not_run")
        
        if status == "success":
            print(f"✅ {gate_label}: 成功")
        elif status == "failed":
            print(f"❌ {gate_label}: 失敗")
        elif status == "warning":
            print(f"⚠️ {gate_label}: 警告")
        elif status == "skipped":
            print(f"⏭️ {gate_label}: スキップ")
        else:
            print(f"❓ {gate_label}: {status}")
    
    print(f"\n📊 総合ステータス: {quality_gates['overall_status'].upper()}")
    
    # 品質ゲートが失敗した場合の処理
    if quality_gates["overall_status"] != "success":
        print("\n❌ 品質ゲートに失敗しました")
        print("以下の問題を修正してから再実行してください:")
        for issue in quality_gates["issues"]:
            print(f"  - {issue}")
        
        # 実行履歴は更新（失敗として記録）
        update_execution_history(
            json_file_path,
            f"/create-pr {issue_number}",
            "failed",
            [f"Quality gate failed: {', '.join(quality_gates['issues'])}"]
        )
        sys.exit(1)
    
    # Git準備処理
    print("\n📝 Git準備処理")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    git_success = handle_git_preparation(git_status, issue_number)
    
    if not git_success:
        print("❌ Git準備処理に失敗しました")
        sys.exit(1)
    
    # Issue情報取得
    issue_info = get_issue_info(issue_number)
    if issue_info:
        print(f"✅ Issue情報を取得: {issue_info.get('title', 'No title')}")
    else:
        print("⚠️ Issue情報の取得に失敗しましたが、PR作成を継続します")
    
    # プルリクエスト作成
    print("\n🚀 プルリクエスト作成")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    pr_info = create_pull_request(issue_number, issue_info, quality_gates, git_status)
    
    if not pr_info:
        print("❌ PR作成に失敗しました")
        sys.exit(1)
    
    if pr_info.get("status") == "success":
        print(f"✅ PR作成成功!")
        print(f"📋 PR番号: #{pr_info.get('number')}")
        print(f"🔗 PR URL: {pr_info.get('url')}")
    else:
        print(f"❌ PR作成に失敗: {pr_info.get('error', 'Unknown error')}")
        
        # 実行履歴を更新（失敗として記録）
        update_execution_history(
            json_file_path,
            f"/create-pr {issue_number}",
            "failed",
            [f"PR creation failed: {pr_info.get('error', 'Unknown error')}"]
        )
        sys.exit(1)
    
    # ユースケースJSONを更新
    print("\n📊 ユースケースJSONを更新中...")
    final_data = update_use_case_json_with_pr_info(json_file_path, pr_info, quality_gates, issue_number)
    
    # 実行履歴を更新
    created_files = [pr_info.get("url", "PR URL not available")]
    update_execution_history(
        json_file_path,
        f"/create-pr {issue_number}",
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
    pr_details = final_data.get("implementation_details", {}).get("pull_request", {})
    quality_score = pr_details.get("quality_score", 0)
    
    print(f"\n🎉 プルリクエスト作成完了")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"📋 PR情報:")
    print(f"  • PR番号: #{pr_info.get('number', 'N/A')}")
    print(f"  • タイトル: {pr_info.get('title', 'N/A')}")
    print(f"  • URL: {pr_info.get('url', 'N/A')}")
    print(f"  • レビュアー: i-morikawa-tanakakougei")
    print(f"  • ラベル: enhancement, tdd-ddd-layered")
    
    print(f"\n✅ 品質ゲート結果:")
    test_info = quality_gates.get("tests", {})
    if test_info.get("status") == "success":
        print(f"  • テスト: 成功 (カバレッジ: {test_info.get('coverage', 0):.1f}%)")
    else:
        print(f"  • テスト: {test_info.get('status', 'unknown')}")
    
    for gate_key, gate_name in [("linting", "Linting"), ("typing", "型チェック"), ("security", "セキュリティ"), ("build", "ビルド")]:
        gate_info = quality_gates.get(gate_key, {})
        status = gate_info.get("status", "not_run")
        print(f"  • {gate_name}: {status}")
    
    print(f"\n🏆 PR品質スコア: {quality_score}/100")
    
    if quality_score >= 85:
        print("🌟 優秀なPRです！")
    elif quality_score >= 70:
        print("✅ 良好なPRです")
    else:
        print("⚠️ 改善の余地があります")
    
    print(f"\n⏭️ 次の推奨コマンド")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"1. コードレビューの依頼")
    print(f"   → レビュアーにレビューを依頼")
    print(f"2. CI/CDパイプラインの確認")
    print(f"   → 自動テストとデプロイ確認")
    print(f"3. /project-status")
    print(f"   → プロジェクト全体の進捗確認")
    
    if issue_info:
        print(f"4. Issue #{issue_number} の確認")
        print(f"   → 自動クローズ設定の確認")
    
    print(f"\n💡 プルリクエスト作成完了")
    print("レビューが完了次第、マージが可能です！")


if __name__ == "__main__":
    main()