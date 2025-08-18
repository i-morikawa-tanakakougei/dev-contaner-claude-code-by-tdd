Given-When-Then仕様に基づいてドメインモデルを設計する

## メタデータ
- **前提条件**: ユースケース仕様が作成されている（03-create-use-case）
- **入力**: Issue番号（必須）、機能名（オプション）
- **出力**: 
  - `docs/domain/issue-X-Y-domain-model.md` - ドメインモデル設計書
  - 更新された`docs/use_cases/issue-X-Y.json`メタデータファイル
  - 設計ステータスで更新された`docs/use_cases/index.md`
- **依存関係**: jq、Git設定、ユースケース仕様ファイル
- **実行タイミング**: ユースケース仕様後、TDDテスト作成前

## 🎯 **TDD/DDD/レイヤードプロセスコンテキスト**

**🔄 コアワークフロー**: ビジョン(00) → 構造(01) → スプリント(02) → ユースケース(03) → ドメイン(04) → テスト(05) → ドメイン(06) → アプリ(07) → インフラ(08) → UI(09) → テスト(10) → リファクタ(11) → 進化(12) → レビュー(13) → フィードバック(14) → PR(15) → ステータス(16)

**🎨 アーキテクチャ**: クリーンアーキテクチャ（ドメイン→アプリケーション→インフラストラクチャ→プレゼンテーション）  
**🧪 開発**: テスト駆動開発（RED→GREEN→REFACTOR）  
**🏗️ 設計**: ドメイン駆動設計（エンティティ、値オブジェクト、集約、リポジトリ）  
**📋 要件**: 完全なトレーサビリティを持つGiven-When-Thenシナリオ  
**🔄 進化**: /evolve-scenariosコマンドによる継続的シナリオ進化

> 📖 **文書管理システム**: [README.md](./README.md)  
> 🗺️ **現在位置**: スプリント実行フェーズ - ドメインモデル設計（04/16）  
> 🎯 **フェーズ目的**: DDD原則に基づくドメインモデルとエンティティの設計  
> ⬅️ **前のステージ**: 03-create-use-case（ユースケース仕様）  
> ➡️ **次のステージ**: 05-create-tests（TDDテスト作成）
>
> **📋 3層アーキテクチャ操作**:  
> - 🎯 **戦略的**: `docs/use_cases/core/index.md`（ユビキタス言語の参照）  
> - 📊 **戦術的**: `docs/use_cases/index.md`（ドメイン設計ステータスの更新）  
> - 🔧 **実行**: `docs/use_cases/issue-X-Y.json`（ドメインモデリングフェーズの追跡）

## よくあるエラーと解決策

### ❌ エラーケース1: ユースケース仕様が見つからない
**原因**: ユースケース仕様作成前にドメインモデリングを開始  
**解決策**: 
```bash
# まずユースケース仕様を作成
/create-use-case <issue-number>
# その後ドメインモデリングを実行
/domain-modeling <issue-number>
```

### ❌ エラーケース2: メタデータファイル検証の失敗
**原因**: 破損または不足しているメタデータJSONファイル  
**解決策**: 
- メタデータファイルが存在し有効なJSON形式であることを確認
- 必要に応じて`/create-use-case`を使用して再生成

### ❌ エラーケース3: ドメイン概念抽出の失敗
**原因**: ユースケース仕様に明確なドメイン概念セクションがない  
**解決策**: 
- 仕様に「## ドメイン概念」セクションを追加
- 「- **EntityName**: description」形式でエンティティを定義

## 実行例

