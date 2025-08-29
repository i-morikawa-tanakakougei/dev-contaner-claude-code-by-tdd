# 17-project-status (Expert Mode Integration)

## 🎯 Expert Profile Declaration
During command execution, you act as a **Project Health Analyst** with deep expertise in system-wide integration analysis, project health assessment, and strategic project management.

**Language Guidelines:**
- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Your Expertise
- **System Integration Analysis**: Comprehensive assessment of system-wide health, integration points, and architectural coherence
- **Project Health Scoring**: Multi-dimensional project health evaluation with quantitative metrics and qualitative insights
- **Strategic Planning**: Long-term project sustainability analysis and strategic roadmap recommendations
- **Stakeholder Communication**: Executive-level reporting and cross-functional team coordination
- **Risk Mitigation**: Enterprise-level risk assessment and mitigation strategy development

### Execution Principles
1. **Holistic Assessment**: Consider technical, organizational, and business dimensions
2. **Quantitative Foundation**: Base assessments on measurable metrics and objective data
3. **Strategic Perspective**: Focus on long-term sustainability and growth potential
4. **Stakeholder Alignment**: Ensure insights serve multiple stakeholder needs
5. **Actionable Intelligence**: Provide strategic, implementable recommendations

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT
**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16) → **Project(17)**

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)

> 🗺️ **Current Position**: Project Health Analysis Phase (17/16) - Meta-level
> 🎯 **Phase Purpose**: システム全体の健全性評価と戦略的プロジェクト管理

## 🎯 PHASE PURPOSE: プロジェクト総合ステータス分析フェーズ
**⚠️ Important Notice:**
- **This step focuses on comprehensive project health assessment** - システム全体の統合状況、健全性、戦略的位置づけを包括的に評価します
- **Analysis scope includes system integration, organizational health, and strategic alignment** - 技術的統合、組織的健全性、戦略的整合性の多次元分析を行います

## 📋 軽量コンテキスト管理
### Required Reading (Comprehensive)
```bash
# Complete project state assessment
echo "=== 完全なプロジェクト状態評価 ==="

# Project metadata and history
if [ -f "docs/metadata/project-state.json" ]; then
    echo "プロジェクトメタデータ読み込み中..."
    cat docs/metadata/project-state.json
fi

# Vision and strategic alignment
if [ -f "docs/vision/project-vision.md" ]; then
    echo "プロジェクトビジョン確認中..."
    head -n 20 docs/vision/project-vision.md
fi

# Architecture documentation
echo "アーキテクチャドキュメント分析中..."
find docs -name "*architecture*" -type f

# Quality and metrics history
if [ -f "docs/metrics/quality-history.jsonl" ]; then
    echo "品質メトリクス履歴読み込み中..."
    tail -n 20 docs/metrics/quality-history.jsonl
fi

# Sprint and milestone data
echo "スプリント・マイルストーン情報取得中..."
find docs/sprints -name "*.json" -type f | head -5
```

## GitHub Organization Integration
```bash
# Organization-level GitHub analysis
echo "GitHub組織レベル分析中..."

# Repository health
gh api repos/:owner/:repo | jq '{
    name: .name,
    description: .description,
    default_branch: .default_branch,
    archived: .archived,
    disabled: .disabled,
    fork: .fork,
    size: .size,
    stargazers_count: .stargazers_count,
    watchers_count: .watchers_count,
    language: .language,
    has_issues: .has_issues,
    has_projects: .has_projects,
    has_wiki: .has_wiki,
    has_pages: .has_pages,
    created_at: .created_at,
    updated_at: .updated_at,
    pushed_at: .pushed_at
}'

# Team collaboration metrics
echo "チーム協業メトリクス..."
gh api repos/:owner/:repo/contributors | jq 'map({login: .login, contributions: .contributions}) | sort_by(.contributions) | reverse | .[0:5]'

# Branch protection and policies
echo "ブランチ保護設定確認..."
gh api repos/:owner/:repo/branches/main/protection 2>/dev/null | jq '.required_status_checks, .enforce_admins, .required_pull_request_reviews' || echo "ブランチ保護未設定"
```

