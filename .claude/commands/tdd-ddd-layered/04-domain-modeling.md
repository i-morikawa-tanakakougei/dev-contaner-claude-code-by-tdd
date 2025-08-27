Use the 04-domain-modeling subagent to design domain models based on the Given-When-Then specification. This command MUST USE the specialized 04-domain-modeling subagent for optimal domain modeling implementation.

## Metadata
- **Prerequisites**: Use case specifications created (03-create-use-case)
- **Input**: Issue number(s) (required), feature name (optional)
- **Output**: 
  - `docs/domain/issue-X-Y-domain-model.md` - Domain model design document
  - Updated `docs/use_cases/issue-X-Y.json` metadata file
  - Updated `docs/use_cases/index.md` with design status
- **Dependencies**: jq, Git configuration, use case specification files
- **Execution Timing**: After use case specification, before TDD test creation

## 🎯 **TDD/DDD/LAYERED PROCESS CONTEXT**

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Sprint Execution Phase - Domain Model Design (04/16)  
> 🎯 **Phase Purpose**: Design domain models and entities based on DDD principles  
> ⬅️ **Previous Stage**: 03-create-use-case (Use Case Specification)  
> ➡️ **Next Stage**: 05-create-tests (TDD Test Creation)
>
> **📋 3-Layer Architecture Operations**:  
> - 🎯 **Strategic**: `docs/use_cases/core/index.md` (Reference ubiquitous language)  
> - 📊 **Tactical**: `docs/use_cases/index.md` (Update domain design status)  
> - 🔧 **Execution**: `docs/use_cases/issue-X-Y.json` (Track domain modeling phase)

## 📋 **DOMAIN MODELING TASK CHECKLIST**

**Use this checklist for comprehensive domain model design:**

### 🔴 Required Tasks

#### **📖 Use Case Analysis**
- [ ] **Review Given-When-Then scenarios**: Extract domain concepts from specifications
- [ ] **Identify entities**: Find objects with identity and lifecycle
- [ ] **Identify value objects**: Find immutable, replaceable objects
- [ ] **Extract business rules**: Identify invariants and constraints

#### **🏗️ Domain Design**
- [ ] **Design entities**: Define entity structure and behavior
- [ ] **Design value objects**: Create immutable value representations
- [ ] **Define aggregates**: Establish consistency boundaries
- [ ] **Design domain services**: Model complex business logic

#### **📊 Documentation**
- [ ] **Create domain model document**: Comprehensive design documentation
- [ ] **Define ubiquitous language**: Domain terminology and definitions
- [ ] **Update metadata**: Mark domain modeling phase as complete
- [ ] **Update project index**: Reflect domain design status

### 🟡 Recommended Tasks

#### **🔍 Design Validation**
- [ ] **Review aggregate boundaries**: Ensure proper consistency boundaries
- [ ] **Validate business rules**: Confirm all invariants are captured
- [ ] **Check domain purity**: Ensure no infrastructure concerns
- [ ] **Review naming**: Consistent use of ubiquitous language

#### **📚 Advanced Design**
- [ ] **Define domain events**: Model significant business events
- [ ] **Design specifications**: Create reusable business rule objects
- [ ] **Plan factories**: Design complex object creation strategies
- [ ] **Consider patterns**: Apply appropriate DDD tactical patterns

## Task Details

**🤖 Agent Integration**: This command MUST USE PROACTIVELY the specialized `04-domain-modeling` subagent for optimal domain model design.
 Claude Code should automatically delegate this task to the 04-domain-modeling subagent based on the command description.

## 📖 Subagent Document Reading Instructions

This command delegates to the specialized `04-domain-modeling` subagent.

**MANDATORY: The subagent MUST read these files before execution:**

1. `docs/index.md` - Project overview and current status
2. `.claude/context/project-context.json` - Current project context
3. `/workspace/.claude/context/current-command-context.json` - Current execution context (includes issue numbers)
4. `docs/use_cases/issue-X-Y.md` - Use case specifications to analyze for domain concepts
5. `docs/vision/project-vision.md` - Project vision for ubiquitous language reference
6. `docs/use_cases/core/index.md` - Core scenarios for domain understanding
7. Any existing domain models in `docs/domain/` - For consistency and pattern reuse
8. `docs/use_cases/index.md` - Current implementation status and dependencies

