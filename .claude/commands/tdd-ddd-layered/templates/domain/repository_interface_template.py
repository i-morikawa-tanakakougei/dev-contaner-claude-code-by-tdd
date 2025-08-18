"""
{{ENTITY_NAME}} Repository Interface

{{ENTITY_NAME}}エンティティの永続化インターフェース定義。
実装日時: {{IMPLEMENTATION_DATE}}
"""

from abc import ABC, abstractmethod
from typing import List, Optional
from .{{ENTITY_LOWER}}.{{ENTITY_LOWER}} import {{ENTITY_NAME}}


class RepositoryError(Exception):
    """リポジトリ操作エラーの基底例外"""
    pass


class {{ENTITY_NAME}}Repository(ABC):
    """{{ENTITY_NAME}}リポジトリインターフェース
    
    {{ENTITY_NAME}}エンティティの永続化操作を定義する。
    具体的な実装は実装者に委ねられる。
    """
    
    @abstractmethod
    def save(self, entity: {{ENTITY_NAME}}) -> None:
        """{{ENTITY_NAME}}を保存する
        
        Args:
            entity: 保存する{{ENTITY_NAME}}エンティティ
            
        Raises:
            RepositoryError: 保存に失敗した場合
        """
        pass
    
    @abstractmethod
    def find_by_id(self, entity_id: str) -> Optional[{{ENTITY_NAME}}]:
        """IDで{{ENTITY_NAME}}を検索する
        
        Args:
            entity_id: 検索するエンティティのID
            
        Returns:
            Optional[{{ENTITY_NAME}}]: 見つかった{{ENTITY_NAME}}、または None
            
        Raises:
            RepositoryError: 検索に失敗した場合
        """
        pass
    
    @abstractmethod
    def find_all(self) -> List[{{ENTITY_NAME}}]:
        """すべての{{ENTITY_NAME}}を取得する
        
        Returns:
            List[{{ENTITY_NAME}}]: すべての{{ENTITY_NAME}}のリスト
            
        Raises:
            RepositoryError: 取得に失敗した場合
        """
        pass
    
    @abstractmethod
    def delete(self, entity_id: str) -> bool:
        """{{ENTITY_NAME}}を削除する
        
        Args:
            entity_id: 削除するエンティティのID
            
        Returns:
            bool: 削除に成功した場合True、エンティティが見つからない場合False
            
        Raises:
            RepositoryError: 削除に失敗した場合
        """
        pass
    
    @abstractmethod
    def exists(self, entity_id: str) -> bool:
        """{{ENTITY_NAME}}が存在するかチェックする
        
        Args:
            entity_id: チェックするエンティティのID
            
        Returns:
            bool: エンティティが存在する場合True
            
        Raises:
            RepositoryError: チェックに失敗した場合
        """
        pass