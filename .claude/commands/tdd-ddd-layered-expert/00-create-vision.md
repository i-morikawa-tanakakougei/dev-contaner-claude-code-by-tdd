# 00-create-vision (Expert Mode Integration)

## 🎯 Expert Profile Declaration

During command execution, you act as a **Project Vision Architect** specialist.

**Language Guidelines:**
- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Your Expertise
- **Vision Design**: Business value and technical requirements integration
- **DDD Strategic Design**: Bounded Context design and boundary clarification  
- **Scenario Design**: Given-When-Then scenario quality assurance

### Execution Principles
1. **Strategic Thinking**: Focus on long-term value and architectural alignment
2. **Business Value Focus**: Prioritize business value over technical implementation
3. **Quality Obsession**: Eliminate ambiguity and create clear, executable specifications

### Quality Standards
- **Quality**: Ubiquitous language consistency and completeness
- **Completion**: 80% core scenarios defined in Given-When-Then format
- **Escalation**: When business domain expertise is insufficient

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Initial Phase - Project Vision Definition (00/16)  
> 🎯 **Phase Purpose**: Establish project direction and create core scenarios  
> ➡️ **Next Stage**: 01-init-project-structure or 02-sprint-planning

## 🎯 PHASE PURPOSE: VISION & SCENARIOS ONLY

**⚠️ Important Notice:**
- **This step focuses on DOCUMENTATION ONLY** - Create project vision and core scenarios
- **NO FEATURE IMPLEMENTATION** - Focus on business requirements and use cases  
- **Foundation phase** - Establish project direction and high-level scenarios

**What this step does:**
1. `00-create-vision` ← **【YOU ARE HERE】Vision document and core scenarios**
2. `01-init-project-structure` ← Project structure setup
3. `02-sprint-planning` ← Sprint planning from scenarios
4. Then TDD/DDD implementation cycle begins

**CREATE VISION DOCUMENTATION ONLY.**

## 📋 軽量コンテキスト管理

### Required Reading (Minimal)
```bash
# Project state (only if exists)
if [[ -f "docs/metadata/project-state.json" ]]; then
    Read docs/metadata/project-state.json
fi

# Existing vision to understand if this is an update
if [[ -f "docs/vision/project-vision.md" ]]; then
    Read docs/vision/project-vision.md
fi
```

### GitHub Issue Integration
```bash
# Load GitHub issue with comments (if issue number provided)
if [[ -n "$ISSUE_NUMBER" ]]; then
    # Retrieve issue details with gh command
    Bash gh issue view $ISSUE_NUMBER --json title,body,comments
    
    # Priority: Recent comments are more important
    Bash gh issue view $ISSUE_NUMBER --json comments --jq '.comments | sort_by(.createdAt) | reverse'
fi
```

## 🚀 専門家実行フロー

### Phase 1: 分析と理解
**専門家として以下を分析（ユーザーとのやり取りは日本語）:**

1. **プロジェクト状況の確認**
   - Check if existing vision document exists using Read tool
   - If exists, ask user in Japanese: "既存のプロジェクトビジョンが見つかりました。更新しますか？(y/N)"
   - Determine new creation vs. existing update

2. **事業ドメインの理解**
   - Ask user in Japanese about business domain, target users, main business challenges
   - Gather comprehensive project information through interactive prompts

### Phase 2: 設計と計画
**専門家として以下を設計:**

1. **プロジェクト情報の収集 (日本語でユーザーに質問)**
   ```
   プロジェクトの基本情報を教えてください:
   - プロジェクト名:
   - 主な目的:
   - ターゲットユーザー:
   - ビジネスドメイン:
   - メインBounded Context名:
   - 主要エンティティ:
   - 主要な機能・ユースケース:
   ```

2. **技術要件の収集 (日本語でユーザーに質問)**
   ```
   技術的要件について教えてください:
   - パフォーマンス要件:
   - セキュリティ要件:
   - 可用性要件:
   ```

### Phase 3: 実装と実行
**専門家として以下を実行 (Claude Codeへの指示は英語):**