**Command-Specific Reading Focus - Domain Modeling:**
- Extract entities, value objects, and aggregates from use case specifications
- Identify business rules, invariants, and domain logic from Given-When-Then scenarios
- Review project vision for ubiquitous language terms and domain concepts
- Check existing domain models to maintain consistency and avoid duplication
- Understand domain boundaries and integration points with other bounded contexts

**CRITICAL:** Use the Read tool to actually read file contents, not just reference paths.

**Additional Context for Subagent Execution:**
- `docs/index.md` - Project navigation and status overview for understanding domain modeling context
- Domain architecture patterns and conventions from existing domain models
- Business glossary and terminology documentation to ensure domain language consistency
- Technical architecture constraints that might influence domain design decisions
- IMPORTANT: Use Read tool to access actual file contents, not just references

1. **Pre-execution Validation**:
   ```bash
   # Validate issue number requirement
   if [[ $# -eq 0 ]]; then
       echo "エラー: 少なくとも1つのイシュー番号を指定してください"
       echo "使用例: /domain-modeling 1"
       echo "使用例: /domain-modeling 1,7 (複数イシュー)"
       exit 1
   fi
   
   # Extract issue numbers from arguments
   issue_numbers=()
   
   # Parse first argument for issue numbers
   IFS=',' read -ra ISSUE_ARRAY <<< "$1"
   for issue in "${ISSUE_ARRAY[@]}"; do
       if [[ "$issue" =~ ^[0-9]+$ ]]; then
           issue_numbers+=("$issue")
       fi
   done
   
   # Check for use case specifications
   missing_specs=()
   for issue_num in "${issue_numbers[@]}"; do
       # Look for use case specification files
       if ! find docs/use_cases/ -name "*issue*${issue_num}*.md" -type f 2>/dev/null | head -1 >/dev/null; then
           missing_specs+=("$issue_num")
       fi
   done
   
   if [[ ${#missing_specs[@]} -gt 0 ]]; then
       echo "❌ エラー: 以下のIssueのユースケース仕様が見つかりません:"
       printf '  - Issue #%s\n' "${missing_specs[@]}"
       echo "💡 先に /create-use-case を実行してください"
       exit 1
   fi
   
   echo "🏗️ Issues: $(printf '#%s ' "${issue_numbers[@]}")のドメインモデリングを開始します"
   ```

