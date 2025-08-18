GitHub IssueからGiven-When-Thenユースケース仕様を作成する

## メタデータ
- **前提条件**: GitHub Issueが作成されている、Gitリポジトリが初期化されている
- **入力**: Issue番号（必須）、機能名（オプション）
- **出力**: 
  - `docs/use_cases/issue-X-Y.md` - ユースケース仕様書
  - `docs/use_cases/issue-X-Y.json` - メタデータ追跡ファイル
  - 新しいエントリで更新された`docs/use_cases/index.md`
  - フィーチャーブランチ`feature/issue-X-Y-feature-name`
- **依存関係**: GitHub CLI（`gh`）、Git設定、jq
- **実行タイミング**: スプリント計画後、ドメインモデリング前

## 🎯 **TDD/DDD/レイヤードプロセスコンテキスト**

**🔄 コアワークフロー**: ビジョン(00) → 構造(01) → スプリント(02) → スプリントレビュー(02.5) → ユースケース(03) → ドメイン(04) → 設計レビュー(04.5) → テスト(05) → テストレビュー(05.5) → ドメイン(06) → アプリ(07) → インフラ(08) → UI(09) → テスト(10) → リファクタ(11) → 進化(12) → レビュー(13) → フィードバック(14) → PR(15) → ステータス(16)

**🎨 アーキテクチャ**: クリーンアーキテクチャ（ドメイン→アプリケーション→インフラストラクチャ→プレゼンテーション）  
**🧪 開発**: テスト駆動開発（RED→GREEN→REFACTOR）  
**🏗️ 設計**: ドメイン駆動設計（エンティティ、値オブジェクト、集約、リポジトリ）  
**📋 要件**: 完全なトレーサビリティを持つGiven-When-Thenシナリオ  
**🔄 進化**: /evolve-scenariosコマンドによる継続的シナリオ進化

> 📖 **文書管理システム**: [README.md](./README.md)  
> 🗺️ **現在位置**: スプリント実行フェーズ - ユースケース仕様作成（03/16）  
> 🎯 **フェーズ目的**: GitHub IssueからGiven-When-Then仕様とメタデータを作成  
> ⬅️ **前のステージ**: 02.5-review-sprint-plan（スプリント計画レビュー）  
> ➡️ **次のステージ**: 04-domain-modeling（ドメインモデル設計）
>
> **📋 3層アーキテクチャ操作**:  
> - 🎯 **戦略的**: `docs/use_cases/core/index.md`（ビジョン整合性の参照）  
> - 📊 **戦術的**: `docs/use_cases/index.md`（新しいユースケースエントリを追加）  
> - 🔧 **実行**: `docs/use_cases/issue-X-Y.json`（詳細メタデータを作成）

## よくあるエラーと解決策

### ❌ エラーケース1: Issueが見つからない、またはアクセスできない
**原因**: 無効なIssue番号またはGitHub権限不足  
**解決策**: 
```bash
# Issueが存在しアクセス可能か確認
gh issue view <issue-number>
# GitHub認証をチェック
gh auth status
```

### ❌ エラーケース2: メタデータテンプレート検証の失敗
**原因**: 手動メタデータ作成または不完全なテンプレート  
**解決策**: 
- 常に`create_metadata_if_not_exists()`関数を使用する
- メタデータJSONファイルを手動で作成しない
- テンプレートに必要なすべてのフェーズが存在することを確認する

### ❌ エラーケース3: フィーチャーブランチ作成の失敗
**原因**: ブランチ名の競合またはGit権限の問題  
**解決策**: 
```bash
# 既存ブランチをチェック
git branch -a
# 作業ディレクトリがクリーンであることを確認
git status
```

## 実行例

### ✅ 成功例
```bash
$ /create-use-case 15 user-management
📋 イシュー #15 からユースケース仕様作成を開始します
🌿 フィーチャーブランチ作成: feature/issue-15-user-management
📋 全イシューの詳細取得と検証中...
=== Issue #15 ===
タイトル: ユーザー管理機能の実装
状態: open
📊 メタデータファイル作成: docs/use_cases/issue-15-user-management.json
✅ 正式メタデータテンプレート確認完了
📄 ユースケース仕様ファイル作成: docs/use_cases/issue-15-user-management.md
📚 インデックスファイル更新: docs/use_cases/index.md
🎉 ユースケース仕様作成完了!
```

