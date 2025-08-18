"""
{{FEATURE_NAME}} Use Case Implementation

アプリケーション層のユースケース実装。
ドメインオブジェクトを orchestrate してビジネス要件を実現する。
実装日時: {{IMPLEMENTATION_DATE}}
"""

from typing import Optional
import logging
{{ENTITY_IMPORTS}}
{{REPOSITORY_IMPORTS}}
from ..dtos.{{FEATURE_NAME_SNAKE}}_dtos import (
    {{FEATURE_NAME_TITLE}}Request,
    {{FEATURE_NAME_TITLE}}Response,
    {{FEATURE_NAME_TITLE}}ListRequest,
    {{FEATURE_NAME_TITLE}}ListResponse
)
from ..exceptions.{{FEATURE_NAME_SNAKE}}_exceptions import (
    {{FEATURE_NAME_TITLE}}ValidationError,
    {{FEATURE_NAME_TITLE}}NotFoundError,
    {{FEATURE_NAME_TITLE}}AuthorizationError,
    {{FEATURE_NAME_TITLE}}BusinessRuleViolationError
)


logger = logging.getLogger(__name__)


class {{FEATURE_NAME_TITLE}}UseCase:
    """{{FEATURE_NAME}}ユースケース
    
    {{FEATURE_NAME}}に関連するビジネス要件を実現するユースケース。
    ドメインオブジェクトを orchestrate し、トランザクション境界を管理する。
    """
    
    def __init__(self{{REPOSITORY_CONSTRUCTOR_PARAMS}}):
        """ユースケース初期化
        
        Args:
            {{REPOSITORY_CONSTRUCTOR_DOCS}}
        """
        {{REPOSITORY_ASSIGNMENTS}}
        logger.info("{{FEATURE_NAME_TITLE}}UseCase initialized")
    
    def execute(self, request: {{FEATURE_NAME_TITLE}}Request) -> {{FEATURE_NAME_TITLE}}Response:
        """{{FEATURE_NAME}}を実行する
        
        Args:
            request: {{FEATURE_NAME}}実行リクエスト
            
        Returns:
            {{FEATURE_NAME_TITLE}}Response: 実行結果
            
        Raises:
            {{FEATURE_NAME_TITLE}}ValidationError: リクエストデータが無効な場合
            {{FEATURE_NAME_TITLE}}AuthorizationError: 権限がない場合
            {{FEATURE_NAME_TITLE}}BusinessRuleViolationError: ビジネスルール違反の場合
        """
        logger.info(f"Executing {{FEATURE_NAME}} for user: {request.user_id}")
        
        try:
            # 1. リクエストバリデーション
            self._validate_request(request)
            
            # 2. 認可チェック
            self._check_authorization(request.user_id)
            
            # 3. ドメインオブジェクトの取得・作成
            {{ENTITY_CREATION_LOGIC}}
            
            # 4. ビジネスロジックの実行
            result = self._execute_business_logic({{ENTITY_PARAMS}}request)
            
            # 5. 永続化
            {{PERSISTENCE_LOGIC}}
            
            # 6. レスポンス作成
            logger.info(f"{{FEATURE_NAME}} executed successfully for user: {request.user_id}")
            return {{FEATURE_NAME_TITLE}}Response.success_response(
                message="{{FEATURE_NAME}} completed successfully",
                data=result
            )
            
        except {{FEATURE_NAME_TITLE}}ValidationError:
            logger.warning(f"Validation error in {{FEATURE_NAME}} for user: {request.user_id}")
            raise
        except {{FEATURE_NAME_TITLE}}AuthorizationError:
            logger.warning(f"Authorization error in {{FEATURE_NAME}} for user: {request.user_id}")
            raise
        except {{FEATURE_NAME_TITLE}}BusinessRuleViolationError:
            logger.warning(f"Business rule violation in {{FEATURE_NAME}} for user: {request.user_id}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in {{FEATURE_NAME}} for user: {request.user_id}: {e}")
            return {{FEATURE_NAME_TITLE}}Response.error_response(
                message="An unexpected error occurred"
            )
    
    def list(self, request: {{FEATURE_NAME_TITLE}}ListRequest) -> {{FEATURE_NAME_TITLE}}ListResponse:
        """{{FEATURE_NAME}}一覧を取得する
        
        Args:
            request: 一覧取得リクエスト
            
        Returns:
            {{FEATURE_NAME_TITLE}}ListResponse: 一覧取得結果
        """
        logger.info(f"Listing {{FEATURE_NAME}} for user: {request.user_id}")
        
        try:
            # 1. リクエストバリデーション
            request.validate()
            
            # 2. 認可チェック
            self._check_authorization(request.user_id)
            
            # 3. データ取得
            {{LIST_LOGIC}}
            
            return {{FEATURE_NAME_TITLE}}ListResponse(
                success=True,
                items=items,
                total_count=len(items),
                page=request.page,
                limit=request.limit,
                message="List retrieved successfully"
            )
            
        except Exception as e:
            logger.error(f"Error listing {{FEATURE_NAME}} for user: {request.user_id}: {e}")
            return {{FEATURE_NAME_TITLE}}ListResponse(
                success=False,
                items=[],
                total_count=0,
                page=request.page,
                limit=request.limit,
                message="Failed to retrieve list"
            )
    
    def _validate_request(self, request: {{FEATURE_NAME_TITLE}}Request) -> None:
        """リクエストバリデーション"""
        try:
            request.validate()
        except (ValueError, TypeError) as e:
            raise {{FEATURE_NAME_TITLE}}ValidationError(str(e))
    
    def _check_authorization(self, user_id: str) -> None:
        """認可チェック"""
        # TODO: 実際の認可ロジックを実装
        if not user_id:
            raise {{FEATURE_NAME_TITLE}}AuthorizationError("User ID is required")
    
    {{CREATE_OR_LOAD_METHODS}}
    
    def _execute_business_logic(self, {{ENTITY_PARAMS_WITH_REQUEST}}request: {{FEATURE_NAME_TITLE}}Request) -> dict:
        """ビジネスロジックの実行"""
        # TODO: 実際のビジネスロジックを実装
        {{SCENARIO_COMMENTS}}
        
        return {
            "processed": True,
            "timestamp": "{{IMPLEMENTATION_DATE}}",
            "data": request.data
        }
    
    {{ENTITY_TO_DICT_METHODS}}