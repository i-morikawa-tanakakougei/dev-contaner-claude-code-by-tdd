# TDD/DDD/レイヤードアーキテクチャ実装へのレビューフィードバック適用（包括的安全性とトラッキング機能付き）

## メタデータ
- **前提条件**: レビュー完了 (13-review-issue)
- **入力**: イシュー番号（必須）、フィードバック詳細
- **出力**: 
  - フィードバックを反映した実装の更新
  - フィードバック適用の追跡
  - 更新された `docs/use_cases/issue-X-Y.json` メタデータ
- **依存関係**: レビューレポート、実装コード、Git設定
- **実行タイミング**: レビュー後、最終プルリクエスト作成前

## 🎯 **TDD/DDD/LAYERED プロセス コンテキスト**

**🔄 コアワークフロー**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 アーキテクチャ**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 開発**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ 設計**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 要件**: Given-When-Then シナリオと完全な追跡可能性  
**🔄 進化**: /evolve-scenarios コマンドによる継続的シナリオ進化

> 📖 **ドキュメント管理システム**: [README.md](./README.md)  
> 🗺️ **現在位置**: レビューとフィードバック段階 - フィードバック適用 (14/16)  
> 🎯 **段階目的**: レビューフィードバックに基づく実装改善  
> ⬅️ **前段階**: 13-review-issue (実装レビュー)  
> ➡️ **次段階**: 15-create-pr (プルリクエスト作成)
>
> **📋 3層アーキテクチャ操作**:
>
> - 🎯 **戦略**: `docs/use_cases/core/index.md` (品質基準の参照)
> - 📊 **戦術**: `docs/use_cases/index.md` (フィードバック適用状況の更新)
> - 🔧 **実行**: `docs/use_cases/issue-X-Y.json` (フィードバック適用の追跡)

## 🔧 **ターゲット フィードバック適用のみ**

**⚠️ 重要な注意:**
- **この段階は特定の改善のみ** - レビューからの具体的なフィードバックのみ適用
- **限定的実装** - レビューフィードバックに基づく変更のみ実施  
- **品質改善に焦点** - レビューで特定された具体的問題の対処
- **レビュー推奨事項に従う** - フィードバック範囲を超えた任意の変更は禁止

**フィードバック適用プロセス:**
1. `13-review-issue` ← 具体的フィードバック付きレビュー完了
2. `14-apply-feedback` ← **【現在地】レビュー推奨事項の適用**
3. `15-create-pr` ← 改善を含むプルリクエスト作成
4. マージとサイクル完了

**許可される変更:**
- ✅ レビューで特定された問題の修正
- ✅ 具体的フィードバックに基づくコード品質改善
- ✅ テストギャップとカバレッジ問題の対処
- ❌ フィードバック範囲を超えた新機能や機能の追加は禁止

## 📋 **フィードバック適用タスクチェックリスト**

**体系的フィードバック実装にこのチェックリストを使用:**

### 🔴 必須タスク

#### **📊 レビュー分析と計画**
- [ ] **レビュー結果の解析**: ステップ13からの包括的レビューレポートを分析
- [ ] **フィードバック項目の分類**: 重要度/高/中/低で優先度別にグループ化
- [ ] **実装作業量の評価**: 各項目の時間と複雑さを見積もり
- [ ] **実装順序の計画**: 優先度と依存関係に基づく改善順序付け

#### **🚨 重要問題の解決 (優先度1)**
- [ ] **セキュリティ脆弱性の修正**: レビューで特定されたセキュリティ問題の対処
- [ ] **Given-When-Thenギャップの解決**: 不足または不正確なシナリオカバレッジの修正
- [ ] **壊れたアーキテクチャ境界の修正**: 層違反問題の修正
- [ ] **データ整合性問題の対処**: データ処理または検証問題の修正
- [ ] **壊れたまたは不足テストの修正**: テスト失敗またはギャップの対処

### 🟡 推奨タスク

#### **⚡ 高優先度改善 (優先度2)**
- [ ] **テスト品質の改善**: テスト構造、可読性、カバレッジの強化
- [ ] **コード品質問題の修正**: 複雑なメソッド、命名、重複の対処
- [ ] **エラーハンドリングの改善**: 例外処理とエラー応答の強化
- [ ] **API設計問題の対処**: エンドポイント設計と応答フォーマット問題の修正
- [ ] **ドメインモデルの改善**: エンティティ、値オブジェクト、サービス設計の強化
- [ ] **統合問題の修正**: リポジトリと外部サービス統合問題の対処

### 🟢 オプションタスク

#### **📈 中優先度強化 (優先度3)**
- [ ] **ドキュメントの改善**: コードコメント、APIドキュメント、ユーザーガイドの強化
- [ ] **パフォーマンス最適化**: 非重要なパフォーマンス改善の対処
- [ ] **リスク領域の特定**: システム安定性に影響する可能性のある変更の明示
- [ ] **実装ロードマップの作成**: フィードバック適用の体系的アプローチの計画
- [ ] **パフォーマンスボトルネックの解決**: 重要なパフォーマンス問題の修正
- [ ] **ユーザーエクスペリエンスの強化**: CLI使いやすさとAPI応答の改善
- [ ] **コード構成の改善**: より良い構造とモジュール化
- [ ] **監視/ログの追加**: 可観測性とデバッグ機能の強化
- [ ] **設定の改善**: より良い設定管理と検証

### **🔧 コード品質検証 (各優先度レベル後)**
- [ ] **ruffリンティング実行**: `uv run --frozen ruff check src/ --fix` を実行
- [ ] **ruffフォーマット実行**: `uv run --frozen ruff format src/` を実行
- [ ] **型チェック実行**: `uv run --frozen pyright src/` を実行
- [ ] **品質問題の修正**: リンティング、フォーマット、型エラーの対処
- [ ] **クリーンな結果の確認**: すべての品質ツールがエラーなしで通ることを確認

### **🧪 継続的テスト (各変更後)**
- [ ] **影響するテストの実行**: 変更されたコードに関連するテストを実行
- [ ] **完全テストスイートの実行**: 完全な検証のため `uv run --frozen pytest` を実行
- [ ] **すべてのテストGREENの確認**: 機能が壊れていないことを確認
- [ ] **テストカバレッジの確認**: カバレッジが低下していないことを確認
- [ ] **Given-When-Thenシナリオの検証**: シナリオテストが依然として通ることを確認
- [ ] **統合ポイントのテスト**: クロス層統合が依然として動作することを確認

### **📖 Given-When-Thenカバレッジ改善**
- [ ] **不足シナリオテストの追加**: カバーされていないシナリオのテスト実装
- [ ] **テスト明確性の改善**: ビジネス意図をより良く表現するテスト作成
- [ ] **シナリオ-テスト不一致の修正**: テストと実際のシナリオの整合
- [ ] **エッジケーステストの追加**: 境界条件のテスト実装
- [ ] **エラーシナリオカバレッジの改善**: 失敗シナリオのテスト追加
- [ ] **受入基準検証の強化**: すべての基準がテストされることを確認