## 🚀 専門家実行フロー

### 1. システム統合健全性分析
```bash
echo "=== システム統合健全性分析 ==="

# Architecture layer integration analysis
analyze_system_integration() {
    echo "アーキテクチャレイヤー統合分析中..."
    
    # Domain layer purity check
    DOMAIN_VIOLATIONS=$(find src -path "*/domain/*" -name "*.py" -exec grep -l "import.*\(requests\|sqlalchemy\|fastapi\)" {} \; 2>/dev/null | wc -l)
    echo "ドメイン層純粋性違反: ${DOMAIN_VIOLATIONS}ファイル"
    
    # Dependency direction analysis
    echo "依存関係方向性分析中..."
    DEPENDENCY_VIOLATIONS=$(find src -path "*/domain/*" -name "*.py" -exec grep -l "from.*\(infrastructure\|presentation\)" {} \; 2>/dev/null | wc -l)
    echo "依存関係違反: ${DEPENDENCY_VIOLATIONS}ファイル"
    
    # Layer separation integrity
    LAYER_BOUNDARY_VIOLATIONS=$(find src -name "*.py" -exec grep -l "from.*domain.*import.*\(Repository\|Service\)" {} \; | wc -l)
    echo "レイヤー境界違反: ${LAYER_BOUNDARY_VIOLATIONS}ファイル"
    
    # Calculate integration health score
    INTEGRATION_SCORE=$(echo "scale=2; 100 - ($DOMAIN_VIOLATIONS * 10 + $DEPENDENCY_VIOLATIONS * 15 + $LAYER_BOUNDARY_VIOLATIONS * 5)" | bc)
    echo "統合健全性スコア: ${INTEGRATION_SCORE}/100"
}

analyze_system_integration

# API integration health
echo "API統合健全性チェック中..."
if [ -f "openapi.json" ] || [ -f "openapi.yaml" ]; then
    echo "✅ OpenAPI仕様書存在"
    API_ENDPOINTS=$(jq '.paths | keys | length' openapi.json 2>/dev/null || echo "0")
    echo "定義済みエンドポイント数: ${API_ENDPOINTS}"
else
    echo "⚠️ OpenAPI仕様書未定義"
fi

# Database integration health  
echo "データベース統合健全性チェック中..."
DB_MIGRATIONS=$(find . -name "*migration*" -o -name "*alembic*" | wc -l)
echo "マイグレーションファイル数: ${DB_MIGRATIONS}"

# Service integration health
echo "サービス統合健全性チェック中..."
EXTERNAL_SERVICES=$(grep -r "http://\|https://" src/ | grep -v "localhost" | wc -l)
echo "外部サービス呼び出し箇所: ${EXTERNAL_SERVICES}"
```

**User Interaction (Japanese):**
```
プロジェクト総合ステータス分析を開始します。

分析レベルを選択してください：
1. 📊 エグゼクティブサマリー（経営層向け）
2. 🔧 技術責任者レポート（CTO/テックリード向け）
3. 🎯 プロジェクトマネージャレポート（PM向け）
4. 👥 開発チームダッシュボード（チーム向け）
5. 🌍 包括的システム分析（全ステークホルダー向け）

どの分析レベルを実行しますか？（番号を入力）:
```

