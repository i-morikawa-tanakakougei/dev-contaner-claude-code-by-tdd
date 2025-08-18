包括的な安全性とトレーサビリティ機能により、スプリントフィードバックに基づいてシナリオを進化させます。

## メタデータ
- **前提条件**: 開発サイクルが進行中または完了
- **入力**: フィーチャー名（必須）、シナリオ進化詳細
- **出力**: 
  - `docs/use_cases/evolved/`内の更新されたシナリオファイル
  - メタデータファイル内の進化追跡
  - スプリント計画との統合
- **依存関係**: 既存のユースケース仕様、Git設定
- **実行タイミング**: 新しいシナリオが発見される開発中のいつでも

## 🎯 **TDD/DDD/LAYEREDプロセスコンテキスト**

**🔄 コアワークフロー**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 アーキテクチャ**: クリーンアーキテクチャ（ドメイン→アプリケーション→インフラストラクチャ→プレゼンテーション）  
**🧪 開発**: テスト駆動開発（RED→GREEN→REFACTOR）  
**🏗️ 設計**: ドメイン駆動設計（エンティティ、値オブジェクト、集約、リポジトリ）  
**📋 要件**: 完全なトレーサビリティを持つGiven-When-Thenシナリオ  
**🔄 進化**: /evolve-scenariosコマンドによる継続的なシナリオ進化

> 📖 **ドキュメント管理システム**: [README.md](./README.md)  
> 🗺️ **現在位置**: シナリオ進化フェーズ - シナリオ進化（12/16）  
> 🎯 **フェーズ目的**: スプリントフィードバックに基づく新しいシナリオの追加  
> ⬅️ **前段階**: 11-refactor（リファクタリング）  
> ➡️ **次段階**: 新しい03-11サイクルまたは13-review-issue（レビュー）
>
> **📋 3層アーキテクチャ操作**:
>
> - 🎯 **戦略**: `docs/use_cases/core/index.md`（コアシナリオの更新）
> - 📊 **戦術**: `docs/use_cases/index.md`（シナリオ進化の追跡）
> - 🔧 **実行**: `docs/use_cases/evolved/`（進化したシナリオドキュメントの作成）

## 🔄 **シナリオ進化: ドキュメント作成のみ**

**⚠️ 重要な注意:**
- **このステップはシナリオ進化のみです** - フィードバックに基づく新しいシナリオを作成します
- **機能実装なし** - 新しい要求の文書化に焦点を当てます  
- **要求発見** - 開発中に発見されたエッジケースと新しい要求をキャプチャします
- **進化したシナリオドキュメントのみ作成** - コード実装は行いません

**進化トリガーポイント:**
- 開発中に新しい要求が発見された時
- スプリントレビューフィードバック後
- エッジケースが特定された時
- 統合問題で不足しているシナリオが明らかになった時

**進化プロセス:**
1. `11-refactor` ← 開発サイクル完了
2. `12-evolve-scenarios` ← **【あなたはここにいます】新しいシナリオの発見と文書化**
3. `02-sprint-planning`に戻る ← 新しいシナリオをバックログに統合
4. 進化したシナリオのための新しい`03-11`開発サイクル

## 📋 **シナリオ進化タスクチェックリスト**

**システマティックなシナリオ発見と統合のためにこのチェックリストを使用してください:**

### 🔴 必須タスク

#### **🔍 フィードバック・発見分析**
- [ ] **スプリント振り返りをレビュー**: 完了したスプリントからのフィードバックを分析する
- [ ] **開発での発見を解析**: 実装中（ステップ06-09）に発見された新しい要求を抽出する
- [ ] **イシューコメントをレビュー**: 言及されたエッジケースについてGitHubイシューコメントをスキャンする
- [ ] **ユーザーフィードバックを分析**: ステークホルダーとエンドユーザーからのフィードバックを処理する

#### **📝 新しいシナリオの特定**
- [ ] **エッジケースを特定**: カバーされていない境界条件とエッジケースを文書化する
- [ ] **エラーシナリオを定義**: エラーハンドリングと失敗モードのシナリオを作成する
- [ ] **パフォーマンスシナリオを抽出**: パフォーマンス関連要求を特定する
- [ ] **セキュリティシナリオを定義**: セキュリティと認証要求を文書化する

#### **📋 Given-When-Thenシナリオ作成**
- [ ] **新しいGiven-When-Thenシナリオを記述**: 各新しい要求に対して構造化されたシナリオを作成する
- [ ] **前提条件を定義**: 新しいシナリオのシステム状態要求を指定する
- [ ] **期待される結果を文書化**: 各シナリオの明確な成功基準を定義する
- [ ] **受け入れ基準を指定**: 各シナリオに対してテスト可能な受け入れ基準を作成する

### 🟡 推奨タスク

#### **🏗️ ドメイン影響評価**
- [ ] **ドメインモデルの変更を評価**: エンティティ、値オブジェクト、サービスに必要な変更を特定する
- [ ] **新しいドメイン概念を特定**: 発見された新しいビジネス用語と概念を文書化する
- [ ] **ユビキタス言語を更新**: プロジェクト語彙に新しい用語を追加する
- [ ] **集約境界を評価**: 新しいシナリオが集約設計に影響するかを判断する
- [ ] **リポジトリの変更を特定**: データアクセスパターンに必要な変更を文書化する
- [ ] **サービスへの影響を評価**: 既存のドメインとアプリケーションサービスへの影響を評価する

#### **📊 優先度・影響分析**
- [ ] **ビジネス優先度を割り当て**: シナリオを高/中/低ビジネス価値として分類する
- [ ] **技術複雑度を評価**: 実装の難易度とリスクを評価する
- [ ] **工数を見積もる**: 各シナリオの実装に対する大まかな見積もりを提供する
- [ ] **依存関係を特定**: シナリオと既存機能の間の依存関係を文書化する
- [ ] **タイムライン影響を評価**: 現在のスプリントとリリース計画への影響を評価する
- [ ] **リスク評価**: シナリオの実装または延期に関連するリスクを特定する

#### **📁 シナリオドキュメント作成**
- [ ] **進化したシナリオファイルを作成**: `docs/use_cases/evolved/`にファイルを生成する
- [ ] **シナリオメタデータを更新**: 関連するissue-X-Y.jsonファイルにシナリオ進化情報を追加する
- [ ] **シナリオを相互参照**: 進化したシナリオを元の要求にリンクする
- [ ] **トレーサビリティを文書化**: 発見源と新しいシナリオの間の明確なリンクを維持する

