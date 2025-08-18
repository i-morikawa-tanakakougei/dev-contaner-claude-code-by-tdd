"""
{{FEATURE_NAME}} Application Exceptions

アプリケーション層固有の例外クラス定義。
実装日時: {{IMPLEMENTATION_DATE}}
"""


class {{FEATURE_NAME_TITLE}}ApplicationError(Exception):
    """{{FEATURE_NAME}}アプリケーション層基底例外
    
    アプリケーション層で発生するすべての例外の基底クラス。
    """
    
    def __init__(self, message: str, details: str = None):
        super().__init__(message)
        self.message = message
        self.details = details
    
    def __str__(self) -> str:
        if self.details:
            return f"{self.message}: {self.details}"
        return self.message


class {{FEATURE_NAME_TITLE}}ValidationError({{FEATURE_NAME_TITLE}}ApplicationError):
    """{{FEATURE_NAME}}バリデーションエラー
    
    入力データの検証に失敗した場合に発生する例外。
    """
    pass


class {{FEATURE_NAME_TITLE}}NotFoundError({{FEATURE_NAME_TITLE}}ApplicationError):
    """{{FEATURE_NAME}}データ未発見エラー
    
    指定されたデータが見つからない場合に発生する例外。
    """
    pass


class {{FEATURE_NAME_TITLE}}AuthorizationError({{FEATURE_NAME_TITLE}}ApplicationError):
    """{{FEATURE_NAME}}認可エラー
    
    ユーザーに適切な権限がない場合に発生する例外。
    """
    pass


class {{FEATURE_NAME_TITLE}}BusinessRuleViolationError({{FEATURE_NAME_TITLE}}ApplicationError):
    """{{FEATURE_NAME}}ビジネスルール違反エラー
    
    ビジネスルールに違反する操作が実行された場合に発生する例外。
    """
    pass


class {{FEATURE_NAME_TITLE}}ConcurrencyError({{FEATURE_NAME_TITLE}}ApplicationError):
    """{{FEATURE_NAME}}同時実行エラー
    
    同時実行による競合状態が発生した場合に発生する例外。
    """
    pass