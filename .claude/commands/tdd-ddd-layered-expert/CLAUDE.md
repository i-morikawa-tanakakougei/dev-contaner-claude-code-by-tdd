# TDD/DDD/Layered Expert カスタムコマンド設計方針

## 📋 MCP統合カスタムコマンド設計ガイドライン

この文書は、TDD/DDD/Layered Expertカスタムコマンド群のMCP統合設計方針を定義します。全カスタムコマンドはこの指針に基づいて実装・改修されます。

---

## 🎯 基本設計原則

### 1. **MCP-First アーキテクチャ**

**原則**: Pythonスクリプトでの複雑性管理ではなく、MCP統合による智能化を優先

```bash
# ❌ 従来方式
.md → Python複雑処理 → Claude Code実行

# ✅ MCP統合方式  
.md → MCP分析・状態管理 → Claude Code統合実行
```

### 2. **責任分離の明確化**

| 層 | 責任 | 実装方式 |
|---|-----|---------|
| **Command Layer** | 実行フロー制御・前提条件チェック | Bash Script (.md) |
| **Intelligence Layer** | 分析・学習・パターン発見 | MCP (Serena + Context7 + Sequential) |
| **Execution Layer** | ファイル操作・Git・ツール実行 | Claude Code Tools |
| **State Management** | セッション・記憶・進捗管理 | Serena MCP Memory |

### 3. **段階的MCP統合**

#### **Phase 1.5**: 2-MCP統合（Serena + Context7）
```bash
# 実証済みパターンの安全な拡張
Serena記憶・分析 + Context7最新パターン → 統合判断
```

#### **Phase 2**: 3-MCP統合（+ Sequential）
```bash  
# 高度な論理的思考統合
Serena + Context7 + Sequential → 体系的品質向上
```

---

## 🧠 MCP統合パターン

### **Pattern A: 分析強化型（設計・計画系）**

**適用コマンド**: 00-create-vision, 02-sprint-planning, 04-domain-modeling

```bash
#!/bin/bash
# コマンド基本構造

echo "🧠 MCP-Enhanced [Command Name]..."

# Phase 1: Serena プロジェクト状態分析
echo "📚 Phase 1: Project context analysis..."
# 既存状態・パターン・履歴の分析指示

# Phase 2: Context7 最新手法統合  
echo "🌐 Phase 2: Latest methodology integration..."
# 業界最新パターン・ベストプラクティス取得指示

# Phase 3: MCP統合判断・実行
echo "🎯 Phase 3: Intelligent execution..."
# MCP分析結果に基づく統合実行指示

# Phase 4: 学習記録
echo "💾 Phase 4: Learning persistence..."
# Serena memory への結果・学習内容記録指示
```

### **Pattern B: 実装支援型（開発系）**

**適用コマンド**: 06-implement-domain, 07-implement-usecase, 08-implement-infra

```bash
#!/bin/bash
# 実装系コマンド構造

echo "🔨 MCP-Enhanced Implementation..."

# Phase 1: Serena 既存コード分析
echo "🔍 Phase 1: Existing code analysis..."
# 既存実装パターン・依存関係・品質分析指示

# Phase 2: Context7 実装パターン統合
echo "📚 Phase 2: Implementation patterns..."  
# 最新フレームワークパターン・実装手法取得指示

# Phase 3: Sequential 段階的実装計画
echo "🧩 Phase 3: Systematic implementation..."
# 論理的実装順序・検証ステップ計画指示

# Phase 4: 統合実装実行
echo "⚡ Phase 4: Coordinated execution..."
# MCP分析に基づく実装実行・品質確保
```

### **Pattern C: 最適化型（保守・改善系）**

**適用コマンド**: 11-refactor, 12-evolve-scenarios, 25-analytics-dashboard

