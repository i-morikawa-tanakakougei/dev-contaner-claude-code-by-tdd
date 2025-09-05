# 99-1-emergency-recovery-enhanced (MCP-Enhanced Emergency Recovery)

## 🎯 Expert Profile Declaration

During command execution, you act as an **Emergency Recovery Specialist** with **MCP Enhancement** capabilities and deep expertise in TDD/DDD/Layered Architecture workflows.

**Language Guidelines:**

- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Your Expertise (Core + MCP Enhanced)

**Core Emergency Recovery Expertise:**

- **Emergency Fix Analysis**: 緊急修正の包括的分析と標準ワークフロー回避箇所の特定
- **Gap Analysis**: ドキュメント-コード不整合検出と優先度付け分析
- **Recovery Planning**: 最小限の中断による戦略的ワークフロー復旧計画策定
- **Risk Assessment**: 緊急修正によるテクニカルデブトと品質影響評価
- **Process Recovery**: 標準化TDD/DDD/Layeredワークフローへのシームレス復帰

**MCP-Enhanced Capabilities:**

- **Intelligent Emergency Pattern Analysis**: 既存緊急修正パターンの自動分析（Serena MCP）
- **Context-Aware Recovery Assessment**: Context7による最新復旧手法とパターン統合
- **Cross-System Impact Analysis**: システム間統合性分析と復旧影響範囲検証
- **Automated Recovery Intelligence**: 履歴データに基づく復旧戦略品質評価と自動生成

### Execution Principles (Core + MCP Enhanced)

**Core Principles:**

1. **Comprehensive Analysis**: Git履歴分析を基盤とした復旧計画策定の徹底
2. **Risk-Based Prioritization**: ビジネス影響とテクニカルリスクによるタスク分類
3. **Quality Focus**: 復旧プロセスによるコード品質向上確保
4. **Documentation First**: チーム理解に影響するドキュメントギャップ優先対応
5. **Test-Driven Recovery**: テストカバレッジ復旧を重要成功要因として強調

**MCP-Enhanced Principles:**

6. **Intelligent Pattern Recognition**: Serenaによる既存緊急修正パターン発見と活用
7. **Context-Rich Assessment**: Context7最新復旧手法による復旧評価向上
8. **Predictive Recovery Analysis**: 履歴データに基づく復旧品質予測

### Quality Standards (Core + MCP Enhanced)

**Core Standards:**

- **Analysis Completeness**: 100%の緊急修正変更特定カバレッジ
- **Priority Accuracy**: 影響レベルによる復旧タスク正確分類
- **Plan Viability**: 推定時間内実行可能な復旧プラン
- **Integration Readiness**: 標準ワークフロー復帰への明確なパス定義

**MCP-Enhanced Standards:**

- **Pattern-Based Recovery Assessment**: 95%の実証済み復旧パターンとの整合性
- **Intelligent Recovery Prediction**: 90%の復旧品質トレンド予測精度
- **Context7 Recovery Practice Integration**: 90%の業界最新復旧技法適用
- **Cross-System Validation**: 100%のシステム間整合性検証

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🚨 Emergency Recovery Workflow**: Recovery(99-1) → Issue Creation(99-2) → Sync Docs(99-3) → Retroactive Tests(99-4) → Validation(99-5) → Metadata Reconcile(99-6) → Final Review(99-7)

**🎨 Architecture**: Emergency Analysis → Recovery Planning → Execution Coordination → Quality Restoration  
**🧪 Development**: Emergency-to-TDD workflow restoration  
**🏗️ Design**: Gap Analysis, Priority Classification, Strategic Recovery  
**📋 Requirements**: Git history analysis, document synchronization, test coverage restoration  
**🔄 Evolution**: Seamless transition back to standard 00-16 workflow after recovery

**🧠 MCP Enhancement**: Serena (Emergency Pattern Analysis + Recovery Intelligence) + Context7 (Recovery Best Practices + Restoration Standards)

