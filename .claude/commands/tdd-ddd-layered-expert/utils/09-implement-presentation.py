#!/usr/bin/env python3
"""
Presentation Layer Implementation Command - 改修版
プレゼンテーション層を実装し、実行履歴を更新
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))
from json_format_utils import (
    load_use_case_json,
    update_execution_history,
    save_use_case_json,
    format_execution_status,
    update_tdd_phase
)


def find_use_case_json(issue_number):
    """Issue番号からJSONファイルを検索"""
    use_cases_dir = Path("docs/use_cases")
    
    if not use_cases_dir.exists():
        return None
    
    # issue-{number}-*.json パターンで検索
    for json_file in use_cases_dir.glob(f"issue-{issue_number}-*.json"):
        return str(json_file)
    
    # 単純なissue-{number}.json も検索
    simple_path = use_cases_dir / f"issue-{issue_number}.json"
    if simple_path.exists():
        return str(simple_path)
    
    return None


def create_presentation_directories():
    """プレゼンテーション層のディレクトリ構造を作成"""
    base_path = Path("src/presentation")
    
    dirs_to_create = [
        base_path,
        base_path / "api" / "controllers",
        base_path / "api" / "middleware",
        base_path / "api" / "responses",
        base_path / "cli" / "commands",
        base_path / "cli" / "handlers",
        base_path / "validators",
        base_path / "serializers",
        base_path / "auth"
    ]
    
    created_dirs = []
    for dir_path in dirs_to_create:
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)
            created_dirs.append(str(dir_path))
        
        # __init__.pyファイルも作成
        init_file = dir_path / "__init__.py"
        if not init_file.exists():
            init_file.write_text("", encoding="utf-8")
    
    return created_dirs


def analyze_application_layer(app_dir):
    """アプリケーション層のユースケースを分析"""
    use_cases = []
    
    app_path = Path(app_dir)
    if not app_path.exists():
        return use_cases
    
    # use_casesディレクトリからユースケースを検索
    use_case_dir = app_path / "use_cases"
    if use_case_dir.exists():
        for py_file in use_case_dir.glob("*.py"):
            if py_file.name != "__init__.py":
                use_cases.append({
                    "use_case_name": py_file.stem,
                    "file_path": str(py_file),
                    "endpoints_needed": True
                })
    
    return use_cases


def generate_api_controller(use_case_name, use_case_data):
    """APIコントローラーを生成"""
    
    entity_name = use_case_name.replace("_use_case", "").replace("UseCase", "")
    controller_class = f"{entity_name.title()}Controller"
    
    content = f'''"""
{entity_name.title()} API Controller
RESTful APIエンドポイントの実装
"""

from typing import Dict, Any, List, Optional
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.responses import JSONResponse

from src.application.use_cases.{use_case_name.lower()} import {use_case_name.title()}
from src.presentation.validators.{entity_name.lower()}_validator import {entity_name.title()}Validator
from src.presentation.serializers.{entity_name.lower()}_serializer import (
    {entity_name.title()}CreateRequest,
    {entity_name.title()}UpdateRequest,
    {entity_name.title()}Response,
    {entity_name.title()}ListResponse
)
from src.presentation.auth.dependencies import get_current_user, require_permission
from src.presentation.api.responses.error_response import ErrorResponse


router = APIRouter(prefix="/{entity_name.lower()}s", tags=["{entity_name.lower()}s"])


class {controller_class}:
    """
    {entity_name.title()} APIコントローラー
    Clean Architectureのプレゼンテーション層として、
    ユーザーインターフェースとアプリケーション層を連携
    """
    
    def __init__(self, use_case: {use_case_name.title()}):
        """
        Args:
            use_case: アプリケーション層のユースケース
        """
        self._use_case = use_case
        self._validator = {entity_name.title()}Validator()
    
    def _handle_error(self, error: Exception) -> JSONResponse:
        """エラーハンドリング共通処理"""
        error_response = ErrorResponse.from_exception(error)
        return JSONResponse(
            status_code=error_response.status_code,
            content=error_response.dict()
        )


# コントローラーインスタンス（DIコンテナで管理される想定）
controller = None  # DIで注入される


@router.post("/", response_model={entity_name.title()}Response, status_code=status.HTTP_201_CREATED)
async def create_{entity_name.lower()}(
    request: {entity_name.title()}CreateRequest,
    current_user=Depends(get_current_user),
    _=Depends(require_permission("{entity_name.lower()}:create"))
) -> {entity_name.title()}Response:
    """
    {entity_name.title()}を新規作成
    
    Args:
        request: 作成リクエスト
        current_user: 認証されたユーザー
        
    Returns:
        作成された{entity_name.title()}の情報
    """
    try:
        # バリデーション
        validation_result = controller._validator.validate_create_request(request.dict())
        if not validation_result.is_valid:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={{"errors": validation_result.errors}}
            )
        
        # ユースケース実行
        result = await controller._use_case.create_{entity_name.lower()}(request.dict())
        
        # レスポンス構築
        return {entity_name.title()}Response.from_domain(result)
        
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={{"message": str(e)}}
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={{"message": "Internal server error"}}
        )


@router.get("/{{id}}", response_model={entity_name.title()}Response)
async def get_{entity_name.lower()}(
    id: str,
    current_user=Depends(get_current_user),
    _=Depends(require_permission("{entity_name.lower()}:read"))
) -> {entity_name.title()}Response:
    """
    {entity_name.title()}を ID で取得
    
    Args:
        id: {entity_name.title()} ID
        current_user: 認証されたユーザー
        
    Returns:
        {entity_name.title()}の情報
    """
    try:
        result = await controller._use_case.get_{entity_name.lower()}_by_id(id)
        
        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={{"message": f"{entity_name.title()} with ID {{id}} not found"}}
            )
        
        return {entity_name.title()}Response.from_domain(result)
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={{"message": "Internal server error"}}
        )


@router.get("/", response_model={entity_name.title()}ListResponse)
async def list_{entity_name.lower()}s(
    page: int = 1,
    limit: int = 20,
    current_user=Depends(get_current_user),
    _=Depends(require_permission("{entity_name.lower()}:read"))
) -> {entity_name.title()}ListResponse:
    """
    {entity_name.title()}一覧を取得
    
    Args:
        page: ページ番号
        limit: 1ページあたりの件数
        current_user: 認証されたユーザー
        
    Returns:
        {entity_name.title()}一覧
    """
    try:
        # ページネーション検証
        if page < 1 or limit < 1 or limit > 100:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={{"message": "Invalid pagination parameters"}}
            )
        
        result = await controller._use_case.list_{entity_name.lower()}s(page=page, limit=limit)
        
        return {entity_name.title()}ListResponse(
            items=[{entity_name.title()}Response.from_domain(item) for item in result.items],
            total=result.total,
            page=page,
            limit=limit,
            pages=result.pages
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={{"message": "Internal server error"}}
        )


@router.put("/{{id}}", response_model={entity_name.title()}Response)
async def update_{entity_name.lower()}(
    id: str,
    request: {entity_name.title()}UpdateRequest,
    current_user=Depends(get_current_user),
    _=Depends(require_permission("{entity_name.lower()}:update"))
) -> {entity_name.title()}Response:
    """
    {entity_name.title()}を更新
    
    Args:
        id: {entity_name.title()} ID
        request: 更新リクエスト
        current_user: 認証されたユーザー
        
    Returns:
        更新された{entity_name.title()}の情報
    """
    try:
        # バリデーション
        validation_result = controller._validator.validate_update_request(request.dict())
        if not validation_result.is_valid:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={{"errors": validation_result.errors}}
            )
        
        # ユースケース実行
        result = await controller._use_case.update_{entity_name.lower()}(id, request.dict())
        
        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={{"message": f"{entity_name.title()} with ID {{id}} not found"}}
            )
        
        return {entity_name.title()}Response.from_domain(result)
        
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={{"message": str(e)}}
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={{"message": "Internal server error"}}
        )


@router.delete("/{{id}}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_{entity_name.lower()}(
    id: str,
    current_user=Depends(get_current_user),
    _=Depends(require_permission("{entity_name.lower()}:delete"))
) -> None:
    """
    {entity_name.title()}を削除
    
    Args:
        id: {entity_name.title()} ID
        current_user: 認証されたユーザー
    """
    try:
        success = await controller._use_case.delete_{entity_name.lower()}(id)
        
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={{"message": f"{entity_name.title()} with ID {{id}} not found"}}
            )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={{"message": "Internal server error"}}
        )
'''
    
    return content


def generate_cli_command(use_case_name, use_case_data):
    """CLIコマンドを生成"""
    
    entity_name = use_case_name.replace("_use_case", "").replace("UseCase", "")
    command_class = f"{entity_name.title()}Command"
    
    content = f'''"""
{entity_name.title()} CLI Command
コマンドライン操作インターフェース
"""

import asyncio
import json
import sys
from typing import Dict, Any, Optional
from argparse import ArgumentParser, Namespace

from src.application.use_cases.{use_case_name.lower()} import {use_case_name.title()}
from src.presentation.validators.{entity_name.lower()}_validator import {entity_name.title()}Validator
from src.presentation.cli.handlers.base_handler import BaseCommandHandler


class {command_class}(BaseCommandHandler):
    """
    {entity_name.title()} CLIコマンド実装
    ユーザーフレンドリーなコマンドライン操作を提供
    """
    
    def __init__(self, use_case: {use_case_name.title()}):
        """
        Args:
            use_case: アプリケーション層のユースケース
        """
        super().__init__()
        self._use_case = use_case
        self._validator = {entity_name.title()}Validator()
    
    def setup_parser(self, parser: ArgumentParser) -> None:
        """コマンド引数を設定"""
        subparsers = parser.add_subparsers(dest='action', help='{entity_name.title()} operations')
        
        # Create command
        create_parser = subparsers.add_parser(
            'create',
            help='Create a new {entity_name.lower()}'
        )
        create_parser.add_argument('--name', required=True, help='{entity_name.title()} name')
        create_parser.add_argument('--description', help='{entity_name.title()} description')
        create_parser.add_argument('--json-file', help='Load data from JSON file')
        
        # Get command
        get_parser = subparsers.add_parser(
            'get',
            help='Get {entity_name.lower()} by ID'
        )
        get_parser.add_argument('id', help='{entity_name.title()} ID')
        get_parser.add_argument('--format', choices=['json', 'table'], default='table', help='Output format')
        
        # List command
        list_parser = subparsers.add_parser(
            'list',
            help='List all {entity_name.lower()}s'
        )
        list_parser.add_argument('--page', type=int, default=1, help='Page number')
        list_parser.add_argument('--limit', type=int, default=20, help='Items per page')
        list_parser.add_argument('--format', choices=['json', 'table'], default='table', help='Output format')
        
        # Update command
        update_parser = subparsers.add_parser(
            'update',
            help='Update {entity_name.lower()}'
        )
        update_parser.add_argument('id', help='{entity_name.title()} ID')
        update_parser.add_argument('--name', help='New {entity_name.lower()} name')
        update_parser.add_argument('--description', help='New description')
        update_parser.add_argument('--json-file', help='Load update data from JSON file')
        
        # Delete command
        delete_parser = subparsers.add_parser(
            'delete',
            help='Delete {entity_name.lower()}'
        )
        delete_parser.add_argument('id', help='{entity_name.title()} ID')
        delete_parser.add_argument('--confirm', action='store_true', help='Skip confirmation prompt')
    
    async def handle_create(self, args: Namespace) -> None:
        """Create コマンドの処理"""
        try:
            # データ準備
            if args.json_file:
                data = self._load_json_file(args.json_file)
            else:
                data = {{
                    'name': args.name,
                    'description': args.description or ''
                }}
            
            # バリデーション
            validation_result = self._validator.validate_create_request(data)
            if not validation_result.is_valid:
                self.print_error("Validation failed:")
                for error in validation_result.errors:
                    self.print_error(f"  - {{error}}")
                sys.exit(1)
            
            # ユースケース実行
            result = await self._use_case.create_{entity_name.lower()}(data)
            
            self.print_success(f"✅ {entity_name.title()} created successfully!")
            self.print_json({{
                'id': result.id.value,
                'name': result.name,
                'description': result.description,
                'created_at': result.created_at.isoformat()
            }})
            
        except Exception as e:
            self.print_error(f"❌ Failed to create {entity_name.lower()}: {{e}}")
            sys.exit(1)
    
    async def handle_get(self, args: Namespace) -> None:
        """Get コマンドの処理"""
        try:
            result = await self._use_case.get_{entity_name.lower()}_by_id(args.id)
            
            if not result:
                self.print_error(f"❌ {entity_name.title()} with ID {{args.id}} not found")
                sys.exit(1)
            
            if args.format == 'json':
                self.print_json({{
                    'id': result.id.value,
                    'name': result.name,
                    'description': result.description,
                    'created_at': result.created_at.isoformat(),
                    'updated_at': result.updated_at.isoformat() if result.updated_at else None
                }})
            else:
                self._print_table([result])
                
        except Exception as e:
            self.print_error(f"❌ Failed to get {entity_name.lower()}: {{e}}")
            sys.exit(1)
    
    async def handle_list(self, args: Namespace) -> None:
        """List コマンドの処理"""
        try:
            result = await self._use_case.list_{entity_name.lower()}s(
                page=args.page, 
                limit=args.limit
            )
            
            if not result.items:
                self.print_info("No {entity_name.lower()}s found")
                return
            
            if args.format == 'json':
                self.print_json({{
                    'items': [{{
                        'id': item.id.value,
                        'name': item.name,
                        'description': item.description,
                        'created_at': item.created_at.isoformat()
                    }} for item in result.items],
                    'pagination': {{
                        'page': args.page,
                        'limit': args.limit,
                        'total': result.total,
                        'pages': result.pages
                    }}
                }})
            else:
                self._print_table(result.items)
                self.print_info(f"Page {{args.page}} of {{result.pages}} ({{result.total}} total items)")
                
        except Exception as e:
            self.print_error(f"❌ Failed to list {entity_name.lower()}s: {{e}}")
            sys.exit(1)
    
    async def handle_update(self, args: Namespace) -> None:
        """Update コマンドの処理"""
        try:
            # データ準備
            if args.json_file:
                data = self._load_json_file(args.json_file)
            else:
                data = {{}}
                if args.name:
                    data['name'] = args.name
                if args.description:
                    data['description'] = args.description
            
            if not data:
                self.print_error("❌ No update data provided")
                sys.exit(1)
            
            # バリデーション
            validation_result = self._validator.validate_update_request(data)
            if not validation_result.is_valid:
                self.print_error("Validation failed:")
                for error in validation_result.errors:
                    self.print_error(f"  - {{error}}")
                sys.exit(1)
            
            # ユースケース実行
            result = await self._use_case.update_{entity_name.lower()}(args.id, data)
            
            if not result:
                self.print_error(f"❌ {entity_name.title()} with ID {{args.id}} not found")
                sys.exit(1)
            
            self.print_success(f"✅ {entity_name.title()} updated successfully!")
            self.print_json({{
                'id': result.id.value,
                'name': result.name,
                'description': result.description,
                'updated_at': result.updated_at.isoformat()
            }})
            
        except Exception as e:
            self.print_error(f"❌ Failed to update {entity_name.lower()}: {{e}}")
            sys.exit(1)
    
    async def handle_delete(self, args: Namespace) -> None:
        """Delete コマンドの処理"""
        try:
            # 確認プロンプト
            if not args.confirm:
                confirm = input(f"Are you sure you want to delete {entity_name.lower()} {{args.id}}? (y/N): ")
                if confirm.lower() not in ['y', 'yes']:
                    self.print_info("Operation cancelled")
                    return
            
            # ユースケース実行
            success = await self._use_case.delete_{entity_name.lower()}(args.id)
            
            if not success:
                self.print_error(f"❌ {entity_name.title()} with ID {{args.id}} not found")
                sys.exit(1)
            
            self.print_success(f"✅ {entity_name.title()} deleted successfully!")
            
        except Exception as e:
            self.print_error(f"❌ Failed to delete {entity_name.lower()}: {{e}}")
            sys.exit(1)
    
    def _print_table(self, items) -> None:
        """テーブル形式で項目を表示"""
        if not items:
            return
            
        # ヘッダー
        print(f"{{:<40}} {{:<30}} {{:<50}} {{:<20}}".format(
            "ID", "Name", "Description", "Created"
        ))
        print("-" * 140)
        
        # データ行
        for item in items:
            description = (item.description[:47] + "...") if len(item.description) > 50 else item.description
            created = item.created_at.strftime("%Y-%m-%d %H:%M:%S")
            
            print(f"{{:<40}} {{:<30}} {{:<50}} {{:<20}}".format(
                item.id.value, item.name, description, created
            ))
    
    async def run(self, args: Namespace) -> None:
        """メインエントリポイント"""
        if not args.action:
            self.print_error("❌ No action specified. Use --help for usage.")
            sys.exit(1)
        
        action_handlers = {{
            'create': self.handle_create,
            'get': self.handle_get,
            'list': self.handle_list,
            'update': self.handle_update,
            'delete': self.handle_delete
        }}
        
        handler = action_handlers.get(args.action)
        if handler:
            await handler(args)
        else:
            self.print_error(f"❌ Unknown action: {{args.action}}")
            sys.exit(1)


def main():
    """CLIメインエントリポイント"""
    # DIコンテナからユースケースを取得する想定
    # use_case = get_use_case_instance()
    # command = {command_class}(use_case)
    
    print("CLI command implementation template generated.")
    print("Please integrate with your DI container and main CLI entry point.")


if __name__ == "__main__":
    main()
'''
    
    return content


def generate_request_response_models(entity_name, use_case_data):
    """リクエスト/レスポンスモデルを生成"""
    
    content = f'''"""
{entity_name.title()} Request/Response Models
APIシリアライゼーション用のPydanticモデル
"""

from typing import Optional, List, Any, Dict
from datetime import datetime
from pydantic import BaseModel, Field, validator

from src.domain.entities.{entity_name.lower()} import {entity_name.title()}


class {entity_name.title()}CreateRequest(BaseModel):
    """
    {entity_name.title()}作成リクエストモデル
    """
    name: str = Field(..., min_length=1, max_length=255, description="{entity_name.title()}名")
    description: Optional[str] = Field(None, max_length=1000, description="説明")
    status: Optional[str] = Field("active", description="ステータス")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict, description="追加メタデータ")
    
    @validator('name')
    def validate_name(cls, v):
        if not v or not v.strip():
            raise ValueError('Name cannot be empty')
        return v.strip()
    
    @validator('status')
    def validate_status(cls, v):
        allowed_statuses = ['active', 'inactive', 'draft']
        if v and v not in allowed_statuses:
            raise ValueError(f'Status must be one of: {{", ".join(allowed_statuses)}}')
        return v
    
    class Config:
        json_schema_extra = {{
            "example": {{
                "name": "Sample {entity_name.title()}",
                "description": "This is a sample {entity_name.lower()} for demonstration",
                "status": "active",
                "metadata": {{
                    "category": "example",
                    "tags": ["sample", "demo"]
                }}
            }}
        }}


class {entity_name.title()}UpdateRequest(BaseModel):
    """
    {entity_name.title()}更新リクエストモデル
    """
    name: Optional[str] = Field(None, min_length=1, max_length=255, description="{entity_name.title()}名")
    description: Optional[str] = Field(None, max_length=1000, description="説明")
    status: Optional[str] = Field(None, description="ステータス")
    metadata: Optional[Dict[str, Any]] = Field(None, description="追加メタデータ")
    
    @validator('name')
    def validate_name(cls, v):
        if v is not None and (not v or not v.strip()):
            raise ValueError('Name cannot be empty')
        return v.strip() if v else None
    
    @validator('status')
    def validate_status(cls, v):
        if v is not None:
            allowed_statuses = ['active', 'inactive', 'draft']
            if v not in allowed_statuses:
                raise ValueError(f'Status must be one of: {{", ".join(allowed_statuses)}}')
        return v
    
    class Config:
        json_schema_extra = {{
            "example": {{
                "name": "Updated {entity_name.title()}",
                "description": "Updated description",
                "status": "active"
            }}
        }}


class {entity_name.title()}Response(BaseModel):
    """
    {entity_name.title()}レスポンスモデル
    """
    id: str = Field(..., description="{entity_name.title()} ID")
    name: str = Field(..., description="{entity_name.title()}名")
    description: Optional[str] = Field(None, description="説明")
    status: str = Field(..., description="ステータス")
    is_active: bool = Field(..., description="アクティブフラグ")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="追加メタデータ")
    created_at: datetime = Field(..., description="作成日時")
    updated_at: Optional[datetime] = Field(None, description="更新日時")
    
    @classmethod
    def from_domain(cls, entity: {entity_name.title()}) -> "{entity_name.title()}Response":
        """
        ドメインエンティティからレスポンスモデルに変換
        
        Args:
            entity: ドメインエンティティ
            
        Returns:
            レスポンスモデル
        """
        return cls(
            id=entity.id.value,
            name=entity.name,
            description=entity.description,
            status=entity.status,
            is_active=entity.is_active,
            metadata=getattr(entity, 'metadata', {{}}),
            created_at=entity.created_at,
            updated_at=entity.updated_at
        )
    
    class Config:
        json_schema_extra = {{
            "example": {{
                "id": "12345678-1234-1234-1234-123456789012",
                "name": "Sample {entity_name.title()}",
                "description": "This is a sample {entity_name.lower()}",
                "status": "active",
                "is_active": True,
                "metadata": {{
                    "category": "example"
                }},
                "created_at": "2024-01-01T00:00:00Z",
                "updated_at": "2024-01-02T00:00:00Z"
            }}
        }}


class {entity_name.title()}ListResponse(BaseModel):
    """
    {entity_name.title()}一覧レスポンスモデル
    """
    items: List[{entity_name.title()}Response] = Field(..., description="{entity_name.title()}一覧")
    total: int = Field(..., description="総件数")
    page: int = Field(..., description="現在のページ")
    limit: int = Field(..., description="1ページあたりの件数")
    pages: int = Field(..., description="総ページ数")
    
    class Config:
        json_schema_extra = {{
            "example": {{
                "items": [
                    {{
                        "id": "12345678-1234-1234-1234-123456789012",
                        "name": "Sample {entity_name.title()} 1",
                        "status": "active",
                        "created_at": "2024-01-01T00:00:00Z"
                    }}
                ],
                "total": 100,
                "page": 1,
                "limit": 20,
                "pages": 5
            }}
        }}


class ValidationError(BaseModel):
    """
    バリデーションエラーモデル
    """
    field: str = Field(..., description="エラーが発生したフィールド")
    message: str = Field(..., description="エラーメッセージ")
    code: str = Field(..., description="エラーコード")


class ErrorResponse(BaseModel):
    """
    エラーレスポンスモデル
    """
    message: str = Field(..., description="エラーメッセージ")
    code: Optional[str] = Field(None, description="エラーコード")
    details: Optional[Dict[str, Any]] = Field(None, description="エラー詳細")
    errors: Optional[List[ValidationError]] = Field(None, description="バリデーションエラー一覧")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="エラー発生時刻")
    
    @classmethod
    def from_exception(cls, error: Exception) -> "ErrorResponse":
        """
        例外からエラーレスポンスを作成
        
        Args:
            error: 例外オブジェクト
            
        Returns:
            エラーレスポンスモデル
        """
        return cls(
            message=str(error),
            code=error.__class__.__name__,
            timestamp=datetime.utcnow()
        )
    
    @property
    def status_code(self) -> int:
        """HTTPステータスコードを決定"""
        error_code_mapping = {{
            'ValueError': 400,
            'ValidationError': 400,
            'NotFoundError': 404,
            'PermissionError': 403,
            'AuthenticationError': 401,
        }}
        return error_code_mapping.get(self.code, 500)
'''
    
    return content


def generate_input_validator(entity_name, use_case_data):
    """入力バリデーターを生成"""
    
    validator_class = f"{entity_name.title()}Validator"
    
    content = f'''"""
{entity_name.title()} Input Validator
入力データのバリデーション処理
"""

import re
from typing import Dict, Any, List, Optional
from dataclasses import dataclass


@dataclass
class ValidationResult:
    """バリデーション結果"""
    is_valid: bool
    errors: List[str]
    
    @classmethod
    def success(cls) -> "ValidationResult":
        """成功結果を作成"""
        return cls(is_valid=True, errors=[])
    
    @classmethod
    def failure(cls, errors: List[str]) -> "ValidationResult":
        """失敗結果を作成"""
        return cls(is_valid=False, errors=errors)


class {validator_class}:
    """
    {entity_name.title()}入力バリデーター
    セキュリティとデータ整合性を確保
    """
    
    def __init__(self):
        # 基本的な正規表現パターン
        self.name_pattern = re.compile(r'^[a-zA-Z0-9\s\-_\.]+$')
        self.email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{{2,}}$')
        self.url_pattern = re.compile(
            r'^https?://(?:[-\w.])+(?:\:[0-9]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:\#(?:[\w.])*)?)?$'
        )
    
    def validate_create_request(self, data: Dict[str, Any]) -> ValidationResult:
        """
        作成リクエストのバリデーション
        
        Args:
            data: リクエストデータ
            
        Returns:
            バリデーション結果
        """
        errors = []
        
        # 必須フィールドチェック
        if not data.get('name'):
            errors.append("Name is required")
        elif not isinstance(data['name'], str):
            errors.append("Name must be a string")
        elif len(data['name'].strip()) == 0:
            errors.append("Name cannot be empty")
        elif len(data['name']) > 255:
            errors.append("Name cannot exceed 255 characters")
        elif not self.name_pattern.match(data['name']):
            errors.append("Name contains invalid characters")
        
        # オプショナルフィールドチェック
        if 'description' in data and data['description'] is not None:
            if not isinstance(data['description'], str):
                errors.append("Description must be a string")
            elif len(data['description']) > 1000:
                errors.append("Description cannot exceed 1000 characters")
        
        # ステータスチェック
        if 'status' in data and data['status'] is not None:
            allowed_statuses = ['active', 'inactive', 'draft']
            if data['status'] not in allowed_statuses:
                errors.append(f"Status must be one of: {{', '.join(allowed_statuses)}}")
        
        # メタデータチェック
        if 'metadata' in data and data['metadata'] is not None:
            if not isinstance(data['metadata'], dict):
                errors.append("Metadata must be a dictionary")
            else:
                # メタデータのサイズ制限
                metadata_str = str(data['metadata'])
                if len(metadata_str) > 5000:
                    errors.append("Metadata is too large (max 5000 characters)")
        
        # セキュリティチェック
        security_errors = self._check_security_violations(data)
        errors.extend(security_errors)
        
        return ValidationResult.success() if not errors else ValidationResult.failure(errors)
    
    def validate_update_request(self, data: Dict[str, Any]) -> ValidationResult:
        """
        更新リクエストのバリデーション
        
        Args:
            data: リクエストデータ
            
        Returns:
            バリデーション結果
        """
        errors = []
        
        # 空のデータチェック
        if not data or all(v is None for v in data.values()):
            errors.append("At least one field must be provided for update")
            return ValidationResult.failure(errors)
        
        # 名前フィールドチェック（提供されている場合）
        if 'name' in data and data['name'] is not None:
            if not isinstance(data['name'], str):
                errors.append("Name must be a string")
            elif len(data['name'].strip()) == 0:
                errors.append("Name cannot be empty")
            elif len(data['name']) > 255:
                errors.append("Name cannot exceed 255 characters")
            elif not self.name_pattern.match(data['name']):
                errors.append("Name contains invalid characters")
        
        # 説明フィールドチェック（提供されている場合）
        if 'description' in data and data['description'] is not None:
            if not isinstance(data['description'], str):
                errors.append("Description must be a string")
            elif len(data['description']) > 1000:
                errors.append("Description cannot exceed 1000 characters")
        
        # ステータスフィールドチェック（提供されている場合）
        if 'status' in data and data['status'] is not None:
            allowed_statuses = ['active', 'inactive', 'draft']
            if data['status'] not in allowed_statuses:
                errors.append(f"Status must be one of: {{', '.join(allowed_statuses)}}")
        
        # メタデータチェック
        if 'metadata' in data and data['metadata'] is not None:
            if not isinstance(data['metadata'], dict):
                errors.append("Metadata must be a dictionary")
            else:
                metadata_str = str(data['metadata'])
                if len(metadata_str) > 5000:
                    errors.append("Metadata is too large (max 5000 characters)")
        
        # セキュリティチェック
        security_errors = self._check_security_violations(data)
        errors.extend(security_errors)
        
        return ValidationResult.success() if not errors else ValidationResult.failure(errors)
    
    def validate_id_parameter(self, id_value: str) -> ValidationResult:
        """
        IDパラメータのバリデーション
        
        Args:
            id_value: ID値
            
        Returns:
            バリデーション結果
        """
        errors = []
        
        if not id_value:
            errors.append("ID is required")
        elif not isinstance(id_value, str):
            errors.append("ID must be a string")
        elif len(id_value) < 1 or len(id_value) > 100:
            errors.append("ID length must be between 1 and 100 characters")
        elif not re.match(r'^[a-zA-Z0-9\-_]+$', id_value):
            errors.append("ID contains invalid characters")
        
        return ValidationResult.success() if not errors else ValidationResult.failure(errors)
    
    def validate_pagination_parameters(self, page: int, limit: int) -> ValidationResult:
        """
        ページネーションパラメータのバリデーション
        
        Args:
            page: ページ番号
            limit: 1ページあたりの件数
            
        Returns:
            バリデーション結果
        """
        errors = []
        
        if page < 1:
            errors.append("Page number must be 1 or greater")
        elif page > 10000:
            errors.append("Page number is too large (max 10000)")
        
        if limit < 1:
            errors.append("Limit must be 1 or greater")
        elif limit > 100:
            errors.append("Limit cannot exceed 100")
        
        return ValidationResult.success() if not errors else ValidationResult.failure(errors)
    
    def _check_security_violations(self, data: Dict[str, Any]) -> List[str]:
        """
        セキュリティ違反をチェック
        
        Args:
            data: チェック対象データ
            
        Returns:
            セキュリティエラー一覧
        """
        errors = []
        
        # SQLインジェクション パターン
        sql_patterns = [
            r'(?i)(union\s+select|select\s+.*\s+from|insert\s+into|update\s+.*\s+set|delete\s+from)',
            r'(?i)(drop\s+table|create\s+table|alter\s+table)',
            r'(?i)(exec\s*\(|execute\s*\()',
            r'[\'"`;].*--',
            r'(?i)(script\s*>|javascript\s*:|vbscript\s*:)',
        ]
        
        # XSSパターン
        xss_patterns = [
            r'(?i)<script[^>]*>.*?</script>',
            r'(?i)<iframe[^>]*>.*?</iframe>',
            r'(?i)javascript\s*:',
            r'(?i)on\w+\s*=',
            r'(?i)<.*?style\s*=.*?expression\s*\(',
        ]
        
        # データ内容をチェック
        for key, value in data.items():
            if isinstance(value, str):
                # SQLインジェクション チェック
                for pattern in sql_patterns:
                    if re.search(pattern, value):
                        errors.append(f"Potential SQL injection detected in field: {{key}}")
                        break
                
                # XSS チェック
                for pattern in xss_patterns:
                    if re.search(pattern, value):
                        errors.append(f"Potential XSS attack detected in field: {{key}}")
                        break
                
                # 過度に長い文字列チェック
                if len(value) > 10000:
                    errors.append(f"Field {{key}} is too long (potential DoS attack)")
        
        return errors
    
    def sanitize_input(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        入力データをサニタイズ
        
        Args:
            data: サニタイズ対象データ
            
        Returns:
            サニタイズされたデータ
        """
        sanitized = {{}}
        
        for key, value in data.items():
            if isinstance(value, str):
                # 前後の空白を削除
                sanitized[key] = value.strip()
            else:
                sanitized[key] = value
        
        return sanitized
