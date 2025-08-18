プロジェクトビジョンとコアシナリオを作成します。

## メタデータ
- **前提条件**: なし（プロジェクト初期フェーズ）
- **入力**: なし（情報収集のための対話型プロンプト）
- **出力**: 
  - `docs/vision/project-vision.md` - プロジェクトビジョンドキュメント
  - `docs/use_cases/core/index.md` - コアシナリオインデックス
  - `docs/steering/*.md` - ステアリングドキュメント（プロダクト/技術/構造）
- **依存関係**: 後続のすべてのコマンドの基盤
- **実行タイミング**: プロジェクト開始時に一度のみ

## 🎯 **TDD/DDD/レイヤードプロセスコンテキスト**

**🔄 コアワークフロー**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 アーキテクチャ**: クリーンアーキテクチャ（Domain→Application→Infrastructure→Presentation）  
**🧪 開発**: テスト駆動開発（RED→GREEN→REFACTOR）  
**🏗️ 設計**: ドメイン駆動設計（Entity、Value Object、Aggregate、Repository）  
**📋 要件**: Given-When-Thenシナリオによる完全なトレーサビリティ  
**🔄 進化**: /evolve-scenariosコマンドによる継続的シナリオ進化

> 📖 **ドキュメント管理システム**: [README.md](./README.md)  
> 🗺️ **現在位置**: 初期フェーズ - プロジェクトビジョン定義（00/16）  
> 🎯 **フェーズ目的**: プロジェクト方向性の確立とコアシナリオ作成  
> ➡️ **次のステージ**: 03-create-use-case（ユースケース仕様）またはsprint-planning
>
> **📋 3層アーキテクチャ操作**:  
> - 🎯 **戦略**: `docs/use_cases/core/index.md`（プロジェクト設計図作成）  
> - 📊 **戦術**: `docs/use_cases/index.md`（実装マップ初期化）  
> - 🔧 **実行**: 各種メタデータファイル（基盤セットアップ）

## 🎯 **フェーズ目的: ビジョンとシナリオのみ**

**⚠️ 重要な注意:**
- **このステップは文書化のみ** - プロジェクトビジョンとコアシナリオを作成
- **機能実装は行わない** - ビジネス要件とユースケースに焦点を当てる  
- **基盤フェーズ** - プロジェクト方向性と高レベルシナリオの確立
- **戦略的文書のみ作成** - コード実装は行わない

**このステップの内容:**
1. `00-create-vision` ← **【ここにいます】ビジョンドキュメントとコアシナリオ**
2. `01-init-project-structure` ← プロジェクト構造セットアップ
3. `02-sprint-planning` ← シナリオからのスプリント計画
4. その後、TDD/DDD実装サイクル開始

**ビジョン文書化のみ作成してください。**

## よくあるエラーと解決策

### ❌ エラーケース1: ビジョンファイルが既に存在
**原因**: プロジェクトビジョンが既に作成済み  
**解決策**: 
- 既存ビジョンの更新を選択（プロンプトで`y`を入力）
- 新しいプロジェクトの場合は、別のディレクトリで実行

### ❌ エラーケース2: Git設定が不完全
**原因**: `git config user.name`が設定されていない  
**解決策**: 
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### ❌ エラーケース3: ディレクトリ作成権限エラー
**原因**: `docs/`ディレクトリへの書き込み権限がない  
**解決策**: プロジェクトルートディレクトリの権限を確認

## 実行例

### ✅ 成功例
```bash
$ /create-vision
🎯 プロジェクトビジョン作成を開始します
以下の質問にお答えください (Enterで次の質問、空白で標準値使用):

📋 基本情報
============
プロジェクト名: MT5 Trading System
プロジェクトの主な目的: 自動売買システムの構築
主要なターゲットユーザー: トレーダー、投資家
ビジネスドメイン: 金融取引

🏗️ アーキテクチャ情報
==================
メインBounded Context名: Trading
主要エンティティ: Order, Position, Account
主要な機能・ユースケース: 注文管理, ポジション管理, リスク管理

⚙️ 技術要件
============
パフォーマンス要件: レイテンシ < 100ms
セキュリティ要件: API認証, データ暗号化
可用性要件: 99.99% アップタイム

✅ 情報収集完了。ビジョンドキュメントを作成します...
🎉 プロジェクトビジョン作成完了!
```

### ❌ 失敗例と修正
```bash
$ /create-vision
⚠️  プロジェクトビジョンが既に存在します: docs/vision/project-vision.md
既存のビジョンを更新しますか？ (y/N): n
ビジョン作成をキャンセルしました

# 修正: 更新が必要な場合は'y'を選択、または新しいプロジェクトディレクトリで実行
```

## 📋 **ビジョン作成タスクチェックリスト**