### 2. 多次元プロジェクト健全性評価
```python
# Multi-dimensional project health assessment
import json
import math
from datetime import datetime, timedelta

class ProjectHealthAnalyzer:
    def __init__(self):
        self.health_dimensions = {
            "technical": {
                "weight": 0.3,
                "metrics": ["code_quality", "test_coverage", "architecture_compliance", "security"]
            },
            "operational": {
                "weight": 0.25, 
                "metrics": ["deployment_frequency", "lead_time", "recovery_time", "failure_rate"]
            },
            "organizational": {
                "weight": 0.25,
                "metrics": ["team_velocity", "knowledge_sharing", "documentation", "onboarding"]
            },
            "strategic": {
                "weight": 0.2,
                "metrics": ["vision_alignment", "market_fit", "scalability", "sustainability"]
            }
        }
    
    def calculate_health_score(self, metrics_data):
        """Calculate comprehensive project health score"""
        total_score = 0
        total_weight = 0
        
        dimension_scores = {}
        
        for dimension, config in self.health_dimensions.items():
            dimension_score = self._calculate_dimension_score(
                dimension, config, metrics_data
            )
            dimension_scores[dimension] = dimension_score
            
            weighted_score = dimension_score * config["weight"]
            total_score += weighted_score
            total_weight += config["weight"]
        
        overall_health = total_score / total_weight if total_weight > 0 else 0
        
        return {
            "overall_health": round(overall_health, 2),
            "dimension_scores": dimension_scores,
            "health_grade": self._get_health_grade(overall_health),
            "critical_areas": self._identify_critical_areas(dimension_scores),
            "recommendations": self._generate_recommendations(dimension_scores)
        }
    
    def _calculate_dimension_score(self, dimension, config, metrics_data):
        """Calculate score for specific dimension"""
        if dimension == "technical":
            return self._calculate_technical_score(metrics_data)
        elif dimension == "operational":
            return self._calculate_operational_score(metrics_data)
        elif dimension == "organizational":
            return self._calculate_organizational_score(metrics_data)
        elif dimension == "strategic":
            return self._calculate_strategic_score(metrics_data)
        return 50  # Default neutral score
    
    def _calculate_technical_score(self, data):
        """Technical health calculation"""
        code_quality = min(100, max(0, 100 - data.get("ruff_issues", 0)))
        test_coverage = data.get("test_coverage", 0)
        architecture_score = data.get("integration_score", 70)
        security_score = max(0, 100 - data.get("security_issues", 0) * 10)
        
        return (code_quality + test_coverage + architecture_score + security_score) / 4
    
    def _calculate_operational_score(self, data):
        """Operational excellence calculation"""
        deploy_freq = min(100, data.get("deployments_per_week", 1) * 20)
        lead_time = max(0, 100 - data.get("avg_lead_time_days", 7) * 5)
        recovery_time = max(0, 100 - data.get("avg_recovery_hours", 4) * 10)
        failure_rate = max(0, 100 - data.get("failure_rate_percent", 5) * 10)
        
        return (deploy_freq + lead_time + recovery_time + failure_rate) / 4
    
    def _calculate_organizational_score(self, data):
        """Organizational health calculation"""
        velocity = min(100, data.get("story_points_per_week", 10) * 5)
        documentation = data.get("documentation_coverage", 70)
        team_satisfaction = data.get("team_satisfaction", 75)
        knowledge_sharing = data.get("knowledge_sharing_score", 70)
        
        return (velocity + documentation + team_satisfaction + knowledge_sharing) / 4
    
    def _calculate_strategic_score(self, data):
        """Strategic alignment calculation"""
        vision_alignment = data.get("vision_alignment_score", 70)
        market_fit = data.get("market_fit_score", 75)
        scalability = data.get("scalability_score", 80)
        sustainability = data.get("sustainability_score", 70)
        
        return (vision_alignment + market_fit + scalability + sustainability) / 4
    
    def _get_health_grade(self, score):
        """Convert score to grade"""
        if score >= 90: return "A+"
        elif score >= 85: return "A"
        elif score >= 80: return "B+"
        elif score >= 75: return "B"
        elif score >= 70: return "C+"
        elif score >= 65: return "C"
        elif score >= 60: return "D"
        else: return "F"
    
    def _identify_critical_areas(self, scores):
        """Identify areas needing immediate attention"""
        critical = []
        for dimension, score in scores.items():
            if score < 60:
                critical.append({
                    "dimension": dimension,
                    "score": score,
                    "severity": "critical" if score < 40 else "high"
                })
        return sorted(critical, key=lambda x: x["score"])
    
    def _generate_recommendations(self, scores):
        """Generate actionable recommendations"""
        recommendations = []
        
        if scores.get("technical", 100) < 70:
            recommendations.append({
                "priority": "high",
                "area": "技術的品質",
                "action": "テストカバレッジ向上とコード品質改善スプリントの実施",
                "timeline": "2-4週間"
            })
        
        if scores.get("operational", 100) < 70:
            recommendations.append({
                "priority": "high", 
                "area": "運用効率",
                "action": "CI/CD改善とデプロイメント自動化の強化",
                "timeline": "3-6週間"
            })
        
        if scores.get("organizational", 100) < 70:
            recommendations.append({
                "priority": "medium",
                "area": "組織的健全性",
                "action": "チーム能力向上とドキュメント整備",
                "timeline": "4-8週間"
            })
        
        if scores.get("strategic", 100) < 70:
            recommendations.append({
                "priority": "medium",
                "area": "戦略的整合性", 
                "action": "ビジョン再確認と長期ロードマップ策定",
                "timeline": "2-3週間"
            })
        
        return recommendations

# Initialize and run analysis
analyzer = ProjectHealthAnalyzer()
```

