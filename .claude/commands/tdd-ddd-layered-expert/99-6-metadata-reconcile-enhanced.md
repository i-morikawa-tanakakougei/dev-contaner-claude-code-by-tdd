# 99-6-metadata-reconcile-enhanced (MCP-Enhanced Metadata Reconciliation)

## 🎯 Expert Profile Declaration

During command execution, you act as a **Metadata Reconciliation Specialist** with **MCP Enhancement** capabilities and deep expertise in emergency metadata management.

**Language Guidelines:**

- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Your Expertise (Core + MCP Enhanced)

**Core Metadata Reconciliation Expertise:**

- **Emergency Metadata Management**: Comprehensive analysis and reconciliation of project metadata after emergency recovery
- **Data Integrity Engineering**: Detection and resolution of inconsistencies between multiple metadata sources 
- **System Synchronization**: Cross-system metadata synchronization with intelligent conflict resolution
- **Project State Analysis**: Deep analysis of project health, progress metrics, and quality indicators

**MCP-Enhanced Capabilities:**

- **Intelligent Metadata Analysis**: Automated metadata pattern analysis using Serena MCP
- **Context-Aware Synchronization**: Context7-based metadata standards and best practices
- **Cross-Reference Validation**: Complete dependency and consistency validation
- **Automated Quality Enhancement**: AI-powered metadata optimization and improvement recommendations

### Execution Principles (Core + MCP Enhanced)

**Core Principles:**

1. **Comprehensive Analysis**: Thoroughly analyze all metadata sources with intelligent pattern recognition
2. **Intelligent Conflict Resolution**: Apply priority-based conflict resolution with automated decision support
3. **Integrity-First Updates**: Ensure metadata integrity with predictive quality validation
4. **Audit Trail Maintenance**: Document all changes with intelligent change tracking

**MCP-Enhanced Principles:**

5. **Intelligent Pattern Recognition**: Leverage Serena for deep metadata analysis and pattern discovery
6. **Context-Rich Validation**: Use Context7 for professional metadata standards and benchmarks
7. **Automated Quality**: Ensure consistency and completeness through intelligent validation

### Quality Standards (Core + MCP Enhanced)

**Core Standards:**

- **Consistency Score**: Achieve 95%+ consistency across all metadata files after reconciliation
- **Data Integrity**: Maintain 100% JSON validity and structural integrity of all metadata files
- **Completeness Verification**: Ensure all required metadata fields are populated with accurate information
- **Audit Traceability**: Complete change tracking and reconciliation decision documentation

**MCP-Enhanced Standards:**

- **Pattern Recognition Coverage**: 95% of metadata patterns identified and validated
- **Automated Quality Assessment**: 90% of quality metrics automated through intelligent analysis
- **Cross-Reference Accuracy**: 100% metadata dependency validation with Serena MCP
- **Standards Compliance**: 95% compliance with Context7 best practices

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🚨 Emergency Recovery Workflow**: Recovery(99-1) → Issue Creation(99-2) → Sync Docs(99-3) → Retroactive Tests(99-4) → Validation(99-5) → Metadata Reconcile(99-6) → Final Review(99-7)

**🎨 Architecture**: Emergency Analysis → Issue Creation → Documentation Sync → Test Creation → Recovery Validation → Quality Restoration  
**🧪 Development**: Emergency-to-TDD workflow restoration and metadata synchronization  
**🏗️ Design**: Metadata Analysis, Consistency Validation, System Synchronization  
**📋 Requirements**: Metadata reconciliation, integrity assurance, system state restoration  
**🔄 Evolution**: Complete metadata consistency and system state synchronization

**🧠 MCP Enhancement**: Serena (Metadata Analysis + Pattern Intelligence) + Context7 (Quality Standards + Best Practices)

> 📖 **Emergency Recovery System**: [99-X Series Commands](./README.md)  
> 🗺️ **Current Position**: Metadata Reconciliation (99-6/99-7) **[MCP-Enhanced Version]**  
> 🎯 **Phase Purpose**: Reconcile project metadata with MCP intelligence after emergency recovery  
> ➡️ **Next Stage**: 99-7-review-emergency-recovery (Final Recovery Review) or specific reconciliation command

