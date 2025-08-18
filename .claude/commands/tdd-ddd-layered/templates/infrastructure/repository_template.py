"""
SQL {{ENTITY_NAME}} Repository Implementation

SQLAlchemyを使用した{{ENTITY_NAME}}リポジトリの具象実装。
実装日時: {{IMPLEMENTATION_DATE}}
"""

from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
import logging

from src.domain.entities.{{ENTITY_LOWER}} import {{ENTITY_NAME}}
from src.domain.repositories.{{ENTITY_LOWER}}_repository import {{ENTITY_NAME}}Repository, RepositoryError
from ..persistence.models.{{ENTITY_LOWER}}_model import {{ENTITY_NAME}}Model
from ..persistence.mappers.{{ENTITY_LOWER}}_mapper import {{ENTITY_NAME}}Mapper


logger = logging.getLogger(__name__)


class Sql{{ENTITY_NAME}}Repository({{ENTITY_NAME}}Repository):
    """SQL {{ENTITY_NAME}}リポジトリ
    
    SQLAlchemyを使用した{{ENTITY_NAME}}エンティティの永続化実装。
    """
    
    def __init__(self, session: Session):
        """SQLリポジトリ初期化
        
        Args:
            session: SQLAlchemyセッション
        """
        self._session = session
        self._mapper = {{ENTITY_NAME}}Mapper()
        logger.info("Sql{{ENTITY_NAME}}Repository initialized")
    
    def save(self, entity: {{ENTITY_NAME}}) -> None:
        """{{ENTITY_NAME}}を保存する
        
        Args:
            entity: 保存する{{ENTITY_NAME}}エンティティ
            
        Raises:
            RepositoryError: 保存に失敗した場合
        """
        try:
            logger.debug(f"Saving {{ENTITY_NAME}} with ID: {entity.id}")
            
            # 既存のモデルを検索
            existing_model = self._session.query({{ENTITY_NAME}}Model).filter_by(id=entity.id).first()
            
            if existing_model:
                # 既存モデルの更新
                self._mapper.update_model_from_entity(existing_model, entity)
                logger.debug(f"Updated existing {{ENTITY_NAME}} model: {entity.id}")
            else:
                # 新規モデルの作成
                model = self._mapper.to_model(entity)
                self._session.add(model)
                logger.debug(f"Created new {{ENTITY_NAME}} model: {entity.id}")
            
            self._session.flush()  # DB制約チェックのために即座に反映
            logger.info(f"{{ENTITY_NAME}} saved successfully: {entity.id}")
            
        except SQLAlchemyError as e:
            logger.error(f"Database error saving {{ENTITY_NAME}} {entity.id}: {e}")
            self._session.rollback()
            raise RepositoryError(f"Failed to save {{ENTITY_NAME}}: {e}")
        except Exception as e:
            logger.error(f"Unexpected error saving {{ENTITY_NAME}} {entity.id}: {e}")
            self._session.rollback()
            raise RepositoryError(f"Unexpected error saving {{ENTITY_NAME}}: {e}")
    
    def find_by_id(self, entity_id: str) -> Optional[{{ENTITY_NAME}}]:
        """IDで{{ENTITY_NAME}}を検索する
        
        Args:
            entity_id: 検索するエンティティのID
            
        Returns:
            Optional[{{ENTITY_NAME}}]: 見つかった{{ENTITY_NAME}}、または None
            
        Raises:
            RepositoryError: 検索に失敗した場合
        """
        try:
            logger.debug(f"Finding {{ENTITY_NAME}} by ID: {entity_id}")
            
            model = self._session.query({{ENTITY_NAME}}Model).filter_by(id=entity_id).first()
            
            if model:
                entity = self._mapper.to_entity(model)
                logger.debug(f"Found {{ENTITY_NAME}}: {entity_id}")
                return entity
            else:
                logger.debug(f"{{ENTITY_NAME}} not found: {entity_id}")
                return None
                
        except SQLAlchemyError as e:
            logger.error(f"Database error finding {{ENTITY_NAME}} {entity_id}: {e}")
            raise RepositoryError(f"Failed to find {{ENTITY_NAME}} by ID {entity_id}: {e}")
        except Exception as e:
            logger.error(f"Unexpected error finding {{ENTITY_NAME}} {entity_id}: {e}")
            raise RepositoryError(f"Unexpected error finding {{ENTITY_NAME}} {entity_id}: {e}")
    
    def find_all(self) -> List[{{ENTITY_NAME}}]:
        """すべての{{ENTITY_NAME}}を取得する
        
        Returns:
            List[{{ENTITY_NAME}}]: すべての{{ENTITY_NAME}}のリスト
            
        Raises:
            RepositoryError: 取得に失敗した場合
        """
        try:
            logger.debug("Finding all {{ENTITY_NAME}}s")
            
            models = self._session.query({{ENTITY_NAME}}Model).filter_by(is_active=True).all()
            entities = [self._mapper.to_entity(model) for model in models]
            
            logger.info(f"Found {len(entities)} {{ENTITY_NAME}}s")
            return entities
            
        except SQLAlchemyError as e:
            logger.error(f"Database error finding all {{ENTITY_NAME}}s: {e}")
            raise RepositoryError(f"Failed to find all {{ENTITY_NAME}}s: {e}")
        except Exception as e:
            logger.error(f"Unexpected error finding all {{ENTITY_NAME}}s: {e}")
            raise RepositoryError(f"Unexpected error finding all {{ENTITY_NAME}}s: {e}")
    
    def delete(self, entity_id: str) -> bool:
        """{{ENTITY_NAME}}を削除する（論理削除）
        
        Args:
            entity_id: 削除するエンティティのID
            
        Returns:
            bool: 削除に成功した場合True、エンティティが見つからない場合False
            
        Raises:
            RepositoryError: 削除に失敗した場合
        """
        try:
            logger.debug(f"Deleting {{ENTITY_NAME}}: {entity_id}")
            
            model = self._session.query({{ENTITY_NAME}}Model).filter_by(id=entity_id).first()
            
            if model:
                # 論理削除（物理削除ではなくフラグを変更）
                model.is_active = False
                self._session.flush()
                logger.info(f"{{ENTITY_NAME}} deleted (logical): {entity_id}")
                return True
            else:
                logger.debug(f"{{ENTITY_NAME}} not found for deletion: {entity_id}")
                return False
                
        except SQLAlchemyError as e:
            logger.error(f"Database error deleting {{ENTITY_NAME}} {entity_id}: {e}")
            self._session.rollback()
            raise RepositoryError(f"Failed to delete {{ENTITY_NAME}} {entity_id}: {e}")
        except Exception as e:
            logger.error(f"Unexpected error deleting {{ENTITY_NAME}} {entity_id}: {e}")
            self._session.rollback()
            raise RepositoryError(f"Unexpected error deleting {{ENTITY_NAME}} {entity_id}: {e}")
    
    def exists(self, entity_id: str) -> bool:
        """{{ENTITY_NAME}}が存在するかチェックする
        
        Args:
            entity_id: チェックするエンティティのID
            
        Returns:
            bool: エンティティが存在する場合True
            
        Raises:
            RepositoryError: チェックに失敗した場合
        """
        try:
            logger.debug(f"Checking existence of {{ENTITY_NAME}}: {entity_id}")
            
            exists = self._session.query({{ENTITY_NAME}}Model).filter_by(
                id=entity_id, 
                is_active=True
            ).first() is not None
            
            logger.debug(f"{{ENTITY_NAME}} {entity_id} exists: {exists}")
            return exists
            
        except SQLAlchemyError as e:
            logger.error(f"Database error checking {{ENTITY_NAME}} existence {entity_id}: {e}")
            raise RepositoryError(f"Failed to check existence of {{ENTITY_NAME}} {entity_id}: {e}")
        except Exception as e:
            logger.error(f"Unexpected error checking {{ENTITY_NAME}} existence {entity_id}: {e}")
            raise RepositoryError(f"Unexpected error checking {{ENTITY_NAME}} existence {entity_id}: {e}")