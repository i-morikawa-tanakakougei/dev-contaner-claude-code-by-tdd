コアシナリオからスプリント計画を作成し、GitHub Issueを作成する

## メタデータ
- **前提条件**: プロジェクトビジョンとコアシナリオ（00-create-vision）
- **入力**: スプリント番号（必須引数）
- **出力**: 
  - `docs/sprints/sprint-X-plan.md` - スプリント計画文書
  - `docs/sprints/sprint-X-backlog.md` - GitHub Issue付きスプリントバックログ
  - スプリントチケット用に作成されたGitHub Issue
  - `docs/use_cases/index.md`をスプリントステータスで更新
- **依存関係**: GitHub CLI（`gh`）、Git設定
- **実行タイミング**: 各スプリントサイクルで呼び出される（反復的）

## 🎯 **TDD/DDD/レイヤードプロセスコンテキスト**

**🔄 コアワークフロー**: ビジョン(00) → 構造(01) → スプリント(02) → ユースケース(03) → ドメイン(04) → テスト(05) → ドメイン(06) → アプリ(07) → インフラ(08) → UI(09) → テスト(10) → リファクタ(11) → 進化(12) → レビュー(13) → フィードバック(14) → PR(15) → ステータス(16)

**🎨 アーキテクチャ**: クリーンアーキテクチャ（ドメイン→アプリケーション→インフラストラクチャ→プレゼンテーション）  
**🧪 開発**: テスト駆動開発（RED→GREEN→REFACTOR）  
**🏗️ 設計**: ドメイン駆動設計（エンティティ、値オブジェクト、集約、リポジトリ）  
**📋 要件**: 完全なトレーサビリティを持つGiven-When-Thenシナリオ  
**🔄 進化**: /evolve-scenariosコマンドによる継続的シナリオ進化

> 📖 **文書管理システム**: [README.md](./README.md)  
> 🗺️ **現在位置**: 反復的スプリント計画（02/16） - 各スプリントサイクルで呼び出される  
> 🎯 **フェーズ目的**: 進捗分析とバックログ調整による継続的スプリント計画  
> ⬅️ **前のステージ**: 01-init-project-structure（プロジェクト構造）  
> ➡️ **次のステージ**: 03-create-use-case（ユースケース仕様）
>
> **📋 3層アーキテクチャ操作**:  
> - 🎯 **戦略的**: `docs/use_cases/core/index.md`（コアシナリオ読み取り）  
> - 📊 **戦術的**: `docs/use_cases/index.md`（実装ロードマップ作成）  
> - 🔧 **実行**: `docs/sprints/sprint-X-backlog.md`（スプリントバックログ作成）

## よくあるエラーと解決策

### ❌ エラーケース1: コアシナリオが見つからない
**原因**: `docs/use_cases/core/index.md`ファイルが存在しないか空である  
**解決策**: 
- まず`/create-vision`コマンドを実行してプロジェクトビジョンを確立する
- コアシナリオが番号付きシナリオで適切にフォーマットされていることを確認する

### ❌ エラーケース2: GitHub CLI が設定されていない
**原因**: `gh`コマンドが認証されていないか、リポジトリがリンクされていない  
**解決策**: 
```bash
gh auth login
gh repo set-default <your-repo>
```

### ❌ エラーケース3: スプリントが既に存在する
**原因**: このスプリント番号のスプリント計画ファイルが既に存在する  
**解決策**: 
- 既存の計画を上書きすることを選択する（プロンプトで`y`を入力）
- 新しい計画には異なるスプリント番号を使用する

## 実行例

### ✅ 成功例
```bash
$ /sprint-planning 1
📋 スプリント1 の計画を作成します
📖 コアシナリオとビジョン文書の確認中...
  ✅ コアシナリオファイル確認: docs/use_cases/core/index.md
  📋 コアシナリオ抽出中...
  ✅ 5 個のコアシナリオを発見
📝 スプリント計画文書作成中...
🎫 GitHub イシュー作成中...
  📋 作成中: プロジェクト基盤セットアップ
    ✅ イシュー #15 作成完了
  📋 作成中: ドメインモデル設計
    ✅ イシュー #16 作成完了
[...]
🎉 スプリント1 計画完了!
```

### ❌ 失敗例と修正
```bash
$ /sprint-planning
エラー: スプリント番号を1つだけ指定してください
使用例: /sprint-planning 1 (スプリント1の計画作成)

# 修正: スプリント番号を提供
$ /sprint-planning 1
```