2. **Context Preparation and Agent Execution**:
   ```bash
   # 🔄 Prepare context for agent (Pattern B: Hybrid approach)
   echo "🏗️ コンテキスト準備とエージェント起動..."
   
   # Create context file with domain modeling information
   context_file="/workspace/.claude/context/current-command-context.json"
   current_time=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
   
   # Build context JSON for domain modeling
   cat > "$context_file" <<EOF
   {
     "command": "domain-modeling",
     "timestamp": "$current_time",
     "issue_numbers": [$(IFS=,; echo "${issue_numbers[*]}")],
     "phase": "domain-modeling",
     "context": {
       "expected_outputs": [
         "docs/domain/issue-X-Y.md",
         "docs/domain/entities/",
         "docs/domain/value-objects/",
         "docs/domain/aggregates/"
       ],
       "architecture_patterns": ["DDD", "Clean Architecture"]
     },
     "additional_instructions": "DDDの原則に基づいてドメインモデルを設計してください。ユースケース仕様を分析し、エンティティ、値オブジェクト、アグリゲート境界を適切に定義してください。ユビキタス言語の一貫性を保ち、ビジネスルールをドメイン層に適切に配置してください。",
     "special_considerations": [
       "既存のユースケース仕様（docs/use_cases/issue-X-Y.md）との整合性確認",
       "アグリゲート境界の適切な設計（不変条件の保護）",
       "ドメインサービスとエンティティの責務分離",
       "リポジトリインターフェースの抽象化レベル調整"
     ],
     "custom_context": {
       "ubiquitous_language_focus": true,
       "aggregate_design": true,
       "domain_purity": true,
       "business_rules_modeling": true
     }
   }
   EOF
   
   echo "✅ コンテキストファイル作成完了: $context_file"
   
   # 🤖 Call the specialized agent with hybrid context
   echo ""
   echo "🏗️ ドメインモデリングエージェントを起動します..."
   echo "専門エージェントがDDD原則に基づいてドメインモデルを設計します"
   echo ""
   
   # Actual Claude Code Task tool invocation with hybrid approach
   # Task tool execution with comprehensive prompt
   task_prompt="タスクを実行してください。

## コンテキスト情報の取得
1. 一時コンテキスト（プロジェクト情報）:
   - /workspace/.claude/context/current-command-context.json を読み込み

2. プロジェクト状況の確認:
   - 必要な文書やファイルを確認
   - 既存の実装や設計を参照

## 実行タスク
[04-domain-modeling固有のタスクを実行]

## 重要: 標準化出力形式の遵守
レポートは必ず以下の構造化セクションで終了してください：

### 📊 実行サマリー
各Critical Taskの完了状態を✅/❌で明記

### 📋 総合判定
APPROVED/CONDITIONAL_APPROVAL/REJECTED/COMPLETED のいずれかを明記

### 💡 次のステップ
判定に基づく具体的なアクションアイテムを列挙

## 処理完了後
- 実行結果の報告
- 次のステップへの案内"

   # Execute with specialized 04-domain-modeling subagent
   # The 04-domain-modeling subagent will be automatically invoked based on the task description
   
   agent_exit_code=$?
   echo "✅ 専用エージェント実行完了 (終了コード: $agent_exit_code)"
   
   echo "✅ エージェント呼び出し設定完了"
   echo "エージェントが以下の処理を実行します:"
   echo "  - コンテキストファイルからのイシュー情報取得"
   echo "  - ユースケース仕様の分析とドメイン概念の抽出"
   echo "  - エンティティと値オブジェクトの設計"
   echo "  - アグリゲート境界の定義と整合性ルールの確立"
   echo "  - ドメインサービスと複雑なビジネスロジックの設計"
   echo "  - リポジトリインターフェースとドメインイベントの定義"
   echo "  - ユビキタス言語の確立とドメインモデル文書の作成"
   ```

3. **Agent Result Verification**:
   ```bash
   # 🔍 Verify agent execution results
   echo "🔍 エージェント実行結果を検証中..."
   
   # Check that domain model documents were created
   echo "  🔍 ドメインモデル文書の作成確認中..."
   
   created_files=()
   for issue_num in "${issue_numbers[@]}"; do
       # Look for domain model files
       domain_pattern="docs/domain/*issue*${issue_num}*.md"
       if ls $domain_pattern 2>/dev/null | head -1 >/dev/null; then
           domain_file=$(ls $domain_pattern 2>/dev/null | head -1)
           created_files+=("$domain_file")
           echo "    ✅ Issue #$issue_num のドメインモデルを確認: $(basename "$domain_file")"
       else
           echo "    ❌ Issue #$issue_num のドメインモデルが見つかりません"
       fi
       
       # Check metadata update
       metadata_pattern="docs/use_cases/*issue*${issue_num}*.json"
       if ls $metadata_pattern 2>/dev/null | head -1 >/dev/null; then
           metadata_file=$(ls $metadata_pattern 2>/dev/null | head -1)
           if command -v jq >/dev/null 2>&1; then
               domain_status=$(jq -r '.phases.domain_model.created // false' "$metadata_file" 2>/dev/null)
               if [[ "$domain_status" == "true" ]]; then
                   echo "    ✅ Issue #$issue_num のメタデータが更新されました"
               else
                   echo "    ⚠️ Issue #$issue_num のメタデータ更新が未確認"
               fi
           fi
       fi
   done
   
   # Check if docs/domain directory exists
   if [[ ! -d "docs/domain" ]]; then
       echo "❌ エラー: docs/domain ディレクトリが作成されていません"
       exit 1
   fi
   
   # Report validation results
   if [[ ${#created_files[@]} -eq 0 ]]; then
       echo "❌ エージェント実行検証失敗: ドメインモデル文書が作成されていません"
       exit 1
   fi
   
   echo "✅ エージェント実行結果検証完了"
   
   # 🔧 Load advanced task verification library
   source "$(dirname "${BASH_SOURCE[0]}")/_task_verification.sh"
   
   # ✨ New: Advanced task verification with retry capability
   echo "🔍 Critical tasks確認中..."
   if ! verify_critical_tasks "04-domain-modeling" "$latest_report"; then
       echo "⚠️ Critical tasks確認で問題が検出されました - 再実行を試行します"
       prepare_retry_context "04-domain-modeling" "1" "${verification_issues[@]}"
       
       # Enhanced context for retry
       echo "🔄 再実行用の強化コンテキスト準備中..."
       prepare_enhanced_context "04-domain-modeling" "$context_file" "${verification_issues[@]}"
       
       echo "💡 推奨アクション: エージェントを再実行してください"
       echo "   重点項目: $(IFS='|'; echo "${verification_issues[*]}")"
       exit 1
   fi
   
   echo "✅ Critical tasks確認完了 - 全項目クリア"
   ```