**包括的なプロジェクトビジョン作成のためのチェックリストを使用してください:**

### 🔴 必須タスク

#### **📝 対話型情報収集**
- [ ] **プロジェクト基本情報の収集**: 名前、目的、ターゲットユーザー、ビジネスドメイン
- [ ] **アーキテクチャ情報の収集**: メインBounded Context、コアエンティティ、主要機能
- [ ] **技術要件の文書化**: パフォーマンス、セキュリティ、可用性要件

#### **📄 ビジョンドキュメント作成**
- [ ] **プロジェクト概要の作成**: 目的、ビジネス価値、開発アプローチ
- [ ] **Bounded Contextの定義**: 責務、ユースケース、境界、依存関係
- [ ] **コアエンティティの文書化**: 主要ビジネスオブジェクトとドメイン概念
- [ ] **ユビキタス言語の確立**: 定義付きドメイン用語表

#### **📋 コアシナリオ定義**
- [ ] **コアシナリオの抽出**: ビジョンから80%カバレッジシナリオ
- [ ] **ビジネス価値による優先順位付け**: 高/中/低優先度分類
- [ ] **Given-When-Then形式での記述**: 構造化されたシナリオ説明

### 🟡 推奨タスク

#### **📄 ビジョンドキュメント強化**
- [ ] **ステークホルダーの定義**: 役割と関心事を持つプライマリ/セカンダリ
- [ ] **非機能要件の設定**: パフォーマンス、セキュリティ、可用性、スケーラビリティ
- [ ] **技術スタックの文書化**: アーキテクチャパターン、開発手法
- [ ] **成功メトリクスの定義**: ビジネス、技術、チーム指標

#### **🧭 ステアリングドキュメント作成**
- [ ] **プロダクトポリシー作成（product.md）**: ビジネス価値、市場、成功メトリクス
- [ ] **技術ポリシー作成（tech.md）**: アーキテクチャ原則、技術スタック、プロセス
- [ ] **構造ポリシー作成（structure.md）**: レイヤードアーキテクチャ、DDDパターン、命名規約

### 🟢 オプションタスク

#### **📄 高度な計画**
- [ ] **リスクと軽減策の評価**: 技術/ビジネスリスクと対策
- [ ] **進化ロードマップの作成**: フェーズ1（MVP）→ フェーズ2 → フェーズ3
- [ ] **情報完全性の検証**: すべての重要な側面がカバーされていることを確認

#### **📊 基盤セットアップ**
- [ ] **ユースケースインデックスの更新**: ビジョン完了状況と次のステップを追加
- [ ] **すべてのアーティファクトをコミット**: ビジョン、コアシナリオ、ステアリングドキュメント
- [ ] **次のフェーズの準備**: プロジェクト構造初期化の準備

**💡 プロTip**: このチェックリストを実際のプロジェクトで使用するためにコピーしてください！

## タスク詳細

以下の手順に従ってください:

1. **安全環境のセットアップと初期検証**:
   ```bash
   # 🔧 すべての安全操作関数をロード
   source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "00-create-vision" "$ARGUMENTS"
   
   # ビジョン作成は引数を必要としませんが、提供された場合は検証
   if [[ ${#issue_numbers[@]} -gt 0 ]] || [[ ${#other_args[@]} -gt 0 ]]; then
       echo "⚠️  create-vision コマンドは引数を必要としません"
       echo "指定された引数は無視されます"
   fi
   
   # ビジョンが既に存在するかチェック
   vision_file="docs/vision/project-vision.md"
   if [[ -f "$vision_file" ]]; then
       echo "⚠️  プロジェクトビジョンが既に存在します: $vision_file"
       echo "既存のビジョンを更新しますか？ (y/N): "
       read -n 1 -r
       echo
       if [[ ! $REPLY =~ ^[Yy]$ ]]; then
           echo "ビジョン作成をキャンセルしました"
           exit 0
       fi
   fi
   ```

