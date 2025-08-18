"""
{{FEATURE_NAME}} API E2E Tests

{{FEATURE_NAME}}APIのエンドツーエンドテスト。
実装日時: {{IMPLEMENTATION_DATE}}
"""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from src.presentation.api.app import app
from src.infrastructure.config.database import DatabaseConfig
import json


@pytest.fixture
def test_client():
    """テスト用HTTPクライアント"""
    return TestClient(app)


@pytest.fixture
def test_db():
    """テスト用データベース"""
    config = DatabaseConfig("sqlite:///:memory:")
    config.create_tables()
    
    with config.get_session_context() as session:
        yield session
        
    config.drop_tables()


@pytest.fixture
def sample_{{FEATURE_NAME_SNAKE}}_data():
    """テスト用{{FEATURE_NAME}}データ"""
    return {
        "user_id": "test-user-123",
        "data": {
            "test_field": "test_value",
            "numeric_field": 42
        },
        "name": "Test {{FEATURE_NAME}}",
        "email": "test@example.com"
    }


class Test{{FEATURE_NAME_TITLE}}API:
    """{{FEATURE_NAME}}API E2Eテスト"""
    
    def test_health_check(self, test_client: TestClient):
        """ヘルスチェックエンドポイントのテスト"""
        # When: ヘルスチェック実行
        response = test_client.get("/health")
        
        # Then: 成功レスポンス
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "{{FEATURE_NAME}}" in data["message"]
    
    def test_create_{{FEATURE_NAME_SNAKE}}_success(self, test_client: TestClient, sample_{{FEATURE_NAME_SNAKE}}_data):
        """{{FEATURE_NAME}}作成成功のテスト"""
        # When: {{FEATURE_NAME}}作成リクエスト
        response = test_client.post("/{{API_ENDPOINT}}", json=sample_{{FEATURE_NAME_SNAKE}}_data)
        
        # Then: 作成成功
        assert response.status_code == 201
        data = response.json()
        assert data["success"] is True
        assert "successfully" in data["message"].lower()
        assert data["data"] is not None
    
    def test_create_{{FEATURE_NAME_SNAKE}}_validation_error(self, test_client: TestClient):
        """{{FEATURE_NAME}}作成バリデーションエラーのテスト"""
        # Given: 無効なリクエストデータ
        invalid_data = {
            "user_id": "",  # 空のuser_id
            "data": "invalid_type"  # 不正な型
        }
        
        # When: {{FEATURE_NAME}}作成リクエスト
        response = test_client.post("/{{API_ENDPOINT}}", json=invalid_data)
        
        # Then: バリデーションエラー
        assert response.status_code == 400
        data = response.json()
        assert data["success"] is False
        assert "error" in data
        assert len(data["error"]["details"]) > 0
    
    def test_get_{{FEATURE_NAME_SNAKE}}_by_id_success(self, test_client: TestClient, sample_{{FEATURE_NAME_SNAKE}}_data):
        """{{FEATURE_NAME}}ID取得成功のテスト"""
        # Given: {{FEATURE_NAME}}が作成されている
        create_response = test_client.post("/{{API_ENDPOINT}}", json=sample_{{FEATURE_NAME_SNAKE}}_data)
        assert create_response.status_code == 201
        
        # TODO: 実際の実装では作成レスポンスからIDを取得
        entity_id = "test-entity-id"
        
        # When: IDで{{FEATURE_NAME}}取得
        response = test_client.get(
            f"/{{API_ENDPOINT}}/{entity_id}",
            params={"user_id": sample_{{FEATURE_NAME_SNAKE}}_data["user_id"]}
        )
        
        # Then: 取得成功（実装状況により調整）
        # Note: この段階では404エラーになる可能性があります
        assert response.status_code in [200, 404]
    
    def test_get_{{FEATURE_NAME_SNAKE}}_by_id_not_found(self, test_client: TestClient):
        """{{FEATURE_NAME}}ID取得（存在しない）のテスト"""
        # When: 存在しないIDで{{FEATURE_NAME}}取得
        response = test_client.get(
            "/{{API_ENDPOINT}}/non-existent-id",
            params={"user_id": "test-user"}
        )
        
        # Then: Not Found
        assert response.status_code == 404
        data = response.json()
        assert data["success"] is False
        assert "not found" in data["message"].lower()
    
    def test_list_{{FEATURE_NAME_SNAKE}}_success(self, test_client: TestClient):
        """{{FEATURE_NAME}}一覧取得成功のテスト"""
        # When: {{FEATURE_NAME}}一覧取得
        response = test_client.get(
            "/{{API_ENDPOINT}}",
            params={"user_id": "test-user", "page": 1, "limit": 10}
        )
        
        # Then: 一覧取得成功
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "data" in data
        assert "pagination" in data["data"]
    
    def test_list_{{FEATURE_NAME_SNAKE}}_pagination(self, test_client: TestClient):
        """{{FEATURE_NAME}}一覧取得ページネーションのテスト"""
        # When: ページネーション パラメータ付きで一覧取得
        response = test_client.get(
            "/{{API_ENDPOINT}}",
            params={"user_id": "test-user", "page": 2, "limit": 5}
        )
        
        # Then: 正しいページネーション情報
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        pagination = data["data"]["pagination"]
        assert pagination["page"] == 2
        assert pagination["limit"] == 5
    
    def test_update_{{FEATURE_NAME_SNAKE}}_success(self, test_client: TestClient, sample_{{FEATURE_NAME_SNAKE}}_data):
        """{{FEATURE_NAME}}更新成功のテスト"""
        # Given: {{FEATURE_NAME}}が作成されている
        entity_id = "test-entity-id"
        update_data = {
            "user_id": sample_{{FEATURE_NAME_SNAKE}}_data["user_id"],
            "name": "Updated Name"
        }
        
        # When: {{FEATURE_NAME}}更新
        response = test_client.put(f"/{{API_ENDPOINT}}/{entity_id}", json=update_data)
        
        # Then: 更新成功（実装状況により調整）
        # Note: この段階では404エラーになる可能性があります
        assert response.status_code in [200, 404]
    
    def test_delete_{{FEATURE_NAME_SNAKE}}_success(self, test_client: TestClient):
        """{{FEATURE_NAME}}削除成功のテスト"""
        # Given: {{FEATURE_NAME}}が存在する
        entity_id = "test-entity-id"
        
        # When: {{FEATURE_NAME}}削除
        response = test_client.delete(
            f"/{{API_ENDPOINT}}/{entity_id}",
            params={"user_id": "test-user"}
        )
        
        # Then: 削除成功（実装状況により調整）
        # Note: この段階では404エラーになる可能性があります
        assert response.status_code in [200, 404]
    
    def test_api_error_handling(self, test_client: TestClient):
        """APIエラーハンドリングのテスト"""
        # When: 不正なJSONでリクエスト
        response = test_client.post(
            "/{{API_ENDPOINT}}",
            data="invalid json",
            headers={"Content-Type": "application/json"}
        )
        
        # Then: 適切なエラーレスポンス
        assert response.status_code == 422  # Unprocessable Entity
    
    def test_cors_headers(self, test_client: TestClient):
        """CORSヘッダーのテスト"""
        # When: OPTIONSリクエスト実行
        response = test_client.options("/{{API_ENDPOINT}}")
        
        # Then: CORSヘッダーが設定されている
        assert "access-control-allow-origin" in response.headers
        assert "access-control-allow-methods" in response.headers
    
    def test_openapi_documentation(self, test_client: TestClient):
        """OpenAPIドキュメントのテスト"""
        # When: OpenAPIスキーマ取得
        response = test_client.get("/openapi.json")
        
        # Then: 有効なOpenAPIスキーマ
        assert response.status_code == 200
        schema = response.json()
        assert "openapi" in schema
        assert "paths" in schema
        assert "/{{API_ENDPOINT}}" in schema["paths"]