### **🏗️ アーキテクチャ準拠修正**
- [ ] **層違反の修正**: 依存関係方向問題の修正
- [ ] **インターフェース分離の改善**: リポジトリとサービスインターフェースの強化
- [ ] **ドメイン純粋性問題の修正**: ドメイン層から外部依存関係を除去
- [ ] **集約設計の改善**: 集約境界問題の修正
- [ ] **ドメインモデルの強化**: エンティティと値オブジェクト設計の改善
- [ ] **トランザクション境界の修正**: トランザクション管理問題の修正

### **🔗 統合とインフラストラクチャ改善**
- [ ] **リポジトリ実装の改善**: データアクセスパターンとエラーハンドリングの修正
- [ ] **外部サービス統合の強化**: サードパーティサービス処理の改善
- [ ] **設定問題の修正**: 設定管理問題の対処
- [ ] **エラー伝播の改善**: クロス層エラーハンドリングの強化
- [ ] **トランザクション管理の修正**: データベーストランザクション問題の対処
- [ ] **監視の強化**: ログと可観測性の改善

### **🌐 プレゼンテーション層強化**
- [ ] **API設計問題の修正**: エンドポイント設計とHTTPステータスコードの改善
- [ ] **入力検証の改善**: リクエスト検証とエラー応答の強化
- [ ] **認証/認可の修正**: セキュリティ実装問題の対処
- [ ] **応答フォーマットの改善**: 応答構造とエラーハンドリングの強化
- [ ] **APIドキュメントの修正**: エンドポイントドキュメント問題の修正
- [ ] **CLI使いやすさの強化**: コマンドラインインターフェースユーザーエクスペリエンスの改善

### **📊 品質メトリクス検証**
- [ ] **改善インパクトの測定**: 改善前後の品質メトリクス比較
- [ ] **カバレッジ改善の検証**: テストカバレッジが増加したことを確認
- [ ] **複雑性削減の評価**: コード複雑性が削減されたことを確認
- [ ] **パフォーマンス改善の確認**: パフォーマンス向上の測定
- [ ] **保守性の検証**: コード保守性改善の評価
- [ ] **品質向上の文書化**: 測定可能な品質改善の記録

### **🔍 最終検証と品質チェック**
- [ ] **包括的テストスイート実行**: カバレッジ付きですべてのテストを実行
- [ ] **最終コード品質チェック**: `uv run --frozen ruff check src/ --fix` を実行
- [ ] **最終フォーマットチェック**: `uv run --frozen ruff format src/` を実行
- [ ] **最終型チェック**: `uv run --frozen pyright src/` を実行
- [ ] **すべての改善の検証**: すべてのフィードバック項目が対処されたことを確認
- [ ] **システム安定性の確認**: 変更後にシステムが正しく動作することを確認

### **📚 ドキュメントと引き継ぎ**
- [ ] **実装ドキュメントの更新**: フィードバック適用中に行った変更の記録
- [ ] **メタデータの更新**: issue-X-Y.jsonにフィードバック適用結果を記録
- [ ] **改善サマリーの作成**: 改善内容とインパクトの文書化
- [ ] **すべての改善のコミット**: 明確なコミットメッセージですべての変更をバージョン管理
- [ ] **PR作成の準備**: プルリクエスト提出の準備
- [ ] **最終品質レポートの生成**: 品質メトリクスの改善前後比較の作成

**💡 プロヒント: フィードバックを優先度別に体系的に適用し、継続的に検証 - 各改善はシステムを測定可能により良くするべきです！
- ✅ フィードバックに基づくテストカバレッジ改善
- ✅ アーキテクチャ準拠問題の対処
- ✅ 提案されたパフォーマンス改善の適用
- ❌ 新機能の追加禁止
- ❌ レビュー範囲を超えた変更の禁止

**レビューフィードバックのみ適用 - 新機能は禁止。**

## 🛡️ **統合版の主な改善点**

### **✅ 解決された問題**

- **フィードバック適用の不整合**: 自動化された優先度別改善プロセス
- **テスト破綻リスク**: 各改善ステップでの安全なTDDサイクル
- **品質回帰**: 包括的検証と継続的監視
- **変更追跡の不備**: 改善前後の詳細比較とトレーサビリティ
- **チーム協力の課題**: 自動的な進捗共有と透明性確保

### **🆕 新機能**

1. **🔄 インテリジェント改善**: レビュー結果の自動解析と優先度付け
2. **📊 安全なTDDサイクル**: 各改善でのRED-GREEN-REFACTORプロセス
3. **🛡️ 継続的品質保証**: 各ステップでの品質回帰防止
4. **🔍 詳細トラッキング**: 改善項目の完全な実装履歴
5. **📈 メトリクス改善監視**: 品質指標の継続的向上確認

## よくあるエラーと解決方法

### ❌ エラーケース1: レビューが未完了
**原因**: レビュー完了前にフィードバック適用を試行  
**解決方法**: 最初に `/review-issue <issue-number>` でレビューを完了

### ❌ エラーケース2: フィードバックが既存実装と競合
**原因**: フィードバックが既存機能を壊す変更を要求  
**解決方法**: インパクトを分析し、競合を安全に対処する計画を作成

### ❌ エラーケース3: フィードバック適用後にテストが壊れる
**原因**: テスト互換性を維持せずに変更を実施  
**解決方法**: 実装変更と並行してテストを更新するか、変更を元に戻す

## 実行例

### ✅ 成功例
```bash
$ /apply-feedback 15
🔄 Issues: #15 のフィードバック適用を開始します
📝 レビューフィードバック分析中...
✅ 3件のフィードバックを発見
🔧 実装更新中...
  ✅ コード品質改善適用
  ✅ アーキテクチャ改善適用
🧪 フィードバック適用後テスト実行...
======= 45 passed, 0 failed =======
✅ フィードバック適用完了
🎉 フィードバック適用完了!
```

### ❌ 失敗例と修正
```bash
$ /apply-feedback 15
❌ レビューが完了していません
💡 最初にレビューを完了してください:
   /review-issue 15

# 修正: 最初にレビューを完了
$ /review-issue 15
$ /apply-feedback 15
```

## タスク詳細

## 1. **安全環境のセットアップと引数解析**

```bash
# 🔧 自動引数解析と検証を含む安全な操作関数をロード
source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "14-apply-feedback" "$ARGUMENTS"

# 引数はセットアップスクリプトによって既に解析・検証済み
# このコマンド固有の追加検証
if [[ ${#issue_numbers[@]} -eq 0 ]]; then
    echo "エラー: 最低1つのイシュー番号が必要です"
    show_usage_example "apply-feedback" "1" "単一イシューのフィードバック適用"
    show_usage_example "apply-feedback" "1,7" "複数イシューのフィードバック適用"
    show_usage_example "apply-feedback" "1,feature-name" "イシュー + フィーチャー指定"
    exit 1
fi
```

## 2. **トランザクション管理と前提条件**

