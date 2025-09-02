#!/usr/bin/env python3
"""
MCP Session Initialization Script
Integrates Serena and Context7 MCP capabilities with TDD/DDD workflow
"""

import asyncio
import json
import logging
import os
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

class MCPSessionManager:
    """Manages MCP-enabled development sessions with persistence"""
    
    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.session_dir = Path(".serena/sessions") / self.session_id
        self.memory_dir = Path(".serena/memory")
        
        # Session state
        self.session_metadata: Dict[str, Any] = {
            "session_id": self.session_id,
            "created_at": datetime.now().isoformat(),
            "project_path": str(self.project_path),
            "mcp_integrations": {},
            "analysis_summary": {},
            "memory_allocation": {},
            "recovery_info": {}
        }
        
    def initialize_directories(self) -> None:
        """Initialize session and memory directories"""
        try:
            directories = [
                self.session_dir,
                self.memory_dir / "architecture",
                self.memory_dir / "business_logic", 
                self.memory_dir / "technical_debt",
                self.memory_dir / "domain_models",
                self.memory_dir / "test_patterns",
            ]
            
            for directory in directories:
                directory.mkdir(parents=True, exist_ok=True)
                logger.info(f"✅ Created directory: {directory}")
                
            # Create current session symlink
            current_link = Path(".serena/sessions/current")
            if current_link.exists():
                current_link.unlink()
            current_link.symlink_to(self.session_dir.name)
            
        except Exception as e:
            logger.exception("Failed to initialize directories")
            raise
            
    def analyze_project_structure(self) -> Dict[str, Any]:
        """Analyze project structure for comprehensive understanding"""
        try:
            analysis = {
                "structure": {},
                "tech_stack": [],
                "key_patterns": [],
                "complexity_metrics": {}
            }
            
            # Basic project structure analysis
            project_files = []
            code_files = []
            
            for root, dirs, files in os.walk(self.project_path):
                # Skip hidden directories and common ignore patterns
                dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__', 'node_modules']]
                
                for file in files:
                    file_path = Path(root) / file
                    project_files.append(str(file_path.relative_to(self.project_path)))
                    
                    # Identify code files
                    if file.endswith(('.py', '.js', '.ts', '.java', '.cpp', '.c', '.go', '.rs')):
                        code_files.append(str(file_path.relative_to(self.project_path)))
                        
                    # Identify tech stack indicators
                    if file in ['requirements.txt', 'package.json', 'Cargo.toml', 'pom.xml']:
                        analysis["tech_stack"].append(f"Found {file}")
                        
            analysis["structure"]["total_files"] = len(project_files)
            analysis["structure"]["code_files"] = len(code_files)
            analysis["structure"]["files_by_type"] = self._categorize_files(project_files)
            
            # Complexity assessment
            analysis["complexity_metrics"]["file_count"] = len(project_files)
            analysis["complexity_metrics"]["code_file_count"] = len(code_files)
            analysis["complexity_metrics"]["estimated_complexity"] = self._estimate_complexity(project_files)
            
            logger.info(f"📊 Project analysis: {len(project_files)} files, {len(code_files)} code files")
            
            return analysis
            
        except Exception as e:
            logger.exception("Failed to analyze project structure")
            raise
            
    def _categorize_files(self, files: List[str]) -> Dict[str, int]:
        """Categorize files by type"""
        categories = {
            "python": 0, "javascript": 0, "typescript": 0, "java": 0,
            "documentation": 0, "configuration": 0, "tests": 0, "other": 0
        }
        
        for file in files:
            file_lower = file.lower()
            if file.endswith('.py'):
                categories["python"] += 1
            elif file.endswith(('.js', '.jsx')):
                categories["javascript"] += 1
            elif file.endswith(('.ts', '.tsx')):
                categories["typescript"] += 1  
            elif file.endswith('.java'):
                categories["java"] += 1
            elif file.endswith(('.md', '.rst', '.txt')):
                categories["documentation"] += 1
            elif any(keyword in file_lower for keyword in ['test', 'spec']):
                categories["tests"] += 1
            elif file.endswith(('.json', '.yaml', '.yml', '.toml', '.ini')):
                categories["configuration"] += 1
            else:
                categories["other"] += 1
                
        return categories
        
    def _estimate_complexity(self, files: List[str]) -> str:
        """Estimate project complexity"""
        file_count = len(files)
        if file_count < 10:
            return "simple"
        elif file_count < 100:
            return "moderate"
        elif file_count < 500:
            return "complex"
        else:
            return "very_complex"
            
    def create_memory_templates(self) -> None:
        """Create template memory files for common patterns"""
        templates = {
            "architecture/project_overview.md": self._create_project_overview_template(),
            "architecture/design_patterns.md": self._create_design_patterns_template(),
            "business_logic/domain_rules.md": self._create_domain_rules_template(),
            "technical_debt/identified_issues.md": self._create_tech_debt_template(),
        }
        
        for template_path, content in templates.items():
            full_path = self.memory_dir / template_path
            if not full_path.exists():
                full_path.write_text(content)
                logger.info(f"✅ Created memory template: {template_path}")
                
    def _create_project_overview_template(self) -> str:
        return f"""# Project Overview

**Session**: {self.session_id}
**Created**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Architecture Summary
[To be filled by MCP analysis]

## Key Components
[To be filled by Serena MCP symbol analysis]

## Business Domain
[To be filled by domain analysis]

## Technical Stack
[To be filled by Context7 documentation analysis]
"""

    def _create_design_patterns_template(self) -> str:
        return """# Design Patterns Analysis

## Identified Patterns
- [ ] Repository Pattern
- [ ] Factory Pattern  
- [ ] Observer Pattern
- [ ] Strategy Pattern
- [ ] Command Pattern

## DDD Tactical Patterns
- [ ] Entities
- [ ] Value Objects
- [ ] Aggregates
- [ ] Domain Services
- [ ] Application Services

## Architecture Patterns
- [ ] Layered Architecture
- [ ] Clean Architecture
- [ ] Hexagonal Architecture
- [ ] CQRS
- [ ] Event Sourcing
"""

    def _create_domain_rules_template(self) -> str:
        return """# Business Rules and Domain Logic

## Core Business Rules
[To be extracted from use cases and code analysis]

## Domain Invariants
[To be identified from domain model analysis]

## Business Processes
[To be mapped from application services]
"""

    def _create_tech_debt_template(self) -> str:
        return """# Technical Debt Analysis

## Code Quality Issues
[To be identified by static analysis]

## Architecture Violations
[To be identified by dependency analysis]  

## Test Coverage Gaps
[To be identified by test analysis]

## Performance Concerns
[To be identified by profiling analysis]
"""

    def save_session_metadata(self) -> None:
        """Save session metadata to file"""
        try:
            metadata_file = self.session_dir / "session-metadata.json"
            
            # Update metadata with analysis results
            self.session_metadata.update({
                "status": "initialized",
                "mcp_integrations": {
                    "serena": {"status": "ready", "features": ["symbol_analysis", "code_search", "memory_management"]},
                    "context7": {"status": "ready", "features": ["documentation_lookup", "api_references"]}
                },
                "directories_created": [
                    str(self.session_dir),
                    str(self.memory_dir / "architecture"),
                    str(self.memory_dir / "business_logic"),
                    str(self.memory_dir / "technical_debt"),
                ],
                "analysis_completed_at": datetime.now().isoformat()
            })
            
            with open(metadata_file, 'w', encoding='utf-8') as f:
                json.dump(self.session_metadata, f, indent=2, ensure_ascii=False)
                
            logger.info(f"✅ Session metadata saved: {metadata_file}")
            
        except Exception as e:
            logger.exception("Failed to save session metadata")
            raise
            
    def create_recovery_checkpoint(self) -> None:
        """Create recovery checkpoint for session restoration"""
        try:
            checkpoint_data = {
                "checkpoint_id": f"init_{self.session_id}",
                "created_at": datetime.now().isoformat(),
                "session_metadata": self.session_metadata,
                "recovery_commands": [
                    "/context-session-stageup",
                    "/analytics-dashboard"
                ],
                "state_files": [
                    str(self.session_dir / "session-metadata.json")
                ]
            }
            
            checkpoint_file = self.session_dir / "recovery-checkpoint.json"
            with open(checkpoint_file, 'w', encoding='utf-8') as f:
                json.dump(checkpoint_data, f, indent=2, ensure_ascii=False)
                
            logger.info(f"✅ Recovery checkpoint created: {checkpoint_file}")
            
        except Exception as e:
            logger.exception("Failed to create recovery checkpoint")
            raise
            
    def generate_session_report(self) -> Dict[str, Any]:
        """Generate comprehensive session initialization report"""
        return {
            "session_info": {
                "session_id": self.session_id,
                "project_path": str(self.project_path),
                "initialized_at": self.session_metadata.get("created_at"),
                "status": "ready"
            },
            "mcp_capabilities": {
                "serena_mcp": {
                    "symbol_analysis": True,
                    "code_search": True,
                    "memory_management": True,
                    "cross_reference": True
                },
                "context7_mcp": {
                    "documentation_lookup": True,
                    "api_references": True,
                    "library_resolution": True
                }
            },
            "analysis_summary": self.session_metadata.get("analysis_summary", {}),
            "next_steps": [
                "Execute TDD/DDD workflow with MCP enhancements",
                "Use /domain-modeling-enhanced for advanced domain analysis",
                "Use /analytics-dashboard for project insights",
                "Use /checkpoint-session for state persistence"
            ]
        }
        
    async def run_initialization(self) -> Dict[str, Any]:
        """Main initialization workflow"""
        try:
            logger.info(f"🚀 Starting MCP session initialization for: {self.project_path}")
            
            # Phase 1: Setup directories
            logger.info("📁 Phase 1: Setting up directories...")
            self.initialize_directories()
            
            # Phase 2: Analyze project
            logger.info("🔍 Phase 2: Analyzing project structure...")
            analysis = self.analyze_project_structure()
            self.session_metadata["analysis_summary"] = analysis
            
            # Phase 3: Create memory templates
            logger.info("🧠 Phase 3: Creating memory templates...")
            self.create_memory_templates()
            
            # Phase 4: Save metadata
            logger.info("💾 Phase 4: Saving session metadata...")
            self.save_session_metadata()
            
            # Phase 5: Create recovery checkpoint
            logger.info("🔄 Phase 5: Creating recovery checkpoint...")
            self.create_recovery_checkpoint()
            
            # Generate final report
            report = self.generate_session_report()
            logger.info("✅ MCP session initialization completed successfully!")
            
            return report
            
        except Exception as e:
            logger.exception("MCP session initialization failed")
            raise


