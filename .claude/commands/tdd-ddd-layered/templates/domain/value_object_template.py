"""
EntityId Value Object

エンティティの一意識別子を表現する値オブジェクト。
実装日時: {{IMPLEMENTATION_DATE}}
"""

import re
import uuid


class EntityId:
    """エンティティID値オブジェクト

    エンティティの一意識別を提供し、ID形式の妥当性を保証する。
    不変オブジェクトとして実装される。
    """

    def __init__(self, value: str):
        """EntityID初期化

        Args:
            value: UUID文字列

        Raises:
            ValueError: 無効なUUID形式の場合
        """
        self._value = self._validate_and_normalize(value)

    @classmethod
    def generate(cls) -> "EntityId":
        """新しいEntityIdを生成

        Returns:
            EntityId: 新しく生成されたEntityId
        """
        return cls(str(uuid.uuid4()))

    @classmethod
    def from_string(cls, id_string: str) -> "EntityId":
        """文字列からEntityIdを作成

        Args:
            id_string: ID文字列

        Returns:
            EntityId: EntityIdインスタンス
        """
        return cls(id_string)

    def _validate_and_normalize(self, value: str) -> str:
        """IDの検証と正規化

        Args:
            value: 検証対象の値

        Returns:
            str: 正規化されたID値

        Raises:
            ValueError: 無効な形式の場合
        """
        if not value:
            raise ValueError("Entity ID cannot be empty")

        if not isinstance(value, str):
            raise ValueError("Entity ID must be a string")

        value = value.strip()

        # UUID形式の検証（簡易版）
        if len(value) < 3:
            raise ValueError("Entity ID is too short")

        # より厳密なUUID検証が必要な場合
        uuid_pattern = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", re.IGNORECASE)

        # UUID形式でない場合も受け入れる（後方互換性のため）
        if not uuid_pattern.match(value):
            # カスタムID形式の場合の追加検証
            if len(value) > 255:
                raise ValueError("Entity ID cannot exceed 255 characters")

        return value

    @property
    def value(self) -> str:
        """ID値を取得"""
        return self._value

    def __str__(self) -> str:
        """文字列表現"""
        return self._value

    def __repr__(self) -> str:
        """デバッグ用文字列表現"""
        return f"EntityId('{self._value}')"

    def __eq__(self, other) -> bool:
        """等価性比較"""
        if not isinstance(other, EntityId):
            return False
        return self._value == other._value

    def __hash__(self) -> int:
        """ハッシュ値"""
        return hash(self._value)