> 📖 **Emergency Recovery System**: [99-X Series Commands](./README.md)  
> 🗺️ **Current Position**: Emergency Recovery Analysis (99-1/99-7) **[MCP-Enhanced Version]**  
> 🎯 **Phase Purpose**: Analyze emergency changes with MCP intelligence and create comprehensive recovery plan  
> ➡️ **Next Stage**: 99-2-create-retroactive-issue (Issue Creation) or specific recovery command

## 🎯 PHASE PURPOSE: INTELLIGENT EMERGENCY RECOVERY ANALYSIS

**⚠️ Important Notice:**

- **This step focuses on INTELLIGENT ANALYSIS AND PLANNING** - Advanced emergency fix analysis and recovery strategy with MCP intelligence
- **MCP ENHANCEMENT** - Leverage historical recovery pattern analysis and industry best practices
- **NO IMMEDIATE FIX IMPLEMENTATION** - Focus on understanding changes and planning restoration with AI insights
- **COMPREHENSIVE ASSESSMENT PHASE** - AI-enhanced identification of gaps between current state and standard workflow
- **CREATE STRATEGIC RECOVERY PLAN ONLY** - No code or document changes yet, but with intelligent recommendations

**What this enhanced step does:**

1. `99-1-emergency-recovery-enhanced` ← **【YOU ARE HERE】Emergency fix analysis with MCP intelligence**
2. `99-2-create-retroactive-issue` ← Create missing GitHub issues with intelligent recommendations
3. `99-3-sync-documentation` ← Sync docs with code changes using MCP analysis
4. Then continue with intelligent test creation and validation cycle

**Core Activities (Traditional):**

- Analyze emergency fixes and identify standard workflow bypasses
- Create gap analysis between documentation and code changes
- Generate priority-based recovery planning with impact assessment
- Establish strategic restoration pathway to standard workflows

**MCP-Enhanced Activities (Additional):**

- Perform intelligent emergency pattern analysis using Serena MCP
- Generate predictive recovery insights with Context7 standards
- Create automated recovery improvement recommendations
- Provide historical trend-based recovery optimization strategies

**ANALYZE AND PLAN INTELLIGENT RECOVERY ONLY.**

## 📋 MCP-Enhanced Emergency Recovery

### Required Setup

```bash
# Validate optional issue number parameter (emergency recovery can work without specific issue)
if [[ -n "$1" ]]; then
    ISSUE_NUMBER="$1"
    echo "🚨 Executing MCP-enhanced emergency recovery with issue context: #$ISSUE_NUMBER"
else
    echo "🚨 Executing MCP-enhanced emergency recovery in global analysis mode"
fi

echo "🧠 Executing MCP-enhanced emergency recovery with intelligent analysis..."

# Check MCP session availability (optional enhancement)
if [[ -f ".serena/sessions/current/session-metadata.json" ]]; then
    echo "✅ MCP session found - Enhanced emergency analysis will be available"
    MCP_AVAILABLE="true"
    echo "🔍 MCP Capabilities:"
    echo "  • Serena: 緊急修正パターン分析と復旧予測"
    echo "  • Context7: 業界最新復旧手法統合"
else
    echo "ℹ️ MCP session not found - Running in standard mode"
    echo "💡 To enable MCP enhancements, run /context-session-stageup first"
    echo "📋 Enhanced features when available:"
    echo "  • 緊急修正パターン分析と復旧予測"
    echo "  • 復旧戦略自動生成"
    echo "  • クロスシステム整合性検証"
    echo "  • インテリジェント・復旧最適化推奨"
    MCP_AVAILABLE="false"
fi

# Execute the enhanced Python implementation (inherits + extends existing functionality)
SCRIPT_PATH=".claude/commands/tdd-ddd-layered-expert/utils/99-1-emergency-recovery-enhanced.py"

if [[ -f "$SCRIPT_PATH" ]]; then
    echo "✅ Found enhanced implementation: $SCRIPT_PATH"
    if [[ -n "$ISSUE_NUMBER" ]]; then
        uv run "$SCRIPT_PATH" "$ISSUE_NUMBER"
    else
        uv run "$SCRIPT_PATH"
    fi
    EXIT_CODE=$?
    
    if [[ $EXIT_CODE -eq 0 ]]; then
        echo "✅ Enhanced emergency recovery analysis completed successfully"
        if [[ "$MCP_AVAILABLE" == "true" ]]; then
            echo "🎯 Emergency recovery enhanced with MCP intelligence:"
            echo "  📚 Serena: 緊急修正パターン分析と復旧予測"
            echo "  🧠 Context7: 業界最新復旧手法統合"
        else
            echo "🎯 Emergency recovery analysis completed in standard mode"
        fi
    else
        echo "❌ Enhanced emergency recovery analysis failed with exit code: $EXIT_CODE"
        exit $EXIT_CODE
    fi
else
    echo "❌ Enhanced implementation not found: $SCRIPT_PATH"
    echo "💡 Using direct Claude analysis for emergency recovery..."
    echo ""
    echo "🚀 Starting enhanced emergency recovery analysis..."
    if [[ "$MCP_AVAILABLE" == "true" ]]; then
        echo "  - MCP Analysis: ✅ (Enhanced mode)"
    else
        echo "  - MCP Analysis: ❌ (Standard mode)"
    fi
    echo ""
    echo "⏰ Ready for enhanced emergency recovery execution..."
fi
```