2. **トランザクション開始と対話型情報収集**:
   ```bash
   # 🔄 アトミックビジョン作成のためのトランザクション開始
   if ! begin_transaction "create_vision"; then
       echo "エラー: トランザクションの開始に失敗しました"
       exit 1
   fi
   
   # 💬 対話型プロジェクト情報収集
   echo "🎯 プロジェクトビジョン作成を開始します"
   echo "以下の質問にお答えください (Enterで次の質問、空白で標準値使用):"
   echo ""
   
   # プロジェクト基本情報
   echo "📋 基本情報"
   echo "============"
   
   read -p "プロジェクト名: " project_name
   if [[ -z "$project_name" ]]; then
       project_name="TDD/DDD Project"
   fi
   
   read -p "プロジェクトの主な目的: " project_purpose
   if [[ -z "$project_purpose" ]]; then
       project_purpose="高品質なソフトウェアをTDD/DDD/レイヤードアーキテクチャで開発"
   fi
   
   read -p "主要なターゲットユーザー: " target_users
   if [[ -z "$target_users" ]]; then
       target_users="エンドユーザー、管理者"
   fi
   
   read -p "ビジネスドメイン (例: EC, 金融, ヘルスケア): " business_domain
   if [[ -z "$business_domain" ]]; then
       business_domain="一般ビジネス"
   fi
   
   echo ""
   echo "🏗️ アーキテクチャ情報"
   echo "=================="
   
   read -p "メインBounded Context名: " main_context
   if [[ -z "$main_context" ]]; then
       main_context="Core"
   fi
   
   read -p "主要エンティティ (カンマ区切り): " main_entities
   if [[ -z "$main_entities" ]]; then
       main_entities="User, Product, Order"
   fi
   
   read -p "主要な機能・ユースケース (カンマ区切り): " main_features
   if [[ -z "$main_features" ]]; then
       main_features="ユーザー管理, データ処理, レポート生成"
   fi
   
   echo ""
   echo "⚙️ 技術要件"
   echo "============"
   
   read -p "パフォーマンス要件: " performance_req
   if [[ -z "$performance_req" ]]; then
       performance_req="レスポンス時間 < 2秒, スループット > 1000 req/sec"
   fi
   
   read -p "セキュリティ要件: " security_req
   if [[ -z "$security_req" ]]; then
       security_req="認証・認可、データ暗号化、監査ログ"
   fi
   
   read -p "可用性要件: " availability_req
   if [[ -z "$availability_req" ]]; then
       availability_req="99.9% アップタイム、24/7運用"
   fi
   
   echo ""
   echo "✅ 情報収集完了。ビジョンドキュメントを作成します..."
   ```

3. **ディレクトリ構造の安全作成**:
   ```bash
   # 📁 必要なディレクトリ構造を安全に作成
   echo "📁 ディレクトリ構造作成中..."
   
   required_dirs=(
       "docs/vision"
       "docs/use_cases/core"
       "docs/steering"
   )
   
   for dir in "${required_dirs[@]}"; do
       echo "  📁 作成中: $dir"
       if ! safe_mkdir "$dir"; then
           echo "エラー: ディレクトリ作成に失敗しました: $dir"
           execute_rollback "directory_creation_failed"
           exit 1
       fi
       add_rollback "rmdir '$dir' 2>/dev/null || true" "Remove created directory: $dir"
   done
   
   echo "✅ ディレクトリ構造作成完了"
   ```

