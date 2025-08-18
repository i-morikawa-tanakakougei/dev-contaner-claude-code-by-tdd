# ユースケース開発状況と進捗の表示（包括的分析とインテリジェント推奨機能付き）

## メタデータ
- **前提条件**: ユースケース開発が進行中または完了
- **入力**: イシュー番号（オプション - 指定されない場合はすべて表示）
- **出力**: 
  - 包括的ステータスレポート
  - 進捗分析とメトリクス
  - 開発推奨事項
- **依存関係**: メタデータファイル、Git履歴、実装ファイル
- **実行タイミング**: 開発中いつでも進捗監視のため

## 🎯 **TDD/DDD/LAYERED プロセス コンテキスト**

**🔄 コアワークフロー**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 アーキテクチャ**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 開発**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ 設計**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 要件**: Given-When-Then シナリオと完全な追跡可能性  
**🔄 進化**: /evolve-scenarios コマンドによる継続的シナリオ進化

> 📖 **ドキュメント管理システム**: [README.md](./README.md)  
> 🗺️ **現在位置**: 進捗追跡 - 開発状況チェック (16/16)  
> 🎯 **段階目的**: 開発進捗の可視化と次のアクション提案  
> 🔄 **実行タイミング**: どのフェーズからでも実行可能  
> 📊 **機能**: メタデータ分析、視覚的進捗表示、次ステップガイダンス
>
> **📋 3層アーキテクチャ操作**:
>
> - 🎯 **戦略**: `docs/use_cases/core/index.md` (プロジェクト概要の読み取り)
> - 📊 **戦術**: `docs/use_cases/index.md` (実装状況の表示)
> - 🔧 **実行**: `docs/use_cases/issue-X-Y.json` (詳細進捗の分析)

## 📊 **ステータス報告: 分析のみ**

**⚠️ 重要な注意:**
- **この段階はステータス報告のみ** - 進捗を表示し現在の状態を分析
- **実装なし** - ステータス読み取りと報告に集中  
- **進捗可視化** - 全フェーズでの開発進捗を表示
- **次アクション推奨** - 最適な次ステップの提案

**ステータスチェック機能:**
- ✅ メタデータファイルの読み取りと分析
- ✅ 視覚的進捗インジケーターの表示
- ✅ 完了パーセンテージの表示
- ✅ 次のアクション推奨
- ✅ ボトルネックと問題の特定
- ❌ 実装変更は行わない
- ❌ ファイルの変更は行わない

## 📋 **プロジェクト状況分析タスクチェックリスト**

**包括的プロジェクト状況可視化と分析にこのチェックリストを使用:**

### 🔴 必須タスク

#### **📊 メタデータ発見と分析**
- [ ] **プロジェクト構造スキャン**: docs/use_cases/ 内のすべてのissue-X-Y.jsonメタデータファイルを発見
- [ ] **メタデータファイル解析**: 各メタデータファイルから進捗情報を抽出
- [ ] **メタデータ整合性検証**: 破損または不完全なメタデータファイルをチェック
- [ ] **プロジェクトデータ集約**: すべてのイシューとフィーチャーからデータを統合

#### **🎯 フィーチャーとイシュー進捗分析**
- [ ] **完了パーセンテージ計算**: 各フィーチャー/イシューの完了率を決定
- [ ] **フェーズ分布分析**: 各開発フェーズにあるイシューの数を表示
- [ ] **ブロック項目特定**: 停滞または進捗していないイシューを発見
- [ ] **ベロシティメトリクス追跡**: 開発ベロシティとトレンド分析を計算

#### **📈 進捗可視化作成**
- [ ] **進捗ダッシュボード作成**: プロジェクト全体進捗の視覚的表現を生成
- [ ] **フィーチャーステータスマトリクス構築**: 全開発フェーズでの各フィーチャーステータスを表示

### 🟡 推奨タスク

#### **🏗️ アーキテクチャと品質メトリクス**
- [ ] **レイヤー実装分析**: ドメイン/アプリケーション/インフラ/プレゼンテーション層の完了状況を表示
- [ ] **アーキテクチャ準拠チェック**: TDD/DDD/Clean Architecture原則への準拠を確認
- [ ] **テストカバレッジレビュー**: 実装済みフィーチャー全体でのテストカバレッジを集約
- [ ] **コード品質評価**: プロジェクト全体の品質メトリクスとトレンドを表示
- [ ] **Given-When-Thenカバレッジ検証**: シナリオ実装完全性をチェック
- [ ] **ドキュメントカバレッジレビュー**: ドキュメント完全性と品質を評価

### 🟢 オプションタスク

#### **🔍 高度分析**
- [ ] **データ不整合特定**: 不正確または古いメタデータを標示
- [ ] **イシュー関係性マッピング**: イシュー間の依存関係と関連性を理解
- [ ] **スコープ変更評価**: 要件が進化または変更されたフィーチャーを特定
- [ ] **実装カバレッジマッピング**: システムの実装済み部分を表示
- [ ] **完了タイムライン生成**: 現在のベロシティに基づく完了予定日を表示
- [ ] **品質メトリクスチャート作成**: テストカバレッジ、コード品質、パフォーマンストレンドを可視化
- [ ] **ボトルネック分析表示**: 遅延を引き起こしているフェーズやフィーチャーを特定
- [ ] **スプリント進捗表示**: 現在のスプリントステータスと今後の作業を表示

### **🚀 次アクション推奨**
- [ ] **緊急優先事項特定**: 最も重要な次ステップを推奨
- [ ] **最適コマンドシーケンス提案**: 次のアクション用の具体的コマンドを提供
- [ ] **緊急イシューフラグ**: 即座の注意が必要なイシューをハイライト
- [ ] **リソース配分推奨**: 開発努力を集中すべき場所を提案
- [ ] **クイックウィン特定**: 短時間で完了できるフィーチャーを指摘
- [ ] **リファクタリング機会提案**: 改善の恩恵を受ける領域を推奨

### **🎯 ステークホルダーコミュニケーション準備**
- [ ] **エグゼクティブサマリー作成**: ステークホルダー向け高レベル進捗サマリーを生成
- [ ] **ビジネス価値レポート準備**: 提供されたビジネス価値と今後の成果物を表示
- [ ] **リスク評価生成**: プロジェクトリスクと軽減戦略を特定し伝達
- [ ] **タイムライン予測作成**: 残り作業に対する現実的な完了見積もりを提供
- [ ] **フィーチャーデモ準備**: デモンストレーション準備完了のフィーチャーを特定
- [ ] **マイルストーン達成文書化**: 達成した主要マイルストーンと今後の予定をハイライト