'''
    
    return content


def generate_auth_dependencies():
    """認証・認可依存性を生成"""
    
    content = '''"""
Authentication and Authorization Dependencies
認証・認可の依存性注入用ユーティリティ
"""

from typing import Dict, Any, Optional
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from datetime import datetime, timedelta
import os


# JWT設定
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your-secret-key-here")
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION_HOURS = int(os.getenv("JWT_EXPIRATION_HOURS", "24"))

# HTTPBearer認証スキーム
security = HTTPBearer()


class AuthenticationError(Exception):
    """認証エラー"""
    pass


class AuthorizationError(Exception):
    """認可エラー"""
    pass


class User:
    """認証済みユーザー情報"""
    
    def __init__(self, user_id: str, username: str, email: str, roles: list = None, permissions: list = None):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.roles = roles or []
        self.permissions = permissions or []
    
    def has_permission(self, permission: str) -> bool:
        """指定された権限を持っているかチェック"""
        return permission in self.permissions
    
    def has_role(self, role: str) -> bool:
        """指定されたロールを持っているかチェック"""
        return role in self.roles


def create_access_token(data: Dict[str, Any]) -> str:
    """
    アクセストークンを作成
    
    Args:
        data: トークンに含めるデータ
        
    Returns:
        JWTトークン
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=JWT_EXPIRATION_HOURS)
    to_encode.update({"exp": expire})
    
    return jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)


def verify_token(token: str) -> Dict[str, Any]:
    """
    トークンを検証してペイロードを取得
    
    Args:
        token: JWTトークン
        
    Returns:
        デコードされたペイロード
        
    Raises:
        AuthenticationError: トークンが無効な場合
    """
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise AuthenticationError("Token has expired")
    except jwt.JWTError:
        raise AuthenticationError("Could not validate token")


async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    """
    現在の認証済みユーザーを取得
    
    Args:
        credentials: HTTPベアラー認証情報
        
    Returns:
        認証済みユーザー情報
        
    Raises:
        HTTPException: 認証に失敗した場合
    """
    try:
        # トークンを検証
        payload = verify_token(credentials.credentials)
        
        # ユーザー情報を取得（実際の実装では、データベースから取得）
        user_id = payload.get("sub")
        if not user_id:
            raise AuthenticationError("Token missing user ID")
        
        # TODO: データベースからユーザー情報を取得
        # user_repository = get_user_repository()  # DIで注入
        # user = await user_repository.find_by_id(user_id)
        
        # 仮のユーザー情報（実際の実装では、データベースから取得）
        user = User(
            user_id=user_id,
            username=payload.get("username", "unknown"),
            email=payload.get("email", "unknown@example.com"),
            roles=payload.get("roles", []),
            permissions=payload.get("permissions", [])
        )
        
        return user
        
    except AuthenticationError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


def require_permission(permission: str):
    """
    指定された権限を要求する依存性
    
    Args:
        permission: 必要な権限名
        
    Returns:
        依存性関数
    """
    def permission_checker(current_user: User = Depends(get_current_user)) -> User:
        if not current_user.has_permission(permission):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Permission '{permission}' required"
            )
        return current_user
    
    return permission_checker


def require_role(role: str):
    """
    指定されたロールを要求する依存性
    
    Args:
        role: 必要なロール名
        
    Returns:
        依存性関数
    """
    def role_checker(current_user: User = Depends(get_current_user)) -> User:
        if not current_user.has_role(role):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Role '{role}' required"
            )
        return current_user
    
    return role_checker


def require_any_permission(*permissions: str):
    """
    指定された権限のいずれかを要求する依存性
    
    Args:
        permissions: 必要な権限名のリスト
        
    Returns:
        依存性関数
    """
    def any_permission_checker(current_user: User = Depends(get_current_user)) -> User:
        if not any(current_user.has_permission(perm) for perm in permissions):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"One of the following permissions required: {', '.join(permissions)}"
            )
        return current_user
    
    return any_permission_checker


def require_any_role(*roles: str):
    """
    指定されたロールのいずれかを要求する依存性
    
    Args:
        roles: 必要なロール名のリスト
        
    Returns:
        依存性関数
    """
    def any_role_checker(current_user: User = Depends(get_current_user)) -> User:
        if not any(current_user.has_role(role) for role in roles):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"One of the following roles required: {', '.join(roles)}"
            )
        return current_user
    
    return any_role_checker


# オプション: 管理者専用の依存性
def require_admin() -> User:
    """管理者権限を要求"""
    return require_role("admin")


# オプション: ユーザー自身のリソースアクセス許可
def require_resource_ownership(resource_user_id_param: str = "user_id"):
    """
    リソースの所有者本人または管理者のみアクセス許可
    
    Args:
        resource_user_id_param: リソースのユーザーIDが格納されているパラメータ名
        
    Returns:
        依存性関数
    """
    def ownership_checker(
        current_user: User = Depends(get_current_user),
        path_params: dict = None  # TODO: FastAPIのPath依存性から取得
    ) -> User:
        # 管理者は全てのリソースにアクセス可能
        if current_user.has_role("admin"):
            return current_user
        
        # リソースの所有者チェック（実装例）
        resource_user_id = path_params.get(resource_user_id_param) if path_params else None
        if resource_user_id and current_user.user_id != resource_user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied: You can only access your own resources"
            )
        
        return current_user
    
    return ownership_checker
'''
    
    return content


def generate_base_command_handler():
    """CLIコマンドハンドラーのベースクラスを生成"""
    
    content = '''"""