## 🎯 PHASE PURPOSE: INTELLIGENT METADATA RECONCILIATION

**⚠️ Important Notice:**

- **This step focuses on METADATA RECONCILIATION** - Intelligent synchronization of project metadata and system state
- **MCP ENHANCEMENT** - Leverage intelligent metadata analysis and professional quality assessment
- **NO CODE CHANGES** - Focus on metadata consistency and system state reconciliation only
- **SYSTEM SYNCHRONIZATION** - Ensure complete metadata integrity and cross-system consistency
- **RECONCILE METADATA ONLY** - No implementation changes, metadata focus only

**What this enhanced step does:**

1. `99-4-create-retroactive-tests-enhanced` ← Previous: Retroactive test creation with MCP enhancement
2. `99-5-validate-recovery-enhanced` ← Previous: Recovery validation with MCP enhancement
3. `99-6-metadata-reconcile-enhanced` ← **【YOU ARE HERE】Metadata reconciliation with MCP enhancement**
4. `99-7-review-emergency-recovery` ← Next: Final recovery review
5. Then complete transition back to standard development workflow

**Core Activities (Traditional):**

- Analyze and reconcile project metadata across multiple systems
- Detect and resolve inconsistencies between metadata sources
- Synchronize system state and project tracking information
- Generate comprehensive metadata reconciliation report

**MCP-Enhanced Activities (Additional):**

- Perform intelligent metadata pattern analysis using Serena MCP
- Apply professional metadata standards using Context7 benchmarks
- Create automated metadata optimization recommendations
- Provide intelligent system synchronization guidance

**RECONCILE METADATA WITH INTELLIGENT ANALYSIS ONLY.**

## 📋 MCP-Enhanced Metadata Analysis

### Required Setup

```bash
# Validate optional context parameter (scope, mode, or specific files)
if [[ -n "$1" ]]; then
    CONTEXT_PARAM="$1"
    echo "🔄 Executing MCP-enhanced metadata reconciliation with context: $CONTEXT_PARAM"
else
    echo "🔄 Executing MCP-enhanced metadata reconciliation in comprehensive analysis mode"
fi

echo "🧠 Executing MCP-enhanced metadata reconciliation with intelligent analysis..."

# Check MCP session availability (optional enhancement)
if [[ -f ".serena/sessions/current/session-metadata.json" ]]; then
    echo "✅ MCP session found - Enhanced metadata reconciliation will be available"
    MCP_AVAILABLE="true"
    echo "🔍 MCP Capabilities:"
    echo "  • Serena: メタデータ分析とパターンインテリジェンス"
    echo "  • Context7: プロフェッショナル品質基準統合"
else
    echo "ℹ️ MCP session not found - Running in standard mode"
    echo "💡 To enable MCP enhancements, run /context-session-stageup first"
    echo "📋 Enhanced features when available:"
    echo "  • 自動メタデータパターン分析"
    echo "  • プロフェッショナル品質基準適用"
    echo "  • クロスリファレンス整合性検証"
    echo "  • インテリジェント最適化推奨"
    MCP_AVAILABLE="false"
fi

# Execute the enhanced Python implementation (inherits + extends existing functionality)
SCRIPT_PATH=".claude/commands/tdd-ddd-layered-expert/utils/99-6-metadata-reconcile-enhanced.py"

if [[ -f "$SCRIPT_PATH" ]]; then
    echo "✅ Found enhanced implementation: $SCRIPT_PATH"
    if [[ -n "$CONTEXT_PARAM" ]]; then
        uv run "$SCRIPT_PATH" "$CONTEXT_PARAM"
    else
        uv run "$SCRIPT_PATH"
    fi
    EXIT_CODE=$?
    
    if [[ $EXIT_CODE -eq 0 ]]; then
        echo "✅ Enhanced metadata reconciliation completed successfully"
        if [[ "$MCP_AVAILABLE" == "true" ]]; then
            echo "🎯 Metadata reconciliation enhanced with MCP intelligence:"
            echo "  🔄 Serena: メタデータ分析とパターンインテリジェンス"
            echo "  🧠 Context7: プロフェッショナル品質基準統合"
        else
            echo "🎯 Metadata reconciliation completed in standard mode"
        fi
    else
        echo "❌ Enhanced metadata reconciliation failed with exit code: $EXIT_CODE"
        exit $EXIT_CODE
    fi
else
    echo "❌ Enhanced implementation not found: $SCRIPT_PATH"
    echo "💡 Using direct Claude analysis for metadata reconciliation..."
    echo ""
    echo "🚀 Starting enhanced metadata reconciliation analysis..."
    if [[ "$MCP_AVAILABLE" == "true" ]]; then
        echo "  - MCP Analysis: ✅ (Enhanced mode)"
    else
        echo "  - MCP Analysis: ❌ (Standard mode)"
    fi
    echo ""
    echo "⏰ Ready for enhanced metadata reconciliation execution..."
fi
```

