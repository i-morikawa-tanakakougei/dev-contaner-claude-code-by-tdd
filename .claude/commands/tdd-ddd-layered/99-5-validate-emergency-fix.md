Use the 99-5-validate-emergency-fix subagent to validate emergency fixes against DDD principles and layered architecture standards. This command MUST USE PROACTIVELY the specialized 99-5-validate-emergency-fix subagent for optimal emergency fix validation.

**📖 Required Reading**: Before execution, this command MUST read the following files:
- `/workspace/.claude/context/current-command-context.json` - Current execution context
- `/workspace/.claude/context/project-context.json` - Overall project state and active sprint information
- `/workspace/docs/metadata/project-state.json` - Integrated project status for update

## Metadata
- **Prerequisites**: GitHub issue created, documentation synchronized, retroactive tests created
- **Input**: 
  - `<issue-number>` (required) - GitHub issue number for the emergency fix
  - `--strict` (optional) - Enable strict validation mode with detailed compliance checking
- **Output**: 
  - Emergency fix validation report
  - DDD compliance assessment
  - Layered architecture violation detection
  - Refactoring recommendations
  - Updated project metadata
- **Dependencies**: GitHub issue, synchronized documentation, completed retroactive tests
- **Execution Timing**: After retroactive test creation (99-4) and before metadata reconciliation

## 🎯 **TDD/DDD/LAYERED PROCESS CONTEXT**

**🚨 Emergency Recovery Workflow**: Recovery(99-1) → Issue Creation(99-2) → Sync Docs(99-3) → Retroactive Tests(99-4) → **Validation(99-5)** → Metadata Reconcile(99-6) → Final Review(99-7)

**🏗️ Validation Architecture**: Analyze→Assess→Report→Recommend  
**📋 Validation Requirements**: DDD compliance, layered architecture adherence, code quality assessment
**🔄 Integration**: Ensures emergency fixes maintain architectural integrity and code quality standards

> 📖 **Emergency Recovery System**: [99-X Series Commands](./README.md)  
> 🗺️ **Current Position**: Emergency Fix Validation (99-5/99-7)  
> 🎯 **Phase Purpose**: Validate emergency fixes against architectural and quality standards  
> ➡️ **Next Stage**: 99-6-reconcile-metadata (Metadata Reconciliation)

## 🎯 **PHASE PURPOSE: EMERGENCY FIX VALIDATION**

**⚠️ Important Notice:**
- **This step is VALIDATION ONLY** - Assess emergency fix quality and compliance
- **NO CODE CHANGES** - Focus on analysis and recommendations, not implementation  
- **Quality assurance phase** - Identify architectural violations and technical debt
- **Generate assessment reports ONLY** - Document findings and provide improvement recommendations

**What this step does:**
1. `99-4-retroactive-test` ← Create tests for emergency changes
2. `99-5-validate-emergency-fix` ← **【YOU ARE HERE】Validate emergency fix implementation**
3. `99-6-reconcile-metadata` ← Reconcile project metadata
4. Then continue with final review and completion

**VALIDATE EMERGENCY FIXES ONLY.**

## Common Errors and Solutions

### ❌ Error Case 1: Cannot access emergency fix code
**Cause**: Issue doesn't contain sufficient code reference or commits not found  
**Solution**: 
- Verify issue contains commit references: `gh issue view <issue-number>`
- Check git log for emergency fix commits: `git log --oneline --grep="fix\|emergency"`
- Link commits to issue manually if needed

### ❌ Error Case 2: Project lacks architectural standards
**Cause**: No established DDD or layered architecture documentation  
**Solution**: 
```bash
# Check for architectural documentation
find docs/ -name "*architecture*" -o -name "*domain*" -o -name "*layers*"
# Create basic architectural baseline if needed
/domain-modeling --baseline
```

### ❌ Error Case 3: Strict mode too restrictive
**Cause**: Strict validation mode flags acceptable emergency compromises  
**Solution**: 
```bash
# Run without strict mode first
/validate-emergency-fix <issue> 
# Review recommendations, then decide on strict compliance
/validate-emergency-fix <issue> --strict
```

## Execution Examples

