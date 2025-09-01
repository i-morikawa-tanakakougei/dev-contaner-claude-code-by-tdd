#!/usr/bin/env python3
"""
Refactor Command - 改修版
TDD REFACTOR Phaseでコードを改善し、実行履歴を更新
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
    update_tdd_phase,
    save_use_case_json,
    format_execution_status
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


def run_code_formatting():
    """コードフォーマットを実行"""
    print("🎨 コードフォーマットを実行中...")
    
    try:
        # Ruffでフォーマット
        result = subprocess.run(
            ["uv", "run", "--frozen", "ruff", "format", "."],
            capture_output=True,
            text=True,
            check=False
        )
        
        if result.returncode == 0:
            print("✅ Ruff format完了")
        else:
            print(f"⚠️ Ruff format警告: {result.stderr}")
        
        # Ruffでリント
        result = subprocess.run(
            ["uv", "run", "--frozen", "ruff", "check", ".", "--fix"],
            capture_output=True,
            text=True,
            check=False
        )
        
        if result.returncode == 0:
            print("✅ Ruff check完了")
        else:
            print(f"⚠️ Ruff check警告: {result.stderr}")
            
        return True
        
    except FileNotFoundError:
        print("⚠️ Ruffが見つかりません。手動でコードフォーマットを実行してください")
        return False


def run_type_checking():
    """型チェックを実行"""
    print("🔍 型チェックを実行中...")
    
    try:
        result = subprocess.run(
            ["uv", "run", "--frozen", "pyright"],
            capture_output=True,
            text=True,
            check=False
        )
        
        if result.returncode == 0:
            print("✅ 型チェック完了")
            return True
        else:
            print(f"⚠️ 型チェック警告: {result.stderr}")
            return False
            
    except FileNotFoundError:
        print("⚠️ Pyrightが見つかりません。手動で型チェックを実行してください")
        return False


def run_tests(issue_number):
    """関連テストを実行"""
    print("🧪 テストを実行中...")
    
    test_path = f"tests/test_issue_{issue_number}/"
    if not Path(test_path).exists():
        print("⚠️ テストファイルが見つかりません")
        return False
    
    try:
        result = subprocess.run(
            ["uv", "run", "--frozen", "pytest", test_path, "-v"],
            capture_output=True,
            text=True,
            check=False
        )
        
        if result.returncode == 0:
            print("✅ すべてのテストが成功")
            return True
        else:
            print(f"❌ テスト失敗: {result.stdout}")
            print(f"エラー詳細: {result.stderr}")
            return False
            
    except FileNotFoundError:
        print("⚠️ Pytestが見つかりません")
        return False


def identify_refactor_opportunities(use_case_data):
    """リファクタリング機会を特定"""
    opportunities = []
    
    # 実行履歴から作成されたファイルを分析
    execution_history = use_case_data.get("execution_history", {})
    commands = execution_history.get("commands_executed", [])
    
    created_files = []
    for cmd in commands:
        files = cmd.get("files_affected", [])
        created_files.extend(files)
    
    # 各ファイルのリファクタリング機会を確認
    for file_path in set(created_files):
        if Path(file_path).exists():
            opportunities.append({
                "file": file_path,
                "suggestions": [
                    "重複コードの除去",
                    "メソッドの分割",
                    "変数名の改善",
                    "型ヒントの追加",
                    "ドキュメント文字列の改善"
                ]
            })
    
    return opportunities


def generate_refactor_suggestions(use_case_data):
    """リファクタリング提案を生成"""
    domain_model = use_case_data.get("domain_model", {})
    
    suggestions = [
        "## 🔧 リファクタリング提案\n"
    ]
    
    # エンティティの改善提案
    entities = domain_model.get("entities", [])
    if entities:
        suggestions.append("### エンティティの改善")
        for entity in entities:
            entity_name = entity.get("name", "")
            suggestions.append(f"- **{entity_name}**: ")
            suggestions.append("  - バリデーションロジックの強化")
            suggestions.append("  - 不変性の確保")
            suggestions.append("  - ファクトリーメソッドの追加")
    
    # 値オブジェクトの改善提案
    value_objects = domain_model.get("value_objects", [])
    if value_objects:
        suggestions.append("\n### 値オブジェクトの改善")
        for vo in value_objects:
            vo_name = vo.get("name", "")
            suggestions.append(f"- **{vo_name}**: ")
            suggestions.append("  - より厳密な検証ルールの実装")
            suggestions.append("  - ファクトリーメソッドの追加")
    
    # 一般的な改善提案
    suggestions.extend([
        "\n### 一般的な改善",
        "- **コードの重複除去**: 共通処理の抽出",
        "- **エラーハンドリング**: 例外処理の統一",
        "- **ログ出力**: 適切なログレベルの設定",
        "- **パフォーマンス**: 計算量の最適化",
        "- **テストカバレッジ**: 追加テストケースの作成"
    ])
    
    return "\n".join(suggestions)


def create_refactor_report(issue_number, opportunities, test_success, format_success, type_check_success):
    """リファクタリングレポートを作成"""
    report_dir = Path("docs/refactor_reports")
    report_dir.mkdir(exist_ok=True)
    
    report_content = f"""# リファクタリングレポート - Issue #{issue_number}