## 🚀 Expert Execution Flow

### Phase 1: Enhanced Metadata State Analysis (Core + MCP Enhanced)

**Analyze the following as expert (User interactions in Japanese):**

**Core Metadata Analysis Activities:**

1. **Emergency Recovery State Assessment**

   - Use Bash tool to analyze emergency recovery command execution history
   - Use Read tool to verify metadata files and system state consistency
   - Extract reconciliation requirements from recovery completion status
   - Validate current metadata accuracy against system reality

2. **Cross-System Consistency Validation**
   - Analyze metadata consistency between project state files
   - Evaluate system synchronization status and data integrity
   - Identify inconsistencies and conflict resolution requirements
   - Assess metadata completeness and quality indicators

**MCP-Enhanced Analysis (if available):**
3. **Intelligent Metadata Pattern Analysis**

   - Use mcp__serena__get_symbols_overview to analyze metadata structure patterns
   - Use mcp__serena__search_for_pattern to identify metadata inconsistencies
   - Use mcp__serena__find_symbol to assess metadata dependency relationships
   - Create memory using mcp__serena__write_memory for metadata analysis results

4. **Cross-Reference Metadata Intelligence**
   - Use mcp__serena__find_referencing_symbols to analyze metadata dependencies
   - Identify reconciliation patterns from historical metadata analysis
   - Extract consistency insights from metadata pattern analysis
   - Document findings in comprehensive metadata intelligence memory

### Phase 2: Quality Standards Compliance Assessment (Core + MCP Enhanced)

**Design the following as expert (Instructions to Claude Code in English):**

**Core Quality Assessment Activities:**

1. **Metadata Integrity Validation**

   ```
   Metadata integrity assessment with comprehensive analysis:
   - Extract metadata consistency metrics and quality indicators
   - Validate JSON syntax and structural integrity across all files
   - Assess data completeness and accuracy of tracking information
   - Verify cross-system synchronization and consistency maintenance
   ```

2. **System State Synchronization Analysis**

   ```
   System state synchronization validation:
   - Validate project tracking accuracy and completeness
   - Verify execution history consistency and audit trail integrity
   - Assess metadata evolution tracking and change management
   - Confirm system health indicators and quality metrics accuracy
   ```

**MCP-Enhanced Assessment (if available):**
3. **Context7 Quality Standards Integration**

```
Use mcp__context7__resolve-library-id for "metadata-management"
Use mcp__context7__get-library-docs for professional metadata standards
Use mcp__context7__get-library-docs for best practice synchronization frameworks
Integrate industry-standard metadata reconciliation and quality guidelines
```

4. **Technology-Specific Quality Enhancement**
   ```
   Identify project metadata framework from system analysis
   Use mcp__context7__resolve-library-id for framework-specific metadata patterns
   Use mcp__context7__get-library-docs for metadata quality methodologies
   Apply technology-specific metadata reconciliation guidance and standards
   ```

### Phase 3: Intelligent Reconciliation and Synchronization (Core + MCP Enhanced)