### ✅ Success Example - Payment Validation Fix
```bash
$ /validate-emergency-fix 342 --strict
🔍 緊急修正検証を開始します (厳密モード)

📋 Issue #342 分析中...
  タイトル: "Emergency Fix: Payment validation null pointer exception"
  対象コミット: a1b2c3d, b2c3d4e
  変更ファイル: src/payment/validator.py, src/payment/models.py

🏗️ レイヤードアーキテクチャ検証中...
  ✅ ドメイン層 (src/payment/models.py):
    - Entity PaymentRequest: 適切な境界維持
    - Value Object Amount: 不変性保持
    - ドメインロジック: 外部依存なし
  
  ⚠️ アプリケーション層 (src/payment/validator.py):
    - PaymentValidator: インフラ層との結合検出
    - 推奨: バリデーションロジックをドメイン層に移動
  
  ✅ インフラストラクチャ層: 変更なし
  ✅ プレゼンテーション層: 変更なし

🎯 DDD原則適合性チェック中...
  ✅ ユビキタス言語: 一貫性維持
  ✅ 集約境界: 適切な分離
  ⚠️ ドメインサービス: 一部ビジネスロジックが流出
  ❌ 値オブジェクト: ValidationResult の不変性に問題

📊 コード品質評価中...
  ✅ 循環複雑度: 平均 3.2 (許容範囲)
  ✅ テストカバレッジ: 82% (目標達成)
  ⚠️ 依存関係: 2箇所でLayer違反の可能性
  ❌ SOLID原則: Single Responsibility Principle 違反 1件

🔄 技術的負債評価中...
  📈 新規技術的負債: Medium (2ポイント)
  📉 解決された技術的負債: Low (1ポイント)  
  📊 全体的影響: +1ポイント (注意が必要)

📝 検証レポート作成完了!

🎉 緊急修正検証完了!
================================

📊 総合評価: B+ (良好、一部改善推奨)
🎯 DDD適合度: 75% (改善余地あり)
🏗️ アーキテクチャ適合度: 80% (概ね良好)
📈 技術的負債影響: +1ポイント (軽微)

⚠️ 重要な推奨改善:
1. ValidationResult を不変な Value Object に修正
2. PaymentValidator のドメインロジックを Domain層に移動
3. Single Responsibility Principle 違反の解決

✅ 緊急性を考慮すると許容範囲内の実装
💡 次回スプリントでのリファクタリングを推奨

次のステップ: /reconcile-metadata --scope issue
```

### ✅ Success Example - Database Timeout Fix  
```bash
$ /validate-emergency-fix 343
🔍 インフラ系緊急修正の検証開始

📋 Issue #343 確認中...
  対象: Database connection timeout hotfix
  変更範囲: Infrastructure layer のみ

🏗️ アーキテクチャ影響分析中...
  ✅ インフラストラクチャ層の変更のみ
  ✅ 他の層への影響なし
  ✅ 依存関係の逆転原則維持

🎯 DDD原則チェック:
  ✅ ドメイン層: 影響なし
  ✅ 境界維持: 適切
  ✅ 技術的関心の分離: 良好

📊 品質評価: A (優良)
💡 推奨改善: なし（適切な緊急対応）

✅ 検証完了 - 優れた緊急対応実装!
```

## 📋 **EMERGENCY FIX VALIDATION TASK CHECKLIST**

**Use this checklist for comprehensive emergency fix validation:**

### 🔴 Required Tasks

#### **🏗️ Layered Architecture Validation**
- [ ] **Layer separation check**: Verify emergency changes maintain proper layer boundaries
- [ ] **Dependency direction**: Ensure dependencies flow in correct direction (UI→App→Domain→Infra)
- [ ] **Layer responsibility**: Confirm each layer maintains its designated responsibilities

#### **🎯 DDD Compliance Assessment**
- [ ] **Entity integrity**: Verify entities maintain identity and business rules
- [ ] **Value object immutability**: Check value objects remain immutable and consistent
- [ ] **Aggregate boundaries**: Ensure aggregates maintain transactional consistency

#### **📊 Code Quality Analysis**
- [ ] **Complexity metrics**: Measure cyclomatic complexity and maintainability
- [ ] **SOLID principles**: Check adherence to Single Responsibility, Open/Closed, etc.
- [ ] **Test coverage impact**: Verify test coverage meets quality standards

### 🟡 Recommended Tasks

#### **🔄 Technical Debt Assessment**
- [ ] **New debt introduction**: Identify technical debt created by emergency fix
- [ ] **Debt resolution tracking**: Note any existing debt that was resolved
- [ ] **Impact prioritization**: Assess severity and urgency of identified issues

