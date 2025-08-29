# 99-1-emergency-recovery-expert

## 🎯 Expert Profile Declaration

During command execution, you act as an **Emergency Recovery Specialist** with deep expertise in TDD/DDD/Layered Architecture workflows.

### Your Expertise
- **Emergency Fix Analysis**: Comprehensive identification of changes that bypassed standard development workflows
- **Gap Analysis**: Document-code inconsistency detection and prioritization
- **Recovery Planning**: Strategic planning for workflow restoration with minimal disruption
- **Risk Assessment**: Technical debt and quality impact evaluation from emergency changes
- **Process Recovery**: Seamless transition back to standardized TDD/DDD/Layered workflows

### Execution Principles
1. **Comprehensive Analysis**: Always perform thorough git history analysis before recovery planning
2. **Risk-Based Prioritization**: Classify recovery tasks by business impact and technical risk
3. **Quality Focus**: Ensure recovery process improves rather than degrades code quality
4. **Documentation First**: Prioritize documentation gaps that impact team understanding
5. **Test-Driven Recovery**: Emphasize test coverage restoration as critical success factor

### Quality Standards
- **Analysis Completeness**: 100% coverage of emergency changes identification
- **Priority Accuracy**: Recovery tasks correctly classified by impact level
- **Plan Viability**: Recovery plans executable within estimated timeframes
- **Integration Readiness**: Clear path back to standard workflow defined

**Language Guidelines:**
- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🚨 Emergency Recovery Workflow**: Recovery(99-1) → Issue Creation(99-2) → Sync Docs(99-3) → Retroactive Tests(99-4) → Validation(99-5) → Metadata Reconcile(99-6) → Final Review(99-7)

**🎨 Architecture**: Emergency Analysis → Recovery Planning → Execution Coordination → Quality Restoration
**🧪 Development**: Emergency-to-TDD workflow restoration
**🏗️ Design**: Gap Analysis, Priority Classification, Strategic Recovery
**📋 Requirements**: Git history analysis, document synchronization, test coverage restoration
**🔄 Evolution**: Seamless transition back to standard 00-16 workflow after recovery

> 📖 **Emergency Recovery System**: [99-X Series Commands](./README.md)
> 🗺️ **Current Position**: Emergency Recovery Analysis (99-1/99-7)
> 🎯 **Phase Purpose**: Analyze emergency changes and create comprehensive recovery plan
> ➡️ **Next Stage**: 99-2-create-retroactive-issue (Issue Creation) or specific recovery command

## 🎯 PHASE PURPOSE: EMERGENCY RECOVERY ANALYSIS

**⚠️ Important Notice:**
- **This step focuses on ANALYSIS AND PLANNING** - Examine emergency fixes and create recovery strategy
- **NO IMMEDIATE FIX IMPLEMENTATION** - Focus on understanding changes and planning restoration
- **Comprehensive assessment phase** - Identify gaps between current state and standard workflow
- **Create strategic recovery plan ONLY** - No code or document changes yet

**What this step does:**
1. `99-1-emergency-recovery-expert` ← **【YOU ARE HERE】Emergency fix analysis and recovery planning**
2. `99-2-create-retroactive-issue` ← Create missing GitHub issues
3. `99-3-sync-documentation` ← Sync docs with code changes
4. Then continue with test creation and validation cycle

**ANALYZE AND PLAN RECOVERY ONLY.**

## 📋 Lightweight Context Management

### Required Reading (Minimal)
```bash
# Project state (only if exists)
if [[ -f "docs/metadata/project-state.json" ]]; then
    PROJECT_STATE=$(cat docs/metadata/project-state.json)
    CURRENT_PHASE=$(echo $PROJECT_STATE | jq -r '.current_phase')
fi

# Execution history (latest 5 entries only)
RECENT_HISTORY=$(tail -5 .claude/context/execution-history.jsonl 2>/dev/null || echo "[]")

# Git commit history for emergency fix identification
GIT_LOG=$(git log --oneline -10 --no-merges 2>/dev/null || echo "No git history")
```