4. **Display Domain Modeling Success Summary**:
   ```bash
   # 📊 Display comprehensive domain modeling summary
   echo ""
   echo "🎉 ドメインモデリング完了!"
   echo "============================================="
   
   # Show created domain files
   echo "📁 作成されたドメインモデル:"
   for file in "${created_files[@]}"; do
       if [[ -f "$file" ]]; then
           echo "   ✅ $file"
       fi
   done
   
   # Show domain concepts summary
   echo ""
   echo "🏗️ ドメイン設計要素:"
   if [[ ${#created_files[@]} -gt 0 ]]; then
       first_file="${created_files[0]}"
       if [[ -f "$first_file" ]]; then
           # Extract entities from domain model (basic grep)
           entity_count=$(grep -c "^### .*Entity" "$first_file" 2>/dev/null || echo "0")
           vo_count=$(grep -c "^### .*Value Object" "$first_file" 2>/dev/null || echo "0")
           service_count=$(grep -c "^### .*Service" "$first_file" 2>/dev/null || echo "0")
           
           echo "   📊 エンティティ: $entity_count 個"
           echo "   📊 値オブジェクト: $vo_count 個"
           echo "   📊 ドメインサービス: $service_count 個"
       fi
   fi
   
   # Show next steps
   echo ""
   echo "📋 次のステップ (TDD テスト作成):"
   for issue_num in "${issue_numbers[@]}"; do
       echo "   /create-tests $issue_num"
   done
   
   echo ""
   echo "📚 重要ドキュメント:"
   echo "   - ドメインモデル: docs/domain/"
   echo "   - ユースケース仕様: docs/use_cases/"
   if [[ ${#created_files[@]} -gt 0 ]]; then
       echo "   - 作成されたモデル: ${created_files[0]}"
   fi
   
   echo ""
   echo "🔗 関連リソース:"
   for issue_num in "${issue_numbers[@]}"; do
       echo "   - Issue #$issue_num: gh issue view $issue_num"
   done
   
   echo ""
   echo "✅ ドメインモデリング完了 - TDD テスト作成準備完了!"
   ```

## Common Errors and Solutions

### ❌ Error Case 1: Use case specification not found
**Cause**: Domain modeling started before use case specification creation  
**Solution**: 
```bash
# Create use case specification first
/create-use-case <issue-number>
# Then proceed with domain modeling
/domain-modeling <issue-number>
```

### ❌ Error Case 2: Insufficient domain analysis
**Cause**: Use case specification lacks detail for domain design  
**Solution**: 
- Review and enhance Given-When-Then scenarios
- Add more specific business rules and constraints
- Clarify entity relationships and behaviors

### ❌ Error Case 3: Aggregate boundary confusion
**Cause**: Unclear consistency boundaries in domain design  
**Solution**: 
- Focus on transactional consistency requirements
- Apply single responsibility principle to aggregates
- Consider business invariants and rules

## Execution Examples

### ✅ Success Example
```bash
$ /domain-modeling 15
🏗️ Issues: #15 のドメインモデリングを開始します
🏗️ ドメインモデリングエージェントを起動します...
✅ エージェント実行結果検証完了
🎉 ドメインモデリング完了!
```

### ❌ Failure Example and Fix
```bash
$ /domain-modeling 15
❌ エラー: Issue #15 のユースケース仕様が見つかりません

# Fix: Create use case specification first
$ /create-use-case 15
$ /domain-modeling 15
```