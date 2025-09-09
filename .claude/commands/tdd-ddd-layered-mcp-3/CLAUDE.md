# TDD/DDD/Layered Expert カスタムコマンド設計方針

## 📋 シンプル・文脈駆動MCP統合ガイドライン

この文書は、TDD/DDD/Layered Expertカスタムコマンド群の設計方針を定義します。**シンプルさ**と**文脈理解**を重視した実装を目指します。

---

## 🎯 基本設計原則

### 1. **文脈駆動アプローチ**

**原則**: Claudeが状況を理解し、最適なMCP統合を判断

```markdown
# ✅ 推奨アプローチ
1. 状況分析: タスクの複雑性を文脈で判断
2. 適応的統合: 複雑性に応じてMCP使用を決定  
3. シンプル実行: 必要最小限の統合

# ❌ 避けるべき複雑なアプローチ  
- Bashスクリプトによる機械的な複雑性評価
- 過度な数値計算・閾値判定システム
- 複雑なカテゴリ分類システム
```

### 2. **SuperClaudeフレームワーク準拠**

**Sequential MCP適用基準（SuperClaudeガイドライン）**:
- **3+ interconnected components**: 相互依存する複数コンポーネント
- **Multi-component failure investigation**: 複数レイヤーの問題調査
- **Systematic analysis needed**: 体系的分析が必要な場面
- **Cross-domain issues**: 複数領域にまたがる問題

### 3. **責任分離の明確化**

| 層 | 責任 | 実装方式 |
|---|-----|---------|
| **Command Layer** | フロー制御・MCP統合判断 | コマンドファイル (.md) |
| **Intelligence Layer** | 分析・学習・体系的思考 | MCP (Serena + Context7 + Sequential) |
| **Execution Layer** | ファイル操作・Git・ツール実行 | Claude Code Tools |
| **State Management** | セッション・記憶・進捗管理 | Serena MCP Memory |

---

## 📋 GitHub Issue統合パターン

### **シンプル・コメント重視アプローチ**

**原則**: 直近のコメントほど重要な情報を含む

#### **標準GitHub Issue解析パターン**

```bash
# GitHub Issue Requirements Loading (Simple & Comment-Focused)
echo "📋 Loading GitHub issue requirements..."

# Basic issue data retrieval
if command -v gh &> /dev/null; then
    ISSUE_DATA=$(gh issue view $ISSUE_NUMBER --json title,body,comments,updatedAt 2>/dev/null)
    
    if [[ $? -eq 0 ]]; then
        echo "✅ GitHub issue #$ISSUE_NUMBER loaded"
        
        # Simple comment analysis with recency priority
        COMMENT_COUNT=$(echo "$ISSUE_DATA" | jq '.comments | length // 0')
        
        if [[ $COMMENT_COUNT -gt 0 ]]; then
            echo "📊 Found $COMMENT_COUNT comments"
            echo "⚠️ PRIORITY: Recent comments contain the most current requirements"
            echo "📅 Implementation should prioritize latest comment content over original description"
            
            # Display recent comments summary (simple)
            echo "📋 Latest Comments (most recent first):"
            echo "$ISSUE_DATA" | jq -r '.comments | sort_by(.updatedAt) | reverse | .[0:3] | .[] | "  💬 [\(.updatedAt)] @\(.author.login): \(.body | split("\n")[0] | .[0:100])..."'
        else
            echo "📝 No comments found - using original issue description"
        fi
        
        # Display issue summary
        echo "📄 Issue: $(echo "$ISSUE_DATA" | jq -r '.title')"
        echo "📅 Last Updated: $(echo "$ISSUE_DATA" | jq -r '.updatedAt')"
        
    else
        echo "⚠️ GitHub CLI failed - falling back to specification files"
    fi
else
    echo "ℹ️ GitHub CLI not available - using specification files"
fi

echo "🎯 Proceeding with implementation based on latest requirements..."
```

#### **重要な実装指針**

**✅ 必須事項**:
- **最新コメント優先**: 直近のコメントを最も重要視する
- **Graceful Degradation**: GitHub CLI失敗時は仕様書ファイルにフォールバック
- **シンプル処理**: 複雑な解析ロジックは避ける
- **明確な優先順位表示**: ユーザーに優先度を明示する

**❌ 避けるべき複雑性**:
- 複雑なJSON処理ロジック
- 統計的分析や数値計算
- 過度なコメント分析
- 一時ファイルの多用

#### **適用対象コマンド**

以下のコマンドでこのパターンを使用：
- `03-create-use-case-enhanced.md`
- `07-implement-usecase-enhanced.md` 
- `08-implement-infra-enhanced.md`
- `09-implement-presentation-enhanced.md`
- その他GitHub issue番号をパラメータとするコマンド