### 🟢 オプションタスク

#### **🔗 統合準備**
- [ ] **スプリントバックログを更新**: シナリオをプロダクトバックログに統合する準備をする
- [ ] **GitHubイシューテンプレートを作成**: 新しいシナリオのイシュー説明を下書きする
- [ ] **実装順序を計画**: 進化したシナリオを実装する最適な順序を提案する
- [ ] **クイックウィンを特定**: 迅速に実装できるシナリオにフラグを立てる
- [ ] **ブロッカーを文書化**: 外部依存関係によってブロックされているシナリオをメモする
- [ ] **ステークホルダーコミュニケーションを準備**: ステークホルダーレビュー用のサマリーを作成する

#### **📈 品質・検証**
- [ ] **シナリオ完全性を検証**: 発見されたすべての要求がキャプチャされていることを確認する
- [ ] **シナリオ品質をレビュー**: シナリオがテスト可能で明確であることをチェックする
- [ ] **受け入れ基準を検証**: 基準が具体的で測定可能であることを確認する
- [ ] **シナリオ一貫性をチェック**: 新しいシナリオが既存のビジョンと一致することを確認する
- [ ] **テスト失敗をレビュー**: 予期しないテスト失敗によって明らかになったシナリオを特定する
- [ ] **統合課題を文書化**: システム統合中に発見されたシナリオをメモする
- [ ] **統合シナリオを特定**: 外部システム相互作用のシナリオを作成する
- [ ] **ユーザビリティシナリオを文書化**: ユーザーエクスペリエンスとインターフェース要求をキャプチャする
- [ ] **代替フローを追加**: 代替パスと決定ポイントを文書化する
- [ ] **エラー条件を含める**: エラーシナリオの期待される動作を定義する
- [ ] **実装ノートを作成**: 将来の実装のためのガイダンスを提供する
- [ ] **サマリーレポートを生成**: スプリント計画のための進化したシナリオの概要を作成する
- [ ] **ビジネス整合性を検証**: シナリオがビジネス価値を提供することを確認する
- [ ] **技術実現可能性をレビュー**: シナリオが技術的に達成可能であることを評価する

### **🔄 スプリント計画統合**
- [ ] **ユースケースインデックスを更新**: 進化したシナリオを戦術追跡ドキュメントに追加する
- [ ] **スプリント計画の準備**: 次回の/sprint-planning実行のためにシナリオをパッケージ化する
- [ ] **プロジェクトロードマップを更新**: プロジェクトタイムラインにシナリオ進化を反映する
- [ ] **進化を通達**: ステークホルダーにシナリオ発見と影響を通知する
- [ ] **学習事項を文書化**: 将来のシナリオ発見を改善するための洞察を記録する
- [ ] **開発チームの準備**: 新しいシナリオと実装アプローチについてチームに説明する

### **📊 進化ドキュメント**
- [ ] **メタデータを更新**: 追跡システムにシナリオ進化活動を記録する
- [ ] **進化レポートを作成**: どのシナリオが追加されたか、なぜ追加されたかを文書化する
- [ ] **シナリオファイルをコミット**: 進化したシナリオドキュメントをすべてバージョン管理する
- [ ] **プロジェクトメトリクスを更新**: プロジェクト健全性メトリクスにシナリオ進化を反映する
- [ ] **発見ノートをアーカイブ**: 将来の参照のために生の発見ノートを保存する
- [ ] **引き継ぎの準備**: 進化したシナリオが次の開発サイクルの準備ができていることを確認する

**💡 プロのヒント: シナリオ進化は要求ギャップを防ぐために重要です - 後で間違って実装するより、今発見して文書化する方が良いです！**
2. `12-evolve-scenarios` ← **【あなたはここにいます】新しいシナリオを文書化**
3. `02-sprint-planning` ← 次のスプリントで新しいシナリオを計画
4. 進化したシナリオのための新しいTDD/DDDサイクルを開始

**新しいシナリオドキュメントのみ作成する。**

## 🛡️ **統合版の主な改善点**

### **✅ 解決された問題**

- **フィードバック分析の不備**: 自動的なフィードバック源の検出と統合
- **シナリオ一貫性**: 既存シナリオとの整合性自動チェック
- **ドキュメント同期**: シナリオ・イシュー・スプリント計画の自動連携
- **影響分析の漏れ**: 進化による影響範囲の包括的分析
- **追跡可能性**: 変更理由から実装までの完全トレーサビリティ

### **🆕 新機能**

1. **🔄 インテリジェント分析**: 多様なフィードバック源の自動統合分析
2. **📊 影響評価エンジン**: シナリオ変更の影響範囲自動計算
3. **🛡️ 整合性保証**: 既存アーキテクチャとの一貫性自動検証
4. **🔍 スマート推奨**: 実装タイミングと優先度の自動提案
5. **📈 進化追跡**: シナリオ進化の詳細履歴とパターン分析

## よくあるエラーと解決策

### ❌ エラーケース1: フィーチャー名が提供されていない
**原因**: 対象フィーチャーを指定せずにシナリオ進化を試行  
**解決策**: フィーチャー名を提供: `/evolve-scenarios <feature-name>`

### ❌ エラーケース2: シナリオが既存の要求と競合
**原因**: 新しいシナリオが確立された仕様と矛盾している  
**解決策**: シナリオを統合する前に競合をレビューして解決する

### ❌ エラーケース3: シナリオドキュメントの不備
**原因**: 適切なGiven-When-Then形式なしでシナリオが追加された  
**解決策**: すべてのシナリオが明確な条件を持つ構造化形式に従うことを確認する

## 実行例

### ✅ 成功例
```bash
$ /evolve-scenarios user-management
🌱 フィーチャー 'user-management' のシナリオ進化を開始します
📖 既存シナリオの分析中...
✅ 3個の既存シナリオを発見
🌱 新しいシナリオを追加中...
  ✅ シナリオ作成: ユーザーパスワードリセット
📋 スプリント統合確認中...
✅ 新しいGitHubイシューを作成
🎉 シナリオ進化完了!
```

