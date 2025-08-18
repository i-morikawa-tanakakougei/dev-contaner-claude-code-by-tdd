# プルリクエスト作成と関連イシューの終了

## メタデータ
- **前提条件**: フィードバック適用済み、すべての実装完了
- **入力**: イシュー番号（必須）
- **出力**: 
  - GitHub プルリクエスト作成
  - イシューリンクと終了準備
  - 最終 `docs/use_cases/issue-X-Y.json` メタデータ更新
- **依存関係**: GitHub CLI (`gh`)、Git設定、完了した実装
- **実行タイミング**: すべての開発フェーズ完了後の最終ステップ

## 🎯 **TDD/DDD/LAYERED プロセス コンテキスト**

**🔄 コアワークフロー**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 アーキテクチャ**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 開発**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ 設計**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 要件**: Given-When-Then シナリオと完全な追跡可能性  
**🔄 進化**: /evolve-scenarios コマンドによる継続的シナリオ進化

> 📖 **ドキュメント管理システム**: [README.md](./README.md)  
> 🗺️ **現在位置**: レビュー段階 - プルリクエスト作成 (15/16)  
> 🎯 **段階目的**: PR作成、実装検証、イシュー終了  
> ⬅️ **前段階**: 14-apply-feedback (フィードバック適用)  
> ➡️ **次段階**: プロジェクト完了または新機能サイクル
>
> **📋 3層アーキテクチャ操作**:  
> - 🎯 **戦略**: `docs/use_cases/core/index.md` (完了参照)  
> - 📊 **戦術**: `docs/use_cases/index.md` (完了としてマーク)  
> - 🔧 **実行**: `docs/use_cases/issue-X-Y.json` (最終メタデータ更新)

## 🚀 **プルリクエスト作成: ファイナライズのみ**

**⚠️ 重要な注意:**
- **この段階はPR作成のみ** - プルリクエスト作成と実装のファイナライズ
- **新規実装なし** - PR作成とイシュー終了に集中  
- **品質ゲート検証** - すべての品質基準が満たされていることを確認
- **ドキュメント完成** - 必要なドキュメント類をすべて完成

**PR作成プロセス:**
1. `14-apply-feedback` ← すべての改善適用済み
2. `15-create-pr` ← **【現在地】PR作成とファイナライズ**
3. `16-use-case-status` ← 最終ステータス確認
4. PRマージとイシュー終了

**PR作成タスク:**
- ✅ すべてのテストが通ることを検証
- ✅ 包括的なPR説明を作成
- ✅ 関連イシューを適切なリンクで終了

## 📋 **プルリクエスト作成タスクチェックリスト**

**高品質PR作成とファイナライズにこのチェックリストを使用:**

### 🔴 必須タスク

#### **🔍 最終品質ゲート検証**
- [ ] **最終テストスイート実行**: `uv run --frozen pytest --cov=src --cov-report=html` を実行
- [ ] **すべてのテストGREEN確認**: 100%テスト成功率を確認
- [ ] **テストカバレッジ検証**: カバレッジがプロジェクト基準（80%+）を満たすことを確認
- [ ] **Given-When-Thenカバレッジ確認**: すべてのシナリオに対応するテストがあることを確認
- [ ] **最終ruffリンティング実行**: `uv run --frozen ruff check src/ --fix` を実行
- [ ] **クリーンな品質結果確認**: すべての品質ツールがエラーなしで通ることを確認

#### **📊 イシュー分析と終了準備**
- [ ] **対象イシューの解析**: コマンド引数からすべてのイシュー番号を抽出
- [ ] **イシュー完了検証**: 対象イシューからのすべての要件が実装されていることを確認
- [ ] **受入基準確認**: すべての受入基準が満たされていることを確認
- [ ] **イシューコメント確認**: 議論された要件がすべて対処されていることを確認

#### **📝 包括的PR説明作成**
- [ ] **エグゼクティブサマリー作成**: 実装内容と理由の明確な概要
- [ ] **ビジネス価値の文書化**: ビジネスインパクトとユーザーメリットの説明
- [ ] **技術変更リスト**: アーキテクチャ、コード、インフラストラクチャ変更の要約
- [ ] **イシュー要件マッピング**: 各イシュー要件がどのように対処されたかを表示

### 🟡 推奨タスク