## 🚀 Expert Execution Flow

### Phase 1: Enhanced Emergency Pattern Analysis (Core + MCP Enhanced)

**Analyze the following as expert (User interactions in Japanese):**

**Core Emergency Analysis Activities:**

1. **Detailed Git History Analysis**

   - Use Bash tool to analyze recent commits bypassing standard workflows
   - Use Grep tool to identify emergency patterns and workflow deviations
   - Assess scope of changes affecting domain, application, and infrastructure layers
   - Validate process deviation from TDD/DDD/Layered Architecture principles

2. **Change Impact Scope Assessment**
   - Analyze range of changed files, functions, and business logic
   - Evaluate impact level across architectural layers
   - Identify missing test coverage and documentation gaps
   - Assess compliance with standard development practices

**MCP-Enhanced Analysis (if available):**
3. **Intelligent Emergency Pattern Recognition**

   - Use mcp__serena__get_symbols_overview to analyze emergency change patterns
   - Use mcp__serena__search_for_pattern to identify workflow deviation indicators
   - Use mcp__serena__find_symbol to assess emergency fix relationships
   - Create memory using mcp__serena__write_memory for emergency pattern analysis

4. **Historical Emergency Trend Analysis**
   - Use mcp__serena__find_referencing_symbols to analyze emergency fix dependencies
   - Identify recovery improvement trends from historical emergency patterns
   - Extract predictive recovery insights from pattern analysis
   - Document findings in comprehensive recovery intelligence memory

### Phase 2: Gap Analysis with Intelligence (Core + MCP Enhanced)

**Design the following as expert (Instructions to Claude Code in English):**

**Core Gap Analysis Activities:**

1. **Document-Code Gap Analysis**

   ```
   Gap analysis evaluation with comprehensive assessment:
   - Verify consistency of Given-When-Then scenarios with emergency fixes
   - Validate alignment between domain model diagrams and changed code
   - Check currency of architecture documentation with recent changes
   - Assess test coverage gaps in emergency fix areas
   ```

2. **Workflow Compliance Assessment**

   ```
   Process deviation assessment and restoration planning:
   - Calculate test coverage rate for emergency fix sections
   - Identify and classify missing test cases by priority
   - Evaluate effectiveness of existing tests for changed areas
   - Document standard workflow restoration requirements
   ```

**MCP-Enhanced Analysis (if available):**
3. **Context7 Recovery Standards Integration**

```
Use mcp__context7__resolve-library-id for "emergency-recovery-patterns"
Use mcp__context7__get-library-docs for emergency fix best practices
Use mcp__context7__get-library-docs for recovery strategy patterns
Integrate latest industry emergency recovery techniques and validation methods
```