### ❌ 失敗例と修正
```bash
$ /evolve-scenarios
エラー: フィーチャー名が必要です
使用例: /evolve-scenarios user-management

# 修正: フィーチャー名を提供
$ /evolve-scenarios user-management
```

## タスク詳細

## 1. **安全な環境のセットアップと引数解析**

```bash
# 🔧 自動引数解析と検証を含むすべての安全操作関数をロード
source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "12-evolve-scenarios" "$ARGUMENTS"

# 引数はセットアップスクリプトによって既に解析・検証済み
# このコマンド特有の追加検証
if [[ ${#other_args[@]} -eq 0 ]]; then
    echo "エラー: フィーチャー名が必要です"
    show_usage_example "evolve-scenarios" "feature-name" "新機能'feature-name'のシナリオ進化"
    show_usage_example "evolve-scenarios" "1,feature-name" "イシュー1関連での'feature-name'シナリオ進化"
    show_usage_example "evolve-scenarios" "1,7,mt5-extended-data" "複数イシュー(1,7)統合での'mt5-extended-data'シナリオ進化"
    exit 1
fi

feature_name="${other_args[0]}"
```

## 2. **トランザクション管理とメタデータ発見**

```bash
# シナリオ進化のトランザクションを開始
transaction_id="evolve_scenarios_$(date +%s)_${feature_name}"
begin_transaction "$transaction_id"

# ロールバックハンドラーをセットアップ
add_rollback_handler "echo '🔄 シナリオ進化をロールバック中...'"
add_rollback_handler "git stash push -m 'Auto-stash evolve scenarios rollback' 2>/dev/null || true"
add_rollback_handler "echo '📋 進化前の状態に復旧しました'"

# メタデータファイルを発見
if [[ ${#issue_numbers[@]} -gt 0 ]]; then
    issue_list=$(IFS=-; echo "${issue_numbers[*]}")
    metadata_file="docs/use_cases/issue-${issue_list}-${feature_name}.json"
    echo "🎯 関連イシュー: #$(IFS=' #'; echo "${issue_numbers[*]}")"
else
    # フィーチャー名に一致するメタデータファイルを検索
    metadata_file=$(find docs/use_cases -name "*-${feature_name}.json" | head -1)
    if [[ -z "$metadata_file" ]]; then
        echo "🆕 新しいフィーチャーとしてシナリオ進化を開始"
        # 新しいフィーチャー用の最小限のメタデータを作成
        metadata_file="docs/use_cases/evolved-${feature_name}.json"
        cat > "$metadata_file" << EOF
{
  "feature": "$feature_name",
  "type": "evolved",
  "created_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "updated_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "phase": "scenario_evolution",
  "phases": {
    "scenario_evolution": {
      "evolution_count": 0,
      "evolved": false
    }
  }
}
EOF
    fi
fi

echo "📊 メタデータファイル: $metadata_file"
echo "🎯 フィーチャー: $feature_name"
```

## 3. **包括的フィードバック分析**

```bash
# 複数のフィードバック源をインテリジェントに分析
echo "🔍 フィードバック源を包括的に分析中..."

feedback_analysis_dir="$(mktemp -d)"
add_rollback_handler "rm -rf '$feedback_analysis_dir'"

analyze_feedback_sources() {
    local analysis_report="$feedback_analysis_dir/feedback_analysis.json"
    local sources_found=0

    # 分析レポートを初期化
    cat > "$analysis_report" << EOF
{
  "analysis_date": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "feature": "$feature_name",
  "sources": {},
  "recommendations": [],
  "priority_score": 0
}
EOF

    # 1. スプリントレビューノート
    echo "  📋 スプリントレビューノートを確認中..."
    if [[ -d "docs/sprints" ]]; then
        local sprint_feedback=""
        for sprint_file in docs/sprints/sprint-*-review.md docs/sprints/sprint-*-retrospective.md; do
            if [[ -f "$sprint_file" ]] && grep -i "$feature_name" "$sprint_file" >/dev/null 2>&1; then
                sprint_feedback+="$(basename "$sprint_file"): $(grep -A 3 -B 1 -i "$feature_name" "$sprint_file" | head -10)\n"
                sources_found=$((sources_found + 1))
            fi
        done

        if [[ -n "$sprint_feedback" ]]; then
            jq --arg feedback "$sprint_feedback" '.sources.sprint_reviews = $feedback' "$analysis_report" > "${analysis_report}.tmp" && mv "${analysis_report}.tmp" "$analysis_report"
            echo "    ✅ スプリントフィードバック発見"
        fi
    fi

    # 2. レビューレポート
    echo "  📝 レビューレポートを確認中..."
    if [[ -d "docs/review" ]]; then
        local review_feedback=""
        for review_file in docs/review/issue-*-review.md; do
            if [[ -f "$review_file" ]] && grep -i "$feature_name" "$review_file" >/dev/null 2>&1; then
                review_feedback+="$(basename "$review_file"): $(grep -A 3 -B 1 -i "$feature_name" "$review_file" | head -10)\n"
                sources_found=$((sources_found + 1))
            fi
        done

        if [[ -n "$review_feedback" ]]; then
            jq --arg feedback "$review_feedback" '.sources.review_reports = $feedback' "$analysis_report" > "${analysis_report}.tmp" && mv "${analysis_report}.tmp" "$analysis_report"
            echo "    ✅ レビューフィードバック発見"
        fi
    fi

    # 3. GitHubイシューコメント
    echo "  💬 GitHub イシューコメントを確認中..."
    if [[ ${#issue_numbers[@]} -gt 0 ]]; then
        local github_feedback=""
        for issue_num in "${issue_numbers[@]}"; do
            if safe_gh_command "issue" "view" "$issue_num" --json comments; then
                local comments=$(safe_gh_command "issue" "view" "$issue_num" --json comments | jq -r '.comments[]?.body // empty' | grep -i "$feature_name" | head -5 || true)
                if [[ -n "$comments" ]]; then
                    github_feedback+="Issue #$issue_num: $comments\n"
                    sources_found=$((sources_found + 1))
                fi
            fi
        done

        if [[ -n "$github_feedback" ]]; then
            jq --arg feedback "$github_feedback" '.sources.github_issues = $feedback' "$analysis_report" > "${analysis_report}.tmp" && mv "${analysis_report}.tmp" "$analysis_report"
            echo "    ✅ GitHub フィードバック発見"
        fi
    fi

    # 4. テスト結果分析
    echo "  🧪 テスト結果を分析中..."
    if [[ -d "docs/test_results" ]]; then
        local test_feedback=""
        for test_dir in docs/test_results/*${feature_name}*; do
            if [[ -d "$test_dir" && -f "$test_dir/comprehensive_test_report.md" ]]; then
                # テストレポートから推奨事項と問題を抽出
                test_feedback+="$(basename "$test_dir"): $(grep -A 3 "推奨事項\|改善点\|エラー" "$test_dir/comprehensive_test_report.md" | head -10)\n"
                sources_found=$((sources_found + 1))
            fi
        done

        if [[ -n "$test_feedback" ]]; then
            jq --arg feedback "$test_feedback" '.sources.test_results = $feedback' "$analysis_report" > "${analysis_report}.tmp" && mv "${analysis_report}.tmp" "$analysis_report"
            echo "    ✅ テスト結果フィードバック発見"
        fi
    fi

    # ソースに基づく優先度スコアを計算
    local priority_score=$((sources_found * 20))
    if [[ $priority_score -gt 100 ]]; then priority_score=100; fi

    jq --argjson score "$priority_score" '.priority_score = $score' "$analysis_report" > "${analysis_report}.tmp" && mv "${analysis_report}.tmp" "$analysis_report"

    echo "📊 フィードバック分析完了: $sources_found 源から情報収集"
    echo "🎯 優先度スコア: $priority_score/100"

    echo "$analysis_report"
}

analysis_report=$(analyze_feedback_sources)
```