## 📋 **フェーズ目的: スプリント計画のみ**

**⚠️ 重要な注意:**
- **このステップは計画のみ** - GitHub Issueとスプリントバックログを作成
- **機能実装なし** - シナリオをチケットに分解することに集中  
- **計画フェーズ** - ビジョンシナリオを実行可能なGitHub Issueに変換
- **計画文書のみ作成** - コード実装なし

**このステップの内容:**
1. `00-create-vision` ← ビジョン文書とコアシナリオ
2. `01-init-project-structure` ← プロジェクト構造とツール設定
3. `02-sprint-planning` ← **【現在位置】スプリント計画とGitHub Issue**
4. `03-create-use-case` ← Issue毎の詳細仕様
5. その後TDD/DDD実装サイクル開始

**スプリント計画とGitHub Issueのみを作成します。**

## 📋 **スプリント計画タスクチェックリスト**

**反復的で継続的なスプリント計画にこのチェックリストを使用してください:**

### 🔴 必須タスク

#### **📊 スプリント進捗分析**
- [ ] **完了したIssueをレビュー**: 前回の計画以降に完了とマークされたGitHub Issueを分析
- [ ] **実際のベロシティを計算**: 計画対実際のストーリーポイント/Issue数を比較
- [ ] **チーム能力を評価**: 現在のチームの可用性と能力の変化を評価

#### **📈 次スプリント計画**
- [ ] **スプリントゴールを定義**: 今後のスプリント反復に向けた明確で測定可能な目標
- [ ] **スプリントバックログアイテムを選択**: 能力、依存関係、優先度に基づいてIssueを選択
- [ ] **不足しているGitHub Issueを作成**: 実装が必要な新しいシナリオ用のIssueを生成
- [ ] **スプリントタイムラインを設定**: 反復期間、マイルストーン、レビュー日を定義

### 🟡 推奨タスク

#### **🌱 新しいシナリオの統合**
- [ ] **進化したシナリオをスキャン**: 新しいシナリオファイルのために`docs/use_cases/evolved/`をチェック
- [ ] **メタデータの進化をレビュー**: すべてのissue-X-Y.jsonファイルから`scenario_evolution`を抽出
- [ ] **スプリント文書を解析**: 新しく発見された要件について`docs/sprints/`をチェック
- [ ] **GitHub Issue コメントをレビュー**: Issue議論で言及された新しいシナリオを抽出
- [ ] **シナリオの完全性を検証**: 発見されたすべてのシナリオが適切なGiven-When-Then形式であることを確認

#### **🔄 バックログの再優先順位付け**
- [ ] **新しいものと既存のものをマージ**: 進化したシナリオを現在のプロダクトバックログに統合
- [ ] **ビジネス価値を再評価**: 新しい学習と市場フィードバックに基づいて優先度を調整
- [ ] **技術的複雑性を更新**: 最近の実装経験に基づいて見積もりを改良
- [ ] **シナリオ競合を解決**: 重複または競合する要件に対処
- [ ] **依存関係を検証**: バックログで適切な前提条件の順序を確保

### 🟢 オプションタスク

#### **📚 文書化とコミュニケーション**
- [ ] **学んだ教訓を文書化**: 見積もり、障害、プロセスに関する洞察を記録
- [ ] **既存のIssueを更新**: 説明、受け入れ基準、見積もりを改良
- [ ] **プロダクトロードマップを更新**: プロジェクト全体のタイムラインとスコープの変更を反映
- [ ] **ユースケースインデックスを更新**: 戦術レベルのステータスを新しいスプリント計画と同期
- [ ] **ステークホルダーに連絡**: チームとビジネスステークホルダーに計画調整を通知
- [ ] **開発の準備**: 選択されたIssueが/create-use-caseワークフローの準備ができていることを確認

**💡 プロTip**: このチェックリストを実際のアジャイルプロジェクトで使用するためにコピーしてください！

## タスク詳細