---

## 🧠 MCP統合パターン

### **基本統合フロー**

```bash
#!/bin/bash
# 標準MCP統合パターン

echo "🚀 [Command Name] with Intelligent MCP Integration..."

# Step 1: 状況分析・複雑性判断
echo "📊 Analyzing task complexity and requirements..."

# Step 2: MCP利用可能性確認
echo "🔧 Checking MCP availability..."

# Step 3: 適応的MCP統合実行
if [task_is_complex]; then
    echo "🧩 Complex task detected - Using Sequential MCP for systematic analysis"
    # Sequential MCP + Serena + Context7 統合実行
else
    echo "⚡ Standard task - Using Serena + Context7 integration"
    # Serena + Context7 実行
fi

# Step 4: 結果統合・学習記録
echo "💾 Recording results and learning insights..."
```

### **複雑性判断の指針**

#### **Sequential MCP使用推奨場面**:
1. **戦略・設計系**: アーキテクチャ決定、ビジョン策定、複雑な設計判断
2. **多層統合問題**: Domain↔UseCase↔Infrastructure↔Presentation間の複雑な統合
3. **デバッグ複雑性**: レイヤー間責任特定、根本原因分析、系統的デバッグ
4. **リスク分析**: 変更影響分析、複数観点からのリスク評価

#### **標準実行場面**:
1. **実装系**: 単一レイヤーでの実装作業
2. **テスト系**: 基本的なテスト作成・実行
3. **ユーティリティ系**: プロジェクト構造作成、クリーンアップ等

---

## 🔧 MCP呼び出しパターン

### **Serena MCP活用**

```bash
# プロジェクト分析・記憶管理
Use mcp__serena__get_symbols_overview to analyze project structure
Use mcp__serena__search_for_pattern "[business_logic_pattern]" to find patterns
Use mcp__serena__write_memory "[memory_name]" "[analysis_results]"
```

### **Context7 MCP活用**

```bash
# 最新パターン・手法取得
Use mcp__context7__resolve-library-id "[technology_name]"
Use mcp__context7__get-library-docs "[library_id]" --topic "[specific_topic]"
```

### **Sequential MCP活用（複雑な場合）**

```bash
# 体系的分析・段階的思考
Use mcp__sequential-thinking__sequentialthinking to systematically analyze: [complex_problem]
- Break down into logical components
- Identify interdependencies and risks  
- Create step-by-step resolution plan
```

---

## 📊 品質保証

### **実行前チェック**

```bash
# MCP利用可能性確認
if command -v mcp__serena__think_about_collected_information &> /dev/null; then
    echo "✅ Serena MCP available"
    MCP_SERENA="available"
else
    echo "ℹ️ Serena MCP not found - standard mode"
    MCP_SERENA="unavailable" 
fi

if command -v mcp__context7__resolve-library-id &> /dev/null; then
    echo "✅ Context7 MCP available"  
    MCP_CONTEXT7="available"
else
    echo "ℹ️ Context7 MCP not found - standard mode"
    MCP_CONTEXT7="unavailable"
fi

if command -v mcp__sequential-thinking__sequentialthinking &> /dev/null; then
    echo "✅ Sequential MCP available"
    MCP_SEQUENTIAL="available"
else  
    echo "ℹ️ Sequential MCP not found - standard logic mode"
    MCP_SEQUENTIAL="unavailable"
fi
```

### **Graceful Degradation**

```bash
# MCP利用不可時の適応的処理
if [[ "$MCP_SERENA" == "unavailable" ]]; then
    echo "📋 Running without code analysis - manual analysis required"
fi

if [[ "$MCP_CONTEXT7" == "unavailable" ]]; then
    echo "📚 Running without latest patterns - using standard approaches"
fi

if [[ "$MCP_SEQUENTIAL" == "unavailable" && task_is_complex ]]; then
    echo "🧩 Complex task but Sequential MCP unavailable"
    echo "📋 Using structured manual approach with step-by-step checklists"
fi
```

---

## 🚀 実装ガイドライン  

### **コマンドファイル構造**

```bash
#!/bin/bash
# [XX-command-name-enhanced].md

# Expert Profile Declaration
# コマンドの専門性・MCP統合機能の宣言

# Process Context  
# TDD/DDD/Layeredワークフロー内での位置・目的

# Complexity & MCP Integration Assessment
# 状況分析・MCP統合判断・利用可能性確認

# Intelligent Execution Flow
# MCP統合実行・適応的処理

# Quality Assurance & Learning  
# 品質確認・学習記録

# Standardized Output
# ユーザー向けサマリー・次ステップ案内
```

### **エラーハンドリング**