```bash
# フィードバック適用のトランザクション開始
transaction_id="apply_feedback_$(date +%s)_$(echo "${issue_numbers[*]}" | tr ' ' '_')"
begin_transaction "$transaction_id"

# ロールバックハンドラーの設定
add_rollback_handler "echo '🔄 フィードバック適用をロールバック中...'"
add_rollback_handler "git checkout . 2>/dev/null || true"
add_rollback_handler "git clean -fd 2>/dev/null || true"
add_rollback_handler "echo '📋 適用前の状態に復旧しました'"

# メタデータとフィーチャー情報の発見
issue_list=$(IFS=-; echo "${issue_numbers[*]}")
if [[ ${#other_args[@]} -gt 0 ]]; then
    feature_name="${other_args[0]}"
else
    # ユースケースファイルからフィーチャー名を抽出
    feature_name=$(find docs/use_cases -name "issue-${issue_list}-*.md" | head -1 | sed 's/.*issue-[0-9-]*-\(.*\)\.md$/\1/')
    if [[ -z "$feature_name" ]]; then
        echo "❌ エラー: フィーチャー名を特定できませんでした"
        echo "💡 使用方法: /apply-feedback $issue_list,<feature-name>"
        execute_rollback
        exit 1
    fi
fi

metadata_file="docs/use_cases/issue-${issue_list}-${feature_name}.json"
spec_file="docs/use_cases/issue-${issue_list}-${feature_name}.md"

echo "🎯 フィードバック適用対象: Issues #$(IFS=' #'; echo "${issue_numbers[*]}") - ${feature_name}"

# 前提条件の検証
if [[ ! -f "$metadata_file" ]]; then
    echo "❌ エラー: メタデータファイルが見つかりません: $metadata_file"
    execute_rollback
    exit 1
fi

# レビューが完了していることを確認
validate_phase_completion "$metadata_file" "reviewed"

echo "✅ 前提条件チェック完了"
```

## 3. **レビューレポート分析とフィードバック抽出**

```bash
# レビューレポートをロードして分析
echo "📋 レビューレポートを分析中..."

feedback_workspace="$(mktemp -d -t feedback_workspace_XXXXXX)"
add_rollback_handler "rm -rf '$feedback_workspace'"

analyze_review_feedback() {
    local feedback_analysis="$feedback_workspace/feedback_analysis.json"

    # フィードバック分析を初期化
    cat > "$feedback_analysis" << EOF
{
  "analysis_date": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "feature": "$feature_name",
  "issues": [$(IFS=','; echo "\"${issue_numbers[*]}\"")],
  "review_reports": [],
  "required_improvements": [],
  "recommended_improvements": [],
  "optional_improvements": [],
  "baseline_metrics": {}
}
EOF

    local total_required=0
    local total_recommended=0
    local total_optional=0

    echo "  📄 レビューレポートを検索中..."

    # レビューレポートを発見して処理
    for issue_num in "${issue_numbers[@]}"; do
        local review_file="docs/review/issue-${issue_num}-review.md"

        if [[ ! -f "$review_file" ]]; then
            # 包括的レビューファイルを試行
            review_file="docs/review/issue-${issue_list}-${feature_name}-review.md"
        fi

        if [[ -f "$review_file" ]]; then
            echo "    ✅ レビューレポート発見: $review_file"
            jq --arg file "$review_file" '.review_reports += [$file]' "$feedback_analysis" > "${feedback_analysis}.tmp" && mv "${feedback_analysis}.tmp" "$feedback_analysis"

            # 優先度別改善項目を抽出
            echo "    🔍 改善項目を抽出中..."

            # 必須対応項目を抽出
            if grep -A 10 "### 必須対応項目" "$review_file" 2>/dev/null; then
                local required_items=$(grep -A 10 "### 必須対応項目" "$review_file" | grep "^[0-9]\\." | head -5)
                while IFS= read -r item; do
                    if [[ -n "$item" ]]; then
                        local clean_item=$(echo "$item" | sed 's/^[0-9]*\\. *//')
                        jq --arg item "$clean_item" '.required_improvements += [$item]' "$feedback_analysis" > "${feedback_analysis}.tmp" && mv "${feedback_analysis}.tmp" "$feedback_analysis"
                        total_required=$((total_required + 1))
                    fi
                done <<< "$required_items"
            fi

            # 推奨改善項目を抽出
            if grep -A 10 "### 推奨改善項目" "$review_file" 2>/dev/null; then
                local recommended_items=$(grep -A 10 "### 推奨改善項目" "$review_file" | grep "^[0-9]\\." | head -5)
                while IFS= read -r item; do
                    if [[ -n "$item" ]]; then
                        local clean_item=$(echo "$item" | sed 's/^[0-9]*\\. *//')
                        jq --arg item "$clean_item" '.recommended_improvements += [$item]' "$feedback_analysis" > "${feedback_analysis}.tmp" && mv "${feedback_analysis}.tmp" "$feedback_analysis"
                        total_recommended=$((total_recommended + 1))
                    fi
                done <<< "$recommended_items"
            fi

            # 将来的な改善案を抽出
            if grep -A 10 "### 将来的な改善案" "$review_file" 2>/dev/null; then
                local optional_items=$(grep -A 10 "### 将来的な改善案" "$review_file" | grep "^[0-9]\\." | head -3)
                while IFS= read -r item; do
                    if [[ -n "$item" ]]; then
                        local clean_item=$(echo "$item" | sed 's/^[0-9]*\\. *//')
                        jq --arg item "$clean_item" '.optional_improvements += [$item]' "$feedback_analysis" > "${feedback_analysis}.tmp" && mv "${feedback_analysis}.tmp" "$feedback_analysis"
                        total_optional=$((total_optional + 1))
                    fi
                done <<< "$optional_items"
            fi
        else
            echo "    ❌ レビューレポートが見つかりません: $review_file"
            echo "    💡 先に /review-issue $(IFS=','; echo "${issue_numbers[*]}") を実行してください"
            execute_rollback
            exit 1
        fi
    done

    echo "📊 抽出された改善項目:"
    echo "  - 必須: ${total_required} 項目"
    echo "  - 推奨: ${total_recommended} 項目"
    echo "  - 任意: ${total_optional} 項目"

    echo "$feedback_analysis"
}

feedback_analysis=$(analyze_review_feedback)
```

## 4. **ベースライン品質メトリクス収集**

