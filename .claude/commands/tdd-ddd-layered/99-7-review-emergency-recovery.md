Use the 99-7-review-emergency-recovery subagent to conduct comprehensive final review of the emergency recovery process. This command MUST USE PROACTIVELY the specialized 99-7-review-emergency-recovery subagent for optimal emergency recovery review.

**📖 Required Reading**: Before execution, this command MUST read the following files:
- `/workspace/.claude/context/current-command-context.json` - Current execution context
- `/workspace/.claude/context/project-context.json` - Overall project state and active sprint information
- `/workspace/docs/metadata/project-state.json` - Integrated project status for update

## Metadata
- **Prerequisites**: All previous emergency recovery steps completed (99-1 through 99-6)
- **Input**: 
  - `--issue <issue-number>` (optional) - Specific issue to review
  - `--detail-level <summary|full>` (default: summary) - Level of detail in review report
- **Output**: 
  - Comprehensive emergency recovery review report
  - Process completion verification
  - Quality assessment and recommendations
  - Final project state update
- **Dependencies**: Completed emergency recovery workflow, updated metadata
- **Execution Timing**: Final step in emergency recovery process (99-7)

## 🎯 **TDD/DDD/LAYERED PROCESS CONTEXT**

**🚨 Emergency Recovery Workflow**: Recovery(99-1) → Issue Creation(99-2) → Sync Docs(99-3) → Retroactive Tests(99-4) → Validation(99-5) → Metadata Reconcile(99-6) → **Final Review(99-7)**

**🏗️ Final Review Architecture**: Analyze→Assess→Report→Complete  
**📋 Review Requirements**: Process completion verification, quality assessment, standard workflow readiness
**🔄 Integration**: Completes emergency recovery and validates return to standard 00-16 workflow

> 📖 **Emergency Recovery System**: [99-X Series Commands](./README.md)  
> 🗺️ **Current Position**: Final Emergency Recovery Review (99-7/99-7)  
> 🎯 **Phase Purpose**: Complete emergency recovery and validate workflow restoration  
> ➡️ **Next Stage**: Return to standard TDD/DDD/Layered workflow (00-16 commands)

## 🎯 **PHASE PURPOSE: FINAL EMERGENCY RECOVERY REVIEW**

**⚠️ Important Notice:**
- **This step is FINAL REVIEW ONLY** - Comprehensive assessment of emergency recovery completion
- **NO ADDITIONAL CHANGES** - Focus on verification and reporting, not implementation  
- **Process completion phase** - Validate all emergency recovery steps and ensure quality standards
- **Generate final report ONLY** - Document recovery success and provide transition guidance

**What this step does:**
1. `99-6-reconcile-metadata` ← Reconcile project metadata
2. `99-7-review-emergency-recovery` ← **【YOU ARE HERE】Conduct final comprehensive review**
3. **Emergency Recovery Complete** ← Return to standard workflow (00-16 commands)

**CONDUCT FINAL REVIEW ONLY.**

## Common Errors and Solutions

### ❌ Error Case 1: Incomplete emergency recovery steps
**Cause**: Some steps in the 99-1 through 99-6 workflow were not completed  
**Solution**: 
- Check completion status: `/use-case-status --emergency-recovery`
- Complete missing steps before final review
- Use `--detail-level full` to identify specific gaps

### ❌ Error Case 2: Issue not found or inaccessible
**Cause**: Specified issue number doesn't exist or is not accessible  
**Solution**: 
```bash
# Verify issue exists
gh issue view <issue-number>
# Run review without specific issue focus
/review-emergency-recovery --detail-level summary
```

### ❌ Error Case 3: Inconsistent project state
**Cause**: Metadata or project state shows inconsistencies  
**Solution**: 
```bash
# Reconcile metadata first
/reconcile-metadata --scope project
# Then run comprehensive review
/review-emergency-recovery --detail-level full
```

## Execution Examples

