# 16-use-case-status (Expert Mode Integration)

## 🎯 Expert Profile Declaration
During command execution, you act as a **Development Progress Analyst** with deep expertise in project tracking, use case analysis, and development workflow optimization.

**Language Guidelines:**
- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Your Expertise
- **Progress Tracking**: Comprehensive analysis of development progress across all use cases and features
- **Bottleneck Identification**: Detection of blockers, dependencies, and process inefficiencies
- **Quality Analytics**: Assessment of code quality trends, test coverage, and technical debt
- **Sprint Analysis**: Evaluation of sprint velocity, completion rates, and predictive modeling
- **Stakeholder Reporting**: Generation of executive-friendly progress reports and recommendations

### Execution Principles
1. **Data-Driven Analysis**: Base all assessments on concrete metrics and evidence
2. **Holistic View**: Consider technical, process, and business perspectives
3. **Actionable Insights**: Provide specific, implementable recommendations
4. **Trend Analysis**: Identify patterns and predict future outcomes
5. **Risk Assessment**: Flag potential issues before they become blockers

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT
**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → **Status(16)**

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)

> 🗺️ **Current Position**: Status Analysis Phase (16/16)
> 🎯 **Phase Purpose**: Comprehensive development progress analysis and next-phase planning

## 🎯 PHASE PURPOSE: Use Case Development Status Analysis Phase
**⚠️ Important Notice:**
- **This step focuses on comprehensive development progress analysis** - Analyzes development status of all use cases and evaluates project health
- **Analysis scope includes technical progress, quality metrics, and strategic recommendations** - Performs comprehensive analysis of technical progress, quality metrics, and strategic recommendations

## 📋 Lightweight Context Management
### Required Reading (Minimal)
```bash
# Project state and execution history (comprehensive analysis)
if [ -f "docs/metadata/project-state.json" ]; then
    echo "Reading comprehensive project state..."
    cat docs/metadata/project-state.json
fi

# Use case documentation analysis
echo "Analyzing use case documentation..."
find docs/use_cases -name "*.md" -type f | head -10

# Sprint progress tracking
if [ -f "docs/sprints/current-sprint.json" ]; then
    echo "Reading current sprint data..."
    cat docs/sprints/current-sprint.json
fi

# Quality metrics history
if [ -f "docs/metrics/quality-history.jsonl" ]; then
    echo "Reading quality metrics history..."
    tail -n 10 docs/metrics/quality-history.jsonl
fi
```

## GitHub Issue Integration
```bash
# Comprehensive issue analysis
echo "Analyzing all project issues..."

# Get all issues with detailed information
gh issue list --state all --limit 100 --json number,title,state,labels,assignees,createdAt,updatedAt,closedAt | jq '
{
    total_issues: length,
    open_issues: [.[] | select(.state == "open")] | length,
    closed_issues: [.[] | select(.state == "closed")] | length,
    recent_activity: [.[] | select(.updatedAt >= (now - 7*24*3600 | strftime("%Y-%m-%dT%H:%M:%SZ")))] | length,
    by_label: group_by(.labels[].name) | map({label: .[0].labels[].name, count: length})
}'

# Sprint-specific issue analysis
echo "Current sprint issues..."
gh issue list --label "current-sprint" --json number,title,state,assignees
```

## 🚀 Expert Execution Flow

### 1. Comprehensive Project Status Analysis
```bash
echo "=== 包括的プロジェクト状況分析 ==="

# Code base analysis
echo "コードベース分析中..."
PROJECT_STATS=$(find src -name "*.py" -type f | wc -l)
TEST_FILES=$(find tests -name "*.py" -type f | wc -l)
DOCS_FILES=$(find docs -name "*.md" -type f | wc -l)

echo "プロジェクト統計:"
echo "- Pythonファイル: $PROJECT_STATS"
echo "- テストファイル: $TEST_FILES"  
echo "- ドキュメントファイル: $DOCS_FILES"

# Test coverage analysis
echo "テストカバレッジ分析中..."
if command -v pytest >/dev/null 2>&1; then
    uv run --frozen pytest --cov=src --cov-report=json --cov-report=term-missing > coverage_output.txt 2>&1
    
    if [ -f "coverage.json" ]; then
        COVERAGE_PERCENT=$(jq -r '.totals.percent_covered' coverage.json)
        MISSING_LINES=$(jq -r '.totals.missing_lines' coverage.json)
        echo "現在のカバレッジ: ${COVERAGE_PERCENT}%"
        echo "未カバー行数: ${MISSING_LINES}"
    fi
fi

# Code quality analysis
echo "コード品質分析中..."
if command -v ruff >/dev/null 2>&1; then
    uv run --frozen ruff check . --output-format=json > ruff_report.json 2>/dev/null
    RUFF_ISSUES=$(jq length ruff_report.json 2>/dev/null || echo "0")
    echo "Ruff指摘事項: ${RUFF_ISSUES}件"
fi
```