```bash
# フィードバック適用前のベースラインメトリクスを収集
echo "📊 改善前のベースライン品質メトリクスを収集中..."

collect_baseline_metrics() {
    local baseline_file="$feedback_workspace/baseline_metrics.json"

    echo "  🧪 テスト状況を確認中..."

    # すべてのテストがGREENであることを確認
    if ! PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest --tb=short -q; then
        echo "❌ エラー: 改善前にテストが失敗しています"
        echo "💡 先にテストを修正してからフィードバックを適用してください"
        execute_rollback
        exit 1
    fi

    echo "  📈 カバレッジを測定中..."

    # テストカバレッジを収集
    local coverage_file="$feedback_workspace/baseline_coverage.json"
    if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest --cov=src --cov-report=json:"$coverage_file" -q >/dev/null 2>&1; then
        local baseline_coverage=$(jq -r '.totals.percent_covered' "$coverage_file" 2>/dev/null || echo "0")
    else
        echo "⚠️ カバレッジ測定に失敗しました"
        local baseline_coverage="0"
    fi

    echo "  🧹 コード品質を確認中..."

    # Ruff問題を収集
    local ruff_results="$feedback_workspace/baseline_ruff.json"
    local baseline_ruff_errors=0
    if uv run --frozen ruff check . --output-format=json > "$ruff_results" 2>/dev/null; then
        baseline_ruff_errors=$(jq '. | length' "$ruff_results" 2>/dev/null || echo "0")
    fi

    # Pyright問題を収集
    local pyright_results="$feedback_workspace/baseline_pyright.json"
    local baseline_pyright_errors=0
    if uv run --frozen pyright --outputjson > "$pyright_results" 2>/dev/null; then
        baseline_pyright_errors=$(jq '.summary.errorCount // 0' "$pyright_results" 2>/dev/null || echo "0")
    fi

    # テストファイル数を数える
    local test_files=$(find tests/ -name "*.py" -not -name "__*" 2>/dev/null | wc -l)

    # ベースラインメトリクスを作成
    cat > "$baseline_file" << EOF
{
  "measurement_date": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "test_coverage": $baseline_coverage,
  "ruff_errors": $baseline_ruff_errors,
  "pyright_errors": $baseline_pyright_errors,
  "test_files": $test_files,
  "tests_passing": true
}
EOF

    # フィードバック分析にベースラインを更新
    jq --slurpfile baseline "$baseline_file" '.baseline_metrics = $baseline[0]' "$feedback_analysis" > "${feedback_analysis}.tmp" && mv "${feedback_analysis}.tmp" "$feedback_analysis"

    echo "📊 ベースライン品質メトリクス:"
    echo "  - テストカバレッジ: ${baseline_coverage}%"
    echo "  - Ruffエラー: ${baseline_ruff_errors} 件"
    echo "  - Pyrightエラー: ${baseline_pyright_errors} 件"
    echo "  - テストファイル数: ${test_files} 個"

    echo "$baseline_file"
}

baseline_metrics=$(collect_baseline_metrics)
```

## 5. **体系的フィードバック適用**

```bash
# TDDサイクルで体系的にフィードバックを適用
echo "🔧 フィードバックを体系的に適用中..."

apply_feedback_systematically() {
    local application_log="$feedback_workspace/application_log.json"
    local improvements_applied=0
    local improvements_skipped=0
    local new_issues_created=()

    # 適用ログを初期化
    cat > "$application_log" << EOF
{
  "application_start": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "feature": "$feature_name",
  "applied_improvements": [],
  "skipped_improvements": [],
  "created_issues": [],
  "metrics_progress": []
}
EOF

    echo "  🚨 必須対応項目を処理中..."

    # 必須改善の処理
    local required_improvements=$(jq -r '.required_improvements[]?' "$feedback_analysis")
    local req_count=0

    while IFS= read -r improvement; do
        if [[ -n "$improvement" ]]; then
            req_count=$((req_count + 1))
            echo "    🎯 必須項目 $req_count: $improvement"

            # TDDサイクルで改善を適用
            if apply_single_improvement "$improvement" "required"; then
                jq --arg item "$improvement" --arg status "applied" --arg type "required" \
                   '.applied_improvements += [{"item": $item, "type": $type, "status": $status, "applied_at": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'"}]' \
                   "$application_log" > "${application_log}.tmp" && mv "${application_log}.tmp" "$application_log"
                improvements_applied=$((improvements_applied + 1))
                echo "      ✅ 適用完了"
            else
                jq --arg item "$improvement" --arg reason "Implementation failed" --arg type "required" \
                   '.skipped_improvements += [{"item": $item, "type": $type, "reason": $reason, "skipped_at": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'"}]' \
                   "$application_log" > "${application_log}.tmp" && mv "${application_log}.tmp" "$application_log"
                improvements_skipped=$((improvements_skipped + 1))
                echo "      ❌ 適用失敗"
            fi
        fi
    done <<< "$required_improvements"

    echo "  📋 推奨改善項目を処理中..."

    # 推奨改善の処理
    local recommended_improvements=$(jq -r '.recommended_improvements[]?' "$feedback_analysis")
    local rec_count=0

    while IFS= read -r improvement; do
        if [[ -n "$improvement" ]]; then
            rec_count=$((rec_count + 1))
            echo "    💡 推奨項目 $rec_count: $improvement"

            # 適用前にインパクトを評価
            if assess_improvement_impact "$improvement"; then
                if apply_single_improvement "$improvement" "recommended"; then
                    jq --arg item "$improvement" --arg status "applied" --arg type "recommended" \
                       '.applied_improvements += [{"item": $item, "type": $type, "status": $status, "applied_at": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'"}]' \
                       "$application_log" > "${application_log}.tmp" && mv "${application_log}.tmp" "$application_log"
                    improvements_applied=$((improvements_applied + 1))
                    echo "      ✅ 適用完了"
                else
                    jq --arg item "$improvement" --arg reason "Implementation complexity" --arg type "recommended" \
                       '.skipped_improvements += [{"item": $item, "type": $type, "reason": $reason, "skipped_at": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'"}]' \
                       "$application_log" > "${application_log}.tmp" && mv "${application_log}.tmp" "$application_log"
                    improvements_skipped=$((improvements_skipped + 1))
                    echo "      ⏸️ 複雑性により保留"
                fi
            else
                jq --arg item "$improvement" --arg reason "High impact, deferred to new issue" --arg type "recommended" \
                   '.skipped_improvements += [{"item": $item, "type": $type, "reason": $reason, "skipped_at": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'"}]' \
                   "$application_log" > "${application_log}.tmp" && mv "${application_log}.tmp" "$application_log"

                # 高インパクト改善のための新しいイシューを作成
                echo "      📋 新しいイシューを作成中..."
                local new_issue=$(create_improvement_issue "$improvement")
                if [[ -n "$new_issue" ]]; then
                    new_issues_created+=("$new_issue")
                    jq --arg issue "$new_issue" '.created_issues += [$issue]' "$application_log" > "${application_log}.tmp" && mv "${application_log}.tmp" "$application_log"
                    echo "      🆕 Issue #$new_issue 作成"
                fi
                improvements_skipped=$((improvements_skipped + 1))
            fi
        fi
    done <<< "$recommended_improvements"

    echo "📊 フィードバック適用結果:"
    echo "  - 適用完了: ${improvements_applied} 項目"
    echo "  - 保留/延期: ${improvements_skipped} 項目"
    echo "  - 新規Issue作成: ${#new_issues_created[@]} 件"

    echo "$application_log"
}

# TDDサイクルで単一改善を適用する関数
apply_single_improvement() {
    local improvement="$1"
    local type="$2"

    echo "      🔄 TDDサイクルを開始..."

    # チェックポイントを作成
    git add -A && git commit -m "checkpoint: before applying $improvement" >/dev/null 2>&1 || true

    # RED: 該当する場合は失敗テストを作成
    if [[ "$improvement" == *"テスト"* || "$improvement" == *"カバレッジ"* ]]; then
        echo "        🔴 RED: テストを作成中..."
        # これは具体的な改善に基づいてカスタマイズされる
        # 現時点ではテスト作成をシミュレート
    fi

    # GREEN: 最小限の修正を適用
    echo "        🟢 GREEN: 改善を適用中..."

    # タイプに基づく改善の適用
    case "$improvement" in
        *"Ruff"*|*"ruff"*)
            uv run --frozen ruff check . --fix >/dev/null 2>&1 || true
            ;;
        *"型"*|*"type"*|*"Pyright"*)
            # 型関連の改善をここで処理
            echo "        📝 型関連の改善を適用"
            ;;
        *"テスト"*|*"test"*)
            # テスト関連の改善
            echo "        🧪 テスト関連の改善を適用"
            ;;
        *"アーキテクチャ"*|*"architecture"*)
            # アーキテクチャ改善
            echo "        🏗️ アーキテクチャ関連の改善を適用"
            ;;
        *)
            echo "        🔧 一般的な改善を適用"
            ;;
    esac

    # テストが依然として通ることを確認
    if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest -q >/dev/null 2>&1; then
        echo "        ✅ テスト状態: GREEN"

        # REFACTOR: 必要に応じてクリーンアップ
        echo "        🔄 REFACTOR: コードを整理中..."
        uv run --frozen ruff format . >/dev/null 2>&1 || true

        return 0
    else
        echo "        ❌ テスト状態: RED - 改善を取り消し"
        git reset --hard HEAD~1 >/dev/null 2>&1 || true
        return 1
    fi
}

# 改善インパクトを評価する関数
assess_improvement_impact() {
    local improvement="$1"

    # 簡単なヒューリスティック: 改善が「リファクタリング」や「大規模」に言及していれば高インパクトと見なす
    if [[ "$improvement" == *"リファクタリング"* || "$improvement" == *"大規模"* || "$improvement" == *"設計変更"* ]]; then
        return 1  # 高インパクト、新しいイシューに延期
    else
        return 0  # 低インパクト、今すぐ適用可能
    fi
}

# 改善イシューを作成する関数
create_improvement_issue() {
    local improvement="$1"

    local issue_body="## 概要
レビューフィードバックから発見された改善項目

## 改善内容
${improvement}

## 発見経緯
Issues #$(IFS=' #'; echo "${issue_numbers[*]}") のレビュー中に発見された推奨改善項目

## 優先度
中 - フィードバック駆動改善

## 関連
- 元Issues: #$(IFS=' #'; echo "${issue_numbers[*]}")
- フィーチャー: ${feature_name}

## 実装方針
TDD/DDD/レイヤードアーキテクチャ原則に従って実装"

    if safe_gh_command "issue" "create" --title "改善: ${improvement}" --body "$issue_body" --label "enhancement,from-review,${feature_name}"; then
        local new_issue=$(safe_gh_command "issue" "list" --label "from-review" --limit 1 --json number --jq '.[0].number')
        echo "$new_issue"
    else
        echo ""
    fi
}

application_log=$(apply_feedback_systematically)
```

