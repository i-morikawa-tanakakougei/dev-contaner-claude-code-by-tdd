# Command: 99-4-retroactive-test-expert

## 🎯 Expert Profile Declaration

During command execution, you act as a **Retroactive Test Creation Specialist** focusing on emergency recovery testing.

**Language Guidelines:**
- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Expert Profile
- **Role**: Retroactive Test Creation Expert
- **Specialized Areas**: 
  - **Emergency Fix Test Design**: Comprehensive test strategies for urgently implemented code changes
  - **TDD Recovery Process**: Retroactive recovery of TDD processes skipped during emergencies
  - **Test Coverage Analysis**: Code coverage evaluation and quality assurance implementation
- **Responsibility Scope**: Retroactive test creation and coverage recovery for emergency-fixed code

### Execution Mindset
1. **TDD Principle Adherence**: Retroactive application of test-first quality standards even in emergencies
2. **Comprehensive Coverage**: Complete implementation of normal case, error case, and boundary value tests
3. **Regression Prevention**: Validate impact on existing functionality and prevent future issues

### Evaluation Criteria
- **Quality**: Achievement of test coverage goals and successful execution of all test cases
- **Completion**: Establishment of sufficient test protection for emergency fixes
- **Escalation**: Propose alternative approaches when coverage goals are not met

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🚨 Emergency Recovery Workflow**: Recovery(99-1) → Issue Creation(99-2) → Sync Docs(99-3) → **Retroactive Tests(99-4)** → Validation(99-5) → Metadata Reconcile(99-6) → Final Review(99-7)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via emergency recovery integration

> 📖 **Document Management System**: [Emergency Recovery Guide](./EMERGENCY-RECOVERY-GUIDE.md)  
> 🗺️ **Current Position**: Retroactive Test Creation (99-4/99-7)  
> 🎯 **Phase Purpose**: Comprehensive test creation for emergency fix code and TDD principle recovery  
> ➡️ **Next Stage**: 99-5-validate-emergency-fix (Emergency Fix Validation)

## 🎯 PHASE PURPOSE: RETROACTIVE TEST CREATION

**⚠️ Important Notice:**
- **This step focuses on TEST CREATION ONLY** - Focus on creating tests for emergency-fixed code
- **FOLLOW TDD PRINCIPLES RETROACTIVELY** - Ensure test quality through retroactive TDD principle application  
- **Coverage restoration phase** - Recover test coverage lost due to emergency fixes

**What this step does:**
1. `99-3-sync-documentation` ← Documentation synchronization with emergency changes
2. `99-4-retroactive-test` ← **【YOU ARE HERE】Create comprehensive tests for emergency changes**
3. `99-5-validate-emergency-fix` ← Validate emergency fix implementation with tests
4. Then continue with metadata reconciliation and emergency recovery finalization

**CREATE RETROACTIVE TESTS FOR EMERGENCY CHANGES ONLY.**

## 📋 Lightweight Context Management

### Required Reading (Minimal)

```bash
# Validate optional issue number or context parameter
if [[ -n "$1" ]]; then
    ISSUE_OR_CONTEXT="$1"
    echo "🧪 Executing retroactive-test with context: $ISSUE_OR_CONTEXT"
else
    echo "🧪 Executing retroactive-test in comprehensive analysis mode"
fi

echo "🧪 Executing retroactive-test with automated Python implementation..."

# Execute the enhanced Python implementation
SCRIPT_PATH=".claude/commands/tdd-ddd-layered-expert/utils/99-4-retroactive-test-expert.py"

if [[ -f "$SCRIPT_PATH" ]]; then
    echo "✅ Found enhanced implementation: $SCRIPT_PATH"
    if [[ -n "$ISSUE_OR_CONTEXT" ]]; then
        uv run "$SCRIPT_PATH" "$ISSUE_OR_CONTEXT"
    else
        uv run "$SCRIPT_PATH"
    fi
    EXIT_CODE=$?

    if [[ $EXIT_CODE -eq 0 ]]; then
        echo "✅ Retroactive test creation completed successfully"
    else
        echo "❌ Retroactive test creation failed with exit code: $EXIT_CODE"
        exit $EXIT_CODE
    fi
else
    echo "❌ Enhanced implementation not found: $SCRIPT_PATH"
    echo "💡 Please ensure the Python implementation is available"
    exit 1
fi
```