### ✅ 成功例
```bash
$ /domain-modeling 15
🏗️ Issues: #15 のドメインモデル設計を開始します
📋 前提条件の検証中...
  🔍 Issue #15 の仕様検索中...
    ✅ Issue #15 の仕様発見: issue-15-user-management.md
    📝 機能名抽出: user-management
✅ 前提条件検証完了: 1 個の仕様を確認
📖 ユースケース仕様分析中...
  📋 分析中: issue-15-user-management.md
  🎯 抽出された概念:
    - エンティティ: 3 個
    - ビジネスルール: 5 個
🏗️ ドメインモデル設計文書作成中...
✅ ドメインモデル設計文書作成完了: docs/domain/issue-15-domain-model.md
🎉 ドメインモデル設計完了!
```

### ❌ 失敗例と修正
```bash
$ /domain-modeling 15
❌ 以下のイシューの仕様が見つかりません:
  - Issue #15
💡 最初に以下のコマンドでユースケース仕様を作成してください:
   /create-use-case 15

# 修正: まずユースケース仕様を作成
$ /create-use-case 15
$ /domain-modeling 15
```

## 🚨 **重要警告: このステップでは実装を行わない**

**⚠️ 重要な注意:**
- **このステップは設計のみ** - コードの実装は行わない
- **設計文書のみ作成** - 実際のPythonコード実装は後のステップで実行  
- **TDDサイクル準備フェーズ** - 実装は`/implement-domain`ステップで行う
- **設計文書とディレクトリ構造のみ作成** - プレースホルダーファイルは作成しない

**正しいTDD/DDDフロー:**
1. `04-domain-modeling` ← **【現在位置】設計文書作成のみ**
2. `05-create-tests` ← TDD RED（失敗テストの作成）  
3. `06-implement-domain` ← TDD GREEN（テストを通すための実装）
4. `11-refactor` ← TDD REFACTOR（品質改善）

**ファイルの実装は行わない。設計文書のみ作成する。**

## 🚨 **CLAUDE CODE必須: シナリオ進化チェック**

**⚠️ AI開発において重要:**
- **ドメインモデリング中に新要件・制約・改善案発見時は作業を中断して `/evolve-scenarios <feature-name>` を実行すること**
- **重要**: ドメインモデル設計は新要件発見の重要な段階です
- **ユーザー向け**: 同様の対応をお願いします - 設計中に新しい要件やエッジケースを発見した場合は必ず記録してください

## 📋 **ドメインモデリングタスクチェックリスト**

**包括的なドメイン設計を確実にするためにこのチェックリストを使用してください:**

### 🔴 必須タスク

#### **📖 要件分析**
- [ ] **仕様を徹底的に読む**: Given-When-Thenシナリオを詳細に分析
- [ ] **ドメイン概念を抽出**: ビジネス用語と概念を特定
- [ ] **ユビキタス言語を確立**: ステークホルダーと用語を統一
- [ ] **ビジネスルールを特定**: 不変条件、制約、検証ルールを定義

#### **🏗️ ドメインモデル設計**  
- [ ] **エンティティを分類**: アイデンティティとライフサイクルを持つオブジェクトを特定
- [ ] **値オブジェクトを分類**: 不変で置換可能なオブジェクトを特定
- [ ] **集約境界を設計**: 整合性とトランザクション境界を定義
- [ ] **集約ルートを特定**: 外部アクセスポイントを決定

#### **📚 文書化と検証**
- [ ] **設計文書を作成**: 包括的なドメインモデル設計文書
- [ ] **設計根拠を記録**: 特定の設計決定を行った理由を文書化

### 🟡 推奨タスク

#### **🏗️ 高度なドメイン設計**
- [ ] **ドメインサービスを設計**: エンティティに属さないビジネスロジックを処理
- [ ] **実装ガイドを作成**: TDD実装のための注記とポリシー
- [ ] **レビュー準備**: ステークホルダーとチームのレビュー用資料

#### **🔗 インターフェースとイベント設計**
- [ ] **リポジトリインターフェースを設計**: 抽象データアクセスインターフェース
- [ ] **ドメインイベントを設計**: システム統合と副作用を定義
- [ ] **依存関係を検証**: クリーンアーキテクチャ原則の準拠を確認

### 🟢 オプションタスク