Base Command Handler
CLIコマンドハンドラーのベースクラス
"""

import json
import sys
from typing import Any, Dict, Optional
from pathlib import Path
from abc import ABC, abstractmethod
from argparse import ArgumentParser, Namespace
import colorama
from colorama import Fore, Style


class BaseCommandHandler(ABC):
    """
    CLIコマンドハンドラーのベースクラス
    共通機能とインターフェースを提供
    """
    
    def __init__(self):
        """コンストラクタ"""
        # カラー出力を初期化
        colorama.init(autoreset=True)
    
    @abstractmethod
    def setup_parser(self, parser: ArgumentParser) -> None:
        """
        コマンド引数を設定
        
        Args:
            parser: ArgumentParserインスタンス
        """
        pass
    
    @abstractmethod
    async def run(self, args: Namespace) -> None:
        """
        メインエントリポイント
        
        Args:
            args: パースされた引数
        """
        pass
    
    def print_success(self, message: str) -> None:
        """成功メッセージを表示"""
        print(f"{Fore.GREEN}{message}{Style.RESET_ALL}")
    
    def print_error(self, message: str) -> None:
        """エラーメッセージを表示"""
        print(f"{Fore.RED}{message}{Style.RESET_ALL}", file=sys.stderr)
    
    def print_warning(self, message: str) -> None:
        """警告メッセージを表示"""
        print(f"{Fore.YELLOW}{message}{Style.RESET_ALL}")
    
    def print_info(self, message: str) -> None:
        """情報メッセージを表示"""
        print(f"{Fore.CYAN}{message}{Style.RESET_ALL}")
    
    def print_json(self, data: Any, indent: int = 2) -> None:
        """JSONデータを整形して表示"""
        try:
            json_str = json.dumps(data, indent=indent, ensure_ascii=False, default=str)
            print(json_str)
        except Exception as e:
            self.print_error(f"Failed to format JSON: {e}")
    
    def _load_json_file(self, file_path: str) -> Dict[str, Any]:
        """
        JSONファイルを読み込み
        
        Args:
            file_path: JSONファイルパス
            
        Returns:
            JSONデータ
            
        Raises:
            FileNotFoundError: ファイルが見つからない場合
            ValueError: JSON形式が不正な場合
        """
        path = Path(file_path)
        
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in {file_path}: {e}")
        except Exception as e:
            raise ValueError(f"Failed to read {file_path}: {e}")
    
    def _save_json_file(self, file_path: str, data: Dict[str, Any]) -> None:
        """
        JSONファイルに保存
        
        Args:
            file_path: 保存先パス
            data: 保存するデータ
        """
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False, default=str)
        except Exception as e:
            raise ValueError(f"Failed to save {file_path}: {e}")
    
    def confirm_action(self, message: str, default: bool = False) -> bool:
        """
        ユーザーに確認を求める
        
        Args:
            message: 確認メッセージ
            default: デフォルト値
            
        Returns:
            ユーザーの選択結果
        """
        suffix = " (Y/n)" if default else " (y/N)"
        response = input(f"{message}{suffix}: ").lower().strip()
        
        if not response:
            return default
        
        return response in ['y', 'yes', 'true', '1']
    
    def print_table(self, headers: list, rows: list, max_width: int = 120) -> None:
        """
        テーブル形式で表示
        
        Args:
            headers: ヘッダー一覧
            rows: データ行一覧
            max_width: 最大幅
        """
        if not rows:
            self.print_info("No data to display")
            return
        
        # 列幅を計算
        col_widths = []
        for i, header in enumerate(headers):
            max_len = len(header)
            for row in rows:
                if i < len(row):
                    cell_len = len(str(row[i]))
                    max_len = max(max_len, cell_len)
            col_widths.append(min(max_len + 2, max_width // len(headers)))
        
        # ヘッダー表示
        header_row = ""
        for i, header in enumerate(headers):
            header_row += f"{header:<{col_widths[i]}}"
        print(f"{Fore.CYAN}{header_row}{Style.RESET_ALL}")
        
        # 区切り線
        separator = ""
        for width in col_widths:
            separator += "-" * width
        print(f"{Fore.CYAN}{separator}{Style.RESET_ALL}")
        
        # データ行表示
        for row in rows:
            data_row = ""
            for i, cell in enumerate(row):
                if i < len(col_widths):
                    cell_str = str(cell)
                    if len(cell_str) > col_widths[i] - 2:
                        cell_str = cell_str[:col_widths[i] - 5] + "..."
                    data_row += f"{cell_str:<{col_widths[i]}}"
            print(data_row)
    
    def print_progress(self, current: int, total: int, message: str = "") -> None:
        """
        進捗バーを表示
        
        Args:
            current: 現在の進捗
            total: 全体数
            message: 追加メッセージ
        """
        if total == 0:
            return
        
        percentage = (current / total) * 100
        bar_length = 40
        filled_length = int(bar_length * current // total)
        
        bar = "=" * filled_length + "-" * (bar_length - filled_length)
        print(f"\\r{Fore.GREEN}[{bar}] {percentage:.1f}% {message}{Style.RESET_ALL}", end="")
        
        if current == total:
            print()  # 改行
    
    def handle_keyboard_interrupt(self) -> None:
        """Ctrl+C割り込みハンドリング"""
        self.print_warning("\\nOperation cancelled by user")
        sys.exit(1)
    
    def exit_with_error(self, message: str, exit_code: int = 1) -> None:
        """エラーメッセージを表示して終了"""
        self.print_error(message)
        sys.exit(exit_code)
    
    def exit_with_success(self, message: str = "") -> None:
        """成功メッセージを表示して終了"""
        if message:
            self.print_success(message)
        sys.exit(0)
'''
    
    return content


def implement_presentation_layer(use_case_data, issue_number, use_cases):
    """プレゼンテーション層を実装"""
    
    created_files = []
    
    # ディレクトリ構造作成
    print("📁 プレゼンテーションディレクトリ構造を作成中...")
    created_dirs = create_presentation_directories()
    
    # ベースコマンドハンドラー作成
    print("🔧 ベースコマンドハンドラーを生成中...")
    base_handler_path = Path("src/presentation/cli/handlers/base_handler.py")
    
    with open(base_handler_path, 'w', encoding='utf-8') as f:
        f.write(generate_base_command_handler())
    created_files.append(str(base_handler_path))
    
    # 認証・認可依存性作成
    print("🔐 認証・認可システムを生成中...")
    auth_deps_path = Path("src/presentation/auth/dependencies.py")
    
    with open(auth_deps_path, 'w', encoding='utf-8') as f:
        f.write(generate_auth_dependencies())
    created_files.append(str(auth_deps_path))
    
    # エラーレスポンスモジュール作成
    print("❌ エラーレスポンスモジュールを生成中...")
    error_response_path = Path("src/presentation/api/responses/error_response.py")
    error_response_path.parent.mkdir(parents=True, exist_ok=True)
    
    error_response_content = '''"""