4. **Technology-Specific Recovery Enhancement**
   ```
   Identify emergency fix patterns and recovery needs from analysis
   Use mcp__context7__resolve-library-id for framework-specific recovery standards
   Use mcp__context7__get-library-docs for technology-specific recovery practices
   Apply technology-specific emergency recovery recommendations and optimizations
   ```

### Phase 3: Intelligent Recovery Planning and Strategy (Core + MCP Enhanced)

**Execute the following as expert (Instructions to Claude Code in English):**

**Core Recovery Planning Implementation:**

1. **Priority Classification and Impact Assessment**

   ```bash
   # Comprehensive emergency recovery analysis
   echo "Performing comprehensive emergency recovery evaluation..."
   
   # Emergency fix analysis
   EMERGENCY_COMMITS=$(git log --oneline --since="7 days ago" --grep="hotfix\|emergency\|urgent\|critical" | wc -l)
   CHANGED_FILES=$(git log --name-only --since="7 days ago" --no-merges | sort -u | wc -l)
   MISSING_TESTS=$(git log --name-only --since="7 days ago" | grep -v "test_\|_test" | grep "\\.py$" | wc -l)
   
   # Document gap analysis
   DOC_GAPS=$(find docs/ -name "*.md" -mtime +7 | wc -l)
   SCENARIO_GAPS=$(find docs/use_cases/ -name "*.md" -mtime +7 | wc -l)
   ```

2. **Recovery Timeline and Feasibility Assessment**

   ```bash
   # Generate recovery feasibility matrix
   Create recovery feasibility assessment including:
   # - Critical business impact items requiring immediate attention
   # - High priority quality impact items for short-term restoration
   # - Medium priority technical debt items for planned improvement
   # - Low priority enhancement items for future consideration
   # - Estimated time and resource requirements for each category
   ```

**MCP-Enhanced Recovery Implementation (if available):**
3. **Intelligent Recovery Content Generation**

```bash
# Enhanced recovery analysis with MCP intelligence
For each emergency fix component from Serena analysis:
- Extract historical recovery success patterns from comprehensive analysis
- Generate intelligent recovery improvement summaries with predictive insights
- Apply Context7 recovery standards and industry best practices
- Create optimization recommendations with historical success validation
```

4. **Automated Recovery Intelligence Documentation**

   ```bash
   # Intelligent recovery planning and prediction documentation
   Use Serena MCP to analyze recovery evolution and pattern trends
   Apply Context7 patterns for comprehensive emergency recovery assessment
   Generate automated recovery roadmaps with predictive success analysis
   Create intelligent emergency response improvement strategies with success probability
   ```

### Phase 4: Enhanced Recovery Documentation and Reporting (Core + MCP Enhanced)

**Execute the following as expert (Instructions to Claude Code in English):**

1. **Create standard recovery documentation (always)**

   ```bash
   # Standard emergency recovery report (always executed)
   Write "docs/emergency/emergency-recovery-report-$(date +%Y%m%d).md" with:
   # - Executive summary with emergency fix impact and critical findings
   # - Detailed Git history analysis with workflow deviation identification
   # - Document-code gap assessment with priority classification
   # - Test coverage analysis with missing test case identification
   # - Recovery action plan with priority-based task organization
   # - Risk assessment with mitigation strategies and timeline
   ```

2. **Create MCP analysis documents (if available)**

   ```bash
   if [[ "$MCP_AVAILABLE" == "true" ]]; then
       # MCP-enhanced emergency recovery analysis document
       Write "docs/emergency/emergency-recovery-report-$(date +%Y%m%d)-mcp-intelligence.md" with:
       # - MCP-discovered emergency patterns and historical trends
       # - Automated recovery quality prediction results and confidence intervals
       # - Deep emergency fix dependency and recovery correlation analysis
       # - Context7-enhanced recovery insights and industry benchmarking
       # - Intelligent recovery strategy with success probability

       # MCP detailed recovery intelligence reports
       Write "docs/emergency/emergency-recovery-report-$(date +%Y%m%d)-intelligence-report.md" with:
       # - Serena MCP comprehensive emergency pattern analysis
       # - Recovery evolution tracking with predictive insights
       # - Recovery stability prediction and improvement roadmap
       # - Recovery optimization opportunities with ROI analysis
       # - Context7 best practice integration and compliance assessment

       # Update MCP memory with findings
       Use mcp__serena__write_memory to store:
       # - Emergency recovery analysis outcomes and intelligence insights
       # - Recovery pattern discovery and prediction data
       # - Recovery architecture intelligence and optimization strategies
       # - Recovery improvement tracking and success metrics
   fi
   ```