#### **🎯 要件トレーサビリティ文書化**
- [ ] **Given-When-Then実装文書化**: シナリオと実際のテスト実装をリンク
- [ ] **品質メトリクス包含**: テストカバレッジ、パフォーマンス、品質改善を報告
- [ ] **クロスイシュー依存関係検証**: イシュー間に依存関係があるかチェック
- [ ] **終了ステートメント準備**: 各イシューの個別終了正当化をドラフト

### 🟢 オプションタスク

#### **🔧 高度品質検証**
- [ ] **最終ruffフォーマット実行**: `uv run --frozen ruff format src/` を実行
- [ ] **最終型チェック実行**: `uv run --frozen pyright src/` を実行
- [ ] **シナリオからコードへのマッピング**: Given-When-Thenシナリオを実装にリンク
- [ ] **受入基準満足の文書化**: 各基準がどのように満たされたかを表示
- [ ] **テストから要件へのリンク**: テストケースを元のビジネス要件に接続
- [ ] **アーキテクチャ決定表示**: 主要設計決定と根拠を文書化
- [ ] **実装ノート包含**: 複雑または非明白な実装選択を説明
- [ ] **将来考慮事項文書化**: 技術的債務や将来改善機会をメモ

### **🔗 プルリクエスト技術セットアップ**
- [ ] **クリーンなgitステータス確認**: 未コミット変更が残っていないことを確認
- [ ] **フィーチャーブランチ作成**: PRが適切なフィーチャーブランチからであることを確認
- [ ] **明確なコミットメッセージ作成**: コミット履歴がクリーンで説明的であることを確認
- [ ] **適切なラベル追加**: PR に関連ラベル（feature、bugfix、enhancement）をタグ
- [ ] **マイルストーン設定**: PRを適切なプロジェクトマイルストーンにリンク
- [ ] **レビュアー追加**: 適切なコードレビュアー（artofzeroを含む）を割り当て

### **📋 PR説明テンプレート実装**
- [ ] **PR タイトル作成**: プロジェクト規約に従った明確で説明的なタイトル
- [ ] **サマリーセクション作成**: 変更とビジネス価値の簡潔な概要
- [ ] **テストプラン文書化**: 変更がどのようにテストされ検証されたかを説明
- [ ] **破壊的変更リスト**: 破壊的変更や移行要件をメモ
- [ ] **スクリーンショット/デモ包含**: 該当する場合は機能の視覚的証拠を追加
- [ ] **デプロイメントノート追加**: 特別なデプロイメントや設定要件を含める

### **🎫 イシュー終了統合**
- [ ] **イシュー終了キーワード追加**: PR説明に「Closes #X, Fixes #Y」構文を含める
- [ ] **イシューリンク検証**: GitHubが対象イシューにPRを適切にリンクすることを確認
- [ ] **イシューラベル確認**: 完了ステータスを反映するようイシューラベルを更新
- [ ] **完了根拠文書化**: 各イシューの要件がどのように満たされたかを説明
- [ ] **部分完了処理**: 部分完了のイシューと予定されるフォローアップをメモ
- [ ] **イシューマイルストーン更新**: イシューが適切にマイルストーン割り当てされていることを確認

### **🚀 CI/CDとマージ準備**
- [ ] **CIパイプライン準備確認**: すべてのCIチェックが実行されるよう設定されていることを確認
- [ ] **ブランチ保護確認**: ブランチ保護ルールが満たされていることを確認
- [ ] **マージ要件検証**: すべてのマージ要件が満たされることを確認
- [ ] **PR作成テスト**: PRが競合なしで作成できることを確認
- [ ] **自動チェック確認**: 自動品質チェックが通ることを確認
- [ ] **マージ戦略計画**: マージコミット vs スカッシュマージアプローチを決定

### **📊 品質とパフォーマンス検証**
- [ ] **パフォーマンスインパクト文書化**: パフォーマンス改善やインパクトを報告
- [ ] **メモリ使用量検証**: メモリリークや過度なメモリ使用がないことを確認
- [ ] **リソース使用率確認**: 適切なリソース使用パターンを確認
- [ ] **エラーハンドリングテスト**: エラーシナリオがエンドツーエンドで正しく動作することを検証
- [ ] **ログと監視確認**: 適切な可観測性が実装されていることを確認
- [ ] **セキュリティ考慮確認**: セキュリティ要件が満たされていることを検証