**Execute the following as expert (Instructions to Claude Code in English):**

**Core Reconciliation Implementation:**

1. **Metadata Consistency Reconciliation Process**

   ```bash
   # Comprehensive metadata reconciliation
   echo "Reconciling metadata consistency across all systems..."
   
   # Analyze emergency recovery completion status
   RECOVERY_REPORTS=$(find docs/emergency -name "*report*" -type f | sort -r)
   
   # Validate metadata file consistency
   METADATA_FILES=(
       "docs/metadata/project-state.json"
       ".claude/context/project-context.json"
       ".claude/context/execution-history.jsonl"
   )
   
   # Reconcile each metadata source
   for file in "${METADATA_FILES[@]}"; do
       echo "Reconciling metadata source: $file"
       # Extract consistency metrics and resolve conflicts
       # Update metadata with current system state
   done
   
   # Validate project state accuracy
   if [[ -f "docs/status/project-status.md" ]]; then
       echo "Validating project status consistency..."
   fi
   ```

2. **System State Validation and Reconciliation**

   ```bash
   # Comprehensive system state reconciliation
   echo "Performing system state metadata reconciliation..."
   
   # Validate emergency recovery completion status
   COMPLETION_STATUS=$(find docs/emergency -name "*validation*" -type f | head -1)
   
   # Reconcile execution history with actual command completion
   if [[ -f ".claude/context/execution-history.jsonl" ]]; then
       echo "Reconciling execution history with system state..."
       # Update execution history with accurate completion status
   fi
   
   # Update project health and quality metrics
   echo "Updating project health and quality indicators..."
   ```

**MCP-Enhanced Implementation (if available):**
3. **Intelligent Metadata Reconciliation**

```bash
# Enhanced metadata reconciliation with MCP intelligence
For each metadata source from Serena analysis:
- Extract metadata pattern consistency and quality indicators
- Generate professional reconciliation strategies using Context7 standards
- Apply intelligent metadata optimization recommendations
- Create comprehensive metadata mapping based on system dependencies
```

4. **Automated Quality Enhancement**

   ```bash
   # Intelligent metadata quality enhancement
   Use Serena MCP to validate metadata-system consistency completeness
   Generate quality metrics and improvement recommendations
   Apply Context7 best practices for metadata reconciliation and synchronization
   Create automated metadata maintenance guidance
   ```

### Phase 4: Enhanced Documentation and Reporting (Core + MCP Enhanced)

**Execute the following as expert (Instructions to Claude Code in English):**

1. **Create standard reconciliation report (always)**

   ```bash
   # Standard metadata reconciliation report (always executed)
   Write "docs/emergency/metadata-reconciliation-report-$(date +%Y%m%d).md" with:
   # - Executive summary with reconciliation results and consistency analysis
   # - Detailed metadata consistency mapping with quality assessment matrix
   # - System synchronization summary with integrity breakdown
   # - Quality assurance reconciliation with standards compliance assessment
   # - Cross-system validation with consistency confirmation
   # - Next steps and recommendations for ongoing metadata maintenance
   ```

2. **Create MCP analysis documents (if available)**

   ```bash
   if [[ "$MCP_AVAILABLE" == "true" ]]; then
       # MCP-enhanced metadata reconciliation analysis document
       Write "docs/emergency/metadata-reconciliation-report-$(date +%Y%m%d)-mcp-intelligence.md" with:
       # - MCP-discovered metadata patterns and reconciliation insights
       # - Automated quality assessment and improvement recommendations
       # - Cross-reference consistency mapping and dependency analysis
       # - Context7-enhanced quality standards and professional benchmarks
       # - Intelligent metadata optimization strategies and maintenance guidance

       # MCP detailed reconciliation intelligence reports
       Write "docs/emergency/metadata-reconciliation-report-$(date +%Y%m%d)-intelligence-report.md" with:
       # - Serena MCP metadata-system analysis summary and pattern validation
       # - Reconciliation quality metrics and consistency indicators
       # - System synchronization results and integrity assessment
       # - Cross-reference analysis and dependency graph validation
       # - Context7 standards integration and compliance assessment

       # Update MCP memory with findings
       Use mcp__serena__write_memory to store:
       # - Metadata reconciliation analysis outcomes and quality metrics
       # - System synchronization consistency and integrity results
       # - Quality intelligence and optimization strategies
       # - Reconciliation tracking and maintenance recommendations
   fi
   ```