4. **安全操作によるビジョンドキュメント作成**:
   ```bash
   # 📄 包括的ビジョンドキュメント作成
   echo "📄 ビジョンドキュメント作成中..."
   
   # ファイル作成前の安全操作検証
   if ! verify_safe_operation "create" "$vision_file" 50; then
       echo "エラー: ファイル作成の安全性チェックに失敗しました"
       execute_rollback "safety_check_failed"
       exit 1
   fi
   
   # ビジョンドキュメントコンテンツ生成
   vision_content="# プロジェクトビジョン: $project_name

   **作成日時**: $(date)
   **最終更新**: $(date)
   **作成者**: $(git config user.name || echo "Unknown")

   ## 概要

   ### プロジェクトの目的
   $project_purpose

   ### ビジネス価値
   - **ターゲットユーザー**: $target_users
   - **ビジネスドメイン**: $business_domain
   - **価値提案**: 高品質なソフトウェアによる効率化とユーザー体験向上

   ### 開発アプローチ
   - **TDD (Test-Driven Development)**: テストファーストによる品質確保
   - **DDD (Domain-Driven Design)**: ビジネスロジック中心の設計
   - **レイヤードアーキテクチャ**: 関心事の分離による保守性向上

   ## Bounded Context

   ### $main_context Context
   - **責務**: メインビジネスロジックとコア機能の提供
   - **主要ユースケース**: 
   $(echo "$main_features" | tr ',' '\n' | sed 's/^[[:space:]]*/  - /')

   ### 境界と依存関係
   - **上流**: 外部システム、ユーザーインターフェース
   - **下流**: データストレージ、外部API、通知システム
   - **共有カーネル**: 共通ユーティリティ、基盤サービス

   ## コアエンティティとドメイン概念

   ### エンティティ
   $(echo "$main_entities" | tr ',' '\n' | while read -r entity; do
       entity=$(echo "$entity" | sed 's/^[[:space:]]*//')
       if [[ -n "$entity" ]]; then
           echo "- **$entity**: ${entity}に関連するビジネスルールと状態を管理"
       fi
   done)

   ### 値オブジェクト
   - **ID**: 不変の識別子（UUID、Email等）
   - **Money**: 金額と通貨の組み合わせ
   - **Address**: 住所情報の構造化表現
   - **DateTime**: 日時情報の適切な表現

   ### ドメインサービス
   - **ValidationService**: ビジネスルール検証
   - **CalculationService**: 複雑な計算ロジック
   - **NotificationService**: 通知ロジックの調整

   ## ユビキタス言語

   | 用語 | 定義 | 使用例 |
   |------|------|--------|
   $(echo "$main_entities" | tr ',' '\n' | head -3 | while read -r entity; do
       entity=$(echo "$entity" | sed 's/^[[:space:]]*//')
       if [[ -n "$entity" ]]; then
           echo "| $entity | ${entity}エンティティ | ${entity}を作成する、${entity}を更新する |"
       fi
   done)
   | アグリゲート | 整合性境界を持つエンティティ群 | 注文アグリゲート、ユーザーアグリゲート |
   | リポジトリ | データアクセスの抽象化 | ${main_entities%%,*}Repository |
   | ユースケース | アプリケーションの具体的な機能 | ${main_features%%,*}機能 |

   ## ステークホルダー

   ### プライマリステークホルダー
   - **エンドユーザー**: システムの主要利用者、直接的な価値を享受
   - **ビジネスオーナー**: ROIと事業成果に責任を持つ
   - **開発チーム**: システムの構築・保守・運用に従事

   ### セカンダリステークホルダー
   - **システム管理者**: 運用・監視・保守業務
   - **サポート担当**: ユーザーサポートとトラブル対応
   - **監査担当**: コンプライアンスとセキュリティ監査

   ## 非機能要件

   ### パフォーマンス
   $performance_req

   ### セキュリティ
   $security_req

   ### 可用性
   $availability_req

   ### スケーラビリティ
   - **水平スケーリング**: ロードバランサーによる負荷分散
   - **垂直スケーリング**: リソース増強による性能向上
   - **データ分散**: 適切なパーティショニング戦略

   ### 保守性
   - **コード品質**: 静的解析ツールによる品質管理
   - **テスト**: 80%以上のテストカバレッジ
   - **ドキュメント**: コードと同期された最新ドキュメント

   ## 技術スタック

   ### アーキテクチャパターン
   - **レイヤードアーキテクチャ**: Presentation → Application → Domain → Infrastructure
   - **CQRS**: 必要に応じてコマンドとクエリの分離
   - **Event Sourcing**: 重要なドメインイベントの記録

   ### 開発手法
   - **TDD**: Red-Green-Refactor サイクル
   - **BDD**: Given-When-Then による仕様記述
   - **Continuous Integration**: 自動テスト・ビルド・デプロイ

   ## 成功指標

   ### ビジネス指標
   - **ユーザー満足度**: NPS > 50
   - **システム稼働率**: > 99.9%
   - **機能提供速度**: スプリントごとの価値提供

   ### 技術指標
   - **コード品質**: SonarQube Grade A
   - **テストカバレッジ**: > 80%
   - **技術債務**: 管理可能なレベル維持

   ### チーム指標
   - **開発効率**: ベロシティの安定向上
   - **品質**: バグ検出・修正時間の短縮
   - **学習**: チーム全体のスキル向上

   ## リスクと対策

   ### 技術リスク
   - **複雑さの増大**: DDD/TDDパターンの学習コスト
     - **対策**: 段階的導入とペアプログラミング
   
   - **パフォーマンス問題**: 分散アーキテクチャのオーバーヘッド
     - **対策**: 適切な監視と継続的な最適化

   ### ビジネスリスク
   - **要件変更**: ビジネス環境の変化による要件変更
     - **対策**: アジャイル開発とステークホルダーとの密な連携

   - **リソース制約**: 開発リソースの制限
     - **対策**: MVP優先とスコープ調整

   ## 進化の方向性

   ### Phase 1: MVP (最小価値製品)
   - コア機能の実装
   - 基本的なユーザー体験
   - 安定したアーキテクチャ基盤

   ### Phase 2: 機能拡張
   - 高度な機能追加
   - ユーザビリティ向上
   - パフォーマンス最適化

   ### Phase 3: スケーリング
   - 大規模対応
   - 多様なプラットフォーム対応
   - AI/ML機能統合

   ---

   **Next Steps**:
   1. スプリント計画: \`/sprint-planning 1\`
   2. プロジェクト初期化: \`/init-project-structure\`
   3. ユースケース作成: \`/create-use-case <issue-number>\`

   **Related Documents**:
   - [Core Scenarios](use_cases/core/index.md)
   - [Steering Documents](../steering/)
   - [Sprint Plans](../sprints/)
   "
   
   # ビジョンドキュメントを安全に作成
   if ! safe_create_file "$vision_file" "$vision_content" true; then
       echo "エラー: ビジョンドキュメントの作成に失敗しました"
       execute_rollback "vision_creation_failed"
       exit 1
   fi
   
   add_rollback "rm -f '$vision_file'" "Remove created vision document"
   echo "✅ ビジョンドキュメント作成完了: $vision_file"
   ```