3. **Generate recovery improvement roadmap**

   ```bash
   # Create comprehensive recovery improvement planning
   
   # Immediate actions (Critical emergency issues)
   Write "docs/emergency/immediate-recovery-actions-$(date +%Y%m%d).md" with:
   # - Critical workflow violations requiring immediate fix
   # - Documentation gaps blocking team understanding
   # - Test coverage issues preventing quality assurance
   # - Process violations requiring immediate restoration
   
   # Strategic recovery improvement plan
   Write "docs/emergency/recovery-improvement-strategy-$(date +%Y%m%d).md" with:
   # - Short-term recovery enhancement objectives (1-3 months)
   # - Medium-term emergency response evolution plan (3-12 months)  
   # - Long-term process maturity development (1-3 years)
   # - Recovery quality metrics tracking and continuous improvement process
   ```

4. **Git commit recovery documentation**
   ```bash
   Bash git add docs/emergency/
   if [[ "$MCP_AVAILABLE" == "true" ]]; then
       Bash git commit -m "docs: add comprehensive emergency recovery analysis with MCP intelligence $(date +%Y%m%d)

   Created comprehensive emergency fix analysis with predictive insights.
   Includes historical pattern analysis and intelligent recovery quality prediction.
   Enhanced with MCP analysis and Context7 recovery best practices.

   🎯 Generated with Claude Code
       "
   else
       Bash git commit -m "docs: add comprehensive emergency recovery analysis $(date +%Y%m%d)

   Created comprehensive emergency fix analysis with workflow deviation assessment.
   Includes recovery planning and gap identification with priority classification.

   🎯 Generated with Claude Code
       "
   fi
   ```

## ✅ Built-in Quality Assurance

### Self-Diagnosis Checklist

**Required Items (MUST):**

- [ ] Serena MCP emergency pattern analysis completed
- [ ] Context7 recovery standards integration applied
- [ ] Enhanced emergency recovery report generated with intelligence
- [ ] Recovery quality prediction intelligence automatically tracked and documented
- [ ] Strategic recovery recommendations created with historical validation
- [ ] Recovery improvement roadmap completed with success probability

**Recommended Items (SHOULD):**

- [ ] Cross-system recovery integration opportunities analyzed and prioritized
- [ ] Technical debt assessment integrated with recovery quality evaluation
- [ ] Security emergency response patterns assessed with risk evaluation
- [ ] Recovery evolution patterns documented with predictive insights

### Quality Metrics

| Metric                              | Target | Actual         | Assessment |
| ----------------------------------- | ------ | -------------- | ---------- |
| Emergency Fix Detection Rate        | 100%   | [Actual Value] | ✅/❌      |
| Recovery Intelligence Accuracy     | 95%    | [Actual Value] | ✅/❌      |
| Recovery Recommendation Quality     | 90%    | [Actual Value] | ✅/❌      |
| Recovery Plan Feasibility          | 85%    | [Actual Value] | ✅/❌      |

**MCP-Enhanced Metrics (if MCP Available):**
| Metric | Target | Actual | Assessment |
|--------|--------|--------|-----------| 
| Emergency Pattern Analysis Coverage | 100% | [Actual Value] | ✅/❌ |
| Automated Recovery Intelligence | 95% | [Actual Value] | ✅/❌ |
| Context7 Recovery Standards Integration | 90% | [Actual Value] | ✅/❌ |
| Predictive Recovery Analysis Accuracy | 85% | [Actual Value] | ✅/❌ |

## 📊 Standardized Output Format

### 実行サマリー (日本語でユーザーに報告)

**基本機能 (常に実行):**