### ❌ 失敗例と修正
```bash
$ /create-use-case
エラー: 最低1つのイシュー番号が必要です
使用例: /create-use-case 1 (単一イシューからユースケース仕様作成)

# 修正: Issue番号を提供
$ /create-use-case 15
```

## 📖 **フェーズ目的: 仕様作成のみ**

**⚠️ 重要な注意:**
- **このステップは仕様作成のみ** - Given-When-Thenユースケース仕様を作成
- **機能実装なし** - 詳細な要件文書化に集中  
- **要件フェーズ** - GitHub Issueを詳細仕様に変換
- **仕様文書のみ作成** - コード実装なし

**TDD/DDDフロー位置:**
1. `02-sprint-planning` ← GitHub Issue作成
2. `03-create-use-case` ← **【現在位置】仕様作成**
3. `04-domain-modeling` ← 設計文書化
4. `05-create-tests` ← TDD RED（失敗テスト）
5. `06-implement-domain` ← TDD GREEN（実装）

**仕様とメタデータのみ作成します。**

## 📋 **ユースケース仕様タスクチェックリスト**

**GitHub Issueを詳細仕様に変換するためにこのチェックリストを使用してください:**

### 🔴 必須タスク

#### **🎫 GitHub Issue分析**
- [ ] **Issue詳細を取得**: GitHub APIからタイトル、説明、ラベル、担当者、マイルストーンを取得
- [ ] **Issue要件を解析**: Issue説明から機能要件を抽出
- [ ] **受け入れ基準を特定**: テスト可能な受け入れ基準を見つけるか推論
- [ ] **ビジネスコンテキストを抽出**: ビジネス価値とユーザーのモチベーションを理解

#### **📝 Given-When-Then仕様作成**
- [ ] **メインシナリオを記述**: Issue要件から主要なGiven-When-Thenシナリオを作成
- [ ] **エラーシナリオを追加**: Issue制約に基づいてエラーハンドリングシナリオを作成
- [ ] **前提条件を定義**: シナリオ実行前のシステム状態要件を指定
- [ ] **事後条件を定義**: 正常実行後の期待されるシステム状態を指定

#### **📊 メタデータとプロジェクト統合**
- [ ] **Issue メタデータJSONを作成**: 包括的な追跡ファイル（issue-X-Y.json）を生成
- [ ] **GitHub Issueにリンク**: 仕様とIssue間のトレーサビリティを確保
- [ ] **ユースケースインデックスを更新**: 戦術レベル追跡文書にエントリを追加
- [ ] **実装準備状況を設定**: ドメインモデリングフェーズの準備完了をマーク

### 🟡 推奨タスク

#### **🔍 要件抽出と検証**
- [ ] **Issue完全性を検証**: Issueに実装のための十分な情報があることを確認
- [ ] **不足情報を特定**: 明確化が必要なギャップをフラグ（重大な場合は/evolve-scenariosを使用）
- [ ] **ユーザーストーリーを抽出**: まだユーザーストーリー形式でない場合はIssueを変換
- [ ] **スコープ境界を定義**: このIssueに含まれる/含まれないものを明確に定義
- [ ] **ビジョンとの検証**: プロジェクトビジョンとコアシナリオとの整合性を確保

#### **🏗️ ドメインコンセプト特定**
- [ ] **ビジネス用語を抽出**: Issue説明からドメイン固有の語彙を特定
- [ ] **キーコンセプトを定義**: 言及されたビジネスエンティティ、プロセス、ルールを文書化
- [ ] **ユビキタス言語にマッピング**: 既存プロジェクト語彙と用語を整合
- [ ] **ドメイン関係を特定**: エンティティ間の関係性を記録
- [ ] **新しいコンセプトをフラグ**: 現在のドメインモデルでカバーされていないコンセプトをマーク

### 🟢 オプションタスク

#### **📝 高度な仕様作成**
- [ ] **代替シナリオを追加**: Issueで言及された代替フローとエッジケースを定義
- [ ] **技術制約を記録**: Issueで言及された技術的制限を特定

