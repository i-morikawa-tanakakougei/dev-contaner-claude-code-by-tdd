# Claude Code TDD/DDD/Layered タスクメタデータ駆動型確認システム設計

**設計日**: 2025-08-20  
**実証検証**: sync-verification-test (SUCCESS)  
**同期処理確認**: 完全同期実行を実証的に確認済み

## 🔍 現状分析と課題

### ✅ 現在の実装状況
1. **サブエージェント統合**: 全23個のTDD/DDD/Layeredエージェントが標準化完了
2. **基本確認機能**: ファイル生成確認、終了コード確認、メタデータ更新確認
3. **同期実行**: Task tool完全同期動作を実証的に確認（45秒実行、即座結果利用可能）

### ❌ 不足している機能
1. **タスクリスト項目の個別確認**: Critical/Important/Optional タスクの完了状態確認
2. **サブエージェント再実行メカニズム**: 結果不十分時の自動再試行
3. **詳細な処理内容確認**: エージェントが実際に実行した内容の検証
4. **標準化されたレポート形式**: ホスト側でルーチン処理可能な出力形式

## 🎯 設計目標

### **堅牢性とシンプルさの両立**
- **堅牢性**: Critical項目の確実な確認でシステム品質保証
- **シンプルさ**: 各コマンド10-20行追加程度の軽微な変更
- **保守性**: 共通ライブラリによる一元管理
- **拡張性**: 新機能追加時の最小限変更

## 🏗️ 解決案設計

### **コアアプローチ: "メタデータドリブン段階的確認"**

```bash
# 1. タスクメタデータを外部化
# 2. Critical項目のみホスト確認  
# 3. サブエージェント標準レポート形式
# 4. 共通パーサーでシンプル確認
# 5. 再実行メカニズム統合
```

## 📋 アーキテクチャ設計

### **1. タスクメタデータ定義システム**

#### 1.1 メタデータファイル構造
```json
// .claude/commands/tdd-ddd-layered/task-definitions/04.5-review-domain-design.json
{
  "command": "04.5-review-domain-design",
  "critical_tasks": [
    "ddd_compliance_check",
    "aggregate_boundary_validation", 
    "business_rules_placement"
  ],
  "important_tasks": [
    "entity_design_review",
    "value_object_validation"
  ],
  "optional_tasks": [
    "performance_assessment",
    "documentation_quality"
  ],
  "output_requirements": {
    "format": "structured_sections",
    "required_sections": ["実行サマリー", "総合判定", "次のステップ"],
    "critical_patterns": [
      "✅.*DDD準拠性",
      "✅.*集約境界", 
      "(APPROVED|CONDITIONAL|REJECTED)"
    ]
  }
}
```

#### 1.2 全コマンド対応メタデータ
```
.claude/commands/tdd-ddd-layered/task-definitions/
├── 04.5-review-domain-design.json     # ドメイン設計レビュー
├── 05.5-review-test-design.json       # テスト設計レビュー  
├── 10.5-review-test-results.json      # テスト結果レビュー
├── 12-evolve-scenarios.json           # シナリオ進化
└── [その他のコマンド定義...]
```

### **2. サブエージェント標準レポート形式**

#### 2.1 構造化出力テンプレート
```markdown
## 📊 実行サマリー
- ✅ Critical Task 1: DDD準拠性確認 → 完了
- ✅ Critical Task 2: 集約境界検証 → 完了  
- ⚠️ Critical Task 3: ビジネスルール配置 → 問題あり

## 📋 総合判定
**ステータス: CONDITIONAL_APPROVAL**

## 💡 次のステップ
1. ビジネスルール配置の修正
2. /create-tests での実装開始
```