#### **📝 Documentation and Compliance**
- [ ] **Architectural documentation**: Verify changes align with documented architecture
- [ ] **Coding standards**: Check adherence to project coding standards
- [ ] **Security implications**: Assess any security considerations from emergency changes

### 🟢 Optional Tasks

#### **📈 Advanced Quality Metrics**
- [ ] **Performance impact**: Analyze potential performance implications
- [ ] **Security vulnerability scan**: Check for introduced security risks
- [ ] **Maintainability assessment**: Evaluate long-term maintainability impact

#### **💡 Improvement Recommendations**
- [ ] **Refactoring suggestions**: Provide specific improvement recommendations
- [ ] **Best practices guidance**: Suggest alignment with established best practices
- [ ] **Future prevention**: Recommend process improvements to prevent similar issues

**💡 Pro Tip**: Use strict mode for critical systems, but be pragmatic about emergency fix constraints!

## Task Details

**🤖 Agent Integration**: This command MUST USE PROACTIVELY the specialized `99-5-validate-emergency-fix` subagent for optimal emergency fix validation. Claude Code should automatically delegate this task to the 99-5-validate-emergency-fix subagent based on the command description.

## 📖 Subagent Document Reading Instructions

This command delegates to the specialized `99-5-validate-emergency-fix` subagent.

**MANDATORY: The subagent MUST read these files before execution:**

1. Source code files modified in the emergency fix (from GitHub issue)
2. `docs/vision/project-vision.md` - Project architectural principles (if exists)
3. `docs/domain/` - Domain model documentation for DDD compliance checking
4. `/workspace/.claude/context/current-command-context.json` - Current execution context
5. `/workspace/docs/metadata/project-state.json` - Project status and quality metrics
6. Existing test files to understand current coverage and quality

**Command-Specific Reading Focus - Emergency Fix Validation:**
- Read GitHub issue to identify specific code changes made in emergency fix
- Analyze modified source code for architectural and DDD principle compliance
- Review project documentation to understand established architectural standards
- Check test coverage and quality metrics to assess validation completeness

**CRITICAL:** Use the Read tool to actually read file contents, not just reference paths.

## サブエージェント実行指示

このコマンドはサブエージェント `99-5-validate-emergency-fix` を呼び出します。

**サブエージェントに対する明示的指示**:
- 実行開始前に以下のファイルを必ず読み込んでください:
  1. 緊急修正されたソースコード - 変更内容の詳細分析
  2. プロジェクトアーキテクチャ文書 - 標準との適合性確認
  3. ドメインモデル文書 - DDD原則との整合性チェック
  4. `/workspace/docs/metadata/project-state.json` - プロジェクト品質基準
  
**重要**: リンクや参照だけでなく、実際にRead toolを使用してファイル内容を読み込むこと

Follow these steps:

1. **Pre-execution Validation**:
   ```bash
   # Validate required parameters
   issue_number=""
   strict_mode=false
   
   # Parse arguments
   if [[ $# -lt 1 ]]; then
       echo "❌ Issue number is required"
       echo "Usage: /validate-emergency-fix <issue-number> [--strict]"
       exit 1
   fi
   
   issue_number="$1"
   shift
   
   while [[ $# -gt 0 ]]; do
       case $1 in
           --strict)
               strict_mode=true
               shift
               ;;
           *)
               echo "⚠️ Unknown parameter: $1"
               echo "Usage: /validate-emergency-fix <issue-number> [--strict]"
               exit 1
               ;;
       esac
   done
   
   # Validate GitHub CLI and issue
   if command -v gh &> /dev/null; then
       if ! gh issue view "$issue_number" >/dev/null 2>&1; then
           echo "❌ GitHub issue #$issue_number not found or not accessible"
           exit 1
       fi
   else
       echo "⚠️ GitHub CLI not found. Issue information may be limited."
   fi
   
   echo "🔍 緊急修正検証を開始します (Issue: #$issue_number$([ "$strict_mode" = true ] && echo ", 厳密モード" || echo ""))"
   ```

