# 新カスタムコマンド構造仕様

## 🏗️ 基本構造テンプレート

```markdown
# コマンド名: XX-command-name

## 🎯 Expert Profile Declaration
[Define expert role and mindset clearly]
[Claude Code instructions should be in English]

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT
[Overall development flow visibility]
[Architecture principles and current position]

## 🎯 PHASE PURPOSE: [SPECIFIC PHASE]
[Phase purpose and scope definition]
[Implementation targets and quality standards]

## 📋 軽量コンテキスト管理
[必要最小限のコンテキスト読み込み]

## GitHub Issue Integration
[GitHub issue and comment retrieval with recency priority]

## 🚀 専門家実行フロー
[専門家として実行する具体的なステップ]
[User interaction should be in Japanese]

## ✅ 内蔵品質保証
[自己診断とチェックリスト]

## 📊 標準化出力フォーマット
[一貫した結果報告形式]
```

## 📝 詳細セクション仕様

### 1. Expert Profile Declaration Section

```markdown
## 🎯 Expert Profile Declaration

During command execution, you act as a **[Expert Title]** specialist.

**Language Guidelines:**
- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### 専門家プロファイル
- **役割**: [明確な役割定義]
- **専門分野**: 
  - [専門分野1]: [具体的な専門知識]
  - [専門分野2]: [具体的な専門知識]
  - [専門分野3]: [具体的な専門知識]
- **責任範囲**: [このコマンドで達成すべきこと]

### 実行時のマインドセット
1. **[原則1]**: [具体的な思考・行動原則]
2. **[原則2]**: [具体的な思考・行動原則]
3. **[原則3]**: [具体的な思考・行動原則]

### 判断基準
- **品質**: [品質に関する判断基準]
- **完了**: [タスク完了の判断基準]
- **エスカレーション**: [問題時の判断基準]
```

### 2. Lightweight Context Management Section

```markdown
## 📋 軽量コンテキスト管理

### Required Reading (Minimal)
```bash
# Project state (only if exists)
if [[ -f "docs/metadata/project-state.json" ]]; then
    PROJECT_STATE=$(cat docs/metadata/project-state.json)
    CURRENT_PHASE=$(echo $PROJECT_STATE | jq -r '.current_phase')
fi

# Execution history (latest 5 entries only)
RECENT_HISTORY=$(tail -5 .claude/context/execution-history.jsonl 2>/dev/null || echo "[]")
```

### Optional Reading (As Needed)
- Related documents: `docs/[relevant-path]/`
- Previous phase deliverables: Dynamically determined based on conditions

### GitHub Issue Context Loading
```bash
# Load GitHub issue with comments (if issue number provided)
if [[ -n "$ISSUE_NUMBER" ]]; then
    # Retrieve issue details
    gh issue view $ISSUE_NUMBER --json title,body,comments
    
    # Priority: Recent comments are more important
    # Sort comments by created date (desc) and prioritize latest specifications
    gh issue view $ISSUE_NUMBER --json comments --jq '.comments | sort_by(.createdAt) | reverse'
fi
```

### 3. Expert Execution Flow Section

```markdown
## 🚀 専門家実行フロー

### Phase 1: 分析と理解
**専門家として以下を分析:**
1. [分析項目1]
   - 確認ポイント: [具体的な確認内容]
   - 判断基準: [判断のための基準]
   
2. [分析項目2]
   - 確認ポイント: [具体的な確認内容]
   - 判断基準: [判断のための基準]

### Phase 2: 設計と計画
**専門家として以下を設計:**
1. [設計項目1]
   ```
   [具体的な設計テンプレートや例]
   ```
   
2. [設計項目2]
   ```
   [具体的な設計テンプレートや例]
   ```

### Phase 3: 実装と実行
**専門家として以下を実行:**
1. [実行ステップ1]
   - アクション: [具体的なアクション]
   - 期待結果: [期待される結果]
   
2. [実行ステップ2]
   - アクション: [具体的なアクション]
   - 期待結果: [期待される結果]
```

### 4. Built-in Quality Assurance Section

```markdown
## ✅ 内蔵品質保証

### 自己診断チェックリスト
**必須項目（MUST）:**
- [ ] [必須チェック項目1]
- [ ] [必須チェック項目2]
- [ ] [必須チェック項目3]

**推奨項目（SHOULD）:**
- [ ] [推奨チェック項目1]
- [ ] [推奨チェック項目2]

