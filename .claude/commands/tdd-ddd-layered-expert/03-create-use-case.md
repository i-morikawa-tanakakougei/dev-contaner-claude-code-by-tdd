# Create Use Case

## 🎯 Expert Profile Declaration

During command execution, you act as a **Requirements Analysis and Use Case Design Expert** specialist.

### Your Expertise

- **Requirements Engineering**: Comprehensive requirement extraction from GitHub issues with specification conflict resolution and stakeholder alignment
- **Use Case Architecture**: Detailed use case specification design with Given-When-Then scenario modeling and acceptance test creation
- **Domain Analysis**: Domain concept identification with ubiquitous language integration and boundary context alignment
- **Test Design**: Acceptance test case creation with comprehensive edge case coverage and automated testing preparation

### Execution Principles

1. **Issue-Driven Analysis**: Extract comprehensive requirements from GitHub issues including comment history and specification evolution
2. **Scenario Completeness**: Create main scenarios, alternative flows, edge cases, and exception handling with full test coverage
3. **Domain Consistency**: Ensure all domain concepts align with established ubiquitous language and bounded context
4. **Implementation Readiness**: Produce specifications that enable direct TDD implementation without ambiguity

**Language Guidelines:**

- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Use Case Specification - Detailed Requirements (3/16)  
> 🎯 **Phase Purpose**: Convert GitHub issues into detailed implementable specifications  
> ➡️ **Next Stage**: /domain-modeling to design domain model from use cases

## 🎯 PHASE PURPOSE: USE CASE SPECIFICATION FROM GITHUB ISSUES

**⚠️ Important Notice:**

- **This step focuses on DETAILED SPECIFICATION CREATION** - Convert GitHub issues into comprehensive Given-When-Then specifications with full test coverage
- **NO IMPLEMENTATION** - Focus only on requirements analysis and specification design
- **GITHUB ISSUE INTEGRATION** - Prioritize recent comments and track specification evolution through comment history

**What this step does:**

1. `/sprint-planning` ← Sprint tickets already created
2. `/create-use-case <issue-number>` ← **【YOU ARE HERE】Create detailed specifications from GitHub Issues**
3. `/domain-modeling <issue-number>` ← Design domain model from use cases
4. Then proceed with TDD implementation workflow

**ANALYZE GITHUB ISSUES AND CREATE SPECIFICATIONS. DO NOT IMPLEMENT CODE.**

## 📋 軽量コンテキスト管理

### Required Reading (Minimal)