1. **安全な環境設定と引数解析**:
   ```bash
   # 🔧 すべての安全操作機能を読み込み
   source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "02-sprint-planning" "$ARGUMENTS"
   
   # スプリント計画は、other_argsに正確に1つの引数（スプリント番号）を期待します
   if [[ ${#other_args[@]} -ne 1 ]]; then
       echo "エラー: スプリント番号を1つだけ指定してください"
       show_usage_example "sprint-planning" "1" "スプリント1の計画作成"
       show_usage_example "sprint-planning" "2" "スプリント2の計画作成"
       exit 1
   fi
   
   # Issue番号はスプリント計画では使用されません
   if [[ ${#issue_numbers[@]} -gt 0 ]]; then
       echo "エラー: スプリント計画にはスプリント番号のみを指定してください（イシュー番号は不要）"
       echo "指定されたイシュー番号: ${issue_numbers[*]}"
       show_usage_example "sprint-planning" "1" "スプリント1の計画作成"
       exit 1
   fi
   
   # スプリント番号が数値であることを検証
   sprint_number="${other_args[0]}"
   if ! [[ "$sprint_number" =~ ^[0-9]+$ ]]; then
       echo "エラー: スプリント番号は数値である必要があります: $sprint_number"
       exit 1
   fi
   
   if [[ "$sprint_number" -eq 0 ]]; then
       echo "エラー: スプリント番号は1以上である必要があります"
       exit 1
   fi
   
   echo "📋 スプリント$sprint_number の計画を作成します"
   ```

2. **トランザクション開始と事前検証**:
   ```bash
   # 🔄 包括的トランザクションを開始
   if ! begin_transaction "sprint_planning_$sprint_number"; then
       echo "エラー: トランザクションの開始に失敗しました"
       exit 1
   fi
   
   # 🔍 スプリントが既に存在するかチェック
   sprint_plan_file="docs/sprints/sprint-$sprint_number-plan.md"
   sprint_backlog_file="docs/sprints/sprint-$sprint_number-backlog.md"
   
   if [[ -f "$sprint_plan_file" ]]; then
       echo "⚠️  スプリント$sprint_number の計画が既に存在します: $sprint_plan_file"
       echo "既存の計画を上書きしますか？ (y/N): "
       read -n 1 -r
       echo
       if [[ ! $REPLY =~ ^[Yy]$ ]]; then
           echo "スプリント計画をキャンセルしました"
           commit_transaction
           exit 0
       fi
       
       # 既存計画をバックアップ
       backup_file="${sprint_plan_file}.backup.$(date +%Y%m%d_%H%M%S)"
       if ! safe_move_file "$sprint_plan_file" "$backup_file" false; then
           echo "エラー: 既存計画のバックアップに失敗しました"
           execute_rollback "backup_failed"
           exit 1
       fi
       add_rollback "mv '$backup_file' '$sprint_plan_file'" "Restore sprint plan backup"
   fi
   
   # 📊 必要に応じてsprintsディレクトリを作成
   if ! safe_mkdir "docs/sprints"; then
       echo "エラー: スプリントディレクトリの作成に失敗しました"
       execute_rollback "sprints_dir_creation_failed"
       exit 1
   fi
   ```

3. **コアシナリオとビジョンのレビュー**:
   ```bash
   # 📖 コアシナリオとビジョン文書をレビュー
   echo "📖 コアシナリオとビジョン文書の確認中..."
   
   core_scenarios_file="docs/use_cases/core/index.md"
   vision_file="docs/vision/project-vision.md"
   
   # コアシナリオをチェック
   if [[ -f "$core_scenarios_file" ]]; then
       if ! check_file_permissions "$core_scenarios_file" "read"; then
           echo "エラー: コアシナリオファイルの読み取り権限がありません: $core_scenarios_file"
           execute_rollback "core_scenarios_access_failed"
           exit 1
       fi
       echo "  ✅ コアシナリオファイル確認: $core_scenarios_file"
       
       # コアインデックスからシナリオを抽出
       echo "  📋 コアシナリオ抽出中..."
       core_scenarios=$(grep -E "^[0-9]+\.\s+\*\*" "$core_scenarios_file" 2>/dev/null || echo "")
       if [[ -z "$core_scenarios" ]]; then
           echo "  ⚠️  コアシナリオが見つかりませんでした（フォーマット: '1. **Scenario Name**'）"
       else
           echo "  ✅ $(echo "$core_scenarios" | wc -l) 個のコアシナリオを発見"
       fi
   else
       echo "  ⚠️  コアシナリオファイルが存在しません: $core_scenarios_file"
       echo "  💡 /create-vision コマンドでビジョンとコアシナリオを最初に作成することを推奨します"
       core_scenarios=""
   fi
   
   # ビジョン文書をチェック
   if [[ -f "$vision_file" ]]; then
       if ! check_file_permissions "$vision_file" "read"; then
           echo "エラー: ビジョンファイルの読み取り権限がありません: $vision_file"
           execute_rollback "vision_access_failed"
           exit 1
       fi
       echo "  ✅ ビジョンファイル確認: $vision_file"
       
       # プロジェクトゴールを抽出
       project_goals=$(grep -A 5 "## 概要\|## Goals\|## ゴール" "$vision_file" 2>/dev/null | tail -n +2 || echo "")
   else
       echo "  ⚠️  ビジョンファイルが存在しません: $vision_file"
       echo "  💡 /create-vision コマンドでプロジェクトビジョンを最初に作成することを推奨します"
       project_goals=""
   fi
   ```