#### **✅ 受け入れ基準とテストガイドライン**
- [ ] **テスト可能な基準を定義**: 要件を具体的で測定可能な基準に変換
- [ ] **テストシナリオを作成**: Given-When-Thenを将来のテスト実装にマッピング
- [ ] **検証ルールを定義**: 入力検証とビジネスルール適用を指定
- [ ] **期待される動作を文書化**: すべての期待されるシステム応答を詳細化
- [ ] **TDDの準備**: テストファースト開発をサポートする構造の基準
- [ ] **ハンドオフの準備**: /domain-modelingに必要なすべての情報が利用可能であることを確認

**💡 プロTip**: GitHub Issueでカバーされていない重大な新しいシナリオを発見した場合は、スコープを拡大するのではなく/evolve-scenariosを使用してください！

> ⚠️ **重要要件 - 正式メタデータテンプレートのみ**:
> - 🚫 **絶対に**メタデータJSONファイルを手動で作成しない
> - ✅ **常に**`_metadata_operations.sh`の`create_metadata_if_not_exists()`関数を使用
> - 🔍 **必須**完全なテンプレート構造の検証（40以上のフィールド）
> - 📊 正式テンプレートには含まれる: scenario_evolution、review、feedback_application、pull_requestフェーズ
> - ❌ 簡略化または手動メタデータファイルは検証失敗を引き起こす

## タスク詳細

1. **安全な環境設定と引数解析**:
   ```bash
   # 🔧 自動引数解析と検証ですべての安全操作機能を読み込み
   source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "03-create-use-case" "$ARGUMENTS"
   
   # 引数はセットアップスクリプトで既に解析・検証済み
   # この特定コマンド用の追加検証
   if [[ ${#issue_numbers[@]} -eq 0 ]]; then
       echo "エラー: 最低1つのイシュー番号が必要です"
       show_usage_example "create-use-case" "1" "単一イシューからユースケース仕様作成"
       show_usage_example "create-use-case" "1,7" "複数イシューからユースケース仕様作成"
       show_usage_example "create-use-case" "1,mt5-data" "イシュー1 + 機能名'mt5-data'を指定"
       exit 1
   fi
   ```

2. **トランザクション開始と開発環境準備**:
   ```bash
   # 🔄 アトミック操作のトランザクション開始
   if ! begin_transaction "create_use_case_$(IFS=-; echo "${issue_numbers[*]}")"; then
       echo "エラー: トランザクションの開始に失敗しました"
       exit 1
   fi
   
   # 📝 機能名を安全に決定
   if [[ ${#other_args[@]} -gt 0 ]]; then
       feature_name="${other_args[0]}"
   else
       # 🔍 エラーハンドリング付きで主要Issueタイトルから派生
       primary_issue="${issue_numbers[0]}"
       echo "イシュー #$primary_issue からフィーチャー名を取得中..."
       
       if ! issue_info=$(safe_get_issue_info "$primary_issue" "json"); then
           echo "エラー: イシュー #$primary_issue の情報取得に失敗しました"
           execute_rollback "issue_fetch_failed"
           exit 1
       fi
       
       feature_name=$(echo "$issue_info" | jq -r '.title' | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | sed 's/^-\|-$//g')
       
       if [[ -z "$feature_name" ]]; then
           echo "エラー: フィーチャー名の生成に失敗しました"
           execute_rollback "feature_name_generation_failed"
           exit 1
       fi
       
       echo "✅ フィーチャー名生成: $feature_name"
   fi
   
   # 🌿 ロールバック付きで安全にフィーチャーブランチを作成
   issue_list=$(IFS=-; echo "${issue_numbers[*]}")
   branch_name="feature/issue-${issue_list}-${feature_name}"
   
   echo "フィーチャーブランチ作成: $branch_name"
   if ! safe_create_or_switch_branch "$branch_name"; then
       echo "エラー: ブランチの作成/切り替えに失敗しました"
       execute_rollback "branch_creation_failed"
       exit 1
   fi
   
   # ブランチクリーンアップのロールバック操作を追加
   add_rollback "git checkout main && git branch -D '$branch_name'" "Clean up feature branch"
   ```