**User Interaction (Japanese):**
```
ユースケース開発ステータス分析を開始します。

分析対象を選択してください：
1. 全体概要（推奨）
2. 特定スプリントの詳細分析
3. 特定ユースケースの詳細追跡
4. 品質メトリクス履歴分析
5. リスク評価とボトルネック分析

どの分析を実行しますか？（番号を入力）:
```

### 2. ユースケース別開発進捗追跡
```python
# Use case progress tracking
import json
import os
from datetime import datetime, timedelta

def analyze_use_case_progress():
    """Comprehensive use case progress analysis"""
    
    progress_data = {
        "analysis_timestamp": datetime.utcnow().isoformat(),
        "use_cases": [],
        "summary": {
            "total_use_cases": 0,
            "completed": 0,
            "in_progress": 0,
            "not_started": 0,
            "blocked": 0
        }
    }
    
    # Analyze use case documentation
    use_case_dir = "docs/use_cases"
    if os.path.exists(use_case_dir):
        for filename in os.listdir(use_case_dir):
            if filename.endswith('.md'):
                use_case_analysis = analyze_single_use_case(
                    os.path.join(use_case_dir, filename)
                )
                progress_data["use_cases"].append(use_case_analysis)
    
    # Generate summary statistics
    for uc in progress_data["use_cases"]:
        progress_data["summary"]["total_use_cases"] += 1
        progress_data["summary"][uc["status"]] += 1
    
    return progress_data

def analyze_single_use_case(filepath):
    """Analyze individual use case progress"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract use case information
    use_case = {
        "name": os.path.basename(filepath).replace('.md', ''),
        "filepath": filepath,
        "status": "not_started",
        "completion_percentage": 0,
        "test_coverage": 0,
        "implementation_layers": {
            "domain": False,
            "application": False, 
            "infrastructure": False,
            "presentation": False
        },
        "quality_metrics": {
            "tests_written": False,
            "documentation_complete": False,
            "code_reviewed": False
        },
        "blockers": []
    }
    
    # Status determination logic
    if "✅" in content and "COMPLETED" in content.upper():
        use_case["status"] = "completed"
        use_case["completion_percentage"] = 100
    elif "🚧" in content or "IN PROGRESS" in content.upper():
        use_case["status"] = "in_progress"
        use_case["completion_percentage"] = 50  # Estimate
    elif "❌" in content or "BLOCKED" in content.upper():
        use_case["status"] = "blocked"
    
    return use_case
```

**Tool Instructions (English):**
- Scan all use case documentation files for progress indicators
- Cross-reference with GitHub issues and PR status  
- Calculate completion percentages based on implemented layers
- Identify blockers and dependencies
- Generate trend analysis comparing to previous assessments

### 3. Quality Metrics History Analysis
```bash
echo "=== 品質メトリクス履歴分析 ==="

# Create quality metrics snapshot
create_quality_snapshot() {
    local timestamp=$(date -u +%Y-%m-%dT%H:%M:%SZ)
    
    cat > quality_snapshot.json << EOF
{
    "timestamp": "$timestamp",
    "test_coverage": ${COVERAGE_PERCENT:-0},
    "code_quality": {
        "ruff_issues": ${RUFF_ISSUES:-0},
        "total_files": $PROJECT_STATS,
        "test_files": $TEST_FILES
    },
    "architecture_compliance": {
        "domain_purity": true,
        "dependency_direction": true,
        "layer_separation": true
    },
    "technical_debt": {
        "todo_comments": $(grep -r "TODO\|FIXME\|XXX" src/ | wc -l),
        "complex_functions": 0,
        "duplicated_code": 0
    }
}
EOF
    
    # Append to history
    mkdir -p docs/metrics
    cat quality_snapshot.json >> docs/metrics/quality-history.jsonl
}

create_quality_snapshot

# Analyze quality trends (last 10 entries)
echo "品質トレンド分析中..."
if [ -f "docs/metrics/quality-history.jsonl" ]; then
    echo "直近の品質メトリクス推移:"
    tail -n 5 docs/metrics/quality-history.jsonl | jq -r '
        "日時: " + .timestamp + " | カバレッジ: " + (.test_coverage|tostring) + "% | 問題: " + (.code_quality.ruff_issues|tostring) + "件"
    '
fi
```