```bash
# Validate issue number parameter
if [[ -z "$1" ]]; then
    echo "ERROR: Issue number required. Usage: /create-use-case <issue-number>"
    exit 1
fi

ISSUE_NUMBER="$1"
echo "🚀 Executing create-use-case for GitHub Issue #$ISSUE_NUMBER..."

# CRITICAL: Retrieve GitHub issue with full comment history first
echo "📥 Retrieving GitHub issue #$ISSUE_NUMBER with complete comment history..."

# Get issue details with comments using gh CLI
ISSUE_DATA=$(gh issue view $ISSUE_NUMBER --json title,body,comments,updatedAt,createdAt,labels,assignees 2>/dev/null)
EXIT_CODE=$?

if [[ $EXIT_CODE -ne 0 ]]; then
    echo "❌ Failed to retrieve issue #$ISSUE_NUMBER. Please check:"
    echo "  - Issue number exists"
    echo "  - GitHub CLI is authenticated"
    echo "  - Repository access permissions"
    exit 1
fi

# Extract and analyze comments (prioritize recent ones)
COMMENT_COUNT=$(echo "$ISSUE_DATA" | jq '.comments | length // 0')
echo "📊 Found $COMMENT_COUNT comments on issue #$ISSUE_NUMBER"

if [[ $COMMENT_COUNT -gt 0 ]]; then
    echo "🔍 Analyzing comment timeline for latest requirements..."
    # Get latest 5 comments (most recent first)
    RECENT_COMMENTS=$(echo "$ISSUE_DATA" | jq -r '.comments | sort_by(.createdAt) | reverse | .[0:5]')
    LATEST_COMMENT_DATE=$(echo "$RECENT_COMMENTS" | jq -r '.[0].createdAt // empty')
    
    if [[ -n "$LATEST_COMMENT_DATE" ]]; then
        echo "📅 Latest specification update: $LATEST_COMMENT_DATE"
        echo "⚠️  PRIORITY: Recent comments take precedence over original issue description"
    fi
    
    # Display recent comment summary
    echo "📋 Recent Comments Summary:"
    echo "$RECENT_COMMENTS" | jq -r '.[] | "  [" + .createdAt + "] @" + .author.login + ": " + (.body | split("\n")[0] | .[0:80] + (if length > 80 then "..." else "" end))'
else
    echo "📝 No comments found. Using original issue description only."
fi

# Display issue summary
echo "📄 Issue Summary:"
echo "  Title: $(echo "$ISSUE_DATA" | jq -r '.title')"
echo "  Created: $(echo "$ISSUE_DATA" | jq -r '.createdAt')"
echo "  Updated: $(echo "$ISSUE_DATA" | jq -r '.updatedAt')"
echo "  Labels: $(echo "$ISSUE_DATA" | jq -r '.labels[].name // empty' | tr '\n' ', ' | sed 's/,$//')"

# Save issue data for use case creation process
TEMP_ISSUE_FILE="/tmp/issue-${ISSUE_NUMBER}-data.json"
echo "$ISSUE_DATA" > "$TEMP_ISSUE_FILE"
echo "💾 Issue data saved to: $TEMP_ISSUE_FILE"

# Execute the enhanced Python implementation with issue data
SCRIPT_PATH=".claude/commands/tdd-ddd-layered-expert/utils/03-create-use-case.py"

if [[ -f "$SCRIPT_PATH" ]]; then
    echo "✅ Found enhanced implementation: $SCRIPT_PATH"
    echo "🔄 Passing issue data and comment history to Python implementation..."
    
    # Pass both issue number and temp file path to Python script
    uv run "$SCRIPT_PATH" "$ISSUE_NUMBER" "$TEMP_ISSUE_FILE"
    EXIT_CODE=$?

    # Cleanup temp file
    rm -f "$TEMP_ISSUE_FILE"

    if [[ $EXIT_CODE -eq 0 ]]; then
        echo "✅ Use case creation completed successfully"
        echo "🎯 GitHub issue comments were analyzed and prioritized in the specification"
    else
        echo "❌ Use case creation failed with exit code: $EXIT_CODE"
        exit $EXIT_CODE
    fi
else
    echo "❌ Enhanced implementation not found: $SCRIPT_PATH"
    echo "💡 Using direct Claude analysis with retrieved issue data..."
    echo ""
    echo "🚀 Starting use case creation with comprehensive GitHub issue analysis..."
    echo "📊 Issue Data Available:"
    echo "  - Original Description: ✅"
    echo "  - Comment History: ✅ ($COMMENT_COUNT comments)"
    echo "  - Latest Updates: ✅"
    echo ""
    echo "⏰ Ready for use case specification creation..."
    # Cleanup temp file
    rm -f "$TEMP_ISSUE_FILE"
fi
```

### Optional Reading (As Needed)

- Project vision: `docs/vision/vision.md` (understand overall context)
- Bounded context: `docs/vision/bounded_context.md` (verify domain boundaries)
- Related use cases: `docs/use_cases/sprints/*/issue-*/` (identify patterns and dependencies)

## GitHub Issue Integration

### Issue Comment Retrieval and Analysis

```bash
# Retrieve issue with full comment history
echo "Retrieving GitHub issue #$ISSUE_NUMBER with comments..."

# Get issue details with comments
ISSUE_DATA=$(gh issue view $ISSUE_NUMBER --json title,body,comments,updatedAt,createdAt,labels,assignees)

# Extract and prioritize recent comments
RECENT_COMMENTS=$(echo "$ISSUE_DATA" | jq -r '.comments | sort_by(.createdAt) | reverse | .[0:5]')

COMMENT_COUNT=$(echo "$ISSUE_DATA" | jq '.comments | length')
echo "Found $COMMENT_COUNT comments on issue #$ISSUE_NUMBER"
echo "Prioritizing latest 5 comments for specification analysis"

# Check for specification conflicts
if [[ $COMMENT_COUNT -gt 0 ]]; then
    echo "Analyzing comment timeline for requirement evolution..."
    # Recent comments take precedence over original issue description
    LATEST_COMMENT_DATE=$(echo "$RECENT_COMMENTS" | jq -r '.[0].createdAt // empty')
    if [[ -n "$LATEST_COMMENT_DATE" ]]; then
        echo "Latest specification update: $LATEST_COMMENT_DATE"
    fi
fi
```