```bash
#!/bin/bash
# 最適化系コマンド構造

echo "⚡ MCP-Enhanced Optimization..."

# Phase 1: Serena 全体品質分析
echo "📊 Phase 1: Comprehensive analysis..."
# 品質メトリクス・問題パターン・改善機会分析指示

# Phase 2: Context7 最新最適化手法
echo "🚀 Phase 2: Latest optimization patterns..."
# 最新リファクタリング・最適化パターン取得指示

# Phase 3: Sequential 段階的改善計画
echo "🎯 Phase 3: Systematic improvement..."
# 論理的改善順序・リスク最小化計画指示

# Phase 4: 安全な改善実行
echo "🛡️ Phase 4: Safe optimization execution..."
# 段階的・検証付き改善実行
```

---

## 🔧 MCP呼び出し標準パターン

### **Serena MCP 活用パターン**

#### **1. プロジェクト分析・記憶管理**
```bash
# プロジェクト構造分析
Use mcp__serena__get_symbols_overview to analyze project structure
Use mcp__serena__list_dir "." --recursive=true to understand codebase

# パターン発見・分析  
Use mcp__serena__search_for_pattern "[business_logic_pattern]" --restrict_search_to_code_files=true
Use mcp__serena__find_symbol "[entity_name]" --depth=1 --include_body=true

# 依存関係分析
Use mcp__serena__find_referencing_symbols "[symbol_name]" "[file_path]"

# セッション・学習管理
Use mcp__serena__write_memory "[memory_name]" "[analysis_results]"
Use mcp__serena__read_memory "[memory_name]" 
Use mcp__serena__list_memories to review available knowledge
```

#### **2. 状態・進捗管理**
```bash
# コマンド実行状態管理
Use mcp__serena__write_memory "command-state-[command_name]-$(date +%Y%m%d)" "{
  \"command\": \"[command_name]\", 
  \"phase\": \"[current_phase]\",
  \"processed_issues\": [issue_numbers],
  \"dependencies_resolved\": true,
  \"quality_metrics\": {...}
}"

# 依存関係状態管理  
Use mcp__serena__write_memory "project-dependencies-$(date +%Y%m%d)" "Updated dependency graph"
```

### **Context7 MCP 活用パターン**

#### **1. 最新パターン・手法取得**
```bash
# ライブラリ・フレームワーク特定
Use mcp__context7__resolve-library-id "[technology_name]" 
Use mcp__context7__resolve-library-id "[pattern_name]"

# 最新ドキュメント・パターン取得
Use mcp__context7__get-library-docs "[library_id]" --topic "[specific_topic]"
Use mcp__context7__get-library-docs "[library_id]" --tokens=5000

# 技術領域別パターン取得
Use mcp__context7__get-library-docs "/domain-driven-design" --topic "entity-patterns"
Use mcp__context7__get-library-docs "/testing-patterns" --topic "tdd-best-practices"  
Use mcp__context7__get-library-docs "/clean-architecture" --topic "layered-design"
```

### **Sequential MCP 活用パターン（Phase 2以降）**

#### **1. 体系的思考・分析**
```bash
# 複雑な問題の体系的分析
Use Sequential MCP to systematically analyze: [complex_problem_description]
Use Sequential MCP to validate approach: [proposed_solution]  
Use Sequential MCP to identify risks: [implementation_plan]

# 段階的実装計画
Use Sequential MCP to create step-by-step plan for: [complex_implementation]
Use Sequential MCP to verify logical consistency: [design_decisions]
```

---

## 📊 品質保証・検証

### **1. 実行前チェック**
```bash
# 前提条件検証
- 必要ファイルの存在確認
- MCP セッション利用可能性確認  
- 依存関係解決状況確認

# MCP状態確認
if [[ -f ".serena/sessions/current/session-metadata.json" ]]; then
    echo "✅ MCP session available - Enhanced analysis enabled"
    MCP_AVAILABLE="true"
else
    echo "ℹ️ MCP session not found - Standard mode"  
    echo "💡 Run /context-session-stageup to enable MCP enhancements"
    MCP_AVAILABLE="false"
fi
```