#### Issue Comment Retrieval and Analysis
```bash
# Load GitHub issue with comments (if issue number provided)
if [[ -n "$ISSUE_NUMBER" ]]; then
    echo "Retrieving GitHub issue #$ISSUE_NUMBER with comments for retroactive test creation..."
    
    # Get issue details with comments
    ISSUE_DATA=$(gh issue view $ISSUE_NUMBER --json title,body,comments,updatedAt,createdAt,labels,assignees)
    
    # Extract and prioritize recent comments
    RECENT_COMMENTS=$(echo "$ISSUE_DATA" | jq -r '.comments | sort_by(.createdAt) | reverse | .[0:5]')
    
    COMMENT_COUNT=$(echo "$ISSUE_DATA" | jq '.comments | length')
    echo "Found $COMMENT_COUNT comments on issue #$ISSUE_NUMBER"
    echo "Prioritizing latest 5 comments for retroactive test creation"
    
    # Check for retroactive test requirements through comments
    if [[ $COMMENT_COUNT -gt 0 ]]; then
        echo "Analyzing comment timeline for test requirements..."
        # Recent comments take precedence for test creation
        LATEST_COMMENT_DATE=$(echo "$RECENT_COMMENTS" | jq -r '.[0].createdAt // empty')
        if [[ -n "$LATEST_COMMENT_DATE" ]]; then
            echo "Latest test requirement update: $LATEST_COMMENT_DATE"
        fi
        
        # Extract retroactive test related comments
        echo "Extracting retroactive test context..."
        echo "$RECENT_COMMENTS" | jq -r '.[] | select(.body | contains("test") or contains("retroactive") or contains("emergency") or contains("coverage") or contains("scenario")) | .body' | head -3
    fi
fi
```

## GitHub Issue Integration

### Issue Comment Retrieval Process
Always retrieve issue comments when processing GitHub issues for emergency fixes:

```bash
# Fetch issue with full context for emergency fix analysis
if [[ -n "$ISSUE_NUMBER" ]]; then
    echo "Retrieving GitHub issue #$ISSUE_NUMBER with comments for emergency fix analysis..."
    
    # Get issue details with comments
    ISSUE_DATA=$(gh issue view $ISSUE_NUMBER --json title,body,comments,updatedAt,createdAt)
    
    # Extract and prioritize recent comments for latest specifications
    RECENT_COMMENTS=$(echo "$ISSUE_DATA" | jq -r '.comments | sort_by(.createdAt) | reverse | .[0:5]')
    
    echo "Found $(echo "$ISSUE_DATA" | jq '.comments | length') comments"
    echo "Prioritizing latest 5 comments for emergency fix specification analysis"
fi
```

### Comment Analysis Strategy for Emergency Fixes
1. **Latest First**: Recent comments override earlier specifications for emergency changes
2. **Authority Recognition**: Identify specification authors vs. discussants for emergency requirements  
3. **Change Tracking**: Monitor emergency fix requirement evolution
4. **Conflict Detection**: Flag contradictory emergency fix requirements

## 🚀 Expert Execution Flow

### Phase 1: Emergency Fix Analysis and Understanding
**As an expert, analyze the following:**
1. **GitHub Issue Analysis**
   - Review Points: Emergency fix details, impact scope, modified files
   - Evaluation Criteria: Quality impact level of emergency fix and required test scope
   
2. **Code Change Identification**
   - Review Points: Actually changed source code, functions, classes
   - Evaluation Criteria: Test target scope and priority

3. **Existing Test Coverage Assessment**
   - Review Points: Current test coverage status, missing areas
   - Evaluation Criteria: Coverage goals and feasibility

### Phase 2: Test Design and Planning
**As an expert, design the following:**
1. **Normal Case Test Case Design**
   ```
   - Expected behavior of emergency-fixed functionality
   - Input value patterns and output value verification
   - Business logic accuracy confirmation
   ```
   
2. **Error Case and Boundary Value Test Case Design**
   ```
   - Error handling validity verification
   - Behavior confirmation under boundary conditions
   - Safety assurance in exceptional situations
   ```

3. **Regression Test Case Design**
   ```
   - Confirmation of no impact on existing functionality
   - System-wide consistency verification
   - Integration operation confirmation
   ```

### Phase 3: Test Implementation and Execution
**As an expert, execute the following:**
1. **Test File Creation**
   - Action: Implement comprehensive test cases in compliance with existing framework
   - Expected Result: Executable and maintainable test suite
   
2. **Test Execution and Verification**
   - Action: Execute created tests and confirm passing
   - Expected Result: Successful execution of all test cases

3. **Coverage Measurement and Evaluation**
   - Action: Measure test coverage and confirm goal achievement
   - Expected Result: Achievement of set coverage goals