## 4. **インテリジェントシナリオ進化戦略**

```bash
# 分析に基づく進化戦略を決定
echo "🧠 シナリオ進化戦略を決定中..."

evolution_strategy_file="$feedback_analysis_dir/evolution_strategy.json"

determine_evolution_strategy() {
    local priority_score=$(jq -r '.priority_score' "$analysis_report")
    local sources=$(jq -r '.sources | keys[]' "$analysis_report")

    # シナリオタイプとアプローチを決定
    local scenario_type="extension"  # デフォルト
    local implementation_timing="next_sprint"  # デフォルト
    local urgency="medium"  # デフォルト

    # コンテンツを分析してタイプを決定
    if jq -r '.sources[]' "$analysis_report" | grep -i "error\|bug\|fail" >/dev/null; then
        scenario_type="error_case"
        urgency="high"
        implementation_timing="current_sprint"
    elif jq -r '.sources[]' "$analysis_report" | grep -i "edge\|special\|corner" >/dev/null; then
        scenario_type="edge_case"
        urgency="medium"
    elif jq -r '.sources[]' "$analysis_report" | grep -i "new\|additional\|feature" >/dev/null; then
        scenario_type="new_feature"
        urgency="low"
    fi

    # 優先度スコアに基づく調整
    if [[ $priority_score -ge 80 ]]; then
        urgency="high"
        implementation_timing="current_sprint"
    elif [[ $priority_score -ge 50 ]]; then
        urgency="medium"
        implementation_timing="next_sprint"
    else
        urgency="low"
        implementation_timing="future_sprint"
    fi

    cat > "$evolution_strategy_file" << EOF
{
  "feature": "$feature_name",
  "scenario_type": "$scenario_type",
  "urgency": "$urgency",
  "implementation_timing": "$implementation_timing",
  "priority_score": $priority_score,
  "sources_count": $(echo "$sources" | wc -l),
  "recommendations": [
    "シナリオタイプ: $scenario_type",
    "実装タイミング: $implementation_timing",
    "緊急度: $urgency"
  ]
}
EOF

    echo "✅ 進化戦略決定完了"
    echo "  📋 シナリオタイプ: $scenario_type"
    echo "  ⏰ 実装タイミング: $implementation_timing"
    echo "  🚨 緊急度: $urgency"
}

determine_evolution_strategy
```

## 5. **安全なシナリオドキュメント作成**

```bash
# シナリオドキュメントを安全に作成または更新
echo "📄 シナリオドキュメントを安全に作成中..."

create_evolved_scenario_document() {
    local doc_type=$(jq -r '.scenario_type' "$evolution_strategy_file")
    local urgency=$(jq -r '.urgency' "$evolution_strategy_file")
    local timing=$(jq -r '.implementation_timing' "$evolution_strategy_file")

    # ドキュメントパスを決定
    local scenario_doc=""
    if [[ -f "docs/use_cases/${feature_name}.md" ]]; then
        # 既存のドキュメントを更新
        scenario_doc="docs/use_cases/${feature_name}.md"
        echo "  📝 既存ドキュメントを更新: $scenario_doc"
    else
        # 新しい進化ドキュメントを作成
        mkdir -p "docs/use_cases/evolved"
        local timestamp=$(date +%Y%m%d)
        scenario_doc="docs/use_cases/evolved/${feature_name}-${doc_type}-${timestamp}.md"
        echo "  🆕 新規ドキュメントを作成: $scenario_doc"
    fi

    # 既存を更新する場合はバックアップを作成
    if [[ -f "$scenario_doc" ]]; then
        cp "$scenario_doc" "${scenario_doc}.backup"
        add_rollback_handler "mv '${scenario_doc}.backup' '$scenario_doc'"
    fi

    # 現在のスプリント番号を取得
    local current_sprint=$(find docs/sprints -name "sprint-*-backlog.md" | sed 's/.*sprint-\([0-9]*\).*/\1/' | sort -n | tail -1)
    if [[ -z "$current_sprint" ]]; then current_sprint="1"; fi

    # 包括的なシナリオドキュメントを生成
    cat > "$scenario_doc" << EOF
# 進化したユースケース: ${feature_name}

## 変更理由
- **発見時期**: Sprint ${current_sprint}
- **フィードバック源**: $(jq -r '.sources | keys | join(", ")' "$analysis_report")
- **重要度**: ${urgency}
- **実装タイミング**: ${timing}

## フィードバック分析詳細

### 分析サマリー
- **優先度スコア**: $(jq -r '.priority_score' "$analysis_report")/100
- **フィードバック源数**: $(jq -r '.sources | length' "$analysis_report")
- **シナリオタイプ**: ${doc_type}

### 主要フィードバック
$(jq -r '.sources | to_entries[] | "#### " + .key + "\n" + .value + "\n"' "$analysis_report")

## 新規/更新シナリオ

### シナリオ1: ${feature_name}の基本進化
- **Given**: 基本機能が実装済みである
- **When**: $(echo "$doc_type" | sed 's/_/ /g')の要求が発生した時
- **Then**: システムは適切に対応する
- **追加理由**: フィードバック分析により$(echo "$doc_type" | sed 's/_/ /g')への対応が必要と判明

### シナリオ2: エラー処理の強化
- **Given**: システムが予期しない状況に遭遇した
- **When**: エラーハンドリングが必要な場合
- **Then**: 適切なエラーメッセージとリカバリ手順を提供する
- **発見経緯**: テスト結果とユーザーフィードバックから

## ドメインへの影響
- **新規概念**: ${doc_type}関連の概念
- **既存概念の変更**: 既存の${feature_name}概念の拡張
- **ユビキタス言語の追加**:
  - ${feature_name}進化: フィードバックに基づく機能改善
  - ${doc_type}: 特定の状況への対応

## 実装への影響
- **影響を受けるレイヤー**: Domain/Application/Infrastructure/Presentation
- **必要な変更**:
  - ドメイン層: 新しいビジネスルールの追加
  - アプリケーション層: 新しいユースケースの実装
  - インフラ層: 必要に応じてデータ永続化の拡張
  - プレゼンテーション層: 新しいAPIエンドポイントの追加
- **推定工数**: $(case "$urgency" in
    "high") echo "2-3日" ;;
    "medium") echo "1-2週間" ;;
    *) echo "2-4週間" ;;
  esac)

## 関連するコアシナリオ
- 既存の${feature_name}機能
- 関係性: 既存機能の拡張・改善

## 進化履歴
- **進化日**: $(date)
- **進化理由**: フィードバック駆動開発
- **関連Issue**: $(if [[ ${#issue_numbers[@]} -gt 0 ]]; then echo "#$(IFS=' #'; echo "${issue_numbers[*]}")"; else echo "新規作成予定"; fi)

EOF

    echo "✅ シナリオドキュメント作成完了: $scenario_doc"
    echo "$scenario_doc"
}

scenario_document=$(create_evolved_scenario_document)
```