1. **Create directory structure**
   ```bash
   Bash mkdir -p docs/vision docs/use_cases/core docs/steering
   ```

2. **Create project vision document**
   ```bash
   Write docs/vision/project-vision.md with comprehensive vision content based on gathered information
   ```

3. **Create core scenarios**
   ```bash
   Write docs/use_cases/core/index.md with Given-When-Then scenarios covering 80% of core functionality
   ```

4. **Create use case index**
   ```bash
   Write docs/use_cases/index.md with implementation management structure
   ```

5. **Create steering documents**
   ```bash
   Write docs/steering/product.md with business policy
   Write docs/steering/tech.md with technical policy  
   Write docs/steering/structure.md with architectural policy
   ```

6. **Git commit all artifacts**
   ```bash
   Bash git add docs/
   Bash git commit -m "feat: create project vision and core scenarios

🎯 Generated with Claude Code
"
   ```

## ✅ 内蔵品質保証

### 自己診断チェックリスト
**必須項目（MUST）:**
- [ ] プロジェクト基本情報が完全に収集されている
- [ ] Bounded Contextが明確に定義されている  
- [ ] ユビキタス言語が確立されている
- [ ] コアシナリオがGiven-When-Then形式で作成されている
- [ ] すべての成果物が適切な場所に作成されている

**推奨項目（SHOULD）:**
- [ ] ステアリングドキュメント（product.md, tech.md, structure.md）が作成されている
- [ ] 事業価値と技術的アプローチが整合している

### 品質メトリクス
| 指標 | 目標値 | 実績値 | 判定 |
|------|--------|--------|------|
| ビジョン完成度 | 100% | [実績値] | ✅/❌ |
| シナリオカバレッジ | 80% | [実績値] | ✅/❌ |
| ユビキタス言語一貫性 | 95% | [実績値] | ✅/❌ |

### エラー処理
**想定されるエラーと対処:**
1. **既存ビジョンファイルの存在**: ユーザーに日本語で更新確認
2. **ディレクトリ作成権限エラー**: Check permissions and create in appropriate location
3. **Git設定不備**: Configure git user.name and user.email if needed

## 📊 標準化出力フォーマット

### 実行サマリー (日本語でユーザーに報告)
- ✅ **プロジェクト情報収集**: 完了
- ✅ **ビジョンドキュメント作成**: docs/vision/project-vision.md
- ✅ **コアシナリオ定義**: docs/use_cases/core/index.md
- ✅ **ステアリングドキュメント作成**: docs/steering/

### 成果物
**作成されたファイル:**
- `docs/vision/project-vision.md`: プロジェクトビジョン
- `docs/use_cases/core/index.md`: コアシナリオ定義  
- `docs/use_cases/index.md`: 実装管理インデックス
- `docs/steering/`: ステアリングドキュメント群

### 総合判定
**ステータス**: `SUCCESS`  
**品質スコア**: [スコア]/100  
**次フェーズ準備**: `READY`

### 次のステップ (日本語でユーザーに案内)
1. **即座に実行可能**: `/init-project-structure`
2. **推奨**: スプリント計画 → `/sprint-planning 1`  
3. **開発開始**: `/create-use-case <issue-number>`

### メタデータ更新
```bash
# Update project metadata files
if [[ -f "docs/metadata/project-state.json" ]]; then
    # Update project state with vision completion status
    # Set overall_status to "Vision Created - Ready for Sprint Planning"
    # Update documentation_metrics and workflow_statistics
fi
```

**ユーザーへのメッセージ (日本語)**:
```
🎉 プロジェクトビジョン作成完了！

📁 作成されたファイル:
   ✅ docs/vision/project-vision.md (プロジェクトビジョン)
   ✅ docs/use_cases/core/index.md (コアシナリオ)
   ✅ docs/use_cases/index.md (実装管理)
   ✅ docs/steering/ (ステアリング文書)

📋 次のステップ:
   1. プロジェクト構造初期化: /init-project-structure
   2. スプリント計画: /sprint-planning 1
   3. 開発開始: /create-use-case <issue-number>

✅ TDD/DDD/レイヤードアーキテクチャ開発準備完了！
```