### **🔍 品質と健全性評価**
- [ ] **プロジェクト健全性評価**: プロジェクト全体の健全性と持続可能性を評価
- [ ] **技術的債務チェック**: 注意が必要な技術的債務領域を特定
- [ ] **チームベロシティレビュー**: チーム生産性と能力を分析
- [ ] **プロセス効果性評価**: TDD/DDDプロセスの効果性を評価
- [ ] **ドキュメント健全性チェック**: ドキュメントが最新で包括的であることを確認
- [ ] **保守性評価**: コードベースの長期保守性を評価

### **🔄 プロセスとワークフロー分析**
- [ ] **コマンド使用パターン分析**: 最も頻繁に使用されるコマンドを表示
- [ ] **プロセスボトルネック特定**: ワークフローで遅延を引き起こすステップを発見
- [ ] **フィードバックサイクルレビュー**: レビューとフィードバックプロセスの効果性を評価
- [ ] **シナリオ進化パターンチェック**: 開発中の要件進化を分析
- [ ] **テスト効果性評価**: テスト品質とカバレッジトレンドを評価
- [ ] **統合パターンレビュー**: クロスフィーチャー統合課題を分析

### **📊 パフォーマンスとスケーラビリティ洞察**
- [ ] **システムパフォーマンス分析**: 実装済みフィーチャー全体でパフォーマンスメトリクスをレビュー
- [ ] **スケーラビリティ準備チェック**: スケーリング準備状況を評価
- [ ] **リソース使用率レビュー**: システムリソース使用パターンを分析
- [ ] **最適化機会特定**: パフォーマンス改善可能領域を発見
- [ ] **統合パフォーマンスチェック**: クロスシステム統合のパフォーマンスを評価
- [ ] **負荷処理検証**: 様々な負荷条件下でのシステム動作をレビュー

### **🎨 カスタマイズ可能レポートオプション**
- [ ] **詳細レポート生成**: 異なる読者向けの包括的レポートを作成
- [ ] **サマリーダッシュボード作成**: 高レベル概要ダッシュボードを生成
- [ ] **ドリルダウン機能提供**: 特定領域の詳細探索を可能にする
- [ ] **進捗データエクスポート**: 外部レポートツール用データエクスポートを有効化
- [ ] **履歴比較作成**: 時系列での進捗トレンドを表示
- [ ] **実行可能洞察生成**: 具体的で実行可能な推奨事項を提供

### **🔮 予測分析と計画**
- [ ] **プロジェクト完了予測**: 現在のトレンドに基づくプロジェクト完了予測
- [ ] **リソース計画推奨**: 最適進捗のためのリソース配分提案
- [ ] **リスク軽減計画**: 潜在リスクを特定し軽減戦略を提案
- [ ] **能力計画分析**: チーム能力と作業負荷分散を評価
- [ ] **依存関係インパクト分析**: 一つの領域の遅延が他領域に与える影響を表示
- [ ] **品質トレンド予測**: 現在のトレンドに基づく品質メトリクス予測

### **📚 ステータス文書化とコミュニケーション**
- [ ] **ステータスレポート生成**: 包括的ステータス文書を作成
- [ ] **チームコミュニケーション準備**: 開発チーム向けステータス更新をドラフト
- [ ] **ステークホルダーブリーフィング作成**: エグゼクティブレベルステータスプレゼンテーションを準備
- [ ] **推奨事項文書化**: すべての推奨事項とその根拠を記録
- [ ] **ステータススナップショットアーカイブ**: 履歴追跡用ステータス情報を保存
- [ ] **フォローアップアクション準備**: 具体的な次ステップと責任を文書化

**💡 プロヒント: このステータス分析を定期的に使用してプロジェクトの可視性を維持し、優先度とリソース配分についてデータ駆動の意思決定を行いましょう！

**マルチフェーズ使用:**
- 任意の開発フェーズから実行可能
- リアルタイム進捗可視性を提供
- TDD/DDDサイクル完了の追跡を支援
- プロジェクト管理の意思決定をサポート

**ステータス報告のみ - 変更なし。**

## 🛡️ **統合版の主な改善点**

### **✅ 解決された問題**

- **進捗可視化の不備**: 多層的・時系列進捗分析とリアルタイム更新
- **次アクション不明確**: AIベース推奨とコンテキスト依存提案
- **品質状況不透明**: 包括的品質メトリクスとトレンド分析
- **チーム連携不足**: GitHub連携とステークホルダー向け報告
- **問題早期発見の欠如**: 予測的問題検出とアラート機能

### **🆕 新機能**

1. **🧠 インテリジェント分析**: AIベースの進捗パターン分析と予測
2. **📊 多次元可視化**: 時系列・品質・リスク・効率性の統合ダッシュボード
3. **🔍 予測アラート**: 潜在的ブロッカーと期限遅延の早期警告
4. **🤝 チーム連携強化**: ステークホルダー別カスタマイズ報告
5. **📈 パフォーマンス最適化**: 開発効率とボトルネック分析

## よくあるエラーと解決方法

### ❌ エラーケース1: ユースケースが見つからない
**原因**: ユースケース作成前にステータスチェックを試行  
**解決方法**: 最初に `/create-use-case <issue-number>` でユースケースを作成

### ❌ エラーケース2: メタデータファイルが破損
**原因**: JSONメタデータファイルが無効な形式  
**解決方法**: JSONファイルを検証・修正するか、ユースケースコマンドで再生成

### ❌ エラーケース3: Git履歴が不完全
**原因**: ステータス分析には正確な報告のためGit履歴が必要  
**解決方法**: Gitリポジトリが適切に初期化されコミットが存在することを確認

## 実行例

### ✅ 成功例
```bash
$ /use-case-status 15
📊 Issues: #15 のステータス分析を開始します
📊 メタデータ分析中...
✅ ユースケース仕様: 完了
✅ ドメインモデル: 完了
✅ TDDテスト: 完了
✅ 全層実装: 完了
✅ リファクタリング: 完了
📊 進捗率: 95% (PR作成準備完了)
🎉 ステータス分析完了!
```

### ❌ 失敗例と修正
```bash
$ /use-case-status 999
❌ Issue #999 のメタデータが見つかりません
💡 有効なイシュー番号を指定してください

# 修正: 有効なイシュー番号を使用するか、すべてを確認する場合は引数なし
$ /use-case-status
```

## タスク詳細

## 1. **安全環境のセットアップと引数解析**

```bash
# 🔧 自動引数解析と検証を含む安全な操作関数をロード
source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "16-use-case-status" "$ARGUMENTS"

# 引数はセットアップスクリプトによって既に解析・検証済み
# このコマンド固有の追加検証
if [[ ${#issue_numbers[@]} -ne 1 ]]; then
    echo "エラー: イシュー番号を1つだけ指定してください（複数イシューの場合は個別に実行）"
    show_usage_example "use-case-status" "1" "イシュー1の進捗確認"
    show_usage_example "use-case-status" "7" "イシュー7の進捗確認"
    exit 1
fi
```

