"""
{{FEATURE_NAME}} API Validators

API入力データのバリデーション処理。
実装日時: {{IMPLEMENTATION_DATE}}
"""

from typing import Dict, Any, List, Optional
import re
from datetime import datetime


class {{FEATURE_NAME_TITLE}}ValidationError(Exception):
    """{{FEATURE_NAME}}バリデーションエラー"""
    
    def __init__(self, message: str, field: str = None, errors: List[str] = None):
        super().__init__(message)
        self.message = message
        self.field = field
        self.errors = errors or []


class {{FEATURE_NAME_TITLE}}Validator:
    """{{FEATURE_NAME}}APIバリデーター
    
    API入力データの検証とサニタイゼーションを行う。
    """
    
    @staticmethod
    def validate_create_request(data: Dict[str, Any]) -> Dict[str, Any]:
        """作成リクエストのバリデーション
        
        Args:
            data: リクエストデータ
            
        Returns:
            Dict[str, Any]: 検証済みデータ
            
        Raises:
            {{FEATURE_NAME_TITLE}}ValidationError: バリデーションエラー
        """
        errors = []
        validated_data = {}
        
        # user_id の検証
        if "user_id" not in data:
            errors.append("user_id is required")
        elif not isinstance(data["user_id"], str):
            errors.append("user_id must be a string")
        elif not data["user_id"].strip():
            errors.append("user_id cannot be empty")
        else:
            validated_data["user_id"] = data["user_id"].strip()
        
        # data フィールドの検証
        if "data" not in data:
            errors.append("data is required")
        elif not isinstance(data["data"], dict):
            errors.append("data must be an object")
        else:
            validated_data["data"] = data["data"]
        
        # 追加のビジネス固有バリデーション
        if "name" in data:
            name_validation = {{FEATURE_NAME_TITLE}}Validator._validate_name(data["name"])
            if name_validation["valid"]:
                validated_data["name"] = name_validation["value"]
            else:
                errors.extend(name_validation["errors"])
        
        if "email" in data:
            email_validation = {{FEATURE_NAME_TITLE}}Validator._validate_email(data["email"])
            if email_validation["valid"]:
                validated_data["email"] = email_validation["value"]
            else:
                errors.extend(email_validation["errors"])
        
        if errors:
            raise {{FEATURE_NAME_TITLE}}ValidationError(
                "Validation failed",
                errors=errors
            )
        
        return validated_data
    
    @staticmethod
    def validate_update_request(data: Dict[str, Any]) -> Dict[str, Any]:
        """更新リクエストのバリデーション
        
        Args:
            data: リクエストデータ
            
        Returns:
            Dict[str, Any]: 検証済みデータ
            
        Raises:
            {{FEATURE_NAME_TITLE}}ValidationError: バリデーションエラー
        """
        errors = []
        validated_data = {}
        
        # user_id の検証（更新時も必要）
        if "user_id" not in data:
            errors.append("user_id is required")
        elif not isinstance(data["user_id"], str):
            errors.append("user_id must be a string")
        elif not data["user_id"].strip():
            errors.append("user_id cannot be empty")
        else:
            validated_data["user_id"] = data["user_id"].strip()
        
        # 更新可能フィールドの検証（部分更新対応）
        if "data" in data:
            if not isinstance(data["data"], dict):
                errors.append("data must be an object")
            else:
                validated_data["data"] = data["data"]
        
        if "name" in data:
            name_validation = {{FEATURE_NAME_TITLE}}Validator._validate_name(data["name"])
            if name_validation["valid"]:
                validated_data["name"] = name_validation["value"]
            else:
                errors.extend(name_validation["errors"])
        
        if errors:
            raise {{FEATURE_NAME_TITLE}}ValidationError(
                "Validation failed",
                errors=errors
            )
        
        return validated_data
    
    @staticmethod
    def validate_list_request(params: Dict[str, Any]) -> Dict[str, Any]:
        """一覧取得リクエストのバリデーション
        
        Args:
            params: クエリパラメータ
            
        Returns:
            Dict[str, Any]: 検証済みパラメータ
            
        Raises:
            {{FEATURE_NAME_TITLE}}ValidationError: バリデーションエラー
        """
        errors = []
        validated_params = {}
        
        # user_id の検証
        if "user_id" not in params:
            errors.append("user_id is required")
        elif not isinstance(params["user_id"], str):
            errors.append("user_id must be a string")
        elif not params["user_id"].strip():
            errors.append("user_id cannot be empty")
        else:
            validated_params["user_id"] = params["user_id"].strip()
        
        # page の検証
        page = params.get("page", "1")
        try:
            page_int = int(page)
            if page_int < 1:
                errors.append("page must be greater than 0")
            else:
                validated_params["page"] = page_int
        except ValueError:
            errors.append("page must be a valid integer")
        
        # limit の検証
        limit = params.get("limit", "10")
        try:
            limit_int = int(limit)
            if limit_int < 1:
                errors.append("limit must be greater than 0")
            elif limit_int > 100:
                errors.append("limit must not exceed 100")
            else:
                validated_params["limit"] = limit_int
        except ValueError:
            errors.append("limit must be a valid integer")
        
        # filters の検証
        if "filters" in params:
            if isinstance(params["filters"], dict):
                validated_params["filters"] = params["filters"]
            else:
                errors.append("filters must be an object")
        
        if errors:
            raise {{FEATURE_NAME_TITLE}}ValidationError(
                "Validation failed",
                errors=errors
            )
        
        return validated_params
    
    @staticmethod
    def validate_id_parameter(entity_id: str) -> str:
        """IDパラメータのバリデーション
        
        Args:
            entity_id: エンティティID
            
        Returns:
            str: 検証済みID
            
        Raises:
            {{FEATURE_NAME_TITLE}}ValidationError: バリデーションエラー
        """
        if not entity_id:
            raise {{FEATURE_NAME_TITLE}}ValidationError("ID is required")
        
        if not isinstance(entity_id, str):
            raise {{FEATURE_NAME_TITLE}}ValidationError("ID must be a string")
        
        entity_id = entity_id.strip()
        if not entity_id:
            raise {{FEATURE_NAME_TITLE}}ValidationError("ID cannot be empty")
        
        # UUID形式の簡易チェック（より厳密な検証は必要に応じて）
        if len(entity_id) < 3:
            raise {{FEATURE_NAME_TITLE}}ValidationError("ID is too short")
        
        return entity_id
    
    @staticmethod
    def _validate_name(name: Any) -> Dict[str, Any]:
        """名前フィールドのバリデーション"""
        if not isinstance(name, str):
            return {"valid": False, "errors": ["name must be a string"]}
        
        name = name.strip()
        if not name:
            return {"valid": False, "errors": ["name cannot be empty"]}
        
        if len(name) > 255:
            return {"valid": False, "errors": ["name cannot exceed 255 characters"]}
        
        # 特殊文字制限（必要に応じて調整）
        if re.search(r'[<>&"\'']', name):
            return {"valid": False, "errors": ["name contains invalid characters"]}
        
        return {"valid": True, "value": name}
    
    @staticmethod
    def _validate_email(email: Any) -> Dict[str, Any]:
        """メールアドレスフィールドのバリデーション"""
        if not isinstance(email, str):
            return {"valid": False, "errors": ["email must be a string"]}
        
        email = email.strip().lower()
        if not email:
            return {"valid": False, "errors": ["email cannot be empty"]}
        
        # 簡易メールアドレス形式チェック
        email_pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
        if not email_pattern.match(email):
            return {"valid": False, "errors": ["email format is invalid"]}
        
        if len(email) > 255:
            return {"valid": False, "errors": ["email cannot exceed 255 characters"]}
        
        return {"valid": True, "value": email}