#### **🔍 品質保証**
- [ ] **アーキテクチャ整合性を検証**: レイヤー依存関係を確認
- [ ] **DDD原則準拠を確認**: エンティティ、値オブジェクト、サービスを検証
- [ ] **ビジネス要件カバレッジを確認**: すべてのGiven-When-Thenシナリオがカバーされていることを確認
- [ ] **拡張性を考慮**: 将来の変更への適応性を評価

**💡 プロTip**: このチェックリストを実際のプロジェクトで使用するためにコピーしてください！

## タスク詳細

1. **安全な環境設定と引数解析**:
   ```bash
   # 🔧 すべての安全操作機能を読み込み
   source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "04-domain-modeling" "$ARGUMENTS"
   
   # ドメインモデリングは少なくとも1つのIssue番号を期待
   if [[ ${#issue_numbers[@]} -eq 0 ]]; then
       echo "エラー: 少なくとも1つのイシュー番号を指定してください"
       show_usage_example "domain-modeling" "1" "単一イシューのドメインモデル設計"
       show_usage_example "domain-modeling" "1,7" "複数イシューのドメインモデル設計"
       show_usage_example "domain-modeling" "1 mt5-extended-data" "イシュー + 機能名指定"
       exit 1
   fi
   
   # Issueリストと機能名を抽出
   issue_list=$(IFS=-; echo "${issue_numbers[*]}")
   if [[ ${#other_args[@]} -gt 0 ]]; then
       feature_name="${other_args[0]}"
   else
       # 機能名は既存のユースケースファイルから抽出される
       feature_name=""
   fi
   
   echo "🏗️ Issues: $(printf '#%s ' "${issue_numbers[@]}")のドメインモデル設計を開始します"
   ```

2. **トランザクション開始と事前検証**:
   ```bash
   # 🔄 包括的トランザクションを開始
   if ! begin_transaction "domain_modeling_${issue_list}"; then
       echo "エラー: トランザクションの開始に失敗しました"
       exit 1
   fi
   
   # 📋 包括的エラーハンドリングで前提条件を検証
   echo "📋 前提条件の検証中..."
   
   # ユースケース仕様をチェック
   missing_specs=()
   found_specs=()
   for issue_num in "${issue_numbers[@]}"; do
       echo "  🔍 Issue #$issue_num の仕様検索中..."
       
       # ユースケース仕様ファイルを検索
       spec_files=$(find docs/use_cases/ -name "*issue-*${issue_num}*" -type f -name "*.md" 2>/dev/null | grep -v index.md || echo "")
       
       if [[ -z "$spec_files" ]]; then
           missing_specs+=("$issue_num")
           echo "    ❌ Issue #$issue_num の仕様が見つかりません"
       else
           found_specs+=("$spec_files")
           echo "    ✅ Issue #$issue_num の仕様発見: $(basename "$spec_files")"
           
           # 提供されていない場合は最初に見つかった仕様から機能名を抽出
           if [[ -z "$feature_name" ]]; then
               feature_name=$(basename "$spec_files" | sed 's/^issue-[0-9-]*-\(.*\)\.md$/\1/')
               echo "    📝 機能名抽出: $feature_name"
           fi
       fi
   done
   
   # 仕様が不足している場合はエラー
   if [[ ${#missing_specs[@]} -gt 0 ]]; then
       echo ""
       echo "❌ 以下のイシューの仕様が見つかりません:"
       printf '  - Issue #%s\n' "${missing_specs[@]}"
       echo ""
       echo "💡 最初に以下のコマンドでユースケース仕様を作成してください:"
       for missing_issue in "${missing_specs[@]}"; do
           echo "   /create-use-case $missing_issue"
       done
       execute_rollback "missing_use_case_specs"
       exit 1
   fi
   
   # 機能名が見つかったか提供されたかを検証
   if [[ -z "$feature_name" ]]; then
       echo "エラー: 機能名を特定できませんでした"
       echo "引数で機能名を指定するか、適切なユースケース仕様ファイルが必要です"
       execute_rollback "feature_name_missing"
       exit 1
   fi
   
   echo "✅ 前提条件検証完了: ${#found_specs[@]} 個の仕様を確認"
   ```

