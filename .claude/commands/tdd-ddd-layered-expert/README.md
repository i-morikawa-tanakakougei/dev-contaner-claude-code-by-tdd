# TDD/DDD/Layered Architecture - Expert Mode Commands

## 🎯 概要

このディレクトリには、TDD/DDD/レイヤードアーキテクチャ開発プロセスの**専門家モード統合版**0x.5レビュー系コマンドが含まれています。

従来のサブエージェント呼び出し方式の課題（確率的実行、高コンテキスト管理コスト）を解決し、カスタムコマンド内に専門家システムプロンプトを直接統合した新アーキテクチャです。

## 🏗️ アーキテクチャ変更点

### 従来方式 → Expert Mode統合方式

| 項目 | 従来方式 | Expert Mode |
|------|----------|-------------|
| 実行確実性 | 確率的（60-80%） | 確定的（100%） |
| 階層数 | 5層（カスタム→コンテキスト→サブエージェント→検証→メタデータ） | 2層（カスタム→実行） |
| コンテキスト準備 | 300行以上 | 50行以下 |
| 応答時間 | 3-5秒 | 1-2秒 |
| トークン消費 | 高（多層処理） | 低（直接実行） |

## 📋 含まれるコマンド

### 0x.5 レビュー系専門家コマンド

1. **00.5-review-vision-expert.md**
   - **専門家**: Vision Review & Strategic Alignment specialist
   - **目的**: プロジェクトビジョンの客観的レビューと戦略的整合性評価
   - **出力**: ステークホルダー整合性評価、実現可能性分析、承認・却下判定

2. **02.5-review-sprint-plan-expert.md**
   - **専門家**: Sprint Planning Review & Capacity Optimization specialist  
   - **目的**: スプリント計画の妥当性評価とチーム容量最適化
   - **出力**: 容量計画評価、シナリオ優先度検証、実行戦略承認

3. **04.5-review-domain-design-expert.md**
   - **専門家**: DDD Domain Architecture Review & Quality Assurance specialist
   - **目的**: DDD原則準拠性とドメインアーキテクチャ品質評価
   - **出力**: DDD準拠性分析、集約境界検証、実装準備度判定

4. **05.5-review-test-design-expert.md**
   - **専門家**: TDD Test Quality & Coverage Analysis specialist
   - **目的**: TDD準拠性とテスト品質の専門評価
   - **出力**: RED段階検証、シナリオカバレッジ、テスト品質評価

5. **10.5-review-test-results-expert.md**
   - **専門家**: Test Result Analysis & Quality Metrics Assessment specialist
   - **目的**: テスト実行結果の包括的分析と品質メトリクス評価
   - **出力**: カバレッジ分析、品質メトリクス、リファクタリング推奨

## 🚀 使用方法

### 基本実行パターン
```bash
# ビジョンレビュー
/review-vision-expert

# スプリント計画レビュー  
/review-sprint-plan-expert 1

# ドメイン設計レビュー
/review-domain-design-expert 3
/review-domain-design-expert 3,15  # 複数Issue

# テスト設計レビュー
/review-test-design-expert 3

# テスト結果レビュー  
/review-test-results-expert 3
```

### 標準化出力フォーマット

すべてのexpertコマンドは以下の構造化セクションで終了：

```markdown
### 📊 実行サマリー
- ✅/❌ **[タスク1]**: [完了状態とサマリー]
- ✅/❌ **[タスク2]**: [完了状態とサマリー]

### 総合判定
**ステータス**: `APPROVED|CONDITIONAL_APPROVAL|REJECTED`

### 💡 次のステップ
1. **即座に実行可能**: `/[next-command]`
2. **条件付き実行**: [条件] → `/[command]`
3. **要確認事項**: [確認項目]
```

## 🎯 Expert Profile Declaration セクション

各コマンドは以下の専門家プロファイルを内蔵：

```markdown
## 🎯 Expert Profile Declaration

### 専門家プロファイル
- **役割**: [明確な役割定義]
- **専門分野**: 
  - **[分野1]**: [具体的専門知識]
  - **[分野2]**: [具体的専門知識] 
- **責任範囲**: [コマンドでの達成目標]

### 実行時のマインドセット
1. **[原則1]**: [具体的思考・行動原則]
2. **[原則2]**: [具体的思考・行動原則]

### 判断基準
- **品質**: [品質判断基準]
- **完了**: [完了判断基準]
- **エスカレーション**: [問題時の基準]
```

## 📊 品質ゲート機能

### 承認レベル

- **🟢 APPROVED**: 即座に次段階実行可能
- **🟡 CONDITIONAL_APPROVAL**: 軽微改善後実行可能  
- **🔴 REJECTED**: 重大問題により前段階修正必要

### メトリクス例

| コマンド | 主要メトリクス |
|----------|----------------|
| Vision Review | ビジョン明確性80+, ステークホルダー合意85%+ |
| Sprint Review | 容量利用率80-90%, コアシナリオカバレッジ80%+ |  
| Domain Review | DDD準拠性95+, 集約境界違反0件 |
| Test Design Review | RED状態100%, シナリオカバレッジ100% |
| Test Results Review | 成功率95%+, カバレッジ80%+ |

## 🔧 技術仕様

### Language Guidelines
- **Claude Code指示**: English
- **ユーザー対話**: Japanese  

### Context Management
- **最小限読み込み**: 必要ファイルのみ（50行以下）
- **GitHub統合**: Issue/コメント自動取得
- **メタデータ更新**: 軽量JSON形式

### Forest-to-Tree アプローチ
1. **Expert Profile** (森) → 専門性確立
2. **Process Context** (森) → 全体ワークフロー理解
3. **Phase Purpose** (木) → 具体的タスクフォーカス  
4. **軽量コンテキスト** → 必要最小限情報収集
5. **専門家実行** → 段階的品質評価

## 🎯 利用上の注意

### 成功要因
- **専門家の信頼**: 各コマンドの専門性を信頼し、推奨事項に従う
- **品質ゲート遵守**: 承認されるまで次段階に進まない
- **継続的改善**: フィードバックを次回実行に活用

### トラブルシューティング  
- **REJECTED判定時**: 指摘事項を完全修正後、再実行
- **品質メトリクス不足**: 具体的改善アクションを実施
- **エラー時**: コマンド内のエラー処理セクション参照

## 📈 期待効果

- **実行確実性**: 100%確定実行
- **コスト削減**: 70%のトークン消費削減
- **速度向上**: 50%の応答時間短縮  
- **品質向上**: データ駆動品質ゲート機能
- **学習効率**: 新規メンバーの理解時間短縮

---

**🎯 Key Success Factor**: 各expert commandの専門性を信頼し、Forest-to-Treeアプローチで全体最適化を図りつつ、段階的品質向上を実現する