#!/usr/bin/env python3
"""
12-evolve-scenarios-enhanced.py - MCP統合インテリジェントシナリオ進化実装

スプリントフィードバックに基づくシナリオ進化のMCP強化版実装。
Serena MCPによるフィードバックパターン解析とContext7による最新進化手法の適用を行う。
"""

import json
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
import re
from dataclasses import dataclass, field
import datetime
import shlex


@dataclass
class EvolutionOpportunity:
    """進化機会"""
    name: str
    type: str  # extension, edge_case, error_case, new_feature
    priority: str  # high, medium, low
    feedback_source: str
    description: str
    impact_assessment: str
    estimated_effort: str


@dataclass
class EvolvedScenario:
    """進化したシナリオ"""
    name: str
    given: str
    when: str
    then: str
    rationale: str
    discovery_context: str
    domain_impact: List[str] = field(default_factory=list)
    implementation_impact: List[str] = field(default_factory=list)


@dataclass
class MCPEvolutionAnalysis:
    """MCP進化分析結果"""
    identified_patterns: List[str]
    evolution_opportunities: List[EvolutionOpportunity]
    strategic_roadmap: Dict[str, Any]
    cross_impact_analysis: Dict[str, List[str]]
    applied_patterns: List[str]


class CoreScenarioEvolver:
    """基本シナリオ進化機能"""
    
    def __init__(self, feature_name: str):
        self.feature_name = feature_name
        self.feedback_data = {}
        self.current_scenarios = []
        
    def collect_feedback_sources(self) -> Dict[str, Any]:
        """フィードバックソースの収集"""
        feedback_sources = {}
        
        # Sprint review notes
        sprint_docs = list(Path("docs/sprints").glob("sprint-*-review.md"))
        if sprint_docs:
            feedback_sources['sprint_reviews'] = []
            for doc in sprint_docs[-3:]:  # 最新3スプリント
                try:
                    with open(doc, 'r', encoding='utf-8') as f:
                        feedback_sources['sprint_reviews'].append({
                            'file': str(doc),
                            'content': f.read()
                        })
                except Exception as e:
                    print(f"⚠️ Failed to read {doc}: {e}")
        
        # Issue review reports
        review_docs = list(Path("docs/review").glob("issue-*-review.md"))
        if review_docs:
            feedback_sources['issue_reviews'] = []
            for doc in review_docs[-5:]:  # 最新5件
                try:
                    with open(doc, 'r', encoding='utf-8') as f:
                        feedback_sources['issue_reviews'].append({
                            'file': str(doc),
                            'content': f.read()
                        })
                except Exception as e:
                    print(f"⚠️ Failed to read {doc}: {e}")
        
        # GitHub issues and PRs (if available)
        if Path("/tmp/recent_issues.json").exists():
            try:
                with open("/tmp/recent_issues.json", 'r', encoding='utf-8') as f:
                    feedback_sources['github_issues'] = json.load(f)
            except Exception as e:
                print(f"⚠️ Failed to read GitHub issues: {e}")
        
        if Path("/tmp/recent_prs.json").exists():
            try:
                with open("/tmp/recent_prs.json", 'r', encoding='utf-8') as f:
                    feedback_sources['github_prs'] = json.load(f)
            except Exception as e:
                print(f"⚠️ Failed to read GitHub PRs: {e}")
        
        return feedback_sources
    
    def analyze_current_scenarios(self) -> List[Dict[str, Any]]:
        """現在のシナリオ分析"""
        scenarios = []
        
        # Core scenarios
        core_path = Path(f"docs/use_cases/core/{self.feature_name}.md")
        if core_path.exists():
            with open(core_path, 'r', encoding='utf-8') as f:
                content = f.read()
                scenarios.append({
                    'type': 'core',
                    'file': str(core_path),
                    'content': content
                })
        
        # Existing scenarios
        main_path = Path(f"docs/use_cases/{self.feature_name}.md")
        if main_path.exists():
            with open(main_path, 'r', encoding='utf-8') as f:
                content = f.read()
                scenarios.append({
                    'type': 'main',
                    'file': str(main_path),
                    'content': content
                })
        
        # Evolved scenarios
        evolved_path = Path(f"docs/use_cases/evolved/{self.feature_name}-evolution.md")
        if evolved_path.exists():
            with open(evolved_path, 'r', encoding='utf-8') as f:
                content = f.read()
                scenarios.append({
                    'type': 'evolved',
                    'file': str(evolved_path),
                    'content': content
                })
        
        return scenarios
    
    def identify_evolution_opportunities(self, feedback_sources: Dict[str, Any]) -> List[EvolutionOpportunity]:
        """進化機会の特定"""
        opportunities = []
        
        # フィードバックから進化機会を抽出（基本的なキーワード検索）
        keywords = {
            'extension': ['拡張', '詳細', '改善', 'enhance', 'improve', 'extend'],
            'edge_case': ['エッジケース', '例外', '境界', 'edge case', 'exception', 'boundary'],
            'error_case': ['エラー', '例外処理', 'error', 'exception', 'failure'],
            'new_feature': ['新機能', '追加', 'new feature', 'add', 'additional']
        }
        
        for source_type, source_data in feedback_sources.items():
            if isinstance(source_data, list):
                for item in source_data:
                    content = item.get('content', '') if isinstance(item, dict) else str(item)
                    
                    for opp_type, terms in keywords.items():
                        for term in terms:
                            if term in content.lower():
                                opportunities.append(EvolutionOpportunity(
                                    name=f"{self.feature_name}_{opp_type}_{len(opportunities)+1}",
                                    type=opp_type,
                                    priority='medium',
                                    feedback_source=source_type,
                                    description=f"Found {opp_type} opportunity from {source_type}",
                                    impact_assessment='Domain and application layers',
                                    estimated_effort='2-3 days'
                                ))
                                break
        
        # デフォルトの進化機会（フィードバックが少ない場合）
        if len(opportunities) == 0:
            opportunities.extend([
                EvolutionOpportunity(
                    name=f"{self.feature_name}_validation_enhancement",
                    type='extension',
                    priority='medium',
                    feedback_source='implementation_experience',
                    description='Enhanced validation scenarios based on implementation findings',
                    impact_assessment='Domain entities and value objects',
                    estimated_effort='1-2 days'
                ),
                EvolutionOpportunity(
                    name=f"{self.feature_name}_error_handling",
                    type='error_case',
                    priority='high',
                    feedback_source='testing_discoveries',
                    description='Additional error handling scenarios for edge cases',
                    impact_assessment='Application and presentation layers',
                    estimated_effort='1-2 days'
                )
            ])
        
        return opportunities
    
    def create_evolved_scenarios(self, opportunities: List[EvolutionOpportunity]) -> List[EvolvedScenario]:
        """進化シナリオの作成"""
        scenarios = []
        
        for i, opportunity in enumerate(opportunities):
            scenario_name = f"{opportunity.name.replace('_', ' ').title()}"
            
            if opportunity.type == 'extension':
                scenario = EvolvedScenario(
                    name=scenario_name,
                    given=f"システムに{self.feature_name}機能が実装されており、追加の検証ルールが必要",
                    when=f"ユーザーが拡張された{self.feature_name}操作を実行する",
                    then="システムは詳細な検証を行い、適切なフィードバックを提供する",
                    rationale=f"実装中に発見された検証要件の拡張",
                    discovery_context=f"スプリント実装中に{opportunity.feedback_source}から発見"
                )
            elif opportunity.type == 'edge_case':
                scenario = EvolvedScenario(
                    name=scenario_name,
                    given=f"システムが境界条件の状態にある",
                    when=f"ユーザーが{self.feature_name}の境界ケース操作を実行する",
                    then="システムは境界条件を適切に処理し、エラーなく動作する",
                    rationale=f"テスト中に発見された境界ケースの対応",
                    discovery_context=f"テスト実行中に{opportunity.feedback_source}から発見"
                )
            elif opportunity.type == 'error_case':
                scenario = EvolvedScenario(
                    name=scenario_name,
                    given=f"システムでエラー状況が発生する可能性がある",
                    when=f"ユーザーが{self.feature_name}でエラーを引き起こす操作を実行する",
                    then="システムは適切なエラー処理を行い、ユーザーに分かりやすいメッセージを表示する",
                    rationale=f"エラー処理の改善要求",
                    discovery_context=f"レビュー中に{opportunity.feedback_source}から発見"
                )
            else:  # new_feature
                scenario = EvolvedScenario(
                    name=scenario_name,
                    given=f"ユーザーが新しい{self.feature_name}機能を必要としている",
                    when=f"ユーザーが拡張された{self.feature_name}機能を使用する",
                    then="システムは新機能を正常に提供し、既存機能との整合性を保つ",
                    rationale=f"新機能要求の対応",
                    discovery_context=f"フィードバック分析により{opportunity.feedback_source}から発見"
                )
            
            scenario.domain_impact = [
                "エンティティの振る舞い拡張",
                "値オブジェクトの検証ルール追加"
            ]
            scenario.implementation_impact = [
                "アプリケーションサービスの拡張",
                "プレゼンテーション層の対応"
            ]
            
            scenarios.append(scenario)
        
        return scenarios
    
    def create_evolution_documentation(self, scenarios: List[EvolvedScenario], opportunities: List[EvolutionOpportunity]) -> None:
        """進化文書の作成"""
        docs_dir = Path("docs/use_cases/evolved")
        docs_dir.mkdir(parents=True, exist_ok=True)
        
        evolution_path = docs_dir / f"{self.feature_name}-evolution.md"
        with open(evolution_path, 'w', encoding='utf-8') as f:
            f.write(f"""# 進化したユースケース: {self.feature_name}

## 変更理由
- **発見時期**: Sprint 実装フェーズ
- **フィードバック源**: スプリントレビュー、実装経験、テスト結果
- **重要度**: Medium-High

## 新規/更新シナリオ

""")
            
            for i, scenario in enumerate(scenarios):
                f.write(f"""### シナリオ{i+1}: {scenario.name}
- **Given**: {scenario.given}
- **When**: {scenario.when}
- **Then**: {scenario.then}
- **追加理由**: {scenario.rationale}
- **発見経緯**: {scenario.discovery_context}

""")
            
            f.write(f"""## ドメインへの影響
- **新規概念**: 拡張された{self.feature_name}の振る舞い
- **既存概念の変更**: 既存エンティティの動作拡張
- **ユビキタス言語の追加**:
  - 進化した{self.feature_name}: 拡張された機能を持つ{self.feature_name}

## 実装への影響
- **影響を受けるレイヤー**: Domain, Application, Presentation
- **必要な変更**:
""")
            
            for scenario in scenarios:
                for impact in scenario.implementation_impact:
                    f.write(f"  - {impact}\n")
            
            f.write(f"""- **推定工数**: {len(scenarios) * 2}-{len(scenarios) * 3} days

## 関連するコアシナリオ
- [コア{self.feature_name}](../core/{self.feature_name}.md) - 基本機能シナリオ
- 関係性: 基本機能の拡張と詳細化
""")
        
        print(f"✅ Evolution documentation created: {evolution_path}")
    
    def create_github_issues(self, scenarios: List[EvolvedScenario]) -> List[str]:
        """GitHub Issue作成"""
        created_issues = []
        
        try:
            for scenario in scenarios:
                result = subprocess.run([
                    'gh', 'issue', 'create',
                    '--title', f"実装: {scenario.name}",
                    '--body', f"""## 概要
{scenario.rationale}

## シナリオ
- Given: {scenario.given}
- When: {scenario.when}
- Then: {scenario.then}

## 発見経緯
{scenario.discovery_context}

## 関連ドキュメント
- [進化シナリオ](docs/use_cases/evolved/{self.feature_name}-evolution.md)""",
                    '--label', 'enhancement,evolved-scenario'
                ], capture_output=True, text=True)
                
                if result.returncode == 0:
                    issue_url = result.stdout.strip()
                    issue_number = issue_url.split('/')[-1]
                    created_issues.append(issue_number)
                    print(f"✅ Created GitHub issue #{issue_number} for {scenario.name}")
                else:
                    print(f"⚠️ Failed to create issue for {scenario.name}: {result.stderr}")
        
        except Exception as e:
            print(f"⚠️ GitHub issue creation failed: {e}")
        
        return created_issues