4. **スプリント計画文書の作成**:
   ```bash
   # 📝 包括的スプリント計画を作成
   echo "📝 スプリント計画文書作成中..."
   
   # スプリント番号に基づいてスプリントゴールを生成
   case "$sprint_number" in
       1)
           sprint_goal="プロジェクト基盤構築とコアドメインモデル設計"
           priority_focus="MVP機能の基盤となるコア機能に集中"
           ;;
       2)
           sprint_goal="主要機能の実装とAPI設計"
           priority_focus="ユーザー価値の高い機能を優先"
           ;;
       3)
           sprint_goal="統合テストと品質向上"
           priority_focus="安定性とパフォーマンスの確保"
           ;;
       *)
           sprint_goal="継続的な機能追加と改善"
           priority_focus="ユーザーフィードバックに基づく優先順位"
           ;;
   esac
   
   # スプリント計画内容を作成
   sprint_plan_content="# スプリント$sprint_number 計画

**作成日時**: $(date)
**計画期間**: $(date -d '+14 days' '+%Y-%m-%d') まで（2週間）

## スプリントゴール
$sprint_goal

## 優先順位の方針
$priority_focus

## プロジェクト概要
$(if [[ -n "$project_goals" ]]; then
    echo "$project_goals"
else
    echo "- TDD/DDD/レイヤードアーキテクチャによる高品質なソフトウェア開発"
    echo "- ビジネス価値の高い機能を段階的に提供"
    echo "- 継続的な品質向上とテスト駆動開発"
fi)

## 選択されたコアシナリオ

$(if [[ -n "$core_scenarios" ]]; then
    echo "$core_scenarios" | head -5 | sed 's/^/### /' | sed 's/\*\*//'
    echo ""
    echo "> **注**: 上記はコアシナリオから自動抽出されました。"
    echo "> 実際の優先順位は開発チームで調整してください。"
else
    echo "### 1. 基盤機能の実装
- **理由**: プロジェクトの基礎となる機能
- **価値**: 後続機能の基盤となる

### 2. コアドメインモデルの設計
- **理由**: ビジネスロジックの中心
- **価値**: ドメインエキスパートとの共通理解

### 3. 基本的なCRUD操作
- **理由**: 最小限の動作確認
- **価値**: エンドツーエンドの動作検証

> **注**: コアシナリオファイルが見つからないため、標準的なシナリオを生成しました。
> /create-vision コマンドでプロジェクト固有のシナリオを作成することを推奨します。"
fi)

## チケット一覧

以下のチケットをGitHubイシューとして作成します：

### チケット1: プロジェクト基盤セットアップ
- **タイプ**: Epic/Setup
- **説明**: TDD/DDD/レイヤードアーキテクチャの基盤構築
- **受け入れ基準**:
  - Given: 空のリポジトリがある
  - When: プロジェクト構造を初期化する
  - Then: 適切なディレクトリ構造とツールチェーンが設定される
- **推定**: 3 Story Points
- **優先度**: Highest
- **依存関係**: なし

### チケット2: ドメインモデル設計
- **タイプ**: Feature/Design
- **説明**: コアドメインエンティティと値オブジェクトの設計
- **受け入れ基準**:
  - Given: ビジネス要件が明確化されている
  - When: ドメインモデルを設計する
  - Then: エンティティ、値オブジェクト、ドメインサービスが定義される
- **推定**: 5 Story Points
- **優先度**: High
- **依存関係**: チケット1

### チケット3: ユースケース実装
- **タイプ**: Feature/Implementation
- **説明**: アプリケーション層のユースケース実装
- **受け入れ基準**:
  - Given: ドメインモデルが定義されている
  - When: ユースケースを実装する
  - Then: ビジネスロジックがアプリケーション層で orchestrate される
- **推定**: 8 Story Points
- **優先度**: High
- **依存関係**: チケット2

### チケット4: API エンドポイント実装
- **タイプ**: Feature/Implementation
- **説明**: プレゼンテーション層のREST API実装
- **受け入れ基準**:
  - Given: ユースケースが実装されている
  - When: API エンドポイントを実装する
  - Then: 外部からユースケースを呼び出せる
- **推定**: 5 Story Points
- **優先度**: Medium
- **依存関係**: チケット3

### チケット5: データ永続化機能
- **タイプ**: Feature/Implementation
- **説明**: インフラ層のリポジトリパターン実装
- **受け入れ基準**:
  - Given: ドメインリポジトリインターフェースが定義されている
  - When: 永続化機能を実装する
  - Then: データの保存・取得ができる
- **推定**: 8 Story Points
- **優先度**: Medium
- **依存関係**: チケット2

## 実装順序

### Week 1 (第1週)
1. **チケット1** (プロジェクト基盤) - 1-2日
2. **チケット2** (ドメインモデル設計) - 2-3日

### Week 2 (第2週)
1. **チケット3** (ユースケース実装) - 3-4日
2. **チケット4** (API実装) - 2日
3. **チケット5** (データ永続化) - 2-3日

## 定義・見積もり

### Story Points基準
- **1 Point**: 半日程度の作業
- **3 Points**: 1日程度の作業
- **5 Points**: 2-3日程度の作業
- **8 Points**: 1週間程度の作業
- **13 Points**: 大きすぎるため分割が必要

## リスクと軽減策

### 技術的リスク
- **リスク**: DDD実装パターンの学習コスト
  - **軽減策**: ペアプログラミングと定期的なコードレビュー
  - **影響**: 実装速度の一時的な低下

- **リスク**: TDDサイクルに慣れるまでの時間
  - **軽減策**: 小さなタスクから始めて段階的に習熟
  - **影響**: 初期の生産性低下

### プロジェクトリスク
- **リスク**: 要件の変更や追加
  - **軽減策**: アジャイルプロセスでの継続的なフィードバック
  - **影響**: スコープ調整の必要性

- **リスク**: チーム間のコミュニケーション不足
  - **軽減策**: 定期的なスタンドアップと振り返り
  - **影響**: 開発の方向性のズレ

## 成功指標

### 品質指標
- ✅ 全テストが通る（テストカバレッジ 80%以上）
- ✅ アーキテクチャ違反がない
- ✅ コードレビューが完了している

### 機能指標
- ✅ 計画されたチケットの80%以上が完了
- ✅ 各レイヤーが適切に分離されている
- ✅ エンドツーエンドのシナリオが動作する

### プロセス指標
- ✅ TDDサイクル（RED-GREEN-REFACTOR）が回っている
- ✅ 定期的なふりかえりが実施されている
- ✅ 継続的インテグレーションが動作している

## ふりかえり予定

- **Daily**: 毎日15分のスタンドアップ
- **Weekly**: 毎週金曜日の進捗確認
- **Sprint End**: スプリント終了時の包括的ふりかえり

## 次スプリントへの準備

- 未完了チケットの評価と優先順位調整
- 新しい要件・課題の整理
- チーム学習事項の共有

---

**作成者**: $(git config user.name || echo "Unknown")
**スプリント管理**: GitHub Issues + Project Board
**更新履歴**: [スプリント$sprint_number バックログ](sprint-$sprint_number-backlog.md)
"
   
   # スプリント計画ファイルを安全に作成
   if ! safe_create_file "$sprint_plan_file" "$sprint_plan_content" true; then
       echo "エラー: スプリント計画ファイルの作成に失敗しました"
       execute_rollback "sprint_plan_creation_failed"
       exit 1
   fi
   
   add_rollback "rm -f '$sprint_plan_file'" "Remove created sprint plan"
   echo "✅ スプリント計画文書作成完了: $sprint_plan_file"
   ```