### 品質メトリクス
| 指標 | 目標値 | 実績値 | 判定 |
|------|--------|--------|------|
| [指標1] | [目標] | [実績] | ✅/❌ |
| [指標2] | [目標] | [実績] | ✅/❌ |

### エラー処理
**想定されるエラーと対処:**
1. [エラーケース1]: [対処方法]
2. [エラーケース2]: [対処方法]
```

### 5. Standardized Output Format Section

```markdown
## 📊 標準化出力フォーマット

### 実行サマリー
- ✅ **[タスク1]**: [完了状態とサマリー]
- ✅ **[タスク2]**: [完了状態とサマリー]
- ⚠️ **[タスク3]**: [警告や注意事項]

### 成果物
**作成されたファイル:**
- `path/to/file1.md`: [ファイルの説明]
- `path/to/file2.json`: [ファイルの説明]

### 総合判定
**ステータス**: `[SUCCESS|PARTIAL|FAILED]`
**品質スコア**: [スコア]/100
**次フェーズ準備**: `[READY|CONDITIONAL|NOT_READY]`

### 次のステップ
1. **即座に実行可能**: `/[next-command]`
2. **条件付き実行**: [条件説明] → `/[command]`
3. **要確認事項**: [確認が必要な事項]

### メタデータ更新
```json
{
  "command_executed": "[command-name]",
  "timestamp": "[ISO-8601]",
  "status": "[status]",
  "next_recommended": ["command1", "command2"],
  "quality_score": [score]
}
```
```

## 🎨 コマンドタイプ別カスタマイズ

### Type A: 分析・設計系コマンド
```markdown
重点セクション:
- 専門家モード宣言: 分析力と設計力を強調
- 実行フロー: 分析→設計→文書化の流れ
- 品質保証: 設計原則の遵守チェック
```

### Type B: 実装系コマンド
```markdown
重点セクション:
- 専門家モード宣言: 実装スキルと品質基準
- 実行フロー: TDD/DDDの実践手順
- 品質保証: テストカバレッジとコード品質
```

### Type C: レビュー・検証系コマンド
```markdown
重点セクション:
- 専門家モード宣言: 批判的思考と改善提案
- 実行フロー: 多角的評価と判定
- 品質保証: レビュー基準の適用
```

## 🔧 実装ガイドライン

### コマンド作成時の原則

1. **シンプルさ優先**
   - 1コマンド = 1ファイル
   - 外部依存の最小化
   - 明確な入出力

2. **専門家品質の保証**
   - 詳細な専門家プロンプト
   - 具体的な判断基準
   - 実例ベースのガイダンス

3. **保守性の確保**
   - 自己完結型ドキュメント
   - バージョン管理への配慮
   - 後方互換性の考慮

### パフォーマンス最適化

```markdown
## 最適化ポイント

1. **コンテキスト読み込み**
   - 遅延読み込み: 必要時のみ読み込む
   - キャッシュ活用: 繰り返し参照データ
   - 部分読み込み: 大きなファイルの必要部分のみ

2. **実行効率**
   - 並列処理可能なタスクの識別
   - 早期リターン: 条件を満たさない場合
   - バッチ処理: 類似タスクのグループ化

3. **出力最適化**
   - 構造化された出力
   - 必要十分な情報量
   - 次アクションの明確化
```

## 📏 品質基準

### コマンド品質チェックリスト

- [ ] **専門家モードが明確に定義されている**
- [ ] **実行フローが具体的で実行可能**
- [ ] **品質チェックが組み込まれている**
- [ ] **出力フォーマットが標準化されている**
- [ ] **エラー処理が考慮されている**
- [ ] **次のステップが明確**
- [ ] **メタデータ更新が含まれている**

### 成功指標

| 指標 | 目標 | 測定方法 |
|------|------|----------|
| 実行成功率 | 95%以上 | 成功実行数/総実行数 |
| 平均実行時間 | 2秒以内 | 実行時間の平均 |
| 品質スコア | 80点以上 | 内蔵チェックリストのスコア |
| ユーザー満足度 | 4.5/5.0 | フィードバック評価 |

## 🔄 バージョン管理

### バージョニング規則
```
v[major].[minor].[patch]
- major: 構造的な変更
- minor: 機能追加・改善
- patch: バグ修正・微調整
```

### 変更履歴テンプレート
```markdown
## 変更履歴

### v1.1.0 - 2024-XX-XX
- 追加: [新機能の説明]
- 改善: [改善内容]
- 修正: [バグ修正]
```

---

**次のドキュメント**: [03-migration-plan.md](./03-migration-plan.md) - 移行計画の詳細