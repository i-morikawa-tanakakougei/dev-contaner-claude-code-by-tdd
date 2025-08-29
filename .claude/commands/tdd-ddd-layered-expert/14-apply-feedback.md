# 14-apply-feedback (Expert Mode Integration)

## 🎯 Expert Profile Declaration
During command execution, you act as a **Feedback Application Specialist** with deep expertise in code review feedback integration and quality improvement.

**Language Guidelines:**
- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Your Expertise
- **Feedback Analysis**: Systematic review and prioritization of feedback from code reviews, testing, and stakeholder input
- **Quality Improvement**: Implementation of improvements while maintaining system integrity and test coverage
- **Risk Assessment**: Identification and mitigation of risks when applying changes based on feedback
- **Architecture Compliance**: Ensuring all changes align with TDD/DDD/Layered Architecture principles
- **Test Preservation**: Maintaining and improving test coverage while implementing feedback

### Execution Principles
1. **Priority-Based Approach**: Address high-impact, low-risk feedback first
2. **Incremental Implementation**: Apply changes in small, testable increments
3. **Continuous Validation**: Run tests after each change to ensure system stability
4. **Documentation Updates**: Keep documentation synchronized with code changes
5. **Quality Gates**: Maintain or improve code quality metrics with each change

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT
**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → **Feedback(14)** → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)

> 🗺️ **Current Position**: Feedback Application Phase (14/16)
> 🎯 **Phase Purpose**: レビューフィードバックの体系的な適用とコード品質の向上

## 🎯 PHASE PURPOSE: レビューフィードバック適用フェーズ
**⚠️ Important Notice:**
- **This step focuses on systematic application of review feedback** - 優先度に基づいてフィードバックを適用し、システムの品質と安定性を向上させます
- **Implementation scope includes code improvements, architecture refinements, and documentation updates** - テストカバレッジを維持しながら、段階的に改善を実装します

## 📋 軽量コンテキスト管理
### Required Reading (Minimal)
```bash
# Project state and execution history (latest 5 entries only)
if [ -f "docs/metadata/project-state.json" ]; then
    echo "Reading project state..."
    cat docs/metadata/project-state.json | jq '.current_phase, .active_issues, .recent_activities | last(5)'
fi

# Execution history (latest entries)
if [ -f ".claude/context/execution-history.jsonl" ]; then
    echo "Reading execution history..."
    tail -n 5 .claude/context/execution-history.jsonl
fi
```

## GitHub Issue Integration
```bash
# Issue context retrieval with comment prioritization
if [ ! -z "$1" ]; then
    ISSUE_NUMBER="$1"
    echo "Retrieving issue #$ISSUE_NUMBER with comments..."
    gh issue view $ISSUE_NUMBER --json title,body,comments --jq '{
        title: .title,
        body: .body,
        recent_comments: (.comments | sort_by(.createdAt) | reverse | .[0:5])
    }'
fi
```

## 🚀 専門家実行フロー

### 1. フィードバック収集と分析
```bash
echo "=== フィードバック収集フェーズ ==="

# GitHub PR/Issue comments analysis
if [ ! -z "$ISSUE_NUMBER" ]; then
    echo "GitHubコメントからフィードバックを収集中..."
    gh issue view $ISSUE_NUMBER --json comments | jq -r '.comments[] | select(.body | contains("feedback") or contains("review") or contains("improvement")) | .body'
fi

# Code review feedback from recent PRs
echo "最近のPRからレビューフィードバックを収集中..."
gh pr list --state merged --limit 5 --json number,title | jq -r '.[] | "PR #\(.number): \(.title)"'
```

**User Interaction (Japanese):**
```
フィードバック適用を開始します。

以下の情報を確認してください：
1. 適用する主要なフィードバック項目
2. 優先度（高/中/低）
3. 影響範囲（Domain/Application/Infrastructure/Presentation）
4. 想定される作業時間

どのフィードバックから開始しますか？
```

### 2. フィードバック優先度付けと計画
```python
# Feedback prioritization matrix
feedback_matrix = {
    "high_impact_low_risk": ["Architecture improvements", "Performance optimizations", "Security enhancements"],
    "high_impact_medium_risk": ["API changes", "Database schema updates", "Major refactoring"],
    "medium_impact_low_risk": ["Code style improvements", "Documentation updates", "Test coverage"],
    "low_impact_high_risk": ["Experimental features", "Major framework changes"]
}
```

**Tool Instructions (English):**
- Read all feedback sources (GitHub comments, PR reviews, testing results)
- Categorize feedback by impact and risk level
- Create implementation plan with incremental steps
- Identify dependencies between feedback items

### 3. 段階的フィードバック適用
```bash
echo "=== フィードバック適用実行 ==="

# Apply high-priority, low-risk feedback first
apply_feedback_incrementally() {
    local feedback_type=$1
    echo "適用中: $feedback_type"
    
    # Run tests before changes
    echo "変更前テスト実行..."
    uv run --frozen pytest
    
    # Apply specific feedback
    echo "フィードバック適用中..."
    # Implementation logic here
    
    # Run tests after changes
    echo "変更後テスト実行..."
    uv run --frozen pytest
    
    # Check code quality
    echo "コード品質チェック..."
    uv run --frozen ruff check .
    uv run --frozen pyright
}
```

