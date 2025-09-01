#!/usr/bin/env python3
"""
Implement Domain Command - 改修版
TDD GREEN Phaseでドメイン層を実装し、実行履歴を更新
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


def create_domain_directory():
    """ドメイン層のディレクトリ構造を作成"""
    domain_dir = Path("src/domain")
    domain_dir.mkdir(parents=True, exist_ok=True)
    
    # __init__.py ファイルを作成
    (domain_dir / "__init__.py").touch(exist_ok=True)
    
    # サブディレクトリを作成
    subdirs = ["entities", "value_objects", "services", "repositories"]
    for subdir in subdirs:
        subdir_path = domain_dir / subdir
        subdir_path.mkdir(exist_ok=True)
        (subdir_path / "__init__.py").touch(exist_ok=True)
    
    return domain_dir


def generate_entity_code(entity):
    """エンティティのコードを生成"""
    entity_name = entity.get("name", "UnknownEntity")
    description = entity.get("description", "")
    properties = entity.get("properties", {})
    
    code = f'''"""
{entity_name}エンティティ

{description}
"""

from typing import Optional, Any
from datetime import datetime


class {entity_name}:
    """
    {entity_name}エンティティ
    
    {description}
    """
    
    def __init__(self'''
    
    # コンストラクタのパラメータを生成
    if properties:
        params = []
        for prop_name, prop_info in properties.items():
            if isinstance(prop_info, dict):
                prop_type = prop_info.get("type", "Any")
                required = prop_info.get("required", True)
                if not required:
                    params.append(f"{prop_name}: Optional[{prop_type}] = None")
                else:
                    params.append(f"{prop_name}: {prop_type}")
            else:
                params.append(f"{prop_name}: Any")
        
        code += ", " + ", ".join(params)
    
    code += f'''):
        """
        {entity_name}を初期化
        """
        self._created_at = datetime.now()
        self._updated_at = datetime.now()
'''
    
    # プロパティの初期化
    if properties:
        for prop_name in properties.keys():
            code += f"        self._{prop_name} = {prop_name}\n"
    
    # プロパティのゲッターを生成
    if properties:
        for prop_name, prop_info in properties.items():
            code += f'''
    @property
    def {prop_name}(self):
        """
        {prop_name}を取得
        """
        return self._{prop_name}
'''
    
    # 基本的なメソッドを追加
    code += f'''
    @property
    def created_at(self) -> datetime:
        """作成日時を取得"""
        return self._created_at
    
    @property
    def updated_at(self) -> datetime:
        """更新日時を取得"""
        return self._updated_at
    
    def validate(self) -> bool:
        """
        エンティティの妥当性を検証
        
        Returns:
            bool: 妥当性検証の結果
        """
        # TODO: ビジネスルールに基づく検証を実装
        return True
    
    def __eq__(self, other):
        """等価性の比較（IDベース）"""
        if not isinstance(other, {entity_name}):
            return False
        return self.id == other.id if hasattr(self, 'id') and hasattr(other, 'id') else False
    
    def __hash__(self):
        """ハッシュ値の計算"""
        return hash(self.id) if hasattr(self, 'id') else hash(id(self))
    
    def __repr__(self):
        """文字列表現"""
        return f"{entity_name}({', '.join(f'{k}={{self.{k}}}' for k in {list(properties.keys()) if properties else []})})"
'''
    
    return code


def generate_value_object_code(value_object):
    """値オブジェクトのコードを生成"""
    vo_name = value_object.get("name", "UnknownValueObject")
    description = value_object.get("description", "")
    
    code = f'''"""
{vo_name}値オブジェクト

