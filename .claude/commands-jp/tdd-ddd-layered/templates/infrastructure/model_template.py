"""
{{ENTITY_NAME}} Database Model

{{ENTITY_NAME}}エンティティのデータベースモデル定義。
実装日時: {{IMPLEMENTATION_DATE}}
"""

from sqlalchemy import Column, String, Text, Boolean, JSON
from .base import BaseModel


class {{ENTITY_NAME}}Model(BaseModel):
    """{{ENTITY_NAME}}データベースモデル
    
    {{ENTITY_NAME}}エンティティのデータベース永続化のためのSQLAlchemyモデル。
    """
    
    __tablename__ = "{{TABLE_NAME}}"
    
    # TODO: 実際のビジネス要件に基づいて適切なカラムを追加
    name = Column(String(255), nullable=True, comment="{{ENTITY_NAME}}名")
    description = Column(Text, nullable=True, comment="説明")
    status = Column(String(50), nullable=True, comment="ステータス")
    data = Column(JSON, nullable=True, comment="追加データ（JSON形式）")
    is_active = Column(Boolean, default=True, nullable=False, comment="アクティブフラグ")
    
    def __repr__(self) -> str:
        return f"<{{ENTITY_NAME}}Model(id={self.id}, name={self.name})>"
    
    @classmethod
    def create_table_sql(cls) -> str:
        """テーブル作成SQL生成（参考用）"""
        return f"""
        CREATE TABLE {cls.__tablename__} (
            id VARCHAR(36) PRIMARY KEY COMMENT '一意識別子（UUID）',
            name VARCHAR(255) COMMENT '{{ENTITY_NAME}}名',
            description TEXT COMMENT '説明',
            status VARCHAR(50) COMMENT 'ステータス',
            data JSON COMMENT '追加データ（JSON形式）',
            is_active BOOLEAN DEFAULT TRUE NOT NULL COMMENT 'アクティブフラグ',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL COMMENT '作成日時',
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL COMMENT '更新日時'
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
        """