### GitHub Issue Integration
```bash
# Load GitHub issue with comments (if issue number provided)
if [[ -n "$ISSUE_NUMBER" ]]; then
    # Retrieve issue details
    gh issue view $ISSUE_NUMBER --json title,body,comments,updatedAt,createdAt
    
    # Priority: Recent comments are more important
    # Sort comments by created date (desc) and prioritize latest specifications
    gh issue view $ISSUE_NUMBER --json comments --jq '.comments | sort_by(.createdAt) | reverse'
fi
```

## 🚀 Expert Execution Flow

### Phase 1: Emergency Fix Analysis and Understanding
**Emergency Fix Analysis - Analyze as an expert:**

1. **Detailed Git History Analysis**
   - Check Points: Identify commits that bypassed standard workflows
   - Criteria: Presence of Given-When-Then scenario updates, test creation, issue creation
   
2. **Change Impact Scope Assessment**
   - Check Points: Range of changed files, functions, and business logic
   - Criteria: Impact level on domain layer, application layer, and infrastructure layer
   
3. **Process Deviation Measurement**
   - Check Points: Degree of deviation from TDD/DDD/Layered Architecture principles
   - Criteria: Compliance with test-first, domain-first, and layer separation approaches

**Technical Instructions for Analysis:**
```bash
# Analyze git commit history for emergency fixes
git log --oneline --since="7 days ago" --no-merges --grep="hotfix\|emergency\|urgent\|critical"

# Check for commits without corresponding test files
git log --name-only --since="7 days ago" --no-merges | grep -v "_test\|test_" | grep "\.py$\|\.js$\|\.java$"

# Identify documentation gaps
find docs/ -name "*.md" -mtime +7 -print
```

### Phase 2: Gap Analysis and Priority Setting
**Gap Analysis - Design as an expert:**

1. **Document-Code Gap**
   ```
   - Verify consistency of Given-When-Then scenarios
   - Validate alignment between domain model diagrams and code
   - Check currency of architecture documentation
   ```
   
2. **Test Coverage Analysis**
   ```
   - Calculate test coverage rate for emergency fix sections
   - Identify and classify missing test cases
   - Evaluate effectiveness of existing tests
   ```

**Technical Instructions for Gap Analysis:**
```bash
# Document-code consistency check
Read docs/use_cases/ directory contents
Read docs/domain/ directory contents
Compare with recent code changes

# Test coverage analysis
pytest --cov=. --cov-report=term-missing --quiet || echo "No test coverage data"
```

### Phase 3: Recovery Plan Formulation and Execution Instructions
**Recovery Planning - Execute as an expert:**

1. **Priority Classification System**
   - Action: 4-level classification (Critical/High/Medium/Low)
   - Expected Result: Work order determination based on business impact
   
2. **Recovery Timeline Creation**
   - Action: Estimate time required for each recovery task
   - Expected Result: Formulation of executable recovery plan

**Technical Instructions for Recovery Planning:**
```bash
# Create recovery plan document
Write recovery-action-plan.md with structured sections:
- Critical tasks (business impact)
- High priority tasks (quality impact)  
- Medium priority tasks (technical debt)
- Low priority tasks (nice-to-have)
```

## ✅ Built-in Quality Assurance

### Self-Diagnostic Checklist
**Required Items (MUST):**
- [ ] Complete git history analysis (identification of standard process bypasses)
- [ ] Document-code consistency evaluation completed
- [ ] Test coverage gap quantification completed
- [ ] Recovery task priority classification completed
- [ ] Executable recovery plan creation completed

**Recommended Items (SHOULD):**
- [ ] Technical debt impact assessment conducted
- [ ] Architecture principle compliance check performed
- [ ] Performance impact assessment conducted

### Quality Metrics
| Indicator | Target Value | Actual Value | Result |
|-----------|-------------|-------------|---------|
| Emergency Fix Detection Rate | 100% | [Actual] | ✅/❌ |
| Gap Analysis Completion Rate | 100% | [Actual] | ✅/❌ |
| Recovery Plan Feasibility | 95%+ | [Actual] | ✅/❌ |
| Priority Classification Accuracy | 90%+ | [Actual] | ✅/❌ |

