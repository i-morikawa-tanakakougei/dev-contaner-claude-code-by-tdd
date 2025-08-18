"""
{{ENTITY_NAME}} Entity

{{ENTITY_NAME}}エンティティの実装。
実装日時: {{IMPLEMENTATION_DATE}}
"""

from datetime import datetime
from typing import Optional
import logging
from ..value_objects.entityid import EntityId


logger = logging.getLogger(__name__)


class {{ENTITY_NAME}}:
    """{{ENTITY_NAME}}エンティティ
    
    {{ENTITY_NAME}}に関連するビジネスロジックとデータを管理する。
    不変条件を維持し、ビジネスルールを強制する責務を持つ。
    """
    
    def __init__(
        self, 
        id: str,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None
    ):
        """{{ENTITY_NAME}}エンティティ初期化
        
        Args:
            id: エンティティの一意識別子
            created_at: 作成日時
            updated_at: 更新日時
        """
        self._id = EntityId.from_string(id)
        self._created_at = created_at or datetime.now()
        self._updated_at = updated_at or datetime.now()
        
        # ビジネスルール検証
        self._validate_business_rules()
        
        logger.info(f"{{ENTITY_NAME}} entity created with ID: {self._id}")
    
    @property
    def id(self) -> str:
        """エンティティID"""
        return str(self._id)
    
    @property
    def created_at(self) -> datetime:
        """作成日時"""
        return self._created_at
    
    @property
    def updated_at(self) -> datetime:
        """更新日時"""
        return self._updated_at
    
    @classmethod
    def create(cls, entity_id: str) -> "{{ENTITY_NAME}}":
        """新しい{{ENTITY_NAME}}エンティティを作成
        
        Args:
            entity_id: エンティティの一意識別子
            
        Returns:
            {{ENTITY_NAME}}: 新しいエンティティインスタンス
        """
        logger.info(f"Creating new {{ENTITY_NAME}} with ID: {entity_id}")
        return cls(id=entity_id)
    
    def update(self) -> None:
        """エンティティの更新日時を現在時刻に更新
        
        ビジネス操作後に呼び出してエンティティの更新を記録する。
        """
        self._updated_at = datetime.now()
        self._validate_business_rules()
        logger.debug(f"{{ENTITY_NAME}} {self._id} updated at {self._updated_at}")
    
    def _validate_business_rules(self) -> None:
        """ビジネスルールの検証
        
        Raises:
            ValueError: ビジネスルールに違反する場合
        """
        # 基本的な不変条件
        if not self._id:
            raise ValueError("Entity ID cannot be empty")
        
        if self._created_at > datetime.now():
            raise ValueError("Created time cannot be in the future")
        
        if self._updated_at < self._created_at:
            raise ValueError("Updated time cannot be before created time")
        
        # TODO: 追加のビジネスルールを実装
    
    def __eq__(self, other) -> bool:
        """エンティティ同等性比較（IDベース）"""
        if not isinstance(other, {{ENTITY_NAME}}):
            return False
        return self._id == other._id
    
    def __hash__(self) -> int:
        """エンティティハッシュ（IDベース）"""
        return hash(self._id)
    
    def __repr__(self) -> str:
        """エンティティ文字列表現"""
        return f"{{ENTITY_NAME}}(id={self._id}, created_at={self._created_at})"