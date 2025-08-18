"""
{{ENTITY_NAME}} Entity-Model Mapper

{{ENTITY_NAME}}エンティティとデータベースモデル間の変換処理。
実装日時: {{IMPLEMENTATION_DATE}}
"""

from typing import Optional
from datetime import datetime
from src.domain.entities.{{ENTITY_LOWER}} import {{ENTITY_NAME}}
from src.domain.value_objects.entityid import EntityId
from ..models.{{ENTITY_LOWER}}_model import {{ENTITY_NAME}}Model


class {{ENTITY_NAME}}Mapper:
    """{{ENTITY_NAME}}エンティティ・モデルマッパー
    
    ドメインエンティティとデータベースモデル間の双方向変換を提供する。
    """
    
    @staticmethod
    def to_model(entity: {{ENTITY_NAME}}) -> {{ENTITY_NAME}}Model:
        """ドメインエンティティをデータベースモデルに変換
        
        Args:
            entity: {{ENTITY_NAME}}ドメインエンティティ
            
        Returns:
            {{ENTITY_NAME}}Model: データベースモデル
        """
        return {{ENTITY_NAME}}Model(
            id=entity.id,
            name=getattr(entity, 'name', None),  # TODO: 実際の属性に合わせて修正
            description=getattr(entity, 'description', None),
            status=getattr(entity, 'status', None),
            data=getattr(entity, 'data', None),
            is_active=getattr(entity, 'is_active', True),
            created_at=entity.created_at,
            updated_at=entity.updated_at
        )
    
    @staticmethod
    def to_entity(model: {{ENTITY_NAME}}Model) -> {{ENTITY_NAME}}:
        """データベースモデルをドメインエンティティに変換
        
        Args:
            model: {{ENTITY_NAME}}データベースモデル
            
        Returns:
            {{ENTITY_NAME}}: ドメインエンティティ
        """
        # TODO: 実際のエンティティコンストラクタに合わせて修正
        entity = {{ENTITY_NAME}}(
            id=model.id,
            created_at=model.created_at,
            updated_at=model.updated_at
        )
        
        # 追加属性の設定（エンティティの実装に依存）
        if hasattr(entity, 'name') and model.name:
            entity.name = model.name
        if hasattr(entity, 'description') and model.description:
            entity.description = model.description
        if hasattr(entity, 'status') and model.status:
            entity.status = model.status
        if hasattr(entity, 'data') and model.data:
            entity.data = model.data
        if hasattr(entity, 'is_active'):
            entity.is_active = model.is_active
        
        return entity
    
    @staticmethod
    def update_model_from_entity(model: {{ENTITY_NAME}}Model, entity: {{ENTITY_NAME}}) -> {{ENTITY_NAME}}Model:
        """既存のデータベースモデルをエンティティの値で更新
        
        Args:
            model: 更新対象のデータベースモデル
            entity: 更新元のドメインエンティティ
            
        Returns:
            {{ENTITY_NAME}}Model: 更新されたデータベースモデル
        """
        # IDと作成日時は変更しない
        if hasattr(entity, 'name'):
            model.name = getattr(entity, 'name', model.name)
        if hasattr(entity, 'description'):
            model.description = getattr(entity, 'description', model.description)
        if hasattr(entity, 'status'):
            model.status = getattr(entity, 'status', model.status)
        if hasattr(entity, 'data'):
            model.data = getattr(entity, 'data', model.data)
        if hasattr(entity, 'is_active'):
            model.is_active = getattr(entity, 'is_active', model.is_active)
        
        model.updated_at = entity.updated_at
        
        return model
    
    @staticmethod
    def create_entity_id(model_id: str) -> EntityId:
        """モデルIDからエンティティIDを作成
        
        Args:
            model_id: データベースモデルのID
            
        Returns:
            EntityId: エンティティID値オブジェクト
        """
        return EntityId.from_string(model_id)