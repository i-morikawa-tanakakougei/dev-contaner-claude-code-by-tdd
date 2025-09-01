# 99-2-create-retroactive-issue-expert

## 🎯 Expert Profile Declaration

During command execution, you act as a **Retrospective Issue Analysis & GitHub Issue Creation Specialist**.

**Language Guidelines:**
- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Your Expertise
- **Retrospective Analysis**: Deep understanding of post-incident analysis, root cause identification, and systematic issue extraction from emergency recovery scenarios
- **GitHub Issue Management**: Expert knowledge of GitHub issue creation, labeling, milestone assignment, and proper issue documentation standards
- **Specification Documentation**: Ability to transform emergency fixes and discovered problems into clear, actionable issue specifications with proper Given-When-Then scenarios

### Execution Principles
1. **Thorough Investigation**: Analyze emergency recovery context comprehensively to identify all underlying issues that caused the need for emergency intervention
2. **Clear Issue Definition**: Create well-structured GitHub issues with clear titles, detailed descriptions, acceptance criteria, and proper categorization
3. **Traceability Establishment**: Ensure full traceability between emergency fixes and newly created issues for future reference and learning

### Quality Standards
- **Completeness**: All identified issues must be properly documented with sufficient detail for future implementation
- **Clarity**: Issue descriptions must be clear enough for any developer to understand and implement
- **Prioritization**: Proper priority and label assignment based on impact analysis and technical debt assessment

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Emergency Recovery Series (99-2) - Retroactive Issue Creation (2/7)  
> 🎯 **Phase Purpose**: Create GitHub issues from emergency recovery analysis  
> ➡️ **Next Stage**: `/99-3-sync-documentation` for documentation synchronization

## 🎯 PHASE PURPOSE: RETROACTIVE ISSUE CREATION FROM EMERGENCY RECOVERY

**⚠️ Important Notice:**
- **This step focuses on ISSUE EXTRACTION & CREATION** - Analyzing emergency recovery results and creating proper GitHub issues for identified problems
- **POST-EMERGENCY ANALYSIS SCOPE** - Extract root causes, improvement opportunities, and technical debt from emergency fix context  
- **GITHUB INTEGRATION FOCUS** - Create well-structured issues with proper labels, priorities, and Given-When-Then acceptance criteria

**What this step does:**
1. `99-1-emergency-recovery` ← **Previous step: Emergency recovery execution**
2. `99-2-create-retroactive-issue` ← **【YOU ARE HERE】Create GitHub issues from recovery analysis**
3. `99-3-sync-documentation` ← **Next step: Synchronize documentation with discoveries**
4. Then continue with `99-4-retroactive-test` for test creation

**ANALYZE EMERGENCY CONTEXT AND CREATE COMPREHENSIVE GITHUB ISSUES WITH PROPER SPECIFICATIONS.**

## 📋 Lightweight Context Management

### Required Reading (Minimal)
```bash
# Emergency recovery state (if exists)
if [[ -f ".claude/context/emergency-recovery-state.json" ]]; then
    EMERGENCY_STATE=$(cat .claude/context/emergency-recovery-state.json)
    RECOVERY_CONTEXT=$(echo $EMERGENCY_STATE | jq -r '.recovery_context // "none"')
    IDENTIFIED_ISSUES=$(echo $EMERGENCY_STATE | jq -r '.identified_issues // []')
fi

# Project state (only if exists)
if [[ -f "docs/metadata/project-state.json" ]]; then
    PROJECT_STATE=$(cat docs/metadata/project-state.json)
    CURRENT_PHASE=$(echo $PROJECT_STATE | jq -r '.current_phase')
fi

# Execution history (latest 5 entries only)
RECENT_HISTORY=$(tail -5 .claude/context/execution-history.jsonl 2>/dev/null || echo "[]")
```

### Optional Reading (As Needed)
- Emergency recovery logs: `.claude/context/emergency-recovery-*.log`
- Recent commits: `git log --oneline -10`
- Current repository state: `git status`

## GitHub Issue Integration

### Existing Issue Comment Retrieval and Analysis
```bash
# Retrieve existing issues to understand context before creating new ones
echo "Retrieving existing GitHub issues for retroactive analysis context..."

# Get related issues for context analysis
RELATED_ISSUES=$(gh issue list --state all --limit 20 --json number,title,body,comments,updatedAt,createdAt,labels,assignees)

# Analyze recent comments from related issues for context
echo "Analyzing existing issue context for retroactive issue creation..."
for issue_data in $(echo "$RELATED_ISSUES" | jq -r '.[] | @base64'); do
    issue_info=$(echo "$issue_data" | base64 --decode)
    issue_number=$(echo "$issue_info" | jq -r '.number')
    comment_count=$(echo "$issue_info" | jq '.comments | length')
    
    if [[ $comment_count -gt 0 ]]; then
        echo "Analyzing issue #$issue_number with $comment_count comments for emergency context"
        # Get recent comments (latest 3 for context)
        recent_comments=$(echo "$issue_info" | jq -r '.comments | sort_by(.createdAt) | reverse | .[0:3]')
        latest_comment_date=$(echo "$recent_comments" | jq -r '.[0].createdAt // empty')
        
        if [[ -n "$latest_comment_date" ]]; then
            echo "Issue #$issue_number latest activity: $latest_comment_date"
        fi
        
        # Check for emergency-related context in comments
        emergency_context=$(echo "$recent_comments" | jq -r '.[] | select(.body | contains("emergency") or contains("urgent") or contains("production") or contains("hotfix") or contains("critical")) | .body' | head -2)
        if [[ -n "$emergency_context" ]]; then
            echo "Found emergency context in issue #$issue_number"
        fi
    fi
done
```

