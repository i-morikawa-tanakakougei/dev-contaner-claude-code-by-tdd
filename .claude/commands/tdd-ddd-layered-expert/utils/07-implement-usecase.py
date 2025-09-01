#!/usr/bin/env python3
"""
Implement Use Case Command - 改修版
アプリケーション層を実装し、実行履歴を更新
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


def create_application_directory():
    """アプリケーション層のディレクトリ構造を作成"""
    app_dir = Path("src/application")
    app_dir.mkdir(parents=True, exist_ok=True)
    
    # __init__.py ファイルを作成
    (app_dir / "__init__.py").touch(exist_ok=True)
    
    # サブディレクトリを作成
    subdirs = ["use_cases", "services", "dtos", "interfaces"]
    for subdir in subdirs:
        subdir_path = app_dir / subdir
        subdir_path.mkdir(exist_ok=True)
        (subdir_path / "__init__.py").touch(exist_ok=True)
    
    return app_dir


def generate_dto_code(scenario):
    """DTOのコードを生成"""
    scenario_id = scenario.get("id", "unknown")
    
    code = f'''"""
{scenario_id} DTO Classes
アプリケーション層での入出力データ転送オブジェクト
"""

from typing import Optional, Any, List
from dataclasses import dataclass
from datetime import datetime


@dataclass
class {scenario_id.replace('-', '_').title()}RequestDTO:
    """
    {scenario_id} リクエストDTO
    """
    # TODO: Given条件から必要な入力パラメータを定義
    # Example fields based on common use case patterns:
    user_id: Optional[str] = None
    request_data: Optional[dict] = None
    timestamp: datetime = None
    
    def __post_init__(self):
        """初期化後の処理"""
        if self.timestamp is None:
            self.timestamp = datetime.now()


@dataclass 
class {scenario_id.replace('-', '_').title()}ResponseDTO:
    """
    {scenario_id} レスポンスDTO
    """
    # TODO: Then条件から必要な出力データを定義
    # Example fields based on common use case patterns:
    success: bool = False
    result_data: Optional[dict] = None
    message: Optional[str] = None
    timestamp: datetime = None
    
    def __post_init__(self):
        """初期化後の処理"""
        if self.timestamp is None:
            self.timestamp = datetime.now()
'''
    
    return code


def generate_use_case_code(scenario, issue_number):
    """ユースケースのコードを生成"""
    scenario_id = scenario.get("id", "unknown")
    scenario_title = scenario.get("title", scenario_id)
    given = scenario.get("given", "前提条件")
    when = scenario.get("when", "実行条件")
    then = scenario.get("then", "期待結果")
    
    class_name = f"{scenario_id.replace('-', '_').title()}UseCase"
    
    code = f'''"""
{class_name}
Issue #{issue_number}: {scenario_title}