## 6. **安全性を伴うGitHubイシュー管理**

```bash
# GitHubイシューを安全に作成またはリンク
echo "🔗 GitHub イシューを安全に管理中..."

manage_github_issues() {
    local new_issues=()

    if [[ ${#issue_numbers[@]} -eq 0 ]]; then
        echo "🆕 新しいイシューを作成中..."

        # イシュー作成のためのシナリオ詳細を抽出
        local scenario_type=$(jq -r '.scenario_type' "$evolution_strategy_file")
        local urgency=$(jq -r '.urgency' "$evolution_strategy_file")
        local timing=$(jq -r '.implementation_timing' "$evolution_strategy_file")

        # 包括的なイシュー本文を作成
        local issue_body="## 概要
${feature_name}のシナリオ進化により発見された新しい要求の実装

## シナリオタイプ
${scenario_type}

## 優先度・緊急度
- 緊急度: ${urgency}
- 実装タイミング: ${timing}
- 優先度スコア: $(jq -r '.priority_score' "$analysis_report")/100

## 発見されたシナリオ
- Given: 基本機能が実装済みである
- When: ${scenario_type}の要求が発生した時
- Then: システムは適切に対応する

## フィードバック源
$(jq -r '.sources | keys | map("- " + .) | join("\n")' "$analysis_report")

## 発見経緯
フィードバック分析により、以下の要求が明確になりました：
$(jq -r '.sources | to_entries[] | "### " + .key + "\n" + (.value | split("\n")[0:3] | join("\n")) + "\n"' "$analysis_report")

## 実装への影響
- 影響レイヤー: Domain/Application/Infrastructure/Presentation
- 推定工数: $(case "$urgency" in
    "high") echo "2-3日" ;;
    "medium") echo "1-2週間" ;;
    *) echo "2-4週間" ;;
  esac)

## 関連ドキュメント
- [進化シナリオ](${scenario_document})"

        # 特性に基づくラベルを決定
        local labels="enhancement,evolved-scenario"
        case "$urgency" in
            "high") labels+=",priority-high,urgent" ;;
            "medium") labels+=",priority-medium" ;;
            "low") labels+=",priority-low" ;;
        esac

        case "$scenario_type" in
            "error_case") labels+=",bug,error-handling" ;;
            "edge_case") labels+=",edge-case" ;;
            "new_feature") labels+=",feature" ;;
        esac

        # 再試行メカニズム付きでイシューを作成
        local issue_title="実装: ${feature_name} ${scenario_type}対応"

        if safe_gh_command "issue" "create" --title "$issue_title" --body "$issue_body" --label "$labels"; then
            local new_issue_number=$(safe_gh_command "issue" "list" --label "evolved-scenario" --limit 1 --json number --jq '.[0].number')
            new_issues+=("$new_issue_number")
            issue_numbers+=("$new_issue_number")
            echo "✅ 新しいイシュー作成: #$new_issue_number"
        else
            echo "⚠️ 警告: イシューの作成に失敗しました"
        fi
    else
        echo "🔗 既存イシューにコメント追加中..."

        local comment="🔄 **シナリオ進化**

${feature_name}に関連して新しいシナリオを追加しました。

📋 **詳細**:
- シナリオタイプ: $(jq -r '.scenario_type' "$evolution_strategy_file")
- 緊急度: $(jq -r '.urgency' "$evolution_strategy_file")
- 実装タイミング: $(jq -r '.implementation_timing' "$evolution_strategy_file")

📄 **ドキュメント**: \`${scenario_document}\`

📊 **フィードバック分析**:
- 優先度スコア: $(jq -r '.priority_score' "$analysis_report")/100
- フィードバック源: $(jq -r '.sources | keys | join(", ")' "$analysis_report")"

        for issue_num in "${issue_numbers[@]}"; do
            if safe_gh_command "issue" "comment" "$issue_num" --body "$comment"; then
                echo "✅ Issue #$issue_num にコメント追加"
            else
                echo "⚠️ 警告: Issue #$issue_num へのコメント追加に失敗"
            fi
        done
    fi

    echo "${new_issues[@]}"
}

new_issue_numbers=($(manage_github_issues))
```