3. **メタデータファイルの特定と検証**:
   ```bash
   # 📊 メタデータファイルを検索・検証
   echo "📊 メタデータファイル検証中..."
   
   metadata_file="docs/use_cases/issue-${issue_list}-${feature_name}.json"
   
   if [[ ! -f "$metadata_file" ]]; then
       echo "エラー: メタデータファイルが見つかりません: $metadata_file"
       echo "💡 先に /create-use-case コマンドを実行してください"
       execute_rollback "metadata_file_missing"
       exit 1
   fi
   
   # メタデータファイル形式を検証
   if ! validate_json_file "$metadata_file"; then
       echo "エラー: メタデータファイルの形式が不正です: $metadata_file"
       execute_rollback "metadata_file_invalid"
       exit 1
   fi
   
   # ドメインモデリングが既に完了しているかチェック
   domain_status=$(jq -r '.phases.domain_model.created // false' "$metadata_file" 2>/dev/null)
   if [[ "$domain_status" == "true" ]]; then
       echo "⚠️  Issue #${issue_list} のドメインモデルは既に設計されています"
       echo "既存の設計を上書きしますか？ (y/N): "
       read -n 1 -r
       echo
       if [[ ! $REPLY =~ ^[Yy]$ ]]; then
           echo "ドメインモデル設計をキャンセルしました"
           commit_transaction
           exit 0
       fi
       echo "🔄 既存のドメインモデルを上書きします"
   fi
   
   echo "✅ メタデータ検証完了"
   ```

4. **ユースケース仕様を読み取りドメイン概念を抽出**:
   ```bash
   # 📖 ユースケース仕様を読み取り・分析
   echo "📖 ユースケース仕様分析中..."
   
   # ドメインディレクトリを安全に作成
   if ! safe_mkdir "docs/domain"; then
       echo "エラー: ドメインディレクトリの作成に失敗しました"
       execute_rollback "domain_dir_creation_failed"
       exit 1
   fi
   
   # すべての仕様からドメイン概念を抽出
   all_entities=()
   all_value_objects=()
   all_domain_services=()
   all_business_rules=()
   
   for spec_file in "${found_specs[@]}"; do
       echo "  📋 分析中: $(basename "$spec_file")"
       
       if ! check_file_permissions "$spec_file" "read"; then
           echo "エラー: 仕様ファイルの読み取り権限がありません: $spec_file"
           execute_rollback "spec_file_access_denied"
           exit 1
       fi
       
       # ドメイン概念セクションからエンティティを抽出
       entities=$(grep -A 20 "## ドメイン概念\\|## Domain Concepts" "$spec_file" 2>/dev/null | \
                 grep -E "^- \\*\\*[A-Z][a-zA-Z]*\\*\\*:" | \
                 sed 's/^- \*\*\([^*]*\)\*\*:.*/\1/' || echo "")
       
       if [[ -n "$entities" ]]; then
           while IFS= read -r entity; do
               [[ -n "$entity" ]] && all_entities+=("$entity")
           done <<< "$entities"
       fi
       
       # シナリオからビジネスルールを抽出
       rules=$(grep -A 5 -B 2 "Then:" "$spec_file" 2>/dev/null | \
              grep -v "^--$" | \
              sed 's/^[[:space:]]*//' || echo "")
       
       if [[ -n "$rules" ]]; then
           all_business_rules+=("$rules")
       fi
   done
   
   # 重複を削除し検証
   unique_entities=($(printf '%s\n' "${all_entities[@]}" | sort -u))
   
   echo "  🎯 抽出された概念:"
   echo "    - エンティティ: ${#unique_entities[@]} 個"
   echo "    - ビジネスルール: ${#all_business_rules[@]} 個"
   
   if [[ ${#unique_entities[@]} -eq 0 ]]; then
       echo "⚠️  ドメイン概念が抽出できませんでした"
       echo "仕様書に '## ドメイン概念' セクションを追加することを推奨します"
   fi
   
   echo "✅ 仕様分析完了"
   ```