Given: {given}
When:  {when}
Then:  {then}
"""

from typing import Optional
from ..dtos.{scenario_id.replace('-', '_')}_dto import (
    {scenario_id.replace('-', '_').title()}RequestDTO,
    {scenario_id.replace('-', '_').title()}ResponseDTO
)
from ...domain.repositories import *  # TODO: 適切なリポジトリをimport
from ...domain.services import *      # TODO: 適切なドメインサービスをimport


class {class_name}:
    """
    {scenario_title} ユースケース
    
    アプリケーションサービスとして以下の責務を持つ：
    1. 入力の検証とDTO変換
    2. ドメインオブジェクトの取得・操作の調整
    3. トランザクション境界の管理
    4. ドメインイベントの処理
    5. 出力DTOへの変換
    """
    
    def __init__(self, 
                 # TODO: 必要なリポジトリとサービスを注入
                 # example_repository: ExampleRepository,
                 # example_service: ExampleService
                 ):
        """
        ユースケースを初期化
        """
        # self._example_repository = example_repository
        # self._example_service = example_service
        pass
    
    async def execute(self, 
                     request: {scenario_id.replace('-', '_').title()}RequestDTO
                     ) -> {scenario_id.replace('-', '_').title()}ResponseDTO:
        """
        ユースケースを実行
        
        Args:
            request: リクエストDTO
            
        Returns:
            ResponseDTO: 実行結果
            
        Raises:
            ValidationError: 入力検証エラー
            DomainError: ビジネスルール違反
            InfrastructureError: インフラストラクチャエラー
        """
        try:
            # 1. 入力検証
            self._validate_request(request)
            
            # 2. ドメインオブジェクトの取得
            # TODO: リポジトリからドメインオブジェクトを取得
            # domain_object = await self._example_repository.find_by_id(request.id)
            
            # 3. ビジネスロジックの実行
            # TODO: ドメインサービスを使用してビジネスロジックを実行
            # result = await self._example_service.process(domain_object, request.data)
            
            # 4. 永続化
            # TODO: 変更されたドメインオブジェクトを永続化
            # saved_object = await self._example_repository.save(result)
            
            # 5. レスポンスDTOの作成
            return {scenario_id.replace('-', '_').title()}ResponseDTO(
                success=True,
                result_data={{"message": "処理が正常に完了しました"}},
                message="Success"
            )
            
        except Exception as e:
            # エラーハンドリング
            return {scenario_id.replace('-', '_').title()}ResponseDTO(
                success=False,
                message=f"エラーが発生しました: {{str(e)}}"
            )
    
    def _validate_request(self, request: {scenario_id.replace('-', '_').title()}RequestDTO) -> None:
        """
        リクエストの妥当性を検証
        
        Args:
            request: 検証対象のリクエスト
            
        Raises:
            ValidationError: 検証に失敗した場合
        """
        # TODO: ビジネスルールに基づく入力検証を実装
        if not request:
            raise ValueError("リクエストが空です")
        
        # Given条件に基づく検証ロジック
        # Example: {given}
        pass
    
    def _handle_business_rules(self) -> None:
        """
        ビジネスルールの実行
        
        When条件: {when}
        Then条件: {then}
        """
        # TODO: ビジネスルール実装
        pass
'''
    
    return code


def generate_application_service_code(use_case_data, issue_number):
    """アプリケーションサービスの統合コードを生成"""
    metadata = use_case_data.get("metadata", {})
    title = metadata.get("title", f"Issue {issue_number}")
    
    code = f'''"""
Issue #{issue_number} Application Service
{title}