3. **Issueの検証とビジョン整合性チェック**:
   ```bash
   # 🔍 すべてのIssue詳細を取得・検証
   echo "📋 全イシューの詳細取得と検証中..."
   
   for issue_num in "${issue_numbers[@]}"; do
       echo "=== Issue #$issue_num ==="
       
       if ! safe_get_issue_info "$issue_num" "plain"; then
           echo "エラー: イシュー #$issue_num へのアクセスに失敗しました"
           execute_rollback "issue_validation_failed"
           exit 1
       fi
       
       # Issueがオープンであることを確認
       if issue_state=$(safe_get_issue_info "$issue_num" "json" | jq -r '.state'); then
           if [[ "$issue_state" == "closed" ]]; then
               echo "警告: イシュー #$issue_num は既に閉じられています" >&2
           fi
       fi
   done
   
   # 📖 ビジョン整合性を安全にチェック
   echo "📖 ビジョンアライメント確認中..."
   
   if [[ -f "docs/vision/project-vision.md" ]]; then
       if check_file_permissions "docs/vision/project-vision.md" "read"; then
           echo "✅ ビジョンドキュメント確認完了"
           # ここに実際の整合性チェックロジックを追加可能
       else
           echo "警告: ビジョンドキュメントの読み取り権限がありません" >&2
       fi
   else
       echo "⚠️  ビジョンドキュメントが存在しません: docs/vision/project-vision.md"
   fi
   ```

4. **アトミック操作でメタデータファイルを作成**:
   ```bash
   # 📊 必須の正式テンプレートを使用してメタデータファイルを安全に作成
   metadata_file="docs/use_cases/issue-${issue_list}-${feature_name}.json"
   
   echo "メタデータファイル作成: $metadata_file"
   
   # 🚫 重要: メタデータファイルを手動で作成しない - 常にcreate_metadata_if_not_exists()を使用
   # この関数は完全な正式テンプレート構造が使用されることを保証
   if ! create_metadata_if_not_exists "$metadata_file" "$feature_name" "${issue_numbers[@]}"; then
       echo "エラー: メタデータファイルの作成に失敗しました"
       execute_rollback "metadata_creation_failed"
       exit 1
   fi
   
   # ✅ 正式テンプレートが使用されたことを確認（すべての必須フェーズが必要）
   if ! jq -e '.phases.scenario_evolution and .phases.review and .phases.feedback_application and .phases.pull_request' "$metadata_file" >/dev/null 2>&1; then
       echo "❌ エラー: 正式テンプレートが使用されていません - 手動作成は禁止されています"
       echo "   必須フィールド: scenario_evolution, review, feedback_application, pull_request"
       execute_rollback "invalid_metadata_template"
       exit 1
   fi
   
   echo "✅ 正式メタデータテンプレート確認完了"
   
   # メタデータファイルのロールバックを追加
   add_rollback "rm -f '$metadata_file'" "Clean up metadata file"
   
   # 🔄 メタデータをアトミックに更新
   echo "メタデータ更新中..."
   if ! update_metadata_atomic "$metadata_file" '
       .phases.use_case.created = true |
       .phases.use_case.approved = false |
       .phase = "use_case_created" |
       .updated_at = "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'"
   '; then
       echo "エラー: メタデータの更新に失敗しました"
       execute_rollback "metadata_update_failed"
       exit 1
   fi
   ```

5. **安全な操作でユースケース仕様ファイルを作成**:
   ```bash
   # 📄 安全な操作で仕様ファイルを作成
   spec_file="docs/use_cases/issue-${issue_list}-${feature_name}.md"
   
   echo "ユースケース仕様ファイル作成: $spec_file"
   
   # 🛡️ ファイル作成前に安全な操作を確認
   if ! verify_safe_operation "create" "$spec_file" 50; then
       echo "エラー: ファイル作成の安全性チェックに失敗しました"
       execute_rollback "safety_check_failed"
       exit 1
   fi
   
   # 📝 仕様内容を生成
   spec_content="$(cat <<EOF
# ユースケース仕様: $feature_name

## 概要
$(for num in "${issue_numbers[@]}"; do echo "- [Issue #$num]($(gh issue view $num --json url --jq '.url' 2>/dev/null || echo 'N/A'))"; done)

## Given-When-Then シナリオ

### メインシナリオ
**Given**: <前提条件を記述>
- システムが正常に稼働している
- ユーザーが適切な権限を持っている

**When**: <実行される操作を記述>
- ユーザーが特定のアクションを実行する

**Then**: <期待される結果を記述>
- システムが期待通りに応答する
- 適切な状態変更が発生する

### 代替シナリオ 1: エラーケース
**Given**: <エラー前提条件>
**When**: <エラー操作>
**Then**: <エラー処理結果>

### 代替シナリオ 2: 境界値ケース
**Given**: <境界値前提条件>
**When**: <境界値操作>
**Then**: <境界値処理結果>

## 非機能要件
- **性能**: レスポンス時間 < 2秒
- **セキュリティ**: 適切な認証・認可
- **可用性**: 99.9% アップタイム

## 受け入れ基準
- [ ] メインシナリオが正常に動作する
- [ ] エラーケースが適切に処理される
- [ ] 非機能要件を満たす
- [ ] セキュリティ要件を満たす
- [ ] テストケースが網羅的に作成されている

## 関連情報
- **作成日時**: $(date)
- **作成者**: $(git config user.name || echo "Unknown")
- **関連イシュー**: $(for num in "${issue_numbers[@]}"; do echo "#$num "; done)
- **ブランチ**: $branch_name
- **メタデータ**: $metadata_file

## 次のステップ
1. ドメインモデル設計: \`/domain-modeling ${issue_numbers[*]}\`
2. テスト作成: \`/create-tests ${issue_numbers[*]}\`
EOF
)"

   # 📄 バックアップ付きで安全にファイルを作成
   if ! safe_create_file "$spec_file" "$spec_content" true; then
       echo "エラー: 仕様ファイルの作成に失敗しました"
       execute_rollback "spec_file_creation_failed"
       exit 1
   fi
   
   # 仕様ファイルのロールバックを追加
   add_rollback "rm -f '$spec_file'" "Clean up specification file"
   ```