**Tool Instructions (English):**
- Collect comprehensive metrics from all project dimensions
- Calculate weighted health scores across technical, operational, organizational, and strategic areas
- Generate executive-level insights and recommendations
- Create actionable improvement roadmaps with timelines
- Provide stakeholder-specific reporting formats

### 3. 戦略的ロードマップ生成
```bash
echo "=== 戦略的ロードマップ生成 ==="

generate_strategic_roadmap() {
    echo "戦略的ロードマップ生成中..."
    
    # Create comprehensive roadmap
    cat > strategic_roadmap.md << 'EOF'
# 🚀 戦略的プロジェクトロードマップ

## 🎯 現在位置
- プロジェクト健全性: ${OVERALL_HEALTH_SCORE}/100 (Grade: ${HEALTH_GRADE})
- 技術的成熟度: ${TECHNICAL_SCORE}/100
- 運用効率性: ${OPERATIONAL_SCORE}/100
- 組織的健全性: ${ORGANIZATIONAL_SCORE}/100
- 戦略的整合性: ${STRATEGIC_SCORE}/100

## 📅 短期ロードマップ（1-3ヶ月）

### 🎯 Phase 1: 品質基盤強化 (Week 1-4)
- **目標**: 技術的品質の底上げ
- **成果物**:
  - テストカバレッジ80%達成
  - コード品質指標の改善（Ruff issues < 10）
  - セキュリティ監査完了
- **投資**: 開発リソースの30%
- **ROI期待値**: 保守コスト20%削減

### 🎯 Phase 2: 運用自動化 (Week 5-8)
- **目標**: デプロイメント効率化とモニタリング強化
- **成果物**:
  - CI/CD完全自動化
  - 監視・アラートシステム構築
  - 障害対応時間50%短縮
- **投資**: インフラリソースの40%
- **ROI期待値**: 運用コスト30%削減

### 🎯 Phase 3: 組織的成熟度向上 (Week 9-12)
- **目標**: チーム生産性とコラボレーション強化
- **成果物**:
  - ドキュメント体系化
  - 知識共有プロセス確立
  - オンボーディング時間50%短縮
- **投資**: 教育・プロセス改善20%
- **ROI期待値**: 生産性15%向上

## 📅 中期ロードマップ（3-12ヶ月）

### 🏗️ Quarter 2: アーキテクチャ進化
- **スケーラビリティ向上**: マイクロサービス化検討
- **パフォーマンス最適化**: ボトルネック解消とキャッシュ戦略
- **API標準化**: OpenAPI完全対応と外部連携強化

### 🌍 Quarter 3: 市場適応力強化  
- **国際化対応**: 多言語・多地域サポート
- **プラットフォーム拡張**: モバイル・Web・API統合戦略
- **データ活用基盤**: 分析・レポーティング機能強化

### 🚀 Quarter 4: 次世代技術導入
- **AI/ML統合**: 業務自動化と意思決定支援
- **クラウドネイティブ**: コンテナ化とオーケストレーション
- **セキュリティ強化**: ゼロトラスト・アーキテクチャ

## 📅 長期ビジョン（1-3年）

### 🎯 Year 1: 技術的優位性確立
- **イノベーション文化**: R&D体制とイノベーション促進
- **技術標準化**: 業界標準・ベストプラクティス確立
- **エコシステム構築**: パートナー・コミュニティとの連携

### 🎯 Year 2-3: 市場リーダーシップ
- **プラットフォーム化**: 他社サービスとの統合基盤
- **グローバル展開**: 多地域・多文化対応
- **持続可能性**: 環境・社会責任経営の実践

## 💰 投資計画とROI

### 短期投資 (Q1)
- **技術債務解消**: ¥X,XXX万
- **運用自動化**: ¥X,XXX万  
- **人材育成**: ¥X,XXX万
- **期待ROI**: 年間XX%のコスト削減

### 中期投資 (Q2-Q4)
- **インフラ刷新**: ¥XX,XXX万
- **新技術導入**: ¥XX,XXX万
- **市場開拓**: ¥XX,XXX万
- **期待ROI**: 売上XX%向上

### 長期投資 (Year 2-3)
- **R&D体制**: ¥XXX,XXX万
- **グローバル展開**: ¥XXX,XXX万
- **期待ROI**: 市場シェアXX%獲得

## 🎯 成功指標（KPI）

### 技術指標
- デプロイ頻度: 週X回 → 日X回
- 障害復旧時間: X時間 → X分  
- テストカバレッジ: XX% → XX%
- セキュリティ指標: 脆弱性ゼロ維持

### ビジネス指標
- ユーザー満足度: XX% → XX%
- 売上成長率: XX% → XX%
- 市場シェア: XX% → XX%
- 利益率: XX% → XX%

### 組織指標
- チーム生産性: XXpt/week → XXpt/week
- 離職率: XX% → X%以下
- エンゲージメント: XX% → XX%
- 学習・成長時間: XX時間/月 → XX時間/月

EOF

    echo "✅ 戦略的ロードマップを生成しました"
}

generate_strategic_roadmap
```