5. **コアシナリオインデックス作成**:
   ```bash
   # 📋 コアシナリオインデックス作成
   echo "📋 コアシナリオインデックス作成中..."
   
   core_index_file="docs/use_cases/core/index.md"
   
   if ! verify_safe_operation "create" "$core_index_file" 30; then
       echo "エラー: コアシナリオインデックス作成の安全性チェックに失敗しました"
       execute_rollback "core_index_safety_check_failed"
       exit 1
   fi
   
   core_index_content="# コアシナリオ一覧

   **プロジェクト**: $project_name
   **作成日時**: $(date)
   **ビジョン**: [project-vision.md](../../vision/project-vision.md)

   ## 概要

   このドキュメントは、プロジェクトの**コアシナリオ（80%カバレッジ）**を定義します。
   これらのシナリオはプロジェクトの主要価値を提供し、MVP（最小価値製品）の基盤となります。

   ## 優先度分類

   ### 🔴 High Priority (MVP必須)
   
   $(echo "$main_features" | tr ',' '\n' | head -3 | nl | while read -r num feature; do
       feature=$(echo "$feature" | sed 's/^[[:space:]]*//')
       if [[ -n "$feature" ]]; then
           echo "$num. **$feature**"
           echo "   - **ビジネス価値**: 高"
           echo "   - **技術リスク**: 中"
           echo "   - **実装優先度**: 必須"
           echo ""
       fi
   done)

   ### 🟡 Medium Priority (v1.0目標)

   $(echo "$main_features" | tr ',' '\n' | tail -n +4 | head -3 | nl -v4 | while read -r num feature; do
       feature=$(echo "$feature" | sed 's/^[[:space:]]*//')
       if [[ -n "$feature" ]]; then
           echo "$num. **$feature**"
           echo "   - **ビジネス価値**: 中"
           echo "   - **技術リスク**: 低"
           echo "   - **実装優先度**: 重要"
           echo ""
       fi
   done)

   ### 🟢 Low Priority (将来拡張)

   7. **高度な分析・レポート機能**
      - **ビジネス価値**: 中
      - **技術リスク**: 高
      - **実装優先度**: 将来

   8. **多言語・多通貨対応**
      - **ビジネス価値**: 低（現在）
      - **技術リスク**: 中
      - **実装優先度**: 将来

   ## Given-When-Then シナリオ

   ### シナリオ1: $(echo "$main_features" | cut -d',' -f1 | sed 's/^[[:space:]]*//')

   **Given**: システムが初期状態にある
   **When**: ユーザーが基本的な操作を実行する
   **Then**: システムが期待される結果を返す

   **詳細**:
   - **前提条件**: ユーザーが認証済み、システムが正常稼働
   - **トリガー**: ユーザーアクション
   - **期待結果**: 成功レスポンス、状態変更、適切な通知

   ### シナリオ2: $(echo "$main_features" | cut -d',' -f2 | sed 's/^[[:space:]]*//')

   **Given**: 基本機能が利用可能である
   **When**: ユーザーが高度な操作を実行する
   **Then**: システムが適切に処理し結果を提供する

   **詳細**:
   - **前提条件**: 基本データが存在、権限が適切
   - **トリガー**: 業務フロー実行
   - **期待結果**: ビジネスルール適用、データ整合性維持

   ### シナリオ3: エラーハンドリング

   **Given**: システムが例外状況に遭遇する
   **When**: エラーが発生する
   **Then**: 適切なエラー処理と回復が実行される

   **詳細**:
   - **前提条件**: 不正入力、システム障害、外部依存の問題
   - **トリガー**: 例外状況
   - **期待結果**: エラーメッセージ、ログ記録、システム安定性維持

   ## 実装ガイドライン

   ### TDD アプローチ
   1. **Red**: シナリオベースのテストを最初に作成
   2. **Green**: 最小限の実装でテストを通す
   3. **Refactor**: ドメインモデルとアーキテクチャを改善

   ### DDD パターン
   - **エンティティ**: 一意性とライフサイクルを持つオブジェクト
   - **値オブジェクト**: 不変で交換可能なオブジェクト
   - **アグリゲート**: 整合性境界を持つエンティティ群
   - **ドメインサービス**: エンティティや値オブジェクトに属さないビジネスロジック

   ### アーキテクチャ分離
   - **ドメイン層**: ビジネスルールと不変条件
   - **アプリケーション層**: ユースケースの調整
   - **インフラ層**: 外部依存の実装
   - **プレゼンテーション層**: ユーザーインターフェース

   ## 次のステップ

   1. **スプリント計画**: \`/sprint-planning 1\`
   2. **イシュー作成**: GitHub Issues for each core scenario
   3. **開発開始**: \`/create-use-case <issue-number>\`

   ## メトリクス

   - **総シナリオ数**: 8+ scenarios
   - **MVP必須**: 3 scenarios
   - **カバレッジ目標**: 80% of core business value
   - **実装期間目標**: 3-4 sprints

   ---

   **ドキュメント管理**:
   - **戦略レベル**: このドキュメント（プロジェクト全体方針）
   - **戦術レベル**: [../index.md](../index.md)（実装状況管理）
   - **実行レベル**: 個別issue-X-Y.jsonファイル（詳細進捗）
   "
   
   if ! safe_create_file "$core_index_file" "$core_index_content" true; then
       echo "エラー: コアシナリオインデックスの作成に失敗しました"
       execute_rollback "core_index_creation_failed"
       exit 1
   fi
   
   add_rollback "rm -f '$core_index_file'" "Remove created core scenarios index"
   echo "✅ コアシナリオインデックス作成完了: $core_index_file"
   ```