5. **ドメインモデル設計文書の作成**:
   ```bash
   # 🏗️ 包括的なドメインモデル設計を作成
   echo "🏗️ ドメインモデル設計文書作成中..."
   
   design_file="docs/domain/issue-${issue_list}-domain-model.md"
   
   # ドメインモデル内容を作成
   domain_model_content="# ドメインモデル設計: $feature_name

**Issues**: $(printf '#%s ' "${issue_numbers[@]}")
**仕様**: docs/use_cases/issue-${issue_list}-${feature_name}.md
**作成日時**: $(date)

## 概要

このドメインモデルは、$(printf 'Issue #%s, ' "${issue_numbers[@]}" | sed 's/, $//')の要件に基づいて設計されています。
DDD（ドメイン駆動設計）の原則に従い、ビジネスロジックを中心とした設計を行います。

## エンティティ

$(if [[ ${#unique_entities[@]} -gt 0 ]]; then
    for entity in "${unique_entities[@]}"; do
        echo "### $entity

- **責務**: ${entity}に関連するビジネスロジックの管理
- **属性**:
  - id: EntityId (一意識別子)
  - created_at: DateTime (作成日時)
  - updated_at: DateTime (更新日時)
  - # TODO: ビジネス要件に基づいて属性を追加
- **振る舞い**:
  - create(): 新しい${entity}を作成
  - update(): ${entity}の情報を更新
  - # TODO: ビジネス要件に基づいてメソッドを追加
- **不変条件**:
  - idは一意でなければならない
  - created_atは未来日時ではならない
  - # TODO: ビジネスルールに基づいて制約を追加
"
    done
else
    echo "### 主要エンティティ

- **責務**: ビジネスロジックの中心となるエンティティ
- **属性**:
  - id: EntityId (一意識別子)
  - # TODO: 仕様に基づいて属性を定義
- **振る舞い**:
  - # TODO: ビジネス操作を定義
- **不変条件**:
  - # TODO: ビジネスルールを定義
"
fi)

## 値オブジェクト

### EntityId
- **責務**: エンティティの一意識別
- **属性**:
  - value: string (UUID形式)
- **振る舞い**:
  - generate(): 新しいIDを生成
  - equals(): ID同士の比較
- **不変条件**:
  - 値は有効なUUID形式でなければならない
  - 空文字やnullは許可されない

### Email（例）
- **責務**: メールアドレスの妥当性保証
- **属性**:
  - value: string
- **振る舞い**:
  - validate(): メールアドレス形式の検証
- **不変条件**:
  - RFC 5322に準拠したメールアドレス形式
  - 最大長255文字

## ドメインサービス

### ${feature_name}DomainService
- **責務**: ${feature_name}に関する複雑なビジネスロジック
- **メソッド**:
  - process${feature_name}(input: InputData): Result - ${feature_name}の主要処理
  - validate${feature_name}Rules(entity: Entity): ValidationResult - ビジネスルール検証

## リポジトリインターフェース

$(if [[ ${#unique_entities[@]} -gt 0 ]]; then
    for entity in "${unique_entities[@]}"; do
        echo "### ${entity}Repository

- **責務**: ${entity}の永続化とデータアクセス
- **メソッド**:
  - save(entity: $entity): void - ${entity}の保存
  - findById(id: EntityId): Optional<$entity> - IDによる検索
  - findAll(): List<$entity> - 全${entity}の取得
  - delete(id: EntityId): void - ${entity}の削除
"
    done
else
    echo "### MainEntityRepository

- **責務**: メインエンティティの永続化
- **メソッド**:
  - save(entity: Entity): void
  - findById(id: EntityId): Optional<Entity>
  - findAll(): List<Entity>
"
fi)

## 集約境界

$(if [[ ${#unique_entities[@]} -gt 0 ]]; then
    main_entity="${unique_entities[0]}"
    echo "- **集約ルート**: $main_entity
- **集約内エンティティ**: [$(IFS=', '; echo "${unique_entities[*]}")]
- **トランザクション境界**: 一つの集約内での操作は単一トランザクション内で実行
- **不変条件**: 集約内の整合性はルートエンティティが保証"
else
    echo "- **集約ルート**: MainEntity
- **集約内エンティティ**: [MainEntity]
- **トランザクション境界**: 集約境界内での整合性保証
- **不変条件**: TODO: 仕様に基づいて定義"
fi)

## ドメインイベント（必要な場合）

### ${feature_name}CreatedEvent
- **発生タイミング**: ${feature_name}が新規作成された時
- **含まれる情報**:
  - entityId: EntityId - 作成されたエンティティのID
  - createdAt: DateTime - 作成日時
  - # TODO: 必要な追加情報

### ${feature_name}UpdatedEvent
- **発生タイミング**: ${feature_name}が更新された時
- **含まれる情報**:
  - entityId: EntityId - 更新されたエンティティのID
  - updatedAt: DateTime - 更新日時
  - changes: List<FieldChange> - 変更内容

## 設計決定の根拠

### エンティティ vs 値オブジェクト
- **エンティティとした理由**: 
  $(for entity in "${unique_entities[@]:0:3}"; do
      echo "- $entity: ライフサイクルを持ち、一意性が重要なため"
  done)

### 集約境界の決定
- **集約サイズ**: ビジネス不変条件を維持する最小単位で設計
- **トランザクション境界**: 一貫性が必要な範囲で集約を定義

### リポジトリパターンの採用
- **理由**: ドメイン層とインフラ層の分離
- **利点**: テスタビリティとデータアクセス技術の変更容易性

## 実装時の注意点

### ドメイン層の純粋性
- 外部ライブラリへの依存を避ける
- インフラストラクチャへの関心事を排除
- ビジネスロジックのみに集中

### テスト戦略
- 単体テスト: 各エンティティ・値オブジェクトの振る舞い
- ドメインサービステスト: 複雑なビジネスロジック
- 集約テスト: 不変条件の検証

## 次のステップ

1. **TDDサイクル開始**: \`/create-tests $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')\`
2. **ドメイン層実装**: \`/implement-domain $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')\`
3. **アーキテクチャ検証**: 依存関係の方向とレイヤー分離の確認

## 備考・質問事項

- [ ] ステークホルダーレビュー待ち
- [ ] パフォーマンス要件の確認
- [ ] セキュリティ要件の検討
- [ ] 既存システムとの統合考慮

---

**設計者**: $(git config user.name || echo "Unknown")
**レビュー状況**: 未レビュー
**承認状況**: 未承認
**実装準備**: TDD実装待ち
"
   
   # ドメインモデル設計ファイルを安全に作成
   if ! safe_create_file "$design_file" "$domain_model_content" true; then
       echo "エラー: ドメインモデル設計ファイルの作成に失敗しました"
       execute_rollback "design_file_creation_failed"
       exit 1
   fi
   
   add_rollback "rm -f '$design_file'" "Remove created domain model design"
   echo "✅ ドメインモデル設計文書作成完了: $design_file"
   ```