### **🔍 レビューサポート文書化**
- [ ] **レビューガイド作成**: レビュアーが何に焦点を当てるべきかガイダンスを提供
- [ ] **テスト手順文書化**: 手動テストのための明確な手順を提供
- [ ] **複雑な変更ハイライト**: 複雑またはリスクの高い変更に注意を喚起
- [ ] **コンテキスト提供**: 主要決定の背景と根拠を説明
- [ ] **参照リンク包含**: 仕様、設計ドキュメント、関連イシューへのリンク
- [ ] **デモ/ウォークスルー準備**: 必要に応じて機能のデモンストレーションを計画

### **📈 メトリクスと成功基準**
- [ ] **品質改善文書化**: コード品質、カバレッジ、複雑性メトリクスを報告
- [ ] **ビジネス価値提供測定**: 可能な場合はビジネスインパクトを定量化
- [ ] **技術改善報告**: 技術的債務削減やアーキテクチャ改善を文書化
- [ ] **ユーザーエクスペリエンス検証**: ユーザーエクスペリエンスが期待を満たすか上回ることを確認
- [ ] **アクセシビリティ確認**: 該当する場合はアクセシビリティ要件が満たされていることを確認
- [ ] **学習記録文書化**: 将来の開発サイクルのための洞察を記録

### **🎉 PR作成と最終ステップ**
- [ ] **プルリクエスト作成**: 包括的な説明と適切なイシューリンクでPRを提出
- [ ] **イシュー自動リンク確認**: GitHubが対象イシューを適切にリンクし終了することを確認
- [ ] **ステークホルダー通知**: PRがレビュー準備完了であることを関連ステークホルダーに通知
- [ ] **プロジェクト追跡更新**: プロジェクトボード、スプリントステータス、チーム通信を更新
- [ ] **レビューサイクル準備**: レビューフィードバックに迅速に対応する準備
- [ ] **CI/CDパイプライン監視**: すべての自動チェックが正常に通ることを確認

### **📚 最終文書化更新**
- [ ] **メタデータファイル更新**: すべての関連issue-X-Y.jsonファイルで実装完了をマーク
- [ ] **ユースケースインデックス更新**: 戦術レベル項目を完了としてマーク
- [ ] **作業ドキュメントアーカイブ**: 作業ノートと一時ファイルを適切に保存
- [ ] **プロジェクトメトリクス更新**: プロジェクト追跡のための完了メトリクスを記録
- [ ] **ハンドオフ文書化準備**: チームのために知識が適切に文書化されていることを確認
- [ ] **開発アーティファクトクリーンアップ**: 一時ファイルと開発専用コードを削除

**💡 プロヒント: よく書かれたPR説明は何時間ものレビュー時間を節約し、スムーズなマージを保証します - 品質PR文書化に投資しましょう！
- ✅ 関連GitHubイシューをリンクして終了
- ✅ 最終文書化を更新
- ❌ 新機能を追加しない
- ❌ 実装変更を行わない

**プルリクエスト作成とファイナライズのみ。**

## よくあるエラーと解決方法

### ❌ エラーケース1: フィードバックが未適用
**原因**: フィードバック適用前にプルリクエスト作成を試行  
**解決方法**: 最初に `/apply-feedback <issue-number>` でフィードバックを適用

### ❌ エラーケース2: GitHub CLI未設定
**原因**: `gh` コマンドが認証されていないかリポジトリが設定されていない  
**解決方法**: 
```bash
gh auth login
gh repo set-default <your-repo>
```

### ❌ エラーケース3: ブランチがリモートにプッシュされていない
**原因**: フィーチャーブランチがローカルにのみ存在  
**解決方法**: PR作成前にブランチをリモートにプッシュ

## 実行例

### ✅ 成功例
```bash
$ /create-pr 15
🚀 Issues: #15 のPR作成を開始します
🔄 フィードバック適用確認中...
✅ フィードバックが適用されています
🌐 ブランチをリモートにプッシュ中...
📄 PR作成中...
✅ PR作成完了: https://github.com/repo/pull/123
🔗 イシューリンク設定中...
✅ Issue #15 をPRにリンク
🎉 PR作成完了!
```

### ❌ 失敗例と修正
```bash
$ /create-pr 15
❌ フィードバックが適用されていません
💡 最初にフィードバックを適用してください:
   /apply-feedback 15

# 修正: 最初にフィードバックを適用
$ /apply-feedback 15
$ /create-pr 15
```