5. **GitHub Issueの安全な作成**:
   ```bash
   # 🎫 スプリントチケット用のGitHub Issueを作成
   echo "🎫 GitHub イシュー作成中..."
   
   # 作成するチケットを定義
   declare -A tickets=(
       ["setup"]="プロジェクト基盤セットアップ|TDD/DDD/レイヤードアーキテクチャの基盤構築とツールチェーン設定|setup,foundation"
       ["domain"]="ドメインモデル設計|コアドメインエンティティ、値オブジェクト、ドメインサービスの設計|domain,design"
       ["usecase"]="ユースケース実装|アプリケーション層のユースケース実装とビジネスロジック orchestration|application,usecase"
       ["api"]="API エンドポイント実装|プレゼンテーション層のREST API実装とコントローラー作成|api,presentation"
       ["persistence"]="データ永続化機能|インフラ層のリポジトリパターン実装とデータアクセス|infrastructure,persistence"
   )
   
   created_issues=()
   
   for ticket_key in "setup" "domain" "usecase" "api" "persistence"; do
       IFS='|' read -ra ticket_info <<< "${tickets[$ticket_key]}"
       ticket_title="${ticket_info[0]}"
       ticket_description="${ticket_info[1]}"
       ticket_labels="${ticket_info[2]}"
       
       echo "  📋 作成中: $ticket_title"
       
       # 詳細なIssue本文を作成
       issue_body="## 概要
$ticket_description

## 受け入れ基準

### $ticket_title の場合:
$(case "$ticket_key" in
    "setup")
        echo "- [ ] プロジェクト構造が初期化されている
- [ ] 必要な依存関係がインストールされている
- [ ] CI/CDパイプラインが設定されている
- [ ] 開発環境が正常に動作する"
        ;;
    "domain")
        echo "- [ ] ドメインエンティティが定義されている
- [ ] 値オブジェクトが適切に実装されている
- [ ] ドメインサービスが必要に応じて作成されている
- [ ] ドメインモデルのテストが作成されている"
        ;;
    "usecase")
        echo "- [ ] ユースケースクラスが実装されている
- [ ] DTOが適切に定義されている
- [ ] ビジネスルールが正しく実装されている
- [ ] ユースケースのテストが作成されている"
        ;;
    "api")
        echo "- [ ] REST API エンドポイントが実装されている
- [ ] バリデーションが適切に設定されている
- [ ] エラーハンドリングが実装されている
- [ ] API ドキュメントが更新されている"
        ;;
    "persistence")
        echo "- [ ] リポジトリインターフェースが実装されている
- [ ] データマッパーが作成されている
- [ ] データベース接続が設定されている
- [ ] 永続化テストが作成されている"
        ;;
esac)

## アーキテクチャ要件

- [ ] レイヤー分離が適切に維持されている
- [ ] 依存関係の方向が正しい（外側 → 内側のみ）
- [ ] ドメイン層に外部依存がない
- [ ] アーキテクチャ検証テストが通る

## テスト要件

- [ ] 単体テストが作成されている（カバレッジ80%以上）
- [ ] 統合テストが必要に応じて作成されている
- [ ] TDDサイクル（RED-GREEN-REFACTOR）が実施されている
- [ ] 全テストが通る

## ドキュメント要件

- [ ] 実装仕様書が更新されている
- [ ] APIドキュメント（該当する場合）が更新されている
- [ ] コードコメントが適切に記述されている

## Definition of Done

- [ ] 機能が完全に実装されている
- [ ] 全テストが通る
- [ ] コードレビューが完了している
- [ ] ドキュメントが更新されている
- [ ] アーキテクチャ検証が通る

---

**スプリント**: Sprint $sprint_number
**推定**: $(case "$ticket_key" in
    "setup") echo "3 Story Points" ;;
    "domain") echo "5 Story Points" ;;
    "usecase") echo "8 Story Points" ;;
    "api") echo "5 Story Points" ;;
    "persistence") echo "8 Story Points" ;;
esac)
**優先度**: $(case "$ticket_key" in
    "setup") echo "Highest" ;;
    "domain") echo "High" ;;
    "usecase") echo "High" ;;
    "api") echo "Medium" ;;
    "persistence") echo "Medium" ;;
esac)
**関連文書**: [スプリント$sprint_number 計画](docs/sprints/sprint-$sprint_number-plan.md)
"
       
       # GitHub Issueを安全に作成
       if issue_number=$(safe_create_issue "$ticket_title" "$issue_body" "$ticket_labels"); then
           created_issues+=("#$issue_number")
           echo "    ✅ イシュー #$issue_number 作成完了"
           
           # TDD/DDDガイダンス付きコメントを追加
           guidance_comment="🎯 **TDD/DDD開発ガイダンス**

このイシューを開発する際は、以下の手順を推奨します：

## TDD サイクル
1. **RED**: まずテストを書く（失敗することを確認）
2. **GREEN**: 最小限の実装でテストを通す
3. **REFACTOR**: コードを改善・整理する

## DDD アプローチ
- ユビキタス言語を使用してコード・ドキュメントを記述
- ビジネスロジックはドメイン層に集約
- 技術的関心事とビジネス関心事を分離

## レイヤード アーキテクチャ
- **Domain**: ビジネスルール、エンティティ、値オブジェクト
- **Application**: ユースケース、アプリケーションサービス
- **Infrastructure**: データアクセス、外部API連携
- **Presentation**: コントローラー、API エンドポイント

## 開発開始コマンド
\`\`\`bash
/create-use-case $issue_number
\`\`\`

📋 **次のステップ**: 上記コマンドでユースケース仕様を作成してから実装を開始してください。
"
           
           if ! safe_add_issue_comment "$issue_number" "$guidance_comment"; then
               echo "    ⚠️  ガイダンスコメントの追加に失敗しました（続行します）"
           fi
           
       else
           echo "    ❌ イシュー作成に失敗しました: $ticket_title"
           execute_rollback "issue_creation_failed"
           exit 1
       fi
   done
   
   echo "✅ GitHub イシュー作成完了: ${#created_issues[@]} 個のイシューを作成"
   ```