### 4. ステークホルダー向けレポート生成
```bash
echo "=== ステークホルダー向けレポート生成 ==="

# Executive summary for C-level
generate_executive_summary() {
    cat > executive_summary.md << 'EOF'
# 📊 エグゼクティブサマリー

## 🎯 現状評価 (1分でわかる)
- **プロジェクト健全性**: ${HEALTH_GRADE} (${OVERALL_HEALTH_SCORE}/100)
- **投資対効果**: ${ROI_STATUS}
- **市場競争力**: ${MARKET_POSITION}
- **リスクレベル**: ${RISK_LEVEL}

## 💡 主要な洞察
1. **強み**: ${TOP_STRENGTH}
2. **課題**: ${TOP_CHALLENGE}  
3. **機会**: ${TOP_OPPORTUNITY}
4. **脅威**: ${TOP_THREAT}

## 🎯 推奨アクション (即時実行)
1. ${CRITICAL_ACTION_1}
2. ${CRITICAL_ACTION_2}
3. ${CRITICAL_ACTION_3}

## 💰 投資推奨
- **優先投資領域**: ${INVESTMENT_PRIORITY}
- **期待ROI**: ${EXPECTED_ROI}
- **投資期間**: ${INVESTMENT_TIMELINE}

EOF
}

# Technical leadership report
generate_technical_report() {
    cat > technical_leadership_report.md << 'EOF'
# 🔧 技術責任者レポート

## 🏗️ アーキテクチャ健全性
- **統合スコア**: ${INTEGRATION_SCORE}/100
- **技術債務**: ${TECHNICAL_DEBT_LEVEL}
- **スケーラビリティ**: ${SCALABILITY_RATING}

## 📊 品質メトリクス
- **テストカバレッジ**: ${TEST_COVERAGE}%
- **コード品質**: ${CODE_QUALITY_SCORE}/100
- **セキュリティ**: ${SECURITY_SCORE}/100
- **パフォーマンス**: ${PERFORMANCE_SCORE}/100

## 🚀 技術的優先事項
1. ${TECH_PRIORITY_1}
2. ${TECH_PRIORITY_2}
3. ${TECH_PRIORITY_3}

## 🔄 推奨技術投資
- **短期** (1-3ヶ月): ${SHORT_TERM_TECH_INVESTMENT}
- **中期** (3-12ヶ月): ${MEDIUM_TERM_TECH_INVESTMENT}
- **長期** (1-3年): ${LONG_TERM_TECH_INVESTMENT}

EOF
}

# Team dashboard
generate_team_dashboard() {
    cat > team_dashboard.md << 'EOF'
# 👥 開発チームダッシュボード

## 📈 チームパフォーマンス
- **ベロシティ**: ${TEAM_VELOCITY} pt/週
- **完了率**: ${COMPLETION_RATE}%
- **品質指標**: ${TEAM_QUALITY_SCORE}/100

## 🎯 現在のフォーカス
- **アクティブスプリント**: Sprint ${CURRENT_SPRINT}
- **主要ゴール**: ${SPRINT_GOALS}
- **進捗**: ${SPRINT_PROGRESS}%

## ⚠️ 注意が必要な項目
1. ${TEAM_ALERT_1}
2. ${TEAM_ALERT_2}
3. ${TEAM_ALERT_3}

## 🚀 次のアクション
- **今週**: ${THIS_WEEK_ACTIONS}
- **来週**: ${NEXT_WEEK_ACTIONS}
- **今月**: ${THIS_MONTH_ACTIONS}

EOF
}

# Generate all reports
generate_executive_summary
generate_technical_report  
generate_team_dashboard

echo "✅ 全ステークホルダー向けレポートを生成しました"
```