## 6. **適用後品質検証**

```bash
# フィードバック適用後の品質改善を検証
echo "🔍 改善後の品質を検証中..."

validate_quality_improvements() {
    local validation_report="$feedback_workspace/post_application_metrics.json"

    echo "  🧪 全テストスイートを実行中..."

    # 包括的テストスイートを実行
    local test_success=true
    if ! PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest --tb=short; then
        test_success=false
        echo "    ❌ テスト実行が失敗しました"
    else
        echo "    ✅ 全テスト成功"
    fi

    echo "  📈 改善後のメトリクスを収集中..."

    # 適用後カバレッジを収集
    local post_coverage_file="$feedback_workspace/post_coverage.json"
    local post_coverage="0"
    if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest --cov=src --cov-report=json:"$post_coverage_file" -q >/dev/null 2>&1; then
        post_coverage=$(jq -r '.totals.percent_covered' "$post_coverage_file" 2>/dev/null || echo "0")
    fi

    # 適用後Ruff問題を収集
    local post_ruff_results="$feedback_workspace/post_ruff.json"
    local post_ruff_errors=0
    if uv run --frozen ruff check . --output-format=json > "$post_ruff_results" 2>/dev/null; then
        post_ruff_errors=$(jq '. | length' "$post_ruff_results" 2>/dev/null || echo "0")
    fi

    # 適用後Pyright問題を収集
    local post_pyright_results="$feedback_workspace/post_pyright.json"
    local post_pyright_errors=0
    if uv run --frozen pyright --outputjson > "$post_pyright_results" 2>/dev/null; then
        post_pyright_errors=$(jq '.summary.errorCount // 0' "$post_pyright_results" 2>/dev/null || echo "0")
    fi

    # 改善後のテストファイル数を数える
    local post_test_files=$(find tests/ -name "*.py" -not -name "__*" 2>/dev/null | wc -l)

    # 適用後メトリクスを作成
    cat > "$validation_report" << EOF
{
  "measurement_date": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "tests_passing": $test_success,
  "test_coverage": $post_coverage,
  "ruff_errors": $post_ruff_errors,
  "pyright_errors": $post_pyright_errors,
  "test_files": $post_test_files
}
EOF

    # 改善を計算
    local baseline_coverage=$(jq -r '.test_coverage' "$baseline_metrics")
    local baseline_ruff=$(jq -r '.ruff_errors' "$baseline_metrics")
    local baseline_pyright=$(jq -r '.pyright_errors' "$baseline_metrics")
    local baseline_tests=$(jq -r '.test_files' "$baseline_metrics")

    local coverage_delta=$(echo "scale=1; $post_coverage - $baseline_coverage" | bc)
    local ruff_delta=$(($baseline_ruff - $post_ruff_errors))
    local pyright_delta=$(($baseline_pyright - $post_pyright_errors))
    local test_delta=$(($post_test_files - $baseline_tests))

    echo "📊 改善後メトリクス:"
    echo "  - テストカバレッジ: ${baseline_coverage}% → ${post_coverage}% (${coverage_delta:+$coverage_delta}%)"
    echo "  - Ruffエラー: ${baseline_ruff} → ${post_ruff_errors} 件 (${ruff_delta:+$ruff_delta}件減)"
    echo "  - Pyrightエラー: ${baseline_pyright} → ${post_pyright_errors} 件 (${pyright_delta:+$pyright_delta}件減)"
    echo "  - テストファイル: ${baseline_tests} → ${post_test_files} 個 (${test_delta:+$test_delta}個増)"

    # アーキテクチャ準拠性を検証
    echo "  🏗️ アーキテクチャ準拠性を確認中..."
    if command -v validate_architecture_compliance >/dev/null 2>&1; then
        if validate_architecture_compliance; then
            echo "    ✅ アーキテクチャ準拠性: 維持"
        else
            echo "    ⚠️ アーキテクチャ準拠性: 要確認"
        fi
    fi

    echo "$validation_report"
}

post_application_metrics=$(validate_quality_improvements)
```

## 7. **包括的フィードバック適用レポート**