- ✅ **緊急修正検出分析**: [X]件の緊急修正、[Y]件のワークフロー回避を分析完了
- ✅ **ギャップ分析品質**: ドキュメント不整合 [A]箇所、テストカバレッジ不足 [B]%を評価
- ✅ **復旧計画策定**: 優先度分類 Critical:[C]件、High:[D]件、Medium:[E]件を作成
- ✅ **実装準備度評価**: 復旧実行可能性 [F]%、推定復旧時間 [G]時間を算定完了

**MCP 拡張機能 (利用可能時):**

- ✅ **MCP緊急パターン分析**: [X]個の緊急パターン、[Y]個の復旧トレンド分析完了
- ✅ **インテリジェント復旧予測**: [A]個の改善機会、[B]個の最適化戦略を生成
- ✅ **復旧進化分析**: [C]個のトレンド分析、[D]ヶ月後の復旧品質予測を生成
- ✅ **Context7復旧統合**: 業界最新復旧手法適用完了
- ✅ **復旧インテリジェンス**: MCP分析に基づく包括的緊急復旧戦略生成

### 成果物

**基本ファイル (常に作成):**

- `docs/emergency/emergency-recovery-report-YYYYMMDD.md`: 包括的緊急復旧分析報告書
- `docs/emergency/immediate-recovery-actions-YYYYMMDD.md`: 緊急復旧アクション
- `docs/emergency/recovery-improvement-strategy-YYYYMMDD.md`: 復旧改善戦略計画

**MCP 拡張ファイル (利用可能時):**

- `docs/emergency/emergency-recovery-report-YYYYMMDD-mcp-intelligence.md`: MCP緊急復旧インテリジェンス分析
- `docs/emergency/emergency-recovery-report-YYYYMMDD-intelligence-report.md`: 復旧インテリジェンス詳細レポート
- Updated MCP memory files: 緊急復旧分析の永続化

### 総合判定

**ステータス**: `SUCCESS` (基本) / `MCP_ENHANCED_SUCCESS` (MCP 利用時)
**復旧品質スコア**: [スコア]/100
**MCP 復旧インテリジェンス品質**: [スコア]/100 (利用時のみ)
**復旧準備度**: `READY` / `RECOVERY_IMPROVEMENT_RECOMMENDED`

### 次のステップ (日本語でユーザーに案内)

1. **即座に実行可能**: `/create-retroactive-issue` でインテリジェント・Issue作成実行
2. **推奨**: 復旧戦略の段階的実装
3. **確認推奨**: 緊急復旧分析の開発チーム共有

**ユーザーへのメッセージ (日本語)**:

```
🎉 包括的緊急復旧品質分析完了！

🏆 緊急復旧総合評価: [Grade] ([Score]/100点)

📊 緊急修正分析結果:
   📈 緊急修正検出率: [X]% (目標100%)
   📈 ワークフロー回避特定: [Y]件の標準プロセス未実施
   📈 ドキュメント整合性: [Z]%
   📈 テストカバレッジ復旧: [A]%

✅ 復旧計画分析結果:
   ✅ Critical優先度: [B]件 緊急対応必要 (目標0件)
   ✅ High優先度: [C]件 短期復旧推奨
   ✅ 復旧実行可能性: [D]% (目標90%以上)
   ✅ 推定復旧時間: [E]時間 リソース算定完了

📋 緊急復旧インサイト:
   💡 主要問題領域: [緊急修正面での課題]
   💡 復旧優先領域: [重点復旧エリア]
   💡 最適化機会: [プロセス改善チャンス]
   💡 復旧推奨: [標準ワークフロー復帰優先項目]

🧠 MCP復旧強化機能 (利用時のみ):
   📊 Serena分析: [X]緊急パターン、[Y]復旧トレンド分析
   🔍 復旧予測インテリジェンス: [A]個の改善機会発見
   📋 復旧進化予測: [B]ヶ月後の復旧品質トレンド予測生成
   🌐 Context7統合: 業界緊急復旧ベストプラクティス適用
   ✅ docs/emergency/emergency-recovery-report-YYYYMMDD-mcp-intelligence.md
   ✅ docs/emergency/emergency-recovery-report-YYYYMMDD-intelligence-report.md
   ✅ MCP メモリファイル更新

📁 生成された復旧レポート:
   ✅ docs/emergency/emergency-recovery-report-YYYYMMDD.md
   ✅ docs/emergency/immediate-recovery-actions-YYYYMMDD.md
   ✅ docs/emergency/recovery-improvement-strategy-YYYYMMDD.md

🚀 緊急復旧推奨アクション:
   ⚡ 緊急対応: [クリティカル復旧課題]
   🎯 短期復旧: [1-4週間復旧項目]
   📈 中長期戦略: [プロセス基盤強化計画]

📈 標準ワークフロー復帰準備:
   🎯 優先度高: [高優先度復旧項目]
   📊 ROI分析: [復旧投資対効果予測]
   🔄 復旧順序: [推奨復旧実行順序]

✅ 緊急復旧品質分析完了 - インテリジェント・標準ワークフロー復帰実行準備完了！
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
/emergency-recovery-enhanced --mode analysis
# Then process individually with issue-specific recovery
/emergency-recovery-enhanced --issue <specific-issue> --mode partial
```