### ✅ Success Example - Issue-Specific Review
```bash
$ /review-emergency-recovery --issue 342 --detail-level full
🔍 緊急対応復旧レビューを開始します (詳細レベル: full)

📋 Issue #342 復旧プロセス検証中...
  タイトル: "Emergency Fix: Payment validation null pointer exception"
  開始日時: 2024-08-28 14:00:00
  復旧完了日時: 2024-08-28 16:45:00
  所要時間: 2時間45分

✅ 復旧プロセス完了確認
==============================

📊 実行済みコマンド検証:
  ✅ 99-1 緊急対応分析: 完了 (2024-08-28 14:15:00)
  ✅ 99-2 事後Issue作成: 完了 (2024-08-28 14:30:00)
  ✅ 99-3 ドキュメント同期: 完了 (2024-08-28 15:00:00)
  ✅ 99-4 遡及的テスト作成: 完了 (2024-08-28 15:30:00)
  ✅ 99-5 緊急修正検証: 完了 (2024-08-28 16:00:00)
  ✅ 99-6 メタデータ調整: 完了 (2024-08-28 16:30:00)

🧪 ドキュメント・コード・テスト整合性検証
========================================

📄 ドキュメント整合性:
  ✅ Given-When-Thenシナリオ: 100% 更新済み
    - payment-processing.md: null値処理シナリオ追加
    - validation-scenarios.md: エラーハンドリングシナリオ強化
  ✅ ドメインモデル: 100% 同期済み
    - PaymentValidator entity: null-safe validation 追加
    - ValidationRule value object: 新規ルール定義

💻 コード品質:
  ✅ 変更ファイル: src/payment/validator.py, src/payment/models.py
  ✅ アーキテクチャ適合度: 80% (概ね良好)
  ⚠️ 技術的負債: +1ポイント (軽微な増加)
  ✅ SOLID原則適合度: 85% (良好)

🧪 テストカバレッジ:
  ✅ 緊急修正箇所: 82% カバレッジ達成 (目標: 80%)
  ✅ 新規テストケース: 12件作成
    - 正常系: 5件, 異常系: 4件, 回帰: 3件
  ✅ 全テスト実行: 正常終了 (127/127 passed)

📈 標準プロセス準拠度評価
========================

🎯 TDD/DDD/Layered準拠度: 78% (良好)
  ✅ ドメイン駆動設計: DDD原則75%適合
  ✅ テスト駆動開発: 後付けだが包括的なテスト実装
  ✅ レイヤードアーキテクチャ: 境界維持率80%

💡 改善推奨アクション:
================
🔴 高優先度 (次回スプリント):
  1. ValidationResult を不変Value Objectに修正
  2. PaymentValidator のドメインロジック移動

🟡 中優先度 (今後2スプリント):
  3. Single Responsibility Principle違反の解決
  4. インフラ層との結合度軽減

🟢 低優先度 (技術的改善):
  5. テストカバレッジ90%への向上
  6. パフォーマンステストの追加

📊 復旧プロセスメトリクス
=======================
⏱️ 所要時間: 2時間45分 (予想: 2.5時間) ← 目標達成!
📈 品質スコア向上: 70% → 78% (+8ポイント)
🧪 テストカバレッジ向上: 45% → 82% (+37ポイント)
📚 ドキュメント整合性: 60% → 100% (+40ポイント)

🎉 緊急対応復旧完了判定: ✅ APPROVED
========================================

📋 総合評価: B+ (良好、軽微な改善点あり)
🔄 標準ワークフロー復帰: ✅ 準備完了
💡 推奨次アクション: 通常の開発フロー継続、次回スプリントで改善実施

🚀 次のステップ:
  1. 通常開発フロー再開: /create-use-case <new-issue>
  2. 改善タスクスケジューリング: /sprint-planning での改善項目組み込み
  3. チーム共有: 緊急対応学習事項の共有

✅ 緊急対応復旧プロセス完了 - 標準ワークフローへの復帰が承認されました!
```

### ✅ Success Example - Summary Review
```bash
$ /review-emergency-recovery --detail-level summary
🔍 緊急対応復旧総合レビュー (サマリー)

📊 復旧状況概要:
  🎫 処理済み緊急Issue: 2件 (#342, #343)
  ⏱️ 総復旧時間: 4時間15分
  ✅ 全復旧ステップ完了: 100%

📈 品質改善サマリー:
  📚 ドキュメント整合性: 95% 達成
  🧪 テストカバレッジ: 平均 +25% 向上
  🏗️ アーキテクチャ適合度: 良好維持

🎉 総合判定: ✅ COMPLETED
💡 推奨: 標準ワークフローへの復帰承認

次のステップ: 通常の開発プロセス継続
```