3. **Perform final metadata validation**

   ```bash
   # Final comprehensive metadata validation
   echo "Performing final metadata reconciliation validation..."
   
   # Validate all metadata consistency
   VALIDATION_CHECKLIST=(
       "docs/metadata/project-state.json"
       ".claude/context/project-context.json"
       ".claude/context/execution-history.jsonl"
       "docs/emergency/*reconciliation-report*.md"
   )
   
   for pattern in "${VALIDATION_CHECKLIST[@]}"; do
       if ls $pattern 1> /dev/null 2>&1; then
           echo "✅ Validation passed: $pattern"
           # Validate JSON syntax for JSON files
           if [[ "$pattern" == *.json || "$pattern" == *.jsonl ]]; then
               python3 -m json.tool "$pattern" > /dev/null 2>&1 && echo "  JSON syntax valid"
           fi
       else
           echo "❌ Validation failed: $pattern not found"
       fi
   done
   
   # Final consistency score calculation
   echo "Calculating final metadata consistency score..."
   ```

4. **Git commit reconciliation documentation**
   ```bash
   Bash git add docs/emergency/ docs/metadata/ .claude/context/
   if [[ "$MCP_AVAILABLE" == "true" ]]; then
       Bash git commit -m "docs: comprehensive metadata reconciliation with MCP intelligence $(date +%Y%m%d)

   Completed comprehensive metadata reconciliation after emergency recovery with intelligent analysis.
   Includes professional quality assessment and automated consistency validation.
   Enhanced with MCP analysis and Context7 best practices.

   🎯 Generated with Claude Code
       "
   else
       Bash git commit -m "docs: comprehensive metadata reconciliation $(date +%Y%m%d)

   Completed comprehensive metadata reconciliation after emergency recovery with quality assessment.
   Includes consistency validation and system synchronization confirmation.

   🎯 Generated with Claude Code
       "
   fi
   ```

## ✅ Built-in Quality Assurance

### Self-Diagnosis Checklist

**Required Items (MUST):**

- [ ] Serena MCP metadata pattern analysis completed
- [ ] Context7 quality standards integration applied
- [ ] Enhanced metadata reconciliation with intelligence
- [ ] Cross-reference consistency validation completed
- [ ] Quality assessment and optimization applied
- [ ] System synchronization validation completed

**Recommended Items (SHOULD):**

- [ ] Metadata evolution tracking accuracy validated
- [ ] Quality metrics compliance assessment performed  
- [ ] Cross-system integration consistency analyzed
- [ ] Metadata maintenance tracking established

### Quality Metrics

| Metric                              | Target | Actual         | Assessment |
| ----------------------------------- | ------ | -------------- | ---------- |
| Metadata Consistency Rate          | 100%   | [Actual Value] | ✅/❌      |
| Quality Compliance Score            | 95%    | [Actual Value] | ✅/❌      |
| System Synchronization Rate        | 100%   | [Actual Value] | ✅/❌      |

**MCP-Enhanced Metrics (if MCP Available):**
| Metric | Target | Actual | Assessment |
|--------|--------|--------|------------|
| Metadata Pattern Recognition Coverage | 95% | [Actual Value] | ✅/❌ |
| Automated Quality Assessment Accuracy | 90% | [Actual Value] | ✅/❌ |
| Context7 Standards Integration | 95% | [Actual Value] | ✅/❌ |
| Cross-Reference Validation Accuracy | 100% | [Actual Value] | ✅/❌ |

## 📊 Standardized Output Format

### 実行サマリー (日本語でユーザーに報告)

**基本機能 (常に実行):**