Error Response Module
APIエラーレスポンスの統一処理
"""

from typing import Dict, Any, Optional, List
from datetime import datetime
from pydantic import BaseModel


class ErrorResponse(BaseModel):
    """統一エラーレスポンス"""
    message: str
    code: Optional[str] = None
    details: Optional[Dict[str, Any]] = None
    timestamp: datetime = datetime.utcnow()
    
    @classmethod
    def from_exception(cls, error: Exception) -> "ErrorResponse":
        return cls(
            message=str(error),
            code=error.__class__.__name__
        )
    
    @property
    def status_code(self) -> int:
        """HTTPステータスコードを決定"""
        status_mapping = {
            'ValueError': 400,
            'ValidationError': 400,
            'NotFoundError': 404,
            'PermissionError': 403,
            'AuthenticationError': 401,
        }
        return status_mapping.get(self.code, 500)
'''
    
    with open(error_response_path, 'w', encoding='utf-8') as f:
        f.write(error_response_content)
    created_files.append(str(error_response_path))
    
    # ユースケース対応の実装生成
    if use_cases:
        print(f"🚀 {len(use_cases)}個のユースケース対応実装を生成中...")
        
        for use_case_info in use_cases:
            use_case_name = use_case_info["use_case_name"]
            entity_name = use_case_name.replace("_use_case", "").replace("UseCase", "")
            
            # APIコントローラー
            controller_path = Path(f"src/presentation/api/controllers/{entity_name.lower()}_controller.py")
            controller_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(controller_path, 'w', encoding='utf-8') as f:
                f.write(generate_api_controller(use_case_name, use_case_data))
            created_files.append(str(controller_path))
            
            # CLIコマンド
            cli_command_path = Path(f"src/presentation/cli/commands/{entity_name.lower()}_command.py")
            cli_command_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(cli_command_path, 'w', encoding='utf-8') as f:
                f.write(generate_cli_command(use_case_name, use_case_data))
            created_files.append(str(cli_command_path))
            
            # リクエスト/レスポンスモデル
            serializer_path = Path(f"src/presentation/serializers/{entity_name.lower()}_serializer.py")
            serializer_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(serializer_path, 'w', encoding='utf-8') as f:
                f.write(generate_request_response_models(entity_name, use_case_data))
            created_files.append(str(serializer_path))
            
            # バリデーター
            validator_path = Path(f"src/presentation/validators/{entity_name.lower()}_validator.py")
            validator_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(validator_path, 'w', encoding='utf-8') as f:
                f.write(generate_input_validator(entity_name, use_case_data))
            created_files.append(str(validator_path))
    
    else:
        print("ℹ️ アプリケーション層のユースケースが見つかりません。汎用テンプレートを生成します。")
        
        # 汎用的なサンプル実装
        sample_entity = "example"
        
        # サンプルAPIコントローラー
        sample_controller_path = Path(f"src/presentation/api/controllers/{sample_entity}_controller.py")
        with open(sample_controller_path, 'w', encoding='utf-8') as f:
            f.write(generate_api_controller(f"{sample_entity}_use_case", use_case_data))
        created_files.append(str(sample_controller_path))
        
        # サンプルバリデーター
        sample_validator_path = Path(f"src/presentation/validators/{sample_entity}_validator.py")
        with open(sample_validator_path, 'w', encoding='utf-8') as f:
            f.write(generate_input_validator(sample_entity, use_case_data))
        created_files.append(str(sample_validator_path))
    
    # FastAPIアプリケーションエントリポイント
    print("🌐 FastAPIアプリケーションを生成中...")
    main_app_path = Path("src/presentation/api/main.py")
    main_app_content = '''"""