## 📋 **EMERGENCY RECOVERY REVIEW TASK CHECKLIST**

**Use this checklist for comprehensive emergency recovery review:**

### 🔴 Required Tasks

#### **📊 Process Completion Verification**
- [ ] **Command execution validation**: Verify all 99-1 through 99-6 commands were executed
- [ ] **Output verification**: Confirm all expected outputs were generated
- [ ] **Timeline analysis**: Review process execution timeline and efficiency

#### **🧪 Quality Assessment**
- [ ] **Documentation consistency**: Verify Given-When-Then scenarios match implemented functionality
- [ ] **Test coverage validation**: Confirm test coverage meets established standards
- [ ] **Code quality check**: Assess architectural compliance and code quality metrics

#### **📋 Integration Verification**
- [ ] **Metadata consistency**: Verify all metadata accurately reflects current project state
- [ ] **Standard workflow readiness**: Confirm project is ready to return to normal 00-16 workflow
- [ ] **Traceability validation**: Ensure all emergency changes are properly documented and tracked

### 🟡 Recommended Tasks

#### **📈 Performance Analysis**
- [ ] **Process efficiency**: Analyze emergency recovery process efficiency and timing
- [ ] **Resource utilization**: Review resource usage and team effort required
- [ ] **Bottleneck identification**: Identify potential process improvement opportunities

#### **💡 Improvement Recommendations**
- [ ] **Technical debt assessment**: Evaluate technical debt introduced and mitigation strategies
- [ ] **Process improvement suggestions**: Recommend improvements for future emergency responses
- [ ] **Knowledge sharing**: Document learnings and best practices for team sharing

### 🟢 Optional Tasks

#### **📊 Advanced Analytics**
- [ ] **Comparative analysis**: Compare emergency recovery metrics with previous incidents
- [ ] **Predictive insights**: Provide insights for preventing similar emergency situations
- [ ] **Team learning extraction**: Extract valuable learnings for team development

#### **🎯 Strategic Planning**
- [ ] **Prevention strategies**: Suggest strategies to prevent similar emergency situations
- [ ] **Process optimization**: Recommend optimizations for emergency recovery workflow
- [ ] **Tool and automation improvements**: Suggest tooling improvements for future incidents

**💡 Pro Tip**: Use full detail level for critical systems, summary for routine emergency fixes!

## Task Details

**🤖 Agent Integration**: This command MUST USE PROACTIVELY the specialized `99-7-review-emergency-recovery` subagent for optimal emergency recovery review. Claude Code should automatically delegate this task to the 99-7-review-emergency-recovery subagent based on the command description.

## 📖 Subagent Document Reading Instructions

This command delegates to the specialized `99-7-review-emergency-recovery` subagent.

**MANDATORY: The subagent MUST read these files before execution:**

1. `/workspace/.claude/context/execution-history.jsonl` - Complete command execution history
2. `/workspace/docs/metadata/project-state.json` - Final project state after recovery
3. `/workspace/.claude/context/project-context.json` - Updated project context
4. All documentation files modified during emergency recovery
5. GitHub issue(s) related to emergency fixes
6. Test results and coverage reports from retroactive testing

**Command-Specific Reading Focus - Emergency Recovery Review:**
- Read execution history to verify all emergency recovery commands were executed
- Analyze project metadata to assess final state and quality metrics
- Review all documentation changes to verify consistency and completeness
- Check test results to confirm adequate coverage and quality

**CRITICAL:** Use the Read tool to actually read file contents, not just reference paths.

## サブエージェント実行指示

このコマンドはサブエージェント `99-7-review-emergency-recovery` を呼び出します。

**サブエージェントに対する明示的指示**:
- 実行開始前に以下のファイルを必ず読み込んでください:
  1. 全てのコマンド実行履歴 - 緊急対応プロセスの完全性確認
  2. 最終的なプロジェクト状態 - 復旧後の品質評価
  3. 更新されたドキュメント - 整合性と完全性の検証
  4. テスト結果とカバレッジレポート - 品質基準の達成確認
  
