Create project vision and core scenarios.

## Metadata
- **Prerequisites**: None (Initial project phase)
- **Input**: None (Interactive prompts for information gathering)
- **Output**: 
  - `docs/vision/project-vision.md` - Project vision document
  - `docs/use_cases/core/index.md` - Core scenarios index
  - `docs/steering/*.md` - Steering documents (product/tech/structure)
- **Dependencies**: Foundation for all subsequent commands
- **Execution Timing**: Once at project start only

## 🎯 **TDD/DDD/LAYERED PROCESS CONTEXT**

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Initial Phase - Project Vision Definition (00/16)  
> 🎯 **Phase Purpose**: Establish project direction and create core scenarios  
> ➡️ **Next Stage**: 03-create-use-case (Use Case Specification) or sprint-planning
>
> **📋 3-Layer Architecture Operations**:  
> - 🎯 **Strategic**: `docs/use_cases/core/index.md` (Create project blueprint)  
> - 📊 **Tactical**: `docs/use_cases/index.md` (Initialize implementation map)  
> - 🔧 **Execution**: Various metadata files (Foundation setup)

## 🎯 **PHASE PURPOSE: VISION & SCENARIOS ONLY**

**⚠️ Important Notice:**
- **This step is DOCUMENTATION ONLY** - Create project vision and core scenarios
- **NO FEATURE IMPLEMENTATION** - Focus on business requirements and use cases  
- **Foundation phase** - Establish project direction and high-level scenarios
- **Create strategic documents ONLY** - No code implementation

**What this step does:**
1. `00-create-vision` ← **【YOU ARE HERE】Vision document and core scenarios**
2. `01-init-project-structure` ← Project structure setup
3. `02-sprint-planning` ← Sprint planning from scenarios
4. Then TDD/DDD implementation cycle begins

**CREATE VISION DOCUMENTATION ONLY.**

## Common Errors and Solutions

### ❌ Error Case 1: Vision file already exists
**Cause**: Project vision has already been created  
**Solution**: 
- Choose to update existing vision (enter `y` at prompt)
- For new project, run in different directory

### ❌ Error Case 2: Git configuration incomplete
**Cause**: `git config user.name` not set  
**Solution**: 
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### ❌ Error Case 3: Directory creation permission error
**Cause**: No write permission for `docs/` directory  
**Solution**: Verify project root directory permissions

## Execution Examples

### ✅ Success Example
```bash
$ /create-vision
🎯 プロジェクトビジョン作成を開始します
以下の質問にお答えください (Enterで次の質問、空白で標準値使用):

📋 基本情報
============
プロジェクト名: MT5 Trading System
プロジェクトの主な目的: 自動売買システムの構築
主要なターゲットユーザー: トレーダー、投資家
ビジネスドメイン: 金融取引

🏗️ アーキテクチャ情報
==================
メインBounded Context名: Trading
主要エンティティ: Order, Position, Account
主要な機能・ユースケース: 注文管理, ポジション管理, リスク管理

⚙️ 技術要件
============
パフォーマンス要件: レイテンシ < 100ms
セキュリティ要件: API認証, データ暗号化
可用性要件: 99.99% アップタイム

✅ 情報収集完了。ビジョンドキュメントを作成します...
🎉 プロジェクトビジョン作成完了!
```

### ❌ Failure Example and Fix
```bash
$ /create-vision
⚠️  プロジェクトビジョンが既に存在します: docs/vision/project-vision.md
既存のビジョンを更新しますか？ (y/N): n
ビジョン作成をキャンセルしました

# Fix: Select 'y' if update needed, or run in new project directory
```

## 📋 **VISION CREATION TASK CHECKLIST**

**Use this checklist for comprehensive project vision creation:**

### 🔴 Required Tasks

#### **📝 Interactive Information Gathering**
- [ ] **Collect project basics**: Name, purpose, target users, business domain
- [ ] **Gather architecture info**: Main bounded context, core entities, key features
- [ ] **Document technical requirements**: Performance, security, availability needs

#### **📄 Vision Document Creation**
- [ ] **Write project overview**: Purpose, business value, development approach
- [ ] **Define bounded context**: Responsibilities, use cases, boundaries, dependencies
- [ ] **Document core entities**: Main business objects and domain concepts
- [ ] **Establish ubiquitous language**: Domain terminology table with definitions

#### **📋 Core Scenarios Definition**
- [ ] **Extract core scenarios**: 80% coverage scenarios from vision
- [ ] **Prioritize by business value**: High/Medium/Low priority classification
- [ ] **Write Given-When-Then format**: Structured scenario descriptions

### 🟡 Recommended Tasks