6. **スプリントバックログ作成とインデックス更新**:
   ```bash
   # 📋 スプリントバックログ文書を作成
   echo "📋 スプリントバックログ作成中..."
   
   backlog_content="# スプリント$sprint_number バックログ

**更新日時**: $(date)
**スプリント期間**: $(date) ～ $(date -d '+14 days')

## 作成されたイシュー

$(for issue in "${created_issues[@]}"; do
    echo "- $issue"
done)

## イシューリンク

$(for i in "${!created_issues[@]}"; do
    issue_num="${created_issues[$i]#\#}"
    ticket_keys=("setup" "domain" "usecase" "api" "persistence")
    ticket_key="${ticket_keys[$i]}"
    ticket_info="${tickets[$ticket_key]}"
    IFS='|' read -ra info <<< "$ticket_info"
    echo "### ${info[0]} ($issue_num)"
    echo "- **GitHub**: [イシュー#$issue_num](https://github.com/$(git config --get remote.origin.url | sed 's/.*github.com[\/:]//;s/\.git$//')/issues/$issue_num)"
    echo "- **説明**: ${info[1]}"
    echo "- **ラベル**: ${info[2]}"
    echo ""
done)

## 進捗管理

### Week 1
- [ ] $(echo "${created_issues[0]}" | sed 's/#/Issue #/') - プロジェクト基盤セットアップ
- [ ] $(echo "${created_issues[1]}" | sed 's/#/Issue #/') - ドメインモデル設計

### Week 2  
- [ ] $(echo "${created_issues[2]}" | sed 's/#/Issue #/') - ユースケース実装
- [ ] $(echo "${created_issues[3]}" | sed 's/#/Issue #/') - API エンドポイント実装
- [ ] $(echo "${created_issues[4]}" | sed 's/#/Issue #/') - データ永続化機能

## 開発フロー

各イシューは以下のコマンドで開発を開始します：

\`\`\`bash
# 1. ユースケース仕様作成
/create-use-case <issue-number> <feature-name>

# 2. ドメインモデル設計
/domain-modeling <issue-number>

# 3. TDD実装サイクル
/create-tests <issue-number>
/implement-domain <issue-number>
/implement-usecase <issue-number>
/implement-infra <issue-number>
/implement-presentation <issue-number>

# 4. テスト・リファクタリング
/run-all-tests <issue-number>
/refactor <issue-number>

# 5. レビュー・PR作成
/review-issue <issue-number>
/create-pr <issue-number>
\`\`\`

## 定期確認

- **Daily Standup**: 毎朝9:00
- **Weekly Review**: 毎週金曜日
- **Sprint Review**: スプリント終了時
- **Retrospective**: スプリント終了後

## メトリクス追跡

- **Velocity**: 完了Story Points / Sprint
- **Burndown**: 残りStory Points推移
- **Quality**: テストカバレッジ、バグ数
- **Architecture**: アーキテクチャ違反数

---

**Next Sprint Planning**: $(date -d '+14 days')
**Created Issues**: ${#created_issues[@]}
**Total Story Points**: 29 Points
"
   
   if ! safe_create_file "$sprint_backlog_file" "$backlog_content" true; then
       echo "エラー: スプリントバックログファイルの作成に失敗しました"
       execute_rollback "backlog_creation_failed"
       exit 1
   fi
   
   add_rollback "rm -f '$sprint_backlog_file'" "Remove created sprint backlog"
   
   # スプリント情報でユースケースインデックスを更新
   use_cases_index="docs/use_cases/index.md"
   if [[ -f "$use_cases_index" ]]; then
       echo "📚 ユースケースインデックス更新中..."
       
       # バックアップを作成
       backup_file="${use_cases_index}.backup.$(date +%Y%m%d_%H%M%S)"
       if ! cp "$use_cases_index" "$backup_file"; then
           echo "エラー: インデックスファイルのバックアップ作成に失敗しました"
           execute_rollback "index_backup_failed"
           exit 1
       fi
       
       add_rollback "mv '$backup_file' '$use_cases_index'" "Restore index backup"
       
       # スプリント計画エントリを追加
       temp_file="${use_cases_index}.tmp"
       if ! sed "/## Planned 📋/a\\
\\
### スプリント$sprint_number 計画済み\\
$(for issue in "${created_issues[@]}"; do echo "- $issue"; done | sed 's/^//')\\
\\
**計画文書**: [sprint-$sprint_number-plan.md](../sprints/sprint-$sprint_number-plan.md)  \\
**バックログ**: [sprint-$sprint_number-backlog.md](../sprints/sprint-$sprint_number-backlog.md)  \\
**作成日**: $(date)  " "$use_cases_index" > "$temp_file"; then
           echo "エラー: インデックスファイルの更新に失敗しました"
           execute_rollback "index_update_failed"
           exit 1
       fi
       
       if ! mv "$temp_file" "$use_cases_index"; then
           echo "エラー: インデックスファイルの置換に失敗しました"
           execute_rollback "index_replacement_failed"
           exit 1
       fi
       
       echo "✅ ユースケースインデックス更新完了"
   fi
   ```