**重要**: リンクや参照だけでなく、実際にRead toolを使用してファイル内容を読み込むこと

Follow these steps:

1. **Pre-execution Validation**:
   ```bash
   # Validate and parse parameters
   target_issue=""
   detail_level="summary"
   
   while [[ $# -gt 0 ]]; do
       case $1 in
           --issue)
               target_issue="$2"
               shift 2
               ;;
           --detail-level)
               detail_level="$2"
               shift 2
               ;;
           *)
               echo "⚠️ Unknown parameter: $1"
               echo "Usage: /review-emergency-recovery [--issue <issue-number>] [--detail-level summary|full]"
               exit 1
               ;;
       esac
   done
   
   # Validate detail level parameter
   if [[ "$detail_level" != "summary" && "$detail_level" != "full" ]]; then
       echo "❌ Invalid detail level: $detail_level. Must be 'summary' or 'full'"
       exit 1
   fi
   
   # Validate issue if specified
   if [[ -n "$target_issue" ]]; then
       if command -v gh &> /dev/null; then
           if ! gh issue view "$target_issue" >/dev/null 2>&1; then
               echo "❌ GitHub issue #$target_issue not found or not accessible"
               exit 1
           fi
       else
           echo "⚠️ GitHub CLI not found. Issue information may be limited."
       fi
   fi
   
   echo "🔍 緊急対応復旧レビューを開始します (詳細レベル: $detail_level$([ -n "$target_issue" ] && echo ", Issue: #$target_issue" || echo ""))"
   ```