#### 2.2 サブエージェント出力指示追加
```markdown
## 🎯 **STANDARDIZED OUTPUT REQUIREMENTS** (各エージェントに追加)

すべてのレビューレポートは以下の構造化セクションで終了してください：

### **📊 実行サマリー**
各Critical Taskの完了状態を明記

### **📋 総合判定** 
APPROVED/CONDITIONAL_APPROVAL/REJECTED のいずれかを明記

### **💡 次のステップ**
具体的なアクションアイテムを列挙
```

### **3. ホスト側確認システム**

#### 3.1 共通確認ライブラリ
```bash
# .claude/commands/tdd-ddd-layered/_task_verification.sh
source "$(dirname "${BASH_SOURCE[0]}")/_validate_structure.sh"

# メタデータ読み込み関数
load_task_metadata() {
    local command_name="$1"
    local metadata_file=".claude/commands/tdd-ddd-layered/task-definitions/${command_name}.json"
    
    if [[ -f "$metadata_file" ]]; then
        critical_tasks=($(jq -r '.critical_tasks[]' "$metadata_file"))
        critical_patterns=($(jq -r '.output_requirements.critical_patterns[]' "$metadata_file"))
    fi
}

# Critical tasks確認関数
verify_critical_tasks() {
    local command_name="$1" 
    local report_file="$2"
    
    load_task_metadata "$command_name"
    
    # パターンベース確認（堅牢で実装簡単）
    for pattern in "${critical_patterns[@]}"; do
        if ! grep -q "$pattern" "$report_file"; then
            verification_issues+=("Missing critical pattern: $pattern")
        fi
    done
    
    # 必須セクション確認
    if ! grep -q "📊 実行サマリー" "$report_file"; then
        verification_issues+=("実行サマリーセクションが見つかりません")
    fi
    
    if ! grep -q "📋 総合判定" "$report_file"; then
        verification_issues+=("総合判定セクションが見つかりません")
    fi
}

# 再実行機能
execute_agent_with_retry() {
    local agent_type="$1"
    local max_attempts="${2:-2}"
    local attempt=1
    
    while [[ $attempt -le $max_attempts ]]; do
        echo "🔄 エージェント実行試行 $attempt/$max_attempts..."
        
        if execute_agent "$agent_type"; then
            if verify_critical_tasks "$agent_type" "$latest_report"; then
                echo "✅ エージェント実行成功 (試行 $attempt)"
                return 0
            else
                echo "⚠️ 結果不十分 - 再試行準備中..."
                prepare_retry_context "$attempt" "${verification_issues[@]}"
            fi
        fi
        
        ((attempt++))
        sleep 2
    done
    
    echo "❌ 最大試行回数に達しました"
    return 1
}

# 再試行コンテキスト改善
prepare_retry_context() {
    local attempt="$1"
    shift
    local issues=("$@")
    local context_file="/workspace/.claude/context/current-command-context.json"
    
    local issues_str=$(IFS=', '; echo "${issues[*]}")
    
    jq --arg attempt "$attempt" \
       --arg issues "$issues_str" \
       '. + {
         "retry_attempt": $attempt,
         "previous_issues": $issues,
         "special_focus": "前回の不足項目に特に注意: " + $issues
       }' "$context_file" > "${context_file}.tmp" && \
    mv "${context_file}.tmp" "$context_file"
}
```

#### 3.2 各コマンドでの使用例
```bash
# 04.5-review-domain-design.md の Agent Result Verification セクション
source "$(dirname "${BASH_SOURCE[0]}")/_task_verification.sh"

echo "🔍 エージェント結果検証中..."
verification_issues=()

# 基本確認（既存）
if [[ ${#review_reports[@]} -eq 0 ]]; then
    verification_issues+=("レポートが生成されていません")
else
    # ✨ 新機能: Critical tasks verification with retry
    if ! execute_agent_with_retry "04.5-review-domain-design" 2; then
        echo "❌ エージェント実行に問題があります:"
        printf '  - %s\n' "${verification_issues[@]}"
        echo ""
        echo "💡 手動での問題解決が必要です:"
        echo "   1. 設計文書の再確認"
        echo "   2. /domain-modeling ${issue_numbers[*]} での再設計"
        echo "   3. このコマンドの再実行"
        exit 1
    fi
fi

echo "✅ エージェント結果検証完了"
```

