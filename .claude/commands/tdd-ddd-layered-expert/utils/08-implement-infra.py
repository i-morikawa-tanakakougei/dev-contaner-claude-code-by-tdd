#!/usr/bin/env python3
"""
Infrastructure Layer Implementation Command - 改修版
インフラストラクチャ層を実装し、実行履歴を更新
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


def create_infrastructure_directories():
    """インフラストラクチャ層のディレクトリ構造を作成"""
    base_path = Path("src/infrastructure")
    
    dirs_to_create = [
        base_path,
        base_path / "repositories",
        base_path / "models", 
        base_path / "external",
        base_path / "config",
        base_path / "database"
    ]
    
    created_dirs = []
    for dir_path in dirs_to_create:
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)
            created_dirs.append(str(dir_path))
        
        # __init__.pyファイルも作成
        init_file = dir_path / "__init__.py"
        if not init_file.exists():
            init_file.write_text("", encoding="utf-8")
    
    return created_dirs


def analyze_repository_interfaces(domain_dir):
    """ドメイン層のリポジトリインターフェースを分析"""
    repository_interfaces = []
    
    domain_path = Path(domain_dir)
    if not domain_path.exists():
        return repository_interfaces
    
    # repositoriesディレクトリからインターフェースを検索
    repo_dir = domain_path / "repositories"
    if repo_dir.exists():
        for py_file in repo_dir.glob("*.py"):
            if py_file.name != "__init__.py":
                repository_interfaces.append({
                    "interface_name": py_file.stem,
                    "file_path": str(py_file),
                    "implementation_needed": True
                })
    
    return repository_interfaces


def generate_repository_implementation(interface_name, use_case_data):
    """リポジトリの具体実装コードを生成"""
    
    entity_name = interface_name.replace("Repository", "").replace("_repository", "")
    class_name = f"Sql{entity_name.title()}Repository"
    
    content = f'''"""
{entity_name.title()} Repository Implementation
SQLAlchemyを使用した{entity_name}リポジトリの具体実装
"""

from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, desc

from src.domain.entities.{entity_name.lower()} import {entity_name.title()}
from src.domain.repositories.{interface_name.lower()} import {interface_name.title()}
from src.infrastructure.models.{entity_name.lower()}_model import {entity_name.title()}Model
from src.infrastructure.mappers.{entity_name.lower()}_mapper import {entity_name.title()}Mapper


class {class_name}({interface_name.title()}):
    """
    {entity_name.title()}リポジトリのSQL実装
    ドメインオブジェクトとデータベースモデル間の変換を担当
    """
    
    def __init__(self, session: Session):
        """
        Args:
            session: SQLAlchemyセッション
        """
        self._session = session
        self._mapper = {entity_name.title()}Mapper()
    
    def save(self, entity: {entity_name.title()}) -> None:
        """エンティティを保存"""
        try:
            # ドメインエンティティをDBモデルに変換
            db_model = self._mapper.to_database(entity)
            
            # 既存レコードの確認
            existing = self._session.query({entity_name.title()}Model).filter(
                {entity_name.title()}Model.id == entity.id.value
            ).first()
            
            if existing:
                # 更新
                for attr, value in db_model.__dict__.items():
                    if not attr.startswith('_'):
                        setattr(existing, attr, value)
            else:
                # 新規作成
                self._session.add(db_model)
            
            self._session.flush()
            
        except Exception as e:
            self._session.rollback()
            raise RuntimeError(f"Failed to save {entity_name.lower()}: {{e}}")
    
    def find_by_id(self, entity_id: str) -> Optional[{entity_name.title()}]:
        """IDでエンティティを検索"""
        try:
            db_model = self._session.query({entity_name.title()}Model).filter(
                {entity_name.title()}Model.id == entity_id
            ).first()
            
            return self._mapper.to_domain(db_model) if db_model else None
            
        except Exception as e:
            raise RuntimeError(f"Failed to find {entity_name.lower()} by ID: {{e}}")
    
    def find_all(self) -> List[{entity_name.title()}]:
        """全エンティティを取得"""
        try:
            db_models = self._session.query({entity_name.title()}Model).all()
            return [self._mapper.to_domain(model) for model in db_models]
            
        except Exception as e:
            raise RuntimeError(f"Failed to find all {entity_name.lower()}s: {{e}}")
    
    def delete(self, entity_id: str) -> None:
        """エンティティを削除"""
        try:
            result = self._session.query({entity_name.title()}Model).filter(
                {entity_name.title()}Model.id == entity_id
            ).delete()
            
            if result == 0:
                raise ValueError(f"{entity_name.title()} with ID {{entity_id}} not found")
            
            self._session.flush()
            
        except Exception as e:
            self._session.rollback()
            raise RuntimeError(f"Failed to delete {entity_name.lower()}: {{e}}")
    
    def count(self) -> int:
        """エンティティの総数を取得"""
        try:
            return self._session.query({entity_name.title()}Model).count()
        except Exception as e:
            raise RuntimeError(f"Failed to count {entity_name.lower()}s: {{e}}")
'''
    
    return content


def generate_database_model(entity_name, use_case_data):
    """データベースモデルを生成"""
    
    class_name = f"{entity_name.title()}Model"
    table_name = f"{entity_name.lower()}s"
    
    content = f'''"""
{entity_name.title()} Database Model
SQLAlchemyを使用した{entity_name}のデータベースモデル定義
"""

from datetime import datetime
from sqlalchemy import Column, String, DateTime, Text, Boolean, Integer
from sqlalchemy.ext.declarative import declarative_base

from src.infrastructure.database.base import Base


class {class_name}(Base):
    """
    {entity_name.title()}のデータベースモデル
    ドメインエンティティに対応するデータベーステーブル構造
    """
    
    __tablename__ = "{table_name}"
    
    # 基本フィールド
    id = Column(String(36), primary_key=True, comment="{entity_name.title()}の一意識別子")
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow, comment="作成日時")
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow, comment="更新日時")
    
    # ビジネスフィールド（ドメインモデルに基づいて調整が必要）
    name = Column(String(255), nullable=False, comment="{entity_name.title()}名")
    description = Column(Text, nullable=True, comment="説明")
    status = Column(String(50), nullable=False, default="active", comment="ステータス")
    is_active = Column(Boolean, nullable=False, default=True, comment="アクティブフラグ")
    
    # インデックス（必要に応じて追加）
    __table_args__ = (
        # Index('idx_{table_name}_status', 'status'),
        # Index('idx_{table_name}_created_at', 'created_at'),
    )
    
    def __repr__(self):
        return f"<{class_name}(id='{{self.id}}', name='{{self.name}}')>"
    
    def to_dict(self):
        """辞書形式でデータを返す"""
        return {{
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'status': self.status,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }}
'''
    
    return content


def generate_data_mapper(entity_name, use_case_data):
    """ドメインエンティティとDBモデル間のマッパーを生成"""
    
    mapper_class = f"{entity_name.title()}Mapper"
    
    content = f'''"""
{entity_name.title()} Data Mapper
ドメインエンティティとデータベースモデル間の変換を担当
"""

from typing import Optional
from datetime import datetime

from src.domain.entities.{entity_name.lower()} import {entity_name.title()}
from src.domain.value_objects.{entity_name.lower()}_id import {entity_name.title()}Id
from src.infrastructure.models.{entity_name.lower()}_model import {entity_name.title()}Model


class {mapper_class}:
    """
    {entity_name.title()}のドメインオブジェクトとデータベースモデル間の変換
    Clean Architectureの依存性逆転原則を維持
    """
    
    def to_domain(self, db_model: {entity_name.title()}Model) -> {entity_name.title()}:
        """
        データベースモデルからドメインエンティティに変換
        
        Args:
            db_model: データベースモデル
            
        Returns:
            ドメインエンティティ
        """
        if not db_model:
            return None
            
        try:
            return {entity_name.title()}(
                id={entity_name.title()}Id(db_model.id),
                name=db_model.name,
                description=db_model.description,
                status=db_model.status,
                is_active=db_model.is_active,
                created_at=db_model.created_at,
                updated_at=db_model.updated_at
            )
        except Exception as e:
            raise RuntimeError(f"Failed to convert DB model to domain entity: {{e}}")
    
    def to_database(self, entity: {entity_name.title()}) -> {entity_name.title()}Model:
        """
        ドメインエンティティからデータベースモデルに変換
        
        Args:
            entity: ドメインエンティティ
            
        Returns:
            データベースモデル
        """
        if not entity:
            return None
            
        try:
            return {entity_name.title()}Model(
                id=entity.id.value,
                name=entity.name,
                description=entity.description,
                status=entity.status,
                is_active=entity.is_active,
                created_at=entity.created_at,
                updated_at=entity.updated_at or datetime.utcnow()
            )
        except Exception as e:
            raise RuntimeError(f"Failed to convert domain entity to DB model: {{e}}")
    
    def update_database_model(self, db_model: {entity_name.title()}Model, entity: {entity_name.title()}) -> None:
        """
        既存のデータベースモデルをドメインエンティティの値で更新
        
        Args:
            db_model: 更新対象のデータベースモデル
            entity: 新しい値を持つドメインエンティティ
        """
        try:
            db_model.name = entity.name
            db_model.description = entity.description
            db_model.status = entity.status
            db_model.is_active = entity.is_active
            db_model.updated_at = datetime.utcnow()
            
        except Exception as e:
            raise RuntimeError(f"Failed to update database model: {{e}}")
'''
    
    return content


def generate_database_configuration():
    """データベース設定ファイルを生成"""
    
    content = '''"""