## 2. **包括的メタデータ発見と検証**

```bash
# 高度検索でメタデータを発見・検証
echo "🔍 メタデータとプロジェクト情報を収集中..."

status_workspace="$(mktemp -d -t status_workspace_XXXXXX)"
cleanup() { rm -rf "$status_workspace" 2>/dev/null || true; }
trap cleanup EXIT

discover_project_metadata() {
    local discovery_report="$status_workspace/discovery_report.json"

    # 発見レポートを初期化
    cat > "$discovery_report" << EOF
{
  "discovery_date": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "requested_issues": [$(IFS=','; echo "\"${issue_numbers[*]}\"")],
  "discovered_features": [],
  "metadata_files": [],
  "related_documents": [],
  "github_status": {}
}
EOF

    issue_list=$(IFS=-; echo "${issue_numbers[*]}")

    # 明示的フィーチャー名を最初に試行
    if [[ ${#other_args[@]} -gt 0 ]]; then
        feature_name="${other_args[0]}"
        metadata_file="docs/use_cases/issue-${issue_list}-${feature_name}.json"
        echo "🎯 指定フィーチャー: $feature_name"
    else
        # イシューパターンに一致するメタデータファイルを検索
        echo "  🔍 イシューパターンに基づくメタデータ検索中..."
        local found_files=()
        mapfile -t found_files < <(find docs/use_cases -name "issue-${issue_list}-*.json" 2>/dev/null)

        if [[ ${#found_files[@]} -eq 0 ]]; then
            # 個別イシュー検索を試行
            echo "  🔄 個別イシューでの検索中..."
            for issue_num in "${issue_numbers[@]}"; do
                mapfile -t -O ${#found_files[@]} found_files < <(find docs/use_cases -name "issue-*${issue_num}*.json" 2>/dev/null)
            done
        fi

        if [[ ${#found_files[@]} -eq 0 ]]; then
            echo "❌ エラー: 指定されたイシューに関連するメタデータファイルが見つかりません"
            echo "💡 ヒント: まず /create-use-case コマンドでユースケースを作成してください"
            echo "💡 使用可能なコマンド:"
            echo "   /create-use-case $(IFS=','; echo "${issue_numbers[*]}"),<feature-name>"
            exit 1
        elif [[ ${#found_files[@]} -eq 1 ]]; then
            metadata_file="${found_files[0]}"
            feature_name=$(basename "$metadata_file" .json | sed 's/issue-[0-9-]*-//')
            echo "✅ メタデータファイル発見: $metadata_file"
        else
            echo "📋 複数のフィーチャーが見つかりました:"
            for i in "${!found_files[@]}"; do
                local file="${found_files[$i]}"
                local fname=$(basename "$file" .json | sed 's/issue-[0-9-]*-//')
                echo "  $((i+1)). $fname ($(basename "$file"))"
            done
            echo "💡 具体的なフィーチャー名を指定してください:"
            echo "   /use-case-status $(IFS=','; echo "${issue_numbers[*]}"),<feature-name>"
            exit 1
        fi
    fi

    # メタデータファイルが存在することを検証
    if [[ ! -f "$metadata_file" ]]; then
        echo "❌ エラー: メタデータファイルが見つかりません: $metadata_file"
        echo "💡 確認事項:"
        echo "   - フィーチャー名のスペルが正しいか"
        echo "   - /create-use-case コマンドが実行済みか"
        echo "   - docs/use_cases/ ディレクトリに *.json ファイルがあるか"
        exit 1
    fi

    # 発見レポートを更新
    jq --arg metadata "$metadata_file" --arg feature "$feature_name" \
       '.metadata_files += [$metadata] | .discovered_features += [$feature]' \
       "$discovery_report" > "${discovery_report}.tmp" && mv "${discovery_report}.tmp" "$discovery_report"

    echo "✅ プロジェクト情報収集完了: $feature_name"
    echo "$discovery_report"
}

discovery_report=$(discover_project_metadata)
metadata_file=$(jq -r '.metadata_files[0]' "$discovery_report")
feature_name=$(jq -r '.discovered_features[0]' "$discovery_report")
```

## 3. **高度メタデータ分析**

```bash
# 包括的メタデータ分析を実行
echo "📊 メタデータを詳細分析中..."

analyze_metadata_comprehensive() {
    local analysis_report="$status_workspace/metadata_analysis.json"

    echo "  📋 基本情報を抽出中..."

    # 基本情報を抽出
    local created_at=$(jq -r '.created_at // "Unknown"' "$metadata_file")
    local updated_at=$(jq -r '.updated_at // "Unknown"' "$metadata_file")
    local current_phase=$(jq -r '.phase // "unknown"' "$metadata_file")
    local issue_array=$(jq -c '.issues // []' "$metadata_file")

    # 分析を初期化
    cat > "$analysis_report" << EOF
{
  "analysis_date": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "feature": "$feature_name",
  "metadata_file": "$metadata_file",
  "basic_info": {
    "created_at": "$created_at",
    "updated_at": "$updated_at",
    "current_phase": "$current_phase",
    "issues": $issue_array
  },
  "phase_analysis": {},
  "file_inventory": {},
  "quality_metrics": {},
  "progress_calculation": {},
  "timeline_analysis": {}
}
EOF

    echo "  🔍 フェーズ別進捗を分析中..."

    # 各開発フェーズを分析
    local phases=("use_case_creation" "domain_modeling" "test_creation" "domain_implementation" "usecase_implementation" "infrastructure_implementation" "presentation_implementation" "all_tests_completed" "refactor" "scenario_evolution" "review" "feedback_application")

    local total_phases=${#phases[@]}
    local completed_phases=0
    local current_phase_index=0

    for i in "${!phases[@]}"; do
        local phase="${phases[$i]}"
        local phase_data=$(jq -c ".phases.${phase} // {}" "$metadata_file")
        local completed=$(jq -r ".phases.${phase}.completed // false" "$metadata_file")
        local created=$(jq -r ".phases.${phase}.created // false" "$metadata_file")

        if [[ "$completed" == "true" ]]; then
            completed_phases=$((completed_phases + 1))
        fi

        if [[ "$current_phase" == *"${phase}"* ]]; then
            current_phase_index=$i
        fi

        # フェーズデータで分析を更新
        jq --arg phase "$phase" --argjson data "$phase_data" \
           --arg status "$(if [[ "$completed" == "true" ]]; then echo "completed"; elif [[ "$created" == "true" ]]; then echo "in_progress"; else echo "pending"; fi)" \
           '.phase_analysis[$phase] = ($data + {"status": $status})' \
           "$analysis_report" > "${analysis_report}.tmp" && mv "${analysis_report}.tmp" "$analysis_report"
    done

    # 進捗パーセンテージを計算
    local progress_percentage=$(( (completed_phases * 100) / total_phases ))

    echo "  📈 進捗率計算: ${completed_phases}/${total_phases} (${progress_percentage}%)"

    # 進捗計算を更新
    jq --argjson total "$total_phases" --argjson completed "$completed_phases" \
       --argjson percentage "$progress_percentage" --argjson current_index "$current_phase_index" \
       '.progress_calculation = {
         "total_phases": $total,
         "completed_phases": $completed,
         "progress_percentage": $percentage,
         "current_phase_index": $current_index
       }' "$analysis_report" > "${analysis_report}.tmp" && mv "${analysis_report}.tmp" "$analysis_report"

    echo "$analysis_report"
}

metadata_analysis=$(analyze_metadata_comprehensive)
```

