# 🚀 TDD/DDD/レイヤードアーキテクチャ カスタムコマンド - クイックスタート

**5分で始めるTDD/DDD開発**

> 📖 初めての方向けの最小構成ガイド  
> 🎯 目的: 15分で最初の機能を完全実装  
> ✅ 結果: GitHubイシューからプルリクエストまで自動化

## 🎯 **まず覚える3つのコマンド**

```bash
# ステップ1: 最初の機能を作成
/create-use-case 1 user-login

# ステップ2: 実装を完了 (自動でTDD RED→GREEN→REFACTOR)
/implement-domain 1

# ステップ3: プルリクエスト作成
/create-pr 1
```

**これだけで完全な機能実装が完了します！**

---

## 🚀 **30秒セットアップ**

### 前提条件チェック
```bash
# GitHubログイン確認
gh auth status

# Pythonプロジェクト確認
ls pyproject.toml  # または requirements.txt
```

### 最初のコマンド実行
```bash
# GitHubイシュー #1 があることを確認してから実行
/create-use-case 1 your-feature-name
```

**✅ 成功すると以下が作成されます:**
- ユースケース仕様書
- メタデータファイル
- 機能用ブランチ

---

## 📋 **基本ワークフロー（推奨パターン）**

### **🎯 パターンA: シンプル機能開発**
```bash
# 1. 機能仕様作成（5分）
/create-use-case 1 login-functionality

# 2. ドメイン設計（3分）  
/domain-modeling 1

# 3. 実装完了（自動TDD）（10分）
/implement-domain 1
/implement-usecase 1
/implement-infra 1
/implement-presentation 1

# 4. プルリクエスト（2分）
/create-pr 1

# 合計: 約20分で完全な機能が完成
```

### **🔄 パターンB: 段階的開発**
```bash
# フェーズ1: 設計のみ
/create-use-case 1 payment-system
/domain-modeling 1

# フェーズ2: テスト作成
/create-tests 1

# フェーズ3: 実装
/implement-domain 1    # テストを通す実装
/run-all-tests 1       # 品質確認

# フェーズ4: 完成
/create-pr 1
```

---

## 💡 **よくある質問 & 解決策**

### **Q: エラーが出た時はどうする？**
```bash
# 現在の状況を確認
/use-case-status 1

# エラーの具体的な解決方法が表示されます
# 例: "先に /domain-modeling 1 を実行してください"
```

### **Q: 複数のイシューをまとめて処理したい**
```bash
# 複数イシューをカンマ区切りで指定
/create-use-case 1,2,3 multi-feature
/create-pr 1,2,3
```

### **Q: 途中で中断した場合は？**
```bash
# いつでも状況確認可能
/use-case-status 1

# 次のアクションが自動で提案されます
```

---

## 🎓 **レベル別学習パス**

### **🌱 初心者（まず試してみる）**
1. `/create-use-case 1 hello-world`
2. `/use-case-status 1` で状況確認
3. 提案されたコマンドを順番に実行

### **⚡ 中級者（効率的な開発）**
1. 基本ワークフローのパターンAを習得
2. 複数イシューでの開発に挑戦
3. `/evolve-scenarios` でフィードバック対応

### **🚀 上級者（カスタマイズ）**
1. 全16コマンドを理解
2. チーム向けのワークフロー最適化
3. CI/CD連携の設定

---

## 📊 **成功の指標**

### **✅ 1週間で達成できること**
- [ ] 最初の機能をプルリクエストまで完成
- [ ] TDD RED→GREEN→REFACTORサイクルを体験
- [ ] ドメイン駆動設計の実践

### **✅ 1ヶ月で達成できること**
- [ ] 3つ以上の機能を完全実装
- [ ] コード品質80%以上を維持
- [ ] チームでの協調開発を実現

---

## 🆘 **トラブルシューティング**

### **よくある問題と即座の解決**

| 問題 | 解決方法 | 実行時間 |
|------|----------|----------|
| GitHub認証エラー | `gh auth login` | 1分 |
| メタデータファイル不明 | `/use-case-status 1` で確認 | 10秒 |
| テストが失敗 | `/run-all-tests 1` で詳細確認 | 30秒 |
| ブランチ競合 | `/create-pr 1` で自動マージ確認 | 1分 |

### **緊急時の復旧方法**
```bash
# 最後の安全な状態に戻る
git checkout main
git pull origin main

# 新しい機能ブランチで再開
/create-use-case 1 recovered-feature
```

---

## 🔗 **次のステップ**

### **さらに学習したい場合**
- **詳細ガイド**: [INTEGRATION_GUIDE.md](INTEGRATION_GUIDE.md)
- **全コマンドリスト**: [README.md](README.md)
- **アーキテクチャ理解**: プロジェクトの `docs/` フォルダを参照

### **チーム導入したい場合**
1. このクイックスタートをチーム内で共有
2. 最初の機能を全員で同時実装してみる
3. 定期的に `/use-case-status` で進捗共有

---

## 🎉 **まとめ**

**このクイックスタートで習得できること:**
- ✅ TDD（テスト駆動開発）の実践
- ✅ DDD（ドメイン駆動設計）の体験  
- ✅ レイヤードアーキテクチャの理解
- ✅ 自動化された高品質開発フロー

**最初の一歩:**
```bash
/create-use-case 1 my-first-feature
```

**結果:** 15-20分後にはプルリクエストが完成し、エンタープライズグレードのコード品質を体験できます。

---

> 💡 **コツ:** 完璧を求めずに、まず動かしてみることから始めましょう。エラーが出ても `/use-case-status` が次にやるべきことを教えてくれます。

**Happy Coding! 🚀**