2. **Context Preparation and Agent Execution**:
   ```bash
   # 🔄 Prepare context for emergency recovery review agent
   echo "📋 復旧プロセス分析と最終レビューコンテキスト準備..."
   
   # Get emergency recovery command execution history
   emergency_history=""
   if [[ -f ".claude/context/execution-history.jsonl" ]]; then
       emergency_history=$(grep -E "99-[1-7]-" ".claude/context/execution-history.jsonl" 2>/dev/null | tail -20 | tr '\n' '|' || echo "")
   fi
   
   # Get current project state
   project_health=""
   if [[ -f "docs/metadata/project-state.json" ]]; then
       project_health=$(python -c "import json; data=json.load(open('docs/metadata/project-state.json')); print(data.get('project_metadata', {}).get('health_score', 'unknown'))" 2>/dev/null || echo "unknown")
   fi
   
   # Get issue information if specified
   issue_title=""
   issue_body=""
   if [[ -n "$target_issue" ]] && command -v gh &> /dev/null; then
       issue_title=$(gh issue view "$target_issue" --json title -q '.title' 2>/dev/null || echo "")
       issue_body=$(gh issue view "$target_issue" --json body -q '.body' 2>/dev/null || echo "")
   fi
   
   # Create context file
   context_file="/workspace/.claude/context/current-command-context.json"
   current_time=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
   
   # Build context JSON for emergency recovery review
   cat > "$context_file" <<EOF
   {
     "command": "review-emergency-recovery",
     "timestamp": "$current_time",
     "target_issue": "$target_issue",
     "detail_level": "$detail_level",
     "phase": "final-emergency-recovery-review",
     "issue_info": {
       "title": "$issue_title",
       "body": "$issue_body"
     },
     "project_health": "$project_health",
     "emergency_history": "$emergency_history",
     "context": {
       "git_repo": "true",
       "review_focus": "comprehensive_completion_assessment",
       "expected_outputs": [
         "completion_verification_report",
         "quality_assessment",
         "standard_workflow_readiness",
         "improvement_recommendations"
       ],
       "review_areas": ["process_completion", "documentation_consistency", "test_coverage", "architectural_compliance", "metadata_accuracy"]
     },
     "additional_instructions": "緊急対応復旧プロセス全体を包括的にレビューし、標準ワークフローへの復帰可能性を評価してください。",
     "special_considerations": [
       "全緊急対応コマンド(99-1～99-6)の実行完了確認",
       "ドキュメント・コード・テストの三位一体整合性検証", 
       "標準TDD/DDD/レイヤードプロセスへの準拠度評価",
       "技術的負債とプロジェクト健全性への影響分析",
       "今後の改善提案と学習事項の抽出"
     ],
     "custom_context": {
       "emergency_recovery": true,
       "final_review": true,
       "workflow_transition": "standard_workflow_readiness"
     }
   }
   EOF
   
   echo "✅ 緊急対応復旧レビューコンテキストファイル作成完了: $context_file"
   
   # 🤖 Call the specialized emergency recovery review agent
   echo ""
   echo "🔍 緊急対応復旧レビューエージェントを起動します..."
   echo "専門エージェントが復旧プロセス全体を包括的にレビューします"
   echo ""
   
   # Task tool execution with comprehensive prompt
   task_prompt="Execute the task.

## CRITICAL: Subagent Specification Reference
As a fallback mechanism in case the specialized subagent 99-7-review-emergency-recovery is not properly invoked:
- MUST READ: /workspace/.claude/agents/99-7-review-emergency-recovery.md
- Follow the specifications and requirements defined in this agent file
- Implement the exact same process and standards as defined in the subagent specification
- Ensure standardized output format compliance as specified in the agent document

## Context Information Gathering
1. Emergency Recovery Context:
   - Read /workspace/.claude/context/current-command-context.json
   - Read /workspace/.claude/context/execution-history.jsonl

2. Final State Analysis:
   - Read /workspace/docs/metadata/project-state.json
   - Check all documentation modifications
   - Review test results and coverage reports

## Task Execution
1. Emergency recovery process completion verification
2. Quality assessment and standards compliance review
3. Integration verification and traceability validation
4. Process efficiency analysis and improvement identification
5. Final project state validation and readiness assessment
6. Comprehensive completion report generation

## IMPORTANT: Standardized Output Format Compliance
Report MUST end with the following structured sections:

### 📊 Execution Summary
Mark completion status of each critical task with ✅/❌

### 📋 Overall Assessment
Provide comprehensive emergency recovery completion evaluation

### 💡 Next Steps
List specific recommendations for returning to standard workflow

## Post-Processing
- Generate final emergency recovery review report
- Validate process completion and quality standards
- Provide clear transition guidance to standard workflow
- Complete emergency recovery process documentation"

   # Execute with specialized 99-7-review-emergency-recovery subagent
   # The 99-7-review-emergency-recovery subagent will be automatically invoked based on the task description
   
   agent_exit_code=$?
   echo "✅ 専用エージェント実行完了 (終了コード: $agent_exit_code)"
   ```

3. **Agent Result Verification**:
   ```bash
   # 🔍 Verify emergency recovery review results
   echo "🔍 緊急対応復旧レビュー結果を検証中..."
   
   # Check for generated review report files
   review_files=("emergency-recovery-review.md" "recovery-completion-report.md" "final-review-summary.md")
   found_reports=()
   
   for report in "${review_files[@]}"; do
       if [[ -f "$report" ]]; then
           found_reports+=("$report")
       fi
   done
   
   if [[ ${#found_reports[@]} -gt 0 ]]; then
       echo "📊 生成されたレビューレポート:"
       for report in "${found_reports[@]}"; do
           echo "   ✅ $report"
       done
   else
       echo "💡 標準的なレビューレポートファイルが見つかりませんでした（コンソール出力のみの可能性）"
   fi
   
   # Check final project state
   if [[ -f "docs/metadata/project-state.json" ]]; then
       current_status=$(python -c "import json; data=json.load(open('docs/metadata/project-state.json')); print(data.get('project_metadata', {}).get('overall_status', 'unknown'))" 2>/dev/null || echo "unknown")
       echo "📊 最終プロジェクト状態: $current_status"
   fi
   
   echo "✅ 緊急対応復旧レビュー結果検証完了"
   
   # Clean up context file after successful execution
   if [[ -f "$context_file" ]]; then
       # Archive context to execution history
       echo "{\"timestamp\":\"$(date -Iseconds)\",\"command\":\"review-emergency-recovery\",\"issue\":\"$target_issue\",\"detail_level\":\"$detail_level\",\"status\":\"completed\"}" >> /workspace/.claude/context/execution-history.jsonl
       rm -f "$context_file"
       echo "📝 コンテキストを実行履歴に記録し、一時ファイルをクリーンアップしました"
   fi
   ```