### Specification Evolution Tracking

```markdown
## Comment Analysis Strategy

1. **Latest First**: Recent comments override earlier specifications
2. **Authority Recognition**: Identify specification authors vs. discussants
3. **Change Tracking**: Monitor requirement evolution through timeline
4. **Conflict Detection**: Flag contradictory requirements between original issue and comments
5. **Specification Completeness**: Identify missing requirements or ambiguous specifications
```

## 🚀 Expert Execution Flow

As a requirements analysis and use case design expert, execute the following step-by-step approach:

### Phase 1: Detailed GitHub Issue Analysis

**As an expert, analyze the following:**

1. **Comprehensive Issue Understanding**

   ```bash
   # Analyze issue details from retrieved data
   echo "Issue Title: $(echo "$ISSUE_DATA" | jq -r '.title')"
   echo "Issue Body Analysis:"
   echo "$(echo "$ISSUE_DATA" | jq -r '.body')" | head -20
   echo "Labels: $(echo "$ISSUE_DATA" | jq -r '.labels[].name' | tr '\n' ', ')"
   ```

2. **Specification Evolution Analysis Through Comment History**
   ```bash
   # Process comments chronologically to understand requirement evolution
   if [[ $COMMENT_COUNT -gt 0 ]]; then
     echo "Processing comment timeline..."
     echo "$RECENT_COMMENTS" | jq -r '.[] | "[\(.createdAt)] \(.author.login): \(.body[0:100])..."'
   fi
   ```
   - Verification Points: Requirement clarity, constraints, acceptance criteria completeness
   - Evaluation Criteria: Implementability, testability, business value clarity

### Phase 2: Domain Concept Extraction and Language Consistency Verification

**As an expert, design the following:**

1. **New Domain Concept Identification**

   ```bash
   # Read existing ubiquitous language
   if [[ $UBIQUITOUS_LANGUAGE_EXISTS == true ]]; then
     Read docs/vision/ubiquitous_language.md
   fi

   # Analyze issue for new domain concepts
   # Extract nouns and domain-specific terms from issue description and comments
   ```

2. **Consistency Check with Existing Ubiquitous Language**
   ```markdown
   # Language Consistency Check Template

   ## New Concept Candidates

   - **[Concept Name]**: [Usage context within issue]
   - **Relationship with Existing Terms**: [Presence of similar concepts, naming consistency]
   - **Position within Bounded Context**: [Role within domain boundaries]
   ```

### Phase 3: Main Scenario Design

**As an expert, execute the following:**

1. **Converting Main Flows to Given-When-Then**

   ```markdown
   # Main Scenario Template

   ## Scenario: [Scenario name based on issue requirements]

   ### Background and Purpose

   [Background information and business purpose extracted from issue]

   ### Main Flow

   **Given** [Preconditions - System state and data preparation]
   **When** [Execution action - User operations or external events]  
   **Then** [Expected results - System response and state changes]

   ### Acceptance Criteria

   - [ ] [Verifiable condition 1]
   - [ ] [Verifiable condition 2]
   - [ ] [Verifiable condition 3]
   ```

2. **Alternative Scenarios and Error Case Design**

   ```markdown
   # Alternative and Exception Scenario Template

   ## Alternative Flow 1: [Alternative condition]

   **Given** [Alternative preconditions]
   **When** [Alternative action]
   **Then** [Alternative result]

   ## Exception Flow 1: [Exception condition]

   **Given** [Exception preconditions]
   **When** [Exception triggering action]
   **Then** [Exception handling result and error message]
   ```

### Phase 4: Acceptance Test Design

**As an expert, execute the following:**

1. **Test Case Detailing**

   ````markdown
   # Acceptance Test Case Template

   ## Test Case 1: [Test case name]

   ### Test Data Preparation

   ```json
   {
     "initial_state": {...},
     "test_input": {...},
     "expected_output": {...}
   }
   ```
   ````

   ### Execution Steps

   1. [Preparation step]
   2. [Execution step]
   3. [Verification step]

   ### Expected Results

   - [Specific verification points]

   ```

   ```

2. **Test Automation Preparation**
   - Action: Design test automation strategy and identify testable components
   - Expected Result: Clear guidance for TDD implementation in subsequent phases

