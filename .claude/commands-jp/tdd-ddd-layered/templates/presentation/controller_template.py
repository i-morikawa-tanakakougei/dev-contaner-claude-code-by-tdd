"""
{{FEATURE_NAME}} API Controller

{{FEATURE_NAME}}機能のAPI エンドポイント制御。
実装日時: {{IMPLEMENTATION_DATE}}
"""

from typing import Dict, Any
import logging
from src.application.use_cases.{{FEATURE_NAME_SNAKE}}_use_case import {{FEATURE_NAME_TITLE}}UseCase
from src.application.dtos.{{FEATURE_NAME_SNAKE}}_dtos import (
    {{FEATURE_NAME_TITLE}}Request,
    {{FEATURE_NAME_TITLE}}ListRequest
)
from src.application.exceptions.{{FEATURE_NAME_SNAKE}}_exceptions import (
    {{FEATURE_NAME_TITLE}}ValidationError,
    {{FEATURE_NAME_TITLE}}NotFoundError,
    {{FEATURE_NAME_TITLE}}AuthorizationError,
    {{FEATURE_NAME_TITLE}}BusinessRuleViolationError
)
from ..validators.{{FEATURE_NAME_SNAKE}}_validator import {{FEATURE_NAME_TITLE}}Validator, {{FEATURE_NAME_TITLE}}ValidationError as APIValidationError
from ..serializers.{{FEATURE_NAME_SNAKE}}_serializer import {{FEATURE_NAME_TITLE}}Serializer


logger = logging.getLogger(__name__)