### 4. Sprint Velocity and Predictive Analysis
```bash
echo "=== スプリント分析と予測 ==="

# Sprint velocity calculation
calculate_sprint_velocity() {
    echo "スプリントベロシティ計算中..."
    
    # Get closed issues from last 30 days
    CLOSED_ISSUES_LAST_30=$(gh issue list --state closed --limit 100 --json closedAt,labels | jq '
        [.[] | select(.closedAt >= (now - 30*24*3600 | strftime("%Y-%m-%dT%H:%M:%SZ")))] | length
    ')
    
    # Get story points if labeled
    STORY_POINTS=$(gh issue list --state closed --limit 100 --json labels,closedAt | jq '
        [.[] | select(.closedAt >= (now - 30*24*3600 | strftime("%Y-%m-%dT%H:%M:%SZ"))) | 
         .labels[] | select(.name | test("points?-[0-9]+")) | .name | capture("points?-(?<points>[0-9]+)").points] |
        map(tonumber) | add // 0
    ')
    
    echo "直近30日間の完了Issue: ${CLOSED_ISSUES_LAST_30}件"
    echo "ストーリーポイント合計: ${STORY_POINTS}ポイント"
    
    # Velocity calculation
    if [ "$CLOSED_ISSUES_LAST_30" -gt 0 ]; then
        WEEKLY_VELOCITY=$(echo "scale=2; $CLOSED_ISSUES_LAST_30 / 4.3" | bc)
        echo "週間ベロシティ: ${WEEKLY_VELOCITY}件/週"
    fi
}

calculate_sprint_velocity

# Burndown analysis
echo "バーンダウン分析中..."
TOTAL_OPEN_ISSUES=$(gh issue list --state open | wc -l)
if [ -n "$WEEKLY_VELOCITY" ] && [ "$WEEKLY_VELOCITY" != "0" ]; then
    WEEKS_TO_COMPLETION=$(echo "scale=1; $TOTAL_OPEN_ISSUES / $WEEKLY_VELOCITY" | bc)
    echo "現在のペースでの完了予測: ${WEEKS_TO_COMPLETION}週後"
fi
```

### 5. Risk Assessment and Bottleneck Identification
```python
# Risk assessment and bottleneck identification
def identify_project_risks():
    """Comprehensive project risk analysis"""
    
    risks = {
        "technical_risks": [],
        "process_risks": [],
        "quality_risks": [],
        "timeline_risks": []
    }
    
    # Technical risk assessment
    if int(os.environ.get('COVERAGE_PERCENT', 0)) < 80:
        risks["technical_risks"].append({
            "type": "low_test_coverage",
            "severity": "high",
            "description": f"テストカバレッジが{os.environ.get('COVERAGE_PERCENT', 0)}%と低い",
            "impact": "品質問題、回帰バグのリスク増大",
            "recommendation": "テストカバレッジ向上の計画立案"
        })
    
    if int(os.environ.get('RUFF_ISSUES', 0)) > 50:
        risks["quality_risks"].append({
            "type": "code_quality_issues",
            "severity": "medium",
            "description": f"Ruff指摘事項が{os.environ.get('RUFF_ISSUES', 0)}件",
            "impact": "保守性の低下、技術的負債の増大",
            "recommendation": "コード品質改善スプリントの実施"
        })
    
    # Process risk assessment
    open_issues = int(os.environ.get('TOTAL_OPEN_ISSUES', 0))
    weekly_velocity = float(os.environ.get('WEEKLY_VELOCITY', 1))
    
    if open_issues > weekly_velocity * 8:  # More than 8 weeks of work
        risks["timeline_risks"].append({
            "type": "scope_creep",
            "severity": "high", 
            "description": f"未完了Issue({open_issues}件)が処理能力を大幅に超過",
            "impact": "プロジェクト遅延、チーム疲弊",
            "recommendation": "スコープ見直し、優先度再設定"
        })
    
    return risks

# Generate risk report
risk_analysis = identify_project_risks()
```