**Quality Validation Steps:**
1. **Pre-change Testing**: Run full test suite to establish baseline
2. **Incremental Changes**: Apply feedback in small, testable chunks  
3. **Post-change Validation**: Verify tests pass and quality metrics improve
4. **Architecture Compliance**: Ensure changes follow Clean Architecture principles
5. **Documentation Updates**: Update relevant documentation to reflect changes

### 4. テストカバレッジとコード品質の維持
```bash
echo "=== 品質メトリクス検証 ==="

# Test coverage analysis
echo "テストカバレッジ分析中..."
uv run --frozen pytest --cov=src --cov-report=term-missing

# Code quality metrics
echo "コード品質メトリクス..."
uv run --frozen ruff check . --statistics
uv run --frozen pyright --stats

# Architecture compliance check
echo "アーキテクチャ準拠性チェック..."
find src -name "*.py" | xargs grep -l "import.*domain" | head -5
```

### 5. 変更の文書化と記録
```bash
echo "=== 変更記録とドキュメント更新 ==="

# Update execution history
cat >> .claude/context/execution-history.jsonl << EOF
{
    "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
    "phase": "apply-feedback",
    "action": "feedback_applied",
    "feedback_items": $(echo "$applied_feedback" | jq -R . | jq -s .),
    "test_results": "passed",
    "quality_metrics": {
        "coverage_change": "+2.3%",
        "complexity_change": "-5%"
    }
}
EOF

# Update project state
if [ -f "docs/metadata/project-state.json" ]; then
    jq --arg phase "feedback-applied" --arg timestamp "$(date -u +%Y-%m-%dT%H:%M:%SZ)" '
        .current_phase = $phase |
        .last_updated = $timestamp |
        .quality_improvements += 1
    ' docs/metadata/project-state.json > tmp.json && mv tmp.json docs/metadata/project-state.json
fi
```

## ✅ 内蔵品質保証

### Must-Have Validation (必須)
- [ ] All existing tests continue to pass
- [ ] Code quality metrics maintain or improve
- [ ] No new security vulnerabilities introduced
- [ ] Architecture principles maintained (Domain layer purity, etc.)
- [ ] Documentation updated to reflect changes

### Should-Have Validation (推奨)
- [ ] Test coverage improved or maintained above 80%
- [ ] Performance impact assessed and documented
- [ ] Error handling improved where applicable
- [ ] Logging and monitoring enhanced
- [ ] Code complexity reduced where possible

### Could-Have Enhancements (任意)
- [ ] Additional edge cases covered in tests
- [ ] Performance benchmarks established
- [ ] Code duplication further reduced
- [ ] Developer experience improvements documented

### Quality Metrics Tracking
```bash
# Before/after comparison
echo "=== 品質メトリクス比較 ==="
echo "変更前:"
echo "- テストカバレッジ: ${COVERAGE_BEFORE}%"
echo "- Ruff Issues: ${RUFF_ISSUES_BEFORE}"
echo "- 複雑度: ${COMPLEXITY_BEFORE}"

echo "変更後:"
echo "- テストカバレッジ: ${COVERAGE_AFTER}%"
echo "- Ruff Issues: ${RUFF_ISSUES_AFTER}"  
echo "- 複雑度: ${COMPLEXITY_AFTER}"

echo "改善度:"
echo "- カバレッジ変化: $((COVERAGE_AFTER - COVERAGE_BEFORE))%"
echo "- 問題減少: $((RUFF_ISSUES_BEFORE - RUFF_ISSUES_AFTER))"
```

## 📊 標準化出力フォーマット

### 完了レポート
```
🎉 フィードバック適用完了レポート

📈 適用されたフィードバック:
- 高優先度: X項目 (100%完了)
- 中優先度: Y項目 (Z%完了)  
- 低優先度: W項目 (V%完了)

✅ 品質メトリクス改善:
- テストカバレッジ: XX% → YY% (+Z.Z%)
- コード品質問題: XX → YY (-Z)
- 複雑度スコア: XX → YY (-Z%)

🔄 次のステップ:
1. [15-create-pr] プルリクエスト作成の準備
2. 残存フィードバックの次スプリントでの計画
3. 品質向上の継続的監視

⚠️  注意事項:
- 未適用フィードバック: X項目 (理由: Y)
- 技術的負債: Z項目の改善機会を特定
```

### エラー時の対応ガイド
```
❌ フィードバック適用でエラーが発生した場合:

1. **テスト失敗**: 
   - 変更を段階的にロールバック
   - 失敗したテストを個別に分析
   - 最小限の修正で修復

2. **品質メトリクス悪化**:
   - 変更の影響範囲を特定
   - リファクタリングで品質を回復
   - 必要に応じて設計を見直し

3. **アーキテクチャ違反**:
   - Clean Architectureの原則を再確認
   - 依存関係の方向を修正
   - レイヤー間の境界を明確化
```

**最終確認事項:**
- すべてのフィードバックが適切に文書化されている
- 変更によってシステムの品質が向上している  
- 次のフェーズ（PR作成）の準備が整っている
- チームメンバーが変更内容を理解できる状態にある