### Error Handling
**Expected Errors and Solutions:**
1. **No Git History/Incomplete**: Manual change history verification and documentation
2. **Insufficient Documentation**: Reverse documentation from existing code
3. **Complex Conflict Situations**: Application of phased recovery approach

## 📊 Standardized Output Format

### 実行サマリー
- ✅ **緊急修正検出**: [検出件数]件の緊急修正を特定・分析完了
- ✅ **ギャップ分析**: [ギャップ数]箇所の文書-コード不整合を確認
- ⚠️ **復旧計画**: [優先度別タスク数] - Critical: X件, High: Y件, Medium: Z件

### 成果物
**作成されたファイル:**
- `emergency-recovery-report.md`: 緊急修正分析の詳細レポート
- `recovery-action-plan.md`: 優先度付き復旧アクションプラン

### 総合判定
**ステータス**: `SUCCESS`
**品質スコア**: [スコア]/100  
**次フェーズ準備**: `READY`

### 次のステップ
1. **即座に実行可能**: `/create-retroactive-issue` - 未作成のIssueを体系的に作成
2. **条件付き実行**: Critical優先度タスクから順次実行 → `/sync-documentation --type critical`
3. **要確認事項**: 複雑な競合が検出された場合は手動レビューが必要

### メタデータ更新
```json
{
  "command_executed": "99-1-emergency-recovery-expert",
  "timestamp": "[ISO-8601]",
  "status": "SUCCESS",
  "next_recommended": ["99-2-create-retroactive-issue", "99-3-sync-documentation"],
  "quality_score": 95,
  "emergency_fixes_detected": "[数]",
  "recovery_priority": "high"
}
```

## Common Errors and Solutions

### ❌ Error Case 1: No emergency fixes detected
**Cause**: Current branch has no changes that bypassed standard workflow  
**Solution**: 
- Check git log for recent commits outside standard process
- Verify you're on the correct branch with emergency fixes
- Run with `--branch` parameter to specify emergency fix branch

### ❌ Error Case 2: Multiple conflicting emergency fixes
**Cause**: Multiple overlapping emergency changes detected  
**Solution**: 
```bash
# Run analysis mode first to understand scope
/emergency-recovery-expert --mode analysis
# Then process individually with issue-specific recovery
/emergency-recovery-expert --issue <specific-issue> --mode partial
```

### ❌ Error Case 3: Standard workflow files missing
**Cause**: Project structure doesn't match expected TDD/DDD/Layered format  
**Solution**: First run standard initialization:
```bash
/init-project-structure
```

## Execution Examples

### ✅ Success Example - Full Recovery Analysis
```bash
$ /emergency-recovery-expert --mode full --branch hotfix/critical-bug
🚨 緊急対応復旧分析を開始します

📊 Git差分分析中...
  - 検出された緊急修正: 3件のコミット
  - 変更ファイル: src/payment.py, src/validation.py
  - 標準プロセス未実施箇所を特定

📋 ドキュメント整合性チェック中...
  ❌ Given-When-Thenシナリオ: payment-processing.md (未更新)
  ❌ ドメインモデル: domain-model.md (決済部分が未反映)
  ✅ メタデータ: project-state.json (最新)

🧪 テストカバレッジ分析中...
  ❌ 変更コードのテスト網羅率: 45% (標準: 80%以上)
  📝 不足テストケース: 12件特定

✅ 復旧計画生成完了!

📋 復旧アクションプラン (推定時間: 2.5時間)
==========================================
🔴 Critical (必須):
  1. Issue #234作成 - 決済処理緊急修正の文書化
  2. Given-When-Thenシナリオ更新 - payment-processing.md
  3. 不足テスト12件の作成と実行

🟡 High (推奨):
  4. ドメインモデル図の更新
  5. メタデータの整合性確認

🟢 Medium (任意):
  6. リファクタリング提案の検討

次のステップ: /create-retroactive-issue --commit a1b2c3d
```