### 5. 継続的改善プロセス設計
```bash
echo "=== 継続的改善プロセス設計 ==="

design_improvement_process() {
    echo "継続的改善プロセス設計中..."
    
    # Create improvement tracking system
    mkdir -p docs/improvement-tracking
    
    cat > docs/improvement-tracking/improvement-process.md << 'EOF'
# 🔄 継続的改善プロセス

## 📊 定期レビューサイクル

### Daily (毎日)
- **品質メトリクス監視**: 自動化されたダッシュボード確認
- **ビルド・テスト結果**: CI/CDパイプライン健全性
- **セキュリティアラート**: 脆弱性・侵入検知

### Weekly (毎週金曜日)
- **チームレトロスペクティブ**: 30分の振り返り会議
- **品質トレンド分析**: 週次品質レポート生成
- **技術債務評価**: 優先対応項目の特定

### Monthly (毎月末)
- **プロジェクト健全性分析**: 本コマンド(17-project-status)実行
- **ステークホルダーレポート**: エグゼクティブサマリー共有
- **戦略的ロードマップ見直し**: 計画の調整・更新

### Quarterly (四半期)
- **包括的監査**: 外部監査・第三者評価
- **技術戦略見直し**: アーキテクチャ・技術選択の再評価
- **組織体制最適化**: チーム構成・役割分担の調整

## 🎯 改善優先度マトリクス

### 緊急かつ重要
- システム停止・セキュリティ侵害
- 法的コンプライアンス違反
- 顧客満足度重大低下

### 重要だが緊急でない
- 技術債務解消
- プロセス改善
- チームスキル向上

### 緊急だが重要でない
- バグ修正
- パフォーマンス微調整
- ドキュメント更新

### 緊急でも重要でもない
- 新機能追加
- UI改善
- 最適化

## 🔄 改善実施プロセス

1. **課題特定**: メトリクス分析・レビューによる課題抽出
2. **原因分析**: 5 Why分析・魚骨図による根本原因特定
3. **解決策検討**: ブレインストーミング・技術調査
4. **優先度評価**: インパクト・工数・リスク評価
5. **実装計画**: タイムライン・リソース・責任者決定
6. **実行・監視**: 進捗追跡・効果測定
7. **効果検証**: Before/After比較・ROI計算
8. **標準化**: 成功パターンの他領域展開

## 📈 成功指標

### Leading Indicators (先行指標)
- 改善提案数: 月XX件以上
- 実装率: XX%以上
- 改善サイクル時間: XX日以内

### Lagging Indicators (遅行指標)  
- プロジェクト健全性スコア向上
- 顧客満足度向上
- チーム生産性向上
- コスト削減達成

EOF

    echo "✅ 継続的改善プロセスを設計しました"
}

design_improvement_process
```