### **2. 実行後検証**
```bash
# 成果物検証
- 生成ファイルの整合性確認
- Git状態の確認
- MCP memory 更新確認

# 品質メトリクス記録
Use mcp__serena__write_memory "quality-metrics-[command]-$(date)" "{
  \"execution_time\": \"[duration]\",
  \"files_processed\": [count],  
  \"issues_resolved\": [count],
  \"mcp_operations\": [count],
  \"success_rate\": \"[percentage]\"
}"
```

---

## 🚀 実装ガイドライン

### **1. コマンドファイル構造**
```bash
#!/bin/bash
# [XX-command-name].md or [XX-command-name-enhanced].md

# ヘッダー: Expert Profile Declaration
# コマンドの専門性・MCP統合機能の宣言

# Phase Context: TDD/DDD/LAYERED PROCESS CONTEXT  
# ワークフロー内での位置・目的の明確化

# MCP Integration Setup
# MCP利用可能性確認・機能説明

# Expert Execution Flow
# Phase分割実行・MCP統合処理・Claude Code指示

# Quality Assurance
# 品質チェック・成果物検証

# Standardized Output  
# ユーザー向けサマリー・次ステップ案内
```

### **2. エラーハンドリング**
```bash
# MCP利用不可時のGraceful Degradation
if [[ "$MCP_AVAILABLE" == "false" ]]; then
    echo "ℹ️ Running in standard mode without MCP enhancements"
    # 基本機能での処理継続
fi

# 段階的エラー回復
if [[ $? -ne 0 ]]; then
    echo "❌ Phase failed, attempting recovery..."
    Use mcp__serena__read_memory "last-successful-state" for recovery
fi
```

### **3. パフォーマンス最適化**
```bash
# MCP呼び出し最適化
- 不要なMCP呼び出し削減
- メモリ読み書きの効率化
- Context7呼び出しのキャッシュ活用

# 並列処理考慮
- 独立したMCP操作の並列化
- セッション管理の安全性確保
```

---

## 📚 運用・保守ガイドライン

### **1. MCP セッション管理**
```bash
# セッション初期化
/context-session-stageup  # MCP統合環境準備

# セッション状態管理
/checkpoint-session milestone_name  # 重要な節目でのバックアップ
/recovery-session milestone_name    # 問題発生時の復旧
```

### **2. 学習・改善サイクル**
```bash
# 実行結果の学習記録
Use mcp__serena__write_memory "[command]-lessons-$(date)" "{
  \"successful_patterns\": [...],
  \"encountered_issues\": [...], 
  \"improvement_opportunities\": [...],
  \"user_feedback\": [...]
}"

# 改善パターンの適用
Use mcp__serena__read_memory "[command]-lessons-*" for pattern analysis
Apply learned patterns to command enhancement
```

### **3. 品質監視・メトリクス**
```bash
# パフォーマンスメトリクス
- MCP応答時間監視
- コマンド実行時間追跡  
- 成功率・エラー率測定

# 品質メトリクス
- 生成ファイル品質評価
- ユーザー満足度追跡
- MCP統合効果測定
```

---

## 🔄 継続改善・発展戦略

### **Phase 1.5 拡張計画**
- 全コマンドへの2-MCP統合（Serena + Context7）
- 実証済みパターンの安全な適用
- 基盤安定化・品質向上

### **Phase 2 Sequential統合**  
- 3-MCP統合による高度な論理的思考
- 体系的品質保証・リスク管理
- 複雑性を論理的に管理

### **Phase 3 完全統合**
- 全フェーズでの3-MCP統合完成
- AI支援による継続改善
- エンタープライズ機能統合

---

**作成日**: 2025-01-05  
**版数**: v1.0 (MCP統合設計方針初版)  
**適用範囲**: 全TDD/DDD/Layered Expertカスタムコマンド  
**次回更新**: Phase 1.5実装完了時