FastAPI Application Entry Point
APIアプリケーションのメインエントリーポイント
"""

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
import uvicorn
import os

# コントローラーのインポート（実装に合わせて調整）
# from src.presentation.api.controllers.example_controller import router as example_router

app = FastAPI(
    title="Clean Architecture API",
    description="TDD/DDD/Layered Architecture による API 実装",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS", "http://localhost:3000,http://localhost:8000").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 信頼できるホスト設定
trusted_hosts = os.getenv("TRUSTED_HOSTS", "localhost,127.0.0.1").split(",")
app.add_middleware(TrustedHostMiddleware, allowed_hosts=trusted_hosts)

# ルーター登録（実装に合わせてコメントアウト解除）
# app.include_router(example_router, prefix="/api/v1")

# ヘルスチェックエンドポイント
@app.get("/health")
async def health_check():
    """ヘルスチェック"""
    return {"status": "healthy", "message": "API is running"}

# グローバル例外ハンドラー
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """グローバル例外ハンドラー"""
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "message": "Internal server error",
            "detail": str(exc) if os.getenv("DEBUG") == "true" else "An error occurred"
        }
    )

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", "8000")),
        reload=os.getenv("DEBUG", "false").lower() == "true"
    )
'''
    
    with open(main_app_path, 'w', encoding='utf-8') as f:
        f.write(main_app_content)
    created_files.append(str(main_app_path))
    
    return created_files


def update_use_case_json_with_presentation(json_file_path, created_files):
    """ユースケースJSONにプレゼンテーション層情報を更新"""
    
    use_case_data = load_use_case_json(json_file_path)
    
    # アーキテクチャ整合性情報を更新
    architecture = use_case_data.get("architecture_alignment", {})
    architecture.setdefault("layers", {})["presentation"] = True  # 実装完了
    architecture.setdefault("patterns_used", []).extend([
        "API Controller Pattern",
        "Request/Response Pattern",
        "Input Validation Pattern", 
        "Authentication/Authorization Pattern",
        "CLI Command Pattern"
    ])
    use_case_data["architecture_alignment"] = architecture
    
    # 実装情報を記録
    presentation_info = use_case_data.get("implementation_details", {})
    presentation_info["presentation_layer"] = {
        "implemented": True,
        "files_created": created_files,
        "components": [
            "API Controllers",
            "CLI Commands",
            "Request/Response Models",
            "Input Validators",
            "Authentication System",
            "Error Handling"
        ],
        "completed_at": datetime.now().isoformat()
    }
    use_case_data["implementation_details"] = presentation_info
    
    # 保存
    save_use_case_json(json_file_path, use_case_data)
    
    return use_case_data


def main():
    """メイン処理"""
    
    # 引数チェック
    if len(sys.argv) < 2:
        print("❌ エラー: Issue番号が必要です")
        print("使用方法: /implement-presentation <issue-number>")
        sys.exit(1)
    
    issue_number = sys.argv[1]
    print(f"\n🎨 Issue #{issue_number} のプレゼンテーション層実装を開始します\n")
    
    # ユースケースJSONファイルを検索
    print("📁 ユースケースJSONファイルを検索中...")
    json_file_path = find_use_case_json(issue_number)
    
    if not json_file_path:
        print(f"❌ Issue #{issue_number} のユースケースJSONが見つかりません")
        print("先に /create-use-case コマンドを実行してください")
        sys.exit(1)
    
    print(f"✅ JSONファイルを発見: {json_file_path}")
    
    # ユースケースデータを読み込み
    print("📝 ユースケースデータを読み込み中...")
    use_case_data = load_use_case_json(json_file_path)
    
    # アプリケーション層のユースケースを分析
    print("🔍 アプリケーション層のユースケースを分析中...")
    use_cases = analyze_application_layer("src/application")
    
    if use_cases:
        print(f"✅ {len(use_cases)}個のユースケースを発見")
        for use_case_info in use_cases:
            print(f"  - {use_case_info['use_case_name']}")
    else:
        print("ℹ️ アプリケーション層のユースケースが見つかりません")
        print("汎用的なプレゼンテーション層テンプレートを生成します")
    
    # プレゼンテーション層を実装
    print("🎨 プレゼンテーション層実装を開始中...")
    created_files = implement_presentation_layer(use_case_data, issue_number, use_cases)
    
    print(f"✅ プレゼンテーション層実装完了: {len(created_files)}個のファイル作成")
    
    # ユースケースJSONにプレゼンテーション層情報を更新
    print("📊 ユースケースJSONを更新中...")
    updated_data = update_use_case_json_with_presentation(json_file_path, created_files)
    
    # 実行履歴を更新
    update_execution_history(
        json_file_path,
        f"/implement-presentation {issue_number}",
        "success",
        created_files
    )
    
    # 最新データを読み込んで表示
    final_data = load_use_case_json(json_file_path)
    
    # 実行状況を表示
    print("\n" + "="*60)
    print(format_execution_status(final_data))
    print("="*60)
    
    # サマリー表示
    print(f"\n📊 実行サマリー")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"🎨 プレゼンテーション層実装: 完了")
    print(f"✅ ユースケース対応数: {len(use_cases)}個")
    print(f"✅ 作成ファイル数: {len(created_files)}個")
    print(f"✅ API コントローラー: 完了")
    print(f"✅ CLI コマンド: 完了")
    print(f"✅ 認証・認可: 完了")
    
    print(f"\n📁 成果物")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    for file_path in created_files:
        print(f"✅ {file_path}")
    
    print(f"\n⏭️ 次の推奨コマンド")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"1. /run-all-tests {issue_number}")
    print(f"   → 全システムテスト実行と品質確認")
    print(f"2. セキュリティ設定の確認")
    print(f"   → JWT_SECRET_KEY等の環境変数設定")
    print(f"3. API動作確認")
    print(f"   → FastAPIサーバー起動とエンドポイントテスト")
    
    print(f"\n💡 プレゼンテーション層実装完了")
    print(f"システム全体が完成しました。テストとデプロイの準備が整いました。")


if __name__ == "__main__":
    main()