## 7. **シナリオインデックスとスプリント統合**

```bash
# シナリオインデックスを更新し、スプリント計画と統合
echo "📋 シナリオインデックスとスプリント統合を更新中..."

update_scenario_index() {
    local index_file="docs/use_cases/index.md"
    local current_sprint=$(find docs/sprints -name "sprint-*-backlog.md" | sed 's/.*sprint-\([0-9]*\).*/\1/' | sort -n | tail -1)
    if [[ -z "$current_sprint" ]]; then current_sprint="1"; fi

    # バックアップを作成
    if [[ -f "$index_file" ]]; then
        cp "$index_file" "${index_file}.backup"
        add_rollback_handler "mv '${index_file}.backup' '$index_file'"
    else
        mkdir -p "$(dirname "$index_file")"
        touch "$index_file"
    fi

    # 進化したシナリオセクションが存在しない場合は追加
    if ! grep -q "## 進化したシナリオ" "$index_file"; then
        cat >> "$index_file" << EOF

## 進化したシナリオ (Sprint ${current_sprint})
EOF
    fi

    # 新しいシナリオエントリを追加
    local scenario_name="${feature_name} $(jq -r '.scenario_type' "$evolution_strategy_file")対応"
    local issue_ref=""
    if [[ ${#issue_numbers[@]} -gt 0 ]]; then
        issue_ref="Issue #$(IFS=' #'; echo "${issue_numbers[*]}")"
    elif [[ ${#new_issue_numbers[@]} -gt 0 ]]; then
        issue_ref="Issue #$(IFS=' #'; echo "${new_issue_numbers[*]}")"
    else
        issue_ref="新規作成予定"
    fi

    cat >> "$index_file" << EOF
- [${scenario_name}]($(basename "$scenario_document")) - ${issue_ref}
  - 追加理由: フィードバック分析による$(jq -r '.scenario_type' "$evolution_strategy_file")要求
  - ステータス: 計画中
  - 緊急度: $(jq -r '.urgency' "$evolution_strategy_file")
  - 実装予定: $(jq -r '.implementation_timing' "$evolution_strategy_file")
EOF

    echo "✅ シナリオインデックス更新完了"
}

update_sprint_integration() {
    local timing=$(jq -r '.implementation_timing' "$evolution_strategy_file")
    local current_sprint=$(find docs/sprints -name "sprint-*-backlog.md" | sed 's/.*sprint-\([0-9]*\).*/\1/' | sort -n | tail -1)
    if [[ -z "$current_sprint" ]]; then current_sprint="1"; fi

    local target_sprint="$current_sprint"
    case "$timing" in
        "current_sprint") target_sprint="$current_sprint" ;;
        "next_sprint") target_sprint=$((current_sprint + 1)) ;;
        "future_sprint") target_sprint=$((current_sprint + 2)) ;;
    esac

    # 必要に応じてスプリントディレクトリを作成
    mkdir -p "docs/sprints"

    local sprint_backlog="docs/sprints/sprint-${target_sprint}-backlog.md"
    local evolution_report="docs/sprints/sprint-${current_sprint}-evolution.md"

    # スプリントバックログを更新
    if [[ ! -f "$sprint_backlog" ]]; then
        cat > "$sprint_backlog" << EOF
# スプリント${target_sprint} バックログ

## 進化したシナリオ

EOF
    fi

    # スプリントバックログに追加
    cat >> "$sprint_backlog" << EOF
### ${feature_name} 進化対応
- **Issue**: $(if [[ ${#issue_numbers[@]} -gt 0 || ${#new_issue_numbers[@]} -gt 0 ]]; then echo "#$(IFS=' #'; echo "${issue_numbers[*]}${new_issue_numbers[*]}")"; else echo "新規作成予定"; fi)
- **タイプ**: $(jq -r '.scenario_type' "$evolution_strategy_file")
- **緊急度**: $(jq -r '.urgency' "$evolution_strategy_file")
- **推定工数**: $(case "$(jq -r '.urgency' "$evolution_strategy_file")" in
    "high") echo "2-3日" ;;
    "medium") echo "1-2週間" ;;
    *) echo "2-4週間" ;;
  esac)

EOF

    # 進化レポートを作成
    cat > "$evolution_report" << EOF
# スプリント${current_sprint} シナリオ進化

## 追加されたシナリオ
1. ${feature_name} $(jq -r '.scenario_type' "$evolution_strategy_file")対応 - Issue $(if [[ ${#issue_numbers[@]} -gt 0 || ${#new_issue_numbers[@]} -gt 0 ]]; then echo "#$(IFS=' #'; echo "${issue_numbers[*]}${new_issue_numbers[*]}")"; else echo "新規作成予定"; fi)
   - 優先度: $(jq -r '.urgency' "$evolution_strategy_file")
   - 実装タイミング: スプリント${target_sprint}

## フィードバック分析結果
- **優先度スコア**: $(jq -r '.priority_score' "$analysis_report")/100
- **フィードバック源**: $(jq -r '.sources | keys | join(", ")' "$analysis_report")

## ビジョンへの影響
$(jq -r '.scenario_type' "$evolution_strategy_file")要求により、${feature_name}の機能拡張が必要。
既存アーキテクチャとの整合性は保たれる予定。

## 学習事項
- フィードバック駆動開発により早期に$(jq -r '.scenario_type' "$evolution_strategy_file")要求を発見
- 継続的なユーザーフィードバック収集の重要性を確認
- テスト結果からの学習により品質向上につながった

## 次のアクション
1. 対象スプリント（${target_sprint}）での実装計画策定
2. 関連チームとの調整
3. アーキテクチャレビューの実施

EOF

    echo "✅ スプリント統合更新完了"
    echo "  📋 対象スプリント: ${target_sprint}"
    echo "  📄 進化レポート: ${evolution_report}"
}

update_scenario_index
update_sprint_integration
```

## 8. **整合性検証とアーキテクチャ影響**

