#!/usr/bin/env python3
"""
MCP-Powered Analytics Dashboard
Comprehensive project analytics and strategic insights using MCP intelligence
"""

import asyncio
import json
import logging
import os
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

class MCPAnalyticsDashboard:
    """Comprehensive analytics dashboard powered by MCP intelligence"""
    
    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path)
        self.session_dir = Path(".serena/sessions/current")
        self.memory_dir = Path(".serena/memory")
        self.analytics_dir = Path("docs/analytics")
        
        # Analytics data storage
        self.project_metrics: Dict[str, Any] = {}
        self.code_analytics: Dict[str, Any] = {}
        self.development_insights: Dict[str, Any] = {}
        self.strategic_recommendations: List[Dict[str, Any]] = []
        
        # Dashboard metadata
        self.dashboard_metadata: Dict[str, Any] = {
            "generated_at": datetime.now().isoformat(),
            "project_path": str(self.project_path),
            "mcp_session_active": False,
            "analytics_version": "1.0",
            "data_sources": [],
            "analysis_scope": "comprehensive"
        }
        
    def validate_mcp_session(self) -> bool:
        """Validate MCP session availability and collect session intelligence"""
        try:
            if not self.session_dir.exists():
                logger.warning("MCP session not found - running basic analytics mode")
                return False
                
            session_metadata_file = self.session_dir / "session-metadata.json"
            if not session_metadata_file.exists():
                logger.warning("MCP session metadata not found")
                return False
                
            # Load session metadata
            with open(session_metadata_file, 'r', encoding='utf-8') as f:
                session_data = json.load(f)
                
            self.dashboard_metadata["mcp_session_active"] = True
            self.dashboard_metadata["session_data"] = session_data
            self.dashboard_metadata["data_sources"].append("mcp_session")
            
            logger.info("✅ MCP session validated - enhanced analytics available")
            return True
            
        except Exception as e:
            logger.warning(f"MCP session validation failed: {e}")
            return False
            
    def collect_memory_intelligence(self) -> Dict[str, Any]:
        """Collect and analyze all MCP memory data"""
        try:
            logger.info("🧠 Collecting MCP memory intelligence...")
            
            memory_intelligence = {
                "memory_categories": {},
                "total_memories": 0,
                "analysis_summaries": {},
                "key_insights": []
            }
            
            if not self.memory_dir.exists():
                logger.warning("No MCP memory directory found")
                return memory_intelligence
                
            # Analyze memory directory structure
            for category_dir in self.memory_dir.iterdir():
                if category_dir.is_dir():
                    category_name = category_dir.name
                    memory_files = list(category_dir.rglob("*.md"))
                    
                    memory_intelligence["memory_categories"][category_name] = {
                        "file_count": len(memory_files),
                        "files": [str(f.relative_to(self.memory_dir)) for f in memory_files],
                        "latest_update": self._get_latest_file_time(memory_files)
                    }
                    
                    memory_intelligence["total_memories"] += len(memory_files)
                    
                    # Extract insights from memory files
                    category_insights = self._extract_category_insights(category_dir, memory_files)
                    memory_intelligence["analysis_summaries"][category_name] = category_insights
                    
            self.dashboard_metadata["data_sources"].append("mcp_memory")
            logger.info(f"✅ Collected {memory_intelligence['total_memories']} memory files")
            
            return memory_intelligence
            
        except Exception as e:
            logger.exception("Failed to collect memory intelligence")
            return {"error": str(e)}
            
    def _get_latest_file_time(self, files: List[Path]) -> str:
        """Get latest modification time from file list"""
        if not files:
            return "N/A"
            
        try:
            latest_time = max(f.stat().st_mtime for f in files if f.exists())
            return datetime.fromtimestamp(latest_time).isoformat()
        except Exception:
            return "N/A"
            
    def _extract_category_insights(self, category_dir: Path, memory_files: List[Path]) -> Dict[str, Any]:
        """Extract insights from memory category"""
        insights = {
            "category": category_dir.name,
            "file_count": len(memory_files),
            "key_topics": [],
            "recent_activities": [],
            "summary": ""
        }
        
        try:
            # Analyze file names for patterns
            file_names = [f.stem for f in memory_files]
            
            # Extract common patterns
            if "architecture" in category_dir.name:
                insights["key_topics"] = ["design_patterns", "architecture_analysis", "technical_debt"]
                insights["summary"] = f"Architecture analysis with {len(memory_files)} documented patterns"
            elif "domain" in category_dir.name:
                insights["key_topics"] = ["domain_models", "business_rules", "aggregate_design"]
                insights["summary"] = f"Domain modeling with {len(memory_files)} model analyses"
            elif "test" in category_dir.name:
                insights["key_topics"] = ["test_patterns", "coverage_analysis", "quality_metrics"]
                insights["summary"] = f"Test analysis with {len(memory_files)} test strategies"
            else:
                insights["key_topics"] = ["general_analysis"]
                insights["summary"] = f"General analysis with {len(memory_files)} memory files"
                
            # Identify recent activities (files modified in last 7 days)
            recent_cutoff = datetime.now() - timedelta(days=7)
            for memory_file in memory_files:
                try:
                    if memory_file.exists():
                        file_time = datetime.fromtimestamp(memory_file.stat().st_mtime)
                        if file_time > recent_cutoff:
                            insights["recent_activities"].append({
                                "file": memory_file.name,
                                "timestamp": file_time.isoformat()
                            })
                except Exception:
                    continue
                    
        except Exception as e:
            logger.warning(f"Failed to extract insights from {category_dir}: {e}")
            
        return insights
        
    def analyze_project_structure(self) -> Dict[str, Any]:
        """Comprehensive project structure analysis"""
        try:
            logger.info("📊 Analyzing project structure...")
            
            structure_analysis = {
                "overview": {},
                "architecture_patterns": {},
                "file_distribution": {},
                "complexity_metrics": {},
                "organization_quality": {}
            }
            
            # Basic project overview
            structure_analysis["overview"] = self._analyze_project_overview()
            
            # Architecture pattern detection
            structure_analysis["architecture_patterns"] = self._detect_architecture_patterns()
            
            # File distribution analysis
            structure_analysis["file_distribution"] = self._analyze_file_distribution()
            
            # Complexity metrics
            structure_analysis["complexity_metrics"] = self._calculate_complexity_metrics()
            
            # Organization quality assessment
            structure_analysis["organization_quality"] = self._assess_organization_quality()
            
            self.dashboard_metadata["data_sources"].append("project_structure")
            logger.info("✅ Project structure analysis completed")
            
            return structure_analysis
            
        except Exception as e:
            logger.exception("Failed to analyze project structure")
            return {"error": str(e)}
            
    def _analyze_project_overview(self) -> Dict[str, Any]:
        """Analyze basic project overview metrics"""
        overview = {
            "total_files": 0,
            "code_files": 0,
            "test_files": 0,
            "documentation_files": 0,
            "configuration_files": 0,
            "primary_languages": {},
            "project_size": "unknown"
        }
        
        try:
            # Count different file types
            for file_path in self.project_path.rglob("*"):
                if file_path.is_file() and not self._should_ignore_file(file_path):
                    overview["total_files"] += 1
                    
                    # Categorize files
                    if self._is_code_file(file_path):
                        overview["code_files"] += 1
                    elif self._is_test_file(file_path):
                        overview["test_files"] += 1
                    elif self._is_documentation_file(file_path):
                        overview["documentation_files"] += 1
                    elif self._is_configuration_file(file_path):
                        overview["configuration_files"] += 1
                        
                    # Track language distribution
                    language = self._detect_language(file_path)
                    if language:
                        overview["primary_languages"][language] = overview["primary_languages"].get(language, 0) + 1
                        
            # Determine project size
            if overview["total_files"] < 50:
                overview["project_size"] = "small"
            elif overview["total_files"] < 200:
                overview["project_size"] = "medium"
            elif overview["total_files"] < 1000:
                overview["project_size"] = "large"
            else:
                overview["project_size"] = "very_large"
                
        except Exception as e:
            logger.warning(f"Failed to analyze project overview: {e}")
            
        return overview
        
    def _should_ignore_file(self, file_path: Path) -> bool:
        """Check if file should be ignored in analysis"""
        ignore_patterns = [
            ".git", "__pycache__", ".pytest_cache", "node_modules",
            ".venv", "venv", ".env", ".DS_Store", ".gitignore"
        ]
        
        return any(pattern in str(file_path) for pattern in ignore_patterns)
        
    def _is_code_file(self, file_path: Path) -> bool:
        """Check if file is a code file"""
        code_extensions = {".py", ".js", ".ts", ".tsx", ".jsx", ".java", ".cpp", ".c", ".go", ".rs", ".php", ".rb"}
        return file_path.suffix.lower() in code_extensions
        
    def _is_test_file(self, file_path: Path) -> bool:
        """Check if file is a test file"""
        test_indicators = ["test", "spec", "_test", "_spec"]
        return any(indicator in file_path.name.lower() for indicator in test_indicators)
        
    def _is_documentation_file(self, file_path: Path) -> bool:
        """Check if file is a documentation file"""
        doc_extensions = {".md", ".rst", ".txt", ".adoc"}
        return file_path.suffix.lower() in doc_extensions
        
    def _is_configuration_file(self, file_path: Path) -> bool:
        """Check if file is a configuration file"""
        config_extensions = {".json", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".xml"}
        config_names = {"Dockerfile", "Makefile", "requirements.txt", "package.json", "pyproject.toml"}
        return file_path.suffix.lower() in config_extensions or file_path.name in config_names
        
    def _detect_language(self, file_path: Path) -> Optional[str]:
        """Detect programming language from file"""
        language_map = {
            ".py": "Python",
            ".js": "JavaScript",
            ".ts": "TypeScript",
            ".tsx": "TypeScript",
            ".jsx": "JavaScript",
            ".java": "Java",
            ".cpp": "C++",
            ".c": "C",
            ".go": "Go",
            ".rs": "Rust",
            ".php": "PHP",
            ".rb": "Ruby"
        }
        
        return language_map.get(file_path.suffix.lower())
        
    def _detect_architecture_patterns(self) -> Dict[str, Any]:
        """Detect architecture patterns in the project"""
        patterns = {
            "layered_architecture": False,
            "clean_architecture": False,
            "hexagonal_architecture": False,
            "microservices": False,
            "monolith": True,  # Default assumption
            "ddd_patterns": False,
            "tdd_patterns": False,
            "confidence_scores": {}
        }
        
        try:
            # Check for layered architecture
            layer_indicators = ["domain", "application", "infrastructure", "presentation"]
            found_layers = []
            
            for indicator in layer_indicators:
                if any(self.project_path.rglob(f"*{indicator}*")):
                    found_layers.append(indicator)
                    
            if len(found_layers) >= 3:
                patterns["layered_architecture"] = True
                patterns["confidence_scores"]["layered_architecture"] = len(found_layers) / len(layer_indicators)
                
            # Check for Clean Architecture
            clean_indicators = ["entities", "use_cases", "interfaces", "frameworks"]
            found_clean = sum(1 for indicator in clean_indicators if any(self.project_path.rglob(f"*{indicator}*")))
            
            if found_clean >= 2:
                patterns["clean_architecture"] = True
                patterns["confidence_scores"]["clean_architecture"] = found_clean / len(clean_indicators)
                
            # Check for DDD patterns
            ddd_indicators = ["aggregate", "entity", "value_object", "repository", "domain_service"]
            found_ddd = sum(1 for indicator in ddd_indicators if any(self.project_path.rglob(f"*{indicator}*")))
            
            if found_ddd >= 3:
                patterns["ddd_patterns"] = True
                patterns["confidence_scores"]["ddd_patterns"] = found_ddd / len(ddd_indicators)
                
            # Check for TDD patterns
            test_dirs = list(self.project_path.rglob("test*"))
            test_files = [f for f in self.project_path.rglob("*test*.py") if f.is_file()]
            
            if len(test_files) > 5 and len(test_dirs) > 0:
                patterns["tdd_patterns"] = True
                patterns["confidence_scores"]["tdd_patterns"] = min(len(test_files) / 20, 1.0)
                
        except Exception as e:
            logger.warning(f"Failed to detect architecture patterns: {e}")
            
        return patterns
        
    def _analyze_file_distribution(self) -> Dict[str, Any]:
        """Analyze file distribution across project"""
        distribution = {
            "by_directory": {},
            "by_type": {},
            "depth_analysis": {},
            "hotspots": []
        }
        
        try:
            directory_counts = Counter()
            type_counts = Counter()
            depth_counts = Counter()
            
            for file_path in self.project_path.rglob("*"):
                if file_path.is_file() and not self._should_ignore_file(file_path):
                    # Directory distribution
                    directory = file_path.parent.relative_to(self.project_path)
                    directory_counts[str(directory)] += 1
                    
                    # Type distribution
                    if self._is_code_file(file_path):
                        type_counts["code"] += 1
                    elif self._is_test_file(file_path):
                        type_counts["test"] += 1
                    elif self._is_documentation_file(file_path):
                        type_counts["documentation"] += 1
                    else:
                        type_counts["other"] += 1
                        
                    # Depth analysis
                    depth = len(file_path.relative_to(self.project_path).parts) - 1
                    depth_counts[depth] += 1
                    
            distribution["by_directory"] = dict(directory_counts.most_common(10))
            distribution["by_type"] = dict(type_counts)
            distribution["depth_analysis"] = dict(depth_counts)
            
            # Identify hotspots (directories with many files)
            for directory, count in directory_counts.most_common(5):
                if count > 10:  # Threshold for hotspot
                    distribution["hotspots"].append({
                        "directory": directory,
                        "file_count": count,
                        "density_score": min(count / 50, 1.0)
                    })
                    
        except Exception as e:
            logger.warning(f"Failed to analyze file distribution: {e}")
            
        return distribution
        
    def _calculate_complexity_metrics(self) -> Dict[str, Any]:
        """Calculate project complexity metrics"""
        metrics = {
            "overall_complexity": "medium",
            "directory_complexity": {},
            "file_size_analysis": {},
            "nesting_depth": {},
            "complexity_score": 0.0
        }
        
        try:
            total_files = 0
            total_size = 0
            large_files = 0
            deep_nesting = 0
            
            for file_path in self.project_path.rglob("*"):
                if file_path.is_file() and not self._should_ignore_file(file_path):
                    total_files += 1
                    
                    # File size analysis
                    try:
                        file_size = file_path.stat().st_size
                        total_size += file_size
                        
                        if file_size > 10000:  # Files larger than 10KB
                            large_files += 1
                            
                    except Exception:
                        continue
                        
                    # Nesting depth analysis
                    depth = len(file_path.relative_to(self.project_path).parts) - 1
                    if depth > 4:  # Deep nesting
                        deep_nesting += 1
                        
            # Calculate complexity metrics
            if total_files > 0:
                avg_file_size = total_size / total_files
                large_file_ratio = large_files / total_files
                deep_nesting_ratio = deep_nesting / total_files
                
                metrics["file_size_analysis"] = {
                    "average_size_bytes": avg_file_size,
                    "large_files_ratio": large_file_ratio,
                    "total_size_mb": total_size / (1024 * 1024)
                }
                
                metrics["nesting_depth"] = {
                    "deep_nesting_ratio": deep_nesting_ratio,
                    "max_depth": max([len(f.relative_to(self.project_path).parts) - 1 
                                    for f in self.project_path.rglob("*") if f.is_file()], default=0)
                }
                
                # Overall complexity score (0-1)
                complexity_factors = [
                    min(total_files / 200, 1.0),  # File count factor
                    large_file_ratio,              # Large file factor
                    deep_nesting_ratio,            # Nesting factor
                ]
                
                metrics["complexity_score"] = sum(complexity_factors) / len(complexity_factors)
                
                if metrics["complexity_score"] < 0.3:
                    metrics["overall_complexity"] = "low"
                elif metrics["complexity_score"] > 0.7:
                    metrics["overall_complexity"] = "high"
                else:
                    metrics["overall_complexity"] = "medium"
                    
        except Exception as e:
            logger.warning(f"Failed to calculate complexity metrics: {e}")
            
        return metrics
        
    def _assess_organization_quality(self) -> Dict[str, Any]:
        """Assess project organization quality"""
        quality = {
            "structure_score": 0.0,
            "naming_consistency": 0.0,
            "separation_of_concerns": 0.0,
            "documentation_coverage": 0.0,
            "overall_quality": "medium",
            "improvement_suggestions": []
        }
        
        try:
            # Structure score (presence of standard directories)
            standard_dirs = ["src", "tests", "docs", "scripts"]
            found_dirs = sum(1 for dir_name in standard_dirs 
                           if any(self.project_path.rglob(dir_name)))
            quality["structure_score"] = found_dirs / len(standard_dirs)
            
            # Documentation coverage (ratio of docs to code)
            code_files = sum(1 for f in self.project_path.rglob("*") 
                           if f.is_file() and self._is_code_file(f) and not self._should_ignore_file(f))
            doc_files = sum(1 for f in self.project_path.rglob("*")
                          if f.is_file() and self._is_documentation_file(f) and not self._should_ignore_file(f))
            
            if code_files > 0:
                quality["documentation_coverage"] = min(doc_files / code_files, 1.0)
            else:
                quality["documentation_coverage"] = 0.0
                
            # Naming consistency (simplified heuristic)
            file_names = [f.stem for f in self.project_path.rglob("*") 
                         if f.is_file() and not self._should_ignore_file(f)]
            
            snake_case_count = sum(1 for name in file_names if "_" in name and name.islower())
            camel_case_count = sum(1 for name in file_names if any(c.isupper() for c in name[1:]))
            
            if len(file_names) > 0:
                consistency_ratio = max(snake_case_count, camel_case_count) / len(file_names)
                quality["naming_consistency"] = consistency_ratio
            else:
                quality["naming_consistency"] = 0.0
                
            # Separation of concerns (presence of different layer directories)
            concern_dirs = ["domain", "application", "infrastructure", "tests", "docs"]
            found_concerns = sum(1 for concern in concern_dirs 
                               if any(self.project_path.rglob(f"*{concern}*")))
            quality["separation_of_concerns"] = found_concerns / len(concern_dirs)
            
            # Overall quality calculation
            quality_factors = [
                quality["structure_score"],
                quality["naming_consistency"], 
                quality["separation_of_concerns"],
                quality["documentation_coverage"]
            ]
            
            quality["overall_quality_score"] = sum(quality_factors) / len(quality_factors)
            
            if quality["overall_quality_score"] < 0.4:
                quality["overall_quality"] = "needs_improvement"
            elif quality["overall_quality_score"] > 0.7:
                quality["overall_quality"] = "excellent"
            else:
                quality["overall_quality"] = "good"
                
            # Generate improvement suggestions
            if quality["structure_score"] < 0.5:
                quality["improvement_suggestions"].append("Add standard directory structure (src/, tests/, docs/)")
            if quality["documentation_coverage"] < 0.3:
                quality["improvement_suggestions"].append("Increase documentation coverage")
            if quality["naming_consistency"] < 0.6:
                quality["improvement_suggestions"].append("Improve naming consistency across files")
            if quality["separation_of_concerns"] < 0.5:
                quality["improvement_suggestions"].append("Improve separation of concerns with clearer layer boundaries")
                
        except Exception as e:
            logger.warning(f"Failed to assess organization quality: {e}")
            
        return quality
        
    def analyze_development_progress(self) -> Dict[str, Any]:
        """Analyze development progress and velocity"""
        try:
            logger.info("📈 Analyzing development progress...")
            
            progress_analysis = {
                "tdd_ddd_workflow": {},
                "completion_metrics": {},
                "velocity_analysis": {},
                "milestone_tracking": {},
                "quality_trends": {}
            }
            
            # Analyze TDD/DDD workflow completion
            progress_analysis["tdd_ddd_workflow"] = self._analyze_tdd_ddd_workflow()
            
            # Calculate completion metrics
            progress_analysis["completion_metrics"] = self._calculate_completion_metrics()
            
            # Analyze development velocity
            progress_analysis["velocity_analysis"] = self._analyze_development_velocity()
            
            # Track milestones
            progress_analysis["milestone_tracking"] = self._track_milestones()
            
            # Analyze quality trends
            progress_analysis["quality_trends"] = self._analyze_quality_trends()
            
            self.dashboard_metadata["data_sources"].append("development_progress")
            logger.info("✅ Development progress analysis completed")
            
            return progress_analysis
            
        except Exception as e:
            logger.exception("Failed to analyze development progress")
            return {"error": str(e)}
            
    def _analyze_tdd_ddd_workflow(self) -> Dict[str, Any]:
        """Analyze TDD/DDD workflow completion status"""
        workflow_status = {
            "completed_phases": [],
            "current_phase": "unknown",
            "completion_percentage": 0.0,
            "phase_analysis": {}
        }
        
        try:
            # Define TDD/DDD workflow phases and their indicators
            phases = {
                "vision": ["docs/vision", "vision.md"],
                "project_structure": ["docs/metadata", "project-state.json"],
                "sprint_planning": ["docs/use_cases/sprints"],
                "use_case_creation": ["docs/use_cases"],
                "domain_modeling": ["docs/domain"],
                "test_creation": ["tests/domain"],
                "implementation": ["src", "domain", "application"],
                "integration": ["tests/integration"],
                "deployment": ["Dockerfile", "docker-compose", "deploy"]
            }
            
            completed_count = 0
            total_phases = len(phases)
            
            for phase, indicators in phases.items():
                phase_completed = any(
                    any(self.project_path.rglob(f"*{indicator}*")) 
                    for indicator in indicators
                )
                
                workflow_status["phase_analysis"][phase] = {
                    "completed": phase_completed,
                    "indicators_found": [
                        indicator for indicator in indicators
                        if any(self.project_path.rglob(f"*{indicator}*"))
                    ]
                }
                
                if phase_completed:
                    workflow_status["completed_phases"].append(phase)
                    completed_count += 1
                else:
                    if workflow_status["current_phase"] == "unknown":
                        workflow_status["current_phase"] = phase
                        
            workflow_status["completion_percentage"] = (completed_count / total_phases) * 100
            
            # If all phases completed, mark as complete
            if completed_count == total_phases:
                workflow_status["current_phase"] = "completed"
                
        except Exception as e:
            logger.warning(f"Failed to analyze TDD/DDD workflow: {e}")
            
        return workflow_status
        
    def _calculate_completion_metrics(self) -> Dict[str, Any]:
        """Calculate various completion metrics"""
        metrics = {
            "code_completion": 0.0,
            "test_completion": 0.0,
            "documentation_completion": 0.0,
            "feature_completion": 0.0,
            "overall_completion": 0.0
        }
        
        try:
            # Code completion (presence of implementation files)
            code_dirs = ["src", "domain", "application", "infrastructure"]
            code_indicators = sum(1 for dir_name in code_dirs 
                                if any(self.project_path.rglob(dir_name)))
            metrics["code_completion"] = (code_indicators / len(code_dirs)) * 100
            
            # Test completion (test coverage estimation)
            test_files = list(self.project_path.rglob("test*.py"))
            code_files = [f for f in self.project_path.rglob("*.py") 
                         if f.is_file() and not self._is_test_file(f) and not self._should_ignore_file(f)]
            
            if len(code_files) > 0:
                test_ratio = len(test_files) / len(code_files)
                metrics["test_completion"] = min(test_ratio * 100, 100)
            else:
                metrics["test_completion"] = 0.0
                
            # Documentation completion
            doc_indicators = ["README.md", "docs/", "API.md", "CONTRIBUTING.md"]
            found_docs = sum(1 for indicator in doc_indicators
                           if any(self.project_path.rglob(f"*{indicator}*")))
            metrics["documentation_completion"] = (found_docs / len(doc_indicators)) * 100
            
            # Feature completion (based on use case files)
            use_case_files = list(self.project_path.rglob("*use*case*.md"))
            implemented_features = len([f for f in use_case_files 
                                      if "completed" in f.read_text(encoding='utf-8', errors='ignore').lower()])
            
            if len(use_case_files) > 0:
                metrics["feature_completion"] = (implemented_features / len(use_case_files)) * 100
            else:
                metrics["feature_completion"] = 0.0
                
            # Overall completion
            completion_factors = [
                metrics["code_completion"],
                metrics["test_completion"],
                metrics["documentation_completion"],
                metrics["feature_completion"]
            ]
            
            metrics["overall_completion"] = sum(completion_factors) / len(completion_factors)
            
        except Exception as e:
            logger.warning(f"Failed to calculate completion metrics: {e}")
            
        return metrics
        
    def _analyze_development_velocity(self) -> Dict[str, Any]:
        """Analyze development velocity metrics"""
        velocity = {
            "recent_activity": {},
            "productivity_score": 0.0,
            "trend_direction": "stable",
            "bottlenecks": []
        }
        
        try:
            # Analyze recent file modifications
            recent_cutoff = datetime.now() - timedelta(days=7)
            recent_files = []
            
            for file_path in self.project_path.rglob("*"):
                if file_path.is_file() and not self._should_ignore_file(file_path):
                    try:
                        file_time = datetime.fromtimestamp(file_path.stat().st_mtime)
                        if file_time > recent_cutoff:
                            recent_files.append({
                                "file": str(file_path.relative_to(self.project_path)),
                                "modified": file_time.isoformat(),
                                "type": self._classify_file_type(file_path)
                            })
                    except Exception:
                        continue
                        
            velocity["recent_activity"] = {
                "files_modified": len(recent_files),
                "file_details": recent_files[:10],  # Show first 10
                "activity_by_type": Counter(f["type"] for f in recent_files)
            }
            
            # Calculate productivity score based on recent activity
            activity_score = min(len(recent_files) / 20, 1.0)  # Normalize to 0-1
            velocity["productivity_score"] = activity_score * 100
            
            # Determine trend direction (simplified)
            if len(recent_files) > 10:
                velocity["trend_direction"] = "increasing"
            elif len(recent_files) < 3:
                velocity["trend_direction"] = "decreasing"
            else:
                velocity["trend_direction"] = "stable"
                
            # Identify potential bottlenecks
            if velocity["productivity_score"] < 20:
                velocity["bottlenecks"].append("Low development activity")
            
            test_files_ratio = len([f for f in recent_files if f["type"] == "test"]) / max(len(recent_files), 1)
            if test_files_ratio < 0.2:
                velocity["bottlenecks"].append("Insufficient test coverage in recent changes")
                
        except Exception as e:
            logger.warning(f"Failed to analyze development velocity: {e}")
            
        return velocity
        
    def _classify_file_type(self, file_path: Path) -> str:
        """Classify file type for velocity analysis"""
        if self._is_test_file(file_path):
            return "test"
        elif self._is_code_file(file_path):
            return "code"
        elif self._is_documentation_file(file_path):
            return "documentation"
        elif self._is_configuration_file(file_path):
            return "configuration"
        else:
            return "other"
            
    def _track_milestones(self) -> Dict[str, Any]:
        """Track project milestones and achievements"""
        milestones = {
            "completed_milestones": [],
            "upcoming_milestones": [],
            "milestone_progress": {},
            "achievements": []
        }
        
        try:
            # Define common project milestones
            milestone_definitions = {
                "project_setup": {
                    "indicators": ["README.md", "pyproject.toml", ".gitignore"],
                    "weight": 1
                },
                "architecture_design": {
                    "indicators": ["docs/architecture", "docs/domain"],
                    "weight": 2
                },
                "domain_modeling": {
                    "indicators": ["domain", "entities", "value_objects"],
                    "weight": 3
                },
                "test_framework": {
                    "indicators": ["tests/", "test_*.py", "pytest"],
                    "weight": 2
                },
                "core_implementation": {
                    "indicators": ["src/", "application/", "infrastructure/"],
                    "weight": 4
                },
                "integration_complete": {
                    "indicators": ["tests/integration", "docker", "api"],
                    "weight": 3
                }
            }
            
            total_weight = sum(m["weight"] for m in milestone_definitions.values())
            completed_weight = 0
            
            for milestone, definition in milestone_definitions.items():
                indicators_found = sum(1 for indicator in definition["indicators"]
                                     if any(self.project_path.rglob(f"*{indicator}*")))
                
                completion_ratio = indicators_found / len(definition["indicators"])
                
                milestones["milestone_progress"][milestone] = {
                    "completion_ratio": completion_ratio,
                    "weight": definition["weight"],
                    "indicators_found": indicators_found,
                    "total_indicators": len(definition["indicators"])
                }
                
                if completion_ratio >= 0.8:  # 80% completion threshold
                    milestones["completed_milestones"].append(milestone)
                    completed_weight += definition["weight"]
                    milestones["achievements"].append(f"Completed {milestone} milestone")
                elif completion_ratio >= 0.3:  # In progress
                    milestones["upcoming_milestones"].append(milestone)
                    
            # Calculate overall milestone progress
            milestones["overall_progress"] = (completed_weight / total_weight) * 100
            
        except Exception as e:
            logger.warning(f"Failed to track milestones: {e}")
            
        return milestones
        
    def _analyze_quality_trends(self) -> Dict[str, Any]:
        """Analyze code quality trends"""
        trends = {
            "current_quality": {},
            "trend_direction": "stable",
            "quality_indicators": {},
            "recommendations": []
        }
        
        try:
            # Current quality indicators
            test_files = list(self.project_path.rglob("test*.py"))
            code_files = [f for f in self.project_path.rglob("*.py") 
                         if not self._is_test_file(f) and not self._should_ignore_file(f)]
            doc_files = list(self.project_path.rglob("*.md"))
            
            trends["current_quality"] = {
                "test_to_code_ratio": len(test_files) / max(len(code_files), 1),
                "documentation_ratio": len(doc_files) / max(len(code_files), 1),
                "file_organization_score": self._calculate_organization_score(),
                "complexity_score": self._calculate_simple_complexity_score()
            }
            
            # Quality indicators
            trends["quality_indicators"] = {
                "has_tests": len(test_files) > 0,
                "has_documentation": len(doc_files) > 0,
                "follows_conventions": self._check_naming_conventions(),
                "has_structure": self._check_project_structure()
            }
            
            # Generate recommendations
            if trends["current_quality"]["test_to_code_ratio"] < 0.5:
                trends["recommendations"].append("Increase test coverage")
            if trends["current_quality"]["documentation_ratio"] < 0.3:
                trends["recommendations"].append("Improve documentation coverage")
            if not trends["quality_indicators"]["has_structure"]:
                trends["recommendations"].append("Improve project structure organization")
                
        except Exception as e:
            logger.warning(f"Failed to analyze quality trends: {e}")
            
        return trends
        
    def _calculate_organization_score(self) -> float:
        """Calculate simple organization score"""
        try:
            standard_dirs = ["src", "tests", "docs"]
            found_dirs = sum(1 for dir_name in standard_dirs 
                           if any(self.project_path.rglob(dir_name)))
            return found_dirs / len(standard_dirs)
        except Exception:
            return 0.0
            
    def _calculate_simple_complexity_score(self) -> float:
        """Calculate simple complexity score"""
        try:
            total_files = sum(1 for f in self.project_path.rglob("*") 
                            if f.is_file() and not self._should_ignore_file(f))
            # Simple heuristic: more files = higher complexity
            return min(total_files / 100, 1.0)
        except Exception:
            return 0.0
            
    def _check_naming_conventions(self) -> bool:
        """Check if project follows naming conventions"""
        try:
            py_files = list(self.project_path.rglob("*.py"))
            if not py_files:
                return True
                
            snake_case_files = sum(1 for f in py_files if f.stem.islower() and "_" in f.stem)
            return (snake_case_files / len(py_files)) > 0.7
        except Exception:
            return False
            
    def _check_project_structure(self) -> bool:
        """Check if project has good structure"""
        try:
            essential_items = ["README.md", "tests", "src"]
            found_items = sum(1 for item in essential_items
                            if any(self.project_path.rglob(f"*{item}*")))
            return found_items >= 2
        except Exception:
            return False
            
    def generate_strategic_recommendations(self, project_analysis: Dict[str, Any],
                                         memory_intelligence: Dict[str, Any],
                                         progress_analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate strategic recommendations based on comprehensive analysis"""
        try:
            logger.info("🎯 Generating strategic recommendations...")
            
            recommendations = []
            
            # Analyze current state for recommendations
            self._add_code_quality_recommendations(recommendations, project_analysis)
            self._add_architecture_recommendations(recommendations, project_analysis)
            self._add_development_process_recommendations(recommendations, progress_analysis)
            self._add_technical_debt_recommendations(recommendations, memory_intelligence)
            self._add_performance_recommendations(recommendations, project_analysis)
            
            # Prioritize recommendations
            for rec in recommendations:
                rec["priority_score"] = self._calculate_recommendation_priority(rec)
                
            # Sort by priority
            recommendations.sort(key=lambda x: x["priority_score"], reverse=True)
            
            logger.info(f"✅ Generated {len(recommendations)} strategic recommendations")
            return recommendations
            
        except Exception as e:
            logger.exception("Failed to generate strategic recommendations")
            return []
            
    def _add_code_quality_recommendations(self, recommendations: List[Dict[str, Any]],
                                        project_analysis: Dict[str, Any]) -> None:
        """Add code quality recommendations"""
        try:
            org_quality = project_analysis.get("organization_quality", {})
            
            if org_quality.get("documentation_coverage", 0) < 0.5:
                recommendations.append({
                    "category": "code_quality",
                    "title": "Improve Documentation Coverage",
                    "description": "Current documentation coverage is below recommended levels",
                    "impact": "high",
                    "effort": "medium",
                    "specific_actions": [
                        "Add comprehensive README documentation",
                        "Document API endpoints and interfaces",
                        "Create developer onboarding guides",
                        "Add inline code comments for complex logic"
                    ],
                    "success_metrics": ["Documentation coverage > 80%", "Developer onboarding time reduced"]
                })
                
            if org_quality.get("naming_consistency", 0) < 0.7:
                recommendations.append({
                    "category": "code_quality", 
                    "title": "Improve Naming Consistency",
                    "description": "File and variable naming lacks consistency across the project",
                    "impact": "medium",
                    "effort": "low",
                    "specific_actions": [
                        "Establish naming convention guidelines",
                        "Refactor inconsistent file names",
                        "Use consistent variable naming patterns",
                        "Apply linting rules for naming conventions"
                    ],
                    "success_metrics": ["Naming consistency > 90%", "Reduced code review comments on naming"]
                })
                
        except Exception as e:
            logger.warning(f"Failed to add code quality recommendations: {e}")
            
    def _add_architecture_recommendations(self, recommendations: List[Dict[str, Any]],
                                        project_analysis: Dict[str, Any]) -> None:
        """Add architecture recommendations"""
        try:
            patterns = project_analysis.get("architecture_patterns", {})
            
            if not patterns.get("layered_architecture", False) and not patterns.get("clean_architecture", False):
                recommendations.append({
                    "category": "architecture",
                    "title": "Implement Layered Architecture",
                    "description": "Project lacks clear architectural layering which impacts maintainability",
                    "impact": "high",
                    "effort": "high",
                    "specific_actions": [
                        "Define clear layer boundaries (Domain, Application, Infrastructure)",
                        "Refactor code to respect layer dependencies",
                        "Implement dependency inversion patterns",
                        "Create architectural documentation and guidelines"
                    ],
                    "success_metrics": ["Clear layer separation", "Reduced coupling between layers", "Improved testability"]
                })
                
            if not patterns.get("ddd_patterns", False):
                recommendations.append({
                    "category": "architecture",
                    "title": "Adopt Domain-Driven Design Patterns",
                    "description": "Implementing DDD patterns will improve domain model clarity",
                    "impact": "high", 
                    "effort": "medium",
                    "specific_actions": [
                        "Identify and model domain entities",
                        "Create value objects to eliminate primitive obsession",
                        "Define aggregate boundaries and roots",
                        "Implement repository patterns for data access"
                    ],
                    "success_metrics": ["Rich domain model", "Clear business logic separation", "Improved code expressiveness"]
                })
                
        except Exception as e:
            logger.warning(f"Failed to add architecture recommendations: {e}")
            
    def _add_development_process_recommendations(self, recommendations: List[Dict[str, Any]],
                                               progress_analysis: Dict[str, Any]) -> None:
        """Add development process recommendations"""
        try:
            completion = progress_analysis.get("completion_metrics", {})
            velocity = progress_analysis.get("velocity_analysis", {})
            
            if completion.get("test_completion", 0) < 70:
                recommendations.append({
                    "category": "development_process",
                    "title": "Increase Test Coverage",
                    "description": "Test coverage is below industry standards, increasing risk",
                    "impact": "high",
                    "effort": "medium", 
                    "specific_actions": [
                        "Set up automated test coverage reporting",
                        "Implement TDD practices for new features",
                        "Add unit tests for existing critical code paths",
                        "Create integration tests for key workflows"
                    ],
                    "success_metrics": ["Test coverage > 80%", "Reduced production bugs", "Faster development cycles"]
                })
                
            if velocity.get("productivity_score", 0) < 30:
                recommendations.append({
                    "category": "development_process",
                    "title": "Optimize Development Workflow",
                    "description": "Low development velocity indicates potential workflow bottlenecks",
                    "impact": "medium",
                    "effort": "medium",
                    "specific_actions": [
                        "Analyze and remove development bottlenecks",
                        "Implement CI/CD pipeline for faster feedback",
                        "Standardize development environment setup",
                        "Improve code review processes"
                    ],
                    "success_metrics": ["Increased commit frequency", "Reduced time to deployment", "Improved developer satisfaction"]
                })
                
        except Exception as e:
            logger.warning(f"Failed to add development process recommendations: {e}")
            
    def _add_technical_debt_recommendations(self, recommendations: List[Dict[str, Any]],
                                          memory_intelligence: Dict[str, Any]) -> None:
        """Add technical debt recommendations"""
        try:
            # Analyze memory for technical debt indicators
            tech_debt_indicators = 0
            
            for category, data in memory_intelligence.get("memory_categories", {}).items():
                if "technical_debt" in category or "debt" in str(data).lower():
                    tech_debt_indicators += data.get("file_count", 0)
                    
            if tech_debt_indicators > 0:
                recommendations.append({
                    "category": "technical_debt",
                    "title": "Address Technical Debt",
                    "description": f"Identified {tech_debt_indicators} technical debt items requiring attention",
                    "impact": "medium",
                    "effort": "high",
                    "specific_actions": [
                        "Prioritize technical debt items by impact",
                        "Allocate regular sprint capacity for debt reduction",
                        "Refactor high-impact code areas",
                        "Implement code quality gates to prevent new debt"
                    ],
                    "success_metrics": ["Reduced technical debt score", "Improved code maintainability", "Faster feature development"]
                })
                
        except Exception as e:
            logger.warning(f"Failed to add technical debt recommendations: {e}")
            
    def _add_performance_recommendations(self, recommendations: List[Dict[str, Any]],
                                       project_analysis: Dict[str, Any]) -> None:
        """Add performance recommendations"""
        try:
            complexity = project_analysis.get("complexity_metrics", {})
            
            if complexity.get("complexity_score", 0) > 0.7:
                recommendations.append({
                    "category": "performance",
                    "title": "Reduce Code Complexity",
                    "description": "High code complexity may impact performance and maintainability",
                    "impact": "medium",
                    "effort": "medium",
                    "specific_actions": [
                        "Identify and refactor complex methods",
                        "Break down large classes and functions",
                        "Implement caching strategies where appropriate",
                        "Optimize database queries and data access patterns"
                    ],
                    "success_metrics": ["Reduced cyclomatic complexity", "Improved response times", "Better resource utilization"]
                })
                
        except Exception as e:
            logger.warning(f"Failed to add performance recommendations: {e}")
            
    def _calculate_recommendation_priority(self, recommendation: Dict[str, Any]) -> float:
        """Calculate priority score for recommendation"""
        try:
            # Priority scoring based on impact and effort
            impact_scores = {"high": 3, "medium": 2, "low": 1}
            effort_scores = {"low": 3, "medium": 2, "high": 1}  # Lower effort = higher score
            
            impact_score = impact_scores.get(recommendation.get("impact", "low"), 1)
            effort_score = effort_scores.get(recommendation.get("effort", "high"), 1)
            
            # Category weights
            category_weights = {
                "code_quality": 1.2,
                "architecture": 1.3,
                "development_process": 1.1,
                "technical_debt": 1.0,
                "performance": 0.9
            }
            
            category_weight = category_weights.get(recommendation.get("category", "other"), 1.0)
            
            return (impact_score * effort_score * category_weight)
            
        except Exception:
            return 0.0
            
    def create_analytics_dashboard(self, project_analysis: Dict[str, Any],
                                 memory_intelligence: Dict[str, Any],
                                 progress_analysis: Dict[str, Any],
                                 recommendations: List[Dict[str, Any]]) -> str:
        """Create comprehensive analytics dashboard HTML"""
        try:
            logger.info("🌐 Creating interactive analytics dashboard...")
            
            # Get current project metrics for dashboard
            overview = project_analysis.get("overview", {})
            completion = progress_analysis.get("completion_metrics", {})
            quality = project_analysis.get("organization_quality", {})
            
            dashboard_html = f'''<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>プロジェクト分析ダッシュボード</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .dashboard-container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
            text-align: center;
        }}
        .header h1 {{
            margin: 0;
            font-size: 2.5rem;
        }}
        .header p {{
            margin: 10px 0 0 0;
            opacity: 0.9;
        }}
        .metrics-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        .metric-card {{
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            text-align: center;
        }}
        .metric-value {{
            font-size: 2rem;
            font-weight: bold;
            color: #667eea;
            margin-bottom: 10px;
        }}
        .metric-label {{
            color: #666;
            font-size: 0.9rem;
        }}
        .charts-container {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-bottom: 30px;
        }}
        .chart-card {{
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .chart-card h3 {{
            margin-top: 0;
            color: #333;
        }}
        .recommendations {{
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .recommendation-item {{
            border-left: 4px solid #667eea;
            padding: 15px;
            margin-bottom: 15px;
            background-color: #f8f9ff;
            border-radius: 0 5px 5px 0;
        }}
        .recommendation-title {{
            font-weight: bold;
            color: #333;
            margin-bottom: 8px;
        }}
        .recommendation-description {{
            color: #666;
            margin-bottom: 10px;
        }}
        .recommendation-meta {{
            font-size: 0.85rem;
            color: #888;
        }}
        .status-indicator {{
            display: inline-block;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            margin-right: 8px;
        }}
        .status-high {{ background-color: #10b981; }}
        .status-medium {{ background-color: #f59e0b; }}
        .status-low {{ background-color: #ef4444; }}
        @media (max-width: 768px) {{
            .charts-container {{
                grid-template-columns: 1fr;
            }}
            .header h1 {{
                font-size: 1.8rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="dashboard-container">
        <div class="header">
            <h1>🚀 プロジェクト分析ダッシュボード</h1>
            <p>MCP統合分析による包括的プロジェクトインサイト</p>
            <p>生成日時: {datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}</p>
        </div>

        <div class="metrics-grid">
            <div class="metric-card">
                <div class="metric-value">{overview.get('total_files', 0)}</div>
                <div class="metric-label">総ファイル数</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">{completion.get('overall_completion', 0):.1f}%</div>
                <div class="metric-label">プロジェクト完了率</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">{completion.get('test_completion', 0):.1f}%</div>
                <div class="metric-label">テストカバレッジ</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">{quality.get('overall_quality_score', 0):.1f}</div>
                <div class="metric-label">品質スコア</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">{memory_intelligence.get('total_memories', 0)}</div>
                <div class="metric-label">MCPメモリ</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">{len(recommendations)}</div>
                <div class="metric-label">推奨改善項目</div>
            </div>
        </div>

        <div class="charts-container">
            <div class="chart-card">
                <h3>📊 プロジェクト完了状況</h3>
                <canvas id="completionChart" width="400" height="200"></canvas>
            </div>
            <div class="chart-card">
                <h3>📈 ファイル構成比率</h3>
                <canvas id="fileDistributionChart" width="400" height="200"></canvas>
            </div>
        </div>

        <div class="recommendations">
            <h3>🎯 戦略的推奨事項（優先度順）</h3>
            {self._generate_recommendations_html(recommendations[:10])}
        </div>
    </div>

    <script>
        // 完了状況チャート
        const completionCtx = document.getElementById('completionChart').getContext('2d');
        new Chart(completionCtx, {{
            type: 'doughnut',
            data: {{
                labels: ['完了', '未完了'],
                datasets: [{{
                    data: [{completion.get('overall_completion', 0):.1f}, {100 - completion.get('overall_completion', 0):.1f}],
                    backgroundColor: ['#10b981', '#e5e7eb'],
                    borderWidth: 0
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{
                        position: 'bottom'
                    }}
                }}
            }}
        }});

        // ファイル構成比率チャート
        const fileDistCtx = document.getElementById('fileDistributionChart').getContext('2d');
        new Chart(fileDistCtx, {{
            type: 'pie',
            data: {{
                labels: ['コードファイル', 'テストファイル', 'ドキュメント', 'その他'],
                datasets: [{{
                    data: [
                        {overview.get('code_files', 0)},
                        {overview.get('test_files', 0)},
                        {overview.get('documentation_files', 0)},
                        {overview.get('total_files', 0) - overview.get('code_files', 0) - overview.get('test_files', 0) - overview.get('documentation_files', 0)}
                    ],
                    backgroundColor: ['#667eea', '#764ba2', '#f093fb', '#f5f7fa'],
                    borderWidth: 2,
                    borderColor: '#fff'
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{
                        position: 'bottom'
                    }}
                }}
            }}
        }});
    </script>
</body>
</html>'''

            return dashboard_html
            
        except Exception as e:
            logger.exception("Failed to create analytics dashboard")
            return "<html><body><h1>Dashboard creation failed</h1></body></html>"
            
    def _generate_recommendations_html(self, recommendations: List[Dict[str, Any]]) -> str:
        """Generate HTML for recommendations section"""
        html = ""
        
        impact_colors = {
            "high": "status-high",
            "medium": "status-medium", 
            "low": "status-low"
        }
        
        for rec in recommendations:
            impact_class = impact_colors.get(rec.get("impact", "low"), "status-low")
            
            html += f'''
            <div class="recommendation-item">
                <div class="recommendation-title">
                    <span class="status-indicator {impact_class}"></span>
                    {rec.get('title', 'Unknown Recommendation')}
                </div>
                <div class="recommendation-description">
                    {rec.get('description', 'No description available')}
                </div>
                <div class="recommendation-meta">
                    カテゴリ: {rec.get('category', 'unknown')} | 
                    インパクト: {rec.get('impact', 'unknown')} | 
                    工数: {rec.get('effort', 'unknown')} |
                    優先度スコア: {rec.get('priority_score', 0):.1f}
                </div>
            </div>'''
            
        return html
        
    def create_executive_summary(self, project_analysis: Dict[str, Any],
                                memory_intelligence: Dict[str, Any],
                                progress_analysis: Dict[str, Any],
                                recommendations: List[Dict[str, Any]]) -> str:
        """Create executive summary report"""
        try:
            logger.info("📋 Creating executive summary...")
            
            # Extract key metrics for summary
            overview = project_analysis.get("overview", {})
            completion = progress_analysis.get("completion_metrics", {})
            quality = project_analysis.get("organization_quality", {})
            workflow = progress_analysis.get("tdd_ddd_workflow", {})
            
            executive_summary = f"""# エグゼクティブサマリー

**生成日時**: {datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}
**分析対象**: {self.project_path}
**分析手法**: MCP統合分析 (Serena + Context7)

## 🎯 プロジェクト概要

### 基本メトリクス
- **総ファイル数**: {overview.get('total_files', 0):,}
- **コードファイル数**: {overview.get('code_files', 0):,}
- **テストファイル数**: {overview.get('test_files', 0):,}
- **プロジェクトサイズ**: {overview.get('project_size', 'unknown').upper()}
- **主要言語**: {', '.join(overview.get('primary_languages', {}).keys()) or 'Unknown'}

### 完了状況
- **総合完了率**: {completion.get('overall_completion', 0):.1f}%
- **コード実装**: {completion.get('code_completion', 0):.1f}%
- **テスト実装**: {completion.get('test_completion', 0):.1f}%
- **ドキュメント**: {completion.get('documentation_completion', 0):.1f}%

## 📊 主要指標

### プロジェクト健全性
{self._generate_health_status(completion, quality)}

### 品質メトリクス
- **コード品質スコア**: {quality.get('overall_quality_score', 0):.2f}/1.0
- **アーキテクチャ品質**: {self._assess_architecture_quality(project_analysis)}
- **テスト品質**: {self._assess_test_quality(completion)}
- **ドキュメント品質**: {self._assess_documentation_quality(completion)}

### TDD/DDD ワークフロー進捗
{self._generate_workflow_status(workflow)}

## 🧠 MCP分析インサイト

### 収集データ概要
- **MCPメモリファイル**: {memory_intelligence.get('total_memories', 0)}個
- **分析カテゴリ**: {len(memory_intelligence.get('memory_categories', {}))}カテゴリ
- **データソース**: {', '.join(self.dashboard_metadata.get('data_sources', []))}

### 主要発見事項
{self._generate_key_findings(project_analysis, memory_intelligence, progress_analysis)}

## 🎯 戦略的推奨事項

### 最優先事項 (HIGH)
{self._generate_priority_recommendations(recommendations, "high")}

### 中優先事項 (MEDIUM)  
{self._generate_priority_recommendations(recommendations, "medium")}

## 📈 ビジネスインパクト

### プロジェクトの強み
{self._identify_project_strengths(project_analysis, progress_analysis)}

### リスク要因
{self._identify_project_risks(project_analysis, progress_analysis, recommendations)}

### 機会領域
{self._identify_opportunities(recommendations, progress_analysis)}

## 📅 推奨アクションプラン

### 即座に実行すべき事項（今週）
{self._generate_immediate_actions(recommendations)}

### 短期目標（1ヶ月以内）
{self._generate_short_term_goals(recommendations)}

### 中期戦略（3ヶ月以内）
{self._generate_medium_term_strategy(recommendations)}

## 📊 成功指標とKPI

### 品質KPI
- テストカバレッジ目標: > 80%
- コード品質スコア目標: > 0.8
- ドキュメントカバレッジ目標: > 70%

### 生産性KPI
- 開発速度向上: 20%向上目標
- バグ発生率削減: 50%削減目標
- デプロイメント頻度向上: 2倍向上目標

### 技術KPI
- 技術的負債削減: 30%削減目標
- アーキテクチャ遵守率: > 95%
- パフォーマンス改善: 25%改善目標

## 💡 次のステップ

1. **即座の行動**: 最優先推奨事項の実装開始
2. **定期監視**: 週次でのメトリクス確認とダッシュボード更新
3. **継続改善**: 月次での戦略見直しと改善計画調整
4. **ステークホルダー報告**: 四半期毎の進捗報告と方針調整

## 📋 付録

### 詳細分析レポート
- **パフォーマンス分析**: `docs/analytics/performance_dashboard.md`
- **開発インサイト**: `docs/analytics/development_insights.md`
- **戦略的推奨事項詳細**: `docs/analytics/strategic_recommendations.md`

### MCP分析データ
- **セッションメタデータ**: `.serena/sessions/current/session-metadata.json`
- **メモリ分析結果**: `.serena/memory/`

---
*このサマリーは MCP統合分析システムにより自動生成されました。定期的な更新により最新の洞察を提供します。*
"""

            return executive_summary
            
        except Exception as e:
            logger.exception("Failed to create executive summary")
            return "# Executive Summary Generation Failed"
            
    def _generate_health_status(self, completion: Dict[str, Any], quality: Dict[str, Any]) -> str:
        """Generate health status summary"""
        overall_completion = completion.get('overall_completion', 0)
        quality_score = quality.get('overall_quality_score', 0) * 100
        
        if overall_completion > 80 and quality_score > 80:
            return "🟢 **優良** - プロジェクトは健全な状態です"
        elif overall_completion > 60 and quality_score > 60:
            return "🟡 **良好** - いくつかの改善余地がありますが、順調に進行しています"
        elif overall_completion > 40 or quality_score > 40:
            return "🟠 **要注意** - 重要な改善が必要です"
        else:
            return "🔴 **警告** - 緊急の対応が必要です"
            
    def _assess_architecture_quality(self, project_analysis: Dict[str, Any]) -> str:
        """Assess architecture quality"""
        patterns = project_analysis.get("architecture_patterns", {})
        
        score = 0
        total = 5
        
        if patterns.get("layered_architecture"):
            score += 1
        if patterns.get("clean_architecture"):
            score += 1
        if patterns.get("ddd_patterns"):
            score += 2
        if patterns.get("tdd_patterns"):
            score += 1
            
        percentage = (score / total) * 100
        
        if percentage > 80:
            return f"優秀 ({percentage:.0f}%)"
        elif percentage > 60:
            return f"良好 ({percentage:.0f}%)"
        else:
            return f"改善要 ({percentage:.0f}%)"
            
    def _assess_test_quality(self, completion: Dict[str, Any]) -> str:
        """Assess test quality"""
        test_completion = completion.get('test_completion', 0)
        
        if test_completion > 80:
            return f"優秀 ({test_completion:.1f}%)"
        elif test_completion > 60:
            return f"良好 ({test_completion:.1f}%)"
        else:
            return f"改善要 ({test_completion:.1f}%)"
            
    def _assess_documentation_quality(self, completion: Dict[str, Any]) -> str:
        """Assess documentation quality"""
        doc_completion = completion.get('documentation_completion', 0)
        
        if doc_completion > 70:
            return f"優秀 ({doc_completion:.1f}%)"
        elif doc_completion > 50:
            return f"良好 ({doc_completion:.1f}%)"
        else:
            return f"改善要 ({doc_completion:.1f}%)"
            
    def _generate_workflow_status(self, workflow: Dict[str, Any]) -> str:
        """Generate workflow status summary"""
        completion_percentage = workflow.get('completion_percentage', 0)
        current_phase = workflow.get('current_phase', 'unknown')
        completed_phases = workflow.get('completed_phases', [])
        
        status = f"""**現在フェーズ**: {current_phase}
**全体進捗**: {completion_percentage:.1f}%
**完了フェーズ**: {len(completed_phases)}個

**完了済み**: {', '.join(completed_phases) if completed_phases else 'なし'}"""
        
        return status
        
    def _generate_key_findings(self, project_analysis: Dict[str, Any],
                             memory_intelligence: Dict[str, Any],
                             progress_analysis: Dict[str, Any]) -> str:
        """Generate key findings from analysis"""
        findings = []
        
        # Architecture findings
        patterns = project_analysis.get("architecture_patterns", {})
        if patterns.get("ddd_patterns"):
            findings.append("✅ DDDパターンの実装が確認されました")
        else:
            findings.append("⚠️ DDDパターンの導入が推奨されます")
            
        # Test findings
        completion = progress_analysis.get("completion_metrics", {})
        test_completion = completion.get("test_completion", 0)
        if test_completion > 70:
            findings.append("✅ テストカバレッジが良好な水準です")
        else:
            findings.append("⚠️ テストカバレッジの向上が必要です")
            
        # Memory intelligence findings
        total_memories = memory_intelligence.get("total_memories", 0)
        if total_memories > 10:
            findings.append(f"✅ {total_memories}個のMCPメモリにより豊富な分析データが蓄積されています")
        else:
            findings.append("📝 MCPメモリデータの蓄積を増やすことで、より詳細な分析が可能になります")
            
        return "\n".join([f"- {finding}" for finding in findings])
        
    def _generate_priority_recommendations(self, recommendations: List[Dict[str, Any]], 
                                          priority: str) -> str:
        """Generate recommendations by priority"""
        priority_recs = [rec for rec in recommendations if rec.get("impact") == priority]
        
        if not priority_recs:
            return "該当する推奨事項はありません。"
            
        result = ""
        for i, rec in enumerate(priority_recs[:3], 1):  # Show top 3
            result += f"""
**{i}. {rec.get('title', 'Unknown')}**
- 説明: {rec.get('description', 'No description')}
- カテゴリ: {rec.get('category', 'unknown')}
- 工数: {rec.get('effort', 'unknown')}
"""
        
        return result
        
    def _identify_project_strengths(self, project_analysis: Dict[str, Any],
                                  progress_analysis: Dict[str, Any]) -> str:
        """Identify project strengths"""
        strengths = []
        
        # Check completion metrics
        completion = progress_analysis.get("completion_metrics", {})
        if completion.get("overall_completion", 0) > 70:
            strengths.append("高い完了率")
            
        # Check architecture patterns
        patterns = project_analysis.get("architecture_patterns", {})
        if patterns.get("ddd_patterns"):
            strengths.append("DDD設計パターンの実装")
        if patterns.get("tdd_patterns"):
            strengths.append("TDD開発プロセス")
            
        # Check organization quality
        quality = project_analysis.get("organization_quality", {})
        if quality.get("overall_quality_score", 0) > 0.7:
            strengths.append("優れたコード組織化")
            
        if not strengths:
            strengths.append("継続的な改善による成長ポテンシャル")
            
        return "\n".join([f"- {strength}" for strength in strengths])
        
    def _identify_project_risks(self, project_analysis: Dict[str, Any],
                              progress_analysis: Dict[str, Any],
                              recommendations: List[Dict[str, Any]]) -> str:
        """Identify project risks"""
        risks = []
        
        # Check high-impact recommendations as risk indicators
        high_impact_recs = [rec for rec in recommendations if rec.get("impact") == "high"]
        if len(high_impact_recs) > 3:
            risks.append("多数の高インパクト改善項目")
            
        # Check test coverage
        completion = progress_analysis.get("completion_metrics", {})
        if completion.get("test_completion", 0) < 50:
            risks.append("低いテストカバレッジ")
            
        # Check documentation
        if completion.get("documentation_completion", 0) < 40:
            risks.append("不十分なドキュメント")
            
        # Check quality score
        quality = project_analysis.get("organization_quality", {})
        if quality.get("overall_quality_score", 0) < 0.5:
            risks.append("コード品質の問題")
            
        if not risks:
            risks.append("現時点で重大なリスクは特定されていません")
            
        return "\n".join([f"- {risk}" for risk in risks])
        
    def _identify_opportunities(self, recommendations: List[Dict[str, Any]],
                              progress_analysis: Dict[str, Any]) -> str:
        """Identify improvement opportunities"""
        opportunities = []
        
        # Check for architecture opportunities
        arch_recs = [rec for rec in recommendations if rec.get("category") == "architecture"]
        if arch_recs:
            opportunities.append("アーキテクチャ改善による保守性向上")
            
        # Check for development process opportunities
        dev_recs = [rec for rec in recommendations if rec.get("category") == "development_process"]
        if dev_recs:
            opportunities.append("開発プロセス最適化による生産性向上")
            
        # Check for performance opportunities
        perf_recs = [rec for rec in recommendations if rec.get("category") == "performance"]
        if perf_recs:
            opportunities.append("パフォーマンス改善によるユーザー体験向上")
            
        # Check progress velocity
        velocity = progress_analysis.get("velocity_analysis", {})
        if velocity.get("productivity_score", 0) < 50:
            opportunities.append("開発速度向上による市場競争力強化")
            
        if not opportunities:
            opportunities.append("継続的改善による長期的価値創出")
            
        return "\n".join([f"- {opportunity}" for opportunity in opportunities])
        
    def _generate_immediate_actions(self, recommendations: List[Dict[str, Any]]) -> str:
        """Generate immediate actions"""
        immediate_actions = []
        
        # High impact, low effort recommendations
        for rec in recommendations:
            if rec.get("impact") == "high" and rec.get("effort") in ["low", "medium"]:
                immediate_actions.append(rec.get("title", "Unknown action"))
                
        if not immediate_actions:
            immediate_actions = [rec.get("title", "Unknown") for rec in recommendations[:2]]
            
        return "\n".join([f"- {action}" for action in immediate_actions[:3]])
        
    def _generate_short_term_goals(self, recommendations: List[Dict[str, Any]]) -> str:
        """Generate short term goals"""
        short_term = []
        
        # Medium impact recommendations
        for rec in recommendations:
            if rec.get("impact") == "medium":
                short_term.append(rec.get("title", "Unknown goal"))
                
        if not short_term:
            short_term = [rec.get("title", "Unknown") for rec in recommendations[2:4]]
            
        return "\n".join([f"- {goal}" for goal in short_term[:3]])
        
    def _generate_medium_term_strategy(self, recommendations: List[Dict[str, Any]]) -> str:
        """Generate medium term strategy"""
        medium_term = []
        
        # High effort recommendations (strategic changes)
        for rec in recommendations:
            if rec.get("effort") == "high":
                medium_term.append(rec.get("title", "Unknown strategy"))
                
        if not medium_term:
            medium_term = ["アーキテクチャ全体の最適化", "開発プロセスの標準化", "品質管理体制の構築"]
            
        return "\n".join([f"- {strategy}" for strategy in medium_term[:3]])
        
    def save_analytics_artifacts(self, project_analysis: Dict[str, Any],
                                memory_intelligence: Dict[str, Any],
                                progress_analysis: Dict[str, Any],
                                recommendations: List[Dict[str, Any]],
                                dashboard_html: str,
                                executive_summary: str) -> None:
        """Save all analytics artifacts"""
        try:
            # Ensure analytics directory exists
            self.analytics_dir.mkdir(parents=True, exist_ok=True)
            
            # Save interactive dashboard
            dashboard_file = self.analytics_dir / "project_analytics_dashboard.html"
            with open(dashboard_file, 'w', encoding='utf-8') as f:
                f.write(dashboard_html)
            logger.info(f"✅ Saved analytics dashboard: {dashboard_file}")
            
            # Save executive summary
            summary_file = self.analytics_dir / "executive_summary.md"
            with open(summary_file, 'w', encoding='utf-8') as f:
                f.write(executive_summary)
            logger.info(f"✅ Saved executive summary: {summary_file}")
            
            # Save detailed analytics data
            analytics_data = {
                "generated_at": self.dashboard_metadata["generated_at"],
                "project_analysis": project_analysis,
                "memory_intelligence": memory_intelligence,
                "progress_analysis": progress_analysis,
                "strategic_recommendations": recommendations
            }
            
            analytics_data_file = self.analytics_dir / "analytics_data.json"
            with open(analytics_data_file, 'w', encoding='utf-8') as f:
                json.dump(analytics_data, f, indent=2, ensure_ascii=False, default=str)
            logger.info(f"✅ Saved analytics data: {analytics_data_file}")
            
            # Create additional reports
            self._create_performance_dashboard(project_analysis, progress_analysis)
            self._create_development_insights(progress_analysis, memory_intelligence)
            self._create_strategic_recommendations_report(recommendations)
            
        except Exception as e:
            logger.exception("Failed to save analytics artifacts")
            raise
            
    def _create_performance_dashboard(self, project_analysis: Dict[str, Any],
                                    progress_analysis: Dict[str, Any]) -> None:
        """Create performance dashboard report"""
        try:
            complexity = project_analysis.get("complexity_metrics", {})
            velocity = progress_analysis.get("velocity_analysis", {})
            
            performance_report = f"""# パフォーマンス分析ダッシュボード

**生成日時**: {datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}

## 📊 コード複雑度メトリクス

### 全体的複雑度
- **複雑度スコア**: {complexity.get('complexity_score', 0):.2f}/1.0
- **複雑度レベル**: {complexity.get('overall_complexity', 'unknown')}

### ファイルサイズ分析
{self._format_file_size_analysis(complexity.get('file_size_analysis', {}))}

### ネスト構造分析
{self._format_nesting_analysis(complexity.get('nesting_depth', {}))}

## 🚀 開発速度分析

### 生産性メトリクス
- **生産性スコア**: {velocity.get('productivity_score', 0):.1f}/100
- **トレンド方向**: {velocity.get('trend_direction', 'unknown')}

### 最近の活動
{self._format_recent_activity(velocity.get('recent_activity', {}))}

### パフォーマンスボトルネック
{self._format_bottlenecks(velocity.get('bottlenecks', []))}

## 💡 パフォーマンス改善推奨事項

### 即座の対応
- コード複雑度の高いファイルのリファクタリング
- 大きなファイルの分割検討
- 深いネスト構造の簡素化

### 中期的改善
- パフォーマンス監視の導入
- 自動化によるボトルネック解消
- 開発プロセスの最適化

## 📈 継続監視指標

### 目標値
- 複雑度スコア: < 0.5
- 生産性スコア: > 70
- 平均ファイルサイズ: < 500行

### 監視頻度
- 週次: 生産性メトリクス
- 月次: 複雑度分析
- 四半期: 全体的パフォーマンス評価
"""

            performance_file = self.analytics_dir / "performance_dashboard.md"
            with open(performance_file, 'w', encoding='utf-8') as f:
                f.write(performance_report)
            logger.info(f"✅ Saved performance dashboard: {performance_file}")
            
        except Exception as e:
            logger.warning(f"Failed to create performance dashboard: {e}")
            
    def _format_file_size_analysis(self, file_size_data: Dict[str, Any]) -> str:
        """Format file size analysis data"""
        if not file_size_data:
            return "ファイルサイズ分析データが利用できません。"
            
        return f"""- **平均ファイルサイズ**: {file_size_data.get('average_size_bytes', 0):.0f} bytes
- **大きなファイルの割合**: {file_size_data.get('large_files_ratio', 0):.1%}
- **総プロジェクトサイズ**: {file_size_data.get('total_size_mb', 0):.1f} MB"""

    def _format_nesting_analysis(self, nesting_data: Dict[str, Any]) -> str:
        """Format nesting analysis data"""
        if not nesting_data:
            return "ネスト構造分析データが利用できません。"
            
        return f"""- **深いネスト比率**: {nesting_data.get('deep_nesting_ratio', 0):.1%}
- **最大ネスト深度**: {nesting_data.get('max_depth', 0)} レベル"""

    def _format_recent_activity(self, activity_data: Dict[str, Any]) -> str:
        """Format recent activity data"""
        if not activity_data:
            return "最近の活動データが利用できません。"
            
        activity_by_type = activity_data.get('activity_by_type', {})
        
        result = f"- **変更ファイル数**: {activity_data.get('files_modified', 0)} (過去7日間)\n"
        
        for file_type, count in activity_by_type.items():
            result += f"- **{file_type}**: {count}ファイル\n"
            
        return result

    def _format_bottlenecks(self, bottlenecks: List[str]) -> str:
        """Format bottlenecks list"""
        if not bottlenecks:
            return "現在、特定されたボトルネックはありません。"
            
        return "\n".join([f"- {bottleneck}" for bottleneck in bottlenecks])
        
    def _create_development_insights(self, progress_analysis: Dict[str, Any],
                                   memory_intelligence: Dict[str, Any]) -> None:
        """Create development insights report"""
        try:
            workflow = progress_analysis.get("tdd_ddd_workflow", {})
            completion = progress_analysis.get("completion_metrics", {})
            milestones = progress_analysis.get("milestone_tracking", {})
            
            insights_report = f"""# 開発インサイトレポート

**生成日時**: {datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}

## 🎯 TDD/DDDワークフロー分析

### 現在の進捗状況
- **現在フェーズ**: {workflow.get('current_phase', 'unknown')}
- **完了率**: {workflow.get('completion_percentage', 0):.1f}%
- **完了フェーズ数**: {len(workflow.get('completed_phases', []))}

### フェーズ別分析
{self._format_phase_analysis(workflow.get('phase_analysis', {}))}

## 📈 完了メトリクス詳細

### カテゴリ別完了率
- **コード実装**: {completion.get('code_completion', 0):.1f}%
- **テスト作成**: {completion.get('test_completion', 0):.1f}%
- **ドキュメント**: {completion.get('documentation_completion', 0):.1f}%
- **機能実装**: {completion.get('feature_completion', 0):.1f}%

### マイルストーン達成状況
{self._format_milestone_analysis(milestones)}

## 🧠 MCPデータ活用インサイト

### データ蓄積状況
{self._format_memory_insights(memory_intelligence)}

### 分析カテゴリ別洞察
{self._format_category_insights(memory_intelligence.get('memory_categories', {}))}

## 🔮 予測と推奨事項

### 完了予測
{self._generate_completion_prediction(completion, workflow)}

### 次のマイルストーン
{self._predict_next_milestone(milestones)}

### 開発効率化提案
{self._generate_efficiency_suggestions(progress_analysis)}

## 📊 長期トレンド分析

### 成長パターン
- プロジェクトは{workflow.get('completion_percentage', 0):.0f}%の進捗を達成
- {len(workflow.get('completed_phases', []))}個の主要フェーズが完了済み

### 改善機会
{self._identify_improvement_opportunities(progress_analysis)}
"""

            insights_file = self.analytics_dir / "development_insights.md"
            with open(insights_file, 'w', encoding='utf-8') as f:
                f.write(insights_report)
            logger.info(f"✅ Saved development insights: {insights_file}")
            
        except Exception as e:
            logger.warning(f"Failed to create development insights: {e}")
            
    def _format_phase_analysis(self, phase_analysis: Dict[str, Any]) -> str:
        """Format phase analysis data"""
        if not phase_analysis:
            return "フェーズ分析データが利用できません。"
            
        result = ""
        for phase, data in phase_analysis.items():
            status = "✅ 完了" if data.get("completed") else "⏳ 未完了"
            indicators = data.get("indicators_found", [])
            result += f"- **{phase}**: {status}"
            if indicators:
                result += f" (発見指標: {', '.join(indicators)})"
            result += "\n"
            
        return result
        
    def _format_milestone_analysis(self, milestones: Dict[str, Any]) -> str:
        """Format milestone analysis"""
        if not milestones:
            return "マイルストーン分析データが利用できません。"
            
        completed = milestones.get("completed_milestones", [])
        upcoming = milestones.get("upcoming_milestones", [])
        overall_progress = milestones.get("overall_progress", 0)
        
        result = f"**全体進捗**: {overall_progress:.1f}%\n"
        result += f"**完了済み**: {', '.join(completed) if completed else 'なし'}\n"
        result += f"**進行中**: {', '.join(upcoming) if upcoming else 'なし'}\n"
        
        return result
        
    def _format_memory_insights(self, memory_intelligence: Dict[str, Any]) -> str:
        """Format memory insights"""
        total_memories = memory_intelligence.get("total_memories", 0)
        categories = len(memory_intelligence.get("memory_categories", {}))
        
        return f"""- **総メモリファイル数**: {total_memories}
- **分析カテゴリ数**: {categories}
- **データ蓄積レベル**: {'豊富' if total_memories > 20 else '標準' if total_memories > 10 else '基本'}"""

    def _format_category_insights(self, categories: Dict[str, Any]) -> str:
        """Format category insights"""
        if not categories:
            return "カテゴリ別インサイトが利用できません。"
            
        result = ""
        for category, data in categories.items():
            file_count = data.get("file_count", 0)
            latest_update = data.get("latest_update", "N/A")
            result += f"- **{category}**: {file_count}ファイル (最終更新: {latest_update})\n"
            
        return result
        
    def _generate_completion_prediction(self, completion: Dict[str, Any],
                                      workflow: Dict[str, Any]) -> str:
        """Generate completion prediction"""
        overall_completion = completion.get("overall_completion", 0)
        
        if overall_completion > 80:
            return "現在の進捗から、プロジェクトは順調に完了に向かっています。"
        elif overall_completion > 60:
            return "良好な進捗です。いくつかの重点領域への集中で完了を加速できます。"
        elif overall_completion > 40:
            return "中程度の進捗です。継続的な取り組みにより着実な完了が見込めます。"
        else:
            return "初期段階です。計画的な取り組みにより段階的な進捗が期待できます。"
            
    def _predict_next_milestone(self, milestones: Dict[str, Any]) -> str:
        """Predict next milestone"""
        upcoming = milestones.get("upcoming_milestones", [])
        
        if upcoming:
            return f"次のマイルストーン候補: {upcoming[0]}"
        else:
            return "現在の完了状況から次のマイルストーンを設定することを推奨します。"
            
    def _generate_efficiency_suggestions(self, progress_analysis: Dict[str, Any]) -> str:
        """Generate efficiency suggestions"""
        velocity = progress_analysis.get("velocity_analysis", {})
        productivity_score = velocity.get("productivity_score", 0)
        
        suggestions = []
        
        if productivity_score < 50:
            suggestions.append("開発ボトルネックの特定と解消")
            
        suggestions.extend([
            "自動化ツールの導入検討",
            "コードレビュープロセスの最適化",
            "継続的インテグレーションの強化"
        ])
        
        return "\n".join([f"- {suggestion}" for suggestion in suggestions])
        
    def _identify_improvement_opportunities(self, progress_analysis: Dict[str, Any]) -> str:
        """Identify improvement opportunities"""
        completion = progress_analysis.get("completion_metrics", {})
        
        opportunities = []
        
        if completion.get("test_completion", 0) < 70:
            opportunities.append("テスト自動化の拡充")
            
        if completion.get("documentation_completion", 0) < 60:
            opportunities.append("ドキュメント自動生成の導入")
            
        opportunities.append("開発プロセスの標準化")
        
        return "\n".join([f"- {opportunity}" for opportunity in opportunities])
        
    def _create_strategic_recommendations_report(self, recommendations: List[Dict[str, Any]]) -> None:
        """Create detailed strategic recommendations report"""
        try:
            recommendations_report = f"""# 戦略的推奨事項詳細レポート

**生成日時**: {datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}
**総推奨項目数**: {len(recommendations)}

## 📋 推奨事項概要

### 優先度別分布
{self._format_priority_distribution(recommendations)}

### カテゴリ別分布
{self._format_category_distribution(recommendations)}

## 🎯 詳細推奨事項

{self._format_detailed_recommendations(recommendations)}

## 📊 実装ロードマップ

### Phase 1: 緊急対応 (1-2週間)
{self._format_phase_recommendations(recommendations, 1)}

### Phase 2: 重要改善 (1ヶ月)
{self._format_phase_recommendations(recommendations, 2)}

### Phase 3: 戦略的改善 (3ヶ月)
{self._format_phase_recommendations(recommendations, 3)}

## 💰 投資対効果分析

{self._format_roi_analysis(recommendations)}

## 📈 成功指標

{self._format_success_metrics(recommendations)}
"""

            recommendations_file = self.analytics_dir / "strategic_recommendations.md"
            with open(recommendations_file, 'w', encoding='utf-8') as f:
                f.write(recommendations_report)
            logger.info(f"✅ Saved strategic recommendations: {recommendations_file}")
            
        except Exception as e:
            logger.warning(f"Failed to create strategic recommendations report: {e}")
            
    def _format_priority_distribution(self, recommendations: List[Dict[str, Any]]) -> str:
        """Format priority distribution"""
        priority_counts = Counter(rec.get("impact", "unknown") for rec in recommendations)
        
        result = ""
        for priority, count in priority_counts.items():
            result += f"- **{priority.upper()}**: {count}項目\n"
            
        return result
        
    def _format_category_distribution(self, recommendations: List[Dict[str, Any]]) -> str:
        """Format category distribution"""
        category_counts = Counter(rec.get("category", "unknown") for rec in recommendations)
        
        result = ""
        for category, count in category_counts.items():
            result += f"- **{category}**: {count}項目\n"
            
        return result
        
    def _format_detailed_recommendations(self, recommendations: List[Dict[str, Any]]) -> str:
        """Format detailed recommendations"""
        result = ""
        
        for i, rec in enumerate(recommendations, 1):
            result += f"""### {i}. {rec.get('title', 'Unknown')}

**カテゴリ**: {rec.get('category', 'unknown')}
**インパクト**: {rec.get('impact', 'unknown')}
**工数**: {rec.get('effort', 'unknown')}
**優先度スコア**: {rec.get('priority_score', 0):.1f}

**説明**: {rec.get('description', 'No description available')}

**具体的アクション**:
{self._format_actions(rec.get('specific_actions', []))}

**成功指標**:
{self._format_metrics(rec.get('success_metrics', []))}

---

"""
        
        return result
        
    def _format_actions(self, actions: List[str]) -> str:
        """Format specific actions"""
        if not actions:
            return "具体的なアクションが定義されていません。"
            
        return "\n".join([f"- {action}" for action in actions])
        
    def _format_metrics(self, metrics: List[str]) -> str:
        """Format success metrics"""
        if not metrics:
            return "成功指標が定義されていません。"
            
        return "\n".join([f"- {metric}" for metric in metrics])
        
    def _format_phase_recommendations(self, recommendations: List[Dict[str, Any]], phase: int) -> str:
        """Format recommendations by implementation phase"""
        if phase == 1:
            # High impact, low effort
            phase_recs = [rec for rec in recommendations 
                         if rec.get("impact") == "high" and rec.get("effort") == "low"]
        elif phase == 2:
            # High impact, medium effort or medium impact, low effort
            phase_recs = [rec for rec in recommendations 
                         if (rec.get("impact") == "high" and rec.get("effort") == "medium") or
                            (rec.get("impact") == "medium" and rec.get("effort") == "low")]
        else:
            # High effort items (strategic changes)
            phase_recs = [rec for rec in recommendations if rec.get("effort") == "high"]
            
        if not phase_recs:
            return "該当する推奨事項はありません。"
            
        result = ""
        for rec in phase_recs[:5]:  # Show top 5 per phase
            result += f"- {rec.get('title', 'Unknown')}\n"
            
        return result
        
    def _format_roi_analysis(self, recommendations: List[Dict[str, Any]]) -> str:
        """Format ROI analysis"""
        high_roi = [rec for rec in recommendations 
                   if rec.get("impact") == "high" and rec.get("effort") in ["low", "medium"]]
        
        result = f"**高ROI推奨事項** ({len(high_roi)}項目):\n"
        
        for rec in high_roi[:3]:
            result += f"- {rec.get('title', 'Unknown')}: 高インパクト、{rec.get('effort', 'unknown')}工数\n"
            
        return result
        
    def _format_success_metrics(self, recommendations: List[Dict[str, Any]]) -> str:
        """Format aggregated success metrics"""
        all_metrics = []
        for rec in recommendations:
            all_metrics.extend(rec.get("success_metrics", []))
            
        # Count common metrics
        metric_counts = Counter(all_metrics)
        
        result = "**共通成功指標**:\n"
        for metric, count in metric_counts.most_common(5):
            result += f"- {metric} ({count}項目で言及)\n"
            
        return result
        
    def generate_analytics_report(self, project_analysis: Dict[str, Any],
                                memory_intelligence: Dict[str, Any],
                                progress_analysis: Dict[str, Any],
                                recommendations: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate final analytics report"""
        return {
            "analytics_info": {
                "generated_at": self.dashboard_metadata["generated_at"],
                "project_path": str(self.project_path),
                "mcp_session_active": self.dashboard_metadata["mcp_session_active"],
                "data_sources": self.dashboard_metadata["data_sources"],
                "status": "completed"
            },
            "project_metrics": {
                "total_files": project_analysis.get("overview", {}).get("total_files", 0),
                "code_files": project_analysis.get("overview", {}).get("code_files", 0),
                "test_files": project_analysis.get("overview", {}).get("test_files", 0),
                "project_size": project_analysis.get("overview", {}).get("project_size", "unknown"),
                "complexity_score": project_analysis.get("complexity_metrics", {}).get("complexity_score", 0),
                "quality_score": project_analysis.get("organization_quality", {}).get("overall_quality_score", 0)
            },
            "progress_metrics": {
                "overall_completion": progress_analysis.get("completion_metrics", {}).get("overall_completion", 0),
                "test_completion": progress_analysis.get("completion_metrics", {}).get("test_completion", 0),
                "documentation_completion": progress_analysis.get("completion_metrics", {}).get("documentation_completion", 0),
                "current_phase": progress_analysis.get("tdd_ddd_workflow", {}).get("current_phase", "unknown"),
                "completed_phases": len(progress_analysis.get("tdd_ddd_workflow", {}).get("completed_phases", [])),
                "productivity_score": progress_analysis.get("velocity_analysis", {}).get("productivity_score", 0)
            },
            "intelligence_metrics": {
                "total_memories": memory_intelligence.get("total_memories", 0),
                "memory_categories": len(memory_intelligence.get("memory_categories", {})),
                "analysis_depth": "comprehensive" if memory_intelligence.get("total_memories", 0) > 20 else "standard"
            },
            "strategic_insights": {
                "total_recommendations": len(recommendations),
                "high_priority_count": len([r for r in recommendations if r.get("impact") == "high"]),
                "categories_addressed": len(set(r.get("category", "unknown") for r in recommendations)),
                "estimated_improvement_potential": self._calculate_improvement_potential(recommendations)
            },
            "generated_artifacts": [
                str(self.analytics_dir / "project_analytics_dashboard.html"),
                str(self.analytics_dir / "executive_summary.md"),
                str(self.analytics_dir / "performance_dashboard.md"),
                str(self.analytics_dir / "development_insights.md"),
                str(self.analytics_dir / "strategic_recommendations.md"),
                str(self.analytics_dir / "analytics_data.json")
            ],
            "next_steps": [
                "Review interactive analytics dashboard",
                "Implement high-priority recommendations",
                "Schedule regular analytics updates",
                "Monitor key performance indicators"
            ]
        }
        
    def _calculate_improvement_potential(self, recommendations: List[Dict[str, Any]]) -> str:
        """Calculate overall improvement potential"""
        high_impact_count = len([r for r in recommendations if r.get("impact") == "high"])
        total_count = len(recommendations)
        
        if high_impact_count > total_count * 0.6:
            return "very_high"
        elif high_impact_count > total_count * 0.4:
            return "high"
        elif high_impact_count > total_count * 0.2:
            return "medium"
        else:
            return "low"
            
    async def run_comprehensive_analytics(self) -> Dict[str, Any]:
        """Main comprehensive analytics workflow"""
        try:
            logger.info("📊 Starting comprehensive MCP-powered analytics...")
            
            # Phase 1: Validate MCP session
            logger.info("🔍 Phase 1: Validating MCP session...")
            mcp_available = self.validate_mcp_session()
            
            # Phase 2: Collect memory intelligence
            logger.info("🧠 Phase 2: Collecting MCP memory intelligence...")
            memory_intelligence = self.collect_memory_intelligence()
            
            # Phase 3: Analyze project structure
            logger.info("📁 Phase 3: Analyzing project structure...")
            project_analysis = self.analyze_project_structure()
            
            # Phase 4: Analyze development progress
            logger.info("📈 Phase 4: Analyzing development progress...")
            progress_analysis = self.analyze_development_progress()
            
            # Phase 5: Generate strategic recommendations
            logger.info("🎯 Phase 5: Generating strategic recommendations...")
            recommendations = self.generate_strategic_recommendations(
                project_analysis, memory_intelligence, progress_analysis
            )
            
            # Phase 6: Create analytics dashboard
            logger.info("🌐 Phase 6: Creating interactive analytics dashboard...")
            dashboard_html = self.create_analytics_dashboard(
                project_analysis, memory_intelligence, progress_analysis, recommendations
            )
            
            # Phase 7: Create executive summary
            logger.info("📋 Phase 7: Creating executive summary...")
            executive_summary = self.create_executive_summary(
                project_analysis, memory_intelligence, progress_analysis, recommendations
            )
            
            # Phase 8: Save all artifacts
            logger.info("💾 Phase 8: Saving analytics artifacts...")
            self.save_analytics_artifacts(
                project_analysis, memory_intelligence, progress_analysis, 
                recommendations, dashboard_html, executive_summary
            )
            
            # Generate final report
            report = self.generate_analytics_report(
                project_analysis, memory_intelligence, progress_analysis, recommendations
            )
            
            logger.info("✅ Comprehensive analytics completed successfully!")
            return report
            
        except Exception as e:
            logger.exception("Comprehensive analytics failed")
            raise


async def main():
    """Main entry point"""
    project_path = sys.argv[1] if len(sys.argv) > 1 else "."
    
    try:
        # Initialize analytics dashboard
        dashboard = MCPAnalyticsDashboard(project_path)
        
        # Run comprehensive analytics
        report = await dashboard.run_comprehensive_analytics()
        
        # Print success summary
        print("\n" + "="*60)
        print("🎉 MCP-POWERED ANALYTICS DASHBOARD COMPLETED")
        print("="*60)
        print(f"Project Path: {report['analytics_info']['project_path']}")
        print(f"Generated At: {report['analytics_info']['generated_at']}")
        print(f"MCP Session Active: {report['analytics_info']['mcp_session_active']}")
        print(f"Data Sources: {', '.join(report['analytics_info']['data_sources'])}")
        print(f"\n📊 Project Metrics:")
        metrics = report['project_metrics']
        print(f"  📁 Total Files: {metrics['total_files']:,}")
        print(f"  💻 Code Files: {metrics['code_files']:,}")
        print(f"  🧪 Test Files: {metrics['test_files']:,}")
        print(f"  📏 Project Size: {metrics['project_size']}")
        print(f"  🔧 Complexity Score: {metrics['complexity_score']:.2f}")
        print(f"  ⭐ Quality Score: {metrics['quality_score']:.2f}")
        print(f"\n📈 Progress Metrics:")
        progress = report['progress_metrics']
        print(f"  🎯 Overall Completion: {progress['overall_completion']:.1f}%")
        print(f"  🧪 Test Completion: {progress['test_completion']:.1f}%")
        print(f"  📚 Documentation: {progress['documentation_completion']:.1f}%")
        print(f"  📊 Current Phase: {progress['current_phase']}")
        print(f"  ✅ Completed Phases: {progress['completed_phases']}")
        print(f"  🚀 Productivity Score: {progress['productivity_score']:.1f}")
        print(f"\n🧠 Intelligence Metrics:")
        intelligence = report['intelligence_metrics']
        print(f"  🗃️ Total Memories: {intelligence['total_memories']}")
        print(f"  📂 Memory Categories: {intelligence['memory_categories']}")
        print(f"  🔍 Analysis Depth: {intelligence['analysis_depth']}")
        print(f"\n🎯 Strategic Insights:")
        insights = report['strategic_insights']
        print(f"  📋 Total Recommendations: {insights['total_recommendations']}")
        print(f"  ⚡ High Priority: {insights['high_priority_count']}")
        print(f"  📊 Categories Addressed: {insights['categories_addressed']}")
        print(f"  📈 Improvement Potential: {insights['estimated_improvement_potential']}")
        print(f"\n📁 Generated Reports:")
        for artifact in report['generated_artifacts']:
            print(f"  ✅ {artifact}")
        print(f"\n🚀 Next Steps:")
        for step in report['next_steps']:
            print(f"  • {step}")
        print("="*60)
        print(f"\n🌐 Interactive Dashboard: {dashboard.analytics_dir}/project_analytics_dashboard.html")
        print(f"📋 Executive Summary: {dashboard.analytics_dir}/executive_summary.md")
        
        sys.exit(0)
        
    except KeyboardInterrupt:
        logger.info("Analytics dashboard cancelled by user")
        sys.exit(1)
    except Exception as e:
        logger.exception("Analytics dashboard failed")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())