```bash
# 段階的エラー回復
if [[ $? -ne 0 ]]; then
    echo "❌ Phase failed, attempting recovery..."
    
    if [[ "$MCP_SERENA" == "available" ]]; then
        Use mcp__serena__read_memory "last-successful-state-[command]" for recovery
    else
        echo "📋 Manual recovery checklist activated"
    fi
fi
```

---

## 📚 運用・保守

### **学習・改善サイクル**

```bash  
# 実行結果の学習記録（Serena MCP利用可能時）
if [[ "$MCP_SERENA" == "available" ]]; then
    Use mcp__serena__write_memory "[command]-insights-$(date +%Y%m%d)" "{
      \"approach_effectiveness\": \"[評価]\",
      \"mcp_integration_results\": \"[結果]\", 
      \"improvement_opportunities\": [\"改善点1\", \"改善点2\"],
      \"user_feedback\": \"[フィードバック]\"
    }"
fi
```

### **継続改善指針**

1. **シンプルさの維持**: 複雑化を避け、理解しやすい実装を保持
2. **文脈適応**: 状況に応じた最適なMCP統合パターン適用
3. **SuperClaudeガイドライン準拠**: 一貫した設計哲学の維持
4. **実証的改善**: 実際の使用結果に基づく継続的改善

---

## 🛠️ **カスタムコマンド改修マニュアル**

### **改修対象と手順**

#### **1. 改修対象ファイル**
```bash
# 戦略・設計系（Sequential推奨）
00-create-vision-enhanced.md
02-sprint-planning-enhanced.md  
04-domain-modeling-enhanced.md
04.5-design-review-enhanced.md
17-project-status-enhanced.md
25-analytics-dashboard.md

# 実装系（標準実行）
03-create-use-case-enhanced.md
05-create-tests-enhanced.md
06-implement-domain-enhanced.md
07-implement-usecase-enhanced.md
08-implement-infra-enhanced.md
09-implement-presentation-enhanced.md

# 品質保証系（動的判断）
05.5-test-review-enhanced.md
10-run-all-tests-enhanced.md
10.5-review-test-results-enhanced.md
11-refactor-enhanced.md
13-review-issue-enhanced.md
14-apply-feedback-enhanced.md

# デバッグ・統合系（Sequential推奨）
09.5-debug-integration-enhanced.md

# ユーティリティ系（標準実行）
01-init-project-structure-enhanced.md
15-create-pr-enhanced.md
16-status-report-enhanced.md
99-*-enhanced.md（緊急対応系）
```

#### **2. 改修手順**

**Step 1: 既存コマンドファイルの構造確認**
```bash
# 現在の構造を理解
- Expert Profile Declaration
- Process Context
- MCP Integration Setup  
- Expert Execution Flow
- Quality Assurance
- Standardized Output
```

**Step 2: GitHub Issue解析ロジックの標準化**
```bash
# ✅ 統一GitHub Issue解析パターン適用
- シンプル・コメント重視アプローチの採用
- 直近コメント最優先の明確な指針
- Graceful Degradation（GitHub CLI失敗時対応）

# ❌ 削除対象（複雑な解析ロジック）
- 過度な統計処理やコメント分析
- 複雑なJSON処理ロジック
- 一時ファイル作成・管理システム

# ✅ 標準パターンの統一適用
- 最新3コメントの簡潔表示
- 優先順位の明確な表示
- エラー処理の標準化
```

**Step 3: 複雑性判断ロジックの置き換え**
```bash
# ❌ 削除対象（複雑なBashロジック）
- 数値計算による複雑性評価
- 機械的な閾値判定システム
- Category A-E等の複雑な分類

# ✅ 置き換え内容（文脈判断）
- SuperClaudeガイドライン準拠の判断基準
- 「3+ interconnected components」等の明確な基準
- Claudeの文脈理解による適応的判断
```

**Step 4: MCP統合部分の標準化**
```bash
# 統一パターンの適用
echo "🚀 [Command Name] with Intelligent MCP Integration..."
echo "📊 Analyzing task complexity and requirements..."
echo "🔧 Checking MCP availability..."

# 複雑性に応じた分岐
if [複雑な戦略・設計・デバッグタスク]; then
    echo "🧩 Complex task detected - Using Sequential MCP for systematic analysis"
    # Sequential + Serena + Context7
else
    echo "⚡ Standard task - Using Serena + Context7 integration"  
    # Serena + Context7
fi
```

**Step 5: 品質保証・エラーハンドリング統一**
```bash
# MCP利用可能性チェック（全コマンド共通）
- Serena MCP availability check
- Context7 MCP availability check  
- Sequential MCP availability check

# Graceful Degradation（全コマンド共通）
- MCP利用不可時の代替処理
- 段階的エラー回復
```