```bash
# 整合性を検証し、アーキテクチャ影響を分析
echo "🏗️ 整合性検証とアーキテクチャ影響分析中..."

validate_scenario_consistency() {
    echo "  🔍 既存シナリオとの整合性をチェック中..."

    local consistency_report="$feedback_analysis_dir/consistency_validation.json"
    local issues_found=0

    # 整合性レポートを初期化
    cat > "$consistency_report" << EOF
{
  "validation_date": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "feature": "$feature_name",
  "checks": {},
  "issues_found": 0,
  "recommendations": []
}
EOF

    # ビジョン整合性をチェック
    if [[ -f "docs/vision/core_vision.md" ]]; then
        if grep -i "$feature_name" "docs/vision/core_vision.md" >/dev/null 2>&1; then
            jq '.checks.vision_alignment = "aligned"' "$consistency_report" > "${consistency_report}.tmp" && mv "${consistency_report}.tmp" "$consistency_report"
            echo "    ✅ ビジョンとの整合性: 整合"
        else
            jq '.checks.vision_alignment = "needs_review" | .issues_found += 1' "$consistency_report" > "${consistency_report}.tmp" && mv "${consistency_report}.tmp" "$consistency_report"
            echo "    ⚠️ ビジョンとの整合性: 要確認"
            issues_found=$((issues_found + 1))
        fi
    fi

    # ユビキタス言語の一貫性をチェック
    if [[ -f "docs/domain/ubiquitous_language.md" ]]; then
        local language_conflicts=$(grep -i "$feature_name" "docs/domain/ubiquitous_language.md" | wc -l)
        if [[ $language_conflicts -gt 0 ]]; then
            jq '.checks.language_consistency = "consistent"' "$consistency_report" > "${consistency_report}.tmp" && mv "${consistency_report}.tmp" "$consistency_report"
            echo "    ✅ ユビキタス言語: 一貫性保持"
        else
            jq '.checks.language_consistency = "needs_update" | .issues_found += 1' "$consistency_report" > "${consistency_report}.tmp" && mv "${consistency_report}.tmp" "$consistency_report"
            echo "    ⚠️ ユビキタス言語: 更新必要"
            issues_found=$((issues_found + 1))
        fi
    fi

    # テスト可能性を検証
    local scenario_type=$(jq -r '.scenario_type' "$evolution_strategy_file")
    case "$scenario_type" in
        "error_case"|"edge_case")
            jq '.checks.testability = "high"' "$consistency_report" > "${consistency_report}.tmp" && mv "${consistency_report}.tmp" "$consistency_report"
            echo "    ✅ テスト可能性: 高"
            ;;
        "new_feature")
            jq '.checks.testability = "medium"' "$consistency_report" > "${consistency_report}.tmp" && mv "${consistency_report}.tmp" "$consistency_report"
            echo "    📊 テスト可能性: 中"
            ;;
        *)
            jq '.checks.testability = "needs_analysis"' "$consistency_report" > "${consistency_report}.tmp" && mv "${consistency_report}.tmp" "$consistency_report"
            echo "    ⚠️ テスト可能性: 要分析"
            issues_found=$((issues_found + 1))
            ;;
    esac

    # 最終的な問題数を更新
    jq --argjson count "$issues_found" '.issues_found = $count' "$consistency_report" > "${consistency_report}.tmp" && mv "${consistency_report}.tmp" "$consistency_report"

    echo "  📊 整合性チェック完了: $issues_found 件の要確認項目"

    return $issues_found
}

analyze_architecture_impact() {
    echo "  🏗️ アーキテクチャ影響を分析中..."

    local impact_report="$feedback_analysis_dir/architecture_impact.json"

    # シナリオタイプに基づく影響レイヤーを決定
    local scenario_type=$(jq -r '.scenario_type' "$evolution_strategy_file")
    local impacted_layers=()
    local complexity_score=0

    case "$scenario_type" in
        "error_case")
            impacted_layers=("Domain" "Application" "Presentation")
            complexity_score=60
            ;;
        "edge_case")
            impacted_layers=("Domain" "Application")
            complexity_score=40
            ;;
        "new_feature")
            impacted_layers=("Domain" "Application" "Infrastructure" "Presentation")
            complexity_score=80
            ;;
        "extension")
            impacted_layers=("Application" "Presentation")
            complexity_score=30
            ;;
    esac

    cat > "$impact_report" << EOF
{
  "analysis_date": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "feature": "$feature_name",
  "scenario_type": "$scenario_type",
  "impacted_layers": $(printf '%s\n' "${impacted_layers[@]}" | jq -R . | jq -s .),
  "complexity_score": $complexity_score,
  "recommendations": [
    "影響レイヤー数: ${#impacted_layers[@]}",
    "複雑度スコア: $complexity_score/100",
    "推奨レビュー: $(if [[ $complexity_score -ge 70 ]]; then echo "アーキテクチャレビュー必須"; elif [[ $complexity_score -ge 40 ]]; then echo "設計レビュー推奨"; else echo "実装レビューで十分"; fi)"
  ]
}
EOF

    echo "  📊 影響分析完了:"
    echo "    🎯 影響レイヤー: ${impacted_layers[*]}"
    echo "    📈 複雑度: $complexity_score/100"

    # 可能であれば現在のアーキテクチャを検証
    if command -v validate_architecture_compliance >/dev/null 2>&1; then
        if validate_architecture_compliance; then
            echo "    ✅ 現在のアーキテクチャ: 準拠"
        else
            echo "    ⚠️ 現在のアーキテクチャ: 要確認"
        fi
    fi
}

# 検証を実行
if validate_scenario_consistency; then
    echo "✅ 整合性検証: 問題なし"
else
    echo "⚠️ 整合性検証: 要確認項目あり（継続可能）"
fi

analyze_architecture_impact
```

## 9. **アトミックメタデータ更新**