6. **メタデータとステータス追跡の更新**:
   ```bash
   # 📊 ドメインモデリング完了でメタデータを更新
   echo "📊 メタデータ更新中..."
   
   if ! update_metadata_atomic "$metadata_file" \
       '.phases.domain_model.created = true | 
        .phases.domain_model.approved = false |
        .phases.domain_model.created_at = "'"$(date -u +%Y-%m-%dT%H:%M:%SZ)"'" |
        .updated_at = "'"$(date -u +%Y-%m-%dT%H:%M:%SZ)"'" |
        .spec_files.domain_model = "'"$design_file"'" |
        .phase = "domain_model_created" |
        .next_commands = ["create-tests", "use-case-status"]'; then
       echo "エラー: メタデータの更新に失敗しました"
       execute_rollback "metadata_update_failed"
       exit 1
   fi
   
   echo "✅ メタデータ更新完了"
   ```

7. **ユースケースインデックスの更新とGitコミット**:
   ```bash
   # 📚 ユースケースインデックスを更新
   echo "📚 ユースケースインデックス更新中..."
   
   use_cases_index="docs/use_cases/index.md"
   if [[ -f "$use_cases_index" ]]; then
       # バックアップを作成
       backup_file="${use_cases_index}.backup.$(date +%Y%m%d_%H%M%S)"
       if ! cp "$use_cases_index" "$backup_file"; then
           echo "エラー: インデックスファイルのバックアップ作成に失敗しました"
           execute_rollback "index_backup_failed"
           exit 1
       fi
       add_rollback "mv '$backup_file' '$use_cases_index'" "Restore index backup"
       
       # 機能のステータスを更新
       feature_line="\\[${feature_name}\\]"
       updated_line="- [${feature_name}]($(basename "${found_specs[0]}")) - Issues: $(printf '#%s ' "${issue_numbers[@]}")- Phase: domain_model_created, Design: ✅)"
       
       if ! sed -i "s|.*${feature_line}.*|${updated_line}|" "$use_cases_index"; then
           echo "エラー: インデックスファイルの更新に失敗しました"
           execute_rollback "index_update_failed"
           exit 1
       fi
       
       echo "✅ インデックス更新完了"
   fi
   
   # 💾 ドメインモデル設計をコミット
   echo "💾 ドメインモデル設計をコミット中..."
   
   commit_message="feat: design domain model for $(printf 'issue #%s ' "${issue_numbers[@]}")- ${feature_name}

Domain Model Design Summary:
- Feature: ${feature_name}
- Issues: $(printf '#%s ' "${issue_numbers[@]}")
- Entities: ${#unique_entities[@]} identified
- Design Document: $design_file

Design includes:
- Entity definitions with responsibilities and invariants
- Value objects for data integrity
- Domain services for complex business logic
- Repository interfaces for persistence
- Aggregate boundaries definition
- Domain events for system integration

Ready for TDD implementation cycle.
"
   
   files_to_commit=("$design_file" "$metadata_file")
   if [[ -f "$use_cases_index" ]]; then
       files_to_commit+=("$use_cases_index")
   fi
   
   if ! safe_git_commit "$commit_message" "${files_to_commit[@]}"; then
       echo "エラー: コミットに失敗しました"
       execute_rollback "commit_failed"
       exit 1
   fi
   
   add_rollback "git reset --hard HEAD~1" "Undo domain model design commit"
   echo "✅ コミット完了"
   ```