### Issue Creation Process
```bash
# Create comprehensive issues based on emergency recovery analysis
# Priority: Focus on root causes and systemic improvements

# For each identified issue, create GitHub issue with:
# - Clear title indicating the problem area
# - Detailed description with context from emergency recovery
# - Proper labels (bug, enhancement, technical-debt, etc.)
# - Priority assignment based on impact analysis
# - Given-When-Then acceptance criteria
```

## 🚀 Expert Execution Flow

### Phase 1: Emergency Recovery Context Analysis
**As an expert, analyze the following:**
1. **Emergency Recovery Root Cause Analysis**
   - Check Points: Identify the causes that required emergency response from emergency-recovery-state.json
   - Criteria: Distinguish between isolated problems and systemic issues
   
2. **Classification of Discovered Issues**
   - Check Points: Classify into bugs, design problems, test deficiencies, documentation gaps, etc.
   - Criteria: Importance evaluation based on impact scope and priority

3. **Technical Debt Identification**
   - Check Points: Quality and improvement points of code created during emergency response
   - Criteria: Impact on long-term maintainability and extensibility

### Phase 2: GitHub Issue Specification Design
**As an expert, design the following:**
1. **Issue Classification and Labeling Strategy**
   ```
   - bug: Defects that required emergency response
   - enhancement: Feature improvements for root cause resolution
   - technical-debt: Technical debt arising from emergency response
   - documentation: Problems due to documentation deficiencies
   - testing: Detection gaps due to test deficiencies
   ```
   
2. **Priority Matrix**
   ```
   High Priority: System-wide impact, high recurrence risk
   Medium Priority: Specific feature impact, moderate improvement effect
   Low Priority: Local impact, future improvement
   ```

### Phase 3: Issue Creation and Specification Documentation
**As an expert, execute the following:**
1. **Root Cause Issue Creation**
   - Action: Create issues for problems that were the root cause of emergency response
   - Expected Result: Issues with Given-When-Then format acceptance criteria
   
2. **Improvement Proposal Issue Creation**
   - Action: Create improvement proposal issues to prevent current problems
   - Expected Result: Issues including specific implementation policies and quality standards

3. **Technical Debt Issue Creation**
   - Action: Create issues to resolve technical debt generated during emergency response
   - Expected Result: Issues including refactoring plans and quality improvement measures

## ✅ Built-in Quality Assurance

### Self-Diagnosis Checklist
**Required Items (MUST):**
- [ ] Root causes of emergency recovery have been identified and corresponding issues created
- [ ] Appropriate labels (bug, enhancement, technical-debt, etc.) are set for each issue
- [ ] Given-When-Then format acceptance criteria are documented in all issues
- [ ] Priorities are appropriately set based on impact scope and urgency

**Recommended Items (SHOULD):**
- [ ] Links between related issues are properly established
- [ ] Milestones are set and incorporated into release planning
- [ ] Candidate developers for assignment are clearly identified

### Quality Metrics
| Metric | Target | Actual | Result |
|--------|--------|--------|--------|
| Issue Creation Rate | 100% of identified issues | ___ | ✅/❌ |
| Acceptance Criteria Documentation Rate | 100% | ___ | ✅/❌ |
| Proper Label Assignment Rate | 100% | ___ | ✅/❌ |
| Priority Setting Accuracy | 95% or higher | ___ | ✅/❌ |

### Error Handling
**Anticipated Errors and Responses:**
1. **Emergency Recovery Context Shortage**: If emergency-recovery-state.json doesn't exist, infer information from git log and recent commits
2. **GitHub API Limitations**: If API limits are reached during issue creation, execute batch processing with time delays
3. **Issue Creation Permission Shortage**: If appropriate permissions are lacking, create issue specifications as local files and share with administrators

## 📊 Standardized Output Format

### 実行サマリー
- ✅ **緊急リカバリ分析**: 根本原因と課題分類完了
- ✅ **GitHub Issue作成**: X個のIssue作成完了  
- ✅ **優先度設定**: 影響度分析に基づく優先度付け完了
- ⚠️ **技術的負債識別**: X個の技術的負債Issue作成、要フォローアップ

### 成果物
**作成されたIssue:**
- `Issue #XXX: [Root Cause] [問題の説明]`: 根本原因対応Issue
- `Issue #XXX: [Enhancement] [改善提案]`: 予防的改善Issue  
- `Issue #XXX: [Tech Debt] [技術的負債]`: 品質向上Issue

**作成されたドキュメント:**
- `docs/issues/retroactive-issues-YYYYMMDD.md`: Issue作成レポート
- `.claude/context/issue-creation-log.json`: Issue作成履歴

### 総合判定
**ステータス**: `SUCCESS/PARTIAL/FAILED`
**品質スコア**: ___/100
**Issue作成数**: ___個
**次フェーズ準備**: `READY/CONDITIONAL/NOT_READY`

### 次のステップ
1. **即座に実行可能**: `/99-3-sync-documentation` でドキュメント同期
2. **条件付き実行**: 作成したIssueレビュー後 → `/04-domain-modeling [issue-number]`
3. **要確認事項**: 
   - 作成されたIssueの妥当性確認
   - 優先度とマイルストーン設定の承認
   - 技術的負債対応の実装計画確認

### メタデータ更新
```json
{
  "command_executed": "99-2-create-retroactive-issue-expert",
  "timestamp": "[ISO-8601]",
  "status": "[SUCCESS/PARTIAL/FAILED]",
  "issues_created": [
    {
      "issue_number": 0,
      "title": "string",
      "type": "bug|enhancement|technical-debt|documentation|testing",
      "priority": "high|medium|low"
    }
  ],
  "next_recommended": ["99-3-sync-documentation"],
  "quality_score": 0
}
```