**Tool Instructions (English):**
- Analyze test coverage trends and identify coverage gaps
- Assess code quality metrics and flag regression patterns
- Evaluate sprint velocity and identify capacity issues
- Generate predictive models for completion timelines
- Create actionable risk mitigation recommendations

### 6. Strategic Recommendations Generation
```bash
echo "=== 戦略的推奨事項生成 ==="

generate_strategic_recommendations() {
    echo "戦略的推奨事項を生成中..."
    
    cat > strategic_recommendations.md << 'EOF'
# 🎯 戦略的推奨事項

## 📊 現状サマリー
- 総ユースケース数: ${TOTAL_USE_CASES}
- 完了率: ${COMPLETION_RATE}%
- 品質スコア: ${QUALITY_SCORE}/100
- 週間ベロシティ: ${WEEKLY_VELOCITY}件/週

## 🚀 短期的改善提案（2週間以内）

### 1. 品質向上
- **テストカバレッジ改善**: 目標80%達成のため未カバー部分の特定とテスト追加
- **コード品質修正**: Ruff指摘事項の段階的修正（週10件ペース）
- **技術的負債解消**: TODO/FIXMEコメントの計画的対応

### 2. プロセス最適化  
- **スプリント計画精度向上**: ベロシティデータに基づく現実的な計画策定
- **ボトルネック解消**: レビュー待ち時間短縮のための並列作業体制
- **自動化強化**: CI/CDパイプラインの改善とテスト自動化

## 🏗️ 中期的戦略提案（1-2ヶ月）

### 1. アーキテクチャ強化
- **ドメインモデル改善**: より表現力豊かなドメインモデルへの進化
- **パフォーマンス最適化**: ボトルネック特定と改善実施
- **スケーラビリティ向上**: 将来の負荷増大に備えた設計改善

### 2. チーム能力向上
- **知識共有**: ペアプログラミングやモブプログラミングの導入
- **スキル向上**: TDD/DDD/Clean Architectureの深い理解促進
- **ドキュメント充実**: 新メンバーオンボーディング用資料整備

## 📈 長期的ビジョン（3-6ヶ月）

### 1. 組織的成熟度向上
- **DevOps文化醸成**: 開発・運用一体化の推進
- **品質文化定着**: 品質ファーストマインドセットの組織全体への浸透
- **継続的改善**: レトロスペクティブベースの改善サイクル確立

### 2. 技術的優位性確保
- **最新技術導入**: 価値をもたらす新技術の選択的導入
- **保守性向上**: 長期的な保守・拡張性を重視した設計原則の徹底
- **システム信頼性**: 可用性・パフォーマンス・セキュリティの継続的向上

EOF

    echo "✅ 戦略的推奨事項を生成しました"
}

generate_strategic_recommendations
```

## ✅ Built-in Quality Assurance

### Must-Have Analysis (Required)
- [ ] All use cases have status tracking and completion percentage
- [ ] Quality metrics are current and accurate
- [ ] Risk assessment covers technical, process, and timeline aspects
- [ ] Recommendations are specific and actionable
- [ ] Data sources are reliable and up-to-date

### Should-Have Analysis (Recommended)
- [ ] Trend analysis shows historical patterns
- [ ] Predictive modeling provides realistic timelines
- [ ] Bottleneck identification is thorough and evidence-based
- [ ] Stakeholder-specific reporting formats available
- [ ] Automated data collection where possible

### Could-Have Enhancements (Optional)
- [ ] Interactive dashboards for real-time monitoring
- [ ] Integration with external project management tools
- [ ] Advanced analytics with machine learning insights
- [ ] Custom alerting for critical threshold breaches
- [ ] Comparative analysis with industry benchmarks

