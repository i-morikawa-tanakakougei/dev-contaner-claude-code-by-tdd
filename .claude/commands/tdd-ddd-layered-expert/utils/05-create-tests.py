#!/usr/bin/env python3
"""
Create Tests Command - 改修版
ユースケースJSONからTDD RED Phase用のテストを作成し、実行履歴を更新
"""

import json
import os
import sys
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


def generate_test_content(use_case_data):
    """ユースケースデータからテストコードを生成"""
    
    metadata = use_case_data.get("metadata", {})
    scenarios = use_case_data.get("scenarios", {})
    domain_model = use_case_data.get("domain_model", {})
    
    test_content = f'''"""
Test for Issue #{metadata.get("issue_id", "")}: {metadata.get("title", "")}
Generated from use case scenarios - TDD RED Phase
"""

import pytest
from datetime import datetime
from typing import Optional, List


class TestUseCaseScenarios:
    """
    ユースケースシナリオのテストクラス
    
    このテストは TDD RED Phase として作成されており、
    初期状態では全て失敗する（未実装のため）
    """
    
    def setup_method(self):
        """各テストメソッド実行前の準備"""
        # テストデータの準備
        self.test_data = {{
            "timestamp": datetime.now(),
            "issue_id": {metadata.get("issue_id", "")},
            "title": "{metadata.get("title", "")}"
        }}
    
'''
    
    # メインシナリオのテスト
    main_scenarios = scenarios.get("main_scenarios", [])
    for i, scenario in enumerate(main_scenarios, 1):
        test_content += f'''
    def test_main_scenario_{i}_{scenario.get("id", f"scenario_{i}").replace("-", "_")}(self):
        """
        メインシナリオ {i}: {scenario.get("title", scenario.get("id", f"Scenario {i}"))}
        
        Given: {scenario.get("given", "前提条件")}
        When:  {scenario.get("when", "実行条件")}
        Then:  {scenario.get("then", "期待結果")}
        """
        # Given: {scenario.get("given", "前提条件")}
        # TODO: 前提条件の準備を実装
        
        # When: {scenario.get("when", "実行条件")}
        # TODO: 実行処理を実装
        
        # Then: {scenario.get("then", "期待結果")}
        # TODO: 結果検証を実装
        
        # 現在は未実装のため、意図的にテストを失敗させる
        pytest.fail("TODO: このテストは未実装です (TDD RED Phase)")
'''
    
    # 代替シナリオのテスト
    alt_scenarios = scenarios.get("alternative_scenarios", [])
    for i, scenario in enumerate(alt_scenarios, 1):
        test_content += f'''
    def test_alternative_scenario_{i}_{scenario.get("id", f"alt_{i}").replace("-", "_")}(self):
        """
        代替シナリオ {i}: {scenario.get("title", scenario.get("id", f"Alternative {i}"))}
        
        Given: {scenario.get("given", "代替前提条件")}
        When:  {scenario.get("when", "代替実行条件")}
        Then:  {scenario.get("then", "代替期待結果")}
        """
        # Given: {scenario.get("given", "代替前提条件")}
        # TODO: 代替前提条件の準備を実装
        
        # When: {scenario.get("when", "代替実行条件")}
        # TODO: 代替実行処理を実装
        
        # Then: {scenario.get("then", "代替期待結果")}
        # TODO: 代替結果検証を実装
        
        pytest.fail("TODO: このテストは未実装です (TDD RED Phase)")
'''
    
    # 例外シナリオのテスト
    exc_scenarios = scenarios.get("exception_scenarios", [])
    for i, scenario in enumerate(exc_scenarios, 1):
        test_content += f'''
    def test_exception_scenario_{i}_{scenario.get("id", f"exc_{i}").replace("-", "_")}(self):
        """
        例外シナリオ {i}: {scenario.get("title", scenario.get("id", f"Exception {i}"))}
        
        Given: {scenario.get("given", "例外前提条件")}
        When:  {scenario.get("when", "例外発生条件")}
        Then:  {scenario.get("then", "例外処理結果")}
        """
        # Given: {scenario.get("given", "例外前提条件")}
        # TODO: 例外前提条件の準備を実装
        
        # When: {scenario.get("when", "例外発生条件")}
        # TODO: 例外発生処理を実装
        
        # Then: {scenario.get("then", "例外処理結果")}
        # TODO: 例外処理結果検証を実装
        
        pytest.fail("TODO: このテストは未実装です (TDD RED Phase)")
'''
    
    # ドメインモデルのテスト（エンティティ用）
    entities = domain_model.get("entities", [])
    if entities:
        test_content += f'''


class TestDomainEntities:
    """ドメインエンティティのテスト"""
    
'''
        for entity in entities:
            entity_name = entity.get("name", "UnknownEntity")
            test_content += f'''
    def test_{entity_name.lower()}_creation(self):
        """
        {entity_name}エンティティの作成テスト
        """
        # TODO: {entity_name}の作成処理を実装
        pytest.fail("TODO: {entity_name}エンティティは未実装です (TDD RED Phase)")
    
    def test_{entity_name.lower()}_validation(self):
        """
        {entity_name}エンティティのバリデーションテスト
        """
        # TODO: {entity_name}のバリデーション処理を実装
        pytest.fail("TODO: {entity_name}バリデーションは未実装です (TDD RED Phase)")
'''
    
    # 値オブジェクトのテスト
    value_objects = domain_model.get("value_objects", [])
    if value_objects:
        test_content += f'''


class TestValueObjects:
    """値オブジェクトのテスト"""
    
'''
        for vo in value_objects:
            vo_name = vo.get("name", "UnknownValueObject")
            test_content += f'''
    def test_{vo_name.lower()}_immutability(self):
        """
        {vo_name}値オブジェクトの不変性テスト
        """
        # TODO: {vo_name}の不変性を実装
        pytest.fail("TODO: {vo_name}値オブジェクトは未実装です (TDD RED Phase)")
'''
    
    test_content += '''

if __name__ == "__main__":
    pytest.main([__file__])
'''
    
    return test_content