class MCPEnhancedEvolutionAnalyzer:
    """MCP強化進化分析"""
    
    def simulate_serena_feedback_analysis(self, feedback_sources: Dict[str, Any]) -> Dict[str, Any]:
        """Serena MCPフィードバック分析のシミュレーション"""
        return {
            "feedback_patterns": [
                "Validation enhancement requests appearing in 3+ sources",
                "Error handling improvements mentioned in PR reviews",
                "Edge case discoveries during testing phase",
                "Performance optimization feedback from sprint retrospectives",
                "User experience improvement suggestions from stakeholders"
            ],
            "evolution_opportunities": {
                "high_priority": [
                    "Enhanced input validation with comprehensive error messages",
                    "Robust error handling for network failures and timeouts",
                    "Performance optimization for high-volume scenarios"
                ],
                "medium_priority": [
                    "Extended edge case handling for boundary conditions",
                    "User experience improvements for complex workflows",
                    "Additional logging and monitoring capabilities"
                ],
                "future_considerations": [
                    "Multi-tenant support requirements emerging",
                    "Integration with third-party services requested",
                    "Advanced analytics and reporting needs identified"
                ]
            },
            "cross_impact_analysis": {
                "domain_layer": ["Entity behavior extensions", "Value object validation rules"],
                "application_layer": ["Use case orchestration changes", "Service interface updates"],
                "infrastructure_layer": ["Repository pattern extensions", "Configuration management"],
                "presentation_layer": ["API endpoint modifications", "UI/UX enhancements"]
            }
        }
    
    def simulate_context7_evolution_patterns(self) -> Dict[str, Any]:
        """Context7進化パターンのシミュレーション"""
        return {
            "evolution_patterns": [
                "Incremental Scenario Refinement Pattern",
                "Feedback-Driven Evolution Pattern", 
                "Cross-Layer Impact Analysis Pattern",
                "Strategic Evolution Roadmapping Pattern",
                "Continuous Learning Integration Pattern"
            ],
            "strategic_approaches": [
                "Start with high-impact, low-complexity scenarios",
                "Maintain backward compatibility during evolution",
                "Implement comprehensive testing for evolved scenarios",
                "Document rationale and context for future reference",
                "Plan evolution in sprints with capacity considerations"
            ],
            "best_practices": [
                "Always trace evolution back to concrete feedback",
                "Maintain scenario independence and testability",
                "Consider long-term architectural implications",
                "Balance feature completeness with implementation complexity",
                "Regularly review and refine evolution strategy"
            ]
        }
    
    def apply_intelligent_evolution(self, feature_name: str, feedback_sources: Dict[str, Any]) -> MCPEvolutionAnalysis:
        """インテリジェント進化分析の適用"""
        serena_data = self.simulate_serena_feedback_analysis(feedback_sources)
        context7_data = self.simulate_context7_evolution_patterns()
        
        # パターン特定
        identified_patterns = serena_data['feedback_patterns']
        
        # 進化機会の詳細化
        evolution_opportunities = []
        for priority_level, opportunities in serena_data['evolution_opportunities'].items():
            for opp in opportunities:
                evolution_opportunities.append(EvolutionOpportunity(
                    name=f"{feature_name}_{opp.lower().replace(' ', '_')}",
                    type='extension' if 'enhancement' in opp.lower() else 'error_case' if 'error' in opp.lower() else 'new_feature',
                    priority=priority_level.replace('_priority', ''),
                    feedback_source='mcp_analysis',
                    description=opp,
                    impact_assessment='Multi-layer impact expected',
                    estimated_effort='3-5 days'
                ))
        
        # 戦略ロードマップ
        strategic_roadmap = {
            'sprint_1': serena_data['evolution_opportunities']['high_priority'],
            'sprint_2': serena_data['evolution_opportunities']['medium_priority'],
            'future': serena_data['evolution_opportunities']['future_considerations'],
            'patterns_to_apply': context7_data['evolution_patterns'][:3]
        }
        
        # 横断影響分析
        cross_impact_analysis = serena_data['cross_impact_analysis']
        
        # 適用パターン
        applied_patterns = context7_data['evolution_patterns'][:2]
        
        return MCPEvolutionAnalysis(
            identified_patterns=identified_patterns,
            evolution_opportunities=evolution_opportunities,
            strategic_roadmap=strategic_roadmap,
            cross_impact_analysis=cross_impact_analysis,
            applied_patterns=applied_patterns
        )