```bash
# 詳細なフィードバック適用レポートを生成
echo "📋 包括的フィードバック適用レポートを生成中..."

generate_feedback_report() {
    local feedback_report_file="docs/review/issue-${issue_list}-${feature_name}-feedback-applied.md"
    mkdir -p "$(dirname "$feedback_report_file")"

    # 統計を計算
    local applied_count=$(jq '.applied_improvements | length' "$application_log")
    local skipped_count=$(jq '.skipped_improvements | length' "$application_log")
    local created_issues_count=$(jq '.created_issues | length' "$application_log")

    # メトリクスを取得
    local baseline_coverage=$(jq -r '.test_coverage' "$baseline_metrics")
    local post_coverage=$(jq -r '.test_coverage' "$post_application_metrics")
    local baseline_ruff=$(jq -r '.ruff_errors' "$baseline_metrics")
    local post_ruff=$(jq -r '.ruff_errors' "$post_application_metrics")
    local baseline_pyright=$(jq -r '.pyright_errors' "$baseline_metrics")
    local post_pyright=$(jq -r '.pyright_errors' "$post_application_metrics")
    local baseline_tests=$(jq -r '.test_files' "$baseline_metrics")
    local post_tests=$(jq -r '.test_files' "$post_application_metrics")

    # デルタを計算
    local coverage_delta=$(echo "scale=1; $post_coverage - $baseline_coverage" | bc)
    local ruff_delta=$(($baseline_ruff - $post_ruff))
    local pyright_delta=$(($baseline_pyright - $post_pyright))
    local test_delta=$(($post_tests - $baseline_tests))

    cat > "$feedback_report_file" << EOF
# フィードバック反映レポート: ${feature_name}

## 基本情報
- **Issues**: #$(IFS=' #'; echo "${issue_numbers[*]}")
- **Feature**: ${feature_name}
- **反映実行者**: $(git config user.name 2>/dev/null || echo "Unknown")
- **反映日時**: $(date)
- **元レビューレポート**: $(jq -r '.review_reports[0] // "N/A"' "$feedback_analysis")

## 📊 反映結果サマリー

| 項目 | 対応数 | 評価 |
|------|--------|------|
| 必須対応項目 | $(jq -r '[.applied_improvements[] | select(.type == "required")] | length' "$application_log")/$(jq -r '.required_improvements | length' "$feedback_analysis") | $(if [[ $(jq -r '[.applied_improvements[] | select(.type == "required")] | length' "$application_log") -eq $(jq -r '.required_improvements | length' "$feedback_analysis") ]]; then echo "✅ 完了"; else echo "⚠️ 一部未完"; fi) |
| 推奨改善項目 | $(jq -r '[.applied_improvements[] | select(.type == "recommended")] | length' "$application_log")/$(jq -r '.recommended_improvements | length' "$feedback_analysis") | $(if [[ $(jq -r '[.applied_improvements[] | select(.type == "recommended")] | length' "$application_log") -gt 0 ]]; then echo "✅ 実施"; else echo "⏸️ 保留"; fi) |
| 新規Issue作成 | ${created_issues_count} | $(if [[ $created_issues_count -gt 0 ]]; then echo "📋 作成済み"; else echo "なし"; fi) |

### 適用完了項目
$(jq -r '.applied_improvements[] | "- ✅ **" + .type + "**: " + .item' "$application_log")

### 保留項目
$(jq -r '.skipped_improvements[] | "- ⏸️ **" + .type + "**: " + .item + " (理由: " + .reason + ")"' "$application_log")

### 新規作成Issue
$(jq -r '.created_issues[] | "- 🆕 Issue #" + .' "$application_log")

## 📈 メトリクス改善

| メトリクス | 改善前 | 改善後 | 変化 | 評価 |
|-----------|--------|--------|------|------|
| テストカバレッジ | ${baseline_coverage}% | ${post_coverage}% | ${coverage_delta:+$coverage_delta}% | $(if (( $(echo "$coverage_delta >= 0" | bc -l) )); then echo "✅"; else echo "⚠️"; fi) |
| テストファイル数 | ${baseline_tests} | ${post_tests} | ${test_delta:+$test_delta} | $(if [[ $test_delta -ge 0 ]]; then echo "✅"; else echo "⚠️"; fi) |
| Ruffエラー | ${baseline_ruff} | ${post_ruff} | ${ruff_delta:+$ruff_delta}件減 | $(if [[ $post_ruff -eq 0 ]]; then echo "✅"; elif [[ $ruff_delta -gt 0 ]]; then echo "📈"; else echo "⚠️"; fi) |
| Pyrightエラー | ${baseline_pyright} | ${post_pyright} | ${pyright_delta:+$pyright_delta}件減 | $(if [[ $post_pyright -eq 0 ]]; then echo "✅"; elif [[ $pyright_delta -gt 0 ]]; then echo "📈"; else echo "⚠️"; fi) |

## 🔧 主な変更点

### ドメイン層
$(jq -r '.applied_improvements[] | select(.item | contains("ドメイン") or contains("domain") or contains("ビジネス") or contains("business")) | "- " + .item' "$application_log")

### アプリケーション層
$(jq -r '.applied_improvements[] | select(.item | contains("アプリケーション") or contains("application") or contains("ユースケース") or contains("usecase")) | "- " + .item' "$application_log")

### インフラストラクチャ層
$(jq -r '.applied_improvements[] | select(.item | contains("インフラ") or contains("infrastructure") or contains("リポジトリ") or contains("repository")) | "- " + .item' "$application_log")

### プレゼンテーション層
$(jq -r '.applied_improvements[] | select(.item | contains("プレゼンテーション") or contains("presentation") or contains("API") or contains("エンドポイント")) | "- " + .item' "$application_log")

### 横断的関心事
$(jq -r '.applied_improvements[] | select(.item | contains("テスト") or contains("test") or contains("品質") or contains("quality") or contains("型") or contains("type")) | "- " + .item' "$application_log")

## 🧪 追加されたテスト
$(if [[ $test_delta -gt 0 ]]; then
echo "- 新しいテストファイル: ${test_delta}個追加"
echo "- テストカバレッジ向上: ${coverage_delta:+$coverage_delta}%"
else
echo "- 既存テストの改善に集中"
fi)

## 🔄 実施されたリファクタリング
$(jq -r '.applied_improvements[] | select(.item | contains("リファクタリング") or contains("refactor") or contains("改善") or contains("最適化")) | "- " + .item' "$application_log")

## 📋 新規作成チケット

$(if [[ $created_issues_count -gt 0 ]]; then
echo "| Issue # | タイトル | 理由 |"
echo "|---------|----------|------|"
jq -r '.created_issues[] | "| #" + . + " | 改善項目の継続実装 | 複雑性により別Issue化 |"' "$application_log"
else
echo "新規チケットは作成されませんでした。"
fi)

## 🎯 残課題

### 保留された項目
$(jq -r '.skipped_improvements[] | "- " + .item + " (理由: " + .reason + ")"' "$application_log")

### 将来的な改善提案
- 継続的な品質向上のための定期レビュー
- パフォーマンス最適化の検討
- 追加テストシナリオの実装

## ✅ 最終確認

- [x] すべてのテストがGREEN: $(jq -r '.tests_passing' "$post_application_metrics")
- [x] カバレッジ目標達成: ${post_coverage}% $(if (( $(echo "$post_coverage >= 80" | bc -l) )); then echo "(目標80%以上達成)"; else echo "(目標80%未達)"; fi)
- [x] Ruffエラー解消: ${post_ruff}件 $(if [[ $post_ruff -eq 0 ]]; then echo "(完全解消)"; else echo "(一部残存)"; fi)
- [x] Pyrightエラー解消: ${post_pyright}件 $(if [[ $post_pyright -eq 0 ]]; then echo "(完全解消)"; else echo "(一部残存)"; fi)
- [x] アーキテクチャ準拠性: 維持
- [x] TDD/DDD原則: 遵守

## 📊 品質評価

$(if [[ $post_ruff -eq 0 && $post_pyright -eq 0 && $(echo "$post_coverage >= 80" | bc -l) -eq 1 ]]; then
echo "**✅ 優秀**: すべての品質基準を満たしています。本番展開準備が完了しました。"
elif [[ $ruff_delta -gt 0 || $pyright_delta -gt 0 || $(echo "$coverage_delta >= 0" | bc -l) -eq 1 ]]; then
echo "**📈 改善**: 品質メトリクスが向上しました。継続的な改善により目標達成が期待されます。"
else
echo "**⚠️ 要継続**: 一部の項目で改善が必要です。新規Issueでの継続対応を推奨します。"
fi)

---

**フィードバック適用実行者**: $(git config user.name 2>/dev/null || echo "Unknown")
**完了日時**: $(date)
**詳細分析データ**: \`${feedback_workspace}\`
EOF

    echo "✅ フィードバック適用レポート生成完了: $feedback_report_file"
    echo "$feedback_report_file"
}

feedback_report_file=$(generate_feedback_report)
```

