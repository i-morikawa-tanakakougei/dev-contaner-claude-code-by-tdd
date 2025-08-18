"""
{{FEATURE_NAME}} DTOs (Data Transfer Objects)

アプリケーション層の入出力データ転送オブジェクト。
実装日時: {{IMPLEMENTATION_DATE}}
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List, Any, Dict


@dataclass
class {{FEATURE_NAME_TITLE}}Request:
    """{{FEATURE_NAME}}実行リクエスト
    
    外部からのリクエストデータを表現するDTO。
    バリデーション機能を含む。
    """
    
    # TODO: 仕様に基づいて適切なフィールドを追加
    user_id: str
    data: Dict[str, Any]
    
    def validate(self) -> None:
        """リクエストデータの検証
        
        Raises:
            ValueError: 無効なデータが含まれている場合
        """
        if not self.user_id:
            raise ValueError("User ID is required")
        
        if not isinstance(self.user_id, str):
            raise TypeError("User ID must be a string")
        
        if not self.data:
            raise ValueError("Data is required")
        
        if not isinstance(self.data, dict):
            raise TypeError("Data must be a dictionary")
        
        # TODO: 仕様に基づいてバリデーションルールを追加


@dataclass
class {{FEATURE_NAME_TITLE}}Response:
    """{{FEATURE_NAME}}実行レスポンス
    
    ユースケース実行結果を表現するDTO。
    """
    
    success: bool
    message: str
    data: Optional[Dict[str, Any]] = None
    timestamp: datetime = None
    
    def __post_init__(self) -> None:
        """レスポンス初期化後処理"""
        if self.timestamp is None:
            self.timestamp = datetime.now()
    
    @classmethod
    def success_response(cls, message: str, data: Optional[Dict[str, Any]] = None) -> "{{FEATURE_NAME_TITLE}}Response":
        """成功レスポンスを作成
        
        Args:
            message: 成功メッセージ
            data: レスポンスデータ
            
        Returns:
            {{FEATURE_NAME_TITLE}}Response: 成功レスポンス
        """
        return cls(
            success=True,
            message=message,
            data=data
        )
    
    @classmethod
    def error_response(cls, message: str) -> "{{FEATURE_NAME_TITLE}}Response":
        """エラーレスポンスを作成
        
        Args:
            message: エラーメッセージ
            
        Returns:
            {{FEATURE_NAME_TITLE}}Response: エラーレスポンス
        """
        return cls(
            success=False,
            message=message
        )


@dataclass
class {{FEATURE_NAME_TITLE}}ListRequest:
    """{{FEATURE_NAME}}一覧取得リクエスト"""
    
    user_id: str
    page: int = 1
    limit: int = 10
    filters: Optional[Dict[str, Any]] = None
    
    def validate(self) -> None:
        """リクエストデータの検証"""
        if not self.user_id:
            raise ValueError("User ID is required")
        
        if self.page < 1:
            raise ValueError("Page must be greater than 0")
        
        if self.limit < 1 or self.limit > 100:
            raise ValueError("Limit must be between 1 and 100")


@dataclass
class {{FEATURE_NAME_TITLE}}ListResponse:
    """{{FEATURE_NAME}}一覧取得レスポンス"""
    
    success: bool
    items: List[Dict[str, Any]]
    total_count: int
    page: int
    limit: int
    message: str = ""
    
    @property
    def has_more(self) -> bool:
        """さらにデータがあるかチェック"""
        return (self.page * self.limit) < self.total_count