Database Configuration
データベース接続設定とセッション管理
"""

import os
from typing import Generator
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import QueuePool

# ベースクラス
Base = declarative_base()

# メタデータ設定
metadata = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    }
)
Base.metadata = metadata


class DatabaseConfig:
    """データベース設定管理"""
    
    def __init__(self):
        self.database_url = os.getenv(
            "DATABASE_URL", 
            "sqlite:///./app.db"  # デフォルトはSQLite
        )
        self.echo_sql = os.getenv("DATABASE_ECHO", "false").lower() == "true"
        self.pool_size = int(os.getenv("DATABASE_POOL_SIZE", "5"))
        self.max_overflow = int(os.getenv("DATABASE_MAX_OVERFLOW", "10"))
    
    def create_engine(self):
        """SQLAlchemyエンジンを作成"""
        if self.database_url.startswith("sqlite"):
            # SQLite設定
            return create_engine(
                self.database_url,
                echo=self.echo_sql,
                connect_args={"check_same_thread": False}
            )
        else:
            # PostgreSQL/MySQL設定
            return create_engine(
                self.database_url,
                echo=self.echo_sql,
                poolclass=QueuePool,
                pool_size=self.pool_size,
                max_overflow=self.max_overflow,
                pool_pre_ping=True,
                pool_recycle=3600
            )


# グローバルな設定とセッション
config = DatabaseConfig()
engine = config.create_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db_session() -> Generator[Session, None, None]:
    """
    データベースセッションを取得
    依存性注入用のジェネレータ
    """
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def init_database():
    """
    データベースを初期化
    テーブル作成とマイグレーション
    """
    try:
        # テーブル作成
        Base.metadata.create_all(bind=engine)
        print("✅ Database tables created successfully")
        
    except Exception as e:
        print(f"❌ Failed to initialize database: {e}")
        raise


def drop_all_tables():
    """
    全テーブルを削除（テスト用）
    注意: 本番環境では使用しないこと
    """
    Base.metadata.drop_all(bind=engine)
    print("⚠️ All database tables dropped")
'''
    
    return content


def implement_infrastructure_layer(use_case_data, issue_number, repository_interfaces):
    """インフラストラクチャ層を実装"""
    
    created_files = []
    
    # ディレクトリ構造作成
    print("📁 インフラストラクチャディレクトリ構造を作成中...")
    created_dirs = create_infrastructure_directories()
    
    # データベース設定ファイル作成
    print("⚙️ データベース設定を生成中...")
    db_config_path = Path("src/infrastructure/database/config.py")
    db_config_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(db_config_path, 'w', encoding='utf-8') as f:
        f.write(generate_database_configuration())
    created_files.append(str(db_config_path))
    
    # base.pyファイル作成
    base_path = Path("src/infrastructure/database/base.py")
    base_content = '''"""