## 🔧 実装方法

### **Phase 1: 基盤構築（2-3日）**

#### 1.1 共通ライブラリ作成
```bash
# 作成ファイル:
.claude/commands/tdd-ddd-layered/_task_verification.sh
.claude/commands/tdd-ddd-layered/task-definitions/
```

#### 1.2 主要3コマンドへの適用
- `04.5-review-domain-design.md`
- `05.5-review-test-design.md`  
- `10.5-review-test-results.md`

### **Phase 2: 標準化拡張（3-4日）**

#### 2.1 サブエージェント出力形式統一
各エージェントに `STANDARDIZED OUTPUT REQUIREMENTS` セクション追加

#### 2.2 残りコマンドへの適用
- `12-evolve-scenarios.md`
- その他必要に応じて拡張

### **Phase 3: 高度機能（1週間）**

#### 3.1 メタデータ駆動システム
JSONファイルベースのタスク定義システム実装

#### 3.2 インテリジェント再実行
問題分析と改善指示付き再実行機能

## 📊 技術的根拠

### **同期実行の実証確認済み**
```
実証テスト結果:
- Task tool実行時間: 45,261ms (45秒)
- ホスト待機: 完全同期確認
- 結果即座利用可能: 復帰後即座にファイルアクセス可能
- 競合状態: なし
```

### **実現可能性評価**
- **技術的実現性**: ✅ 100% (同期処理により確実な実装可能)
- **パフォーマンス**: ✅ 1-2秒以内での高速確認処理
- **保守性**: ✅ 共通ライブラリで重複排除
- **拡張性**: ✅ 新コマンド追加時数行で対応

## 🎯 期待効果

### **堅牢性向上**
- **Critical項目確実確認**: 最重要タスクの100%検証
- **自動回復機能**: 多くの問題を自動解決
- **品質保証**: エラー率大幅削減

### **シンプルさ維持**
- **軽微な変更**: 各コマンド10-20行追加のみ
- **統一インターフェース**: 学習コストなし
- **段階的導入**: リスク最小化

### **開発効率向上**
- **自動化**: 手動確認作業の削減
- **透明性**: 問題の早期発見と解決
- **信頼性**: 開発者の認知負荷軽減

## 🚀 実装ロードマップ

### **Step 1: 即効対応（今週）**
1. `_task_verification.sh` 作成
2. 主要3コマンドでの試験実装
3. 動作検証とフィードバック収集

### **Step 2: 段階展開（来週）**
1. サブエージェント出力形式統一
2. メタデータファイル作成
3. 再実行機能実装

### **Step 3: 全体統合（2週間後）**
1. 全コマンドへの適用
2. テスト自動化
3. ドキュメント整備

## 💡 推奨実装優先度

### 🔥 緊急度：高
- [ ] 共通ライブラリ `_task_verification.sh` 作成
- [ ] 主要3コマンドへの適用
- [ ] Critical項目確認機能実装

### ⚡ 緊急度：中  
- [ ] サブエージェント出力形式統一
- [ ] 再実行メカニズム実装
- [ ] メタデータファイルシステム

### 📋 緊急度：低
- [ ] 全コマンドへの適用
- [ ] インテリジェント再実行
- [ ] 高度な分析機能

## 🎉 成功指標

### **技術指標**
- Critical項目確認率: 100%
- 自動回復成功率: 80%以上
- 平均確認処理時間: 2秒以内

### **開発体験指標**  
- コマンド実行成功率向上: 30%以上
- エラー解決時間短縮: 50%以上
- 開発者満足度: 高評価

---

**次のアクション**: ユーザー精査後、Step 1から段階的実装開始

**実装準備状況**: ✅ 技術検証完了、設計確定、実装可能状態