```bash
# 進化情報でメタデータを更新
echo "📊 メタデータを原子的に更新中..."

if [[ -f "$metadata_file" ]]; then
    # 進化サイクルをカウント
    current_count=$(jq '.phases.scenario_evolution.evolution_count // 0' "$metadata_file")
    new_count=$((current_count + 1))

    # メタデータ用のすべてのイシュー番号を準備
    all_issues=("${issue_numbers[@]}" "${new_issue_numbers[@]}")
    issue_json=$(printf '%s\n' "${all_issues[@]}" | jq -R . | jq -s .)

    # メタデータをアトミックに更新
    update_metadata_atomic "$metadata_file" "
        .phases.scenario_evolution.evolved = true |
        .phases.scenario_evolution.evolution_count = ${new_count} |
        .phases.scenario_evolution.last_evolved_at = \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\" |
        .phases.scenario_evolution.scenario_type = \"$(jq -r '.scenario_type' "$evolution_strategy_file")\" |
        .phases.scenario_evolution.urgency = \"$(jq -r '.urgency' "$evolution_strategy_file")\" |
        .phases.scenario_evolution.implementation_timing = \"$(jq -r '.implementation_timing' "$evolution_strategy_file")\" |
        .phases.scenario_evolution.scenario_document = \"$scenario_document\" |
        .phases.scenario_evolution.analysis_report = \"$analysis_report\" |
        .phases.scenario_evolution.related_issues = $issue_json |
        .updated_at = \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\" |
        .phase = \"scenarios_evolved\"
    "

    echo "✅ メタデータ更新完了（進化回数: ${new_count}）"
else
    echo "⚠️ 警告: メタデータファイルが見つかりません"
fi
```

## 10. **トランザクションコミットとサマリー**

```bash
# トランザクションをコミットし、包括的なサマリーを提供
echo "💾 シナリオ進化をコミット中..."

# 作成されたすべてのファイルをgitに追加
git add -A

# 包括的なコミットメッセージを作成
commit_message="feat: evolve scenarios for ${feature_name}

Scenario evolution cycle #${new_count} completed based on comprehensive feedback analysis.

Evolution Details:
- Feature: ${feature_name}
- Type: $(jq -r '.scenario_type' "$evolution_strategy_file")
- Urgency: $(jq -r '.urgency' "$evolution_strategy_file")
- Implementation: $(jq -r '.implementation_timing' "$evolution_strategy_file")
- Priority Score: $(jq -r '.priority_score' "$analysis_report")/100

Generated Documents:
- Scenario Document: ${scenario_document}
- Analysis Report: ${analysis_report}
- Strategy Document: ${evolution_strategy_file}

Feedback Sources:
$(jq -r '.sources | keys | map("- " + .) | join("\n")' "$analysis_report")

Related Issues: $(if [[ ${#issue_numbers[@]} -gt 0 || ${#new_issue_numbers[@]} -gt 0 ]]; then echo "#$(IFS=' #'; echo "${issue_numbers[*]}${new_issue_numbers[*]}")"; else echo "None"; fi)"

# 変更をコミット
if git commit -m "$commit_message"; then
    echo "✅ Git コミット完了"
else
    echo "⚠️ 警告: Git コミットに失敗しました"
fi

# トランザクションをコミット
commit_transaction

# 包括的なサマリーを表示
echo ""
echo "🎉 シナリオ進化完了!"
echo ""
echo "📊 **進化サマリー**:"
echo "   - Feature: ${feature_name}"
echo "   - Evolution Cycle: ${new_count}"
echo "   - Scenario Type: $(jq -r '.scenario_type' "$evolution_strategy_file")"
echo "   - Urgency: $(jq -r '.urgency' "$evolution_strategy_file")"
echo "   - Implementation: $(jq -r '.implementation_timing' "$evolution_strategy_file")"
echo "   - Priority Score: $(jq -r '.priority_score' "$analysis_report")/100"
echo ""
echo "🔍 **フィードバック分析**:"
echo "   - Sources: $(jq -r '.sources | length' "$analysis_report") 種類"
echo "   - Source Types: $(jq -r '.sources | keys | join(", ")' "$analysis_report")"
echo ""
echo "📋 **作成されたリソース**:"
echo "   - 📄 シナリオドキュメント: ${scenario_document}"
echo "   - 📊 分析レポート: ${analysis_report}"
echo "   - 🎯 戦略ドキュメント: ${evolution_strategy_file}"
if [[ ${#new_issue_numbers[@]} -gt 0 ]]; then
    echo "   - 🆕 新規Issue: #$(IFS=' #'; echo "${new_issue_numbers[*]}")"
fi
if [[ ${#issue_numbers[@]} -gt 0 ]]; then
    echo "   - 🔗 関連Issue: #$(IFS=' #'; echo "${issue_numbers[*]}")"
fi
echo ""
echo "🔍 **次のステップ**:"

case "$(jq -r '.implementation_timing' "$evolution_strategy_file")" in
    "current_sprint")
        echo "   - 🚨 緊急: 現在のスプリントで実装開始"
        echo "   - 💡 推奨: /create-tests $(if [[ ${#issue_numbers[@]} -gt 0 || ${#new_issue_numbers[@]} -gt 0 ]]; then echo "$(IFS=','; echo "${issue_numbers[*]}${new_issue_numbers[*]}")"; else echo "<issue-number>"; fi)"
        ;;
    "next_sprint")
        echo "   - 📅 計画: 次のスプリントで実装予定"
        echo "   - 💡 推奨: /sprint-planning $((current_sprint + 1))"
        ;;
    *)
        echo "   - 📋 計画: 将来のスプリントで実装検討"
        echo "   - 💡 推奨: /use-case-status で状況確認"
        ;;
esac

echo "   - 📊 状況確認: /use-case-status ${feature_name}"
echo "   - 📝 レビュー: /review-issue $(if [[ ${#issue_numbers[@]} -gt 0 || ${#new_issue_numbers[@]} -gt 0 ]]; then echo "$(IFS=','; echo "${issue_numbers[*]}${new_issue_numbers[*]}")"; else echo "<issue-number>"; fi)"
echo ""
echo "✅ シナリオ進化プロセスが正常に完了しました"
```

## 重要な注意事項

### **包括的フィードバック分析**

- 複数のフィードバック源（スプリント、レビュー、GitHub、テスト）の自動統合
- 優先度スコアによる客観的な重要度評価
- 進化戦略の自動決定とタイミング提案

### **安全性保証**

- 全操作でのトランザクション管理とロールバック機能
- 既存ドキュメントのバックアップと復旧
- GitHub APIの安全な実行とエラーハンドリング

### **整合性とトレーサビリティ**

- 既存アーキテクチャとの一貫性自動検証
- フィードバックから実装までの完全追跡
- スプリント計画との自動統合

### **チーム協力支援**

- 詳細な分析レポートと推奨事項の提供
- GitHubイシューとの完全連携
- 実装タイミングの最適化提案

**統合版シナリオ進化コマンドにより、フィードバック駆動開発が安全かつ効率的に実現されます！**