2. **Context Preparation and Agent Execution**:
   ```bash
   # 🔄 Prepare context for emergency fix validation agent
   echo "📋 緊急修正分析と検証コンテキスト準備..."
   
   # Extract issue information if GitHub CLI is available
   issue_title=""
   issue_body=""
   if command -v gh &> /dev/null; then
       issue_title=$(gh issue view "$issue_number" --json title -q '.title' 2>/dev/null || echo "")
       issue_body=$(gh issue view "$issue_number" --json body -q '.body' 2>/dev/null || echo "")
   fi
   
   # Detect project architecture documentation
   arch_docs=""
   if [[ -d "docs/architecture" ]]; then
       arch_docs="docs/architecture"
   elif [[ -d "docs/domain" ]]; then
       arch_docs="docs/domain"
   elif [[ -f "docs/vision/project-vision.md" ]]; then
       arch_docs="docs/vision"
   fi
   
   # Create context file
   context_file="/workspace/.claude/context/current-command-context.json"
   current_time=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
   
   # Build context JSON for emergency fix validation
   cat > "$context_file" <<EOF
   {
     "command": "validate-emergency-fix",
     "timestamp": "$current_time",
     "issue_number": "$issue_number",
     "strict_mode": $strict_mode,
     "phase": "emergency-fix-validation",
     "issue_info": {
       "title": "$issue_title",
       "body": "$issue_body"
     },
     "architecture_docs": "$arch_docs",
     "context": {
       "git_repo": "true",
       "validation_focus": "architecture_compliance",
       "expected_outputs": [
         "validation_report",
         "compliance_assessment", 
         "refactoring_recommendations"
       ],
       "validation_areas": ["layered_architecture", "ddd_principles", "code_quality", "technical_debt"]
     },
     "additional_instructions": "緊急修正されたコードを分析し、DDD原則とレイヤードアーキテクチャの適合性を検証してください。",
     "special_considerations": [
       "Issue内容からの緊急修正範囲特定",
       "レイヤードアーキテクチャ境界の検証", 
       "DDD原則（Entity、Value Object、Aggregate）への適合性確認",
       "SOLID原則とコード品質の評価",
       "技術的負債の影響評価"
     ],
     "custom_context": {
       "emergency_recovery": true,
       "architecture_validation": "high",
       "compliance_reporting": true
     }
   }
   EOF
   
   echo "✅ 緊急修正検証コンテキストファイル作成完了: $context_file"
   
   # 🤖 Call the specialized emergency fix validation agent
   echo ""
   echo "🔍 緊急修正検証エージェントを起動します..."
   echo "専門エージェントが緊急修正のアーキテクチャ適合性を検証します"
   echo ""
   
   # Task tool execution with comprehensive prompt
   task_prompt="Execute the task.

## CRITICAL: Subagent Specification Reference
As a fallback mechanism in case the specialized subagent 99-5-validate-emergency-fix is not properly invoked:
- MUST READ: /workspace/.claude/agents/99-5-validate-emergency-fix.md
- Follow the specifications and requirements defined in this agent file
- Implement the exact same process and standards as defined in the subagent specification
- Ensure standardized output format compliance as specified in the agent document

## Context Information Gathering
1. Emergency Recovery Context:
   - Read /workspace/.claude/context/current-command-context.json

2. Emergency Fix Analysis:
   - Read GitHub issue details for emergency fix
   - Analyze modified source code files
   - Review existing architectural documentation

## Task Execution
1. Emergency fix scope and impact identification
2. Layered architecture compliance validation
3. DDD principles adherence assessment
4. Code quality and SOLID principles evaluation
5. Technical debt impact analysis
6. Comprehensive validation report generation

## IMPORTANT: Standardized Output Format Compliance
Report MUST end with the following structured sections:

### 📊 Execution Summary
Mark completion status of each critical task with ✅/❌

### 📋 Overall Assessment
Provide comprehensive emergency fix validation results and compliance ratings

### 💡 Next Steps
List specific follow-up actions and improvement recommendations

## Post-Processing
- Generate validation report with architectural compliance assessment
- Provide DDD principle compliance evaluation
- Offer refactoring recommendations and improvement suggestions
- Guide next steps in emergency recovery process"

   # Execute with specialized 99-5-validate-emergency-fix subagent
   # The 99-5-validate-emergency-fix subagent will be automatically invoked based on the task description
   
   agent_exit_code=$?
   echo "✅ 専用エージェント実行完了 (終了コード: $agent_exit_code)"
   ```