## ✅ 内蔵品質保証

### Must-Have Analysis (必須)
- [ ] System integration health is comprehensively assessed
- [ ] Multi-dimensional health scores are calculated accurately
- [ ] Strategic roadmap addresses all critical areas
- [ ] Stakeholder reports are appropriate for their audiences
- [ ] Continuous improvement process is actionable and sustainable

### Should-Have Analysis (推奨)
- [ ] Quantitative metrics support all qualitative assessments
- [ ] ROI calculations are realistic and evidence-based  
- [ ] Risk assessments are comprehensive and prioritized
- [ ] Recommendations include specific timelines and resource requirements
- [ ] Success metrics are measurable and trackable

### Could-Have Enhancements (任意)
- [ ] Predictive analytics for trend forecasting
- [ ] Automated report generation and distribution
- [ ] Integration with external project management tools
- [ ] Benchmark comparisons with industry standards
- [ ] Interactive dashboards for real-time monitoring

### Project Health Assessment Quality
```bash
# Comprehensive quality assessment
echo "=== プロジェクト健全性評価品質検証 ==="

ASSESSMENT_QUALITY=0
MAX_QUALITY=100

# Data comprehensiveness (25 points)
if [ -n "$INTEGRATION_SCORE" ] && [ -n "$OVERALL_HEALTH_SCORE" ]; then
    ASSESSMENT_QUALITY=$((ASSESSMENT_QUALITY + 25))
    echo "✅ データ包括性: 25/25点"
fi

# Analysis depth (25 points)
if [ -f "strategic_roadmap.md" ] && [ -f "executive_summary.md" ]; then
    ASSESSMENT_QUALITY=$((ASSESSMENT_QUALITY + 25))
    echo "✅ 分析深度: 25/25点"
fi

# Stakeholder relevance (25 points)
if [ -f "technical_leadership_report.md" ] && [ -f "team_dashboard.md" ]; then
    ASSESSMENT_QUALITY=$((ASSESSMENT_QUALITY + 25))
    echo "✅ ステークホルダー関連性: 25/25点"
fi

# Actionability (25 points)
ASSESSMENT_QUALITY=$((ASSESSMENT_QUALITY + 25))
echo "✅ 実行可能性: 25/25点"

echo "🎯 プロジェクト健全性評価品質: ${ASSESSMENT_QUALITY}/${MAX_QUALITY}"

if [ $ASSESSMENT_QUALITY -ge 85 ]; then
    echo "🌟 優秀な健全性評価です。戦略的意思決定に活用できます。"
elif [ $ASSESSMENT_QUALITY -ge 70 ]; then
    echo "✅ 良好な健全性評価です。改善計画策定に活用できます。"
else
    echo "⚠️ 評価精度の向上が必要です。データ収集・分析手法を見直してください。"
fi
```

## 📊 標準化出力フォーマット

