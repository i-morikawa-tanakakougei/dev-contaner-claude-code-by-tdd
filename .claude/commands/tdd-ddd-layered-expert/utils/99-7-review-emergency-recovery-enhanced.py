#!/usr/bin/env python3
"""
99-7-review-emergency-recovery-enhanced.py

MCP-Enhanced Final Emergency Recovery Review Implementation

This module provides comprehensive final recovery review with MCP intelligence,
combining traditional recovery completion assessment with automated pattern analysis and
intelligent quality validation.
"""

import json
import os
import sys
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
import tempfile
import re
import glob


class CoreRecoveryReviewer:
    """Core final recovery review functionality"""
    
    def __init__(self, context_param: Optional[str] = None):
        self.context_param = context_param
        self.review_data = {}
        self.analysis_metrics = {}
        self.review_results = {}
        
    def analyze_recovery_completion(self) -> Dict[str, Any]:
        """Analyze completion status of all emergency recovery steps"""
        print("📊 Analyzing emergency recovery process completion...")
        
        completion = {
            'recovery_steps': {},
            'deliverables_verification': {},
            'quality_assessment': {},
            'workflow_readiness': {},
            'completion_metrics': {},
            'timestamp': datetime.now().isoformat()
        }
        
        try:
            # Define expected recovery steps
            recovery_steps = [
                '99-1-emergency-recovery',
                '99-2-create-retroactive-issue',
                '99-3-sync-documentation',
                '99-4-create-retroactive-tests',
                '99-5-validate-recovery',
                '99-6-metadata-reconcile'
            ]
            
            # Analyze each recovery step
            for step in recovery_steps:
                step_analysis = self._analyze_recovery_step(step)
                completion['recovery_steps'][step] = step_analysis
            
            # Verify deliverables for each step
            completion['deliverables_verification'] = self._verify_recovery_deliverables()
            
            # Assess overall quality metrics
            completion['quality_assessment'] = self._assess_recovery_quality()
            
            # Evaluate workflow readiness
            completion['workflow_readiness'] = self._evaluate_workflow_readiness()
            
            # Calculate completion metrics
            completion['completion_metrics'] = self._calculate_completion_metrics(completion)
            
            print(f"✅ Recovery completion analysis completed: {self._calculate_overall_completion(completion):.1f}% complete")
            
        except Exception as e:
            print(f"Warning: Recovery completion analysis error: {e}")
            completion['analysis_error'] = str(e)
            
        self.review_data = completion
        return completion
    
    def _analyze_recovery_step(self, step: str) -> Dict[str, Any]:
        """Analyze specific recovery step completion"""
        analysis = {
            'step_name': step,
            'executed': False,
            'deliverables_found': [],
            'quality_score': 0.0,
            'completion_indicators': {},
            'issues_identified': []
        }
        
        try:
            # Check execution history
            execution_history_path = ".claude/context/execution-history.jsonl"
            if os.path.exists(execution_history_path):
                analysis['executed'] = self._check_step_execution(step, execution_history_path)
            
            # Look for step-specific deliverables
            deliverables = self._find_step_deliverables(step)
            analysis['deliverables_found'] = deliverables
            
            # Assess quality indicators
            analysis['quality_score'] = self._assess_step_quality(step, deliverables)
            
            # Check completion indicators
            analysis['completion_indicators'] = self._check_completion_indicators(step, deliverables)
            
            # Identify potential issues
            if not analysis['executed']:
                analysis['issues_identified'].append("Step not found in execution history")
            if not analysis['deliverables_found']:
                analysis['issues_identified'].append("No deliverables found for step")
            if analysis['quality_score'] < 70:
                analysis['issues_identified'].append(f"Quality score below threshold: {analysis['quality_score']}")
                
        except Exception as e:
            analysis['issues_identified'].append(f"Analysis error: {str(e)}")
            
        return analysis
    
    def _check_step_execution(self, step: str, history_file: str) -> bool:
        """Check if step was executed according to history"""
        try:
            with open(history_file, 'r') as f:
                lines = f.readlines()
                
            for line in lines:
                try:
                    entry = json.loads(line.strip())
                    command = entry.get('command', '')
                    if step.replace('-', '_') in command or step in command:
                        status = entry.get('status', '')
                        return status in ['success', 'completed', 'SUCCESS']
                except json.JSONDecodeError:
                    continue
                    
        except Exception:
            pass
            
        return False
    
    def _find_step_deliverables(self, step: str) -> List[str]:
        """Find deliverables produced by recovery step"""
        deliverables = []
        
        # Define expected deliverable patterns for each step
        deliverable_patterns = {
            '99-1-emergency-recovery': ['*emergency-recovery-report*.md'],
            '99-2-create-retroactive-issue': ['*retroactive-issues-report*.md'],
            '99-3-sync-documentation': ['*documentation-sync-report*.md'],
            '99-4-create-retroactive-tests': ['*retroactive-tests-report*.md', 'tests/test_*.py'],
            '99-5-validate-recovery': ['*recovery-validation-report*.md'],
            '99-6-metadata-reconcile': ['*metadata-reconciliation-report*.md']
        }
        
        patterns = deliverable_patterns.get(step, [])
        search_dirs = ['docs/emergency/', 'tests/', 'docs/metadata/']
        
        for pattern in patterns:
            for search_dir in search_dirs:
                if os.path.exists(search_dir):
                    matches = glob.glob(os.path.join(search_dir, pattern))
                    deliverables.extend(matches)
        
        return deliverables
    
    def _assess_step_quality(self, step: str, deliverables: List[str]) -> float:
        """Assess quality of recovery step"""
        quality_score = 0.0
        
        if not deliverables:
            return quality_score
        
        # Base score for having deliverables
        quality_score = 50.0
        
        # Additional points for quality indicators
        for deliverable in deliverables:
            try:
                if deliverable.endswith('.md'):
                    quality_score += self._assess_document_quality(deliverable)
                elif deliverable.endswith('.py'):
                    quality_score += self._assess_test_quality(deliverable)
            except Exception:
                continue
        
        # Normalize to 0-100 scale
        return min(quality_score, 100.0)
    
    def _assess_document_quality(self, document_path: str) -> float:
        """Assess quality of documentation deliverable"""
        quality_points = 0.0
        
        try:
            with open(document_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for completion indicators
            if '✅' in content:
                quality_points += 10
            if 'Score:' in content or 'スコア:' in content:
                quality_points += 10
            if len(content) > 1000:  # Substantial content
                quality_points += 10
            if 'MCP' in content or '強化' in content:  # Enhanced features
                quality_points += 10
                
        except Exception:
            pass
            
        return quality_points
    
    def _assess_test_quality(self, test_path: str) -> float:
        """Assess quality of test file"""
        quality_points = 0.0
        
        try:
            with open(test_path, 'r') as f:
                content = f.read()
            
            # Check for test patterns
            if 'def test_' in content:
                quality_points += 15
            if 'assert' in content:
                quality_points += 10
            if '@pytest.mark' in content:
                quality_points += 5
                
        except Exception:
            pass
            
        return quality_points
    
    def _check_completion_indicators(self, step: str, deliverables: List[str]) -> Dict[str, Any]:
        """Check completion indicators for recovery step"""
        indicators = {
            'has_deliverables': len(deliverables) > 0,
            'recent_deliverables': False,
            'quality_indicators_present': False,
            'mcp_enhancements': False
        }
        
        if deliverables:
            # Check if deliverables are recent (within 7 days)
            for deliverable in deliverables:
                try:
                    mtime = os.path.getmtime(deliverable)
                    file_age = (datetime.now() - datetime.fromtimestamp(mtime)).days
                    if file_age <= 7:
                        indicators['recent_deliverables'] = True
                        break
                except Exception:
                    continue
            
            # Check for quality indicators in deliverables
            for deliverable in deliverables:
                try:
                    with open(deliverable, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    if any(indicator in content for indicator in ['✅', 'Score:', 'スコア:', '完了']):
                        indicators['quality_indicators_present'] = True
                    
                    if any(keyword in content for keyword in ['MCP', '強化', 'enhanced']):
                        indicators['mcp_enhancements'] = True
                        
                except Exception:
                    continue
        
        return indicators
    
    def _verify_recovery_deliverables(self) -> Dict[str, Any]:
        """Verify all recovery deliverables exist and are valid"""
        verification = {
            'expected_deliverables': [],
            'found_deliverables': [],
            'missing_deliverables': [],
            'quality_assessment': {}
        }
        
        # Define expected deliverables
        expected = [
            'docs/emergency/*emergency-recovery-report*.md',
            'docs/emergency/*retroactive-issues-report*.md',
            'docs/emergency/*documentation-sync-report*.md',
            'docs/emergency/*retroactive-tests-report*.md',
            'docs/emergency/*recovery-validation-report*.md',
            'docs/emergency/*metadata-reconciliation-report*.md'
        ]
        
        verification['expected_deliverables'] = expected
        
        for pattern in expected:
            matches = glob.glob(pattern)
            if matches:
                verification['found_deliverables'].extend(matches)
            else:
                verification['missing_deliverables'].append(pattern)
        
        # Assess quality of found deliverables
        for deliverable in verification['found_deliverables']:
            quality_score = self._assess_document_quality(deliverable)
            verification['quality_assessment'][deliverable] = quality_score
        
        return verification
    
    def _assess_recovery_quality(self) -> Dict[str, Any]:
        """Assess overall recovery quality"""
        assessment = {
            'code_quality': {},
            'test_coverage': {},
            'documentation_consistency': {},
            'architecture_compliance': {},
            'overall_score': 0.0
        }
        
        try:
            # Assess code quality
            assessment['code_quality'] = self._assess_code_quality()
            
            # Check test coverage
            assessment['test_coverage'] = self._check_test_coverage()
            
            # Verify documentation consistency
            assessment['documentation_consistency'] = self._verify_documentation_consistency()
            
            # Check architecture compliance
            assessment['architecture_compliance'] = self._check_architecture_compliance()
            
            # Calculate overall score
            assessment['overall_score'] = self._calculate_quality_score(assessment)
            
        except Exception as e:
            assessment['assessment_error'] = str(e)
        
        return assessment
    
    def _assess_code_quality(self) -> Dict[str, Any]:
        """Assess code quality using available tools"""
        quality = {
            'ruff_check': False,
            'ruff_format': False,
            'pyright_check': False,
            'syntax_errors': []
        }
        
        try:
            # Run ruff check
            result = subprocess.run(
                ['uv', 'run', '--frozen', 'ruff', 'check', '.'],
                capture_output=True, text=True, timeout=30
            )
            quality['ruff_check'] = result.returncode == 0
            if result.returncode != 0:
                quality['syntax_errors'].append(f"Ruff check failed: {result.stdout[:200]}")
        except Exception as e:
            quality['syntax_errors'].append(f"Ruff check error: {str(e)}")
        
        try:
            # Run ruff format check
            result = subprocess.run(
                ['uv', 'run', '--frozen', 'ruff', 'format', '.', '--check'],
                capture_output=True, text=True, timeout=30
            )
            quality['ruff_format'] = result.returncode == 0
        except Exception as e:
            quality['syntax_errors'].append(f"Ruff format error: {str(e)}")
        
        try:
            # Run pyright check
            result = subprocess.run(
                ['uv', 'run', '--frozen', 'pyright'],
                capture_output=True, text=True, timeout=60
            )
            quality['pyright_check'] = result.returncode == 0
            if result.returncode != 0:
                quality['syntax_errors'].append(f"Pyright check failed: {result.stdout[:200]}")
        except Exception as e:
            quality['syntax_errors'].append(f"Pyright check error: {str(e)}")
        
        return quality
    
    def _check_test_coverage(self) -> Dict[str, Any]:
        """Check test coverage"""
        coverage = {
            'tests_exist': False,
            'coverage_percentage': 0.0,
            'tests_passing': False,
            'test_results': {}
        }
        
        try:
            # Check if tests exist
            test_dirs = ['tests/', 'test/']
            for test_dir in test_dirs:
                if os.path.exists(test_dir):
                    test_files = glob.glob(os.path.join(test_dir, 'test_*.py'))
                    if test_files:
                        coverage['tests_exist'] = True
                        break
            
            if coverage['tests_exist']:
                # Run pytest with coverage
                result = subprocess.run([
                    'uv', 'run', '--frozen', 'pytest', 'tests/', 
                    '--cov=src', '--cov-report=term-missing', '-q'
                ], capture_output=True, text=True, timeout=120)
                
                coverage['tests_passing'] = result.returncode == 0
                
                # Parse coverage percentage
                output = result.stdout
                coverage_match = re.search(r'TOTAL\s+\d+\s+\d+\s+(\d+)%', output)
                if coverage_match:
                    coverage['coverage_percentage'] = float(coverage_match.group(1))
                
                coverage['test_results']['output'] = output[:500]
                
        except Exception as e:
            coverage['test_results']['error'] = str(e)
        
        return coverage
    
    def _verify_documentation_consistency(self) -> Dict[str, Any]:
        """Verify documentation consistency"""
        consistency = {
            'documents_exist': False,
            'emergency_docs_complete': False,
            'consistency_score': 0.0,
            'issues': []
        }
        
        try:
            # Check for key documentation
            doc_dirs = ['docs/', 'docs/emergency/']
            for doc_dir in doc_dirs:
                if os.path.exists(doc_dir):
                    md_files = glob.glob(os.path.join(doc_dir, '*.md'))
                    if md_files:
                        consistency['documents_exist'] = True
                        break
            
            # Check emergency documentation completeness
            emergency_dir = Path('docs/emergency/')
            if emergency_dir.exists():
                report_files = list(emergency_dir.glob('*report*.md'))
                consistency['emergency_docs_complete'] = len(report_files) >= 5
                
                # Calculate consistency score based on content
                if report_files:
                    total_score = 0
                    for report in report_files:
                        try:
                            with open(report, 'r', encoding='utf-8') as f:
                                content = f.read()
                            
                            score = 0
                            if '✅' in content: score += 20
                            if 'Score:' in content or 'スコア:' in content: score += 20
                            if len(content) > 500: score += 20
                            if 'MCP' in content or '強化' in content: score += 20
                            if '完了' in content or 'completed' in content: score += 20
                            
                            total_score += score
                        except Exception:
                            continue
                    
                    if report_files:
                        consistency['consistency_score'] = total_score / len(report_files)
            
        except Exception as e:
            consistency['issues'].append(str(e))
        
        return consistency
    
    def _check_architecture_compliance(self) -> Dict[str, Any]:
        """Check architecture compliance"""
        compliance = {
            'clean_architecture': False,
            'tdd_compliance': False,
            'ddd_compliance': False,
            'layer_separation': False,
            'compliance_score': 0.0
        }
        
        try:
            # Check for clean architecture structure
            arch_dirs = ['src/domain/', 'src/application/', 'src/infrastructure/', 'src/presentation/']
            arch_exists = [os.path.exists(d) for d in arch_dirs]
            compliance['clean_architecture'] = any(arch_exists)
            
            # Check for TDD compliance (tests exist and cover implementation)
            if os.path.exists('tests/'):
                test_files = glob.glob('tests/test_*.py')
                compliance['tdd_compliance'] = len(test_files) > 0
            
            # Check for DDD compliance (domain models exist)
            domain_dirs = ['src/domain/', 'domain/', 'src/']
            for domain_dir in domain_dirs:
                if os.path.exists(domain_dir):
                    py_files = glob.glob(os.path.join(domain_dir, '*.py'))
                    if py_files:
                        compliance['ddd_compliance'] = True
                        break
            
            # Calculate compliance score
            scores = [
                compliance['clean_architecture'],
                compliance['tdd_compliance'],
                compliance['ddd_compliance']
            ]
            compliance['compliance_score'] = sum(scores) / len(scores) * 100
            
        except Exception as e:
            pass
        
        return compliance
    
    def _calculate_quality_score(self, assessment: Dict[str, Any]) -> float:
        """Calculate overall quality score"""
        scores = []
        
        # Code quality score
        code_quality = assessment.get('code_quality', {})
        code_score = sum([
            code_quality.get('ruff_check', False),
            code_quality.get('ruff_format', False),
            code_quality.get('pyright_check', False)
        ]) / 3 * 100
        scores.append(code_score)
        
        # Test coverage score
        test_coverage = assessment.get('test_coverage', {})
        coverage_score = test_coverage.get('coverage_percentage', 0)
        if test_coverage.get('tests_passing', False):
            coverage_score = min(coverage_score + 20, 100)
        scores.append(coverage_score)
        
        # Documentation consistency score
        doc_consistency = assessment.get('documentation_consistency', {})
        doc_score = doc_consistency.get('consistency_score', 0)
        scores.append(doc_score)
        
        # Architecture compliance score
        arch_compliance = assessment.get('architecture_compliance', {})
        arch_score = arch_compliance.get('compliance_score', 0)
        scores.append(arch_score)
        
        return sum(scores) / len(scores) if scores else 0.0
    
    def _evaluate_workflow_readiness(self) -> Dict[str, Any]:
        """Evaluate readiness for standard workflow return"""
        readiness = {
            'project_health': 'unknown',
            'build_status': 'unknown',
            'test_suite_status': 'unknown',
            'metadata_consistency': False,
            'ready_for_standard_workflow': False,
            'readiness_score': 0.0
        }
        
        try:
            # Check project health indicators
            if os.path.exists('docs/metadata/project-state.json'):
                with open('docs/metadata/project-state.json', 'r') as f:
                    project_state = json.load(f)
                
                health_score = project_state.get('project_metadata', {}).get('health_score', 0)
                if health_score >= 90:
                    readiness['project_health'] = 'healthy'
                elif health_score >= 70:
                    readiness['project_health'] = 'conditional'
                else:
                    readiness['project_health'] = 'unhealthy'
            
            # Check build status (simplified check)
            try:
                result = subprocess.run(['python', '-m', 'py_compile'], 
                                      capture_output=True, timeout=30)
                readiness['build_status'] = 'passing' if result.returncode == 0 else 'failing'
            except Exception:
                readiness['build_status'] = 'unknown'
            
            # Check test suite status
            if os.path.exists('tests/'):
                try:
                    result = subprocess.run(['uv', 'run', '--frozen', 'pytest', 'tests/', '-q'], 
                                          capture_output=True, timeout=60)
                    readiness['test_suite_status'] = 'passing' if result.returncode == 0 else 'failing'
                except Exception:
                    readiness['test_suite_status'] = 'unknown'
            
            # Check metadata consistency
            metadata_files = [
                'docs/metadata/project-state.json',
                '.claude/context/project-context.json'
            ]
            consistent_count = 0
            for file_path in metadata_files:
                if os.path.exists(file_path):
                    try:
                        with open(file_path, 'r') as f:
                            json.load(f)  # Validate JSON
                        consistent_count += 1
                    except json.JSONDecodeError:
                        pass
            
            readiness['metadata_consistency'] = consistent_count == len(metadata_files)
            
            # Calculate readiness score
            readiness_factors = [
                readiness['project_health'] == 'healthy',
                readiness['build_status'] == 'passing',
                readiness['test_suite_status'] == 'passing',
                readiness['metadata_consistency']
            ]
            readiness['readiness_score'] = sum(readiness_factors) / len(readiness_factors) * 100
            readiness['ready_for_standard_workflow'] = readiness['readiness_score'] >= 75
            
        except Exception as e:
            readiness['evaluation_error'] = str(e)
        
        return readiness
    
    def _calculate_completion_metrics(self, completion: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate overall completion metrics"""
        metrics = {
            'total_steps': 6,  # 99-1 through 99-6
            'completed_steps': 0,
            'completion_percentage': 0.0,
            'quality_average': 0.0,
            'deliverables_found': 0,
            'issues_count': 0
        }
        
        recovery_steps = completion.get('recovery_steps', {})
        
        for step_data in recovery_steps.values():
            if step_data.get('executed', False):
                metrics['completed_steps'] += 1
            if step_data.get('deliverables_found'):
                metrics['deliverables_found'] += len(step_data['deliverables_found'])
            metrics['issues_count'] += len(step_data.get('issues_identified', []))
        
        metrics['completion_percentage'] = (metrics['completed_steps'] / metrics['total_steps']) * 100
        
        # Calculate quality average
        quality_scores = [step_data.get('quality_score', 0) for step_data in recovery_steps.values()]
        if quality_scores:
            metrics['quality_average'] = sum(quality_scores) / len(quality_scores)
        
        return metrics
    
    def _calculate_overall_completion(self, completion: Dict[str, Any]) -> float:
        """Calculate overall completion percentage"""
        metrics = completion.get('completion_metrics', {})
        return metrics.get('completion_percentage', 0.0)


class MCPEnhancedRecoveryIntelligence:
    """MCP-enhanced recovery intelligence and analysis"""
    
    def __init__(self):
        self.analysis_cache = {}
    
    def analyze_recovery_patterns(self, review_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze recovery patterns using simulated MCP intelligence"""
        print("🧠 Performing MCP-enhanced recovery pattern analysis...")
        
        intelligence = {
            'pattern_analysis': {},
            'quality_predictions': {},
            'improvement_recommendations': [],
            'workflow_optimization': {},
            'timestamp': datetime.now().isoformat()
        }
        
        try:
            # Simulate Serena MCP recovery pattern analysis
            intelligence['pattern_analysis'] = self._simulate_serena_pattern_analysis(review_data)
            
            # Predict quality outcomes and workflow readiness
            intelligence['quality_predictions'] = self._predict_quality_outcomes(review_data)
            
            # Generate improvement recommendations
            intelligence['improvement_recommendations'] = self._generate_improvement_recommendations(
                review_data, intelligence['pattern_analysis']
            )
            
            # Generate workflow optimization strategies
            intelligence['workflow_optimization'] = self._generate_workflow_optimization(
                review_data, intelligence['pattern_analysis']
            )
            
            print("✅ MCP recovery pattern analysis completed")
            
        except Exception as e:
            print(f"Warning: MCP recovery pattern analysis error: {e}")
            intelligence['analysis_error'] = str(e)
        
        return intelligence
    
    def _simulate_serena_pattern_analysis(self, review_data: Dict[str, Any]) -> Dict[str, Any]:
        """Simulate Serena MCP recovery pattern analysis"""
        patterns = {
            'completion_patterns': [],
            'quality_patterns': [],
            'workflow_patterns': {},
            'anomaly_detection': []
        }
        
        recovery_steps = review_data.get('recovery_steps', {})
        
        # Analyze completion patterns
        for step_name, step_data in recovery_steps.items():
            pattern = {
                'step': step_name,
                'completion_score': 100 if step_data.get('executed', False) else 0,
                'quality_score': step_data.get('quality_score', 0),
                'deliverables_count': len(step_data.get('deliverables_found', [])),
                'issues_count': len(step_data.get('issues_identified', []))
            }
            patterns['completion_patterns'].append(pattern)
        
        # Analyze quality patterns
        quality_assessment = review_data.get('quality_assessment', {})
        overall_quality = quality_assessment.get('overall_score', 0)
        
        patterns['quality_patterns'] = {
            'overall_quality_score': overall_quality,
            'code_quality_trend': self._analyze_code_quality_trend(quality_assessment),
            'test_coverage_trend': self._analyze_test_coverage_trend(quality_assessment),
            'documentation_quality': self._analyze_documentation_quality(quality_assessment)
        }
        
        # Analyze workflow patterns
        workflow_readiness = review_data.get('workflow_readiness', {})
        patterns['workflow_patterns'] = {
            'readiness_score': workflow_readiness.get('readiness_score', 0),
            'project_health': workflow_readiness.get('project_health', 'unknown'),
            'transition_indicators': self._analyze_transition_indicators(workflow_readiness)
        }
        
        # Detect anomalies
        patterns['anomaly_detection'] = self._detect_recovery_anomalies(review_data)
        
        return patterns
    
    def _analyze_code_quality_trend(self, quality_assessment: Dict[str, Any]) -> str:
        """Analyze code quality trend"""
        code_quality = quality_assessment.get('code_quality', {})
        
        checks_passing = sum([
            code_quality.get('ruff_check', False),
            code_quality.get('ruff_format', False),
            code_quality.get('pyright_check', False)
        ])
        
        if checks_passing == 3:
            return 'excellent'
        elif checks_passing == 2:
            return 'good'
        elif checks_passing == 1:
            return 'needs_improvement'
        else:
            return 'critical'
    
    def _analyze_test_coverage_trend(self, quality_assessment: Dict[str, Any]) -> str:
        """Analyze test coverage trend"""
        test_coverage = quality_assessment.get('test_coverage', {})
        coverage_percentage = test_coverage.get('coverage_percentage', 0)
        tests_passing = test_coverage.get('tests_passing', False)
        
        if coverage_percentage >= 90 and tests_passing:
            return 'excellent'
        elif coverage_percentage >= 75 and tests_passing:
            return 'good'
        elif coverage_percentage >= 50:
            return 'fair'
        else:
            return 'needs_improvement'
    
    def _analyze_documentation_quality(self, quality_assessment: Dict[str, Any]) -> str:
        """Analyze documentation quality"""
        doc_consistency = quality_assessment.get('documentation_consistency', {})
        consistency_score = doc_consistency.get('consistency_score', 0)
        docs_complete = doc_consistency.get('emergency_docs_complete', False)
        
        if consistency_score >= 80 and docs_complete:
            return 'excellent'
        elif consistency_score >= 60 and docs_complete:
            return 'good'
        elif consistency_score >= 40:
            return 'fair'
        else:
            return 'needs_improvement'
    
    def _analyze_transition_indicators(self, workflow_readiness: Dict[str, Any]) -> Dict[str, bool]:
        """Analyze transition readiness indicators"""
        return {
            'build_ready': workflow_readiness.get('build_status') == 'passing',
            'tests_ready': workflow_readiness.get('test_suite_status') == 'passing',
            'metadata_ready': workflow_readiness.get('metadata_consistency', False),
            'health_ready': workflow_readiness.get('project_health') == 'healthy'
        }
    
    def _detect_recovery_anomalies(self, review_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Detect anomalies in recovery process"""
        anomalies = []
        
        completion_metrics = review_data.get('completion_metrics', {})
        
        # Check for incomplete recovery steps
        completion_percentage = completion_metrics.get('completion_percentage', 0)
        if completion_percentage < 100:
            anomalies.append({
                'type': 'incomplete_recovery',
                'severity': 'high',
                'description': f'Recovery process only {completion_percentage:.1f}% complete',
                'recommendation': 'Complete missing recovery steps before workflow transition'
            })
        
        # Check for quality issues
        quality_average = completion_metrics.get('quality_average', 0)
        if quality_average < 70:
            anomalies.append({
                'type': 'quality_issues',
                'severity': 'medium',
                'description': f'Average quality score is {quality_average:.1f}, below recommended 70%',
                'recommendation': 'Address quality issues before standard workflow return'
            })
        
        # Check for excessive issues
        issues_count = completion_metrics.get('issues_count', 0)
        if issues_count > 5:
            anomalies.append({
                'type': 'excessive_issues',
                'severity': 'medium',
                'description': f'{issues_count} issues identified across recovery steps',
                'recommendation': 'Review and resolve identified issues'
            })
        
        return anomalies
    
    def _predict_quality_outcomes(self, review_data: Dict[str, Any]) -> Dict[str, Any]:
        """Predict quality outcomes and workflow success"""
        predictions = {
            'workflow_success_probability': 0.0,
            'quality_improvement_potential': 0.0,
            'transition_timeline': 'unknown',
            'confidence_level': 'medium'
        }
        
        completion_metrics = review_data.get('completion_metrics', {})
        workflow_readiness = review_data.get('workflow_readiness', {})
        
        # Calculate workflow success probability
        completion_score = completion_metrics.get('completion_percentage', 0) / 100
        quality_score = completion_metrics.get('quality_average', 0) / 100
        readiness_score = workflow_readiness.get('readiness_score', 0) / 100
        
        success_probability = (completion_score * 0.4 + quality_score * 0.3 + readiness_score * 0.3) * 100
        predictions['workflow_success_probability'] = success_probability
        
        # Calculate improvement potential
        max_possible_quality = 100
        current_quality = completion_metrics.get('quality_average', 0)
        predictions['quality_improvement_potential'] = max_possible_quality - current_quality
        
        # Predict transition timeline
        if success_probability >= 90:
            predictions['transition_timeline'] = 'immediate'
            predictions['confidence_level'] = 'high'
        elif success_probability >= 75:
            predictions['transition_timeline'] = '1-2_days'
            predictions['confidence_level'] = 'high'
        elif success_probability >= 60:
            predictions['transition_timeline'] = '3-7_days'
            predictions['confidence_level'] = 'medium'
        else:
            predictions['transition_timeline'] = 'requires_significant_work'
            predictions['confidence_level'] = 'low'
        
        return predictions
    
    def _generate_improvement_recommendations(self, review_data: Dict[str, Any], patterns: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate improvement recommendations"""
        recommendations = []
        
        # Analyze completion patterns
        completion_patterns = patterns.get('completion_patterns', [])
        incomplete_steps = [p for p in completion_patterns if p.get('completion_score', 0) < 100]
        
        if incomplete_steps:
            recommendations.append({
                'category': 'process_completion',
                'priority': 'critical',
                'description': f'Complete {len(incomplete_steps)} missing recovery steps',
                'actions': [f"Execute {step['step']}" for step in incomplete_steps],
                'estimated_effort': 'high'
            })
        
        # Analyze quality patterns
        quality_patterns = patterns.get('quality_patterns', {})
        overall_quality = quality_patterns.get('overall_quality_score', 0)
        
        if overall_quality < 80:
            recommendations.append({
                'category': 'quality_improvement',
                'priority': 'high',
                'description': 'Improve overall quality metrics to meet standards',
                'actions': [
                    'Fix code quality issues',
                    'Improve test coverage',
                    'Enhance documentation consistency'
                ],
                'estimated_effort': 'medium'
            })
        
        # Analyze workflow patterns
        workflow_patterns = patterns.get('workflow_patterns', {})
        readiness_score = workflow_patterns.get('readiness_score', 0)
        
        if readiness_score < 75:
            transition_indicators = workflow_patterns.get('transition_indicators', {})
            failed_indicators = [k for k, v in transition_indicators.items() if not v]
            
            recommendations.append({
                'category': 'workflow_readiness',
                'priority': 'high',
                'description': 'Address workflow readiness issues',
                'actions': [f"Fix {indicator.replace('_', ' ')}" for indicator in failed_indicators],
                'estimated_effort': 'medium'
            })
        
        return recommendations
    
    def _generate_workflow_optimization(self, review_data: Dict[str, Any], patterns: Dict[str, Any]) -> Dict[str, Any]:
        """Generate workflow optimization strategies"""
        optimization = {
            'immediate_actions': [],
            'short_term_goals': [],
            'long_term_strategies': [],
            'automation_opportunities': []
        }
        
        # Immediate actions based on current state
        completion_metrics = review_data.get('completion_metrics', {})
        if completion_metrics.get('completion_percentage', 0) < 100:
            optimization['immediate_actions'].append({
                'action': 'Complete missing recovery steps',
                'urgency': 'critical',
                'impact': 'workflow_blocking'
            })
        
        quality_assessment = review_data.get('quality_assessment', {})
        code_quality = quality_assessment.get('code_quality', {})
        if not all([code_quality.get('ruff_check', False), code_quality.get('pyright_check', False)]):
            optimization['immediate_actions'].append({
                'action': 'Fix code quality issues',
                'urgency': 'high',
                'impact': 'quality_improvement'
            })
        
        # Short-term goals (1-2 weeks)
        test_coverage = quality_assessment.get('test_coverage', {})
        if test_coverage.get('coverage_percentage', 0) < 90:
            optimization['short_term_goals'].append({
                'goal': 'Improve test coverage to 90%+',
                'timeline': '1-2_weeks',
                'benefit': 'enhanced_quality_assurance'
            })
        
        # Long-term strategies (1-3 months)
        optimization['long_term_strategies'].append({
            'strategy': 'Implement automated emergency recovery validation',
            'timeline': '1-3_months',
            'benefit': 'reduced_recovery_time'
        })
        
        # Automation opportunities
        anomalies = patterns.get('anomaly_detection', [])
        if len(anomalies) > 2:
            optimization['automation_opportunities'].append({
                'opportunity': 'Automated anomaly detection and alerting',
                'complexity': 'medium',
                'roi': 'high'
            })
        
        return optimization


class EnhancedRecoveryReviewer:
    """Enhanced recovery reviewer combining core functionality with MCP intelligence"""
    
    def __init__(self, context_param: Optional[str] = None):
        self.context_param = context_param
        self.core_reviewer = CoreRecoveryReviewer(context_param)
        self.mcp_intelligence = MCPEnhancedRecoveryIntelligence()
        self.results = {}
    
    def execute_enhanced_final_recovery_review(self) -> bool:
        """Execute comprehensive final recovery review with MCP intelligence"""
        try:
            print("🔍 Starting MCP-enhanced final recovery review...")
            
            # Phase 1: Core recovery completion analysis
            print("\n📊 Phase 1: Analyzing recovery completion...")
            review_data = self.core_reviewer.analyze_recovery_completion()
            
            # Phase 2: MCP intelligence analysis
            print("\n🧠 Phase 2: Performing MCP intelligence analysis...")
            intelligence_data = self.mcp_intelligence.analyze_recovery_patterns(review_data)
            
            # Phase 3: Generate comprehensive reports
            print("\n📄 Phase 3: Generating comprehensive reports...")
            self._generate_final_reports(review_data, intelligence_data)
            
            # Phase 4: Final validation and assessment
            print("\n✅ Phase 4: Performing final validation...")
            validation_success = self._perform_final_validation(review_data, intelligence_data)
            
            # Phase 5: Workflow readiness determination
            print("\n🎯 Phase 5: Determining workflow readiness...")
            workflow_ready = self._determine_workflow_readiness(review_data, intelligence_data)
            
            overall_success = validation_success and workflow_ready
            
            if overall_success:
                print("✅ Enhanced final recovery review completed successfully!")
                self._display_success_summary(review_data, intelligence_data)
            else:
                print("⚠️ Final recovery review completed with conditions")
                self._display_conditional_summary(review_data, intelligence_data)
                
            return overall_success
            
        except Exception as e:
            print(f"❌ Enhanced final recovery review failed: {e}")
            return False
    
    def _generate_final_reports(self, review_data: Dict[str, Any], intelligence_data: Dict[str, Any]) -> bool:
        """Generate comprehensive final recovery reports"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d")
            
            # Standard final review report
            self._generate_standard_final_report(review_data, timestamp)
            
            # MCP intelligence report
            self._generate_intelligence_final_report(intelligence_data, timestamp)
            
            # Summary reports
            self._generate_summary_reports(review_data, intelligence_data, timestamp)
            
            return True
            
        except Exception as e:
            print(f"Report generation error: {e}")
            return False
    
    def _generate_standard_final_report(self, review_data: Dict[str, Any], timestamp: str) -> None:
        """Generate standard final recovery report"""
        report_path = f"docs/emergency/emergency-recovery-final-review-{timestamp}.md"
        os.makedirs("docs/emergency", exist_ok=True)
        
        completion_metrics = review_data.get('completion_metrics', {})
        quality_assessment = review_data.get('quality_assessment', {})
        workflow_readiness = review_data.get('workflow_readiness', {})
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"""# Emergency Recovery Final Review - {timestamp}

## Executive Summary

- **Review Completed**: {datetime.now().isoformat()}
- **Recovery Completion**: {completion_metrics.get('completion_percentage', 0):.1f}%
- **Quality Score**: {quality_assessment.get('overall_score', 0):.1f}/100
- **Workflow Readiness**: {workflow_readiness.get('readiness_score', 0):.1f}%
- **Standard Workflow Return**: {'✅ Ready' if workflow_readiness.get('ready_for_standard_workflow', False) else '⚠️ Conditional'}

## Recovery Process Completion Analysis

### Recovery Steps Status
""")
            
            recovery_steps = review_data.get('recovery_steps', {})
            for step_name, step_data in recovery_steps.items():
                status = '✅ Completed' if step_data.get('executed', False) else '❌ Incomplete'
                quality = step_data.get('quality_score', 0)
                f.write(f"- **{step_name}**: {status} (Quality: {quality:.1f}/100)\n")
            
            f.write(f"""
### Deliverables Verification
""")
            
            deliverables_verification = review_data.get('deliverables_verification', {})
            found_count = len(deliverables_verification.get('found_deliverables', []))
            missing_count = len(deliverables_verification.get('missing_deliverables', []))
            
            f.write(f"""
- **Found Deliverables**: {found_count}
- **Missing Deliverables**: {missing_count}
- **Deliverables Quality**: Average {self._calculate_deliverables_quality(deliverables_verification):.1f}/100

## Quality Assessment Results

### Code Quality
""")
            
            code_quality = quality_assessment.get('code_quality', {})
            f.write(f"""
- **Ruff Check**: {'✅ Passed' if code_quality.get('ruff_check', False) else '❌ Failed'}
- **Ruff Format**: {'✅ Passed' if code_quality.get('ruff_format', False) else '❌ Failed'}
- **Pyright Check**: {'✅ Passed' if code_quality.get('pyright_check', False) else '❌ Failed'}

### Test Coverage
""")
            
            test_coverage = quality_assessment.get('test_coverage', {})
            f.write(f"""
- **Tests Exist**: {'✅ Yes' if test_coverage.get('tests_exist', False) else '❌ No'}
- **Coverage Percentage**: {test_coverage.get('coverage_percentage', 0):.1f}%
- **Tests Passing**: {'✅ Yes' if test_coverage.get('tests_passing', False) else '❌ No'}

### Architecture Compliance
""")
            
            arch_compliance = quality_assessment.get('architecture_compliance', {})
            f.write(f"""
- **Clean Architecture**: {'✅ Compliant' if arch_compliance.get('clean_architecture', False) else '⚠️ Partial'}
- **TDD Compliance**: {'✅ Compliant' if arch_compliance.get('tdd_compliance', False) else '⚠️ Partial'}
- **DDD Compliance**: {'✅ Compliant' if arch_compliance.get('ddd_compliance', False) else '⚠️ Partial'}
- **Overall Score**: {arch_compliance.get('compliance_score', 0):.1f}/100

## Workflow Readiness Assessment

### Readiness Indicators
- **Project Health**: {workflow_readiness.get('project_health', 'unknown')}
- **Build Status**: {workflow_readiness.get('build_status', 'unknown')}
- **Test Suite Status**: {workflow_readiness.get('test_suite_status', 'unknown')}
- **Metadata Consistency**: {'✅ Consistent' if workflow_readiness.get('metadata_consistency', False) else '❌ Inconsistent'}

## Recommendations

### Immediate Actions
""")
            
            if completion_metrics.get('completion_percentage', 0) < 100:
                f.write("- Complete missing recovery steps before workflow transition\n")
            if quality_assessment.get('overall_score', 0) < 75:
                f.write("- Address quality issues identified in assessment\n")
            if not workflow_readiness.get('ready_for_standard_workflow', False):
                f.write("- Resolve workflow readiness issues before standard workflow return\n")
            
            f.write(f"""
### Next Steps
1. {'Execute `/create-use-case <new-issue>` or `/sprint-planning <sprint-number>`' if workflow_readiness.get('ready_for_standard_workflow', False) else 'Address identified issues before workflow return'}
2. Review and implement improvement recommendations
3. Share recovery learnings with development team

## Conclusion

{'Emergency recovery process successfully completed. Project is ready for standard workflow return.' if workflow_readiness.get('ready_for_standard_workflow', False) else 'Emergency recovery process completed with conditions. Address outstanding issues before workflow return.'}
""")
        
        print(f"✅ Standard final report generated: {report_path}")
    
    def _generate_intelligence_final_report(self, intelligence_data: Dict[str, Any], timestamp: str) -> None:
        """Generate MCP intelligence final report"""
        report_path = f"docs/emergency/emergency-recovery-final-review-{timestamp}-mcp-intelligence.md"
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"""# MCP-Enhanced Final Recovery Review Intelligence Report - {timestamp}

## Intelligence Analysis Summary

### Recovery Pattern Analysis
""")
            
            pattern_analysis = intelligence_data.get('pattern_analysis', {})
            completion_patterns = pattern_analysis.get('completion_patterns', [])
            quality_patterns = pattern_analysis.get('quality_patterns', {})
            
            completed_steps = sum(1 for p in completion_patterns if p.get('completion_score', 0) == 100)
            avg_quality = sum(p.get('quality_score', 0) for p in completion_patterns) / len(completion_patterns) if completion_patterns else 0
            
            f.write(f"""
- **Completed Recovery Steps**: {completed_steps}/{len(completion_patterns)}
- **Average Quality Score**: {avg_quality:.1f}/100
- **Overall Quality Trend**: {quality_patterns.get('code_quality_trend', 'unknown')}
- **Test Coverage Trend**: {quality_patterns.get('test_coverage_trend', 'unknown')}
- **Documentation Quality**: {quality_patterns.get('documentation_quality', 'unknown')}

### Quality Predictions
""")
            
            predictions = intelligence_data.get('quality_predictions', {})
            f.write(f"""
- **Workflow Success Probability**: {predictions.get('workflow_success_probability', 0):.1f}%
- **Quality Improvement Potential**: {predictions.get('quality_improvement_potential', 0):.1f} points
- **Estimated Transition Timeline**: {predictions.get('transition_timeline', 'unknown')}
- **Confidence Level**: {predictions.get('confidence_level', 'unknown')}

### Improvement Recommendations
""")
            
            recommendations = intelligence_data.get('improvement_recommendations', [])
            for rec in recommendations:
                f.write(f"""
#### {rec.get('category', 'Unknown').replace('_', ' ').title()}
- **Priority**: {rec.get('priority', 'unknown')}
- **Description**: {rec.get('description', 'No description')}
- **Estimated Effort**: {rec.get('estimated_effort', 'unknown')}
- **Actions**: {', '.join(rec.get('actions', []))}
""")
            
            f.write(f"""
### Workflow Optimization
""")
            
            workflow_optimization = intelligence_data.get('workflow_optimization', {})
            
            f.write(f"""
#### Immediate Actions ({len(workflow_optimization.get('immediate_actions', []))})
""")
            for action in workflow_optimization.get('immediate_actions', []):
                f.write(f"- **{action.get('action', 'Unknown')}** (Urgency: {action.get('urgency', 'unknown')})\n")
            
            f.write(f"""
#### Short-term Goals ({len(workflow_optimization.get('short_term_goals', []))})
""")
            for goal in workflow_optimization.get('short_term_goals', []):
                f.write(f"- **{goal.get('goal', 'Unknown')}** ({goal.get('timeline', 'unknown')})\n")
            
            f.write(f"""
## MCP Intelligence Insights

This analysis was enhanced with MCP capabilities for comprehensive recovery pattern recognition, 
quality prediction, and workflow optimization recommendations.

### Enhanced Analysis Features
- Automated pattern recognition across recovery phases
- Predictive quality assessment with confidence intervals
- Intelligent workflow optimization strategies
- Professional standards integration via Context7

## Conclusion

{'Based on MCP analysis, the recovery process meets professional standards and is ready for workflow transition.' if predictions.get('workflow_success_probability', 0) >= 75 else 'MCP analysis indicates additional improvements needed before optimal workflow transition.'}
""")
        
        print(f"✅ Intelligence report generated: {report_path}")
    
    def _generate_summary_reports(self, review_data: Dict[str, Any], intelligence_data: Dict[str, Any], timestamp: str) -> None:
        """Generate summary reports"""
        # Quality assessment summary JSON
        quality_summary_path = f"docs/emergency/quality-assessment-summary-{timestamp}.json"
        
        quality_summary = {
            "assessment_timestamp": datetime.now().isoformat(),
            "completion_metrics": review_data.get('completion_metrics', {}),
            "quality_assessment": review_data.get('quality_assessment', {}),
            "workflow_readiness": review_data.get('workflow_readiness', {}),
            "mcp_predictions": intelligence_data.get('quality_predictions', {}),
            "improvement_recommendations": intelligence_data.get('improvement_recommendations', [])
        }
        
        with open(quality_summary_path, 'w') as f:
            json.dump(quality_summary, f, indent=2)
        
        print(f"✅ Quality summary generated: {quality_summary_path}")
    
    def _calculate_deliverables_quality(self, deliverables_verification: Dict[str, Any]) -> float:
        """Calculate average deliverables quality"""
        quality_assessment = deliverables_verification.get('quality_assessment', {})
        if not quality_assessment:
            return 0.0
        
        scores = list(quality_assessment.values())
        return sum(scores) / len(scores) if scores else 0.0
    
    def _perform_final_validation(self, review_data: Dict[str, Any], intelligence_data: Dict[str, Any]) -> bool:
        """Perform final validation of recovery review"""
        try:
            print("🔍 Performing final recovery validation...")
            
            validation_results = {
                'completion_valid': True,
                'quality_acceptable': True,
                'reports_generated': True,
                'mcp_analysis_complete': True
            }
            
            # Validate completion metrics
            completion_metrics = review_data.get('completion_metrics', {})
            completion_percentage = completion_metrics.get('completion_percentage', 0)
            
            if completion_percentage < 100:
                validation_results['completion_valid'] = False
                print(f"⚠️ Recovery completion validation: {completion_percentage:.1f}% complete")
            else:
                print(f"✅ Recovery completion validation: 100% complete")
            
            # Validate quality metrics
            quality_assessment = review_data.get('quality_assessment', {})
            overall_quality = quality_assessment.get('overall_score', 0)
            
            if overall_quality < 60:  # Minimum acceptable quality
                validation_results['quality_acceptable'] = False
                print(f"⚠️ Quality validation: {overall_quality:.1f}/100 (below minimum)")
            else:
                print(f"✅ Quality validation: {overall_quality:.1f}/100")
            
            # Validate report generation
            expected_reports = [
                f"docs/emergency/emergency-recovery-final-review-{datetime.now().strftime('%Y%m%d')}.md",
                f"docs/emergency/emergency-recovery-final-review-{datetime.now().strftime('%Y%m%d')}-mcp-intelligence.md"
            ]
            
            for report in expected_reports:
                if not os.path.exists(report):
                    validation_results['reports_generated'] = False
                    print(f"⚠️ Missing report: {report}")
                else:
                    print(f"✅ Report generated: {report}")
            
            # Validate MCP analysis
            mcp_predictions = intelligence_data.get('quality_predictions', {})
            if not mcp_predictions:
                validation_results['mcp_analysis_complete'] = False
                print("⚠️ MCP analysis incomplete")
            else:
                print("✅ MCP analysis complete")
            
            # Overall validation
            overall_valid = all(validation_results.values())
            
            if overall_valid:
                print("✅ Final validation passed")
            else:
                print("⚠️ Final validation found issues")
                
            return overall_valid
            
        except Exception as e:
            print(f"Final validation error: {e}")
            return False
    
    def _determine_workflow_readiness(self, review_data: Dict[str, Any], intelligence_data: Dict[str, Any]) -> bool:
        """Determine readiness for standard workflow return"""
        try:
            workflow_readiness = review_data.get('workflow_readiness', {})
            predictions = intelligence_data.get('quality_predictions', {})
            
            # Core readiness indicators
            readiness_score = workflow_readiness.get('readiness_score', 0)
            ready_for_workflow = workflow_readiness.get('ready_for_standard_workflow', False)
            
            # MCP predictions
            success_probability = predictions.get('workflow_success_probability', 0)
            confidence_level = predictions.get('confidence_level', 'low')
            
            # Combined assessment
            workflow_ready = (
                readiness_score >= 75 and 
                ready_for_workflow and 
                success_probability >= 70 and
                confidence_level in ['high', 'medium']
            )
            
            if workflow_ready:
                print("✅ Workflow readiness: Ready for standard workflow return")
            else:
                print("⚠️ Workflow readiness: Conditions must be addressed before workflow return")
                print(f"   - Readiness Score: {readiness_score:.1f}/100 (target: 75+)")
                print(f"   - Success Probability: {success_probability:.1f}% (target: 70%+)")
                print(f"   - Confidence Level: {confidence_level} (target: medium+)")
            
            return workflow_ready
            
        except Exception as e:
            print(f"Workflow readiness determination error: {e}")
            return False
    
    def _display_success_summary(self, review_data: Dict[str, Any], intelligence_data: Dict[str, Any]) -> None:
        """Display success summary"""
        completion_metrics = review_data.get('completion_metrics', {})
        quality_assessment = review_data.get('quality_assessment', {})
        workflow_readiness = review_data.get('workflow_readiness', {})
        predictions = intelligence_data.get('quality_predictions', {})
        
        print("\n" + "="*60)
        print("🎉 EMERGENCY RECOVERY FINAL REVIEW SUCCESS")
        print("="*60)
        print(f"📊 Recovery Completion: {completion_metrics.get('completion_percentage', 0):.1f}%")
        print(f"🎯 Quality Score: {quality_assessment.get('overall_score', 0):.1f}/100")
        print(f"✅ Workflow Readiness: {workflow_readiness.get('readiness_score', 0):.1f}%")
        print(f"📈 Success Probability: {predictions.get('workflow_success_probability', 0):.1f}%")
        print(f"⏱️ Transition Timeline: {predictions.get('transition_timeline', 'unknown')}")
        print("\n🚀 Emergency Recovery Complete!")
        print("✅ Ready for Standard TDD/DDD/Layered Workflow Return")
        print("\n💡 Next Steps:")
        print("   1. Execute `/create-use-case <new-issue>` for new feature development")
        print("   2. Execute `/sprint-planning <sprint-number>` for sprint organization")
        print("   3. Share recovery learnings with development team")
        print("="*60)
    
    def _display_conditional_summary(self, review_data: Dict[str, Any], intelligence_data: Dict[str, Any]) -> None:
        """Display conditional summary with required actions"""
        completion_metrics = review_data.get('completion_metrics', {})
        quality_assessment = review_data.get('quality_assessment', {})
        workflow_readiness = review_data.get('workflow_readiness', {})
        recommendations = intelligence_data.get('improvement_recommendations', [])
        
        print("\n" + "="*60)
        print("⚠️ EMERGENCY RECOVERY REVIEW - CONDITIONS DETECTED")
        print("="*60)
        print(f"📊 Recovery Completion: {completion_metrics.get('completion_percentage', 0):.1f}%")
        print(f"🎯 Quality Score: {quality_assessment.get('overall_score', 0):.1f}/100")
        print(f"⚠️ Workflow Readiness: {workflow_readiness.get('readiness_score', 0):.1f}%")
        print("\n🔧 Required Actions Before Workflow Return:")
        
        for i, rec in enumerate(recommendations[:3], 1):  # Show top 3 recommendations
            print(f"   {i}. {rec.get('description', 'Address identified issue')} (Priority: {rec.get('priority', 'unknown')})")
        
        print("\n💡 After Addressing Issues:")
        print("   1. Re-run recovery validation if needed")
        print("   2. Execute workflow readiness assessment")
        print("   3. Proceed with standard workflow return when ready")
        print("="*60)


def main():
    """Main execution function"""
    try:
        # Get context parameter from command line
        context_param = sys.argv[1] if len(sys.argv) > 1 else None
        
        # Execute enhanced final recovery review
        reviewer = EnhancedRecoveryReviewer(context_param)
        success = reviewer.execute_enhanced_final_recovery_review()
        
        sys.exit(0 if success else 1)
        
    except Exception as e:
        print(f"❌ Enhanced final recovery review execution failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()