3. **Agent Result Verification**:
   ```bash
   # 🔍 Verify emergency fix validation results
   echo "🔍 緊急修正検証結果を検証中..."
   
   # Check for generated validation report
   validation_files=("validation-report.md" "emergency-fix-validation.md" "compliance-assessment.md")
   found_reports=()
   
   for report in "${validation_files[@]}"; do
       if [[ -f "$report" ]]; then
           found_reports+=("$report")
       fi
   done
   
   if [[ ${#found_reports[@]} -gt 0 ]]; then
       echo "📊 生成された検証レポート:"
       for report in "${found_reports[@]}"; do
           echo "   ✅ $report"
       done
   else
       echo "💡 標準的な検証レポートファイルが見つかりませんでした（別の形式で出力された可能性）"
   fi
   
   echo "✅ 緊急修正検証結果検証完了"
   
   # Clean up context file after successful execution
   if [[ -f "$context_file" ]]; then
       # Archive context to execution history
       echo "{\"timestamp\":\"$(date -Iseconds)\",\"command\":\"validate-emergency-fix\",\"issue\":\"$issue_number\",\"strict_mode\":$strict_mode,\"status\":\"completed\"}" >> /workspace/.claude/context/execution-history.jsonl
       rm -f "$context_file"
       echo "📝 コンテキストを実行履歴に記録し、一時ファイルをクリーンアップしました"
   fi
   ```

4. **Display Validation Summary**:
   ```bash
   # 📊 Display comprehensive validation summary
   echo ""
   echo "🎉 緊急修正検証完了!"
   echo "======================"
   
   echo "📋 検証情報:"
   echo "   🎫 Issue: #$issue_number"
   if [[ -n "$issue_title" ]]; then
       echo "   📝 タイトル: $issue_title"
   fi
   echo "   🔍 検証モード: $([ "$strict_mode" = true ] && echo "厳密" || echo "標準")"
   echo "   📁 アーキテクチャ文書: $arch_docs"
   
   # Show generated validation reports
   if [[ ${#found_reports[@]} -gt 0 ]]; then
       echo ""
       echo "📊 生成された検証レポート:"
       for report in "${found_reports[@]}"; do
           echo "   📄 $report"
       done
   fi
   
   echo ""
   echo "📋 推奨次のステップ:"
   echo "   1. 検証レポート確認: 生成されたレポートを詳細確認"
   echo "   2. 改善項目の検討: 推奨される改善点の優先順位付け"
   echo "   3. メタデータ調整: /reconcile-metadata --scope issue"
   echo "   4. 最終レビュー: /review-emergency-recovery --issue $issue_number"
   
   echo ""
   echo "💡 補足情報:"
   echo "   - 検証結果に基づいて次回スプリントでの改善を検討してください"
   echo "   - Critical項目がある場合は早急な対応を検討してください"
   echo "   - 技術的負債が増加した場合は返済計画を立ててください"
   echo ""
   echo "✅ 緊急修正検証完了 - アーキテクチャ適合性の評価が完了しました!"
   ```

## 🔄 **PHASE 3: ENHANCED INTEGRATION CAPABILITIES**

### **Critical Enhancement Features**
This command implements Phase 3 advanced emergency fix validation capabilities:

1. **Intelligent Architectural Compliance Analysis with Multi-layer Validation**
2. **Automated DDD Principle Assessment with Domain Boundary Verification** 
3. **Smart Technical Debt Impact Analysis with Priority-based Recommendations**
4. **Enhanced Code Quality Metrics with SOLID Principle Validation**

### **Project State Updates**

**CRITICAL**: After successful emergency fix validation, MUST update integrated project metadata:

1. **Project State Update**:
   ```bash
   # Update docs/metadata/project-state.json
   # - Update code_quality_metrics.validation_results
   # - Set technical_debt_metrics.emergency_fix_impact
   # - Update architecture_compliance_score
   # - Add to recent_activity.last_command_executed
   ```

2. **Project Context Update**:
   ```bash
   # Update .claude/context/project-context.json  
   # - Add validation_results to emergency_recovery_status
   # - Set current_state.last_command and last_command_timestamp
   # - Update architecture_compliance.last_validation_timestamp
   ```

**⚠️ Error Handling**: If emergency fix validation fails:
- 📖 Consult: [Manual Sync Guide](../../docs/maintenance/manual-sync-guide.md)
- 🔄 Check Status: `/use-case-status` for current project state  
- 🔍 Manual Review: Perform manual architectural review and document findings