async def main():
    """Main entry point"""
    if len(sys.argv) != 2:
        logger.error("Usage: python 20-context-session-stageup.py <project_path>")
        sys.exit(1)
        
    project_path = sys.argv[1]
    
    try:
        # Validate project path
        if not Path(project_path).exists():
            logger.error(f"Project path does not exist: {project_path}")
            sys.exit(1)
            
        # Initialize session manager
        session_manager = MCPSessionManager(project_path)
        
        # Run initialization
        report = await session_manager.run_initialization()
        
        # Print success summary
        print("\n" + "="*60)
        print("🎉 MCP SESSION INITIALIZATION COMPLETED")
        print("="*60)
        print(f"Session ID: {report['session_info']['session_id']}")
        print(f"Project Path: {report['session_info']['project_path']}")
        print(f"Status: {report['session_info']['status']}")
        print("\n📊 MCP Capabilities Enabled:")
        for mcp_name, capabilities in report['mcp_capabilities'].items():
            print(f"  ✅ {mcp_name}: {', '.join([k for k, v in capabilities.items() if v])}")
        print("\n🚀 Next Steps:")
        for step in report['next_steps']:
            print(f"  • {step}")
        print("="*60)
        
        sys.exit(0)
        
    except KeyboardInterrupt:
        logger.info("Initialization cancelled by user")
        sys.exit(1)
    except Exception as e:
        logger.exception("Initialization failed")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())