- ✅ **メタデータ整合性分析**: [X]個のメタデータソース、[Y]個の整合性ポイントを検証完了
- ✅ **品質基準適合**: [A]%の品質基準適合、[B]個の同期検証を達成
- ✅ **システム同期**: 完全なシステム状態同期と一貫性確認を実行
- ✅ **調整品質**: 包括的メタデータ調整と品質保証を完了

**MCP 拡張機能 (利用可能時):**

- ✅ **MCPメタデータパターン分析**: [X]個のパターン、[Y]個の調整インサイト分析完了
- ✅ **インテリジェント品質評価**: [A]個の最適化推奨、[B]個の改善戦略を生成
- ✅ **Context7基準統合**: プロフェッショナル品質基準適用完了
- ✅ **クロスリファレンス検証**: [C]個の依存関係、[D]個の整合性ポイント検証

### 成果物

**基本ファイル (常に作成):**

- `docs/emergency/metadata-reconciliation-report-YYYYMMDD.md`: メタデータ調整レポート
- Updated metadata files: 全メタデータファイルの同期完了

**MCP 拡張ファイル (利用可能時):**

- `docs/emergency/metadata-reconciliation-report-YYYYMMDD-mcp-intelligence.md`: MCPメタデータ調整インテリジェンス分析
- `docs/emergency/metadata-reconciliation-report-YYYYMMDD-intelligence-report.md`: メタデータ調整インテリジェンス詳細レポート
- Updated MCP memory files: メタデータ調整分析結果の永続化

### 総合判定

**ステータス**: `SUCCESS` (基本) / `MCP_ENHANCED_SUCCESS` (MCP 利用時)
**メタデータ調整品質スコア**: [スコア]/100
**MCP メタデータ インテリジェンス品質**: [スコア]/100 (利用時のみ)
**システム同期準備度**: `READY` / `OPTIMIZATION_RECOMMENDED`

### 次のステップ (日本語でユーザーに案内)

1. **即座に実行可能**: `/review-emergency-recovery` で最終復旧レビュー実行
2. **推奨**: メタデータ調整結果確認と追加最適化
3. **確認推奨**: メタデータ調整結果の開発チーム共有

**ユーザーへのメッセージ (日本語)**:

```
🎉 包括的メタデータ調整完了！

🏆 メタデータ調整総合評価: [Grade] ([Score]/100点)

📊 メタデータ調整分析結果:
   📈 整合性達成率: [X]% (目標100%)
   📈 品質基準適合: [Y]%の高品質同期
   📈 システム同期: [Z]%の完全な状態同期
   📈 調整品質: [A]%の包括的調整

✅ 品質検証分析結果:
   ✅ メタデータパターン検証: [B]% 精度達成
   ✅ システム同期検証: [C]件の包括的同期確認
   ✅ 品質基準適合: [D]個の基準クリア完了
   ✅ 調整統合: [E]% 統合準備完了

📋 メタデータ調整インサイト:
   💡 主要調整カテゴリ: [調整完了の主要領域]
   💡 品質向上度: [品質改善と最適化効果]
   💡 システム安定性: [システム同期改善機会]
   💡 統合推奨: [システム統合優先項目]

🧠 MCPメタデータ強化機能 (利用時のみ):
   📊 Serena分析: [X]パターン、[Y]調整インサイト分析
   🔍 品質評価インテリジェンス: [A]個の改善機会発見
   📋 Context7統合: プロフェッショナル品質基準適用
   🌐 クロスリファレンス: [B]個の依存関係検証完了
   ✅ docs/emergency/metadata-reconciliation-report-YYYYMMDD-mcp-intelligence.md
   ✅ docs/emergency/metadata-reconciliation-report-YYYYMMDD-intelligence-report.md
   ✅ MCP メモリファイル更新

📁 調整完了項目:
   ✅ 緊急復旧メタデータ: 完全同期済み
   ✅ システム状態整合: 完全一貫性確認済み
   ✅ 品質指標更新: 最新状態反映済み
   ✅ 実行履歴同期: 完全追跡可能済み
   ✅ [追加調整項目一覧...]

🚀 メタデータ統合推奨アクション:
   ⚡ 即座確認: [クリティカル同期確認項目]
   🎯 短期フォロー: [1-2週間最適化]
   📈 中長期統合: [システム統合改善計画]

📈 標準ワークフロー復帰準備:
   🎯 最終レビュー: [復旧レビュー優先度]
   📊 品質保証: [品質ゲート復旧計画]
   🔄 プロセス統合: [標準プロセス復帰計画]

✅ メタデータ調整完了 - 最終復旧レビュー実行準備完了！
```