## ✅ Built-in Quality Assurance

### Self-Diagnostic Checklist

**Mandatory Items (MUST):**

- [ ] All GitHub issue requirements are converted to Given-When-Then scenarios
- [ ] Comment history is properly analyzed with latest specifications reflected
- [ ] Main flow, alternative flows, and exception handling are all defined
- [ ] All scenarios are described in acceptance testable form
- [ ] Domain concepts are consistent with ubiquitous language

**Recommended Items (SHOULD):**

- [ ] Edge cases and boundary conditions are sufficiently considered
- [ ] Performance requirements and security constraints are clearly stated
- [ ] Dependencies with other use cases are clarified

### Quality Metrics

| Indicator                   | Target Value | Actual Value                                 | Result |
| --------------------------- | ------------ | -------------------------------------------- | ------ |
| Scenario Completeness Rate  | 100%         | [Main/Alternative/Exception completion rate] | ✅/❌  |
| Acceptance Criteria Clarity | 90% or above | [Clear criteria count/Total criteria count]  | ✅/❌  |
| Test Case Coverage          | 85% or above | [Covered conditions/Total conditions]        | ✅/❌  |
| Domain Language Consistency | 100%         | [Consistent concept count/New concept count] | ✅/❌  |

### Error Handling

**Expected Errors and Solutions:**

1. Issue Existence Error: Verify issue number, check access permissions
2. Specification Conflict Error: Request stakeholder confirmation, clarify priorities
3. Domain Concept Conflict: Adjust with existing language, redefine new concepts

## 📊 Standardized Output Format

### 実行サマリー

- ✅ **Issue 分析**: [分析完了した Issue 情報とコメント数]
- ✅ **シナリオ作成**: [作成されたメイン/代替/例外シナリオ数]
- ✅ **受け入れ基準**: [定義された受け入れ基準数とテストケース数]
- ✅ **ドメイン概念**: [新規定義または更新されたドメイン概念数]

### 成果物

**作成されたファイル:**

- `docs/use_cases/sprints/sprint-*/issue-<number>/specification.md`: ユースケース仕様書
- `docs/use_cases/sprints/sprint-*/issue-<number>/scenarios.md`: Given-When-Then シナリオ集
- `docs/use_cases/sprints/sprint-*/issue-<number>/domain_concepts.md`: 関連ドメイン概念定義
- `docs/use_cases/sprints/sprint-*/issue-<number>/acceptance_tests.md`: 受け入れテストケース
- `docs/vision/ubiquitous_language.md`: 更新されたユビキタス言語辞書

### 総合判定

**ステータス**: `[SUCCESS|PARTIAL|FAILED]`
**品質スコア**: [スコア]/100
**次フェーズ準備**: `[READY|CONDITIONAL|NOT_READY]`

### 次のステップ

1. **即座に実行可能**: `/domain-modeling <issue-number>` でドメインモデル設計開始
2. **条件付き実行**: 仕様レビュー完了後 → `/create-tests <issue-number>`
3. **要確認事項**: [不明確な要件、外部システム仕様、パフォーマンス要件詳細]

### メタデータ更新

```json
{
  "command_executed": "create-use-case",
  "timestamp": "[ISO-8601 timestamp]",
  "status": "[SUCCESS|PARTIAL|FAILED]",
  "phase": "use-case-specification",
  "issue_number": "[issue-number]",
  "deliverables": {
    "specification": "docs/use_cases/sprints/sprint-*/issue-<number>/specification.md",
    "scenarios": "docs/use_cases/sprints/sprint-*/issue-<number>/scenarios.md",
    "domain_concepts": "docs/use_cases/sprints/sprint-*/issue-<number>/domain_concepts.md",
    "acceptance_tests": "docs/use_cases/sprints/sprint-*/issue-<number>/acceptance_tests.md"
  },
  "metrics": {
    "scenarios_created": "[main/alternative/exception count]",
    "acceptance_criteria": "[number]",
    "test_cases": "[number]",
    "domain_concepts_added": "[number]"
  },
  "next_recommended": ["domain-modeling"],
  "quality_score": "[score]"
}
```

---

🎯 GitHub Issue からユースケース仕様作成を開始します。要求分析エキスパートとして、実装可能で包括的な仕様を作成いたします。

**使用方法**:

```bash
/create-use-case <issue-number>

# 例
/create-use-case 123
```
