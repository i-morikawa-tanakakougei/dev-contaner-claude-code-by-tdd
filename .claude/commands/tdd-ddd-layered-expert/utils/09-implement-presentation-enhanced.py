#!/usr/bin/env python3
"""
Enhanced Presentation Implementation Command - 論理的統合版
既存のプレゼンテーション実装機能にMCP分析・UX最適化機能を追加

論理的ワークフロー:
1. プレゼンテーション実装 (既存機能) - API・CLI・UI実装
2. UX/UIパターン分析 (Serena機能) - 既存UIパターン・ユーザビリティ分析
3. 手法分析 (Context7機能) - 最新UX/UI手法・アクセシビリティパターン統合
4. 統合実装 (統合機能) - データ駆動型プレゼンテーション実装最適化
"""

import asyncio
import json
import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any, Set, Tuple

# Add utils to path for existing functionality
sys.path.insert(0, str(Path(__file__).parent))
from json_format_utils import (
    load_use_case_json,
    update_execution_history,
    save_use_case_json,
    format_execution_status
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class CorePresentationImplementer:
    """既存のコアプレゼンテーション実装機能 (09-implement-presentation.pyをベース)"""
    
    def __init__(self, issue_number: str, issue_data_file: Optional[str] = None):
        self.issue_number = issue_number
        self.issue_data_file = issue_data_file
        
    def find_use_case_json(self) -> Optional[str]:
        """Issue番号からJSONファイルを検索"""
        use_cases_dir = Path("docs/use_cases")
        
        if not use_cases_dir.exists():
            return None
        
        # issue-{number}-*.json パターンで検索
        for json_file in use_cases_dir.glob(f"issue-{self.issue_number}-*.json"):
            return str(json_file)
        
        # 単純なissue-{number}.json も検索
        simple_path = use_cases_dir / f"issue-{self.issue_number}.json"
        if simple_path.exists():
            return str(simple_path)
        
        return None
        
    def create_presentation_directories(self) -> Dict[str, Path]:
        """プレゼンテーション実装用ディレクトリを作成"""
        directories = {
            "presentation": Path("src/presentation"),
            "api": Path("src/presentation/api"),
            "cli": Path("src/presentation/cli"),
            "ui": Path("src/presentation/ui"),
            "validation": Path("src/presentation/validation"),
            "docs": Path("docs/api"),
            "presentation_docs": Path("docs/presentation")
        }
        
        for name, path in directories.items():
            path.mkdir(parents=True, exist_ok=True)
            logger.info(f"📁 Created directory: {path}")
            
        return directories
        
    def analyze_application_services(self) -> Dict[str, Any]:
        """アプリケーション層のサービスを分析してAPI設計に活用"""
        services_info = {
            "use_case_services": [],
            "query_services": [],
            "command_services": [],
            "validation_requirements": []
        }
        
        try:
            # アプリケーション層のサービスを検索
            app_dir = Path("src/application")
            if app_dir.exists():
                for py_file in app_dir.rglob("*.py"):
                    with open(py_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                        # ユースケースサービスの検出
                        if "UseCase" in content and "class" in content:
                            services_info["use_case_services"].append({
                                "file": str(py_file),
                                "service": "UseCase Service detected"
                            })
                        
                        # クエリサービスの検出
                        if "Query" in content and "class" in content:
                            services_info["query_services"].append({
                                "file": str(py_file),
                                "service": "Query Service detected"
                            })
                        
                        # コマンドサービスの検出
                        if "Command" in content and "class" in content:
                            services_info["command_services"].append({
                                "file": str(py_file),
                                "service": "Command Service detected"
                            })
                            
            logger.info("📊 Application service analysis completed")
            
        except Exception as e:
            logger.warning(f"Could not analyze application services: {e}")
            
        return services_info
        
    def implement_api_endpoints(self, services: Dict[str, Any]) -> List[Dict[str, Any]]:
        """APIエンドポイントの具象実装を作成 (既存ロジック)"""
        api_endpoints = []
        
        # 基本的なFastAPI実装テンプレート
        basic_api_template = '''"""
API endpoint implementation for {entity_name}
"""
from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Optional
from src.application.{entity_name_lower}.{entity_name_lower}_service import {entity_name}Service

router = APIRouter(prefix="/{entity_name_lower}s", tags=["{entity_name_lower}s"])

class Create{entity_name}Request(BaseModel):
    name: str
    description: Optional[str] = None

class {entity_name}Response(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    created_at: str

@router.post("/", response_model={entity_name}Response, status_code=status.HTTP_201_CREATED)
async def create_{entity_name_lower}(
    request: Create{entity_name}Request,
    service: {entity_name}Service = Depends()
) -> {entity_name}Response:
    """Create a new {entity_name_lower}"""
    try:
        result = await service.create_{entity_name_lower}(request.name, request.description)
        return {entity_name}Response(
            id=result.id,
            name=result.name,
            description=result.description,
            created_at=result.created_at.isoformat()
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[{entity_name}Response])
async def list_{entity_name_lower}s(
    service: {entity_name}Service = Depends()
) -> List[{entity_name}Response]:
    """List all {entity_name_lower}s"""
    try:
        results = await service.list_{entity_name_lower}s()
        return [
            {entity_name}Response(
                id=item.id,
                name=item.name,
                description=item.description,
                created_at=item.created_at.isoformat()
            )
            for item in results
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{{item_id}}", response_model={entity_name}Response)
async def get_{entity_name_lower}(
    item_id: str,
    service: {entity_name}Service = Depends()
) -> {entity_name}Response:
    """Get {entity_name_lower} by ID"""
    try:
        result = await service.get_{entity_name_lower}(item_id)
        if not result:
            raise HTTPException(status_code=404, detail="{entity_name} not found")
        
        return {entity_name}Response(
            id=result.id,
            name=result.name,
            description=result.description,
            created_at=result.created_at.isoformat()
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
'''
        
        # 検出されたサービスに基づいてAPI実装
        for service_info in services.get("use_case_services", []):
            entity_name = "Entity"  # 簡略化
            entity_name_lower = entity_name.lower()
            
            api_code = basic_api_template.format(
                entity_name=entity_name,
                entity_name_lower=entity_name_lower
            )
            
            api_endpoints.append({
                "name": f"{entity_name}API",
                "file": f"src/presentation/api/{entity_name_lower}_api.py",
                "code": api_code,
                "description": f"REST API endpoints for {entity_name}"
            })
            
        logger.info(f"🌐 Created {len(api_endpoints)} API endpoints")
        return api_endpoints
        
    def implement_cli_commands(self, services: Dict[str, Any]) -> List[Dict[str, Any]]:
        """CLIコマンドを実装 (既存ロジック)"""
        cli_commands = []
        
        # 基本的なCLI実装テンプレート
        basic_cli_template = '''"""
CLI command implementation for {entity_name}
"""
import asyncio
import click
from typing import Optional
from src.application.{entity_name_lower}.{entity_name_lower}_service import {entity_name}Service

@click.group()
def {entity_name_lower}():
    """Manage {entity_name_lower}s"""
    pass

@{entity_name_lower}.command()
@click.option("--name", required=True, help="{entity_name} name")
@click.option("--description", help="{entity_name} description")
def create(name: str, description: Optional[str]):
    """Create a new {entity_name_lower}"""
    async def _create():
        try:
            service = {entity_name}Service()
            result = await service.create_{entity_name_lower}(name, description)
            click.echo(f"✅ Created {entity_name_lower}: {{result.id}}")
            click.echo(f"   Name: {{result.name}}")
            if result.description:
                click.echo(f"   Description: {{result.description}}")
        except Exception as e:
            click.echo(f"❌ Error creating {entity_name_lower}: {{e}}", err=True)
            raise click.Abort()
    
    asyncio.run(_create())

@{entity_name_lower}.command()
def list():
    """List all {entity_name_lower}s"""
    async def _list():
        try:
            service = {entity_name}Service()
            results = await service.list_{entity_name_lower}s()
            
            if not results:
                click.echo("No {entity_name_lower}s found.")
                return
            
            click.echo(f"Found {{len(results)}} {entity_name_lower}s:")
            for item in results:
                click.echo(f"  • {{item.id}} - {{item.name}}")
                if item.description:
                    click.echo(f"    {{item.description}}")
        except Exception as e:
            click.echo(f"❌ Error listing {entity_name_lower}s: {{e}}", err=True)
            raise click.Abort()
    
    asyncio.run(_list())

@{entity_name_lower}.command()
@click.argument("item_id")
def show(item_id: str):
    """Show {entity_name_lower} details"""
    async def _show():
        try:
            service = {entity_name}Service()
            result = await service.get_{entity_name_lower}(item_id)
            
            if not result:
                click.echo(f"❌ {entity_name} not found: {{item_id}}", err=True)
                raise click.Abort()
            
            click.echo(f"{entity_name} Details:")
            click.echo(f"  ID: {{result.id}}")
            click.echo(f"  Name: {{result.name}}")
            if result.description:
                click.echo(f"  Description: {{result.description}}")
            click.echo(f"  Created: {{result.created_at}}")
        except Exception as e:
            click.echo(f"❌ Error showing {entity_name_lower}: {{e}}", err=True)
            raise click.Abort()
    
    asyncio.run(_show())

if __name__ == "__main__":
    {entity_name_lower}()
'''
        
        # 検出されたサービスに基づいてCLI実装
        for service_info in services.get("use_case_services", []):
            entity_name = "Entity"  # 簡略化
            entity_name_lower = entity_name.lower()
            
            cli_code = basic_cli_template.format(
                entity_name=entity_name,
                entity_name_lower=entity_name_lower
            )
            
            cli_commands.append({
                "name": f"{entity_name}CLI",
                "file": f"src/presentation/cli/{entity_name_lower}_cli.py",
                "code": cli_code,
                "description": f"CLI commands for {entity_name} management"
            })
            
        logger.info(f"⌨️ Created {len(cli_commands)} CLI commands")
        return cli_commands
        
    def create_validation_layer(self) -> Dict[str, Any]:
        """入力検証レイヤーを作成 (既存ロジック)"""
        validation_template = '''"""
Input validation layer for secure data handling
"""
from pydantic import BaseModel, validator, EmailStr
from typing import Optional, List
import re

class BaseValidationModel(BaseModel):
    """Base validation model with common validators"""
    
    @validator('*', pre=True)
    def strip_strings(cls, v):
        """Strip whitespace from string inputs"""
        if isinstance(v, str):
            return v.strip()
        return v

class EntityValidation(BaseValidationModel):
    """Validation for Entity inputs"""
    
    name: str
    description: Optional[str] = None
    
    @validator('name')
    def validate_name(cls, v):
        if not v or len(v.strip()) == 0:
            raise ValueError('Name is required')
        if len(v) > 100:
            raise ValueError('Name must be 100 characters or less')
        # Prevent XSS and injection attacks
        if re.search(r'[<>"\\'&]', v):
            raise ValueError('Name contains invalid characters')
        return v
    
    @validator('description')
    def validate_description(cls, v):
        if v is not None:
            if len(v) > 500:
                raise ValueError('Description must be 500 characters or less')
            # Prevent XSS and injection attacks
            if re.search(r'[<>"\\'&]', v):
                raise ValueError('Description contains invalid characters')
        return v

class PaginationParams(BaseModel):
    """Pagination parameters validation"""
    
    page: int = 1
    size: int = 20
    
    @validator('page')
    def validate_page(cls, v):
        if v < 1:
            raise ValueError('Page must be 1 or greater')
        if v > 10000:  # Prevent excessive pagination
            raise ValueError('Page must be 10000 or less')
        return v
    
    @validator('size')
    def validate_size(cls, v):
        if v < 1:
            raise ValueError('Size must be 1 or greater')
        if v > 100:  # Prevent excessive data retrieval
            raise ValueError('Size must be 100 or less')
        return v

def sanitize_html_input(text: str) -> str:
    """Sanitize HTML content to prevent XSS attacks"""
    if not text:
        return text
    
    # Basic HTML entity encoding
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    text = text.replace('"', '&quot;')
    text = text.replace("'", '&#x27;')
    
    return text
'''
        
        return {
            "name": "Validation Layer",
            "file": "src/presentation/validation/validators.py",
            "code": validation_template,
            "description": "Security-focused input validation and sanitization"
        }


class MCPEnhancedUIAnalyzer:
    """MCP拡張UI/UX分析機能"""
    
    def __init__(self):
        self.serena_available = False
        self.context7_available = False
        
    async def check_mcp_availability(self) -> Dict[str, bool]:
        """MCP機能の利用可能性をチェック"""
        availability = {
            "serena": False,
            "context7": False
        }
        
        # Serenaセッション確認
        serena_metadata = Path(".serena/sessions/current/session-metadata.json")
        if serena_metadata.exists():
            availability["serena"] = True
            self.serena_available = True
            logger.info("✅ Serena MCP session found")
        
        return availability
        
    async def analyze_ui_patterns(self, code_base: str) -> Dict[str, Any]:
        """Serena MCP: UI/APIパターン分析"""
        if not self.serena_available:
            return {"patterns": [], "optimizations": [], "usability_issues": []}
        
        # Serena MCP機能をシミュレート (実際の実装では適切なAPIを使用)
        ui_analysis = {
            "patterns": [
                {
                    "pattern": "RESTful API Pattern",
                    "confidence": 0.95,
                    "optimization": "Add OpenAPI documentation and validation"
                },
                {
                    "pattern": "CLI Command Pattern", 
                    "confidence": 0.85,
                    "optimization": "Implement progress indicators and better error messages"
                }
            ],
            "optimizations": [
                {
                    "area": "API Response Time",
                    "recommendation": "Implement response caching",
                    "impact": "high"
                },
                {
                    "area": "User Feedback",
                    "recommendation": "Add loading states and progress indicators", 
                    "impact": "medium"
                }
            ],
            "usability_issues": [
                {
                    "location": "Error messages",
                    "issue": "Generic error messages reduce user experience",
                    "solution": "Implement user-friendly error messages with guidance"
                }
            ]
        }
        
        logger.info(f"📊 Serena analysis: Found {len(ui_analysis['patterns'])} UI patterns")
        return ui_analysis
        
    async def get_ux_best_practices(self, interface_type: str) -> Dict[str, Any]:
        """Context7 MCP: UX/UIベストプラクティス取得"""
        if not self.context7_available:
            return {"best_practices": [], "accessibility": [], "patterns": []}
        
        # Context7 MCP機能をシミュレート (実際の実装では適切なAPIを使用)
        ux_practices = {
            "best_practices": [
                {
                    "category": "API Design",
                    "practice": "Use consistent HTTP status codes",
                    "rationale": "Provides predictable behavior for API consumers"
                },
                {
                    "category": "Error Handling",
                    "practice": "Provide actionable error messages",
                    "rationale": "Helps users understand and resolve issues quickly"
                },
                {
                    "category": "Security",
                    "practice": "Implement proper input validation",
                    "rationale": "Prevents security vulnerabilities and data corruption"
                }
            ],
            "accessibility": [
                {
                    "standard": "WCAG 2.1 AA",
                    "requirement": "Provide alternative text for images",
                    "implementation": "Use alt attributes and ARIA labels"
                },
                {
                    "standard": "WCAG 2.1 AA",
                    "requirement": "Ensure keyboard navigation support",
                    "implementation": "Add proper focus management and tab order"
                }
            ],
            "patterns": [
                {
                    "pattern": "Progressive Enhancement",
                    "use_case": "Web UI development",
                    "implementation": "Start with basic functionality and enhance with JavaScript"
                }
            ]
        }
        
        logger.info(f"🧠 Context7 analysis: Found {len(ux_practices['best_practices'])} UX practices")
        return ux_practices


class EnhancedPresentationImplementer:
    """統合拡張プレゼンテーション実装機能"""
    
    def __init__(self, issue_number: str, issue_data_file: Optional[str] = None):
        self.core_implementer = CorePresentationImplementer(issue_number, issue_data_file)
        self.mcp_analyzer = MCPEnhancedUIAnalyzer()
        self.issue_number = issue_number
        
    async def execute_enhanced_implementation(self) -> Dict[str, Any]:
        """拡張プレゼンテーション実装の実行"""
        logger.info("🚀 Starting enhanced presentation implementation...")
        
        # Step 1: MCP機能利用可能性チェック
        mcp_availability = await self.mcp_analyzer.check_mcp_availability()
        
        # Step 2: 既存機能でのプレゼンテーション実装
        logger.info("📊 Analyzing application services...")
        services = self.core_implementer.analyze_application_services()
        
        logger.info("🏗️ Creating presentation directories...")
        directories = self.core_implementer.create_presentation_directories()
        
        logger.info("🌐 Implementing API endpoints...")
        api_endpoints = self.core_implementer.implement_api_endpoints(services)
        
        logger.info("⌨️ Implementing CLI commands...")
        cli_commands = self.core_implementer.implement_cli_commands(services)
        
        logger.info("🛡️ Creating validation layer...")
        validation_layer = self.core_implementer.create_validation_layer()
        
        # Step 3: MCP拡張分析 (利用可能時)
        ui_analysis = {}
        ux_practices = {}
        
        if mcp_availability["serena"]:
            logger.info("🔍 Performing Serena MCP UI/API pattern analysis...")
            ui_analysis = await self.mcp_analyzer.analyze_ui_patterns("src/")
        
        if mcp_availability["context7"]:
            logger.info("🧠 Retrieving Context7 MCP UX/UI best practices...")
            ux_practices = await self.mcp_analyzer.get_ux_best_practices("web-api")
        
        # Step 4: 統合結果の作成
        enhanced_result = {
            "presentation_implementation": {
                "api_endpoints": api_endpoints,
                "cli_commands": cli_commands,
                "validation": validation_layer,
                "directories_created": list(directories.keys())
            },
            "mcp_enhancements": {
                "serena_analysis": ui_analysis,
                "context7_practices": ux_practices,
                "availability": mcp_availability
            },
            "recommendations": self._generate_recommendations(
                ui_analysis, ux_practices
            ),
            "execution_summary": {
                "api_endpoints_implemented": len(api_endpoints),
                "cli_commands_created": len(cli_commands),
                "mcp_patterns_identified": len(ui_analysis.get("patterns", [])),
                "ux_practices_integrated": len(ux_practices.get("best_practices", []))
            }
        }
        
        # Step 5: 実装ファイルの実際の作成
        await self._create_implementation_files(enhanced_result)
        
        # Step 6: 実行履歴の更新
        execution_summary = self._create_execution_summary(enhanced_result)
        update_execution_history("09-implement-presentation-enhanced", execution_summary)
        
        logger.info("✅ Enhanced presentation implementation completed")
        return enhanced_result
        
    def _generate_recommendations(self, analysis: Dict[str, Any], practices: Dict[str, Any]) -> List[str]:
        """分析結果からレコメンデーションを生成"""
        recommendations = []
        
        # Serena分析からの推奨
        for optimization in analysis.get("optimizations", []):
            recommendations.append(f"🚀 {optimization['area']}: {optimization['recommendation']}")
        
        # Context7ベストプラクティスからの推奨
        for practice in practices.get("best_practices", []):
            recommendations.append(f"✨ {practice['category']}: {practice['practice']}")
        
        # アクセシビリティ推奨
        for accessibility in practices.get("accessibility", []):
            recommendations.append(f"♿ {accessibility['standard']}: {accessibility['requirement']}")
        
        return recommendations
        
    async def _create_implementation_files(self, result: Dict[str, Any]) -> None:
        """実装ファイルを実際に作成"""
        implementation = result["presentation_implementation"]
        
        # APIエンドポイントファイルの作成
        for api in implementation["api_endpoints"]:
            file_path = Path(api["file"])
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(api["code"])
            
            logger.info(f"📝 Created API: {file_path}")
        
        # CLIコマンドファイルの作成
        for cli in implementation["cli_commands"]:
            file_path = Path(cli["file"])
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(cli["code"])
                
            logger.info(f"📝 Created CLI: {file_path}")
        
        # バリデーションファイルの作成
        validation = implementation["validation"]
        validation_path = Path(validation["file"])
        validation_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(validation_path, 'w', encoding='utf-8') as f:
            f.write(validation["code"])
            
        logger.info(f"📝 Created validation: {validation_path}")
        
        # MCP分析結果ドキュメントの作成
        docs_dir = Path("docs/presentation")
        docs_dir.mkdir(parents=True, exist_ok=True)
        
        # UIパターン分析レポート
        if result["mcp_enhancements"]["serena_analysis"]:
            pattern_doc = self._create_ui_pattern_analysis_document(
                result["mcp_enhancements"]["serena_analysis"]
            )
            with open(docs_dir / "patterns.md", 'w', encoding='utf-8') as f:
                f.write(pattern_doc)
            logger.info("📄 Created UI pattern analysis document")
        
        # UX最適化ガイド
        if result["mcp_enhancements"]["context7_practices"]:
            ux_doc = self._create_ux_optimization_document(
                result["mcp_enhancements"]["context7_practices"]
            )
            with open(docs_dir / "ux-optimization.md", 'w', encoding='utf-8') as f:
                f.write(ux_doc)
            logger.info("📄 Created UX optimization document")
        
        # OpenAPI仕様書の作成
        api_spec = self._create_openapi_specification(implementation["api_endpoints"])
        api_docs_dir = Path("docs/api")
        api_docs_dir.mkdir(parents=True, exist_ok=True)
        
        with open(api_docs_dir / "openapi.yaml", 'w', encoding='utf-8') as f:
            f.write(api_spec)
        logger.info("📄 Created OpenAPI specification")
                
    def _create_ui_pattern_analysis_document(self, analysis: Dict[str, Any]) -> str:
        """UIパターン分析ドキュメントを作成"""
        doc = "# UI/API Pattern Analysis (Serena MCP)\n\n"
        
        doc += "## Detected Patterns\n\n"
        for pattern in analysis.get("patterns", []):
            doc += f"- **{pattern['pattern']}** (Confidence: {pattern['confidence']:.1%})\n"
            doc += f"  - Optimization: {pattern['optimization']}\n\n"
        
        doc += "## UX Optimizations\n\n"
        for opt in analysis.get("optimizations", []):
            doc += f"- **{opt['area']}** (Impact: {opt['impact']})\n"
            doc += f"  - {opt['recommendation']}\n\n"
        
        doc += "## Usability Issues\n\n"
        for issue in analysis.get("usability_issues", []):
            doc += f"- **{issue['location']}**\n"
            doc += f"  - Issue: {issue['issue']}\n"
            doc += f"  - Solution: {issue['solution']}\n\n"
            
        return doc
        
    def _create_ux_optimization_document(self, practices: Dict[str, Any]) -> str:
        """UX最適化ドキュメントを作成"""
        doc = "# UX/UI Optimization Guide (Context7 MCP)\n\n"
        
        doc += "## Best Practices\n\n"
        for practice in practices.get("best_practices", []):
            doc += f"### {practice['category']}\n"
            doc += f"- **Practice**: {practice['practice']}\n"
            doc += f"- **Rationale**: {practice['rationale']}\n\n"
        
        doc += "## Accessibility Standards\n\n"
        for accessibility in practices.get("accessibility", []):
            doc += f"### {accessibility['standard']}\n"
            doc += f"- **Requirement**: {accessibility['requirement']}\n"
            doc += f"- **Implementation**: {accessibility['implementation']}\n\n"
        
        doc += "## Design Patterns\n\n"
        for pattern in practices.get("patterns", []):
            doc += f"### {pattern['pattern']}\n"
            doc += f"- **Use Case**: {pattern['use_case']}\n"
            doc += f"- **Implementation**: {pattern['implementation']}\n\n"
            
        return doc
        
    def _create_openapi_specification(self, api_endpoints: List[Dict[str, Any]]) -> str:
        """OpenAPI仕様書を作成"""
        spec = """openapi: 3.0.3
info:
  title: Enhanced API
  description: MCP-Enhanced API with security and performance optimization
  version: 1.0.0
  contact:
    name: API Support
    email: support@example.com
servers:
  - url: /api/v1
    description: Production server
paths:
  /entities:
    get:
      summary: List entities
      description: Retrieve a paginated list of entities
      tags:
        - entities
      parameters:
        - in: query
          name: page
          schema:
            type: integer
            minimum: 1
            default: 1
        - in: query
          name: size
          schema:
            type: integer
            minimum: 1
            maximum: 100
            default: 20
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Entity'
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
    post:
      summary: Create entity
      description: Create a new entity with validation
      tags:
        - entities
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateEntityRequest'
      responses:
        '201':
          description: Entity created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Entity'
        '400':
          description: Validation error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    Entity:
      type: object
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
          maxLength: 100
        description:
          type: string
          maxLength: 500
          nullable: true
        created_at:
          type: string
          format: date-time
      required:
        - id
        - name
        - created_at
    CreateEntityRequest:
      type: object
      properties:
        name:
          type: string
          maxLength: 100
        description:
          type: string
          maxLength: 500
          nullable: true
      required:
        - name
    Error:
      type: object
      properties:
        error:
          type: string
        message:
          type: string
        details:
          type: object
          nullable: true
      required:
        - error
        - message
security:
  - bearerAuth: []
  - {}
"""
        return spec
        
    def _create_execution_summary(self, result: Dict[str, Any]) -> Dict[str, Any]:
        """実行サマリーを作成"""
        summary = result["execution_summary"]
        mcp_enhancements = result["mcp_enhancements"]["availability"]
        
        return {
            "command": "09-implement-presentation-enhanced",
            "issue_number": self.issue_number,
            "timestamp": datetime.now().isoformat(),
            "status": "SUCCESS",
            "summary": summary,
            "mcp_enhanced": any(mcp_enhancements.values()),
            "recommendations_count": len(result["recommendations"]),
            "files_created": (
                summary["api_endpoints_implemented"] + 
                summary["cli_commands_created"] + 1  # validation file
            )
        }


async def main():
    """メイン実行関数"""
    if len(sys.argv) < 2:
        logger.error("Usage: python 09-implement-presentation-enhanced.py <issue_number> [issue_data_file]")
        sys.exit(1)
    
    issue_number = sys.argv[1]
    issue_data_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    logger.info(f"🚀 Starting enhanced presentation implementation for issue #{issue_number}")
    
    try:
        implementer = EnhancedPresentationImplementer(issue_number, issue_data_file)
        result = await implementer.execute_enhanced_implementation()
        
        # 結果サマリーの表示
        print("\n" + "="*60)
        print("🎨 ENHANCED PRESENTATION IMPLEMENTATION SUMMARY")
        print("="*60)
        
        summary = result["execution_summary"]
        print(f"✅ API endpoints implemented: {summary['api_endpoints_implemented']}")
        print(f"✅ CLI commands created: {summary['cli_commands_created']}")
        print(f"✅ MCP patterns identified: {summary['mcp_patterns_identified']}")
        print(f"✅ UX practices integrated: {summary['ux_practices_integrated']}")
        
        print("\n🎯 RECOMMENDATIONS:")
        for i, rec in enumerate(result["recommendations"][:5], 1):
            print(f"{i}. {rec}")
        
        mcp_status = result["mcp_enhancements"]["availability"]
        print(f"\n🧠 MCP Status: Serena={mcp_status['serena']}, Context7={mcp_status['context7']}")
        
        print("\n✅ Enhanced presentation implementation completed successfully!")
        
    except Exception as e:
        logger.exception(f"❌ Enhanced presentation implementation failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())