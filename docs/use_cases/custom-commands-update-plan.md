# カスタムコマンド改修計画

## 改修の目的
1. **実行履歴の完全な追跡**: どのコマンドが実行済みか明確に把握
2. **JSONフォーマットの標準化**: 一貫性のあるデータ構造の実装
3. **進捗の可視化**: TDD/DDDプロセスの進行状況を即座に確認

## 改修対象コマンド一覧

### Phase 1: コア機能の改修（優先度：高）

#### 1. `03-create-use-case`
**改修内容**:
- 新しい標準フォーマットでJSONを作成
- `execution_history`セクションの初期化
- コマンド実行履歴の自動記録

**変更箇所**:
```python
# 新フォーマットでのJSON作成
use_case_data = {
    "metadata": {...},
    "scenarios": {...},
    "execution_history": {
        "commands_executed": [{
            "command": "/create-use-case",
            "executed_at": datetime.now().isoformat(),
            "status": "success",
            "files_affected": [json_file_path]
        }],
        "last_command": "/create-use-case"
    }
}
```

#### 2. `05-create-tests`
**改修内容**:
- `execution_history.tdd_phases.RED`の更新
- テストファイル作成の記録

#### 3. `06-implement-domain`
**改修内容**:
- `execution_history.tdd_phases.GREEN`の更新
- ドメイン実装ファイルの記録

#### 4. `11-refactor`
**改修内容**:
- `execution_history.tdd_phases.REFACTOR`の更新
- リファクタリングで変更されたファイルの記録

### Phase 2: ステータス表示の改修（優先度：中）

#### 5. `16-use-case-status`
**改修内容**:
- 実行履歴から進捗状況を表示
- 未実行コマンドのハイライト表示
- TDDフェーズの視覚的表示

**新しい出力形式**:
```
📊 Issue #2: PostgreSQL Database Environment
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 TDD進捗:
  RED Phase    : ✅ 完了 (2024-01-15 10:30)
  GREEN Phase  : 🔄 進行中
  REFACTOR     : ⏳ 未開始

📝 実行済みコマンド:
  ✅ /create-use-case 2      (2024-01-15 09:00)
  ✅ /domain-modeling 2      (2024-01-15 09:30)
  ✅ /create-tests 2         (2024-01-15 10:30)
  🔄 /implement-domain 2     (実行中)

⏭️ 次の推奨コマンド:
  - /implement-usecase 2
  - /implement-infra 2
```

#### 6. `17-project-status`
**改修内容**:
- 全イシューの実行状況を集計表示
- プロジェクト全体の進捗率計算

### Phase 3: 互換性とユーティリティ（優先度：低）

#### 7. JSONフォーマット変換ユーティリティ
**新規作成**:
- `.claude/commands/tdd-ddd-layered-expert/98-migrate-json-format`
- 旧フォーマットから新フォーマットへの自動変換

#### 8. 実行履歴分析ツール
**新規作成**:
- `.claude/commands/tdd-ddd-layered-expert/97-analyze-execution-history`
- 実行時間の分析
- ボトルネックの特定

## 実装アプローチ

### 1. 共通ユーティリティ関数の作成
```python
def update_execution_history(json_path, command_name, status="success", files_affected=None):
    """実行履歴を更新する共通関数"""
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    if 'execution_history' not in data:
        data['execution_history'] = {
            "tdd_phases": {},
            "commands_executed": []
        }
    
    data['execution_history']['commands_executed'].append({
        "command": command_name,
        "executed_at": datetime.now().isoformat(),
        "status": status,
        "files_affected": files_affected or []
    })
    
    data['execution_history']['last_command'] = command_name
    
    with open(json_path, 'w') as f:
        json.dump(data, f, indent=2)
```

### 2. 後方互換性の維持
```python
def load_use_case_json(json_path):
    """新旧両フォーマットを読み込む"""
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    # 旧フォーマットの検出と変換
    if 'use_case_metadata' in data:
        data['metadata'] = data.pop('use_case_metadata')
    
    if 'scenarios' in data:
        if 'main_success' in data['scenarios']:
            data['scenarios']['main_scenarios'] = data['scenarios'].pop('main_success')
        if 'alternative_flows' in data['scenarios']:
            data['scenarios']['alternative_scenarios'] = data['scenarios'].pop('alternative_flows')
    
    return data
```

## 実施スケジュール

### Week 1: 基盤整備
- [ ] 共通ユーティリティ関数の実装
- [ ] テスト環境の準備
- [ ] バックアップの作成

### Week 2: Phase 1実装
- [ ] コア機能コマンドの改修
- [ ] 単体テストの実装
- [ ] 統合テストの実施

### Week 3: Phase 2実装
- [ ] ステータス表示コマンドの改修
- [ ] UIの改善
- [ ] ドキュメントの更新

### Week 4: Phase 3とリリース
- [ ] ユーティリティツールの作成
- [ ] 全体テストの実施
- [ ] 移行ガイドの最終化

## リスクと対策

1. **既存ワークフローへの影響**
   - 対策: 後方互換性の維持、段階的な移行

2. **パフォーマンスの低下**
   - 対策: 実行履歴の効率的な管理、定期的なクリーンアップ

3. **データ整合性の問題**
   - 対策: バリデーションの強化、自動修復機能

## 成功指標

1. **実行履歴の完全性**: 100%のコマンド実行が記録される
2. **互換性**: 既存のワークフローが中断なく動作
3. **パフォーマンス**: コマンド実行時間の増加が5%以内
4. **ユーザビリティ**: 進捗状況が一目で把握可能