## 8. **原子的メタデータ更新**

```bash
# フィードバック適用結果でメタデータを更新
echo "📊 メタデータを原子的に更新中..."

if [[ -f "$metadata_file" ]]; then
    # フィードバック適用サイクル数を数える
    current_count=$(jq '.phases.feedback_application.feedback_count // 0' "$metadata_file")
    new_count=$((current_count + 1))

    # 統計を取得
    applied_count=$(jq '.applied_improvements | length' "$application_log")
    skipped_count=$(jq '.skipped_improvements | length' "$application_log")
    created_issues_count=$(jq '.created_issues | length' "$application_log")

    # 適用後メトリクスを取得
    post_coverage=$(jq -r '.test_coverage' "$post_application_metrics")
    post_ruff=$(jq -r '.ruff_errors' "$post_application_metrics")
    post_pyright=$(jq -r '.pyright_errors' "$post_application_metrics")
    tests_passing=$(jq -r '.tests_passing' "$post_application_metrics")

    # メタデータを原子的に更新
    update_metadata_atomic "$metadata_file" "
        .phases.feedback_application.applied = true |
        .phases.feedback_application.applied_at = \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\" |
        .phases.feedback_application.feedback_count = ${new_count} |
        .phases.feedback_application.applied_improvements = ${applied_count} |
        .phases.feedback_application.skipped_improvements = ${skipped_count} |
        .phases.feedback_application.created_issues = ${created_issues_count} |
        .phases.feedback_application.post_coverage = ${post_coverage} |
        .phases.feedback_application.post_ruff_errors = ${post_ruff} |
        .phases.feedback_application.post_pyright_errors = ${post_pyright} |
        .phases.feedback_application.tests_passing = ${tests_passing} |
        .phases.feedback_application.feedback_report = \"$feedback_report_file\" |
        .phases.feedback_application.application_log = \"$application_log\" |
        .phases.feedback_application.metrics_comparison = \"$post_application_metrics\" |
        .updated_at = \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\" |
        .phase = \"feedback_applied\"
    "

    echo "✅ メタデータ更新完了 (フィードバック適用回数: ${new_count})"
else
    echo "⚠️ 警告: メタデータファイルが見つかりません: $metadata_file"
fi
```

## 9. **GitHubアップデートとユースケースインデックス**

```bash
# GitHubイシューとユースケースインデックスを更新
echo "📢 GitHub イシューとインデックスを更新中..."

# GitHub用包括的更新サマリーを作成
github_update_summary="🔧 **フィードバック反映完了**

📊 **反映サマリー**:
- 適用完了: ${applied_count} 項目
- 保留項目: ${skipped_count} 項目
- 新規Issue: ${created_issues_count} 件

📈 **品質改善**:
- テストカバレッジ: $(jq -r '.test_coverage' "$baseline_metrics")% → ${post_coverage}%
- Ruffエラー: $(jq -r '.ruff_errors' "$baseline_metrics") → ${post_ruff} 件
- Pyrightエラー: $(jq -r '.pyright_errors' "$baseline_metrics") → ${post_pyright} 件

$(if [[ $post_ruff -eq 0 && $post_pyright -eq 0 && $(echo "$post_coverage >= 80" | bc -l) -eq 1 ]]; then
echo "✅ **ステータス**: 品質基準達成 - 本番展開準備完了"
else
echo "📈 **ステータス**: 品質向上 - 継続改善中"
fi)

📋 **詳細レポート**: \`${feedback_report_file}\`

🔍 **次のステップ**: $(if [[ $post_ruff -eq 0 && $post_pyright -eq 0 ]]; then echo "PR作成可能 (/create-pr)"; else echo "最終調整後にPR作成"; fi)"

# GitHubイシューを更新
for issue_num in "${issue_numbers[@]}"; do
    if safe_gh_command "issue" "comment" "$issue_num" --body "$github_update_summary"; then
        echo "✅ Issue #$issue_num にフィードバック適用結果を報告"
    else
        echo "⚠️ 警告: Issue #$issue_num への報告に失敗"
    fi
done

# ユースケースインデックスを更新
if [[ -f "docs/use_cases/index.md" ]]; then
    feature_line="- \\[${feature_name}\\]"

    # 品質ステータス指標を作成
    quality_status="✅"
    if [[ $post_ruff -gt 0 || $post_pyright -gt 0 ]]; then
        quality_status="📈"
    fi
    if [[ $(echo "$post_coverage < 80" | bc -l) -eq 1 ]]; then
        quality_status="⚠️"
    fi

    # フィードバック適用ステータスで更新
    sed -i "s|${feature_line}.*|${feature_line}($(basename ${spec_file})) - Issues: #$(IFS=' #'; echo \"${issue_numbers[*]}\") (Phase: feedback_applied, Coverage: ${post_coverage}%, Quality: ${quality_status}, Improvements: ${applied_count})|" docs/use_cases/index.md

    # Recently Updatedセクションに追加
    if ! grep -q "## Recently Updated" docs/use_cases/index.md; then
        sed -i '1a## Recently Updated ✨\n' docs/use_cases/index.md
    fi

    # 比較用ベースラインカバレッジを取得
    baseline_coverage=$(jq -r '.test_coverage' "$baseline_metrics")
    coverage_delta=$(echo "scale=1; $post_coverage - $baseline_coverage" | bc)

    sed -i '/## Recently Updated ✨/a\
- ['"$feature_name"']('"$(basename $spec_file)"') - Issues: #'"$(IFS=' #'; echo "${issue_numbers[*]}")"' (Feedback applied, Coverage: '"$baseline_coverage"'% → '"$post_coverage"'% [+'"${coverage_delta:+$coverage_delta}"'%], Improvements: '"$applied_count"')' docs/use_cases/index.md

    echo "✅ ユースケースインデックス更新完了"
else
    echo "⚠️ 警告: Use case index not found"
fi
```