#### **📄 Vision Document Enhancement**
- [ ] **Define stakeholders**: Primary/secondary with roles and interests
- [ ] **Set non-functional requirements**: Performance, security, availability, scalability
- [ ] **Document technical stack**: Architecture patterns, development methods
- [ ] **Define success metrics**: Business, technical, and team indicators

#### **🧭 Steering Documents Creation**
- [ ] **Create product policy (product.md)**: Business value, market, success metrics
- [ ] **Create technical policy (tech.md)**: Architecture principles, tech stack, process
- [ ] **Create structural policy (structure.md)**: Layered architecture, DDD patterns, naming

### 🟢 Optional Tasks

#### **📄 Advanced Planning**
- [ ] **Assess risks and mitigation**: Technical/business risks with countermeasures
- [ ] **Create evolution roadmap**: Phase 1 (MVP) → Phase 2 → Phase 3
- [ ] **Validate information completeness**: Ensure all critical aspects are covered

#### **📊 Foundation Setup**
- [ ] **Update use cases index**: Add vision completion status and next steps
- [ ] **Commit all artifacts**: Vision, core scenarios, steering documents
- [ ] **Prepare for next phase**: Ready for project structure initialization

**💡 Pro Tip**: Copy this checklist for use in actual projects!

## Task Details

**🤖 Agent Integration**: This command uses the specialized `00-create-vision` agent for optimal TDD/DDD/Layered Architecture implementation.

Follow these steps:

1. **Pre-execution Validation**:
   ```bash
   # Validate arguments (vision creation requires no arguments)
   if [[ $# -gt 0 ]]; then
       echo "⚠️  create-vision コマンドは引数を必要としません"
       echo "指定された引数は無視されます"
   fi
   
   # Check if vision already exists
   vision_file="docs/vision/project-vision.md"
   if [[ -f "$vision_file" ]]; then
       echo "⚠️  プロジェクトビジョンが既に存在します: $vision_file"
       echo "既存のビジョンを更新しますか？ (y/N): "
       read -n 1 -r
       echo
       if [[ ! $REPLY =~ ^[Yy]$ ]]; then
           echo "ビジョン作成をキャンセルしました"
           exit 0
       fi
   fi
   ```

2. **Context Preparation and Agent Execution**:
   ```bash
   # 🔄 Prepare context for agent (Pattern B: Hybrid approach)
   echo "🎯 コンテキスト準備とエージェント起動..."
   
   # Create context file with command arguments and project information
   context_file="/workspace/.claude/context/current-command-context.json"
   current_time=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
   
   # Build context JSON for vision creation
   cat > "$context_file" <<EOF
   {
     "command": "create-vision",
     "timestamp": "$current_time",
     "project_name": "$project_name",
     "phase": "vision-creation",
     "context": {
       "git_repo": $(git rev-parse --is-inside-work-tree 2>/dev/null && echo "true" || echo "false"),
       "expected_outputs": [
         "docs/vision/project-vision.md",
         "docs/use_cases/core/index.md",
         "docs/use_cases/index.md"
       ],
       "architecture_patterns": ["TDD", "DDD", "Layered Architecture"]
     },
     "additional_instructions": "プロジェクトビジョンを作成し、TDD/DDD/レイヤードアーキテクチャに基づいた開発基盤を構築してください。コアシナリオの定義とユビキタス言語の確立を重視してください。",
     "special_considerations": [
       "対話型の情報収集によるビジョン精緻化",
       "bounded contextの明確な定義",
       "Given-When-Thenシナリオの品質確保",
       "プロジェクト全体の整合性維持"
     ],
     "custom_context": {
       "interactive_mode": true,
       "documentation_focus": "high",
       "architecture_validation": true
     }
   }
   EOF
   
   echo "✅ コンテキストファイル作成完了: $context_file"
   
   # 🤖 Call the specialized agent with hybrid context
   echo ""
   echo "🎯 ビジョン作成エージェントを起動します..."
   echo "専門エージェントがTDD/DDD/レイヤードアーキテクチャに基づいてビジョンを作成します"
   echo ""
   
   # Actual Claude Code Task tool invocation with hybrid approach
   cat <<'AGENT_CALL'
   Task tool will be called with:
   - subagent_type: "00-create-vision"
   - description: "Create project vision with TDD/DDD/Layered Architecture foundation"
   - prompt: |
     プロジェクトビジョン作成タスクを実行してください。
     
     ## コンテキスト情報の取得
     1. 一時コンテキスト（引数情報）:
        - /workspace/.claude/context/current-command-context.json を読み込み
     
     2. プロジェクト状況の確認:
        - 既存のdocs/構造があれば現在の状況を確認
        - Gitリポジトリの状態確認
     
     ## 実行タスク
     1. インタラクティブな情報収集
     2. プロジェクトビジョン文書作成
     3. コアシナリオ定義（Given-When-Then形式）
     4. ユビキタス言語の確立
     5. ステアリング文書作成
     6. 必要なディレクトリ構造の作成
     7. Gitコミットと整合性チェック
     
     ## 処理完了後
     - 作成したファイルのパスを報告
     - 次のステップ（プロジェクト構造初期化）への案内
   AGENT_CALL
   
   echo "✅ エージェント呼び出し設定完了"
   echo "エージェントが以下の処理を実行します:"
   echo "  - コンテキストファイルからのプロジェクト情報取得"
   echo "  - インタラクティブな情報収集"
   echo "  - プロジェクトビジョン文書作成"
   echo "  - コアシナリオ定義"
   echo "  - ステアリング文書作成"
   echo "  - 必要なディレクトリ構造の作成"
   echo "  - Gitコミットと整合性チェック"
   ```