#### **3. 改修時の注意点**

**❌ やってはいけないこと**
- 複雑な数値計算システムの導入
- 機械的な判断ロジックの実装
- 過度な分岐条件の追加
- libディレクトリへの依存

**✅ 必ず行うべきこと**
- SuperClaudeガイドライン準拠の確認
- 文脈判断中心の設計
- シンプルで理解しやすい実装
- 既存のコマンド構造の維持

#### **4. 改修完了チェックリスト**

**各コマンドで確認すべき項目**:
- [ ] **GitHub Issue解析が標準化されている**
  - [ ] シンプル・コメント重視パターンが適用されている
  - [ ] 直近コメント最優先の指針が明確に表示されている
  - [ ] Graceful Degradation（GitHub CLI失敗時対応）が実装されている
- [ ] **複雑性判断ロジックが適切化されている**
  - [ ] 複雑なBashロジックが削除されている  
  - [ ] SuperClaudeガイドラインに準拠した判断基準が適用されている
- [ ] **MCP統合が標準化されている**
  - [ ] MCP利用可能性チェックが標準化されている
  - [ ] エラーハンドリングが統一されている
- [ ] **品質保証が統一されている**
  - [ ] 学習・改善サイクルが組み込まれている

#### **5. サンプル改修例**

**A. GitHub Issue解析の改修**

**改修前（複雑）**:
```bash
# 複雑なコメント分析システム
ISSUE_DATA=$(gh issue view $ISSUE_NUMBER --json title,body,comments,updatedAt,createdAt,labels,assignees 2>/dev/null)
COMMENT_COUNT=$(echo "$ISSUE_DATA" | jq '.comments | length // 0')
RECENT_COMMENTS=$(echo "$ISSUE_DATA" | jq -r '.comments | sort_by(.createdAt) | reverse | .[0:5]')
LATEST_COMMENT_DATE=$(echo "$RECENT_COMMENTS" | jq -r '.[0].createdAt // empty')
# [さらに複雑な処理が続く...]
```

**改修後（シンプル）**:
```bash
# シンプル・コメント重視GitHub Issue解析
echo "📋 Loading GitHub issue requirements..."
if command -v gh &> /dev/null; then
    ISSUE_DATA=$(gh issue view $ISSUE_NUMBER --json title,body,comments,updatedAt 2>/dev/null)
    if [[ $? -eq 0 ]]; then
        echo "✅ GitHub issue #$ISSUE_NUMBER loaded"
        COMMENT_COUNT=$(echo "$ISSUE_DATA" | jq '.comments | length // 0')
        if [[ $COMMENT_COUNT -gt 0 ]]; then
            echo "⚠️ PRIORITY: Recent comments contain the most current requirements"
            echo "$ISSUE_DATA" | jq -r '.comments | sort_by(.updatedAt) | reverse | .[0:3] | .[] | "  💬 [\(.updatedAt)] @\(.author.login): \(.body | split("\n")[0] | .[0:100])..."'
        fi
    fi
fi
```

**B. 複雑性判断の改修**

**改修前（複雑）**:
```bash
# 複雑な数値計算システム
COMPLEXITY_SCORE=$(calculate_5d_complexity "$context")
if [[ $COMPLEXITY_SCORE -ge 12 ]]; then
    USE_SEQUENTIAL="true"
fi
```

**改修後（シンプル）**:
```bash
# 文脈判断による適応的統合
echo "📊 Analyzing task complexity and requirements..."
if [[ "$COMMAND_TYPE" == "strategic-design" ]]; then
    echo "🧩 Strategic complexity detected - Using Sequential MCP"
    USE_SEQUENTIAL="true"
else
    echo "⚡ Standard execution with Serena + Context7"
    USE_SEQUENTIAL="false" 
fi
```

---

## 🔄 発展戦略

### **Phase 2.1: シンプル統合完成**（現在）
- 複雑なBashロジック撤廃完了
- 文脈駆動アプローチ確立
- SuperClaudeガイドライン準拠

### **Phase 2.2: 効果検証・最適化**  
- シンプル統合の効果測定
- ユーザビリティ向上
- パフォーマンス最適化

### **Phase 3: 次世代統合**
- AI支援による自動改善
- より高度な文脈理解
- エンタープライズ機能統合

---

**作成日**: 2025-09-06  
**版数**: v3.0 (シンプル・文脈駆動版)  
**設計哲学**: SuperClaudeフレームワーク準拠・シンプルさ重視  
**適用範囲**: 全TDD/DDD/Layered Expertカスタムコマンド  
**次回更新**: Phase 2.2効果検証完了時