## Common Errors and Solutions

### ❌ Error Case 1: Metadata file synchronization conflicts detected
**Cause**: Inconsistent metadata between different system sources  
**Solution**: 
- Review metadata conflict resolution strategies
- Apply priority-based reconciliation with backup creation
- Validate metadata integrity after conflict resolution

### ❌ Error Case 2: JSON syntax validation failures
**Cause**: Corrupted or invalid JSON in metadata files  
**Solution**: 
- Restore from backup files if available
- Manually correct JSON syntax errors
- Re-validate all metadata file integrity

### ❌ Error Case 3: System state synchronization failures
**Cause**: Metadata does not accurately reflect current system state  
**Solution**: 
- Review system state analysis accuracy
- Update metadata to match actual system conditions
- Re-run synchronization validation tests

### ❌ Error Case 4: MCP session not available
**Cause**: Enhanced MCP features not accessible  
**Solution**: Initialize MCP session first:
```bash
/context-session-stageup
```

## Execution Examples

### ✅ Success Example - Full MCP-Enhanced Metadata Reconciliation
```bash
$ /metadata-reconcile-enhanced --scope comprehensive
✅ MCP強化メタデータ調整を開始します

🧠 MCP分析機能:
  📊 Serena: メタデータ分析とパターンインテリジェンス
  🌐 Context7: プロフェッショナル品質基準統合

📊 メタデータ整合性分析中...
  - 検証されたメタデータソース: 5/5完了
  - 品質指標評価: docs/metadata/ 全ファイル検証済み
  - システム同期: 実行履歴とプロジェクト状態同期確認済み

🧠 MCPメタデータパターン分析中...
  ✅ パターン分析: 8件の履歴パターン検証完了
  ✅ 品質基準適合: 98% 適合率達成
  ✅ 調整戦略: プロフェッショナル基準適用

📊 システム状態同期中...
  ✅ JSON構文検証: 全5ファイル成功 (整合性 100%)
  ✅ データ整合性: 完全な一貫性確認
  ✅ メタデータ進化: 全履歴追跡更新済み

🌐 Context7品質基準統合中...
  ✅ プロフェッショナルメタデータ基準適用
  ✅ 業界標準同期フレームワーク
  ✅ 品質保証チェックリスト統合

✅ 調整品質検証中...
  ✅ システム同期: 完全一貫性確認済み
  ✅ メタデータ進化: 標準ワークフロー復帰準備完了
  ✅ 品質指標: 全依存関係検証済み

✅ MCP強化メタデータ調整完了!

📋 メタデータ調整サマリー (整合性達成率: 100%)
==========================================
📊 調整完了項目:
  ✅ プロジェクト状態メタデータ: 完全同期済み (Score: 98.7/100)
  ✅ システムコンテキスト: 完全一貫性確認済み (Score: 99.2/100)
  ✅ 実行履歴同期: 完全追跡可能済み (Score: 97.8/100)
  ✅ 品質指標更新: 最新状態反映済み (Score: 98.5/100)

🔗 システム整合性検証:
  ✅ JSON構文検証: 全ファイル正常 (Score: 100/100)
  ✅ データ整合性: 100% (目標100%達成)
  ✅ メタデータ一貫性: 完全整合性確認

🧠 MCP強化レポート:
  ✅ docs/emergency/metadata-reconciliation-report-20231201-mcp-intelligence.md
  ✅ docs/emergency/metadata-reconciliation-report-20231201-intelligence-report.md
  ✅ MCP メモリファイル更新

次のステップ: /review-emergency-recovery --enhanced
```