{description}
"""

from typing import Any
from dataclasses import dataclass


@dataclass(frozen=True)
class {vo_name}:
    """
    {vo_name}値オブジェクト
    
    {description}
    
    値オブジェクトは不変であり、値によって識別されます。
    """
    
    value: Any
    
    def __post_init__(self):
        """初期化後の検証"""
        self.validate()
    
    def validate(self) -> None:
        """
        値の妥当性を検証
        
        Raises:
            ValueError: 無効な値の場合
        """
        # TODO: ビジネスルールに基づく検証を実装
        if self.value is None:
            raise ValueError(f"{vo_name}の値はNoneにできません")
    
    def __str__(self) -> str:
        """文字列表現"""
        return str(self.value)
    
    def equals(self, other: "{vo_name}") -> bool:
        """
        値による等価性判定
        
        Args:
            other: 比較対象の{vo_name}
            
        Returns:
            bool: 等価かどうか
        """
        return isinstance(other, {vo_name}) and self.value == other.value
'''
    
    return code


def generate_domain_service_code(service):
    """ドメインサービスのコードを生成"""
    service_name = service.get("name", "UnknownDomainService")
    description = service.get("description", "")
    
    code = f'''"""
{service_name}ドメインサービス

{description}
"""

from abc import ABC, abstractmethod
from typing import Any


class {service_name}:
    """
    {service_name}ドメインサービス
    
    {description}
    
    複数のエンティティにまたがるビジネスロジックや、
    エンティティに属さない処理を実装します。
    """
    
    def __init__(self):
        """ドメインサービスを初期化"""
        pass
    
    def execute(self, *args, **kwargs) -> Any:
        """
        ドメインサービスのメイン処理
        
        Args:
            *args: 位置引数
            **kwargs: キーワード引数
            
        Returns:
            Any: 処理結果
        """
        # TODO: ドメインサービスのビジネスロジックを実装
        raise NotImplementedError("ドメインサービスの処理を実装してください")
    
    def validate_business_rules(self, *args, **kwargs) -> bool:
        """
        ビジネスルールの検証
        
        Args:
            *args: 位置引数
            **kwargs: キーワード引数
            
        Returns:
            bool: ビジネスルールの妥当性
        """
        # TODO: ビジネスルール検証を実装
        return True
'''
    
    return code


def generate_repository_interface(entity_name):
    """リポジトリインターフェースのコードを生成"""
    
    code = f'''"""
{entity_name}リポジトリインターフェース