## ✅ Built-in Quality Assurance

### Self-Diagnostic Checklist
**Mandatory Items (MUST):**
- [ ] **GitHub Issue Analysis Complete**: Complete understanding of emergency fix content
- [ ] **Code Change Identification Complete**: Clear identification of test targets
- [ ] **Test Case Design Complete**: Design of normal, error, and regression tests
- [ ] **Test Implementation Complete**: Creation of executable test files
- [ ] **Test Execution Confirmation**: Successful execution of all test cases
- [ ] **Coverage Goal Achievement**: Achievement of set coverage goals

**Recommended Items (SHOULD):**
- [ ] **Test Naming Convention Compliance**: Clear and understandable test method names
- [ ] **Test Documentation Creation**: Documentation of complex test scenarios
- [ ] **Appropriate Mock/Stub Usage**: Proper isolation of unit tests

### Quality Metrics
| Metric | Target | Actual | Result |
|--------|--------|--------|--------|
| Test Coverage | Set Value% | [Actual] | ✅/❌ |
| Test Execution Success Rate | 100% | [Actual] | ✅/❌ |
| Created Test Cases Count | Minimum 10 | [Actual] | ✅/❌ |

### Error Handling
**Expected Errors and Countermeasures:**
1. **Test Framework Not Detected**: Use appropriate framework according to project conventions
2. **Coverage Goal Not Met**: Create additional test cases or adjust coverage goals
3. **Test Execution Failure**: Review test logic and re-examine emergency fix code

## 📊 Standardized Output Format

### 実行サマリー
- ✅ **緊急修正分析**: [GitHub Issue #X 分析完了とコード変更特定]
- ✅ **テストケース設計**: [正常系X件、異常系Y件、回帰テストZ件設計完了]
- ✅ **テスト実装**: [テストファイル作成とフレームワーク統合]
- ✅ **テスト実行**: [全テストケース実行成功]
- ✅ **カバレッジ達成**: [目標X%達成、実績Y%]

### 成果物
**作成されたファイル:**
- `tests/[module]/test_[module]_emergency.py`: [緊急修正用テストファイル]
- `tests/[module]/test_[module]_regression.py`: [回帰テスト用ファイル]
- `tests/integration/test_[integration]_emergency.py`: [統合テストファイル]

### 総合判定
**ステータス**: `SUCCESS`
**品質スコア**: [スコア]/100
**カバレッジ達成**: `[達成率]% (目標: [目標値]%)`
**次フェーズ準備**: `READY`

### 次のステップ
1. **即座に実行可能**: `/validate-emergency-fix [issue-number] --strict`
2. **条件付き実行**: カバレッジ不足時 → `/retroactive-test [issue-number] --coverage-target [higher-target]`
3. **要確認事項**: テスト実行失敗時の緊急修正コード見直し

### メタデータ更新

実行履歴と遡及的テスト作成情報が自動的にJSONファイルに記録されます：

```json
{
  "retroactive_tests": {
    "creation_completed_at": "[ISO-8601]",
    "status": "SUCCESS|PARTIAL|FAILED",
    "target_context": "[issue_number|comprehensive]",
    "emergency_fixes_covered": [count],
    "test_statistics": {
      "total_tests_created": [count],
      "unit_tests": [count],
      "integration_tests": [count],
      "regression_tests": [count],
      "test_files_created": [count]
    },
    "coverage_analysis": {
      "baseline_coverage": [percentage],
      "target_coverage": [percentage],
      "achieved_coverage": [percentage],
      "coverage_improvement": [percentage],
      "uncovered_critical_areas": [count]
    },
    "test_quality_metrics": {
      "test_success_rate": [percentage],
      "assertion_density": [average_per_test],
      "test_complexity_score": [score],
      "maintainability_score": [score]
    },
    "emergency_fix_analysis": {
      "analyzed_commits": [count],
      "code_changes_tested": [count],
      "edge_cases_covered": [count],
      "regression_scenarios": [count]
    },
    "created_test_files": [
      {
        "file_path": "[path]",
        "test_type": "unit|integration|regression",
        "tests_count": [count],
        "coverage_target": "[module_or_function]"
      }
    ],
    "next_actions": ["/validate-emergency-fix", "/run-all-tests"]
  },
  "execution_history": {
    "commands_executed": [
      {
        "command": "/retroactive-test [issue-or-context]",
        "executed_at": "[ISO-8601]",
        "status": "success|failed",
        "files_affected": ["test_files...", "coverage_reports..."]
      }
    ]
  }
}
```