## 4. **ファイルインベントリと品質評価**

```bash
# 包括的ファイルインベントリと品質評価を実施
echo "📁 ファイルインベントリと品質評価を実行中..."

conduct_file_quality_assessment() {
    local inventory_report="$status_workspace/file_inventory.json"

    # インベントリを初期化
    cat > "$inventory_report" << EOF
{
  "inventory_date": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "feature": "$feature_name",
  "documents": {},
  "implementation": {},
  "tests": {},
  "quality_metrics": {},
  "file_health": {}
}
EOF

    echo "  📄 ドキュメントファイルを検索中..."

    # 仕様ファイルを検索
    local spec_file=""
    local spec_candidates=()
    mapfile -t spec_candidates < <(find docs/use_cases -name "*${feature_name}*" -name "*.md" 2>/dev/null)
    if [[ ${#spec_candidates[@]} -gt 0 ]]; then
        spec_file="${spec_candidates[0]}"
    fi

    # ドメインドキュメントを検索
    local domain_docs=()
    mapfile -t domain_docs < <(find docs/domain -name "*${feature_name}*" 2>/dev/null)

    # テストレポートを検索
    local test_reports=()
    mapfile -t test_reports < <(find docs/test_results -name "*${feature_name}*" 2>/dev/null)

    # レビュードキュメントを検索
    local review_docs=()
    mapfile -t review_docs < <(find docs/review -name "*${feature_name}*" 2>/dev/null)

    # ドキュメントインベントリを更新
    jq --arg spec "$spec_file" \
       --argjson domain_docs "$(printf '%s\n' "${domain_docs[@]}" | jq -R . | jq -s .)" \
       --argjson test_reports "$(printf '%s\n' "${test_reports[@]}" | jq -R . | jq -s .)" \
       --argjson review_docs "$(printf '%s\n' "${review_docs[@]}" | jq -R . | jq -s .)" \
       '.documents = {
         "specification": $spec,
         "domain_docs": $domain_docs,
         "test_reports": $test_reports,
         "review_docs": $review_docs
       }' "$inventory_report" > "${inventory_report}.tmp" && mv "${inventory_report}.tmp" "$inventory_report"

    echo "  🏗️ 実装ファイルを検索中..."

    # レイヤー別実装ファイルを検索
    local layers=("domain" "application" "infrastructure" "presentation")
    for layer in "${layers[@]}"; do
        if [[ -d "src/$layer" ]]; then
            local layer_files=()
            mapfile -t layer_files < <(find "src/$layer" -name "*.py" 2>/dev/null)

            jq --arg layer "$layer" \
               --argjson files "$(printf '%s\n' "${layer_files[@]}" | jq -R . | jq -s .)" \
               --argjson count "${#layer_files[@]}" \
               '.implementation[$layer] = {"files": $files, "count": $count}' \
               "$inventory_report" > "${inventory_report}.tmp" && mv "${inventory_report}.tmp" "$inventory_report"
        fi
    done

    echo "  🧪 テストファイルを検索中..."

    # テストファイルを検索
    local test_types=("unit" "integration" "e2e")
    for test_type in "${test_types[@]}"; do
        if [[ -d "tests/$test_type" ]]; then
            local test_files=()
            mapfile -t test_files < <(find "tests/$test_type" -name "*.py" 2>/dev/null)

            jq --arg type "$test_type" \
               --argjson files "$(printf '%s\n' "${test_files[@]}" | jq -R . | jq -s .)" \
               --argjson count "${#test_files[@]}" \
               '.tests[$type] = {"files": $files, "count": $count}' \
               "$inventory_report" > "${inventory_report}.tmp" && mv "${inventory_report}.tmp" "$inventory_report"
        fi
    done

    echo "  📊 品質メトリクスを収集中..."

    # 可能な場合は品質メトリクスを収集
    local coverage_percent="N/A"
    local ruff_errors="N/A"
    local pyright_errors="N/A"

    # pytestが利用可能な場合はテストカバレッジを取得
    if command -v uv >/dev/null 2>&1 && [[ -d "tests" ]]; then
        local coverage_file="$status_workspace/quick_coverage.json"
        if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" timeout 30 uv run --frozen pytest --cov=src --cov-report=json:"$coverage_file" -q >/dev/null 2>&1; then
            coverage_percent=$(jq -r '.totals.percent_covered // "N/A"' "$coverage_file" 2>/dev/null || echo "N/A")
        fi
    fi

    # 利用可能な場合はRuffイシューを取得
    if command -v uv >/dev/null 2>&1; then
        local ruff_file="$status_workspace/quick_ruff.json"
        if timeout 15 uv run --frozen ruff check . --output-format=json > "$ruff_file" 2>/dev/null; then
            ruff_errors=$(jq '. | length' "$ruff_file" 2>/dev/null || echo "N/A")
        fi
    fi

    # 利用可能な場合はPyrightイシューを取得
    if command -v uv >/dev/null 2>&1; then
        local pyright_file="$status_workspace/quick_pyright.json"
        if timeout 15 uv run --frozen pyright --outputjson > "$pyright_file" 2>/dev/null; then
            pyright_errors=$(jq '.summary.errorCount // "N/A"' "$pyright_file" 2>/dev/null || echo "N/A")
        fi
    fi

    # 品質メトリクスを更新
    jq --arg coverage "$coverage_percent" \
       --arg ruff "$ruff_errors" \
       --arg pyright "$pyright_errors" \
       '.quality_metrics = {
         "test_coverage": $coverage,
         "ruff_errors": $ruff,
         "pyright_errors": $pyright
       }' "$inventory_report" > "${inventory_report}.tmp" && mv "${inventory_report}.tmp" "$inventory_report"

    echo "✅ ファイルインベントリ完了"
    echo "$inventory_report"
}

file_inventory=$(conduct_file_quality_assessment)
```

## 5. **GitHub統合とステータス同期**

