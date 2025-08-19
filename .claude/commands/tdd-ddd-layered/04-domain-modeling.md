Design domain models based on the Given-When-Then specification.

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

**🤖 Agent Integration**: This command uses the specialized `04-domain-modeling` agent for optimal domain model design.

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

2. **Execute Domain Modeling Agent**:
   ```bash
   # 🤖 Delegate to specialized domain modeling agent
   echo "🏗️ ドメインモデリングエージェントを起動します..."
   echo "専門エージェントがDDD原則に基づいてドメインモデルを設計します"
   echo ""
   
   # Call the specialized agent using Claude Code's Task tool
   # The agent will handle:
   # - Use case specification analysis for domain concepts
   # - Entity and value object identification and design
   # - Aggregate boundary definition and consistency rules
   # - Domain service design for complex business logic
   # - Repository interface definition
   # - Domain event identification
   # - Ubiquitous language establishment
   # - Domain model documentation creation
   
   # Note: In actual implementation, this would be handled by the Claude Code system
   # when the /domain-modeling command is executed. The agent integration happens
   # automatically through the Task tool with subagent_type="04-domain-modeling"
   
   echo "✅ ドメインモデリングエージェント呼び出し完了"
   echo "エージェントが以下の処理を実行しました:"
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