Database Base Module
SQLAlchemyベースクラスとユーティリティ
"""

from sqlalchemy.ext.declarative import declarative_base

# ベースクラス - すべてのモデルで使用
Base = declarative_base()
'''
    with open(base_path, 'w', encoding='utf-8') as f:
        f.write(base_content)
    created_files.append(str(base_path))
    
    # リポジトリ実装の生成
    if repository_interfaces:
        print(f"🔧 {len(repository_interfaces)}個のリポジトリ実装を生成中...")
        
        for repo_info in repository_interfaces:
            interface_name = repo_info["interface_name"]
            entity_name = interface_name.replace("Repository", "").replace("_repository", "")
            
            # リポジトリ実装
            repo_impl_path = Path(f"src/infrastructure/repositories/{interface_name.lower()}_impl.py")
            repo_impl_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(repo_impl_path, 'w', encoding='utf-8') as f:
                f.write(generate_repository_implementation(interface_name, use_case_data))
            created_files.append(str(repo_impl_path))
            
            # データベースモデル
            model_path = Path(f"src/infrastructure/models/{entity_name.lower()}_model.py")
            model_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(model_path, 'w', encoding='utf-8') as f:
                f.write(generate_database_model(entity_name, use_case_data))
            created_files.append(str(model_path))
            
            # データマッパー
            mapper_dir = Path("src/infrastructure/mappers")
            mapper_dir.mkdir(parents=True, exist_ok=True)
            mapper_path = mapper_dir / f"{entity_name.lower()}_mapper.py"
            
            with open(mapper_path, 'w', encoding='utf-8') as f:
                f.write(generate_data_mapper(entity_name, use_case_data))
            created_files.append(str(mapper_path))
    
    else:
        print("ℹ️ リポジトリインターフェースが見つかりません。汎用的な設定のみ生成します。")
    
    # 外部サービス統合の例
    print("🌐 外部サービス統合の例を生成中...")
    external_service_path = Path("src/infrastructure/external/example_api_client.py")
    external_service_path.parent.mkdir(parents=True, exist_ok=True)
    
    external_service_content = '''"""