## タスク詳細

1. **安全環境のセットアップと検証**:
   ```bash
   # 🔧 すべての安全操作関数をロード
   source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "15-create-pr" "$ARGUMENTS"
   
   # 最低1つのイシュー番号があることを検証
   if [[ ${#issue_numbers[@]} -eq 0 ]]; then
       echo "エラー: 最低1つのイシュー番号が必要です"
       show_usage_example "create-pr" "1" "イシュー1のPR作成"
       show_usage_example "create-pr" "1,7" "複数イシュー統合PR作成"
       exit 1
   fi
   ```

2. **トランザクション開始と事前検証**:
   ```bash
   # 🔄 包括的トランザクション開始
   if ! begin_transaction "create_pr_$(IFS=-; echo "${issue_numbers[*]}")"; then
       echo "エラー: トランザクションの開始に失敗しました"
       exit 1
   fi
   
   # 📝 フィーチャー名とメタデータファイルを決定
   if [[ ${#other_args[@]} -gt 0 ]]; then
       feature_name="${other_args[0]}"
   else
       # 既存ファイルからメタデータファイルを検索
       issue_list=$(IFS=-; echo "${issue_numbers[*]}")
       metadata_file=$(find docs/use_cases -name "issue-${issue_list}-*.json" 2>/dev/null | head -1)
       
       if [[ -z "$metadata_file" ]]; then
           echo "エラー: フィーチャー名が指定されておらず、メタデータファイルも見つかりません"
           echo "使用方法: /create-pr ${issue_numbers[*]} フィーチャー名"
           execute_rollback "metadata_not_found"
           exit 1
       fi
       
       feature_name=$(basename "$metadata_file" .json | sed 's/issue-[0-9-]*-//')
   fi
   
   # メタデータファイルパスを設定
   issue_list=$(IFS=-; echo "${issue_numbers[*]}")
   metadata_file="docs/use_cases/issue-${issue_list}-${feature_name}.json"
   
   echo "🔍 メタデータファイル: $metadata_file"
   echo "🏷️  フィーチャー名: $feature_name"
   ```

3. **包括的PR前検証**:
   ```bash
   # 🔍 すべての前提条件を検証
   echo "📋 PR作成前の包括的検証実行中..."
   
   # 1. メタデータファイル検証
   if [[ ! -f "$metadata_file" ]]; then
       echo "エラー: メタデータファイルが存在しません: $metadata_file"
       execute_rollback "metadata_missing"
       exit 1
   fi
   
   if ! validate_metadata_integrity "$metadata_file"; then
       echo "エラー: メタデータファイルの整合性チェックに失敗しました"
       execute_rollback "metadata_invalid"
       exit 1
   fi
   
   # 2. 必要なフェーズがすべて完了していることを確認
   echo "📊 開発フェーズ完了状況確認中..."
   
   required_phases=("use_case" "domain_model" "tests" "domain_implementation" "usecase_implementation" "infrastructure_implementation" "presentation_implementation" "all_tests" "refactor")
   
   for phase in "${required_phases[@]}"; do
       phase_completed=$(jq -r ".phases.${phase}.completed // .phases.${phase}.created // false" "$metadata_file")
       if [[ "$phase_completed" != "true" ]]; then
           echo "エラー: 必須フェーズが未完了です: $phase"
           echo "現在の状態: $phase_completed"
           execute_rollback "phase_incomplete"
           exit 1
       fi
       echo "  ✅ $phase: 完了"
   done
   
   # 3. GitHubイシューが存在してアクセス可能であることを検証
   echo "🔍 GitHub イシュー検証中..."
   for issue_num in "${issue_numbers[@]}"; do
       if ! safe_get_issue_info "$issue_num" "json" >/dev/null; then
           echo "エラー: イシュー #$issue_num にアクセスできません"
           execute_rollback "issue_access_failed"
           exit 1
       fi
       echo "  ✅ イシュー #$issue_num: アクセス可能"
   done
   
   # 4. Git リポジトリ状態検証
   echo "🌳 Git リポジトリ状態確認中..."
   
   current_branch=$(git branch --show-current)
   if [[ -z "$current_branch" ]]; then
       echo "エラー: 現在のブランチ名を取得できません"
       execute_rollback "branch_detection_failed"
       exit 1
   fi
   
   expected_branch="feature/issue-${issue_list}-${feature_name}"
   if [[ "$current_branch" != "$expected_branch" ]]; then
       echo "警告: 期待されるブランチと異なります"
       echo "現在: $current_branch"
       echo "期待: $expected_branch"
   fi
   
   # 5. 未コミット変更をチェック
   if ! git diff-index --quiet HEAD --; then
       echo "⚠️  未コミットの変更があります。PR作成前にコミットします。"
       
       # 残りの変更を安全にコミット
       if ! safe_git_commit "chore: final changes before PR creation

   Final cleanup and preparation for pull request.
   
   Related issues: $(for num in "${issue_numbers[@]}"; do echo "#$num "; done)" "." ; then
           echo "エラー: 最終コミットに失敗しました"
           execute_rollback "final_commit_failed"
           exit 1
       fi
       
       add_rollback "git reset --hard HEAD~1" "Undo final commit"
   fi
   ```