```bash
# 包括的ステータスのためGitHubと同期
echo "🔗 GitHub連携と状況同期を実行中..."

sync_github_status() {
    local github_report="$status_workspace/github_status.json"

    # GitHubステータスレポートを初期化
    cat > "$github_report" << EOF
{
  "sync_date": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "feature": "$feature_name",
  "issues": {},
  "repository_info": {},
  "team_activity": {}
}
EOF

    echo "  🎯 GitHub イシュー情報を取得中..."

    # 各イシュー番号の情報を取得
    for issue_num in "${issue_numbers[@]}"; do
        echo "    📋 Issue #$issue_num を確認中..."

        if safe_gh_command "issue" "view" "$issue_num" --json state,title,labels,assignees,updatedAt,comments; then
            local issue_data=$(safe_gh_command "issue" "view" "$issue_num" --json state,title,labels,assignees,updatedAt,comments)

            if [[ -n "$issue_data" ]]; then
                local state=$(echo "$issue_data" | jq -r '.state // "unknown"')
                local title=$(echo "$issue_data" | jq -r '.title // "Unknown"')
                local updated_at=$(echo "$issue_data" | jq -r '.updatedAt // "Unknown"')
                local assignees_count=$(echo "$issue_data" | jq '.assignees | length')
                local comments_count=$(echo "$issue_data" | jq '.comments | length')
                local labels=$(echo "$issue_data" | jq -c '.labels // []')

                jq --arg issue "$issue_num" \
                   --arg state "$state" \
                   --arg title "$title" \
                   --arg updated "$updated_at" \
                   --argjson assignees "$assignees_count" \
                   --argjson comments "$comments_count" \
                   --argjson labels "$labels" \
                   '.issues[$issue] = {
                     "state": $state,
                     "title": $title,
                     "updated_at": $updated,
                     "assignees_count": $assignees,
                     "comments_count": $comments,
                     "labels": $labels
                   }' "$github_report" > "${github_report}.tmp" && mv "${github_report}.tmp" "$github_report"

                echo "      ✅ Issue #$issue_num: $state ($title)"
            else
                echo "      ⚠️ Issue #$issue_num: 情報取得に失敗"
            fi
        else
            echo "      ❌ Issue #$issue_num: アクセスできません"
        fi
    done

    echo "  📊 リポジトリ情報を取得中..."

    # 基本リポジトリ情報を取得
    if safe_gh_command "repo" "view" --json name,defaultBranch,pushedAt; then
        local repo_data=$(safe_gh_command "repo" "view" --json name,defaultBranch,pushedAt)

        if [[ -n "$repo_data" ]]; then
            jq --argjson repo "$repo_data" '.repository_info = $repo' "$github_report" > "${github_report}.tmp" && mv "${github_report}.tmp" "$github_report"
            echo "    ✅ リポジトリ情報取得完了"
        fi
    else
        echo "    ⚠️ リポジトリ情報の取得に失敗"
    fi

    echo "$github_report"
}

github_status=$(sync_github_status)
```

## 6. **インテリジェント次アクション推奨**

```bash
# インテリジェント次アクション推奨を生成
echo "🧠 次のアクションを知的に推奨中..."

generate_smart_recommendations() {
    local recommendations_report="$status_workspace/recommendations.json"

    # 現在の進捗データを取得
    local current_phase=$(jq -r '.basic_info.current_phase' "$metadata_analysis")
    local progress_percentage=$(jq -r '.progress_calculation.progress_percentage' "$metadata_analysis")
    local completed_phases=$(jq -r '.progress_calculation.completed_phases' "$metadata_analysis")

    # 推奨事項を初期化
    cat > "$recommendations_report" << EOF
{
  "analysis_date": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "feature": "$feature_name",
  "current_phase": "$current_phase",
  "progress_percentage": $progress_percentage,
  "recommendations": {
    "immediate_actions": [],
    "next_milestones": [],
    "quality_improvements": [],
    "risk_mitigation": []
  },
  "priority_matrix": {},
  "estimated_effort": {}
}
EOF

    echo "  🎯 現在フェーズを分析中: $current_phase"

    # 現在フェーズに基づく即座の次アクションを決定
    local immediate_actions=()
    local next_milestones=()
    local quality_improvements=()
    local risk_items=()

    case "$current_phase" in
        "created"|"use_case_created")
            immediate_actions+=("ドメインモデリングの実行: /domain-modeling $(IFS=','; echo "${issue_numbers[*]}")")
            next_milestones+=("ドメイン設計の完了")
            ;;
        "domain_modeled")
            immediate_actions+=("テスト作成(RED): /create-tests $(IFS=','; echo "${issue_numbers[*]}")")
            next_milestones+=("失敗テストの作成とTDD開始")
            ;;
        "tests_created")
            immediate_actions+=("ドメイン実装(GREEN): /implement-domain $(IFS=','; echo "${issue_numbers[*]}")")
            next_milestones+=("ドメイン層の実装完了")
            ;;
        "domain_implemented")
            immediate_actions+=("アプリケーション層実装: /implement-usecase $(IFS=','; echo "${issue_numbers[*]}")")
            next_milestones+=("ユースケース層の実装完了")
            ;;
        "usecase_implemented")
            immediate_actions+=("インフラ層実装: /implement-infra $(IFS=','; echo "${issue_numbers[*]}")")
            next_milestones+=("永続化層の実装完了")
            ;;
        "infrastructure_implemented")
            immediate_actions+=("プレゼンテーション層実装: /implement-presentation $(IFS=','; echo "${issue_numbers[*]}")")
            next_milestones+=("API/UI層の実装完了")
            ;;
        "presentation_implemented")
            immediate_actions+=("全テスト実行: /run-all-tests $(IFS=','; echo "${issue_numbers[*]}")")
            next_milestones+=("包括的テストの実行と品質確認")
            ;;
        "all_tests_completed")
            immediate_actions+=("リファクタリング: /refactor $(IFS=','; echo "${issue_numbers[*]}")")
            next_milestones+=("コード品質の向上(REFACTOR)")
            ;;
        "refactored")
            immediate_actions+=("レビュー実行: /review-issue $(IFS=','; echo "${issue_numbers[*]}")")
            next_milestones+=("実装の包括的レビュー")
            ;;
        "reviewed")
            immediate_actions+=("フィードバック適用: /apply-feedback $(IFS=','; echo "${issue_numbers[*]}")")
            next_milestones+=("レビューフィードバックの反映")
            ;;
        "feedback_applied")
            immediate_actions+=("プルリクエスト作成: /create-pr $(IFS=','; echo "${issue_numbers[*]}")")
            next_milestones+=("本番展開の準備完了")
            ;;
        *)
            immediate_actions+=("進捗状況の詳細確認が必要")
            next_milestones+=("現在のフェーズの特定と適切なアクション決定")
            ;;
    esac

    # メトリクスに基づく品質改善推奨事項を追加
    local coverage=$(jq -r '.quality_metrics.test_coverage // "N/A"' "$file_inventory")
    local ruff_errors=$(jq -r '.quality_metrics.ruff_errors // "N/A"' "$file_inventory")
    local pyright_errors=$(jq -r '.quality_metrics.pyright_errors // "N/A"' "$file_inventory")

    if [[ "$coverage" != "N/A" && "$coverage" != "null" ]]; then
        if (( $(echo "$coverage < 80" | bc -l 2>/dev/null || echo 0) )); then
            quality_improvements+=("テストカバレッジを80%以上に向上 (現在: ${coverage}%)")
        fi
    fi

    if [[ "$ruff_errors" != "N/A" && "$ruff_errors" != "null" && "$ruff_errors" != "0" ]]; then
        quality_improvements+=("Ruffエラーの修正: ${ruff_errors}件")
    fi

    if [[ "$pyright_errors" != "N/A" && "$pyright_errors" != "null" && "$pyright_errors" != "0" ]]; then
        quality_improvements+=("Pyright型エラーの修正: ${pyright_errors}件")
    fi

    # GitHubステータスに基づくリスク軽減を追加
    local open_issues=$(jq -r '[.issues[] | select(.state == "open")] | length' "$github_status")
    if [[ $open_issues -gt 1 ]]; then
        risk_items+=("複数のオープンイシューが存在: ${open_issues}件 - 優先度の明確化が必要")
    fi

    # 古いイシューをチェック（7日以上更新されていない）
    local stale_threshold=$(date -u -d '7 days ago' +%Y-%m-%dT%H:%M:%SZ)
    local stale_issues=$(jq -r --arg threshold "$stale_threshold" '[.issues[] | select(.updated_at < $threshold)] | length' "$github_status")
    if [[ $stale_issues -gt 0 ]]; then
        risk_items+=("更新が停滞しているイシュー: ${stale_issues}件 - 定期的な進捗確認が必要")
    fi

    # 推奨事項を更新
    jq --argjson immediate "$(printf '%s\n' "${immediate_actions[@]}" | jq -R . | jq -s .)" \
       --argjson milestones "$(printf '%s\n' "${next_milestones[@]}" | jq -R . | jq -s .)" \
       --argjson quality "$(printf '%s\n' "${quality_improvements[@]}" | jq -R . | jq -s .)" \
       --argjson risks "$(printf '%s\n' "${risk_items[@]}" | jq -R . | jq -s .)" \
       '.recommendations.immediate_actions = $immediate |
        .recommendations.next_milestones = $milestones |
        .recommendations.quality_improvements = $quality |
        .recommendations.risk_mitigation = $risks' \
       "$recommendations_report" > "${recommendations_report}.tmp" && mv "${recommendations_report}.tmp" "$recommendations_report"

    echo "✅ 推奨アクション生成完了"
    echo "$recommendations_report"
}

recommendations=$(generate_smart_recommendations)
```