6. **ステアリングドキュメント作成**:
   ```bash
   # 🧭 プロジェクトコンテキスト管理のためのステアリングドキュメント作成
   echo "🧭 ステアリング文書作成中..."
   
   steering_docs=(
       "docs/steering/product.md"
       "docs/steering/tech.md" 
       "docs/steering/structure.md"
   )
   
   # プロダクトステアリングドキュメント
   product_content="# プロダクトポリシー

   **更新日時**: $(date)
   **プロジェクト**: $project_name

   ## プロダクト方針

   ### ビジネス価値優先
   - ユーザー体験の継続的改善
   - ROI（投資対効果）を重視した機能開発
   - データドリブンな意思決定

   ### 品質保証
   - テストファーストアプローチの徹底
   - 継続的品質向上
   - セキュリティ・プライバシー保護

   ### 市場適応性
   - ユーザーフィードバックの迅速な反映
   - 競合分析による差別化戦略
   - スケーラブルな成長戦略

   ## ターゲット市場

   ### プライマリターゲット
   $target_users

   ### セカンダリターゲット
   - 技術に詳しいアーリーアダプター
   - 効率化を求める組織・チーム

   ## 成功メトリクス

   - **ユーザー満足度**: NPS > 50
   - **機能利用率**: 主要機能 > 80%
   - **品質指標**: バグ率 < 1%
   "
   
   if ! safe_create_file "${steering_docs[0]}" "$product_content" true; then
       echo "エラー: プロダクトステアリング文書の作成に失敗しました"
       execute_rollback "product_steering_failed"
       exit 1
   fi
   
   # 技術ステアリングドキュメント
   tech_content="# 技術ポリシー

   **更新日時**: $(date)
   **プロジェクト**: $project_name

   ## 技術方針

   ### アーキテクチャ原則
   - TDD/DDD/レイヤードアーキテクチャの堅持
   - 関心事の分離と疎結合設計
   - 拡張性と保守性の両立

   ### 技術スタック
   - **言語**: Python 3.9+
   - **フレームワーク**: FastAPI, Pydantic
   - **テスト**: pytest, pytest-asyncio
   - **品質**: ruff, pyright
   - **データベース**: PostgreSQL, Redis
   - **インフラ**: Docker, Kubernetes

   ### 開発プロセス
   - **バージョン管理**: Git Flow
   - **CI/CD**: GitHub Actions
   - **コードレビュー**: Pull Request必須
   - **ドキュメント**: コードと同期維持

   ## 非機能要件

   ### パフォーマンス
   $performance_req

   ### セキュリティ
   $security_req

   ### 運用要件
   - 24/7監視体制
   - 自動復旧メカニズム
   - バックアップ・災害復旧計画
   "
   
   if ! safe_create_file "${steering_docs[1]}" "$tech_content" true; then
       echo "エラー: 技術ステアリング文書の作成に失敗しました"
       execute_rollback "tech_steering_failed"
       exit 1
   fi
   
   # 構造ステアリングドキュメント
   structure_content="# 構造ポリシー

   **更新日時**: $(date)
   **プロジェクト**: $project_name

   ## 構造方針

   ### レイヤードアーキテクチャ
   - **Presentation Layer**: UI/API (外向き)
   - **Application Layer**: ユースケース調整
   - **Domain Layer**: ビジネスロジック (内部)
   - **Infrastructure Layer**: データアクセス (外部)

   ### 依存関係の方向
   ```
   Presentation → Application → Domain ← Infrastructure
   ```

   ### パッケージ構造
   ```
   src/
   ├── domain/          # ビジネスロジック
   ├── application/     # ユースケース
   ├── infrastructure/  # データアクセス
   └── presentation/    # API・UI
   ```

   ## DDDパターン適用

   ### エンティティ設計
   - 一意性とライフサイクル管理
   - 不変条件の保持
   - 責務の明確化

   ### 値オブジェクト活用
   - 不変性の保証
   - 自己検証機能
   - 交換可能性

   ### アグリゲート境界
   - 整合性境界の明確化
   - トランザクション境界の定義
   - 他アグリゲートとの疎結合

   ## 命名規約

   ### クラス命名
   - Entity: 名詞 (User, Product)
   - ValueObject: 名詞 + VO (EmailVO, MoneyVO)
   - Service: 動詞 + Service (ValidationService)
   - Repository: Entity + Repository (UserRepository)

   ### メソッド命名
   - Command: 動詞で開始 (create, update, delete)
   - Query: 疑問詞で開始 (find, get, exists)
   - Predicate: is/has/can で開始

   ## 品質基準

   - **テストカバレッジ**: > 80%
   - **循環的複雑度**: < 10
   - **クラス結合度**: 低結合維持
   - **パッケージ凝集度**: 高凝集維持
   "
   
   if ! safe_create_file "${steering_docs[2]}" "$structure_content" true; then
       echo "エラー: 構造ステアリング文書の作成に失敗しました"
       execute_rollback "structure_steering_failed"
       exit 1
   fi
   
   # すべてのステアリングドキュメントのロールバック追加
   for doc in "${steering_docs[@]}"; do
       add_rollback "rm -f '$doc'" "Remove steering document: $doc"
   done
   
   echo "✅ ステアリング文書作成完了 (${#steering_docs[@]} ファイル)"
   ```