7. **最終コミットと成功**:
   ```bash
   # 💾 すべてのスプリント計画成果物をコミット
   echo "💾 スプリント計画をコミット中..."
   
   commit_message="feat: create sprint $sprint_number planning and GitHub issues

Sprint Planning Summary:
- Sprint Goal: $sprint_goal
- Created Issues: ${#created_issues[@]} tickets
- Total Story Points: 29 points
- Sprint Duration: 2 weeks

Created Files:
- $sprint_plan_file (comprehensive sprint plan)
- $sprint_backlog_file (GitHub issues backlog)
- Updated $use_cases_index (sprint planning status)

GitHub Issues Created:
$(for issue in "${created_issues[@]}"; do echo "  - $issue"; done)

Ready for development workflow with TDD/DDD/Layered Architecture.
"
   
   files_to_commit=("$sprint_plan_file" "$sprint_backlog_file")
   if [[ -f "$use_cases_index" ]]; then
       files_to_commit+=("$use_cases_index")
   fi
   
   if ! safe_git_commit "$commit_message" "${files_to_commit[@]}"; then
       echo "エラー: コミットに失敗しました"
       execute_rollback "commit_failed"
       exit 1
   fi
   
   add_rollback "git reset --hard HEAD~1" "Undo sprint planning commit"
   
   # 🎉 トランザクションコミット（成功！）
   if commit_transaction; then
       echo ""
       echo "🎉 スプリント$sprint_number 計画完了!"
       echo "============================================="
       echo "📋 作成されたイシュー: ${#created_issues[@]} 個"
       echo "📊 総Story Points: 29 points"
       echo "⏱️  スプリント期間: 2週間"
       echo ""
       echo "📁 作成ファイル:"
       echo "   - $sprint_plan_file"
       echo "   - $sprint_backlog_file"
       echo ""
       echo "🎫 GitHub イシュー:"
       for issue in "${created_issues[@]}"; do
           echo "   - $issue"
       done
       echo ""
       echo "🚀 開発フロー:"
       echo "   1. 各イシューでユースケース仕様作成: /create-use-case <issue-number>"
       echo "   2. TDD/DDD開発サイクル実行"
       echo "   3. レビュー・PR作成・マージ"
       echo ""
       echo "📋 次のコマンド例:"
       if [[ ${#created_issues[@]} -gt 0 ]]; then
           first_issue="${created_issues[0]#\#}"
           echo "   /create-use-case $first_issue project-setup"
       fi
       echo ""
       
       # 操作ログサマリーを表示
       echo "📊 操作ログサマリー:"
       show_github_operation_log | tail -3
       show_git_operation_log | tail -2
       show_transaction_log | tail -2
       
       echo ""
       echo "✅ スプリント計画完了 - 開発開始準備完了!"
       
   else
       echo "❌ トランザクション コミット失敗"
       exit 1
   fi
   ```