8. **GitHub Issueの更新**:
   ```bash
   # 🎫 ドメインモデル完了でGitHub Issueを更新
   echo "🎫 GitHubイシュー更新中..."
   
   for issue_num in "${issue_numbers[@]}"; do
       echo "  📝 Issue #$issue_num コメント追加中..."
       
       issue_comment="🏗️ **ドメインモデル設計完了**

ドメインモデルの設計が完了しました。

## 📋 設計文書
- **ファイル**: [$design_file]($design_file)
- **作成日時**: $(date)

## 🎯 設計内容
- **エンティティ**: ${#unique_entities[@]} 個特定
- **ドメイン構造**: 完全なクリーンアーキテクチャ対応
- **ビジネスルール**: 仕様から抽出・整理済み

## 📊 実装準備状況
- [x] ユースケース仕様作成
- [x] ドメインモデル設計
- [ ] TDDテスト作成
- [ ] ドメイン層実装
- [ ] アプリケーション層実装

## 🚀 次のステップ

TDDサイクルを開始してください：
\`\`\`bash
/create-tests $issue_num
\`\`\`

## 📚 関連ドキュメント
- [ドメインモデル設計]($design_file)
- [ユースケース仕様]($(basename "${found_specs[0]}" .md).md)

---
**Phase**: domain_model_created → 次: create_tests
"
       
       if ! safe_add_issue_comment "$issue_num" "$issue_comment"; then
           echo "    ⚠️  Issue #$issue_num へのコメント追加に失敗しました（続行します）"
       else
           echo "    ✅ Issue #$issue_num コメント追加完了"
       fi
   done
   
   echo "✅ GitHub イシュー更新完了"
   ```