6. **インデックスファイルを安全に更新**:
   ```bash
   # 📚 戦術レベルインデックスファイルを安全に更新
   index_file="docs/use_cases/index.md"
   
   echo "インデックスファイル更新: $index_file"
   
   # 🔍 存在しない場合はインデックスファイルを作成
   if [[ ! -f "$index_file" ]]; then
       index_content="# Use Case Implementation Status

## In Progress 🚧
- [$feature_name]($spec_file) - Issues: $(IFS=', #'; echo "#${issue_numbers[*]}") (Phase: use_case_created)

## Completed ✅
(None yet)

## Evolved Scenarios
(None yet)
"
       
       if ! safe_create_file "$index_file" "$index_content" true; then
           echo "エラー: インデックスファイルの作成に失敗しました"
           execute_rollback "index_creation_failed"
           exit 1
       fi
   else
       # 🔄 既存インデックスファイルを安全に更新
       # 修正前にバックアップを作成
       backup_file="${index_file}.backup.$(date +%Y%m%d_%H%M%S)"
       if ! cp "$index_file" "$backup_file"; then
           echo "エラー: インデックスファイルのバックアップ作成に失敗しました"
           execute_rollback "index_backup_failed"
           exit 1
       fi
       
       add_rollback "mv '$backup_file' '$index_file'" "Restore index file backup"
       
       # 一時ファイルを使用した安全な更新
       temp_file="${index_file}.tmp"
       if ! sed "/## In Progress 🚧/a\\
- [$feature_name]($spec_file) - Issues: $(IFS=', #'; echo "#${issue_numbers[*]}") (Phase: use_case_created)" "$index_file" > "$temp_file"; then
           echo "エラー: インデックスファイルの更新に失敗しました"
           execute_rollback "index_update_failed"
           exit 1
       fi
       
       if ! mv "$temp_file" "$index_file"; then
           echo "エラー: インデックスファイルの置換に失敗しました"
           execute_rollback "index_replacement_failed"
           exit 1
       fi
   fi
   ```

7. **安全な変更のコミット**:
   ```bash
   # 💾 安全なgit操作でコミット
   commit_message="feat: add use case specification for $feature_name

Create Given-When-Then scenarios and metadata tracking for:
$(for num in "${issue_numbers[@]}"; do echo "- Issue #$num"; done)

Files created:
- $spec_file (use case specification)
- $metadata_file (metadata tracking)
- $index_file (updated index)

Related issues: $(for num in "${issue_numbers[@]}"; do echo "Closes #$num"; done | tr '\n' ' ')
"
   
   echo "変更をコミット中..."
   if ! safe_git_commit "$commit_message" "$spec_file" "$metadata_file" "$index_file"; then
       echo "エラー: コミットに失敗しました"
       execute_rollback "commit_failed"
       exit 1
   fi
   
   # コミットクリーンアップを含むようにロールバックを更新
   add_rollback "git reset --hard HEAD~1" "Undo commit"
   ```

