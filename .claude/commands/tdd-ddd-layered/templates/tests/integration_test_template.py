"""
SQL {{ENTITY_NAME}} Repository Integration Tests

SQLAlchemy{{ENTITY_NAME}}リポジトリの統合テスト。
実装日時: {{IMPLEMENTATION_DATE}}
"""

import pytest
from sqlalchemy.orm import Session
from src.domain.entities.{{ENTITY_LOWER}} import {{ENTITY_NAME}}
from src.infrastructure.repositories.sql_{{ENTITY_LOWER}}_repository import Sql{{ENTITY_NAME}}Repository
from src.infrastructure.config.database import DatabaseConfig
from src.infrastructure.persistence.models.{{ENTITY_LOWER}}_model import {{ENTITY_NAME}}Model


@pytest.fixture
def db_session():
    """テスト用データベースセッション"""
    config = DatabaseConfig("sqlite:///:memory:")
    config.create_tables()
    
    with config.get_session_context() as session:
        yield session
        
    config.drop_tables()


@pytest.fixture
def repository(db_session: Session):
    """{{ENTITY_NAME}}リポジトリインスタンス"""
    return Sql{{ENTITY_NAME}}Repository(db_session)


@pytest.fixture
def sample_entity():
    """テスト用{{ENTITY_NAME}}エンティティ"""
    return {{ENTITY_NAME}}.create("test-entity-id")


class TestSql{{ENTITY_NAME}}Repository:
    """SQL{{ENTITY_NAME}}Repository統合テスト"""
    
    def test_save_new_entity(self, repository: Sql{{ENTITY_NAME}}Repository, sample_entity: {{ENTITY_NAME}}, db_session: Session):
        """新しいエンティティの保存"""
        # When: エンティティを保存
        repository.save(sample_entity)
        db_session.commit()
        
        # Then: データベースに保存されている
        model = db_session.query({{ENTITY_NAME}}Model).filter_by(id=sample_entity.id).first()
        assert model is not None
        assert model.id == sample_entity.id
        assert model.is_active is True
    
    def test_save_existing_entity(self, repository: Sql{{ENTITY_NAME}}Repository, sample_entity: {{ENTITY_NAME}}, db_session: Session):
        """既存エンティティの更新"""
        # Given: エンティティが既に保存されている
        repository.save(sample_entity)
        db_session.commit()
        
        # When: エンティティを更新して再保存
        sample_entity.update()
        repository.save(sample_entity)
        db_session.commit()
        
        # Then: データベースで更新されている
        model = db_session.query({{ENTITY_NAME}}Model).filter_by(id=sample_entity.id).first()
        assert model is not None
        assert model.updated_at > model.created_at
    
    def test_find_by_id_existing(self, repository: Sql{{ENTITY_NAME}}Repository, sample_entity: {{ENTITY_NAME}}, db_session: Session):
        """存在するエンティティのID検索"""
        # Given: エンティティが保存されている
        repository.save(sample_entity)
        db_session.commit()
        
        # When: IDで検索
        found_entity = repository.find_by_id(sample_entity.id)
        
        # Then: エンティティが見つかる
        assert found_entity is not None
        assert found_entity.id == sample_entity.id
    
    def test_find_by_id_not_existing(self, repository: Sql{{ENTITY_NAME}}Repository):
        """存在しないエンティティのID検索"""
        # When: 存在しないIDで検索
        found_entity = repository.find_by_id("non-existent-id")
        
        # Then: Noneが返される
        assert found_entity is None
    
    def test_find_all(self, repository: Sql{{ENTITY_NAME}}Repository, db_session: Session):
        """全エンティティの取得"""
        # Given: 複数のエンティティが保存されている
        entity1 = {{ENTITY_NAME}}.create("entity-1")
        entity2 = {{ENTITY_NAME}}.create("entity-2")
        repository.save(entity1)
        repository.save(entity2)
        db_session.commit()
        
        # When: 全エンティティを取得
        entities = repository.find_all()
        
        # Then: 保存されたエンティティが取得される
        assert len(entities) == 2
        entity_ids = [e.id for e in entities]
        assert "entity-1" in entity_ids
        assert "entity-2" in entity_ids
    
    def test_delete_existing_entity(self, repository: Sql{{ENTITY_NAME}}Repository, sample_entity: {{ENTITY_NAME}}, db_session: Session):
        """存在するエンティティの削除"""
        # Given: エンティティが保存されている
        repository.save(sample_entity)
        db_session.commit()
        
        # When: エンティティを削除
        result = repository.delete(sample_entity.id)
        db_session.commit()
        
        # Then: 論理削除され、find_allで取得されない
        assert result is True
        entities = repository.find_all()
        assert len(entities) == 0
        
        # But: 物理的にはデータベースに存在する（論理削除）
        model = db_session.query({{ENTITY_NAME}}Model).filter_by(id=sample_entity.id).first()
        assert model is not None
        assert model.is_active is False
    
    def test_delete_non_existing_entity(self, repository: Sql{{ENTITY_NAME}}Repository):
        """存在しないエンティティの削除"""
        # When: 存在しないエンティティを削除
        result = repository.delete("non-existent-id")
        
        # Then: Falseが返される
        assert result is False
    
    def test_exists_existing_entity(self, repository: Sql{{ENTITY_NAME}}Repository, sample_entity: {{ENTITY_NAME}}, db_session: Session):
        """存在するエンティティの存在チェック"""
        # Given: エンティティが保存されている
        repository.save(sample_entity)
        db_session.commit()
        
        # When: 存在チェック
        exists = repository.exists(sample_entity.id)
        
        # Then: Trueが返される
        assert exists is True
    
    def test_exists_non_existing_entity(self, repository: Sql{{ENTITY_NAME}}Repository):
        """存在しないエンティティの存在チェック"""
        # When: 存在しないエンティティの存在チェック
        exists = repository.exists("non-existent-id")
        
        # Then: Falseが返される
        assert exists is False