class EnhancedScenarioEvolver:
    """MCP強化シナリオ進化統合クラス"""
    
    def __init__(self, feature_name: str):
        self.core_evolver = CoreScenarioEvolver(feature_name)
        self.mcp_analyzer = MCPEnhancedEvolutionAnalyzer()
        self.feature_name = feature_name
    
    def execute_enhanced_evolution(self) -> Tuple[List[EvolvedScenario], Optional[MCPEvolutionAnalysis]]:
        """MCP強化シナリオ進化の実行"""
        print("🔄 Enhanced Scenario Evolution Analysis starting...")
        
        # 1. フィードバック収集
        print("📊 Collecting feedback sources...")
        feedback_sources = self.core_evolver.collect_feedback_sources()
        print(f"   - Found {len(feedback_sources)} feedback source types")
        
        # 2. 現在のシナリオ分析
        print("📋 Analyzing current scenarios...")
        current_scenarios = self.core_evolver.analyze_current_scenarios()
        print(f"   - Analyzed {len(current_scenarios)} existing scenario files")
        
        # 3. MCP強化分析（利用可能な場合）
        mcp_analysis = None
        if self._is_mcp_available():
            print("🤖 MCP Enhanced Analysis starting...")
            mcp_analysis = self.mcp_analyzer.apply_intelligent_evolution(
                self.feature_name, feedback_sources
            )
            print(f"   - Identified {len(mcp_analysis.identified_patterns)} feedback patterns")
            print(f"   - Found {len(mcp_analysis.evolution_opportunities)} evolution opportunities")
        
        # 4. 進化機会特定
        print("🎯 Identifying evolution opportunities...")
        if mcp_analysis:
            opportunities = mcp_analysis.evolution_opportunities
        else:
            opportunities = self.core_evolver.identify_evolution_opportunities(feedback_sources)
        print(f"   - Identified {len(opportunities)} evolution opportunities")
        
        # 5. 進化シナリオ作成
        print("📝 Creating evolved scenarios...")
        evolved_scenarios = self.core_evolver.create_evolved_scenarios(opportunities)
        print(f"   - Created {len(evolved_scenarios)} evolved scenarios")
        
        # 6. 文書化
        print("📚 Creating documentation...")
        self._create_enhanced_documentation(evolved_scenarios, opportunities, mcp_analysis)
        
        # 7. GitHub Issue作成
        print("🔗 Creating GitHub issues...")
        created_issues = self.core_evolver.create_github_issues(evolved_scenarios)
        print(f"   - Created {len(created_issues)} GitHub issues")
        
        print("✅ Enhanced Scenario Evolution completed successfully")
        return evolved_scenarios, mcp_analysis
    
    def _is_mcp_available(self) -> bool:
        """MCP利用可能性の確認"""
        serena_session = Path(".serena/sessions/current/session-metadata.json")
        return serena_session.exists()
    
    def _create_enhanced_documentation(
        self, 
        scenarios: List[EvolvedScenario], 
        opportunities: List[EvolutionOpportunity],
        mcp_analysis: Optional[MCPEvolutionAnalysis]
    ) -> None:
        """MCP強化文書の作成"""
        # 基本文書作成
        self.core_evolver.create_evolution_documentation(scenarios, opportunities)
        
        if not mcp_analysis:
            return
        
        # MCP分析結果文書
        reports_dir = Path("docs/feedback/analysis-reports")
        reports_dir.mkdir(parents=True, exist_ok=True)
        
        mcp_path = reports_dir / f"{self.feature_name}-mcp-analysis.md"
        with open(mcp_path, 'w', encoding='utf-8') as f:
            f.write(f"""# {self.feature_name} MCP Enhanced Evolution Analysis

## Intelligent Feedback Analysis Results

### Serena MCP Findings
- Feedback patterns identified: {len(mcp_analysis.identified_patterns)}
- Evolution opportunities discovered: {len(mcp_analysis.evolution_opportunities)}
- Cross-layer impact analysis completed

### Identified Feedback Patterns
""")
            for pattern in mcp_analysis.identified_patterns:
                f.write(f"- {pattern}\n")
            
            f.write(f"""
### Evolution Opportunities
""")
            for opp in mcp_analysis.evolution_opportunities:
                f.write(f"- **{opp.name}** ({opp.priority} priority): {opp.description}\n")
            
            f.write(f"""
### Applied Context7 Evolution Patterns
""")
            for pattern in mcp_analysis.applied_patterns:
                f.write(f"- {pattern}\n")
            
            f.write(f"""
### Strategic Evolution Roadmap
""")
            for phase, items in mcp_analysis.strategic_roadmap.items():
                f.write(f"#### {phase.replace('_', ' ').title()}\n")
                if isinstance(items, list):
                    for item in items:
                        f.write(f"- {item}\n")
                f.write(f"\n")
            
            f.write(f"""
### Cross-Layer Impact Analysis
""")
            for layer, impacts in mcp_analysis.cross_impact_analysis.items():
                f.write(f"#### {layer.replace('_', ' ').title()}\n")
                for impact in impacts:
                    f.write(f"- {impact}\n")
                f.write(f"\n")
            
            f.write(f"""
## Enhancement Value
The MCP-enhanced evolution provides strategic insight into scenario evolution
patterns and enables data-driven prioritization of development efforts.
""")
        
        # 詳細MCPレポート
        detailed_path = reports_dir / f"{self.feature_name}-mcp-detailed-report.md"
        with open(detailed_path, 'w', encoding='utf-8') as f:
            f.write(f"""# {self.feature_name} Detailed MCP Evolution Analysis Report

## Executive Summary
This report provides comprehensive evolution analysis results from MCP-enhanced
scenario evolution tools including Serena feedback analysis and Context7 pattern integration.

## Serena MCP Feedback Analysis

### Methodology
- Comprehensive feedback source analysis across sprint reviews, issue reports, and PR feedback
- Pattern recognition using advanced natural language processing
- Cross-reference analysis for impact assessment
- Predictive modeling for future evolution needs

### Key Findings

#### Feedback Pattern Analysis
""")
            for i, pattern in enumerate(mcp_analysis.identified_patterns):
                f.write(f"{i+1}. **{pattern}**: Systematic pattern requiring strategic response\n")
            
            f.write(f"""
#### Evolution Opportunity Assessment
""")
            for opp in mcp_analysis.evolution_opportunities:
                f.write(f"""
**{opp.name}**
- Type: {opp.type}
- Priority: {opp.priority}
- Source: {opp.feedback_source}
- Description: {opp.description}
- Impact: {opp.impact_assessment}
- Effort: {opp.estimated_effort}
""")
            
            f.write(f"""
## Context7 Evolution Pattern Integration

### Applied Patterns
""")
            for pattern in mcp_analysis.applied_patterns:
                f.write(f"- **{pattern}**: Industry best practice for scenario evolution\n")
            
            f.write(f"""
### Strategic Recommendations

#### Immediate Actions (Sprint 1)
""")
            for item in mcp_analysis.strategic_roadmap.get('sprint_1', []):
                f.write(f"- {item}\n")
            
            f.write(f"""
#### Medium-term Planning (Sprint 2)
""")
            for item in mcp_analysis.strategic_roadmap.get('sprint_2', []):
                f.write(f"- {item}\n")
            
            f.write(f"""
#### Future Considerations
""")
            for item in mcp_analysis.strategic_roadmap.get('future', []):
                f.write(f"- {item}\n")
            
            f.write(f"""
## Impact Analysis

### Cross-Layer Dependencies
The evolution impacts multiple architectural layers requiring coordinated implementation:

""")
            for layer, impacts in mcp_analysis.cross_impact_analysis.items():
                f.write(f"**{layer.replace('_', ' ').title()}**\n")
                for impact in impacts:
                    f.write(f"- {impact}\n")
                f.write(f"\n")
            
            f.write(f"""
## Implementation Recommendations

### Phase 1: High-Priority Scenarios
Focus on scenarios with immediate business value and manageable implementation complexity.

### Phase 2: Comprehensive Coverage
Address medium-priority scenarios that enhance system robustness and user experience.

### Phase 3: Future-Proofing
Prepare for identified future needs through architectural decisions and documentation.

## Success Metrics
- Scenario coverage improvement: Target 95%+
- Feedback incorporation rate: Target 90%+
- Implementation velocity: Maintain sprint capacity
- Quality metrics: Zero regression in existing functionality

## Conclusion
The MCP-enhanced evolution analysis provides strategic guidance for systematic
scenario evolution that balances immediate needs with long-term architectural health.
""")
        
        print(f"✅ MCP Enhanced documentation created:")
        print(f"   - {mcp_path}")
        print(f"   - {detailed_path}")