## 実行日時
{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 品質チェック結果

| チェック項目 | 結果 | 詳細 |
|------------|------|------|
| コードフォーマット | {'✅ 成功' if format_success else '❌ 失敗'} | Ruff format + check |
| 型チェック | {'✅ 成功' if type_check_success else '❌ 失敗'} | Pyright |
| テスト実行 | {'✅ 成功' if test_success else '❌ 失敗'} | Pytest |

## 総合判定
{'✅ リファクタリング成功' if all([test_success, format_success, type_check_success]) else '⚠️ 改善が必要'}

## リファクタリング機会

"""
    
    for opportunity in opportunities:
        report_content += f"### {opportunity['file']}\n"
        for suggestion in opportunity['suggestions']:
            report_content += f"- {suggestion}\n"
        report_content += "\n"
    
    report_content += f"""
## 推奨事項

### 次のステップ
1. 失敗した品質チェックの修正
2. 重複コードの除去
3. パフォーマンスの最適化
4. テストカバレッジの向上

### 継続的改善
- 定期的なリファクタリングの実施
- コードレビューの強化
- 自動化ツールの活用

---
Generated by /refactor command
"""
    
    report_file = report_dir / f"issue-{issue_number}-refactor-report.md"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    return str(report_file)


def main():
    """メイン処理"""
    
    # 引数チェック
    if len(sys.argv) < 2:
        print("❌ エラー: Issue番号が必要です")
        print("使用方法: /refactor <issue-number>")
        sys.exit(1)
    
    issue_number = sys.argv[1]
    print(f"\n🔧 Issue #{issue_number} のリファクタリング（REFACTOR Phase）を開始します\n")
    
    # ユースケースJSONファイルを検索
    print("📁 ユースケースJSONファイルを検索中...")
    json_file_path = find_use_case_json(issue_number)
    
    if not json_file_path:
        print(f"❌ Issue #{issue_number} のユースケースJSONが見つかりません")
        print("先に /create-use-case コマンドを実行してください")
        sys.exit(1)
    
    print(f"✅ JSONファイルを発見: {json_file_path}")
    
    # ユースケースデータを読み込み
    print("📝 ユースケースデータを読み込み中...")
    use_case_data = load_use_case_json(json_file_path)
    
    # GREEN Phaseの完了確認
    tdd_phases = use_case_data.get("execution_history", {}).get("tdd_phases", {})
    if tdd_phases.get("GREEN", {}).get("status") != "completed":
        print("⚠️ 警告: GREEN Phase（実装）が完了していません")
        print("先に実装コマンドを実行してください")
    
    # リファクタリング機会を特定
    print("🔍 リファクタリング機会を分析中...")
    opportunities = identify_refactor_opportunities(use_case_data)
    
    # 品質チェックを実行
    print("\n📊 品質チェックを実行中...")
    format_success = run_code_formatting()
    type_check_success = run_type_checking()
    test_success = run_tests(issue_number)
    
    # リファクタリング提案を生成
    suggestions = generate_refactor_suggestions(use_case_data)
    print(f"\n{suggestions}")
    
    # レポートを作成
    print("\n📋 リファクタリングレポートを作成中...")
    report_file = create_refactor_report(
        issue_number, 
        opportunities, 
        test_success, 
        format_success, 
        type_check_success
    )
    
    # TDDフェーズを更新
    print("📊 TDDフェーズを更新中...")
    refactor_status = "completed" if all([test_success, format_success, type_check_success]) else "in_progress"
    
    update_tdd_phase(
        json_file_path,
        "REFACTOR",
        refactor_status,
        f"/refactor {issue_number}",
        files_modified=[report_file]
    )
    
    # 実行履歴を更新
    execution_status = "success" if refactor_status == "completed" else "partial"
    update_execution_history(
        json_file_path,
        f"/refactor {issue_number}",
        execution_status,
        [report_file]
    )
    
    # 更新されたデータを読み込み
    updated_data = load_use_case_json(json_file_path)
    
    # 実行状況を表示
    print("\n" + "="*60)
    print(format_execution_status(updated_data))
    print("="*60)
    
    # サマリー表示
    total_checks = 3
    successful_checks = sum([test_success, format_success, type_check_success])
    
    print(f"\n📊 実行サマリー")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"🔧 TDD REFACTOR Phase: {'✅ 完了' if refactor_status == 'completed' else '🔄 進行中'}")
    print(f"✅ 品質チェック: {successful_checks}/{total_checks}個成功")
    print(f"  - コードフォーマット: {'✅' if format_success else '❌'}")
    print(f"  - 型チェック: {'✅' if type_check_success else '❌'}")
    print(f"  - テスト実行: {'✅' if test_success else '❌'}")
    print(f"✅ リファクタリング機会: {len(opportunities)}件特定")
    
    print(f"\n📁 成果物")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"✅ {report_file}")
    print(f"✅ {json_file_path} (実行履歴更新)")
    
    print(f"\n⏭️ 次の推奨コマンド")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    if refactor_status == "completed":
        print(f"1. /run-all-tests {issue_number} - 全体テストの実行")
        print(f"2. /create-pr {issue_number} - プルリクエストの作成")
        print(f"3. /use-case-status {issue_number} - 進捗状況の確認")
    else:
        print(f"1. 品質チェック失敗項目の修正")
        print(f"2. /refactor {issue_number} - 再実行")
    
    status_icon = "🎉" if refactor_status == "completed" else "⚠️"
    status_msg = "リファクタリング完了！TDD サイクルが完了しました。" if refactor_status == "completed" else "品質チェックに失敗した項目があります。修正後に再実行してください。"
    print(f"\n{status_icon} {status_msg}")


if __name__ == "__main__":
    main()