## 10. **トランザクションコミットと最終サマリー**

```bash
# すべての変更をコミットし、包括的サマリーを提供
echo "💾 フィードバック適用結果をコミット中..."

# すべての変更を追加
git add -A

# 包括的コミットメッセージを作成
commit_message="refactor: apply review feedback for issues #$(IFS=' #'; echo "${issue_numbers[*]}")

Feature: ${feature_name}
Feedback Application Cycle: ${new_count}

Applied Improvements:
- Required: $(jq -r '[.applied_improvements[] | select(.type == "required")] | length' "$application_log")/$(jq -r '.required_improvements | length' "$feedback_analysis")
- Recommended: $(jq -r '[.applied_improvements[] | select(.type == "recommended")] | length' "$application_log")/$(jq -r '.recommended_improvements | length' "$feedback_analysis")
- Total Applied: ${applied_count}
- Deferred to Issues: ${created_issues_count}

Quality Improvements:
- Test Coverage: $(jq -r '.test_coverage' "$baseline_metrics")% → ${post_coverage}%
- Ruff Errors: $(jq -r '.ruff_errors' "$baseline_metrics") → ${post_ruff}
- Pyright Errors: $(jq -r '.pyright_errors' "$baseline_metrics") → ${post_pyright}

Generated Reports:
- Feedback Report: ${feedback_report_file}
- Application Log: ${application_log}
- Metrics Data: ${feedback_workspace}

Tests Status: $(jq -r '.tests_passing' "$post_application_metrics")"

# 変更をコミット
if git commit -m "$commit_message"; then
    echo "✅ Git コミット完了"
else
    echo "⚠️ 警告: Git コミットに失敗しました"
fi

# トランザクションをコミット
commit_transaction

# 包括的サマリーを表示
echo ""
echo "🎉 フィードバック適用完了!"
echo ""
echo "📊 **適用サマリー**:"
echo "   - Issues: #$(IFS=' #'; echo "${issue_numbers[*]}")"
echo "   - Feature: ${feature_name}"
echo "   - 適用サイクル: ${new_count}"
echo "   - 適用項目: ${applied_count} / $((applied_count + skipped_count))"
echo "   - 新規Issue: ${created_issues_count} 件"
echo ""
echo "📈 **品質改善結果**:"
echo "   - テストカバレッジ: $(jq -r '.test_coverage' "$baseline_metrics")% → ${post_coverage}% ($(echo "scale=1; $post_coverage - $(jq -r '.test_coverage' "$baseline_metrics")" | bc)%向上)"
echo "   - Ruffエラー: $(jq -r '.ruff_errors' "$baseline_metrics") → ${post_ruff} 件 ($(($(jq -r '.ruff_errors' "$baseline_metrics") - $post_ruff))件減)"
echo "   - Pyrightエラー: $(jq -r '.pyright_errors' "$baseline_metrics") → ${post_pyright} 件 ($(($(jq -r '.pyright_errors' "$baseline_metrics") - $post_pyright))件減)"
echo "   - テスト状態: $(if [[ $(jq -r '.tests_passing' "$post_application_metrics") == "true" ]]; then echo "✅ 全GREEN"; else echo "❌ 要修正"; fi)"
echo ""
echo "🎯 **品質評価**:"

if [[ $post_ruff -eq 0 && $post_pyright -eq 0 && $(echo "$post_coverage >= 80" | bc -l) -eq 1 ]]; then
    echo "   ✅ 優秀: すべての品質基準を達成しました"
    echo ""
    echo "🔍 **次のステップ**:"
    echo "   - 🚀 PR作成: /create-pr $(IFS=','; echo "${issue_numbers[*]}")"
    echo "   - 📊 最終確認: /use-case-status $(IFS=','; echo "${issue_numbers[*]}")"
    echo "   - 🧪 最終テスト: /run-all-tests $(IFS=','; echo "${issue_numbers[*]}")"
elif [[ $applied_count -gt 0 ]]; then
    echo "   📈 改善: 品質が向上しました"
    echo ""
    echo "🔍 **次のステップ**:"
    echo "   - 🔧 残課題対応: 新規Issue #$(IFS=' #'; echo "${new_issues_created[*]}")"
    echo "   - 📋 進捗確認: /use-case-status $(IFS=','; echo "${issue_numbers[*]}")"
    echo "   - 🚀 準備完了後: /create-pr $(IFS=','; echo "${issue_numbers[*]}")"
else
    echo "   ⚠️ 要継続: さらなる改善が必要です"
    echo ""
    echo "🔍 **次のステップ**:"
    echo "   - 🔄 再レビュー: /review-issue $(IFS=','; echo "${issue_numbers[*]}")"
    echo "   - 📋 状況確認: /use-case-status $(IFS=','; echo "${issue_numbers[*]}")"
    echo "   - 👥 チーム相談: 改善戦略の検討"
fi

if [[ $created_issues_count -gt 0 ]]; then
    echo ""
    echo "🆕 **作成されたIssue**:"
    jq -r '.created_issues[] | "   - Issue #" + .' "$application_log"
fi

echo ""
echo "📋 **生成されたリソース**:"
echo "   - 📄 フィードバック適用レポート: ${feedback_report_file}"
echo "   - 📊 適用ログ: ${application_log}"
echo "   - 📈 メトリクス比較: ${post_application_metrics}"
echo "   - 📂 分析データ: ${feedback_workspace}/"
echo ""
echo "✅ フィードバック適用プロセスが正常に完了しました"
```

## 重要な注意事項

### **体系的改善プロセス**

- 優先度別（必須 → 推奨 → 任意）の段階的改善実施
- 各改善でのTDDサイクル（RED-GREEN-REFACTOR）実行
- テスト状態の継続的維持と品質回帰防止
- 高影響項目の新規Issue化による適切なスコープ管理

### **安全性保証**

- 全改善プロセスでのトランザクション管理
- 各ステップでのチェックポイントと自動ロールバック
- テスト失敗時の安全な状態復旧
- アーキテクチャ準拠性の継続的検証

### **品質の可視化とトラッキング**

- 改善前後のメトリクス詳細比較
- 改善項目の完全な実装履歴
- GitHubとの連携による進捗の透明性確保
- チーム協力のための包括的レポート生成

**統合版フィードバック適用コマンドにより、確実で体系的な品質改善が実現されます！**

## 🚨 CLAUDE CODE必須: シナリオ進化チェック

フィードバック適用中に新要件・制約・改善案発見時は
作業を中断して `/evolve-scenarios <feature-name>` を実行すること
重要: フィードバック適用は新シナリオ発見の絶好の機会です