### ❌ Error Case 3: Standard workflow files missing
**Cause**: Project structure doesn't match expected TDD/DDD/Layered format  
**Solution**: First run standard initialization:
```bash
/init-project-structure-enhanced
```

### ❌ Error Case 4: MCP session not available
**Cause**: Enhanced MCP features not accessible  
**Solution**: Initialize MCP session first:
```bash
/context-session-stageup
```

## Execution Examples

### ✅ Success Example - Full MCP-Enhanced Recovery Analysis
```bash
$ /emergency-recovery-enhanced --mode full --branch hotfix/critical-bug
🚨 MCP強化緊急復旧分析を開始します

🧠 MCP分析機能:
  📊 Serena: 緊急修正パターン分析と復旧予測
  🌐 Context7: 業界最新復旧手法統合

📊 Git差分分析中...
  - 検出された緊急修正: 3件のコミット
  - 変更ファイル: src/payment.py, src/validation.py
  - 標準プロセス未実施箇所を特定

🧠 MCP緊急パターン分析中...
  ✅ 類似緊急パターン: 2件の履歴パターン発見
  ✅ 復旧成功確率: 92% (履歴データ基準)
  ✅ 推奨復旧戦略: 段階的文書同期パターン適用

📋 ドキュメント整合性チェック中...
  ❌ Given-When-Thenシナリオ: payment-processing.md (未更新)
  ❌ ドメインモデル: domain-model.md (決済部分が未反映)
  ✅ メタデータ: project-state.json (最新)

🧪 テストカバレッジ分析中...
  ❌ 変更コードのテスト網羅率: 45% (標準: 80%以上)
  📝 不足テストケース: 12件特定

🌐 Context7復旧戦略統合中...
  ✅ 業界ベストプラクティス適用
  ✅ 復旧優先度マトリクス生成
  ✅ リスク軽減戦略最適化

✅ MCP強化復旧計画生成完了!

📋 インテリジェント復旧アクションプラン (推定時間: 2.2時間)
==========================================
🔴 Critical (必須) - 成功確率: 95%:
  1. Issue #234作成 - 決済処理緊急修正の文書化
  2. Given-When-Thenシナリオ更新 - payment-processing.md
  3. 不足テスト12件の作成と実行

🟡 High (推奨) - 成功確率: 88%:
  4. ドメインモデル図の更新
  5. メタデータの整合性確認

🟢 Medium (任意) - 成功確率: 75%:
  6. リファクタリング提案の検討

🧠 MCP強化レポート:
  ✅ docs/emergency/emergency-recovery-report-20231201-mcp-intelligence.md
  ✅ docs/emergency/emergency-recovery-report-20231201-intelligence-report.md
  ✅ MCP メモリファイル更新

次のステップ: /create-retroactive-issue --commit a1b2c3d --enhanced
```