8. **GitHub Issueの更新**:
   ```bash
   # 📢 安全なGitHub操作でIssueを更新
   echo "GitHub イシューの更新中..."
   
   for issue_num in "${issue_numbers[@]}"; do
       comment_body="✅ **ユースケース仕様作成完了**

**作成ファイル:**
- 📋 仕様書: \`$spec_file\`
- 📊 メタデータ: \`$metadata_file\`
- 🌳 ブランチ: \`$branch_name\`

**次のステップ:**
\`\`\`bash
/domain-modeling ${issue_numbers[*]}
\`\`\`

**進捗状況:** TDD フェーズ 1/3 (RED-GREEN-REFACTOR)
"
       
       if ! safe_add_issue_comment "$issue_num" "$comment_body"; then
           echo "警告: イシュー #$issue_num へのコメント追加に失敗しました (続行します)" >&2
           # GitHub APIエラーは警告のみで処理続行
       else
           echo "✅ イシュー #$issue_num にコメント追加完了"
       fi
   done
   ```

9. **最終検証とトランザクションコミット**:
   ```bash
   # 🔍 最終検証
   echo "最終検証実行中..."
   
   # メタデータ整合性チェック
   if ! validate_metadata_integrity "$metadata_file"; then
       echo "エラー: メタデータの整合性チェックに失敗しました"
       execute_rollback "final_validation_failed"
       exit 1
   fi
   
   # 🚨 重要: 正式テンプレート準拠の再チェック
   echo "正式テンプレート完全性チェック..."
   required_phases=("scenario_evolution" "review" "feedback_application" "pull_request" "all_tests" "refactor")
   for phase in "${required_phases[@]}"; do
       if ! jq -e ".phases.$phase" "$metadata_file" >/dev/null 2>&1; then
           echo "❌ エラー: 必須フェーズが不足: $phase"
           echo "   正式テンプレートではありません。create_metadata_if_not_exists()を使用してください"
           execute_rollback "incomplete_metadata_template"
           exit 1
       fi
   done
   echo "✅ 正式テンプレート完全性確認完了"
   
   # ファイル存在確認
   for file in "$spec_file" "$metadata_file" "$index_file"; do
       if [[ ! -f "$file" ]]; then
           echo "エラー: 必要なファイルが存在しません: $file"
           execute_rollback "file_missing"
           exit 1
       fi
   done
   
   # Gitステータス確認
   if ! git diff --quiet HEAD~1 HEAD; then
       echo "✅ 変更が正常にコミットされています"
   else
       echo "エラー: 期待される変更がコミットされていません"
       execute_rollback "commit_verification_failed"
       exit 1
   fi
   
   # 🎉 トランザクションコミット（成功！）
   if commit_transaction; then
       echo ""
       echo "🎉 ユースケース仕様作成完了!"
       echo "================================="
       echo "📁 仕様ファイル: $spec_file"
       echo "📊 メタデータ: $metadata_file"
       echo "📚 インデックス: $index_file"
       echo "🌳 ブランチ: $branch_name"
       echo "🔢 関連イシュー: $(IFS=', #'; echo "#${issue_numbers[*]}")"
       echo ""
       echo "📋 次のコマンド実行:"
       echo "   /domain-modeling ${issue_numbers[*]}"
       echo ""
       echo "🚨 MANDATORY FOR CLAUDE CODE: SCENARIO EVOLUTION CHECK"
       echo "   Claude Code: 新しい要件・エラー・エッジケースを発見時は"
       echo "   必ず /evolve-scenarios <feature-name> を実行すること"
       echo "   ユーザー: 上記と同様の対応をお願いします"
       echo "   警告: このルール違反は重大な実装漏れを引き起こします"
       echo ""
       
       # 🔍 メタデータテンプレート検証を表示
       echo "📊 メタデータテンプレート情報:"
       echo "   フェーズ数: $(jq '.phases | length' "$metadata_file")"
       echo "   テンプレート版: 正式版 ($(jq -r '.created_at' "$metadata_file"))"
       echo "   必須フィールド: ✅ 全て含まれています"
       echo ""
       
       # 操作ログを表示
       echo "📊 操作ログ:"
       show_git_operation_log
       show_file_operation_log
       show_github_operation_log
       show_transaction_log
       
   else
       echo "❌ トランザクション コミット失敗"
       exit 1
   fi
   ```