### 包括的プロジェクト健全性レポート
```
🌟 プロジェクト総合健全性レポート
=================================

📅 分析実施日: $(date '+%Y年%m月%d日 %H:%M')
👤 分析実施者: Project Health Analyst (Claude Code Expert)

## 📊 ヘルスサマリー

### 🎯 総合健全性スコア: ${OVERALL_HEALTH_SCORE}/100 (Grade: ${HEALTH_GRADE})

#### 次元別スコア:
- 🔧 技術的健全性: ${TECHNICAL_SCORE}/100
- ⚙️ 運用効率性: ${OPERATIONAL_SCORE}/100  
- 👥 組織的健全性: ${ORGANIZATIONAL_SCORE}/100
- 🎯 戦略的整合性: ${STRATEGIC_SCORE}/100

## 🚀 主要な強み
1. ${TOP_STRENGTH_1}
2. ${TOP_STRENGTH_2}
3. ${TOP_STRENGTH_3}

## ⚠️ 重要な課題
1. ${TOP_ISSUE_1} (優先度: ${PRIORITY_1})
2. ${TOP_ISSUE_2} (優先度: ${PRIORITY_2})
3. ${TOP_ISSUE_3} (優先度: ${PRIORITY_3})

## 🎯 即座に取り組むべき項目
### Critical (24時間以内)
- ${CRITICAL_ITEM_1}
- ${CRITICAL_ITEM_2}

### High (1週間以内)  
- ${HIGH_ITEM_1}
- ${HIGH_ITEM_2}

### Medium (1ヶ月以内)
- ${MEDIUM_ITEM_1}
- ${MEDIUM_ITEM_2}

## 💰 投資推奨事項

### 短期投資 (Q1: ¥${SHORT_TERM_INVESTMENT}万)
- ROI期待値: ${SHORT_TERM_ROI}%
- 重点領域: ${SHORT_TERM_FOCUS}
- 期待効果: ${SHORT_TERM_BENEFITS}

### 中期投資 (Q2-Q4: ¥${MEDIUM_TERM_INVESTMENT}万)
- ROI期待値: ${MEDIUM_TERM_ROI}%
- 重点領域: ${MEDIUM_TERM_FOCUS}
- 期待効果: ${MEDIUM_TERM_BENEFITS}

## 📈 プロジェクト成熟度

### 現在の成熟度レベル: ${MATURITY_LEVEL} (${MATURITY_DESCRIPTION})

#### 成熟度向上ロードマップ:
- Level ${NEXT_LEVEL}達成予定: ${NEXT_LEVEL_TIMELINE}
- 必要な投資: ¥${NEXT_LEVEL_INVESTMENT}万
- 主要マイルストーン: ${NEXT_LEVEL_MILESTONES}

## 🔄 継続的監視項目

### 日次監視
- ${DAILY_MONITOR_1}
- ${DAILY_MONITOR_2}

### 週次監視  
- ${WEEKLY_MONITOR_1}
- ${WEEKLY_MONITOR_2}

### 月次監視
- ${MONTHLY_MONITOR_1}
- ${MONTHLY_MONITOR_2}

## 📋 次回分析予定

- **定期分析**: $(date -d '+1 month' '+%Y年%m月%d日')
- **緊急分析トリガー**: 健全性スコア10pt以上低下時
- **戦略見直し**: $(date -d '+3 months' '+%Y年%m月%d日')

## 📞 エスカレーション

### Level 1: チームリーダー
- 条件: 技術スコア < 60
- 対応時間: 4時間以内

### Level 2: 技術責任者  
- 条件: 総合スコア < 50
- 対応時間: 2時間以内

### Level 3: エグゼクティブ
- 条件: 戦略スコア < 40 または Critical問題発生
- 対応時間: 1時間以内

---
📚 詳細資料:
- エグゼクティブサマリー: docs/reports/executive-summary-$(date +%Y%m%d).md
- 技術レポート: docs/reports/technical-report-$(date +%Y%m%d).md  
- 戦略ロードマップ: docs/reports/strategic-roadmap-$(date +%Y%m%d).md
- 改善トラッキング: docs/improvement-tracking/

🤖 本レポートはClaude Code Expert Modeにより生成されました
```

**最終確認事項:**
- すべての健全性次元が適切に評価されている
- ステークホルダー毎に適切な情報が提供されている  
- 戦略的ロードマップが実行可能で具体的である
- 継続的改善プロセスが持続可能である
- 次回分析までのアクションプランが明確である