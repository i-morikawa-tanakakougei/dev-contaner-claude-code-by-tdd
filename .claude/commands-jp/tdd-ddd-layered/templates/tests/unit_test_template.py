"""
{{ENTITY_NAME}} Unit Tests

{{ENTITY_NAME}}エンティティの単体テスト。
実装日時: {{IMPLEMENTATION_DATE}}
"""

import pytest
from datetime import datetime
from src.domain.entities.{{ENTITY_LOWER}} import {{ENTITY_NAME}}


class Test{{ENTITY_NAME}}:
    """{{ENTITY_NAME}}エンティティの単体テスト"""
    
    def test_create_{{ENTITY_LOWER}}_with_valid_data(self):
        """有効なデータで{{ENTITY_NAME}}を作成"""
        # Given: 有効なエンティティデータ
        entity_id = "test-{{ENTITY_LOWER}}-123"
        
        # When: エンティティを作成
        entity = {{ENTITY_NAME}}.create(entity_id)
        
        # Then: 正しく作成される
        assert entity.id == entity_id
        assert isinstance(entity.created_at, datetime)
        assert isinstance(entity.updated_at, datetime)
        assert entity.created_at <= entity.updated_at
    
    def test_create_{{ENTITY_LOWER}}_with_empty_id(self):
        """空のIDで{{ENTITY_NAME}}作成時にエラー"""
        # When/Then: 空のIDでエンティティ作成するとエラー
        with pytest.raises(ValueError, match="Entity ID cannot be empty"):
            {{ENTITY_NAME}}.create("")
    
    def test_update_{{ENTITY_LOWER}}_timestamp(self):
        """{{ENTITY_NAME}}の更新日時が正しく更新される"""
        # Given: エンティティが作成されている
        entity = {{ENTITY_NAME}}.create("test-{{ENTITY_LOWER}}-456")
        original_updated_at = entity.updated_at
        
        # When: エンティティを更新
        entity.update()
        
        # Then: 更新日時が変更される
        assert entity.updated_at > original_updated_at
    
    def test_{{ENTITY_LOWER}}_equality(self):
        """{{ENTITY_NAME}}の同等性比較"""
        # Given: 同じIDの2つのエンティティ
        entity_id = "test-{{ENTITY_LOWER}}-789"
        entity1 = {{ENTITY_NAME}}.create(entity_id)
        entity2 = {{ENTITY_NAME}}.create(entity_id)
        
        # When/Then: 同じIDのエンティティは等しい
        assert entity1 == entity2
        
        # When/Then: 異なるIDのエンティティは等しくない
        entity3 = {{ENTITY_NAME}}.create("different-id")
        assert entity1 != entity3
    
    def test_{{ENTITY_LOWER}}_hash(self):
        """{{ENTITY_NAME}}のハッシュ値はIDベース"""
        # Given: 同じIDの2つのエンティティ
        entity_id = "test-{{ENTITY_LOWER}}-hash"
        entity1 = {{ENTITY_NAME}}.create(entity_id)
        entity2 = {{ENTITY_NAME}}.create(entity_id)
        
        # When/Then: 同じIDのエンティティは同じハッシュ値
        assert hash(entity1) == hash(entity2)
    
    def test_{{ENTITY_LOWER}}_string_representation(self):
        """{{ENTITY_NAME}}の文字列表現"""
        # Given: エンティティ
        entity_id = "test-{{ENTITY_LOWER}}-repr"
        entity = {{ENTITY_NAME}}.create(entity_id)
        
        # When: 文字列表現を取得
        repr_str = repr(entity)
        
        # Then: IDと作成日時が含まれる
        assert entity_id in repr_str
        assert "{{ENTITY_NAME}}" in repr_str
    
    def test_{{ENTITY_LOWER}}_business_rules_validation(self):
        """{{ENTITY_NAME}}のビジネスルール検証"""
        # Given: 不正な作成日時のエンティティデータ
        future_date = datetime(2100, 1, 1)
        
        # When/Then: 未来日時での作成はエラー
        with pytest.raises(ValueError, match="Created time cannot be in the future"):
            {{ENTITY_NAME}}(
                id="test-id",
                created_at=future_date,
                updated_at=datetime.now()
            )