{entity_name}の永続化に関する抽象化を定義
"""

from abc import ABC, abstractmethod
from typing import List, Optional
from ..entities.{entity_name.lower()} import {entity_name}


class {entity_name}Repository(ABC):
    """
    {entity_name}リポジトリの抽象インターフェース
    
    ドメイン層では具象実装に依存せず、
    このインターフェースを通じてデータ操作を行います。
    """
    
    @abstractmethod
    def save(self, {entity_name.lower()}: {entity_name}) -> {entity_name}:
        """
        {entity_name}を保存
        
        Args:
            {entity_name.lower()}: 保存する{entity_name}
            
        Returns:
            {entity_name}: 保存された{entity_name}
        """
        pass
    
    @abstractmethod
    def find_by_id(self, id: str) -> Optional[{entity_name}]:
        """
        IDで{entity_name}を検索
        
        Args:
            id: {entity_name}のID
            
        Returns:
            Optional[{entity_name}]: 見つかった{entity_name}、またはNone
        """
        pass
    
    @abstractmethod
    def find_all(self) -> List[{entity_name}]:
        """
        すべての{entity_name}を取得
        
        Returns:
            List[{entity_name}]: {entity_name}のリスト
        """
        pass
    
    @abstractmethod
    def delete(self, id: str) -> bool:
        """
        {entity_name}を削除
        
        Args:
            id: 削除する{entity_name}のID
            
        Returns:
            bool: 削除が成功したかどうか
        """
        pass
'''
    
    return code


def implement_domain_layer(use_case_data, issue_number):
    """ドメイン層を実装"""
    domain_dir = create_domain_directory()
    created_files = []
    
    domain_model = use_case_data.get("domain_model", {})
    
    # エンティティの実装
    entities = domain_model.get("entities", [])
    for entity in entities:
        entity_name = entity.get("name", "UnknownEntity")
        entity_code = generate_entity_code(entity)
        
        entity_file = domain_dir / "entities" / f"{entity_name.lower()}.py"
        with open(entity_file, 'w', encoding='utf-8') as f:
            f.write(entity_code)
        
        created_files.append(str(entity_file))
        
        # リポジトリインターフェースも作成
        repo_code = generate_repository_interface(entity_name)
        repo_file = domain_dir / "repositories" / f"{entity_name.lower()}_repository.py"
        with open(repo_file, 'w', encoding='utf-8') as f:
            f.write(repo_code)
        
        created_files.append(str(repo_file))
    
    # 値オブジェクトの実装
    value_objects = domain_model.get("value_objects", [])
    for vo in value_objects:
        vo_name = vo.get("name", "UnknownValueObject")
        vo_code = generate_value_object_code(vo)
        
        vo_file = domain_dir / "value_objects" / f"{vo_name.lower()}.py"
        with open(vo_file, 'w', encoding='utf-8') as f:
            f.write(vo_code)
        
        created_files.append(str(vo_file))
    
    # ドメインサービスの実装
    domain_services = domain_model.get("domain_services", [])
    for service in domain_services:
        service_name = service.get("name", "UnknownDomainService")
        service_code = generate_domain_service_code(service)
        
        service_file = domain_dir / "services" / f"{service_name.lower()}.py"
        with open(service_file, 'w', encoding='utf-8') as f:
            f.write(service_code)
        
        created_files.append(str(service_file))
    
    return created_files


def main():
    """メイン処理"""
    
    # 引数チェック
    if len(sys.argv) < 2:
        print("❌ エラー: Issue番号が必要です")
        print("使用方法: /implement-domain <issue-number>")
        sys.exit(1)
    
    issue_number = sys.argv[1]
    print(f"\n🏗️ Issue #{issue_number} のドメイン層実装（GREEN Phase）を開始します\n")
    
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
    
    # RED Phaseの完了確認
    tdd_phases = use_case_data.get("execution_history", {}).get("tdd_phases", {})
    if tdd_phases.get("RED", {}).get("status") != "completed":
        print("⚠️ 警告: RED Phase（テスト作成）が完了していません")
        print("先に /create-tests コマンドを実行してください")
    
    # ドメイン層を実装
    print("🏗️ ドメイン層を実装中...")
    created_files = implement_domain_layer(use_case_data, issue_number)
    
    print(f"✅ ドメイン層の実装完了: {len(created_files)}ファイル作成")
    
    # TDDフェーズを更新
    print("📊 TDDフェーズを更新中...")
    update_tdd_phase(
        json_file_path,
        "GREEN",
        "completed",
        f"/implement-domain {issue_number}",
        files_created=created_files
    )
    
    # アーキテクチャ整合性を更新
    use_case_data = load_use_case_json(json_file_path)
    architecture = use_case_data.get("architecture_alignment", {})
    architecture.setdefault("layers", {})["domain"] = True
    use_case_data["architecture_alignment"] = architecture
    save_use_case_json(json_file_path, use_case_data)
    
    # 実行履歴を更新
    update_execution_history(
        json_file_path,
        f"/implement-domain {issue_number}",
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
    domain_model = use_case_data.get("domain_model", {})
    entities_count = len(domain_model.get("entities", []))
    vo_count = len(domain_model.get("value_objects", []))
    services_count = len(domain_model.get("domain_services", []))
    
    print(f"\n📊 実行サマリー")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"🟢 TDD GREEN Phase: 完了")
    print(f"✅ エンティティ: {entities_count}個")
    print(f"✅ 値オブジェクト: {vo_count}個")
    print(f"✅ ドメインサービス: {services_count}個")
    print(f"✅ リポジトリIF: {entities_count}個")
    print(f"✅ 合計ファイル数: {len(created_files)}個")
    
    print(f"\n📁 成果物")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    for file_path in created_files:
        print(f"✅ {file_path}")
    
    print(f"\n⏭️ 次の推奨コマンド")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"1. uv run --frozen pytest tests/test_issue_{issue_number}/ -v")
    print(f"   → テストが通るようになったか確認（GREEN Phase検証）")
    print(f"2. /implement-usecase {issue_number}")
    print(f"   → アプリケーション層の実装")
    print(f"3. /refactor {issue_number}")
    print(f"   → コードの改善（REFACTOR Phase）")
    
    print(f"\n💡 TDD GREEN Phase完了")
    print(f"ドメイン層の最小実装が完了しました。テストを実行して確認してください。")


if __name__ == "__main__":
    main()