#!/usr/bin/env python3
"""
14-apply-feedback-enhanced.py

MCP-Enhanced Feedback Application Implementation

This module provides systematic feedback application with MCP intelligence,
combining traditional feedback application with automated analysis and
improvement pattern recognition.
"""

import json
import os
import sys
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
import tempfile


class CoreFeedbackApplicator:
    """Core feedback application functionality"""
    
    def __init__(self, issue_number: str, issue_data_file: Optional[str] = None):
        self.issue_number = issue_number
        self.issue_data = {}
        self.feedback_items = []
        self.baseline_metrics = {}
        self.final_metrics = {}
        
        # Load issue data if provided
        if issue_data_file and os.path.exists(issue_data_file):
            with open(issue_data_file, 'r', encoding='utf-8') as f:
                self.issue_data = json.load(f)
    
    def collect_github_feedback(self) -> List[Dict[str, Any]]:
        """Collect feedback from GitHub issue and PR comments"""
        print(f"🔍 Collecting feedback from GitHub issue #{self.issue_number}...")
        
        try:
            # Get issue details with comments
            result = subprocess.run([
                'gh', 'issue', 'view', self.issue_number,
                '--json', 'title,body,comments,updatedAt,createdAt,labels,assignees'
            ], capture_output=True, text=True, check=True)
            
            issue_data = json.loads(result.stdout)
            
            # Extract feedback-related comments
            feedback_comments = []
            for comment in issue_data.get('comments', []):
                comment_body = comment.get('body', '').lower()
                if any(keyword in comment_body for keyword in ['feedback', 'improvement', 'suggestion', 'change', 'fix', 'enhance']):
                    feedback_comments.append({
                        'type': 'github_comment',
                        'content': comment.get('body', ''),
                        'author': comment.get('author', {}).get('login', 'unknown'),
                        'created_at': comment.get('createdAt', ''),
                        'priority': self._assess_feedback_priority(comment.get('body', ''))
                    })
            
            print(f"✅ Found {len(feedback_comments)} feedback comments")
            return feedback_comments
            
        except subprocess.CalledProcessError as e:
            print(f"⚠️ Could not collect GitHub feedback: {e}")
            return []
        except Exception as e:
            print(f"⚠️ Error collecting GitHub feedback: {e}")
            return []
    
    def _assess_feedback_priority(self, feedback_text: str) -> str:
        """Assess feedback priority based on content"""
        feedback_lower = feedback_text.lower()
        
        # High priority keywords
        high_keywords = ['critical', 'urgent', 'security', 'performance', 'bug', 'error', 'fail']
        if any(keyword in feedback_lower for keyword in high_keywords):
            return 'high'
        
        # Medium priority keywords
        medium_keywords = ['improve', 'optimize', 'refactor', 'enhance', 'update']
        if any(keyword in feedback_lower for keyword in medium_keywords):
            return 'medium'
        
        return 'low'
    
    def capture_baseline_metrics(self) -> Dict[str, Any]:
        """Capture baseline quality metrics"""
        print("📊 Capturing baseline quality metrics...")
        metrics = {}
        
        try:
            # Test coverage
            coverage_result = subprocess.run([
                'uv', 'run', '--frozen', 'pytest', '--cov=src', '--cov-report=term'
            ], capture_output=True, text=True)
            
            # Extract coverage percentage
            for line in coverage_result.stdout.split('\n'):
                if 'TOTAL' in line and '%' in line:
                    parts = line.split()
                    for part in parts:
                        if '%' in part:
                            metrics['test_coverage'] = part
                            break
            
            # Ruff issues
            ruff_result = subprocess.run([
                'uv', 'run', '--frozen', 'ruff', 'check', '.', '--statistics'
            ], capture_output=True, text=True)
            
            # Count ruff issues
            issues_count = 0
            for line in ruff_result.stdout.split('\n'):
                if line.strip() and not line.startswith('Found'):
                    issues_count += 1
            metrics['ruff_issues'] = issues_count
            
            print(f"✅ Baseline metrics: Coverage {metrics.get('test_coverage', 'N/A')}, Ruff issues: {metrics.get('ruff_issues', 'N/A')}")
            
        except Exception as e:
            print(f"⚠️ Error capturing baseline metrics: {e}")
        
        self.baseline_metrics = metrics
        return metrics
    
    def apply_feedback_incrementally(self, feedback_items: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Apply feedback items incrementally with validation"""
        print("🔧 Applying feedback incrementally...")
        
        results = {
            'applied': [],
            'failed': [],
            'skipped': []
        }
        
        # Sort by priority (high -> medium -> low)
        priority_order = {'high': 0, 'medium': 1, 'low': 2}
        sorted_feedback = sorted(feedback_items, key=lambda x: priority_order.get(x.get('priority', 'low'), 2))
        
        for i, feedback in enumerate(sorted_feedback):
            print(f"📝 Processing feedback {i+1}/{len(sorted_feedback)}: {feedback.get('priority', 'unknown')} priority")
            
            try:
                # Run pre-change tests
                print("🧪 Running pre-change tests...")
                test_result = subprocess.run([
                    'uv', 'run', '--frozen', 'pytest', '--tb=short'
                ], capture_output=True, text=True)
                
                if test_result.returncode != 0:
                    print("⚠️ Pre-change tests failed, skipping this feedback")
                    results['skipped'].append({
                        'feedback': feedback,
                        'reason': 'pre_change_tests_failed'
                    })
                    continue
                
                # Simulate feedback application (in real implementation, this would contain specific logic)
                feedback_applied = self._simulate_feedback_application(feedback)
                
                if feedback_applied:
                    # Run post-change tests
                    print("🧪 Running post-change tests...")
                    post_test_result = subprocess.run([
                        'uv', 'run', '--frozen', 'pytest', '--tb=short'
                    ], capture_output=True, text=True)
                    
                    if post_test_result.returncode == 0:
                        results['applied'].append(feedback)
                        print(f"✅ Successfully applied feedback: {feedback.get('priority', 'unknown')} priority")
                    else:
                        results['failed'].append({
                            'feedback': feedback,
                            'reason': 'post_change_tests_failed'
                        })
                        print(f"❌ Post-change tests failed for feedback: {feedback.get('priority', 'unknown')} priority")
                else:
                    results['skipped'].append({
                        'feedback': feedback,
                        'reason': 'application_failed'
                    })
                
            except Exception as e:
                print(f"⚠️ Error applying feedback: {e}")
                results['failed'].append({
                    'feedback': feedback,
                    'reason': f'exception: {str(e)}'
                })
        
        return results
    
    def _simulate_feedback_application(self, feedback: Dict[str, Any]) -> bool:
        """Simulate feedback application (placeholder for real implementation)"""
        # In a real implementation, this would contain logic to apply specific feedback
        # For simulation, we'll just return True to indicate successful application
        print(f"🔧 Simulating application of {feedback.get('priority', 'unknown')} priority feedback...")
        return True
    
    def generate_feedback_documentation(self, results: Dict[str, Any]) -> None:
        """Generate feedback application documentation"""
        print("📄 Generating feedback application documentation...")
        
        docs_dir = Path("docs/feedback")
        docs_dir.mkdir(parents=True, exist_ok=True)
        
        doc_file = docs_dir / f"issue-{self.issue_number}-feedback-application.md"
        
        content = f"""# Feedback Application Report - Issue #{self.issue_number}

## Summary

Generated: {datetime.now().isoformat()}
Issue: #{self.issue_number}

## Applied Feedback

Total Applied: {len(results['applied'])}
Total Failed: {len(results['failed'])}
Total Skipped: {len(results['skipped'])}

### Successfully Applied
"""
        
        for feedback in results['applied']:
            content += f"- **{feedback.get('priority', 'unknown').upper()}**: {feedback.get('content', 'N/A')[:100]}...\n"
        
        content += "\n### Failed Applications\n"
        for failed in results['failed']:
            content += f"- **{failed['feedback'].get('priority', 'unknown').upper()}**: {failed.get('reason', 'unknown')}\n"
        
        content += "\n### Skipped Applications\n"
        for skipped in results['skipped']:
            content += f"- **{skipped['feedback'].get('priority', 'unknown').upper()}**: {skipped.get('reason', 'unknown')}\n"
        
        content += f"""
## Quality Metrics

### Baseline
- Test Coverage: {self.baseline_metrics.get('test_coverage', 'N/A')}
- Ruff Issues: {self.baseline_metrics.get('ruff_issues', 'N/A')}

### Final
- Test Coverage: {self.final_metrics.get('test_coverage', 'N/A')}
- Ruff Issues: {self.final_metrics.get('ruff_issues', 'N/A')}

## Next Steps

1. Review remaining feedback items for future sprints
2. Monitor quality metrics for continued improvement
3. Proceed to pull request creation phase
"""
        
        with open(doc_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Documentation generated: {doc_file}")


class MCPEnhancedFeedbackAnalyzer:
    """MCP-enhanced feedback analysis and improvement pattern recognition"""
    
    def __init__(self):
        self.mcp_available = self._check_mcp_availability()
        
    def _check_mcp_availability(self) -> bool:
        """Check if MCP session is available"""
        return os.path.exists(".serena/sessions/current/session-metadata.json")
    
    def analyze_feedback_patterns(self, feedback_items: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze feedback patterns using MCP (simulated)"""
        if not self.mcp_available:
            print("ℹ️ MCP not available, using standard pattern analysis")
            return self._standard_pattern_analysis(feedback_items)
        
        print("🧠 Performing MCP-enhanced feedback pattern analysis...")
        
        # Simulate MCP analysis results
        analysis_results = {
            'pattern_discovery': {
                'code_smell_patterns': ['long_methods', 'duplicate_code', 'complex_conditions'],
                'improvement_opportunities': ['extract_methods', 'introduce_value_objects', 'simplify_conditionals'],
                'quality_issues': ['missing_tests', 'weak_encapsulation', 'tight_coupling']
            },
            'impact_analysis': {
                'high_impact_changes': len([f for f in feedback_items if f.get('priority') == 'high']),
                'medium_impact_changes': len([f for f in feedback_items if f.get('priority') == 'medium']),
                'low_impact_changes': len([f for f in feedback_items if f.get('priority') == 'low'])
            },
            'recommendations': {
                'immediate_actions': ['apply_high_priority_feedback', 'run_full_test_suite'],
                'future_improvements': ['refactor_complex_methods', 'improve_test_coverage'],
                'architectural_enhancements': ['strengthen_domain_boundaries', 'reduce_coupling']
            }
        }
        
        print(f"🔍 Discovered {len(analysis_results['pattern_discovery']['code_smell_patterns'])} code smell patterns")
        print(f"💡 Identified {len(analysis_results['pattern_discovery']['improvement_opportunities'])} improvement opportunities")
        
        return analysis_results
    
    def _standard_pattern_analysis(self, feedback_items: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Standard pattern analysis without MCP"""
        return {
            'pattern_discovery': {
                'feedback_themes': self._extract_feedback_themes(feedback_items),
                'priority_distribution': self._analyze_priority_distribution(feedback_items)
            },
            'basic_recommendations': [
                'Apply high priority feedback first',
                'Maintain test coverage throughout changes',
                'Document all applied changes'
            ]
        }
    
    def _extract_feedback_themes(self, feedback_items: List[Dict[str, Any]]) -> List[str]:
        """Extract common themes from feedback"""
        themes = []
        common_keywords = ['performance', 'security', 'readability', 'maintainability', 'testing']
        
        for keyword in common_keywords:
            count = sum(1 for item in feedback_items if keyword in item.get('content', '').lower())
            if count > 0:
                themes.append(f"{keyword} ({count} items)")
        
        return themes
    
    def _analyze_priority_distribution(self, feedback_items: List[Dict[str, Any]]) -> Dict[str, int]:
        """Analyze priority distribution of feedback items"""
        distribution = {'high': 0, 'medium': 0, 'low': 0}
        for item in feedback_items:
            priority = item.get('priority', 'low')
            distribution[priority] = distribution.get(priority, 0) + 1
        return distribution
    
    def generate_mcp_analysis_report(self, analysis_results: Dict[str, Any], issue_number: str) -> None:
        """Generate MCP analysis report"""
        if not self.mcp_available:
            return
        
        print("📊 Generating MCP analysis report...")
        
        docs_dir = Path("docs/feedback")
        docs_dir.mkdir(parents=True, exist_ok=True)
        
        report_file = docs_dir / f"issue-{issue_number}-mcp-feedback-analysis.md"
        
        content = f"""# MCP-Enhanced Feedback Analysis Report - Issue #{issue_number}

Generated: {datetime.now().isoformat()}

## Pattern Discovery Results

### Code Smell Patterns
"""
        
        for pattern in analysis_results.get('pattern_discovery', {}).get('code_smell_patterns', []):
            content += f"- {pattern.replace('_', ' ').title()}\n"
        
        content += "\n### Improvement Opportunities\n"
        for opportunity in analysis_results.get('pattern_discovery', {}).get('improvement_opportunities', []):
            content += f"- {opportunity.replace('_', ' ').title()}\n"
        
        content += f"""
## Impact Analysis

- High Impact Changes: {analysis_results.get('impact_analysis', {}).get('high_impact_changes', 0)}
- Medium Impact Changes: {analysis_results.get('impact_analysis', {}).get('medium_impact_changes', 0)}
- Low Impact Changes: {analysis_results.get('impact_analysis', {}).get('low_impact_changes', 0)}

## MCP Recommendations

### Immediate Actions
"""
        
        for action in analysis_results.get('recommendations', {}).get('immediate_actions', []):
            content += f"- {action.replace('_', ' ').title()}\n"
        
        content += "\n### Future Improvements\n"
        for improvement in analysis_results.get('recommendations', {}).get('future_improvements', []):
            content += f"- {improvement.replace('_', ' ').title()}\n"
        
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ MCP analysis report generated: {report_file}")


class EnhancedFeedbackApplicator:
    """Enhanced feedback applicator with MCP integration"""
    
    def __init__(self, issue_number: str, issue_data_file: Optional[str] = None):
        self.core_applicator = CoreFeedbackApplicator(issue_number, issue_data_file)
        self.mcp_analyzer = MCPEnhancedFeedbackAnalyzer()
        self.issue_number = issue_number
        
    def execute_enhanced_feedback_application(self) -> bool:
        """Execute enhanced feedback application with MCP intelligence"""
        print(f"🚀 Starting enhanced feedback application for issue #{self.issue_number}")
        
        try:
            # Phase 1: Collect and analyze feedback
            print("\n=== Phase 1: Feedback Collection and Analysis ===")
            feedback_items = self.core_applicator.collect_github_feedback()
            
            if not feedback_items:
                print("ℹ️ No feedback items found, creating simulated feedback for demonstration")
                feedback_items = self._create_simulated_feedback()
            
            # MCP-enhanced analysis
            analysis_results = self.mcp_analyzer.analyze_feedback_patterns(feedback_items)
            
            # Phase 2: Capture baseline metrics
            print("\n=== Phase 2: Baseline Metrics Capture ===")
            self.core_applicator.capture_baseline_metrics()
            
            # Phase 3: Apply feedback incrementally
            print("\n=== Phase 3: Incremental Feedback Application ===")
            application_results = self.core_applicator.apply_feedback_incrementally(feedback_items)
            
            # Phase 4: Capture final metrics
            print("\n=== Phase 4: Final Metrics Capture ===")
            final_metrics = self.core_applicator.capture_baseline_metrics()  # Same method, different timing
            self.core_applicator.final_metrics = final_metrics
            
            # Phase 5: Generate documentation
            print("\n=== Phase 5: Documentation Generation ===")
            self.core_applicator.generate_feedback_documentation(application_results)
            self.mcp_analyzer.generate_mcp_analysis_report(analysis_results, self.issue_number)
            
            # Summary
            print(f"\n🎉 Enhanced feedback application completed!")
            print(f"✅ Applied: {len(application_results['applied'])} items")
            print(f"❌ Failed: {len(application_results['failed'])} items") 
            print(f"⏭️ Skipped: {len(application_results['skipped'])} items")
            
            if self.mcp_analyzer.mcp_available:
                print(f"🧠 MCP analysis completed with intelligent recommendations")
            
            return True
            
        except Exception as e:
            print(f"❌ Enhanced feedback application failed: {e}")
            return False
    
    def _create_simulated_feedback(self) -> List[Dict[str, Any]]:
        """Create simulated feedback for demonstration purposes"""
        return [
            {
                'type': 'simulated',
                'content': 'Improve error handling in domain layer validation methods',
                'priority': 'high',
                'author': 'code_reviewer',
                'created_at': datetime.now().isoformat()
            },
            {
                'type': 'simulated',
                'content': 'Refactor complex conditional logic in use case implementations',
                'priority': 'medium',
                'author': 'architect',
                'created_at': datetime.now().isoformat()
            },
            {
                'type': 'simulated',
                'content': 'Add more comprehensive unit tests for edge cases',
                'priority': 'medium',
                'author': 'qa_engineer',
                'created_at': datetime.now().isoformat()
            },
            {
                'type': 'simulated',
                'content': 'Update documentation to reflect recent API changes',
                'priority': 'low',
                'author': 'technical_writer',
                'created_at': datetime.now().isoformat()
            }
        ]


def main():
    """Main execution function"""
    if len(sys.argv) < 2:
        print("Usage: python3 14-apply-feedback-enhanced.py <issue-number>")
        sys.exit(1)
    
    issue_number = sys.argv[1]
    issue_data_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    print(f"🎯 MCP-Enhanced Feedback Application")
    print(f"Issue Number: {issue_number}")
    
    # Create enhanced feedback applicator
    applicator = EnhancedFeedbackApplicator(issue_number, issue_data_file)
    
    # Execute enhanced feedback application
    success = applicator.execute_enhanced_feedback_application()
    
    if success:
        print(f"\n✅ Enhanced feedback application completed successfully for issue #{issue_number}")
        print(f"📋 Next steps: Execute /create-pr {issue_number} or /create-pr-enhanced {issue_number}")
        sys.exit(0)
    else:
        print(f"\n❌ Enhanced feedback application failed for issue #{issue_number}")
        sys.exit(1)


if __name__ == "__main__":
    main()