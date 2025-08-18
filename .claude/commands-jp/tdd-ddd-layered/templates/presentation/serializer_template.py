"""
{{FEATURE_NAME}} API Serializers

API レスポンスデータのシリアライゼーション処理。
実装日時: {{IMPLEMENTATION_DATE}}
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
from src.application.dtos.{{FEATURE_NAME_SNAKE}}_dtos import (
    {{FEATURE_NAME_TITLE}}Response,
    {{FEATURE_NAME_TITLE}}ListResponse
)


class {{FEATURE_NAME_TITLE}}Serializer:
    """{{FEATURE_NAME}}APIシリアライザー
    
    アプリケーション層のDTOをAPI レスポンス形式に変換する。
    """
    
    @staticmethod
    def serialize_response(response: {{FEATURE_NAME_TITLE}}Response) -> Dict[str, Any]:
        """単一レスポンスのシリアライゼーション
        
        Args:
            response: アプリケーション層のレスポンスDTO
            
        Returns:
            Dict[str, Any]: JSON シリアライズ可能な辞書
        """
        return {
            "success": response.success,
            "message": response.message,
            "data": response.data,
            "timestamp": response.timestamp.isoformat() if response.timestamp else None,
            "meta": {
                "version": "1.0",
                "request_id": None  # TODO: リクエストIDトラッキング
            }
        }
    
    @staticmethod
    def serialize_list_response(response: {{FEATURE_NAME_TITLE}}ListResponse) -> Dict[str, Any]:
        """一覧レスポンスのシリアライゼーション
        
        Args:
            response: アプリケーション層の一覧レスポンスDTO
            
        Returns:
            Dict[str, Any]: JSON シリアライズ可能な辞書
        """
        return {
            "success": response.success,
            "message": response.message,
            "data": {
                "items": response.items,
                "pagination": {
                    "page": response.page,
                    "limit": response.limit,
                    "total_count": response.total_count,
                    "has_more": response.has_more,
                    "total_pages": (response.total_count + response.limit - 1) // response.limit
                }
            },
            "meta": {
                "version": "1.0",
                "request_id": None  # TODO: リクエストIDトラッキング
            }
        }
    
    @staticmethod
    def serialize_error_response(
        message: str, 
        errors: Optional[List[str]] = None,
        error_code: Optional[str] = None,
        status_code: int = 400
    ) -> Dict[str, Any]:
        """エラーレスポンスのシリアライゼーション
        
        Args:
            message: エラーメッセージ
            errors: 詳細エラーリスト
            error_code: エラーコード
            status_code: HTTPステータスコード
            
        Returns:
            Dict[str, Any]: JSON シリアライズ可能な辞書
        """
        return {
            "success": False,
            "message": message,
            "data": None,
            "error": {
                "code": error_code or f"{{FEATURE_NAME_TITLE}}_ERROR",
                "details": errors or [],
                "status_code": status_code
            },
            "timestamp": datetime.now().isoformat(),
            "meta": {
                "version": "1.0",
                "request_id": None  # TODO: リクエストIDトラッキング
            }
        }
    
    @staticmethod
    def serialize_validation_error_response(
        validation_error: Exception,
        status_code: int = 400
    ) -> Dict[str, Any]:
        """バリデーションエラーレスポンスのシリアライゼーション
        
        Args:
            validation_error: バリデーションエラー
            status_code: HTTPステータスコード
            
        Returns:
            Dict[str, Any]: JSON シリアライズ可能な辞書
        """
        errors = []
        error_message = str(validation_error)
        
        # バリデーションエラーの詳細抽出
        if hasattr(validation_error, 'errors'):
            errors = validation_error.errors
        elif hasattr(validation_error, 'detail'):
            errors = [validation_error.detail]
        
        return {{FEATURE_NAME_TITLE}}Serializer.serialize_error_response(
            message=error_message,
            errors=errors,
            error_code="VALIDATION_ERROR",
            status_code=status_code
        )
    
    @staticmethod
    def serialize_not_found_response(entity_id: str) -> Dict[str, Any]:
        """Not Found エラーレスポンスのシリアライゼーション
        
        Args:
            entity_id: 見つからなかったエンティティのID
            
        Returns:
            Dict[str, Any]: JSON シリアライズ可能な辞書
        """
        return {{FEATURE_NAME_TITLE}}Serializer.serialize_error_response(
            message=f"{{FEATURE_NAME}} not found: {entity_id}",
            error_code="NOT_FOUND",
            status_code=404
        )
    
    @staticmethod
    def serialize_authorization_error_response() -> Dict[str, Any]:
        """認可エラーレスポンスのシリアライゼーション
        
        Returns:
            Dict[str, Any]: JSON シリアライズ可能な辞書
        """
        return {{FEATURE_NAME_TITLE}}Serializer.serialize_error_response(
            message="Insufficient permissions",
            error_code="AUTHORIZATION_ERROR",
            status_code=403
        )
    
    @staticmethod
    def serialize_server_error_response() -> Dict[str, Any]:
        """サーバーエラーレスポンスのシリアライゼーション
        
        Returns:
            Dict[str, Any]: JSON シリアライズ可能な辞書
        """
        return {{FEATURE_NAME_TITLE}}Serializer.serialize_error_response(
            message="Internal server error",
            error_code="INTERNAL_SERVER_ERROR",
            status_code=500
        )
    
    @staticmethod
    def serialize_health_check_response() -> Dict[str, Any]:
        """ヘルスチェックレスポンスのシリアライゼーション
        
        Returns:
            Dict[str, Any]: JSON シリアライズ可能な辞書
        """
        return {
            "success": True,
            "message": "{{FEATURE_NAME}} API is healthy",
            "data": {
                "status": "healthy",
                "timestamp": datetime.now().isoformat(),
                "version": "1.0"
            },
            "meta": {
                "version": "1.0",
                "service": "{{FEATURE_NAME}}"
            }
        }