def create_test_directory(issue_number):
    """テスト用ディレクトリを作成"""
    test_dir = Path("tests") / f"test_issue_{issue_number}"
    test_dir.mkdir(parents=True, exist_ok=True)
    return test_dir


def main():
    """メイン処理"""
    
    # 引数チェック
    if len(sys.argv) < 2:
        print("❌ エラー: Issue番号が必要です")
        print("使用方法: /create-tests <issue-number>")
        sys.exit(1)
    
    issue_number = sys.argv[1]
    print(f"\n🧪 Issue #{issue_number} のTDDテスト（RED Phase）を作成します\n")
    
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
    
    # テストコードを生成
    print("🧪 テストコードを生成中...")
    test_content = generate_test_content(use_case_data)
    
    # テストディレクトリを作成
    test_dir = create_test_directory(issue_number)
    
    # テストファイルを保存
    test_file_path = test_dir / f"test_use_case_{issue_number}.py"
    with open(test_file_path, 'w', encoding='utf-8') as f:
        f.write(test_content)
    
    print(f"✅ テストファイルを作成: {test_file_path}")
    
    # TDDフェーズを更新
    print("📊 TDDフェーズを更新中...")
    update_tdd_phase(
        json_file_path,
        "RED",
        "completed",
        f"/create-tests {issue_number}",
        files_created=[str(test_file_path)]
    )
    
    # 実行履歴を更新
    update_execution_history(
        json_file_path,
        f"/create-tests {issue_number}",
        "success",
        [str(test_file_path)]
    )
    
    # 更新されたデータを読み込み
    updated_data = load_use_case_json(json_file_path)
    
    # 実行状況を表示
    print("\n" + "="*60)
    print(format_execution_status(updated_data))
    print("="*60)
    
    # サマリー表示
    scenarios = use_case_data.get("scenarios", {})
    main_count = len(scenarios.get("main_scenarios", []))
    alt_count = len(scenarios.get("alternative_scenarios", []))
    exc_count = len(scenarios.get("exception_scenarios", []))
    total_tests = main_count + alt_count + exc_count
    
    entities = use_case_data.get("domain_model", {}).get("entities", [])
    value_objects = use_case_data.get("domain_model", {}).get("value_objects", [])
    domain_tests = len(entities) * 2 + len(value_objects)  # 各エンティティに2つのテスト
    
    print(f"\n📊 実行サマリー")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"🔴 TDD RED Phase: 完了")
    print(f"✅ シナリオテスト: {total_tests}件 (メイン:{main_count}, 代替:{alt_count}, 例外:{exc_count})")
    print(f"✅ ドメインテスト: {domain_tests}件 (エンティティ:{len(entities)}, 値オブジェクト:{len(value_objects)})")
    print(f"✅ 合計テスト数: {total_tests + domain_tests}件")
    
    print(f"\n📁 成果物")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"✅ {test_file_path}")
    print(f"✅ {json_file_path} (実行履歴更新)")
    
    print(f"\n⏭️ 次の推奨コマンド")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"1. uv run --frozen pytest {test_file_path} -v")
    print(f"   → すべてのテストが失敗することを確認（RED Phase検証）")
    print(f"2. /implement-domain {issue_number}")
    print(f"   → ドメイン層の実装開始（GREEN Phase）")
    
    print(f"\n💡 TDD RED Phase完了")
    print(f"すべてのテストは意図的に失敗します。これがTDDの正常な開始状態です。")


if __name__ == "__main__":
    main()