このファイルは複数のユースケースを統合するアプリケーションサービスです
"""

from typing import List
from .dtos import *
from .use_cases import *
from ..domain.repositories import *
from ..domain.services import *


class Issue{issue_number}ApplicationService:
    """
    Issue #{issue_number} のアプリケーションサービス
    
    複数のユースケースを調整し、トランザクション境界を管理します
    """
    
    def __init__(self):
        """アプリケーションサービスを初期化"""
        # TODO: 依存関係の注入を実装
        pass
    
    async def get_available_use_cases(self) -> List[str]:
        """
        利用可能なユースケース一覧を取得
        
        Returns:
            List[str]: ユースケース名のリスト
        """
        return [
            # TODO: 実装されたユースケースを列挙
            "メインシナリオ",
            "代替シナリオ", 
            "例外シナリオ"
        ]
    
    async def execute_workflow(self, workflow_data: dict) -> dict:
        """
        ワークフロー全体を実行
        
        Args:
            workflow_data: ワークフロー実行データ
            
        Returns:
            dict: 実行結果
        """
        results = []
        
        # TODO: ユースケースチェーンの実行
        # 1. メインシナリオの実行
        # 2. 必要に応じて代替シナリオの実行
        # 3. 例外処理の実行
        
        return {{
            "success": True,
            "results": results,
            "message": "ワークフロー実行完了"
        }}
'''
    
    return code


def implement_application_layer(use_case_data, issue_number):
    """アプリケーション層を実装"""
    app_dir = create_application_directory()
    created_files = []
    
    scenarios = use_case_data.get("scenarios", {})
    
    # 各シナリオに対してDTOとユースケースを生成
    all_scenarios = []
    all_scenarios.extend(scenarios.get("main_scenarios", []))
    all_scenarios.extend(scenarios.get("alternative_scenarios", []))
    all_scenarios.extend(scenarios.get("exception_scenarios", []))
    
    for scenario in all_scenarios:
        scenario_id = scenario.get("id", f"scenario_{len(created_files)}")
        
        # DTO生成
        dto_code = generate_dto_code(scenario)
        dto_file = app_dir / "dtos" / f"{scenario_id.replace('-', '_')}_dto.py"
        with open(dto_file, 'w', encoding='utf-8') as f:
            f.write(dto_code)
        created_files.append(str(dto_file))
        
        # ユースケース生成
        use_case_code = generate_use_case_code(scenario, issue_number)
        use_case_file = app_dir / "use_cases" / f"{scenario_id.replace('-', '_')}_use_case.py"
        with open(use_case_file, 'w', encoding='utf-8') as f:
            f.write(use_case_code)
        created_files.append(str(use_case_file))
    
    # アプリケーションサービス生成
    app_service_code = generate_application_service_code(use_case_data, issue_number)
    app_service_file = app_dir / "services" / f"issue_{issue_number}_application_service.py"
    with open(app_service_file, 'w', encoding='utf-8') as f:
        f.write(app_service_code)
    created_files.append(str(app_service_file))
    
    return created_files


def main():
    """メイン処理"""
    
    # 引数チェック
    if len(sys.argv) < 2:
        print("❌ エラー: Issue番号が必要です")
        print("使用方法: /implement-usecase <issue-number>")
        sys.exit(1)
    
    issue_number = sys.argv[1]
    print(f"\n🏗️ Issue #{issue_number} のアプリケーション層実装を開始します\n")
    
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
        print("⚠️ 警告: GREEN Phase（ドメイン実装）が完了していません")
        print("先に /implement-domain コマンドを実行することを推奨します")
    
    # アプリケーション層を実装
    print("🏗️ アプリケーション層を実装中...")
    created_files = implement_application_layer(use_case_data, issue_number)
    
    print(f"✅ アプリケーション層の実装完了: {len(created_files)}ファイル作成")
    
    # アーキテクチャ整合性を更新
    use_case_data = load_use_case_json(json_file_path)
    architecture = use_case_data.get("architecture_alignment", {})
    architecture.setdefault("layers", {})["application"] = True
    use_case_data["architecture_alignment"] = architecture
    save_use_case_json(json_file_path, use_case_data)
    
    # 実行履歴を更新
    update_execution_history(
        json_file_path,
        f"/implement-usecase {issue_number}",
        "success",
        created_files
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
    total_scenarios = main_count + alt_count + exc_count
    
    print(f"\n📊 実行サマリー")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"🏗️ アプリケーション層実装: 完了")
    print(f"✅ シナリオ総数: {total_scenarios}個 (メイン:{main_count}, 代替:{alt_count}, 例外:{exc_count})")
    print(f"✅ 生成DTO: {total_scenarios}個")
    print(f"✅ 生成ユースケース: {total_scenarios}個")
    print(f"✅ アプリケーションサービス: 1個")
    print(f"✅ 合計ファイル数: {len(created_files)}個")
    
    print(f"\n📁 成果物")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    for file_path in created_files:
        print(f"✅ {file_path}")
    
    print(f"\n⏭️ 次の推奨コマンド")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"1. /implement-infra {issue_number}")
    print(f"   → インフラストラクチャ層の実装")
    print(f"2. /implement-presentation {issue_number}")
    print(f"   → プレゼンテーション層の実装")
    print(f"3. /run-all-tests {issue_number}")
    print(f"   → 統合テストの実行")
    
    print(f"\n💡 アプリケーション層実装完了")
    print(f"ユースケースとDTOが生成されました。必要に応じてビジネスロジックを実装してください。")


if __name__ == "__main__":
    main()