7. **ユースケースインデックス更新と最終検証**:
   ```bash
   # 📚 ビジョン情報でユースケースインデックスを更新
   use_cases_index="docs/use_cases/index.md"
   
   echo "📚 ユースケースインデックス更新中..."
   
   # ユースケースインデックスを作成または更新
   if [[ -f "$use_cases_index" ]]; then
       # 既存ファイルをバックアップ
       backup_file="${use_cases_index}.backup.$(date +%Y%m%d_%H%M%S)"
       if ! cp "$use_cases_index" "$backup_file"; then
           echo "エラー: インデックスファイルのバックアップ作成に失敗しました"
           execute_rollback "index_backup_failed"
           exit 1
       fi
       add_rollback "mv '$backup_file' '$use_cases_index'" "Restore index backup"
       
       # ビジョンセクションを追加
       temp_file="${use_cases_index}.tmp"
       if ! sed "1i\\
   # Use Case Implementation Status\\
   \\
   **プロジェクト**: $project_name\\
   **ビジョン作成**: $(date)\\
   **コアシナリオ**: [core/index.md](core/index.md)\\
   \\
   ## プロジェクトビジョン完了 ✅\\
   \\
   - ✅ ビジョンドキュメント作成: [project-vision.md](../vision/project-vision.md)\\
   - ✅ コアシナリオ定義: [core/index.md](core/index.md)\\
   - ✅ ステアリング文書作成: [steering/](../steering/)\\
   \\
   ## 次のステップ\\
   \\
   1. プロジェクト構造初期化: \`/init-project-structure\`\\
   2. スプリント計画作成: \`/sprint-planning 1\`\\
   3. 開発開始: \`/create-use-case <issue-number>\`\\
   \\
   " "$use_cases_index" > "$temp_file"; then
           echo "エラー: インデックスファイルの更新に失敗しました"
           execute_rollback "index_update_failed"
           exit 1
       fi
       
       if ! mv "$temp_file" "$use_cases_index"; then
           echo "エラー: インデックスファイルの置換に失敗しました"
           execute_rollback "index_replacement_failed"
           exit 1
       fi
   else
       # 新しいインデックスファイルを作成
       index_content="# Use Case Implementation Status

   **プロジェクト**: $project_name
   **ビジョン作成**: $(date)
   **コアシナリオ**: [core/index.md](core/index.md)

   ## プロジェクトビジョン完了 ✅

   - ✅ ビジョンドキュメント作成: [project-vision.md](../vision/project-vision.md)
   - ✅ コアシナリオ定義: [core/index.md](core/index.md)
   - ✅ ステアリング文書作成: [steering/](../steering/)

   ## 次のステップ

   1. プロジェクト構造初期化: \`/init-project-structure\`
   2. スプリント計画作成: \`/sprint-planning 1\`
   3. 開発開始: \`/create-use-case <issue-number>\`

   ## 実装ステータス

   ### Completed ✅
   - ビジョン策定とコアシナリオ定義

   ### Planned 📋
   (スプリント計画後に追加されます)

   ### In Progress 🚧
   (開発開始後に追加されます)

   ### Evolved Scenarios 🌱
   (開発中に発見された新しい要件)
   "
       
       if ! safe_create_file "$use_cases_index" "$index_content" true; then
           echo "エラー: インデックスファイルの作成に失敗しました"
           execute_rollback "index_creation_failed"
           exit 1
       fi
       
       add_rollback "rm -f '$use_cases_index'" "Remove created index file"
   fi
   
   echo "✅ ユースケースインデックス更新完了"
   
   # 🔍 最終包括検証
   echo "🔍 最終検証実行中..."
   
   created_files=(
       "$vision_file"
       "$core_index_file"
       "${steering_docs[@]}"
       "$use_cases_index"
   )
   
   # すべてのファイルが作成されたことを検証
   missing_files=()
   for file in "${created_files[@]}"; do
       if [[ ! -f "$file" ]]; then
           missing_files+=("$file")
       fi
   done
   
   if [[ ${#missing_files[@]} -gt 0 ]]; then
       echo "エラー: 以下のファイルが作成されていません:"
       printf '  - %s\n' "${missing_files[@]}"
       execute_rollback "file_validation_failed"
       exit 1
   fi
   
   # ディレクトリ構造を検証
   for dir in "${required_dirs[@]}"; do
       if [[ ! -d "$dir" ]]; then
           echo "エラー: 必要なディレクトリが存在しません: $dir"
           execute_rollback "directory_validation_failed"
           exit 1
       fi
   done
   
   echo "✅ 最終検証完了 - 全ファイルとディレクトリが正常に作成されました"
   ```