3. **Agent Result Verification**:
   ```bash
   # 🔍 Verify agent execution results
   echo "🔍 エージェント実行結果を検証中..."
   
   # Check that essential files were created by the agent
   required_files=(
       "docs/vision/project-vision.md"
       "docs/use_cases/core/index.md"
       "docs/use_cases/index.md"
   )
   
   required_dirs=(
       "docs/vision"
       "docs/use_cases/core"
       "docs/steering"
   )
   
   # Validate directory structure
   missing_dirs=()
   for dir in "${required_dirs[@]}"; do
       if [[ ! -d "$dir" ]]; then
           missing_dirs+=("$dir")
       fi
   done
   
   # Validate essential files
   missing_files=()
   for file in "${required_files[@]}"; do
       if [[ ! -f "$file" ]]; then
           missing_files+=("$file")
       fi
   done
   
   # Report validation results
   if [[ ${#missing_dirs[@]} -gt 0 ]] || [[ ${#missing_files[@]} -gt 0 ]]; then
       echo "❌ エージェント実行検証失敗:"
       if [[ ${#missing_dirs[@]} -gt 0 ]]; then
           echo "  未作成ディレクトリ: ${missing_dirs[*]}"
       fi
       if [[ ${#missing_files[@]} -gt 0 ]]; then
           echo "  未作成ファイル: ${missing_files[*]}"
       fi
       exit 1
   fi
   
   echo "✅ エージェント実行結果検証完了"
   
   # Clean up context file after successful execution
   if [[ -f "$context_file" ]]; then
       # Archive context to execution history
       echo "{\"timestamp\":\"$(date -Iseconds)\",\"command\":\"create-vision\",\"project\":\"$project_name\",\"status\":\"completed\"}" >> /workspace/.claude/context/execution-history.jsonl
       rm -f "$context_file"
       echo "📝 コンテキストを実行履歴に記録し、一時ファイルをクリーンアップしました"
   fi
   ```

4. **Display Success Summary**:
   ```bash
   # 📊 Display comprehensive success summary
   echo ""
   echo "🎉 プロジェクトビジョン作成完了!"
   echo "====================================="
   
   # Show created files
   echo "📁 作成されたファイル:"
   if [[ -f "docs/vision/project-vision.md" ]]; then
       echo "   ✅ docs/vision/project-vision.md (プロジェクトビジョン)"
   fi
   if [[ -f "docs/use_cases/core/index.md" ]]; then
       echo "   ✅ docs/use_cases/core/index.md (コアシナリオ)"
   fi
   if [[ -f "docs/use_cases/index.md" ]]; then
       echo "   ✅ docs/use_cases/index.md (実装状況管理)"
   fi
   
   # Check for steering documents
   steering_count=0
   for doc in docs/steering/*.md; do
       if [[ -f "$doc" ]]; then
           ((steering_count++))
       fi
   done
   if [[ $steering_count -gt 0 ]]; then
       echo "   ✅ docs/steering/ (${steering_count}個のステアリング文書)"
   fi
   
   echo ""
   echo "📋 次のステップ:"
   echo "   1. プロジェクト構造初期化: /init-project-structure"
   echo "   2. スプリント計画: /sprint-planning 1"
   echo "   3. 開発開始: /create-use-case <issue-number>"
   echo ""
   echo "📚 重要ドキュメント:"
   echo "   - ビジョン: docs/vision/project-vision.md"
   echo "   - コアシナリオ: docs/use_cases/core/index.md"
   echo "   - 実装状況: docs/use_cases/index.md"
   echo ""
   echo "✅ TDD/DDD/レイヤードアーキテクチャ開発準備完了!"
   ```