9. **最終成功とガイダンス**:
    ```bash
    # 🎉 トランザクションコミット（成功！）
    if commit_transaction; then
        echo ""
        echo "🎉 ドメインモデル設計完了!"
        echo "============================================="
        echo "🏗️ 機能名: $feature_name"
        echo "🎫 対象イシュー: $(printf '#%s ' "${issue_numbers[@]}")"
        echo "📊 特定エンティティ: ${#unique_entities[@]} 個"
        echo ""
        echo "📋 設計文書:"
        echo "   - ドメインモデル: $design_file"
        echo "   - メタデータ: $metadata_file"
        echo ""
        echo "🎯 設計内容:"
        if [[ ${#unique_entities[@]} -gt 0 ]]; then
            echo "   エンティティ:"
            printf '     - %s\n' "${unique_entities[@]:0:5}"  # 最初の5つを表示
            [[ ${#unique_entities[@]} -gt 5 ]] && echo "     - ... (${#unique_entities[@]} 個)"
        fi
        echo "   - 値オブジェクト: EntityId, Email等"
        echo "   - ドメインサービス: ${feature_name}DomainService"
        echo "   - リポジトリIF: エンティティ対応"
        echo "   - ドメインイベント: 作成・更新イベント"
        echo ""
        echo "🚀 次のステップ:"
        echo "   1. TDDテスト作成: /create-tests $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
        echo "   2. 進捗確認: /use-case-status $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
        echo "   3. レビュー要請: チームでドメインモデル設計をレビュー"
        echo ""
        echo "🚨 MANDATORY FOR CLAUDE CODE: SCENARIO EVOLUTION CHECK"
        echo "   Claude Code: 設計中に新要件・制約・エッジケース発見時は"
        echo "   作業を中断して /evolve-scenarios <feature-name> を実行すること"
        echo "   ユーザー: 同様の対応をお願いします"
        echo "   CRITICAL: 新シナリオの放置は致命的な実装漏れを引き起こします"
        echo ""
        echo "💡 設計レビューポイント:"
        echo "   - ユビキタス言語の一貫性"
        echo "   - 集約境界の適切性"
        echo "   - ビジネスルールの網羅性"
        echo "   - エンティティ vs 値オブジェクトの分類"
        echo ""
        
        # 操作ログサマリーを表示
        echo "📊 操作ログサマリー:"
        show_github_operation_log | tail -2
        show_git_operation_log | tail -2
        show_transaction_log | tail -2
        
        echo ""
        echo "✅ DDD原則に基づくドメインモデル設計完了 - TDD実装準備完了!"
        
    else
        echo "❌ トランザクション コミット失敗"
        exit 1
    fi
    ```

重要な注意事項:
- **設計のみ** - コードの実装やプレースホルダーファイルを作成しない
- 技術実装ではなくドメインロジックに焦点を当てる
- 仕様からのユビキタス言語を使用
- 集約を小さく結束度高く保つ
- 明確な境界と不変条件を定義
- 後の実装のための包括的な設計文書を作成
- すべてのユーザー向け出力は**日本語**である必要があります