8. **変更をコミットして成功**:
   ```bash
   # 💾 ビジョン関連ファイルをすべてコミット
   echo "💾 ビジョン関連ファイルをコミット中..."
   
   commit_message="feat: create comprehensive project vision and core scenarios

   Vision Creation Summary:
   - Project: $project_name
   - Domain: $business_domain
   - Core Features: $(echo "$main_features" | tr ',' ', ')

   Created Documents:
   - $vision_file (comprehensive project vision)
   - $core_index_file (core scenarios with 80% coverage)
   - docs/steering/ (product/tech/structure policies)
   - $use_cases_index (implementation status tracking)

   Vision Components:
   - Business goals and value proposition
   - Bounded contexts and domain modeling
   - Core entities and ubiquitous language
   - Non-functional requirements
   - Success metrics and risk assessment

   Ready for:
   1. Project structure initialization (/init-project-structure)
   2. Sprint planning (/sprint-planning 1)
   3. Development workflow (/create-use-case)
   "
   
   if ! safe_git_commit "$commit_message" "${created_files[@]}"; then
       echo "エラー: コミットに失敗しました"
       execute_rollback "commit_failed"
       exit 1
   fi
   
   add_rollback "git reset --hard HEAD~1" "Undo vision creation commit"
   
   # 🎉 トランザクションコミット（成功！）
   if commit_transaction; then
       echo ""
       echo "🎉 プロジェクトビジョン作成完了!"
       echo "============================================="
       echo "📋 プロジェクト: $project_name"
       echo "🎯 ドメイン: $business_domain"
       echo "👥 ターゲット: $target_users"
       echo ""
       echo "📁 作成ファイル:"
       for file in "${created_files[@]}"; do
           echo "   - $file"
       done
       echo ""
       echo "🏗️ アーキテクチャ基盤:"
       echo "   - Bounded Context: $main_context"
       echo "   - 主要エンティティ: $main_entities"
       echo "   - コア機能: $main_features"
       echo ""
       echo "📊 品質要件:"
       echo "   - パフォーマンス: $performance_req"
       echo "   - セキュリティ: $security_req"
       echo "   - 可用性: $availability_req"
       echo ""
       echo "📋 次のステップ:"
       echo "   1. プロジェクト構造初期化: /init-project-structure"
       echo "   2. スプリント計画: /sprint-planning 1"
       echo "   3. 開発開始: 各イシューで /create-use-case <issue-number>"
       echo ""
       echo "📚 重要ドキュメント:"
       echo "   - ビジョン: $vision_file"
       echo "   - コアシナリオ: $core_index_file"
       echo "   - 実装状況: $use_cases_index"
       echo ""
       
       # 操作ログサマリーを表示
       echo "📊 操作ログサマリー:"
       show_git_operation_log | tail -2
       show_file_operation_log | tail -3
       show_transaction_log | tail -2
       
       echo ""
       echo "✅ ビジョン策定完了 - TDD/DDD開発準備完了!"
       
   else
       echo "❌ トランザクション コミット失敗"
       exit 1
   fi
   ```