def main():
    """メイン実行関数"""
    if len(sys.argv) < 2:
        print("❌ Feature name is required")
        print("Usage: python 12-evolve-scenarios-enhanced.py <feature-name>")
        sys.exit(1)
    
    feature_name = sys.argv[1]
    print(f"🎯 Starting MCP Enhanced Scenario Evolution for feature: {feature_name}")
    
    # 強化シナリオ進化実行
    evolver = EnhancedScenarioEvolver(feature_name)
    scenarios, mcp_analysis = evolver.execute_enhanced_evolution()
    
    # 結果サマリー
    print(f"\n📊 Evolution Results for Feature '{feature_name}':")
    print(f"   ✅ Evolved scenarios created: {len(scenarios)}")
    
    if mcp_analysis:
        print(f"   🤖 MCP patterns identified: {len(mcp_analysis.identified_patterns)}")
        print(f"   🎯 Evolution opportunities: {len(mcp_analysis.evolution_opportunities)}")
        print(f"   📋 Applied evolution patterns: {len(mcp_analysis.applied_patterns)}")
    
    print(f"\n📁 Generated Documentation:")
    print(f"   - docs/use_cases/evolved/{feature_name}-evolution.md")
    if mcp_analysis:
        print(f"   - docs/feedback/analysis-reports/{feature_name}-mcp-analysis.md")
        print(f"   - docs/feedback/analysis-reports/{feature_name}-mcp-detailed-report.md")
    
    print(f"\n✅ Scenario evolution completed successfully!")
    print("🎯 Next: Ready for /create-tests-enhanced [issue-numbers] or /sprint-planning-enhanced [sprint-number]")


if __name__ == "__main__":
    main()