Example External API Client
外部APIとの統合例
"""

import os
import httpx
from typing import Optional, Dict, Any
from datetime import datetime, timedelta


class ExampleApiClient:
    """
    外部APIクライアントの実装例
    実際のAPIに合わせてカスタマイズが必要
    """
    
    def __init__(self):
        self.base_url = os.getenv("EXTERNAL_API_BASE_URL", "https://api.example.com")
        self.api_key = os.getenv("EXTERNAL_API_KEY", "")
        self.timeout = int(os.getenv("EXTERNAL_API_TIMEOUT", "30"))
        
        if not self.api_key:
            raise ValueError("EXTERNAL_API_KEY environment variable is required")
    
    async def fetch_data(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        外部APIからデータを取得
        
        Args:
            endpoint: APIエンドポイント
            params: クエリパラメータ
            
        Returns:
            API応答データ
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "User-Agent": "InfrastructureLayer/1.0"
        }
        
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(url, headers=headers, params=params)
                response.raise_for_status()
                
                return response.json()
                
        except httpx.HTTPStatusError as e:
            raise RuntimeError(f"API request failed with status {e.response.status_code}: {e.response.text}")
        except httpx.RequestError as e:
            raise RuntimeError(f"API request error: {e}")
    
    async def post_data(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        外部APIにデータを送信
        
        Args:
            endpoint: APIエンドポイント
            data: 送信データ
            
        Returns:
            API応答データ
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "User-Agent": "InfrastructureLayer/1.0"
        }
        
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(url, headers=headers, json=data)
                response.raise_for_status()
                
                return response.json()
                
        except httpx.HTTPStatusError as e:
            raise RuntimeError(f"API request failed with status {e.response.status_code}: {e.response.text}")
        except httpx.RequestError as e:
            raise RuntimeError(f"API request error: {e}")
'''
    
    with open(external_service_path, 'w', encoding='utf-8') as f:
        f.write(external_service_content)
    created_files.append(str(external_service_path))
    
    return created_files


def update_use_case_json_with_infrastructure(json_file_path, created_files):
    """ユースケースJSONにインフラストラクチャ層情報を更新"""
    
    use_case_data = load_use_case_json(json_file_path)
    
    # アーキテクチャ整合性情報を更新
    architecture = use_case_data.get("architecture_alignment", {})
    architecture.setdefault("layers", {})["infrastructure"] = True  # 実装完了
    architecture.setdefault("patterns_used", []).extend([
        "Repository Pattern Implementation",
        "Data Mapper Pattern",
        "Database Abstraction Layer",
        "External Service Integration"
    ])
    use_case_data["architecture_alignment"] = architecture
    
    # 実装情報を記録
    infrastructure_info = use_case_data.get("implementation_details", {})
    infrastructure_info["infrastructure_layer"] = {
        "implemented": True,
        "files_created": created_files,
        "components": [
            "Repository Implementations",
            "Database Models",
            "Data Mappers",
            "Database Configuration",
            "External Service Clients"
        ],
        "completed_at": datetime.now().isoformat()
    }
    use_case_data["implementation_details"] = infrastructure_info
    
    # 保存
    save_use_case_json(json_file_path, use_case_data)
    
    return use_case_data


def main():
    """メイン処理"""
    
    # 引数チェック
    if len(sys.argv) < 2:
        print("❌ エラー: Issue番号が必要です")
        print("使用方法: /implement-infra <issue-number>")
        sys.exit(1)
    
    issue_number = sys.argv[1]
    print(f"\n🏗️ Issue #{issue_number} のインフラストラクチャ層実装を開始します\n")
    
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
    
    # ドメイン層のリポジトリインターフェースを分析
    print("🔍 ドメイン層のリポジトリインターフェースを分析中...")
    repository_interfaces = analyze_repository_interfaces("src/domain")
    
    if repository_interfaces:
        print(f"✅ {len(repository_interfaces)}個のリポジトリインターフェースを発見")
        for repo_info in repository_interfaces:
            print(f"  - {repo_info['interface_name']}")
    else:
        print("ℹ️ リポジトリインターフェースが見つかりません")
        print("汎用的なインフラストラクチャ設定を生成します")
    
    # インフラストラクチャ層を実装
    print("🔧 インフラストラクチャ層実装を開始中...")
    created_files = implement_infrastructure_layer(use_case_data, issue_number, repository_interfaces)
    
    print(f"✅ インフラストラクチャ層実装完了: {len(created_files)}個のファイル作成")
    
    # ユースケースJSONにインフラストラクチャ層情報を更新
    print("📊 ユースケースJSONを更新中...")
    updated_data = update_use_case_json_with_infrastructure(json_file_path, created_files)
    
    # 実行履歴を更新
    update_execution_history(
        json_file_path,
        f"/implement-infra {issue_number}",
        "success",
        created_files
    )
    
    # 最新データを読み込んで表示
    final_data = load_use_case_json(json_file_path)
    
    # 実行状況を表示
    print("\n" + "="*60)
    print(format_execution_status(final_data))
    print("="*60)
    
    # サマリー表示
    print(f"\n📊 実行サマリー")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"🏗️ インフラストラクチャ層実装: 完了")
    print(f"✅ リポジトリ実装数: {len(repository_interfaces)}個")
    print(f"✅ 作成ファイル数: {len(created_files)}個")
    print(f"✅ データベース設定: 完了")
    print(f"✅ 外部サービス統合: 準備完了")
    
    print(f"\n📁 成果物")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    for file_path in created_files:
        print(f"✅ {file_path}")
    
    print(f"\n⏭️ 次の推奨コマンド")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"1. /implement-presentation {issue_number}")
    print(f"   → プレゼンテーション層実装（API/UI層）")
    print(f"2. データベース接続設定の確認")
    print(f"   → DATABASE_URL等の環境変数設定")
    print(f"3. 外部APIキーの設定")
    print(f"   → EXTERNAL_API_KEY等の環境変数設定")
    
    print(f"\n💡 インフラストラクチャ層実装完了")
    print(f"データベース設定と外部サービス接続を確認してください。")


if __name__ == "__main__":
    main()