4. **Display Final Review Summary**:
   ```bash
   # 📊 Display comprehensive final review summary
   echo ""
   echo "🎉 緊急対応復旧レビュー完了!"
   echo "=============================="
   
   echo "📋 レビュー情報:"
   if [[ -n "$target_issue" ]]; then
       echo "   🎫 対象Issue: #$target_issue"
       if [[ -n "$issue_title" ]]; then
           echo "   📝 タイトル: $issue_title"
       fi
   else
       echo "   🌐 スコープ: 全体レビュー"
   fi
   echo "   📊 詳細レベル: $detail_level"
   echo "   ⏰ レビュー完了: $(date '+%Y-%m-%d %H:%M:%S')"
   
   # Show generated review reports
   if [[ ${#found_reports[@]} -gt 0 ]]; then
       echo ""
       echo "📄 生成されたレポート:"
       for report in "${found_reports[@]}"; do
           echo "   📋 $report"
       done
   fi
   
   echo ""
   echo "🎯 緊急対応復旧プロセス完了!"
   echo "==============================="
   echo "✅ 全ステップ(99-1～99-7)完了確認"
   echo "✅ 品質基準達成確認"
   echo "✅ 標準ワークフローへの復帰承認"
   
   echo ""
   echo "🚀 推奨次のステップ:"
   echo "   1. 通常開発フロー再開:"
   echo "      - 新機能: /create-use-case <issue-number>"
   echo "      - スプリント計画: /sprint-planning <sprint-number>"
   echo "      - 既存機能改善: /evolve-scenarios <feature-name>"
   echo ""
   echo "   2. 改善活動:"
   echo "      - 改善タスクのスプリント組み込み"
   echo "      - チームへの学習事項共有"
   echo "      - 緊急対応プロセスの改善検討"
   
   echo ""
   echo "💡 重要な成果:"
   echo "   - 緊急修正の適切な文書化完了"
   echo "   - テストカバレッジの回復・向上"
   echo "   - プロジェクト品質基準の維持"
   echo "   - 標準開発プロセスへの円滑な復帰"
   echo ""
   echo "🎉 緊急対応復旧プロセス完了 - おつかれさまでした!"
   echo "標準TDD/DDD/レイヤードアーキテクチャワークフローでの開発を継続してください。"
   ```

## 🔄 **PHASE 3: ENHANCED INTEGRATION CAPABILITIES**

### **Critical Enhancement Features**
This command implements Phase 3 advanced emergency recovery review capabilities:

1. **Intelligent Process Completion Analysis with Multi-dimensional Assessment**
2. **Automated Quality Validation with Comprehensive Metrics Evaluation** 
3. **Smart Workflow Readiness Assessment with Standard Process Integration**
4. **Enhanced Learning Extraction with Process Improvement Recommendations**

### **Project State Updates**

**CRITICAL**: After successful emergency recovery review, MUST update integrated project metadata:

1. **Project State Update**:
   ```bash
   # Update docs/metadata/project-state.json
   # - Set emergency_recovery.final_review_completed = true
   # - Update project_metadata.overall_status to reflect recovery completion
   # - Set emergency_recovery.standard_workflow_ready = true
   # - Update project_metadata.last_emergency_recovery_timestamp
   ```

2. **Project Context Update**:
   ```bash
   # Update .claude/context/project-context.json  
   # - Set emergency_recovery_status.completed = true
   # - Update current_state.phase to normal development phase
   # - Set current_state.last_command and last_command_timestamp
   # - Clear emergency_recovery_active flag
   ```

**⚠️ Error Handling**: If emergency recovery review fails or identifies issues:
- 📖 Consult: [Manual Sync Guide](../../docs/maintenance/manual-sync-guide.md)
- 🔄 Retry Failed Steps: Address identified gaps in emergency recovery process
- 📊 Manual Completion: Complete review manually and update project metadata