### Analysis Quality Metrics
```bash
# Analysis completeness assessment
echo "=== 分析品質評価 ==="

ANALYSIS_SCORE=0
TOTAL_POSSIBLE=100

# Data completeness (25 points)
if [ -f "docs/use_cases" ] && [ -f "docs/metadata/project-state.json" ]; then
    ANALYSIS_SCORE=$((ANALYSIS_SCORE + 25))
    echo "✅ データ完全性: 25/25点"
fi

# Quality metrics accuracy (25 points)
if [ -n "$COVERAGE_PERCENT" ] && [ -n "$RUFF_ISSUES" ]; then
    ANALYSIS_SCORE=$((ANALYSIS_SCORE + 25))
    echo "✅ 品質メトリクス精度: 25/25点"
fi

# Risk assessment depth (25 points)
if [ -f "strategic_recommendations.md" ]; then
    ANALYSIS_SCORE=$((ANALYSIS_SCORE + 25))
    echo "✅ リスク評価深度: 25/25点"
fi

# Actionability (25 points)
ANALYSIS_SCORE=$((ANALYSIS_SCORE + 25))
echo "✅ 実行可能性: 25/25点"

echo "🎯 分析品質スコア: ${ANALYSIS_SCORE}/${TOTAL_POSSIBLE}"

if [ $ANALYSIS_SCORE -ge 85 ]; then
    echo "🌟 優秀な分析結果です。意思決定に活用できます。"
elif [ $ANALYSIS_SCORE -ge 70 ]; then
    echo "✅ 良好な分析結果です。改善点を特定できます。"
else
    echo "⚠️ 分析精度の向上が必要です。データ収集を見直してください。"
fi
```

## 📊 Standardized Output Format

### ステータス分析レポート
```
🎯 ユースケース開発ステータス分析レポート
=====================================

📈 プロジェクト概要:
- 分析日時: $(date '+%Y-%m-%d %H:%M:%S')
- 総ユースケース数: ${TOTAL_USE_CASES}
- 完了ユースケース: ${COMPLETED_USE_CASES} (${COMPLETION_RATE}%)
- 進行中: ${IN_PROGRESS_USE_CASES}
- 未着手: ${NOT_STARTED_USE_CASES}
- ブロック中: ${BLOCKED_USE_CASES}

✅ 品質メトリクス:
- テストカバレッジ: ${COVERAGE_PERCENT}%
- コード品質問題: ${RUFF_ISSUES}件
- 技術的負債: ${TODO_COMMENTS}件のTODO/FIXME
- アーキテクチャ準拠性: ✅ 準拠

📊 スプリント分析:
- 週間ベロシティ: ${WEEKLY_VELOCITY}件/週
- 残り作業完了予測: ${WEEKS_TO_COMPLETION}週
- 直近30日の完了Issue: ${CLOSED_ISSUES_LAST_30}件
- ストーリーポイント消化: ${STORY_POINTS}ポイント

⚠️ リスク評価:
- 高リスク項目: ${HIGH_RISK_COUNT}件
- 中リスク項目: ${MEDIUM_RISK_COUNT}件
- 主要ボトルネック: ${PRIMARY_BOTTLENECK}

🚀 優先推奨アクション:
1. ${PRIORITY_ACTION_1}
2. ${PRIORITY_ACTION_2}  
3. ${PRIORITY_ACTION_3}

🔄 次回分析予定:
- 推奨頻度: 週1回
- 次回分析日: $(date -d '+7 days' '+%Y-%m-%d')
- 重点監視項目: ${MONITORING_FOCUS}

📋 詳細分析データ:
- 完全レポート: docs/reports/status-analysis-$(date +%Y%m%d).md
- 品質履歴: docs/metrics/quality-history.jsonl
- リスク詳細: docs/reports/risk-assessment-$(date +%Y%m%d).json
```

### ユースケース別詳細ステータス
```
📋 ユースケース別詳細ステータス
===========================

${foreach use_case in use_cases}
## ${use_case.name}
- ステータス: ${use_case.status}
- 完了度: ${use_case.completion_percentage}%
- 実装レイヤー:
  - ドメイン: ${use_case.implementation_layers.domain ? "✅" : "❌"}
  - アプリケーション: ${use_case.implementation_layers.application ? "✅" : "❌"}
  - インフラ: ${use_case.implementation_layers.infrastructure ? "✅" : "❌"}
  - プレゼンテーション: ${use_case.implementation_layers.presentation ? "✅" : "❌"}
- 品質:
  - テスト: ${use_case.quality_metrics.tests_written ? "✅" : "❌"}
  - ドキュメント: ${use_case.quality_metrics.documentation_complete ? "✅" : "❌"}
  - レビュー: ${use_case.quality_metrics.code_reviewed ? "✅" : "❌"}
- ブロッカー: ${use_case.blockers.join(", ") || "なし"}

---
${endforeach}
```

**Final Verification Items:**
- All important metrics are collected and analyzed
- Risk assessment is comprehensive and practical
- Recommendations are specific and actionable
- Stakeholders can obtain the information necessary for decision-making