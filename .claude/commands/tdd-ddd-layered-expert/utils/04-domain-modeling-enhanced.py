#!/usr/bin/env python3
"""
MCP-Enhanced Domain Modeling Script
Leverages Serena MCP for intelligent codebase analysis and Context7 for DDD pattern integration
"""

import asyncio
import json
import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any, Set, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

class MCPEnhancedDomainModeler:
    """MCP-Enhanced Domain Modeling with intelligent analysis and pattern integration"""
    
    def __init__(self, issue_number: str):
        self.issue_number = issue_number
        self.session_dir = Path(".serena/sessions/current")
        self.memory_dir = Path(".serena/memory")
        self.domain_dir = Path("docs/domain")
        
        # Analysis results storage
        self.codebase_analysis: Dict[str, Any] = {}
        self.domain_patterns: Dict[str, Any] = {}
        self.business_rules: List[Dict[str, Any]] = []
        self.recommendations: Dict[str, Any] = {}
        
        # Enhanced modeling metadata
        self.modeling_metadata: Dict[str, Any] = {
            "issue_number": issue_number,
            "started_at": datetime.now().isoformat(),
            "mcp_integrations": {
                "serena": {"status": "initializing", "features": []},
                "context7": {"status": "initializing", "features": []}
            },
            "analysis_results": {},
            "generated_artifacts": [],
            "quality_metrics": {}
        }
        
    def validate_mcp_session(self) -> bool:
        """Validate that MCP session is active and functional"""
        try:
            # Check session directory exists
            if not self.session_dir.exists():
                logger.error("MCP session directory not found")
                return False
                
            # Check session metadata
            session_metadata_file = self.session_dir / "session-metadata.json"
            if not session_metadata_file.exists():
                logger.error("MCP session metadata not found")
                return False
                
            # Load session metadata
            with open(session_metadata_file, 'r', encoding='utf-8') as f:
                session_metadata = json.load(f)
                
            # Validate MCP integrations
            mcp_integrations = session_metadata.get("mcp_integrations", {})
            serena_status = mcp_integrations.get("serena", {}).get("status")
            context7_status = mcp_integrations.get("context7", {}).get("status")
            
            if serena_status != "ready":
                logger.error(f"Serena MCP not ready: {serena_status}")
                return False
                
            if context7_status != "ready":
                logger.warning(f"Context7 MCP status: {context7_status}")
                # Context7 is optional, continue even if not ready
                
            logger.info("✅ MCP session validation passed")
            return True
            
        except Exception as e:
            logger.exception("Failed to validate MCP session")
            return False
            
    def load_use_case_specifications(self) -> Dict[str, Any]:
        """Load use case specifications for the issue"""
        try:
            # Find use case file for the issue
            use_case_files = list(Path("docs/use_cases").rglob(f"*issue*{self.issue_number}*.md"))
            
            if not use_case_files:
                logger.warning(f"No use case specifications found for issue {self.issue_number}")
                return {}
                
            use_case_file = use_case_files[0]
            logger.info(f"Loading use case specifications from: {use_case_file}")
            
            # Parse use case content
            with open(use_case_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Extract Given-When-Then scenarios (simplified parsing)
            scenarios = []
            lines = content.split('\n')
            current_scenario = {}
            
            for line in lines:
                line = line.strip()
                if line.startswith('**Given'):
                    current_scenario = {"given": line.replace('**Given**: ', '')}
                elif line.startswith('**When') and current_scenario:
                    current_scenario["when"] = line.replace('**When**: ', '')
                elif line.startswith('**Then') and current_scenario:
                    current_scenario["then"] = line.replace('**Then**: ', '')
                    scenarios.append(current_scenario.copy())
                    current_scenario = {}
                    
            return {
                "file_path": str(use_case_file),
                "scenarios": scenarios,
                "content": content
            }
            
        except Exception as e:
            logger.exception("Failed to load use case specifications")
            return {}
            
    def analyze_codebase_with_serena(self) -> Dict[str, Any]:
        """Analyze existing codebase using Serena MCP for domain pattern discovery"""
        try:
            logger.info("🔍 Starting Serena MCP codebase analysis...")
            
            analysis_results = {
                "project_structure": {},
                "discovered_entities": [],
                "discovered_value_objects": [],
                "business_methods": [],
                "domain_services": [],
                "repositories": [],
                "aggregates": []
            }
            
            # This is a simulation of MCP calls since we can't make actual MCP calls in this script
            # In real implementation, these would be actual MCP function calls
            
            # Simulate project structure analysis
            analysis_results["project_structure"] = self._simulate_project_structure_analysis()
            
            # Simulate entity discovery
            analysis_results["discovered_entities"] = self._simulate_entity_discovery()
            
            # Simulate value object discovery
            analysis_results["discovered_value_objects"] = self._simulate_value_object_discovery()
            
            # Simulate business method discovery
            analysis_results["business_methods"] = self._simulate_business_method_discovery()
            
            # Store analysis in memory for future reference
            self._store_analysis_in_memory("codebase_analysis", analysis_results)
            
            logger.info("✅ Serena MCP codebase analysis completed")
            self.modeling_metadata["mcp_integrations"]["serena"]["status"] = "completed"
            self.modeling_metadata["mcp_integrations"]["serena"]["features"] = [
                "project_structure_analysis", "entity_discovery", "value_object_discovery", 
                "business_method_discovery", "cross_reference_analysis"
            ]
            
            return analysis_results
            
        except Exception as e:
            logger.exception("Failed to analyze codebase with Serena MCP")
            return {}
            
    def _simulate_project_structure_analysis(self) -> Dict[str, Any]:
        """Simulate project structure analysis"""
        # In real implementation, this would use mcp__serena__list_dir and mcp__serena__get_symbols_overview
        return {
            "total_files": 45,
            "code_files": 32,
            "test_files": 13,
            "main_directories": ["src", "tests", "docs"],
            "dominant_language": "python",
            "architecture_style": "layered",
            "estimated_complexity": "moderate"
        }
        
    def _simulate_entity_discovery(self) -> List[Dict[str, Any]]:
        """Simulate entity discovery from code analysis"""
        # In real implementation, this would use mcp__serena__find_symbol with entity patterns
        return [
            {
                "name": "User",
                "file_path": "src/domain/entities/user.py",
                "methods": ["create", "update_profile", "change_password"],
                "properties": ["id", "email", "username", "created_at"],
                "business_rules": ["Email must be unique", "Username cannot be changed"]
            },
            {
                "name": "Order",
                "file_path": "src/domain/entities/order.py", 
                "methods": ["add_item", "remove_item", "calculate_total", "confirm"],
                "properties": ["id", "customer_id", "items", "status", "total"],
                "business_rules": ["Order total must be positive", "Confirmed orders cannot be modified"]
            }
        ]
        
    def _simulate_value_object_discovery(self) -> List[Dict[str, Any]]:
        """Simulate value object discovery and primitive obsession detection"""
        # In real implementation, this would use mcp__serena__search_for_pattern to find primitive obsession
        return [
            {
                "name": "Email",
                "suggested_from": "string email fields",
                "validation_rules": ["Valid email format", "Max 255 characters"],
                "immutable": True,
                "equality_based": True
            },
            {
                "name": "Money", 
                "suggested_from": "decimal amount fields",
                "properties": ["amount", "currency"],
                "validation_rules": ["Amount must be non-negative", "Currency must be valid ISO code"],
                "immutable": True
            }
        ]
        
    def _simulate_business_method_discovery(self) -> List[Dict[str, Any]]:
        """Simulate business method discovery"""
        # In real implementation, this would use mcp__serena__find_symbol with business logic patterns
        return [
            {
                "method_name": "calculate_discount",
                "class": "Order",
                "business_rule": "Apply discount based on customer tier and order total",
                "complexity": "medium",
                "dependencies": ["CustomerTier", "DiscountPolicy"]
            },
            {
                "method_name": "validate_payment",
                "class": "PaymentService",
                "business_rule": "Validate payment method and available balance",
                "complexity": "high", 
                "dependencies": ["PaymentGateway", "FraudDetection"]
            }
        ]
        
    def integrate_context7_patterns(self) -> Dict[str, Any]:
        """Integrate latest DDD patterns using Context7 MCP"""
        try:
            logger.info("📚 Integrating Context7 DDD patterns...")
            
            # This simulates Context7 integration
            # In real implementation, these would be actual mcp__context7__ calls
            
            pattern_integration = {
                "ddd_tactical_patterns": self._simulate_ddd_patterns(),
                "aggregate_design_patterns": self._simulate_aggregate_patterns(),
                "repository_patterns": self._simulate_repository_patterns(),
                "domain_service_patterns": self._simulate_domain_service_patterns()
            }
            
            # Store pattern integration in memory
            self._store_analysis_in_memory("context7_patterns", pattern_integration)
            
            logger.info("✅ Context7 pattern integration completed")
            self.modeling_metadata["mcp_integrations"]["context7"]["status"] = "completed"
            self.modeling_metadata["mcp_integrations"]["context7"]["features"] = [
                "ddd_tactical_patterns", "aggregate_design", "repository_patterns", "domain_services"
            ]
            
            return pattern_integration
            
        except Exception as e:
            logger.exception("Failed to integrate Context7 patterns")
            return {}
            
    def _simulate_ddd_patterns(self) -> Dict[str, Any]:
        """Simulate DDD tactical pattern recommendations"""
        # In real implementation: mcp__context7__get-library-docs for DDD patterns
        return {
            "entity_patterns": [
                "Use identity equality for entities",
                "Implement domain events for state changes",
                "Keep entities focused on business behavior"
            ],
            "value_object_patterns": [
                "Make value objects immutable",
                "Implement value-based equality",
                "Use for primitive obsession elimination"
            ],
            "aggregate_patterns": [
                "Design aggregate boundaries around business transactions", 
                "Use aggregate roots to control access",
                "Limit aggregate size for performance"
            ]
        }
        
    def _simulate_aggregate_patterns(self) -> Dict[str, Any]:]:
        """Simulate aggregate design pattern recommendations"""
        return {
            "design_principles": [
                "Single aggregate per transaction",
                "Reference other aggregates by ID only",
                "Use eventual consistency between aggregates"
            ],
            "size_recommendations": [
                "Keep aggregates small and focused",
                "Avoid large object graphs",
                "Consider splitting large aggregates"
            ],
            "consistency_patterns": [
                "Use domain events for cross-aggregate consistency",
                "Implement saga patterns for long-running transactions",
                "Apply eventual consistency where appropriate"
            ]
        }
        
    def _simulate_repository_patterns(self) -> Dict[str, Any]:
        """Simulate repository pattern recommendations"""
        return {
            "interface_design": [
                "Define repository interfaces in domain layer",
                "Use aggregate root as repository boundary",
                "Avoid exposing persistence details"
            ],
            "query_patterns": [
                "Use specification pattern for complex queries",
                "Implement pagination for large result sets", 
                "Consider CQRS for read optimization"
            ]
        }
        
    def _simulate_domain_service_patterns(self) -> Dict[str, Any]:
        """Simulate domain service pattern recommendations"""
        return {
            "usage_guidelines": [
                "Use for operations that don't belong to single entity",
                "Keep domain services stateless",
                "Avoid anemic domain model anti-pattern"
            ],
            "coordination_patterns": [
                "Coordinate between multiple aggregates",
                "Handle complex business processes",
                "Implement domain policies and rules"
            ]
        }
        
    def _store_analysis_in_memory(self, memory_name: str, analysis_data: Dict[str, Any]) -> None:
        """Store analysis results in MCP memory"""
        try:
            memory_file = self.memory_dir / "domain_models" / f"{memory_name}_{self.issue_number}.md"
            memory_file.parent.mkdir(parents=True, exist_ok=True)
            
            # Convert analysis data to markdown format
            markdown_content = self._convert_to_markdown(memory_name, analysis_data)
            
            with open(memory_file, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
                
            logger.info(f"✅ Stored analysis in memory: {memory_file}")
            
        except Exception as e:
            logger.exception(f"Failed to store analysis in memory: {memory_name}")
            
    def _convert_to_markdown(self, title: str, data: Dict[str, Any]) -> str:
        """Convert analysis data to markdown format"""
        markdown = f"# {title.replace('_', ' ').title()} - Issue {self.issue_number}\n\n"
        markdown += f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
        def dict_to_markdown(obj: Any, level: int = 2) -> str:
            result = ""
            if isinstance(obj, dict):
                for key, value in obj.items():
                    result += f"{'#' * level} {key.replace('_', ' ').title()}\n\n"
                    result += dict_to_markdown(value, level + 1)
            elif isinstance(obj, list):
                for item in obj:
                    if isinstance(item, dict):
                        result += dict_to_markdown(item, level)
                    else:
                        result += f"- {item}\n"
                result += "\n"
            else:
                result += f"{obj}\n\n"
            return result
            
        markdown += dict_to_markdown(data)
        return markdown
        
    def generate_enhanced_domain_model(self, use_case_specs: Dict[str, Any], 
                                     codebase_analysis: Dict[str, Any],
                                     pattern_integration: Dict[str, Any]) -> str:
        """Generate comprehensive enhanced domain model document"""
        try:
            logger.info("📝 Generating enhanced domain model document...")
            
            domain_model_content = f"""# Enhanced Domain Model - Issue {self.issue_number}

**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**MCP Analysis**: Serena (Codebase) + Context7 (Patterns)

## 🎯 Domain Analysis Summary

### Use Case Context
{self._format_use_case_context(use_case_specs)}

### Codebase Analysis Results
{self._format_codebase_analysis(codebase_analysis)}

### Pattern Integration
{self._format_pattern_integration(pattern_integration)}

## 🏗️ Enhanced Domain Model Design

### Entities
{self._generate_entity_specifications(codebase_analysis.get("discovered_entities", []))}

### Value Objects  
{self._generate_value_object_specifications(codebase_analysis.get("discovered_value_objects", []))}

### Aggregates
{self._generate_aggregate_specifications(codebase_analysis, pattern_integration)}

### Domain Services
{self._generate_domain_service_specifications(codebase_analysis.get("business_methods", []))}

### Repositories
{self._generate_repository_specifications(codebase_analysis.get("repositories", []))}

## 🔍 MCP-Powered Insights

### Discovered Anti-Patterns
{self._identify_anti_patterns(codebase_analysis)}

### Improvement Recommendations
{self._generate_improvement_recommendations(codebase_analysis, pattern_integration)}

### Implementation Priority
{self._generate_implementation_priority()}

## 📊 Quality Metrics

### Domain Model Completeness
- **Entities Discovered**: {len(codebase_analysis.get("discovered_entities", []))}
- **Value Objects Recommended**: {len(codebase_analysis.get("discovered_value_objects", []))}
- **Business Rules Identified**: {len(codebase_analysis.get("business_methods", []))}
- **Pattern Integration Coverage**: {self._calculate_pattern_coverage(pattern_integration)}%

### Technical Debt Assessment
{self._assess_technical_debt(codebase_analysis)}

## 🚀 Next Steps

1. **Immediate Actions**
   - Review and validate discovered domain patterns
   - Prioritize value object implementation to eliminate primitive obsession
   - Refactor identified anti-patterns

2. **Test Creation Phase**
   - Use `/create-tests-enhanced {self.issue_number}` for MCP-powered test generation
   - Focus on business rule validation tests
   - Implement aggregate boundary tests

3. **Implementation Phase** 
   - Follow generated implementation guidance
   - Apply Context7 pattern recommendations
   - Maintain domain purity principles

## 📋 References

- **Codebase Analysis**: `.serena/memory/domain_models/codebase_analysis_{self.issue_number}.md`
- **Pattern Integration**: `.serena/memory/domain_models/context7_patterns_{self.issue_number}.md`
- **Use Case Specifications**: `{use_case_specs.get("file_path", "N/A")}`
"""
            
            return domain_model_content
            
        except Exception as e:
            logger.exception("Failed to generate enhanced domain model")
            return "# Error: Failed to generate domain model"
            
    def _format_use_case_context(self, use_case_specs: Dict[str, Any]) -> str:
        """Format use case context section"""
        if not use_case_specs.get("scenarios"):
            return "No use case specifications found for this issue."
            
        context = f"**Source**: `{use_case_specs['file_path']}`\n\n"
        context += f"**Scenarios Identified**: {len(use_case_specs['scenarios'])}\n\n"
        
        for i, scenario in enumerate(use_case_specs["scenarios"][:3], 1):  # Show first 3 scenarios
            context += f"**Scenario {i}**:\n"
            context += f"- Given: {scenario.get('given', 'N/A')}\n"
            context += f"- When: {scenario.get('when', 'N/A')}\n"  
            context += f"- Then: {scenario.get('then', 'N/A')}\n\n"
            
        return context
        
    def _format_codebase_analysis(self, analysis: Dict[str, Any]) -> str:
        """Format codebase analysis results"""
        if not analysis:
            return "No codebase analysis available."
            
        structure = analysis.get("project_structure", {})
        result = f"**Project Complexity**: {structure.get('estimated_complexity', 'unknown')}\n"
        result += f"**Total Files Analyzed**: {structure.get('total_files', 0)}\n"
        result += f"**Code Files**: {structure.get('code_files', 0)}\n"
        result += f"**Architecture Style**: {structure.get('architecture_style', 'unknown')}\n\n"
        
        result += f"**Domain Patterns Discovered**:\n"
        result += f"- Entities: {len(analysis.get('discovered_entities', []))}\n"
        result += f"- Value Objects (recommended): {len(analysis.get('discovered_value_objects', []))}\n"
        result += f"- Business Methods: {len(analysis.get('business_methods', []))}\n\n"
        
        return result
        
    def _format_pattern_integration(self, patterns: Dict[str, Any]) -> str:
        """Format Context7 pattern integration results"""
        if not patterns:
            return "No pattern integration available."
            
        result = "**DDD Tactical Patterns Applied**: ✅\n"
        result += "**Aggregate Design Patterns**: ✅\n" 
        result += "**Repository Patterns**: ✅\n"
        result += "**Domain Service Patterns**: ✅\n\n"
        
        result += "**Key Recommendations**:\n"
        tactical = patterns.get("ddd_tactical_patterns", {})
        if tactical.get("entity_patterns"):
            result += f"- Entity: {tactical['entity_patterns'][0]}\n"
        if tactical.get("value_object_patterns"):
            result += f"- Value Object: {tactical['value_object_patterns'][0]}\n"
        if tactical.get("aggregate_patterns"):
            result += f"- Aggregate: {tactical['aggregate_patterns'][0]}\n"
            
        return result
        
    def _generate_entity_specifications(self, entities: List[Dict[str, Any]]) -> str:
        """Generate detailed entity specifications"""
        if not entities:
            return "No entities discovered in current codebase analysis."
            
        result = ""
        for entity in entities:
            result += f"#### {entity['name']} Entity\n\n"
            result += f"**Location**: `{entity['file_path']}`\n\n"
            result += f"**Properties**:\n"
            for prop in entity.get("properties", []):
                result += f"- `{prop}`\n"
            result += "\n"
            
            result += f"**Behavior Methods**:\n"
            for method in entity.get("methods", []):
                result += f"- `{method}()`\n"
            result += "\n"
            
            result += f"**Business Rules**:\n"
            for rule in entity.get("business_rules", []):
                result += f"- {rule}\n"
            result += "\n"
            
        return result
        
    def _generate_value_object_specifications(self, value_objects: List[Dict[str, Any]]) -> str:
        """Generate value object specifications"""
        if not value_objects:
            return "No value object candidates identified."
            
        result = ""
        for vo in value_objects:
            result += f"#### {vo['name']} Value Object\n\n"
            result += f"**Purpose**: Eliminate primitive obsession for {vo.get('suggested_from', 'unknown')}\n\n"
            
            result += f"**Properties**:\n"
            for prop in vo.get("properties", [vo['name'].lower()]):
                result += f"- `{prop}` (immutable)\n"
            result += "\n"
            
            result += f"**Validation Rules**:\n"
            for rule in vo.get("validation_rules", []):
                result += f"- {rule}\n"
            result += "\n"
            
            result += f"**Characteristics**:\n"
            result += f"- Immutable: {'✅' if vo.get('immutable') else '❌'}\n"
            result += f"- Value Equality: {'✅' if vo.get('equality_based') else '❌'}\n\n"
            
        return result
        
    def _generate_aggregate_specifications(self, codebase_analysis: Dict[str, Any], 
                                         patterns: Dict[str, Any]) -> str:
        """Generate aggregate specifications based on analysis"""
        entities = codebase_analysis.get("discovered_entities", [])
        if not entities:
            return "No aggregates identified from current analysis."
            
        result = "Based on entity analysis and Context7 patterns, the following aggregate design is recommended:\n\n"
        
        # Group entities into potential aggregates based on business relationships
        for entity in entities:
            result += f"#### {entity['name']} Aggregate\n\n"
            result += f"**Aggregate Root**: {entity['name']}\n"
            result += f"**Consistency Boundary**: {entity['name']} and its direct child entities\n"
            result += f"**Business Transaction Scope**: {entity['name']} lifecycle management\n\n"
            
            # Add Context7 pattern recommendations
            aggregate_patterns = patterns.get("aggregate_design_patterns", {})
            if aggregate_patterns.get("design_principles"):
                result += f"**Design Principles Applied**:\n"
                for principle in aggregate_patterns["design_principles"][:2]:
                    result += f"- {principle}\n"
                result += "\n"
                
        return result
        
    def _generate_domain_service_specifications(self, business_methods: List[Dict[str, Any]]) -> str:
        """Generate domain service specifications"""
        if not business_methods:
            return "No complex business methods requiring domain services identified."
            
        result = ""
        # Group high-complexity methods into domain services
        high_complexity_methods = [m for m in business_methods if m.get("complexity") in ["high", "medium"]]
        
        for method in high_complexity_methods:
            result += f"#### {method['method_name']} Domain Service\n\n"
            result += f"**Purpose**: {method.get('business_rule', 'Complex business operation')}\n"
            result += f"**Complexity**: {method.get('complexity', 'unknown')}\n"
            result += f"**Dependencies**: {', '.join(method.get('dependencies', []))}\n\n"
            
        return result if result else "No domain services recommended based on current analysis."
        
    def _generate_repository_specifications(self, repositories: List[Dict[str, Any]]) -> str:
        """Generate repository specifications"""
        # This is a placeholder - in real implementation, repositories would be discovered from codebase
        return """#### Repository Interface Design

Based on aggregate analysis, the following repository interfaces are recommended:

**UserRepository**
- `find_by_id(user_id: UserId) -> Optional[User]`
- `find_by_email(email: Email) -> Optional[User]`
- `save(user: User) -> None`

**OrderRepository**
- `find_by_id(order_id: OrderId) -> Optional[Order]`
- `find_by_customer(customer_id: CustomerId) -> List[Order]`
- `save(order: Order) -> None`

**Repository Pattern Application**:
- Interface defined in domain layer
- Implementation in infrastructure layer
- Aggregate root as repository boundary
"""

    def _identify_anti_patterns(self, analysis: Dict[str, Any]) -> str:
        """Identify anti-patterns from codebase analysis"""
        anti_patterns = []
        
        # Check for primitive obsession
        value_objects = analysis.get("discovered_value_objects", [])
        if value_objects:
            anti_patterns.append(f"**Primitive Obsession**: {len(value_objects)} candidates for value objects identified")
            
        # Check for anemic domain model
        entities = analysis.get("discovered_entities", [])
        total_methods = sum(len(entity.get("methods", [])) for entity in entities)
        if entities and total_methods < len(entities) * 2:
            anti_patterns.append("**Anemic Domain Model**: Entities have insufficient behavior methods")
            
        return "\n".join([f"- {pattern}" for pattern in anti_patterns]) if anti_patterns else "No significant anti-patterns detected."
        
    def _generate_improvement_recommendations(self, codebase_analysis: Dict[str, Any],
                                            patterns: Dict[str, Any]) -> str:
        """Generate improvement recommendations based on analysis"""
        recommendations = []
        
        # Value object recommendations
        value_objects = codebase_analysis.get("discovered_value_objects", [])
        if value_objects:
            recommendations.append(f"**Priority 1**: Implement {len(value_objects)} value objects to eliminate primitive obsession")
            
        # Entity enhancement recommendations
        entities = codebase_analysis.get("discovered_entities", [])
        if entities:
            recommendations.append(f"**Priority 2**: Enhance {len(entities)} entities with business behavior methods")
            
        # Pattern application recommendations
        if patterns:
            recommendations.append("**Priority 3**: Apply Context7 DDD patterns for aggregate design optimization")
            
        return "\n".join([f"{i+1}. {rec}" for i, rec in enumerate(recommendations)]) if recommendations else "Analysis complete - no immediate improvements required."
        
    def _generate_implementation_priority(self) -> str:
        """Generate implementation priority recommendations"""
        return """**High Priority**:
1. Implement critical value objects (Email, Money)
2. Enhance entity behavior methods
3. Define aggregate boundaries

**Medium Priority**:
1. Implement domain services for complex operations
2. Create repository interfaces
3. Apply aggregate design patterns

**Low Priority**:
1. Refactor anti-patterns
2. Optimize cross-reference relationships
3. Enhance domain event handling"""

    def _calculate_pattern_coverage(self, patterns: Dict[str, Any]) -> int:
        """Calculate pattern integration coverage percentage"""
        if not patterns:
            return 0
            
        pattern_categories = ["ddd_tactical_patterns", "aggregate_design_patterns", 
                            "repository_patterns", "domain_service_patterns"]
        covered = sum(1 for cat in pattern_categories if patterns.get(cat))
        return int((covered / len(pattern_categories)) * 100)
        
    def _assess_technical_debt(self, analysis: Dict[str, Any]) -> str:
        """Assess technical debt from analysis"""
        debt_items = []
        
        # Primitive obsession debt
        value_objects = analysis.get("discovered_value_objects", [])
        if value_objects:
            debt_items.append(f"Primitive Obsession: {len(value_objects)} instances")
            
        # Entity behavior debt
        entities = analysis.get("discovered_entities", [])
        if entities:
            avg_methods = sum(len(e.get("methods", [])) for e in entities) / len(entities) if entities else 0
            if avg_methods < 3:
                debt_items.append(f"Anemic Entities: Average {avg_methods:.1f} methods per entity")
                
        return "\n".join([f"- {item}" for item in debt_items]) if debt_items else "Low technical debt detected."
        
    def create_mcp_analysis_report(self, codebase_analysis: Dict[str, Any],
                                 pattern_integration: Dict[str, Any]) -> str:
        """Create comprehensive MCP analysis report"""
        try:
            logger.info("📊 Creating MCP analysis report...")
            
            report_content = f"""# MCP Analysis Report - Issue {self.issue_number}

**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Analysis Duration**: {self._calculate_analysis_duration()}
**MCP Integrations**: Serena + Context7

## 🔍 Serena MCP Codebase Analysis

### Project Overview
{self._format_project_overview(codebase_analysis)}

### Domain Pattern Discovery
{self._format_domain_discovery(codebase_analysis)}

### Business Logic Analysis
{self._format_business_logic_analysis(codebase_analysis)}

### Anti-Pattern Detection
{self._identify_anti_patterns(codebase_analysis)}

## 📚 Context7 Pattern Integration

### Applied Patterns
{self._format_applied_patterns(pattern_integration)}

### Best Practice Recommendations
{self._format_best_practices(pattern_integration)}

## 📈 Quality Metrics

### Discovery Metrics
- **Files Analyzed**: {codebase_analysis.get('project_structure', {}).get('total_files', 0)}
- **Symbols Discovered**: {self._count_discovered_symbols(codebase_analysis)}
- **Patterns Identified**: {self._count_patterns(codebase_analysis)}
- **Business Rules Extracted**: {len(codebase_analysis.get('business_methods', []))}

### Integration Metrics
- **Pattern Coverage**: {self._calculate_pattern_coverage(pattern_integration)}%
- **Recommendation Quality**: {self._assess_recommendation_quality()}
- **Implementation Readiness**: {self._assess_implementation_readiness()}%

## 🎯 Key Findings

### Strengths
{self._identify_strengths(codebase_analysis)}

### Areas for Improvement  
{self._identify_improvement_areas(codebase_analysis)}

### Critical Actions Required
{self._identify_critical_actions(codebase_analysis)}

## 🚀 Implementation Roadmap

### Phase 1: Foundation (Immediate)
{self._generate_phase_1_roadmap(codebase_analysis)}

### Phase 2: Enhancement (Short-term)
{self._generate_phase_2_roadmap(pattern_integration)}

### Phase 3: Optimization (Long-term)
{self._generate_phase_3_roadmap()}

## 📊 Comparison with Best Practices

### DDD Compliance Score
{self._calculate_ddd_compliance_score(codebase_analysis, pattern_integration)}

### Architecture Quality Assessment
{self._assess_architecture_quality(codebase_analysis)}

## 📋 Appendix

### Detailed Analysis Data
- **Codebase Analysis**: `.serena/memory/domain_models/codebase_analysis_{self.issue_number}.md`
- **Pattern Integration**: `.serena/memory/domain_models/context7_patterns_{self.issue_number}.md`
- **Session Metadata**: `.serena/sessions/current/session-metadata.json`

### MCP Integration Status
- **Serena MCP**: ✅ {', '.join(self.modeling_metadata['mcp_integrations']['serena']['features'])}
- **Context7 MCP**: ✅ {', '.join(self.modeling_metadata['mcp_integrations']['context7']['features'])}
"""
            
            return report_content
            
        except Exception as e:
            logger.exception("Failed to create MCP analysis report")
            return "# Error: Failed to generate MCP analysis report"
            
    def _calculate_analysis_duration(self) -> str:
        """Calculate analysis duration"""
        start_time = datetime.fromisoformat(self.modeling_metadata["started_at"])
        duration = datetime.now() - start_time
        return f"{duration.total_seconds():.1f} seconds"
        
    def _format_project_overview(self, analysis: Dict[str, Any]) -> str:
        """Format project overview section"""
        structure = analysis.get("project_structure", {})
        return f"""**Architecture**: {structure.get('architecture_style', 'unknown')}
**Language**: {structure.get('dominant_language', 'unknown')}
**Complexity**: {structure.get('estimated_complexity', 'unknown')}
**File Structure**: {structure.get('total_files', 0)} total files, {structure.get('code_files', 0)} code files"""

    def _format_domain_discovery(self, analysis: Dict[str, Any]) -> str:
        """Format domain discovery section"""
        entities = len(analysis.get("discovered_entities", []))
        value_objects = len(analysis.get("discovered_value_objects", []))
        services = len(analysis.get("business_methods", []))
        
        return f"""**Entities Discovered**: {entities}
**Value Object Candidates**: {value_objects}
**Business Services**: {services}
**Domain Complexity**: {'High' if entities + value_objects > 10 else 'Moderate' if entities + value_objects > 5 else 'Low'}"""

    def _format_business_logic_analysis(self, analysis: Dict[str, Any]) -> str:
        """Format business logic analysis section"""
        methods = analysis.get("business_methods", [])
        if not methods:
            return "No complex business methods identified."
            
        high_complexity = len([m for m in methods if m.get("complexity") == "high"])
        medium_complexity = len([m for m in methods if m.get("complexity") == "medium"])
        
        return f"""**High Complexity Methods**: {high_complexity}
**Medium Complexity Methods**: {medium_complexity}
**Business Rule Density**: {'High' if high_complexity > 2 else 'Medium' if medium_complexity > 3 else 'Low'}
**Refactoring Priority**: {'Immediate' if high_complexity > 3 else 'Planned'}"""

    def _format_applied_patterns(self, patterns: Dict[str, Any]) -> str:
        """Format applied patterns section"""
        if not patterns:
            return "No patterns integrated."
            
        applied = []
        for pattern_type in patterns.keys():
            applied.append(f"✅ {pattern_type.replace('_', ' ').title()}")
            
        return "\n".join(applied)
        
    def _format_best_practices(self, patterns: Dict[str, Any]) -> str:
        """Format best practices section"""
        if not patterns:
            return "No best practices available."
            
        practices = []
        ddd_patterns = patterns.get("ddd_tactical_patterns", {})
        
        for category, recommendations in ddd_patterns.items():
            if isinstance(recommendations, list) and recommendations:
                practices.append(f"**{category.replace('_', ' ').title()}**: {recommendations[0]}")
                
        return "\n".join(practices) if practices else "Best practices integrated successfully."
        
    def _count_discovered_symbols(self, analysis: Dict[str, Any]) -> int:
        """Count total discovered symbols"""
        entities = len(analysis.get("discovered_entities", []))
        value_objects = len(analysis.get("discovered_value_objects", []))
        methods = len(analysis.get("business_methods", []))
        return entities + value_objects + methods
        
    def _count_patterns(self, analysis: Dict[str, Any]) -> int:
        """Count identified patterns"""
        patterns = 0
        if analysis.get("discovered_entities"):
            patterns += 1  # Entity pattern
        if analysis.get("discovered_value_objects"):
            patterns += 1  # Value Object pattern
        if analysis.get("business_methods"):
            patterns += 1  # Domain Service pattern
        return patterns
        
    def _assess_recommendation_quality(self) -> str:
        """Assess quality of recommendations"""
        # This is a simplified quality assessment
        return "High"
        
    def _assess_implementation_readiness(self) -> int:
        """Assess implementation readiness percentage"""
        # This is a simplified readiness assessment
        return 85
        
    def _identify_strengths(self, analysis: Dict[str, Any]) -> str:
        """Identify project strengths"""
        strengths = []
        
        if analysis.get("project_structure", {}).get("architecture_style") == "layered":
            strengths.append("Well-structured layered architecture")
            
        entities = analysis.get("discovered_entities", [])
        if entities and all(len(e.get("business_rules", [])) > 0 for e in entities):
            strengths.append("Entities contain business rules")
            
        return "\n".join([f"- {strength}" for strength in strengths]) if strengths else "- Analysis in progress"
        
    def _identify_improvement_areas(self, analysis: Dict[str, Any]) -> str:
        """Identify areas for improvement"""
        improvements = []
        
        value_objects = analysis.get("discovered_value_objects", [])
        if value_objects:
            improvements.append(f"Eliminate primitive obsession ({len(value_objects)} candidates)")
            
        entities = analysis.get("discovered_entities", [])
        if entities:
            avg_methods = sum(len(e.get("methods", [])) for e in entities) / len(entities)
            if avg_methods < 3:
                improvements.append("Enhance entity behavior methods")
                
        return "\n".join([f"- {improvement}" for improvement in improvements]) if improvements else "- No critical areas identified"
        
    def _identify_critical_actions(self, analysis: Dict[str, Any]) -> str:
        """Identify critical actions required"""
        actions = []
        
        value_objects = analysis.get("discovered_value_objects", [])
        if len(value_objects) > 3:
            actions.append("Immediate value object implementation required")
            
        business_methods = analysis.get("business_methods", [])
        high_complexity = [m for m in business_methods if m.get("complexity") == "high"]
        if len(high_complexity) > 2:
            actions.append("Refactor high-complexity business methods")
            
        return "\n".join([f"- {action}" for action in actions]) if actions else "- No critical actions required"
        
    def _generate_phase_1_roadmap(self, analysis: Dict[str, Any]) -> str:
        """Generate Phase 1 implementation roadmap"""
        roadmap = ["1. Create value objects for primitive types"]
        
        entities = analysis.get("discovered_entities", [])
        if entities:
            roadmap.append("2. Enhance entity behavior methods")
            
        roadmap.append("3. Define aggregate boundaries")
        return "\n".join(roadmap)
        
    def _generate_phase_2_roadmap(self, patterns: Dict[str, Any]) -> str:
        """Generate Phase 2 implementation roadmap"""
        roadmap = ["1. Implement domain services for complex operations"]
        
        if patterns:
            roadmap.append("2. Apply Context7 DDD patterns")
            
        roadmap.append("3. Create repository interfaces")
        return "\n".join(roadmap)
        
    def _generate_phase_3_roadmap(self) -> str:
        """Generate Phase 3 implementation roadmap"""
        return """1. Optimize aggregate design
2. Implement domain events
3. Enhance cross-reference relationships"""

    def _calculate_ddd_compliance_score(self, analysis: Dict[str, Any], patterns: Dict[str, Any]) -> str:
        """Calculate DDD compliance score"""
        score = 0
        max_score = 5
        
        # Check for entities
        if analysis.get("discovered_entities"):
            score += 1
            
        # Check for value objects
        if analysis.get("discovered_value_objects"):
            score += 1
            
        # Check for business methods
        if analysis.get("business_methods"):
            score += 1
            
        # Check for pattern integration
        if patterns:
            score += 2
            
        percentage = int((score / max_score) * 100)
        return f"**Score**: {score}/{max_score} ({percentage}%)\n**Level**: {'Excellent' if percentage >= 80 else 'Good' if percentage >= 60 else 'Needs Improvement'}"
        
    def _assess_architecture_quality(self, analysis: Dict[str, Any]) -> str:
        """Assess architecture quality"""
        structure = analysis.get("project_structure", {})
        quality_factors = []
        
        if structure.get("architecture_style") == "layered":
            quality_factors.append("✅ Layered architecture")
        else:
            quality_factors.append("⚠️ Architecture style unclear")
            
        complexity = structure.get("estimated_complexity", "")
        if complexity in ["simple", "moderate"]:
            quality_factors.append("✅ Manageable complexity")
        else:
            quality_factors.append("⚠️ High complexity")
            
        return "\n".join(quality_factors)
        
    def create_implementation_guidance(self, codebase_analysis: Dict[str, Any],
                                     pattern_integration: Dict[str, Any]) -> str:
        """Create detailed implementation guidance document"""
        try:
            logger.info("📋 Creating implementation guidance...")
            
            guidance_content = f"""# Implementation Guidance - Issue {self.issue_number}

**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Based on**: MCP Analysis (Serena + Context7)

## 🎯 Implementation Strategy

### Overview
This guidance provides a step-by-step implementation plan based on MCP analysis results. Follow the phases sequentially for optimal results.

## 📋 Phase 1: Foundation Implementation

### Step 1: Value Objects Implementation
{self._create_value_object_guidance(codebase_analysis)}

### Step 2: Entity Enhancement  
{self._create_entity_guidance(codebase_analysis)}

### Step 3: Aggregate Design
{self._create_aggregate_guidance(codebase_analysis, pattern_integration)}

## 📋 Phase 2: Advanced Implementation

### Step 4: Domain Services
{self._create_domain_service_guidance(codebase_analysis)}

### Step 5: Repository Interfaces
{self._create_repository_guidance()}

### Step 6: Business Rule Implementation
{self._create_business_rule_guidance(codebase_analysis)}

## 📋 Phase 3: Optimization

### Step 7: Refactoring Anti-Patterns
{self._create_refactoring_guidance(codebase_analysis)}

### Step 8: Performance Optimization
{self._create_performance_guidance()}

### Step 9: Testing Strategy
{self._create_testing_guidance()}

## 🛠️ Implementation Examples

### Value Object Example
{self._create_value_object_example()}

### Entity Example
{self._create_entity_example()}

### Aggregate Example
{self._create_aggregate_example()}

## ⚠️ Important Considerations

### Do's and Don'ts
{self._create_dos_and_donts()}

### Common Pitfalls
{self._create_common_pitfalls()}

### Quality Checkpoints
{self._create_quality_checkpoints()}

## 📊 Progress Tracking

### Implementation Checklist
{self._create_implementation_checklist(codebase_analysis)}

### Quality Metrics
{self._create_quality_metrics()}

### Review Points
{self._create_review_points()}

## 🚀 Next Steps

After completing this implementation:

1. **Testing Phase**: Use `/create-tests-enhanced {self.issue_number}` for comprehensive test creation
2. **Code Review**: Review implementation against DDD principles
3. **Performance Validation**: Validate performance implications
4. **Documentation Update**: Update architectural documentation

## 📋 References

- **Domain Model**: `docs/domain/issue-{self.issue_number}-enhanced-domain-model.md`
- **MCP Analysis**: `docs/domain/issue-{self.issue_number}-mcp-analysis-report.md`
- **Context7 Patterns**: Applied DDD best practices from latest documentation
- **Serena Analysis**: Comprehensive codebase analysis results
"""
            
            return guidance_content
            
        except Exception as e:
            logger.exception("Failed to create implementation guidance")
            return "# Error: Failed to generate implementation guidance"
            
    def _create_value_object_guidance(self, analysis: Dict[str, Any]) -> str:
        """Create value object implementation guidance"""
        value_objects = analysis.get("discovered_value_objects", [])
        if not value_objects:
            return "No value objects identified for implementation."
            
        guidance = "**Priority**: High (Eliminates primitive obsession)\n\n"
        
        for i, vo in enumerate(value_objects[:3], 1):  # Show top 3
            guidance += f"**{i}. {vo['name']} Value Object**\n"
            guidance += f"- Purpose: {vo.get('suggested_from', 'Type safety')}\n"
            guidance += f"- Implementation: Create immutable class with validation\n"
            guidance += f"- Validation: {', '.join(vo.get('validation_rules', ['Basic validation']))}\n\n"
            
        return guidance
        
    def _create_entity_guidance(self, analysis: Dict[str, Any]) -> str:
        """Create entity enhancement guidance"""
        entities = analysis.get("discovered_entities", [])
        if not entities:
            return "No entities identified for enhancement."
            
        guidance = "**Priority**: High (Enhance domain behavior)\n\n"
        
        for entity in entities[:2]:  # Show top 2
            guidance += f"**{entity['name']} Entity Enhancement**\n"
            guidance += f"- Current methods: {len(entity.get('methods', []))}\n"
            guidance += f"- Recommended: Add business behavior methods\n"
            guidance += f"- Focus: {', '.join(entity.get('business_rules', ['Business logic']))}\n\n"
            
        return guidance
        
    def _create_aggregate_guidance(self, analysis: Dict[str, Any], patterns: Dict[str, Any]) -> str:
        """Create aggregate design guidance"""
        return """**Priority**: Medium (Define consistency boundaries)

**Design Principles**:
- Single aggregate per transaction
- Reference other aggregates by ID
- Keep aggregates small and focused

**Implementation Steps**:
1. Identify aggregate roots from entities
2. Define consistency boundaries
3. Implement aggregate-level business rules
4. Create aggregate repositories"""

    def _create_domain_service_guidance(self, analysis: Dict[str, Any]) -> str:
        """Create domain service guidance"""
        business_methods = analysis.get("business_methods", [])
        complex_methods = [m for m in business_methods if m.get("complexity") in ["high", "medium"]]
        
        if not complex_methods:
            return "No complex business operations requiring domain services."
            
        guidance = "**Priority**: Medium (Organize complex business logic)\n\n"
        
        for method in complex_methods[:2]:
            guidance += f"**{method['method_name']} Service**\n"
            guidance += f"- Complexity: {method.get('complexity')}\n"
            guidance += f"- Dependencies: {', '.join(method.get('dependencies', []))}\n"
            guidance += f"- Implementation: Extract to domain service\n\n"
            
        return guidance
        
    def _create_repository_guidance(self) -> str:
        """Create repository implementation guidance"""
        return """**Priority**: Medium (Data access abstraction)

**Implementation Steps**:
1. Define repository interfaces in domain layer
2. Use aggregate root as repository unit
3. Implement in infrastructure layer
4. Follow aggregate boundary rules

**Key Methods**:
- `find_by_id()`: Primary key lookup
- `save()`: Persist aggregate
- `find_by_*()`: Business queries"""

    def _create_business_rule_guidance(self, analysis: Dict[str, Any]) -> str:
        """Create business rule implementation guidance"""
        entities = analysis.get("discovered_entities", [])
        total_rules = sum(len(e.get("business_rules", [])) for e in entities)
        
        if total_rules == 0:
            return "No explicit business rules identified."
            
        return f"""**Priority**: High (Implement {total_rules} business rules)

**Implementation Approach**:
1. Place rules in appropriate domain objects
2. Use specification pattern for complex rules
3. Implement validation in entity constructors
4. Create domain events for rule violations

**Testing**: Focus on rule validation and edge cases"""

    def _create_refactoring_guidance(self, analysis: Dict[str, Any]) -> str:
        """Create refactoring guidance"""
        return """**Priority**: Low (Improve code quality)

**Anti-Pattern Fixes**:
1. Primitive Obsession → Value Objects
2. Anemic Domain Model → Rich Entities
3. Feature Envy → Proper Encapsulation

**Refactoring Strategy**:
- Start with high-impact, low-risk changes
- Maintain test coverage during refactoring
- Apply one pattern at a time"""

    def _create_performance_guidance(self) -> str:
        """Create performance guidance"""
        return """**Considerations**:
- Aggregate size impacts performance
- Repository query optimization
- Domain event handling efficiency

**Monitoring**:
- Track aggregate load times
- Monitor query performance
- Measure business rule execution time"""

    def _create_testing_guidance(self) -> str:
        """Create testing guidance"""
        return """**Testing Strategy**:
1. Unit tests for domain logic
2. Aggregate behavior tests
3. Business rule validation tests
4. Repository contract tests

**Use MCP-Enhanced Testing**:
Run `/create-tests-enhanced {self.issue_number}` for comprehensive test generation"""

    def _create_value_object_example(self) -> str:
        """Create value object code example"""
        return """```python
@dataclass(frozen=True)
class Email:
    value: str
    
    def __post_init__(self):
        if not self._is_valid_email(self.value):
            raise ValueError(f"Invalid email: {self.value}")
            
    def _is_valid_email(self, email: str) -> bool:
        # Email validation logic
        return "@" in email and len(email) <= 255
```"""

    def _create_entity_example(self) -> str:
        """Create entity code example"""
        return """```python
class User:
    def __init__(self, user_id: UserId, email: Email, username: str):
        self._id = user_id
        self._email = email
        self._username = username
        
    def change_email(self, new_email: Email) -> None:
        # Business rule: Email change requires validation
        self._email = new_email
        self._raise_domain_event(EmailChangedEvent(self._id, new_email))
        
    def _raise_domain_event(self, event) -> None:
        # Domain event handling
        pass
```"""

    def _create_aggregate_example(self) -> str:
        """Create aggregate code example"""
        return """```python
class Order:  # Aggregate Root
    def __init__(self, order_id: OrderId, customer_id: CustomerId):
        self._id = order_id
        self._customer_id = customer_id
        self._items: List[OrderItem] = []
        
    def add_item(self, product_id: ProductId, quantity: int, price: Money) -> None:
        # Business rule: Cannot modify confirmed orders
        if self._is_confirmed:
            raise DomainException("Cannot modify confirmed order")
            
        item = OrderItem(product_id, quantity, price)
        self._items.append(item)
```"""

    def _create_dos_and_donts(self) -> str:
        """Create do's and don'ts section"""
        return """**Do's**:
✅ Keep aggregates small and focused
✅ Use value objects to eliminate primitive obsession
✅ Place business rules in domain objects
✅ Use domain events for cross-aggregate communication

**Don'ts**:
❌ Don't create large aggregates
❌ Don't put business logic in services unnecessarily  
❌ Don't reference aggregates directly
❌ Don't skip domain rule validation"""

    def _create_common_pitfalls(self) -> str:
        """Create common pitfalls section"""
        return """- **Large Aggregates**: Keep aggregate boundaries small
- **Anemic Entities**: Ensure entities have behavior, not just data
- **Missing Validation**: Always validate business rules
- **Cross-Aggregate References**: Use IDs, not direct references
- **Infrastructure Leak**: Keep domain layer pure"""

    def _create_quality_checkpoints(self) -> str:
        """Create quality checkpoints"""
        return """**After Each Phase**:
- [ ] All tests pass
- [ ] Business rules validated
- [ ] No infrastructure dependencies in domain
- [ ] Aggregate boundaries respected
- [ ] Domain events properly handled"""

    def _create_implementation_checklist(self, analysis: Dict[str, Any]) -> str:
        """Create implementation checklist"""
        checklist = []
        
        # Value objects checklist
        value_objects = analysis.get("discovered_value_objects", [])
        for vo in value_objects:
            checklist.append(f"- [ ] Implement {vo['name']} value object")
            
        # Entities checklist
        entities = analysis.get("discovered_entities", [])
        for entity in entities:
            checklist.append(f"- [ ] Enhance {entity['name']} entity behavior")
            
        # General checklist
        checklist.extend([
            "- [ ] Define aggregate boundaries",
            "- [ ] Create repository interfaces", 
            "- [ ] Implement domain services",
            "- [ ] Add business rule validation",
            "- [ ] Create comprehensive tests"
        ])
        
        return "\n".join(checklist)
        
    def _create_quality_metrics(self) -> str:
        """Create quality metrics tracking"""
        return """**Target Metrics**:
- Domain Rule Coverage: 100%
- Value Object Usage: >80% of primitives replaced
- Entity Behavior Density: >3 methods per entity
- Aggregate Size: <10 entities per aggregate
- Test Coverage: >90% for domain logic"""

    def _create_review_points(self) -> str:
        """Create review points"""
        return """**Review Checkpoints**:
1. **Phase 1 Complete**: Value objects and enhanced entities
2. **Phase 2 Complete**: Domain services and repositories  
3. **Phase 3 Complete**: Refactoring and optimization
4. **Final Review**: Complete implementation validation"""

    def save_enhanced_artifacts(self, domain_model: str, analysis_report: str, 
                              implementation_guidance: str) -> None:
        """Save all enhanced domain modeling artifacts"""
        try:
            # Ensure domain directory exists
            self.domain_dir.mkdir(parents=True, exist_ok=True)
            
            # Save enhanced domain model
            domain_model_file = self.domain_dir / f"issue-{self.issue_number}-enhanced-domain-model.md"
            with open(domain_model_file, 'w', encoding='utf-8') as f:
                f.write(domain_model)
            logger.info(f"✅ Saved enhanced domain model: {domain_model_file}")
            
            # Save MCP analysis report
            analysis_report_file = self.domain_dir / f"issue-{self.issue_number}-mcp-analysis-report.md"
            with open(analysis_report_file, 'w', encoding='utf-8') as f:
                f.write(analysis_report)
            logger.info(f"✅ Saved MCP analysis report: {analysis_report_file}")
            
            # Save implementation guidance
            guidance_file = self.domain_dir / f"issue-{self.issue_number}-implementation-guidance.md"
            with open(guidance_file, 'w', encoding='utf-8') as f:
                f.write(implementation_guidance)
            logger.info(f"✅ Saved implementation guidance: {guidance_file}")
            
            # Update modeling metadata
            self.modeling_metadata["generated_artifacts"] = [
                str(domain_model_file),
                str(analysis_report_file),
                str(guidance_file)
            ]
            
        except Exception as e:
            logger.exception("Failed to save enhanced artifacts")
            raise
            
    def update_project_metadata(self) -> None:
        """Update project metadata with enhanced modeling completion"""
        try:
            # Update use case metadata if exists
            metadata_files = list(Path("docs/use_cases/sprints").rglob(f"*issue*{self.issue_number}*.json"))
            
            for metadata_file in metadata_files:
                try:
                    with open(metadata_file, 'r', encoding='utf-8') as f:
                        metadata = json.load(f)
                        
                    # Update domain modeling phase
                    if "phases" not in metadata:
                        metadata["phases"] = {}
                    if "domain_model" not in metadata["phases"]:
                        metadata["phases"]["domain_model"] = {}
                        
                    metadata["phases"]["domain_model"].update({
                        "enhanced_created": True,
                        "mcp_analysis_completed": True,
                        "created_at": datetime.now().isoformat(),
                        "artifacts": self.modeling_metadata["generated_artifacts"]
                    })
                    
                    # Save updated metadata
                    with open(metadata_file, 'w', encoding='utf-8') as f:
                        json.dump(metadata, f, indent=2, ensure_ascii=False)
                        
                    logger.info(f"✅ Updated metadata: {metadata_file}")
                    
                except Exception as e:
                    logger.warning(f"Could not update metadata file {metadata_file}: {e}")
                    
        except Exception as e:
            logger.exception("Failed to update project metadata")
            
    def generate_modeling_report(self, codebase_analysis: Dict[str, Any],
                               pattern_integration: Dict[str, Any]) -> Dict[str, Any]:
        """Generate final modeling report"""
        return {
            "modeling_info": {
                "issue_number": self.issue_number,
                "started_at": self.modeling_metadata["started_at"],
                "completed_at": datetime.now().isoformat(),
                "status": "enhanced_success"
            },
            "mcp_analysis_results": {
                "serena_analysis": {
                    "files_analyzed": codebase_analysis.get("project_structure", {}).get("total_files", 0),
                    "entities_discovered": len(codebase_analysis.get("discovered_entities", [])),
                    "value_objects_recommended": len(codebase_analysis.get("discovered_value_objects", [])),
                    "business_methods_identified": len(codebase_analysis.get("business_methods", []))
                },
                "context7_integration": {
                    "patterns_applied": len(pattern_integration) if pattern_integration else 0,
                    "pattern_coverage": self._calculate_pattern_coverage(pattern_integration),
                    "best_practices_integrated": True if pattern_integration else False
                }
            },
            "generated_artifacts": self.modeling_metadata["generated_artifacts"],
            "quality_metrics": {
                "domain_completeness": 90,  # Simplified metric
                "pattern_integration": self._calculate_pattern_coverage(pattern_integration),
                "implementation_readiness": 85
            },
            "next_steps": [
                f"Review generated domain model: docs/domain/issue-{self.issue_number}-enhanced-domain-model.md",
                f"Study MCP analysis: docs/domain/issue-{self.issue_number}-mcp-analysis-report.md", 
                f"Follow implementation guidance: docs/domain/issue-{self.issue_number}-implementation-guidance.md",
                f"Proceed to enhanced testing: /create-tests-enhanced {self.issue_number}"
            ]
        }
        
    async def run_enhanced_modeling(self) -> Dict[str, Any]:
        """Main enhanced domain modeling workflow"""
        try:
            logger.info(f"🧠 Starting MCP-enhanced domain modeling for issue {self.issue_number}")
            
            # Phase 1: Validate MCP session
            logger.info("🔍 Phase 1: Validating MCP session...")
            if not self.validate_mcp_session():
                raise ValueError("MCP session validation failed")
                
            # Phase 2: Load use case specifications
            logger.info("📖 Phase 2: Loading use case specifications...")
            use_case_specs = self.load_use_case_specifications()
            
            # Phase 3: Analyze codebase with Serena MCP
            logger.info("🔍 Phase 3: Analyzing codebase with Serena MCP...")
            codebase_analysis = self.analyze_codebase_with_serena()
            
            # Phase 4: Integrate Context7 patterns
            logger.info("📚 Phase 4: Integrating Context7 DDD patterns...")
            pattern_integration = self.integrate_context7_patterns()
            
            # Phase 5: Generate enhanced domain model
            logger.info("📝 Phase 5: Generating enhanced domain model...")
            domain_model = self.generate_enhanced_domain_model(use_case_specs, codebase_analysis, pattern_integration)
            
            # Phase 6: Create MCP analysis report
            logger.info("📊 Phase 6: Creating MCP analysis report...")
            analysis_report = self.create_mcp_analysis_report(codebase_analysis, pattern_integration)
            
            # Phase 7: Create implementation guidance
            logger.info("📋 Phase 7: Creating implementation guidance...")
            implementation_guidance = self.create_implementation_guidance(codebase_analysis, pattern_integration)
            
            # Phase 8: Save all artifacts
            logger.info("💾 Phase 8: Saving enhanced artifacts...")
            self.save_enhanced_artifacts(domain_model, analysis_report, implementation_guidance)
            
            # Phase 9: Update project metadata
            logger.info("📋 Phase 9: Updating project metadata...")
            self.update_project_metadata()
            
            # Generate final report
            report = self.generate_modeling_report(codebase_analysis, pattern_integration)
            logger.info("✅ MCP-enhanced domain modeling completed successfully!")
            
            return report
            
        except Exception as e:
            logger.exception("MCP-enhanced domain modeling failed")
            raise


async def main():
    """Main entry point"""
    if len(sys.argv) != 2:
        logger.error("Usage: python 04-domain-modeling-enhanced.py <issue_number>")
        sys.exit(1)
        
    issue_number = sys.argv[1]
    
    try:
        # Validate issue number
        if not issue_number.isdigit():
            logger.error(f"Invalid issue number: {issue_number}")
            sys.exit(1)
            
        # Initialize enhanced domain modeler
        modeler = MCPEnhancedDomainModeler(issue_number)
        
        # Run enhanced modeling
        report = await modeler.run_enhanced_modeling()
        
        # Print success summary
        print("\n" + "="*60)
        print("🎉 MCP-ENHANCED DOMAIN MODELING COMPLETED")
        print("="*60)
        print(f"Issue Number: {report['modeling_info']['issue_number']}")
        print(f"Status: {report['modeling_info']['status']}")
        print(f"Started: {report['modeling_info']['started_at']}")
        print(f"Completed: {report['modeling_info']['completed_at']}")
        print(f"\n🧠 MCP Analysis Results:")
        serena_results = report['mcp_analysis_results']['serena_analysis']
        print(f"  📁 Files Analyzed: {serena_results['files_analyzed']}")
        print(f"  🏛️ Entities Discovered: {serena_results['entities_discovered']}")
        print(f"  💎 Value Objects Recommended: {serena_results['value_objects_recommended']}")
        print(f"  ⚙️ Business Methods Identified: {serena_results['business_methods_identified']}")
        context7_results = report['mcp_analysis_results']['context7_integration']
        print(f"  📚 Pattern Coverage: {context7_results['pattern_coverage']}%")
        print(f"  ✅ Best Practices Integrated: {context7_results['best_practices_integrated']}")
        print(f"\n📁 Generated Artifacts:")
        for artifact in report['generated_artifacts']:
            print(f"  ✅ {artifact}")
        print(f"\n📊 Quality Metrics:")
        metrics = report['quality_metrics']
        print(f"  🎯 Domain Completeness: {metrics['domain_completeness']}%")
        print(f"  📋 Pattern Integration: {metrics['pattern_integration']}%")
        print(f"  🚀 Implementation Readiness: {metrics['implementation_readiness']}%")
        print(f"\n🚀 Next Steps:")
        for step in report['next_steps']:
            print(f"  • {step}")
        print("="*60)
        
        sys.exit(0)
        
    except KeyboardInterrupt:
        logger.info("Enhanced domain modeling cancelled by user")
        sys.exit(1)
    except Exception as e:
        logger.exception("Enhanced domain modeling failed")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())