4. **アーキテクチャと品質検証**:
   ```bash
   # 🏗️ アーキテクチャ検証
   echo "🏗️ アーキテクチャ検証実行中..."
   
   if ! validate_architecture; then
       echo "エラー: アーキテクチャ検証に失敗しました"
       echo "PR作成前にアーキテクチャ違反を修正してください"
       execute_rollback "architecture_validation_failed"
       exit 1
   fi
   
   echo "✅ アーキテクチャ検証完了"
   
   # 🧪 利用可能な場合はすべてのテストを実行
   echo "🧪 テスト実行中..."
   
   if [[ -f "pyproject.toml" ]] && command -v uv &> /dev/null; then
       echo "Python プロジェクト検出 - テスト実行中..."
       
       if ! uv run --frozen pytest --tb=short; then
           echo "エラー: テストが失敗しました"
           echo "PR作成前にテストを修正してください"
           execute_rollback "tests_failed"
           exit 1
       fi
       
       echo "✅ 全テスト成功"
   else
       echo "⚠️  テスト環境が検出されませんでした"
   fi
   ```

5. **PR内容生成とブランチプッシュ**:
   ```bash
   # 📝 包括的PR内容を生成
   echo "📝 PR内容生成中..."
   
   # メタデータから情報を抽出
   creation_date=$(jq -r '.created_at' "$metadata_file")
   phases_completed=$(jq -r '.phases | keys[]' "$metadata_file" | wc -l)
   
   # PRタイトルを生成
   pr_title="feat: implement $feature_name"
   if [[ ${#issue_numbers[@]} -gt 1 ]]; then
       pr_title="$pr_title (multiple issues)"
   fi
   
   # 包括的PR本文を生成
   pr_body="$(cat <<EOF
## 📋 Summary
   
   Implementation of **$feature_name** feature covering the following requirements:
   $(for num in "${issue_numbers[@]}"; do echo "- Closes #$num"; done)
   
## 🎯 What Changed
   
   ### 📊 Implementation Overview
   - **Development Phases Completed**: $phases_completed
   - **Architecture**: TDD/DDD/Layered Architecture
   - **Created**: $creation_date
   - **Branch**: $current_branch
   
   ### 🏗️ Architecture Layers Implemented
   - ✅ **Domain Layer**: Core business logic and entities
   - ✅ **Application Layer**: Use cases and orchestration
   - ✅ **Infrastructure Layer**: Data persistence and external services
   - ✅ **Presentation Layer**: API endpoints and user interfaces
   
   ### 📁 Files Modified/Created
   $(git diff --name-status main..HEAD | sed 's/^/   - /')
   
## 🧪 Test Plan
   
   - [x] Unit tests for domain entities and value objects
   - [x] Integration tests for use cases
   - [x] Architecture compliance validation
   - [x] End-to-end scenario testing
   - [x] Error handling and edge cases
   
## 🔍 Review Checklist
   
   ### Code Quality
   - [x] Follows TDD/DDD principles
   - [x] Proper layer separation maintained
   - [x] No architectural violations
   - [x] Comprehensive error handling
   
   ### Documentation
   - [x] Use case specifications updated
   - [x] API documentation current
   - [x] README updated if needed
   
   ### Testing
   - [x] All tests passing
   - [x] Test coverage adequate
   - [x] Integration tests included
   
## 📊 Metadata
   
   - **Feature**: $feature_name
   - **Issues**: $(IFS=', #'; echo "#${issue_numbers[*]}")
   - **Metadata File**: \`$metadata_file\`
   - **Development Phases**: $(jq -r '.phases | keys | join(", ")' "$metadata_file")
   
## 🚀 Deployment Notes
   
   This feature is ready for deployment and includes:
   - Database migrations (if applicable)
   - Configuration changes documented
   - Backward compatibility maintained
   
   ---
   
   **Generated**: $(date)
   **Branch**: $current_branch
EOF
)"

   # 🚀 ブランチを安全にプッシュ
   echo "🚀 ブランチをプッシュ中: $current_branch"
   
   if ! safe_git_push "$current_branch"; then
       echo "エラー: ブランチのプッシュに失敗しました"
       execute_rollback "push_failed"
       exit 1
   fi
   
   add_rollback "git push origin --delete '$current_branch'" "Delete remote branch"
   echo "✅ ブランチプッシュ完了"
   ```