## 7. **包括的ステータスレポート生成**

```bash
# 美しく包括的なステータスレポートを生成
echo "📋 包括的ステータスレポートを生成中..."

generate_status_report() {
    local status_report_file="$status_workspace/use_case_status_report.md"

    # レポート用データを抽出
    local created_at=$(jq -r '.basic_info.created_at' "$metadata_analysis")
    local updated_at=$(jq -r '.basic_info.updated_at' "$metadata_analysis")
    local current_phase=$(jq -r '.basic_info.current_phase' "$metadata_analysis")
    local progress_percentage=$(jq -r '.progress_calculation.progress_percentage' "$metadata_analysis")
    local completed_phases=$(jq -r '.progress_calculation.completed_phases' "$metadata_analysis")
    local total_phases=$(jq -r '.progress_calculation.total_phases' "$metadata_analysis")

    # 進捗バーを作成
    local progress_filled=$((progress_percentage / 8))  # ~12ブロック用8%ずつ
    local progress_empty=$((12 - progress_filled))
    local progress_bar=""
    for ((i=0; i<progress_filled; i++)); do progress_bar+="█"; done
    for ((i=0; i<progress_empty; i++)); do progress_bar+="░"; done

    # ファイル情報を抽出
    local spec_file=$(jq -r '.documents.specification // "未作成"' "$file_inventory")
    local domain_docs_count=$(jq '.documents.domain_docs | length' "$file_inventory")
    local test_reports_count=$(jq '.documents.test_reports | length' "$file_inventory")
    local review_docs_count=$(jq '.documents.review_docs | length' "$file_inventory")

    # 実装カウントを抽出
    local domain_files=$(jq '.implementation.domain.count // 0' "$file_inventory")
    local app_files=$(jq '.implementation.application.count // 0' "$file_inventory")
    local infra_files=$(jq '.implementation.infrastructure.count // 0' "$file_inventory")
    local pres_files=$(jq '.implementation.presentation.count // 0' "$file_inventory")

    # テストカウントを抽出
    local unit_tests=$(jq '.tests.unit.count // 0' "$file_inventory")
    local integration_tests=$(jq '.tests.integration.count // 0' "$file_inventory")
    local e2e_tests=$(jq '.tests.e2e.count // 0' "$file_inventory")

    # 品質メトリクスを抽出
    local coverage=$(jq -r '.quality_metrics.test_coverage // "N/A"' "$file_inventory")
    local ruff_errors=$(jq -r '.quality_metrics.ruff_errors // "N/A"' "$file_inventory")
    local pyright_errors=$(jq -r '.quality_metrics.pyright_errors // "N/A"' "$file_inventory")

    cat > "$status_report_file" << EOF
# 📊 ユースケース開発状況レポート

## 🎯 基本情報

| 項目 | 詳細 |
|------|------|
| **機能名** | ${feature_name} |
| **関連イシュー** | #$(IFS=' #'; echo "${issue_numbers[*]}") |
| **作成日時** | ${created_at} |
| **最終更新** | ${updated_at} |
| **現在フェーズ** | ${current_phase} |
| **メタデータファイル** | \`${metadata_file}\` |

## 📈 全体進捗状況

### 進捗概要
\`\`\`
[${progress_bar}] ${progress_percentage}% 完了
\`\`\`

**完了フェーズ**: ${completed_phases} / ${total_phases}

### フェーズ別詳細進捗

$(
echo "| フェーズ | 状態 | 完了日時 | 詳細 |"
echo "|---------|------|----------|------|"

# フェーズステータステーブルを生成
phases=("use_case_creation" "domain_modeling" "test_creation" "domain_implementation" "usecase_implementation" "infrastructure_implementation" "presentation_implementation" "all_tests_completed" "refactor" "scenario_evolution" "review" "feedback_application")
phase_names=("📝 ユースケース仕様" "🏗️ ドメインモデル" "🧪 テスト作成(RED)" "💼 ドメイン実装(GREEN)" "🔧 アプリケーション層" "🏭 インフラ層" "🖼️ プレゼンテーション層" "🧪 全テスト実行" "🔄 リファクタリング" "📋 シナリオ進化" "🔍 実装レビュー" "🔧 フィードバック適用")

for i in "${!phases[@]}"; do
    phase="${phases[$i]}"
    phase_name="${phase_names[$i]}"

    completed=$(jq -r ".phase_analysis.${phase}.completed // false" "$metadata_analysis")
    completed_at=$(jq -r ".phase_analysis.${phase}.completed_at // \"-\"" "$metadata_analysis")
    created=$(jq -r ".phase_analysis.${phase}.created // false" "$metadata_analysis")

    if [[ "$completed" == "true" ]]; then
        status="✅ 完了"
    elif [[ "$created" == "true" ]]; then
        status="🚧 実装中"
    else
        status="⏳ 未着手"
    fi

    echo "| ${phase_name} | ${status} | ${completed_at} | - |"
done
)

## 📁 ファイル一覧

### 📄 ドキュメント
| 種類 | ファイル/数量 | 状態 |
|------|---------------|------|
| ユースケース仕様 | \`${spec_file}\` | $(if [[ "$spec_file" != "未作成" ]]; then echo "✅ 存在"; else echo "❌ 未作成"; fi) |
| ドメイン設計書 | ${domain_docs_count} ファイル | $(if [[ $domain_docs_count -gt 0 ]]; then echo "✅ 存在"; else echo "❌ 未作成"; fi) |
| テストレポート | ${test_reports_count} ファイル | $(if [[ $test_reports_count -gt 0 ]]; then echo "✅ 存在"; else echo "❌ 未作成"; fi) |
| レビューレポート | ${review_docs_count} ファイル | $(if [[ $review_docs_count -gt 0 ]]; then echo "✅ 存在"; else echo "❌ 未作成"; fi) |

### 🏗️ 実装ファイル
| レイヤー | ファイル数 | 状態 |
|----------|------------|------|
| Domain | ${domain_files} ファイル | $(if [[ $domain_files -gt 0 ]]; then echo "✅ 実装済み"; else echo "❌ 未実装"; fi) |
| Application | ${app_files} ファイル | $(if [[ $app_files -gt 0 ]]; then echo "✅ 実装済み"; else echo "❌ 未実装"; fi) |
| Infrastructure | ${infra_files} ファイル | $(if [[ $infra_files -gt 0 ]]; then echo "✅ 実装済み"; else echo "❌ 未実装"; fi) |
| Presentation | ${pres_files} ファイル | $(if [[ $pres_files -gt 0 ]]; then echo "✅ 実装済み"; else echo "❌ 未実装"; fi) |

### 🧪 テストファイル
| テスト種別 | ファイル数 | 状態 |
|------------|------------|------|
| Unit Tests | ${unit_tests} ファイル | $(if [[ $unit_tests -gt 0 ]]; then echo "✅ 存在"; else echo "❌ 未作成"; fi) |
| Integration Tests | ${integration_tests} ファイル | $(if [[ $integration_tests -gt 0 ]]; then echo "✅ 存在"; else echo "❌ 未作成"; fi) |
| E2E Tests | ${e2e_tests} ファイル | $(if [[ $e2e_tests -gt 0 ]]; then echo "✅ 存在"; else echo "❌ 未作成"; fi) |

## 📊 品質メトリクス

| メトリクス | 現在値 | 目標 | 評価 |
|-----------|--------|------|------|
| テストカバレッジ | ${coverage}% | >80% | $(if [[ "$coverage" != "N/A" && "$coverage" != "null" ]]; then if (( $(echo "$coverage >= 80" | bc -l 2>/dev/null || echo 0) )); then echo "✅ 達成"; else echo "⚠️ 要改善"; fi; else echo "❓ 未測定"; fi) |
| Ruffエラー | ${ruff_errors} 件 | 0件 | $(if [[ "$ruff_errors" == "0" ]]; then echo "✅ 適合"; elif [[ "$ruff_errors" != "N/A" && "$ruff_errors" != "null" ]]; then echo "⚠️ 要修正"; else echo "❓ 未確認"; fi) |
| Pyrightエラー | ${pyright_errors} 件 | 0件 | $(if [[ "$pyright_errors" == "0" ]]; then echo "✅ 適合"; elif [[ "$pyright_errors" != "N/A" && "$pyright_errors" != "null" ]]; then echo "⚠️ 要修正"; else echo "❓ 未確認"; fi) |

## 🔗 GitHub 連携状況

$(
echo "| Issue # | 状態 | タイトル | 最終更新 | コメント数 |"
echo "|---------|------|----------|----------|------------|"

for issue_num in "${issue_numbers[@]}"; do
    state=$(jq -r ".issues.\"${issue_num}\".state // \"unknown\"" "$github_status")
    title=$(jq -r ".issues.\"${issue_num}\".title // \"Unknown\"" "$github_status")
    updated=$(jq -r ".issues.\"${issue_num}\".updated_at // \"Unknown\"" "$github_status")
    comments=$(jq -r ".issues.\"${issue_num}\".comments_count // 0" "$github_status")

    state_icon="❓"
    case "$state" in
        "open") state_icon="🔓" ;;
        "closed") state_icon="✅" ;;
    esac

    echo "| #${issue_num} | ${state_icon} ${state} | ${title} | ${updated} | ${comments} |"
done
)

## 🎯 次のアクション

### 🚨 即座に実行すべき項目
$(jq -r '.recommendations.immediate_actions[] | "- " + .' "$recommendations")

### 📋 次のマイルストーン
$(jq -r '.recommendations.next_milestones[] | "- " + .' "$recommendations")

$(if jq -e '.recommendations.quality_improvements | length > 0' "$recommendations" >/dev/null; then
echo "### 📈 品質改善推奨項目"
jq -r '.recommendations.quality_improvements[] | "- " + .' "$recommendations"
fi)

$(if jq -e '.recommendations.risk_mitigation | length > 0' "$recommendations" >/dev/null; then
echo "### ⚠️ リスク軽減項目"
jq -r '.recommendations.risk_mitigation[] | "- " + .' "$recommendations"
fi)

## 📈 開発効率分析

### タイムライン概要
- **開始**: $(echo "$created_at" | cut -d'T' -f1)
- **最終更新**: $(echo "$updated_at" | cut -d'T' -f1)
- **経過日数**: $(( ($(date -d "$updated_at" +%s 2>/dev/null || date +%s) - $(date -d "$created_at" +%s 2>/dev/null || date +%s)) / 86400 )) 日
- **進捗率**: ${progress_percentage}%

### 推定残り作業
$(
remaining_phases=$((total_phases - completed_phases))
if [[ $remaining_phases -eq 0 ]]; then
    echo "🎉 **完了**: 全フェーズが完了しています！"
elif [[ $remaining_phases -le 2 ]]; then
    echo "🏁 **最終段階**: あと${remaining_phases}フェーズで完了"
else
    echo "⏳ **継続中**: あと${remaining_phases}フェーズが残っています"
fi
)

## 🎉 ステータスサマリー

$(
if [[ $progress_percentage -ge 100 ]]; then
    echo "✅ **完了**: 全開発フェーズが完了しました！本番展開準備完了です。"
elif [[ $progress_percentage -ge 80 ]]; then
    echo "🏁 **最終段階**: 開発がほぼ完了しています。最終調整とレビューに集中してください。"
elif [[ $progress_percentage -ge 60 ]]; then
    echo "🚀 **順調**: 開発が順調に進んでいます。品質確保に注意して継続してください。"
elif [[ $progress_percentage -ge 40 ]]; then
    echo "⚡ **中盤**: 実装の中盤です。アーキテクチャの一貫性を保ちながら進めてください。"
elif [[ $progress_percentage -ge 20 ]]; then
    echo "🌱 **初期段階**: 基礎設計から実装への移行期です。設計の品質確保が重要です。"
else
    echo "🚀 **開始**: プロジェクトの初期段階です。しっかりとした基盤作りに集中してください。"
fi
)

---

**レポート生成日時**: $(date)
**次回確認推奨**: $(date -d '+1 day')
EOF

    echo "✅ ステータスレポート生成完了: $status_report_file"
    echo "$status_report_file"
}

status_report_file=$(generate_status_report)
```