class {{FEATURE_NAME_TITLE}}Controller:
    """{{FEATURE_NAME}}APIコントローラー
    
    {{FEATURE_NAME}}機能のHTTP リクエスト処理を行う。
    ビジネスロジックは含まず、リクエスト・レスポンスの変換のみを担当。
    """
    
    def __init__(self, use_case: {{FEATURE_NAME_TITLE}}UseCase):
        """コントローラー初期化
        
        Args:
            use_case: {{FEATURE_NAME}}ユースケース
        """
        self._use_case = use_case
        logger.info("{{FEATURE_NAME_TITLE}}Controller initialized")
    
    def handle_create(self, request_data: Dict[str, Any]) -> Dict[str, Any]:
        """{{FEATURE_NAME}}作成リクエストの処理
        
        Args:
            request_data: HTTP リクエストデータ
            
        Returns:
            Dict[str, Any]: HTTP レスポンスデータ
        """
        try:
            logger.info("Handling {{FEATURE_NAME}} create request")
            
            # 1. 入力バリデーション
            validated_data = {{FEATURE_NAME_TITLE}}Validator.validate_create_request(request_data)
            
            # 2. DTO変換
            request_dto = {{FEATURE_NAME_TITLE}}Request(**validated_data)
            
            # 3. ユースケース実行
            response_dto = self._use_case.execute(request_dto)
            
            # 4. レスポンスシリアライゼーション
            response_data = {{FEATURE_NAME_TITLE}}Serializer.serialize_response(response_dto)
            
            logger.info("{{FEATURE_NAME}} create request handled successfully")
            return response_data
            
        except APIValidationError as e:
            logger.warning(f"API validation error in create: {e}")
            return {{FEATURE_NAME_TITLE}}Serializer.serialize_validation_error_response(e)
        except {{FEATURE_NAME_TITLE}}ValidationError as e:
            logger.warning(f"Application validation error in create: {e}")
            return {{FEATURE_NAME_TITLE}}Serializer.serialize_validation_error_response(e)
        except {{FEATURE_NAME_TITLE}}AuthorizationError as e:
            logger.warning(f"Authorization error in create: {e}")
            return {{FEATURE_NAME_TITLE}}Serializer.serialize_authorization_error_response()
        except {{FEATURE_NAME_TITLE}}BusinessRuleViolationError as e:
            logger.warning(f"Business rule violation in create: {e}")
            return {{FEATURE_NAME_TITLE}}Serializer.serialize_error_response(
                message=str(e),
                error_code="BUSINESS_RULE_VIOLATION",
                status_code=422
            )
        except Exception as e:
            logger.error(f"Unexpected error in create: {e}")
            return {{FEATURE_NAME_TITLE}}Serializer.serialize_server_error_response()
    
    def handle_get_by_id(self, entity_id: str, user_id: str) -> Dict[str, Any]:
        """IDによる{{FEATURE_NAME}}取得リクエストの処理
        
        Args:
            entity_id: エンティティID
            user_id: ユーザーID
            
        Returns:
            Dict[str, Any]: HTTP レスポンスデータ
        """
        try:
            logger.info(f"Handling {{FEATURE_NAME}} get by ID: {entity_id}")
            
            # 1. IDバリデーション
            validated_id = {{FEATURE_NAME_TITLE}}Validator.validate_id_parameter(entity_id)
            
            # 2. DTO作成（取得用のシンプルなリクエスト）
            request_dto = {{FEATURE_NAME_TITLE}}Request(
                user_id=user_id,
                data={"entity_id": validated_id}
            )
            
            # 3. ユースケース実行（取得ロジック）
            # Note: 実際の実装では get_by_id メソッドをユースケースに追加
            response_dto = self._use_case.execute(request_dto)
            
            # 4. レスポンスシリアライゼーション
            response_data = {{FEATURE_NAME_TITLE}}Serializer.serialize_response(response_dto)
            
            logger.info(f"{{FEATURE_NAME}} get by ID handled successfully: {entity_id}")
            return response_data
            
        except APIValidationError as e:
            logger.warning(f"API validation error in get by ID: {e}")
            return {{FEATURE_NAME_TITLE}}Serializer.serialize_validation_error_response(e)
        except {{FEATURE_NAME_TITLE}}NotFoundError as e:
            logger.warning(f"{{FEATURE_NAME}} not found: {entity_id}")
            return {{FEATURE_NAME_TITLE}}Serializer.serialize_not_found_response(entity_id)
        except {{FEATURE_NAME_TITLE}}AuthorizationError as e:
            logger.warning(f"Authorization error in get by ID: {e}")
            return {{FEATURE_NAME_TITLE}}Serializer.serialize_authorization_error_response()
        except Exception as e:
            logger.error(f"Unexpected error in get by ID: {e}")
            return {{FEATURE_NAME_TITLE}}Serializer.serialize_server_error_response()
    
    def handle_list(self, query_params: Dict[str, Any]) -> Dict[str, Any]:
        """{{FEATURE_NAME}}一覧取得リクエストの処理
        
        Args:
            query_params: クエリパラメータ
            
        Returns:
            Dict[str, Any]: HTTP レスポンスデータ
        """
        try:
            logger.info("Handling {{FEATURE_NAME}} list request")
            
            # 1. パラメータバリデーション
            validated_params = {{FEATURE_NAME_TITLE}}Validator.validate_list_request(query_params)
            
            # 2. DTO変換
            request_dto = {{FEATURE_NAME_TITLE}}ListRequest(**validated_params)
            
            # 3. ユースケース実行
            response_dto = self._use_case.list(request_dto)
            
            # 4. レスポンスシリアライゼーション
            response_data = {{FEATURE_NAME_TITLE}}Serializer.serialize_list_response(response_dto)
            
            logger.info("{{FEATURE_NAME}} list request handled successfully")
            return response_data
            
        except APIValidationError as e:
            logger.warning(f"API validation error in list: {e}")
            return {{FEATURE_NAME_TITLE}}Serializer.serialize_validation_error_response(e)
        except {{FEATURE_NAME_TITLE}}AuthorizationError as e:
            logger.warning(f"Authorization error in list: {e}")
            return {{FEATURE_NAME_TITLE}}Serializer.serialize_authorization_error_response()
        except Exception as e:
            logger.error(f"Unexpected error in list: {e}")
            return {{FEATURE_NAME_TITLE}}Serializer.serialize_server_error_response()
    
    def handle_update(self, entity_id: str, request_data: Dict[str, Any]) -> Dict[str, Any]:
        """{{FEATURE_NAME}}更新リクエストの処理
        
        Args:
            entity_id: 更新対象のエンティティID
            request_data: HTTP リクエストデータ
            
        Returns:
            Dict[str, Any]: HTTP レスポンスデータ
        """
        try:
            logger.info(f"Handling {{FEATURE_NAME}} update request: {entity_id}")
            
            # 1. IDバリデーション
            validated_id = {{FEATURE_NAME_TITLE}}Validator.validate_id_parameter(entity_id)
            
            # 2. 入力バリデーション
            validated_data = {{FEATURE_NAME_TITLE}}Validator.validate_update_request(request_data)
            
            # 3. エンティティIDを追加
            validated_data["entity_id"] = validated_id
            
            # 4. DTO変換
            request_dto = {{FEATURE_NAME_TITLE}}Request(**validated_data)
            
            # 5. ユースケース実行（更新ロジック）
            response_dto = self._use_case.execute(request_dto)
            
            # 6. レスポンスシリアライゼーション
            response_data = {{FEATURE_NAME_TITLE}}Serializer.serialize_response(response_dto)
            
            logger.info(f"{{FEATURE_NAME}} update request handled successfully: {entity_id}")
            return response_data
            
        except APIValidationError as e:
            logger.warning(f"API validation error in update: {e}")
            return {{FEATURE_NAME_TITLE}}Serializer.serialize_validation_error_response(e)
        except {{FEATURE_NAME_TITLE}}NotFoundError as e:
            logger.warning(f"{{FEATURE_NAME}} not found for update: {entity_id}")
            return {{FEATURE_NAME_TITLE}}Serializer.serialize_not_found_response(entity_id)
        except {{FEATURE_NAME_TITLE}}AuthorizationError as e:
            logger.warning(f"Authorization error in update: {e}")
            return {{FEATURE_NAME_TITLE}}Serializer.serialize_authorization_error_response()
        except {{FEATURE_NAME_TITLE}}BusinessRuleViolationError as e:
            logger.warning(f"Business rule violation in update: {e}")
            return {{FEATURE_NAME_TITLE}}Serializer.serialize_error_response(
                message=str(e),
                error_code="BUSINESS_RULE_VIOLATION",
                status_code=422
            )
        except Exception as e:
            logger.error(f"Unexpected error in update: {e}")
            return {{FEATURE_NAME_TITLE}}Serializer.serialize_server_error_response()
    
    def handle_delete(self, entity_id: str, user_id: str) -> Dict[str, Any]:
        """{{FEATURE_NAME}}削除リクエストの処理
        
        Args:
            entity_id: 削除対象のエンティティID
            user_id: ユーザーID
            
        Returns:
            Dict[str, Any]: HTTP レスポンスデータ
        """
        try:
            logger.info(f"Handling {{FEATURE_NAME}} delete request: {entity_id}")
            
            # 1. IDバリデーション
            validated_id = {{FEATURE_NAME_TITLE}}Validator.validate_id_parameter(entity_id)
            
            # 2. DTO作成（削除用）
            request_dto = {{FEATURE_NAME_TITLE}}Request(
                user_id=user_id,
                data={"entity_id": validated_id, "action": "delete"}
            )
            
            # 3. ユースケース実行（削除ロジック）
            response_dto = self._use_case.execute(request_dto)
            
            # 4. レスポンスシリアライゼーション
            response_data = {{FEATURE_NAME_TITLE}}Serializer.serialize_response(response_dto)
            
            logger.info(f"{{FEATURE_NAME}} delete request handled successfully: {entity_id}")
            return response_data
            
        except APIValidationError as e:
            logger.warning(f"API validation error in delete: {e}")
            return {{FEATURE_NAME_TITLE}}Serializer.serialize_validation_error_response(e)
        except {{FEATURE_NAME_TITLE}}NotFoundError as e:
            logger.warning(f"{{FEATURE_NAME}} not found for delete: {entity_id}")
            return {{FEATURE_NAME_TITLE}}Serializer.serialize_not_found_response(entity_id)
        except {{FEATURE_NAME_TITLE}}AuthorizationError as e:
            logger.warning(f"Authorization error in delete: {e}")
            return {{FEATURE_NAME_TITLE}}Serializer.serialize_authorization_error_response()
        except Exception as e:
            logger.error(f"Unexpected error in delete: {e}")
            return {{FEATURE_NAME_TITLE}}Serializer.serialize_server_error_response()
    
    def handle_health_check(self) -> Dict[str, Any]:
        """ヘルスチェックリクエストの処理
        
        Returns:
            Dict[str, Any]: HTTP レスポンスデータ
        """
        logger.debug("Handling health check request")
        return {{FEATURE_NAME_TITLE}}Serializer.serialize_health_check_response()