6. **プルリクエスト作成**:
   ```bash
   # 🔀 プルリクエストを安全に作成
   echo "🔀 プルリクエスト作成中..."
   
   pr_number=$(safe_create_pull_request "$pr_title" "$pr_body" "main" "$current_branch")
   
   if [[ -z "$pr_number" ]]; then
       echo "エラー: プルリクエストの作成に失敗しました"
       execute_rollback "pr_creation_failed"
       exit 1
   fi
   
   echo "✅ プルリクエスト作成成功: #$pr_number"
   add_rollback "gh pr close '$pr_number' --delete-branch" "Close PR and cleanup"
   ```

7. **メタデータとインデックスファイル更新**:
   ```bash
   # 📊 PR情報でメタデータを更新
   echo "📊 メタデータファイル更新中..."
   
   if ! update_metadata_atomic "$metadata_file" "
       .phases.pull_request.created = true |
       .phases.pull_request.pr_number = $pr_number |
       .phases.pull_request.merged = false |
       .phase = \"pull_request_created\" |
       .updated_at = \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\"
   "; then
       echo "エラー: メタデータの更新に失敗しました"
       execute_rollback "metadata_update_failed"
       exit 1
   fi
   
   # 📚 戦術インデックスファイルを更新
   index_file="docs/use_cases/index.md"
   
   if [[ -f "$index_file" ]]; then
       echo "📚 インデックスファイル更新中..."
       
       # バックアップを作成
       backup_file="${index_file}.backup.$(date +%Y%m%d_%H%M%S)"
       if ! cp "$index_file" "$backup_file"; then
           echo "エラー: インデックスファイルのバックアップ作成に失敗しました"
           execute_rollback "index_backup_failed"
           exit 1
       fi
       
       add_rollback "mv '$backup_file' '$index_file'" "Restore index backup"
       
       # "In Progress" から "Review" にステータスを更新
       temp_file="${index_file}.tmp"
       if ! sed "s/- \[${feature_name}\].*Phase: [^)]*)/- [$feature_name](issue-${issue_list}-${feature_name}.md) - Issues: $(IFS=', #'; echo "#${issue_numbers[*]}") (Phase: pull_request_created, PR: #$pr_number)/" "$index_file" > "$temp_file"; then
           echo "エラー: インデックスファイルの更新に失敗しました"
           execute_rollback "index_update_failed"
           exit 1
       fi
       
       if ! mv "$temp_file" "$index_file"; then
           echo "エラー: インデックスファイルの置換に失敗しました"
           execute_rollback "index_replacement_failed"
           exit 1
       fi
       
       echo "✅ インデックスファイル更新完了"
   fi
   ```