## 8. **美しいコンソール表示**

```bash
# コンソールで美しいステータスを表示
echo ""
echo "🎉 ユースケース開発状況レポート"
echo "=================================="
echo ""
echo "🎯 **基本情報**"
echo "  機能名: $feature_name"
echo "  関連イシュー: #$(IFS=' #'; echo "${issue_numbers[*]}")"
echo "  現在フェーズ: $(jq -r '.basic_info.current_phase' "$metadata_analysis")"
echo ""

# 美しい進捗バーを表示
progress_percentage=$(jq -r '.progress_calculation.progress_percentage' "$metadata_analysis")
completed_phases=$(jq -r '.progress_calculation.completed_phases' "$metadata_analysis")
total_phases=$(jq -r '.progress_calculation.total_phases' "$metadata_analysis")

progress_filled=$((progress_percentage / 5))  # 20ブロック用5%ずつ
progress_empty=$((20 - progress_filled))
progress_bar=""
for ((i=0; i<progress_filled; i++)); do progress_bar+="█"; done
for ((i=0; i<progress_empty; i++)); do progress_bar+="░"; done

echo "📈 **全体進捗**"
echo "  [${progress_bar}] ${progress_percentage}%"
echo "  完了フェーズ: ${completed_phases}/${total_phases}"
echo ""

# 即座の次アクションを表示
echo "🎯 **次のアクション**"
jq -r '.recommendations.immediate_actions[] | "  ▶ " + .' "$recommendations"
echo ""

# 品質ステータスを表示
coverage=$(jq -r '.quality_metrics.test_coverage // "N/A"' "$file_inventory")
ruff_errors=$(jq -r '.quality_metrics.ruff_errors // "N/A"' "$file_inventory")
pyright_errors=$(jq -r '.quality_metrics.pyright_errors // "N/A"' "$file_inventory")

echo "📊 **品質状況**"
echo "  テストカバレッジ: ${coverage}%"
echo "  Ruffエラー: ${ruff_errors} 件"
echo "  Pyrightエラー: ${pyright_errors} 件"
echo ""

# GitHubステータスサマリーを表示
open_issues=$(jq -r '[.issues[] | select(.state == "open")] | length' "$github_status")
closed_issues=$(jq -r '[.issues[] | select(.state == "closed")] | length' "$github_status")

echo "🔗 **GitHub状況**"
echo "  オープンイシュー: ${open_issues} 件"
echo "  完了イシュー: ${closed_issues} 件"
echo ""

# 主要ファイルを表示
spec_file=$(jq -r '.documents.specification // "未作成"' "$file_inventory")
echo "📁 **主要ファイル**"
echo "  ユースケース仕様: $(basename "$spec_file")"
echo "  メタデータ: $(basename "$metadata_file")"
echo "  詳細レポート: $(basename "$status_report_file")"
echo ""

# ステータスサマリーを表示
echo "🎯 **ステータスサマリー**"
if [[ $progress_percentage -ge 100 ]]; then
    echo "  ✅ 完了: 全開発フェーズが完了しました！"
elif [[ $progress_percentage -ge 80 ]]; then
    echo "  🏁 最終段階: もうすぐ完了です"
elif [[ $progress_percentage -ge 60 ]]; then
    echo "  🚀 順調: 開発が順調に進んでいます"
elif [[ $progress_percentage -ge 40 ]]; then
    echo "  ⚡ 中盤: 実装の中盤です"
elif [[ $progress_percentage -ge 20 ]]; then
    echo "  🌱 初期段階: 基礎から実装への移行期"
else
    echo "  🚀 開始: プロジェクトの初期段階"
fi
echo ""

echo "📋 **詳細レポート**: $status_report_file"
echo "🔄 **更新**: /use-case-status $(IFS=','; echo "${issue_numbers[*]}") で最新状況確認"
echo ""
echo "✅ ステータス確認が完了しました"
```

## 重要な注意事項

### **包括的状況把握**

- メタデータ・ファイル・GitHub・品質の多角的分析
- リアルタイム進捗計算と可視化
- インテリジェントな次アクション推奨
- 過去実績と将来予測の統合表示

### **チーム協力支援**

- ステークホルダー向け詳細レポート生成
- GitHubイシューとの完全同期
- 品質メトリクスの透明性確保
- プロジェクト健全性の継続監視

### **使いやすさと効率性**

- 読み取り専用での安全な実行
- 高速な情報収集とタイムアウト制御
- 美しいコンソール表示と詳細レポート
- 具体的なコマンド提案と実行可能性

**統合版ステータス確認コマンドにより、プロジェクトの完全な可視性と効率的な意思決定支援が実現されます！**

## 🚨 CLAUDE CODE必須: シナリオ進化チェック

ステータス確認中に新課題・ギャップ・改善点発見時は
作業を中断して `/evolve-scenarios <feature-name>` を実行すること
重要: ステータス確認は問題発見と進化の重要な機会です