8. **最終コミットとイシュー更新**:
   ```bash
   # 💾 メタデータ更新をコミット
   echo "💾 メタデータ変更をコミット中..."
   
   if ! safe_git_commit "chore: update metadata for PR #$pr_number

   Update metadata and index files to reflect PR creation.
   
   - PR #$pr_number created for $feature_name
   - Status updated to pull_request_created
   - Index file updated with PR reference
   
   Related issues: $(for num in "${issue_numbers[@]}"; do echo "#$num "; done)" "$metadata_file" "$index_file"; then
       echo "エラー: メタデータコミットに失敗しました"
       execute_rollback "metadata_commit_failed"
       exit 1
   fi
   
   add_rollback "git reset --hard HEAD~1" "Undo metadata commit"
   
   # 🚀 最終変更をプッシュ
   if ! safe_git_push "$current_branch"; then
       echo "エラー: 最終プッシュに失敗しました"
       execute_rollback "final_push_failed"
       exit 1
   fi
   
   # 📢 PR情報でGitHubイシューを更新
   echo "📢 GitHub イシュー更新中..."
   
   for issue_num in "${issue_numbers[@]}"; do
       comment_body="🎉 **プルリクエスト作成完了**

   **Pull Request**: [#$pr_number]($(gh pr view $pr_number --json url --jq '.url' 2>/dev/null || echo 'N/A'))
   **Branch**: \`$current_branch\`
   **Feature**: $feature_name

   **🔍 Review Ready:**
   - ✅ All development phases completed
   - ✅ Architecture validation passed
   - ✅ All tests passing
   - ✅ Code ready for review

   **📊 Implementation Summary:**
   - Domain layer: Business logic implemented
   - Application layer: Use cases orchestrated  
   - Infrastructure layer: Persistence implemented
   - Presentation layer: API endpoints created

   **Next Steps:**
   1. Code review by team members
   2. Address any review feedback
   3. Merge when approved
   4. Deploy to staging/production

   This issue will be automatically closed when the PR is merged.
   "
       
       if ! safe_add_issue_comment "$issue_num" "$comment_body"; then
           echo "警告: イシュー #$issue_num へのコメント追加に失敗しました (続行します)" >&2
       else
           echo "✅ イシュー #$issue_num にPR情報コメント追加完了"
       fi
   done
   ```

9. **最終検証と成功**:
   ```bash
   # 🔍 最終包括検証を実行
   echo "🔍 最終検証実行中..."
   
   # PRが正常に作成されたことを確認
   if ! gh pr view "$pr_number" >/dev/null 2>&1; then
       echo "エラー: 作成されたPRにアクセスできません: #$pr_number"
       execute_rollback "pr_verification_failed"
       exit 1
   fi
   
   # メタデータが更新されたことを確認
   pr_created_status=$(jq -r '.phases.pull_request.created' "$metadata_file")
   if [[ "$pr_created_status" != "true" ]]; then
       echo "エラー: メタデータのPR作成状態が正しく更新されていません"
       execute_rollback "metadata_verification_failed"
       exit 1
   fi
   
   # ブランチがプッシュされ最新であることを確認
   if ! check_remote_sync "$current_branch" >/dev/null; then
       echo "エラー: ブランチがリモートと同期されていません"
       execute_rollback "sync_verification_failed"
       exit 1
   fi
   
   # 🎉 トランザクションコミット（成功！）
   if commit_transaction; then
       echo ""
       echo "🎉 プルリクエスト作成完了!"
       echo "========================================="
       echo "🔀 Pull Request: #$pr_number"
       echo "🌳 Branch: $current_branch"
       echo "🏷️  Feature: $feature_name"
       echo "🔢 Issues: $(IFS=', #'; echo "#${issue_numbers[*]}")"
       echo "📊 Metadata: $metadata_file"
       echo ""
       echo "🔗 PR URL: $(gh pr view $pr_number --json url --jq '.url' 2>/dev/null || echo 'N/A')"
       echo ""
       echo "📋 次のステップ:"
       echo "   1. チームメンバーによるコードレビュー"
       echo "   2. レビューフィードバック対応 (必要に応じて)"
       echo "   3. 承認後のマージ"
       echo "   4. 本番デプロイ"
       echo ""
       
       # 包括的操作ログを表示
       echo "📊 操作ログサマリー:"
       show_git_operation_log | tail -5
       show_github_operation_log | tail -3
       show_transaction_log | tail -3
       
       echo ""
       echo "✅ 全開発フェーズ完了 - レビュー準備完了!"
       echo ""
       echo "🚨 CLAUDE CODE必須: シナリオ進化チェック"
       echo "   PR作成中に新要件・制約・改善案発見時は"
       echo "   作業を中断して /evolve-scenarios <feature-name> を実行すること"
       echo "   重要: PR統合は最終チェックと新要件発見の重要な段階です"
       
   else
       echo "❌ トランザクション コミット失敗"
       exit 1
   fi
   ```