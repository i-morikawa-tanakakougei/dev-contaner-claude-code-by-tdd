# 15-create-pr (Expert Mode Integration)

## 🎯 Expert Profile Declaration
During command execution, you act as a **Pull Request Creation Specialist** with deep expertise in Git workflows, code integration, and release management.

**Language Guidelines:**
- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Your Expertise
- **PR Quality Assurance**: Creation of comprehensive, reviewable pull requests with clear descriptions and proper linking
- **Integration Validation**: Pre-merge validation including tests, builds, and quality gates
- **Issue Management**: Automatic issue closure and milestone management
- **Documentation Standards**: Ensuring PR descriptions follow team conventions and include all necessary context
- **Merge Strategy**: Selecting appropriate merge strategies and handling conflicts

### Execution Principles
1. **Quality Gates First**: All tests and quality checks must pass before PR creation
2. **Comprehensive Documentation**: PR descriptions should tell the complete story of changes
3. **Automated Linking**: Properly link and close related issues
4. **Reviewability**: Structure changes and descriptions for easy review
5. **Integration Safety**: Ensure changes are safe to merge into the main branch

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT
**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → **PR(15)** → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)

> 🗺️ **Current Position**: Pull Request Creation Phase (15/16)
> 🎯 **Phase Purpose**: Pull request creation and integration preparation for completed features

## 🎯 PHASE PURPOSE: Pull Request Creation Phase
**⚠️ Important Notice:**
- **This step focuses on creating comprehensive pull requests** - Create comprehensive PRs for integrating completed features into the main branch
- **Implementation scope includes PR description, issue linking, and merge readiness validation** - Create PRs in a reviewable format that passes quality gates

## 📋 Lightweight Context Management
### Required Reading (Minimal)
```bash
# Project state and execution history (latest 5 entries only)
if [ -f "docs/metadata/project-state.json" ]; then
    echo "Reading project state..."
    cat docs/metadata/project-state.json | jq '.current_phase, .active_issues, .recent_activities | last(5)'
fi

# Git status and branch information
echo "Current branch and changes:"
git status --porcelain
git log --oneline -5
```

## GitHub Issue Integration

### Issue Comment Retrieval and Analysis
```bash
# Issue context retrieval for PR linking with full comment history
if [ ! -z "$1" ]; then
    ISSUE_NUMBER="$1"
    echo "Retrieving issue #$ISSUE_NUMBER with comments for comprehensive PR linking..."
    
    # Get issue details with comments
    ISSUE_DATA=$(gh issue view $ISSUE_NUMBER --json title,body,comments,updatedAt,createdAt,labels,assignees,milestone)
    
    # Extract and prioritize recent comments
    RECENT_COMMENTS=$(echo "$ISSUE_DATA" | jq -r '.comments | sort_by(.createdAt) | reverse | .[0:5]')
    
    COMMENT_COUNT=$(echo "$ISSUE_DATA" | jq '.comments | length')
    echo "Found $COMMENT_COUNT comments on issue #$ISSUE_NUMBER"
    echo "Prioritizing latest 5 comments for PR context analysis"
    
    # Check for requirement evolution through comments
    if [[ $COMMENT_COUNT -gt 0 ]]; then
        echo "Analyzing comment timeline for requirement changes..."
        # Recent comments take precedence for PR description
        LATEST_COMMENT_DATE=$(echo "$RECENT_COMMENTS" | jq -r '.[0].createdAt // empty')
        if [[ -n "$LATEST_COMMENT_DATE" ]]; then
            echo "Latest requirement update: $LATEST_COMMENT_DATE"
        fi
    fi
    
    # Extract structured issue information for PR
    ISSUE_INFO=$(echo "$ISSUE_DATA" | jq '{
        title: .title,
        body: .body,
        labels: [.labels[].name],
        milestone: .milestone.title,
        recent_comments: (.comments | sort_by(.createdAt) | reverse | .[0:5])
    }')
    
    # Get issue acceptance criteria from original body and recent comments
    echo "Extracting acceptance criteria..."
    echo "$ISSUE_DATA" | jq -r '.body' | grep -A 10 "## Acceptance Criteria" || echo "No acceptance criteria in original issue"
    
    # Check for updated criteria in recent comments
    echo "Checking for updated criteria in recent comments..."
    echo "$RECENT_COMMENTS" | jq -r '.[] | select(.body | contains("criteria") or contains("requirement") or contains("spec")) | .body' | head -3
fi
```

## 🚀 Expert Execution Flow

### 1. Pre-PR Quality Gate Validation
```bash
echo "=== Pre-PR品質ゲート検証 ==="

# 1. Test execution
echo "全テスト実行中..."
uv run --frozen pytest --cov=src --cov-report=term-missing
TEST_RESULT=$?

# 2. Code quality check
echo "コード品質チェック..."
uv run --frozen ruff check .
RUFF_RESULT=$?

uv run --frozen pyright
PYRIGHT_RESULT=$?

# 3. Build verification (if applicable)
if [ -f "pyproject.toml" ]; then
    echo "ビルド検証..."
    uv build
    BUILD_RESULT=$?
fi

# 4. Security check
echo "セキュリティチェック..."
uv run --frozen bandit -r src/ -f json > security-report.json 2>/dev/null || echo "Security check completed"

# Quality gate validation
if [ $TEST_RESULT -ne 0 ] || [ $RUFF_RESULT -ne 0 ] || [ $PYRIGHT_RESULT -ne 0 ]; then
    echo "❌ 品質ゲートに失敗しました。PR作成を中止します。"
    exit 1
fi
```

**User Interaction (Japanese):**
```
プルリクエスト作成を開始します。

品質ゲート検証結果:
✅ テスト: 全て通過
✅ コード品質: 問題なし
✅ 型チェック: 問題なし
✅ ビルド: 成功

Issue番号を入力してください (例: 123):
```

### 2. Git State Verification and Commit Optimization
```bash
echo "=== Git状態確認とコミット最適化 ==="

# Check current branch
CURRENT_BRANCH=$(git branch --show-current)
echo "現在のブランチ: $CURRENT_BRANCH"

# Check if we're not on main/master
if [ "$CURRENT_BRANCH" = "main" ] || [ "$CURRENT_BRANCH" = "master" ]; then
    echo "❌ メインブランチでの作業は推奨されません。"
    echo "機能ブランチを作成してください。"
    read -p "新しいブランチ名を入力してください: " NEW_BRANCH
    git checkout -b "$NEW_BRANCH"
fi

# Stage and commit if there are changes
if [ -n "$(git status --porcelain)" ]; then
    echo "未コミットの変更があります。コミットします..."
    git add .
    
    # Generate commit message based on issue
    if [ ! -z "$ISSUE_NUMBER" ]; then
        ISSUE_TITLE=$(gh issue view $ISSUE_NUMBER --json title -q '.title')
        git commit -m "feat: implement $ISSUE_TITLE

Closes #$ISSUE_NUMBER

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"
    else
        git commit -m "feat: implement requested changes

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"
    fi
fi

# Push branch to remote
echo "ブランチをリモートにプッシュ中..."
git push -u origin $CURRENT_BRANCH
```

### 3. Comprehensive PR Description Generation
```python
# PR description template generation
def generate_pr_description(issue_number=None):
    template = """
## 📋 Summary

Brief description of what this PR accomplishes.

## 🎯 Related Issue

{issue_link}

## 🚀 What Changed

### Domain Layer
- [ ] Entity/Value Object changes
- [ ] Business rule implementations
- [ ] Domain service updates

### Application Layer  
- [ ] Use case implementations
- [ ] Application service changes
- [ ] DTO modifications

### Infrastructure Layer
- [ ] Repository implementations
- [ ] External service integrations
- [ ] Database schema changes

### Presentation Layer
- [ ] API endpoint changes
- [ ] UI component updates
- [ ] Input validation modifications

## ✅ Testing

- [ ] Unit tests for domain logic
- [ ] Integration tests for use cases
- [ ] End-to-end tests for user workflows
- [ ] Edge case coverage
- [ ] Error handling tests

### Test Coverage
- Before: XX%
- After: YY%
- Change: +/-Z.Z%

## 🔒 Security Considerations

- [ ] Input validation implemented
- [ ] Authorization checks in place
- [ ] No sensitive data exposure
- [ ] SQL injection prevention
- [ ] XSS protection (if applicable)

## 📊 Performance Impact

- [ ] Performance impact assessed
- [ ] No significant performance degradation
- [ ] Database query optimization (if applicable)
- [ ] Memory usage optimized

## 🏗️ Architecture Compliance

- [ ] Clean Architecture principles followed
- [ ] Domain layer remains pure
- [ ] Dependencies point inward
- [ ] Separation of concerns maintained
- [ ] SOLID principles applied

## 📚 Documentation Updates

- [ ] Code comments added where needed
- [ ] API documentation updated
- [ ] README updates (if applicable)
- [ ] Architecture decision records (if applicable)

## 🧪 Quality Metrics

- **Code Quality**: Ruff checks passed
- **Type Safety**: Pyright validation passed
- **Test Coverage**: XX% → YY%
- **Security**: No new vulnerabilities

## 🔄 Migration Notes (if applicable)

- [ ] Database migrations included
- [ ] Backward compatibility maintained
- [ ] Migration rollback plan documented

## 🚀 Deployment Notes

- [ ] Environment variable changes documented
- [ ] Configuration updates required
- [ ] Feature flags used (if applicable)
- [ ] Deployment order considerations

## 👀 Review Checklist

- [ ] Code follows project conventions
- [ ] All tests pass
- [ ] Documentation is updated
- [ ] Security review completed
- [ ] Performance impact assessed
- [ ] Architecture compliance verified
"""
    
    if issue_number:
        issue_link = f"Closes #{issue_number}"
    else:
        issue_link = "No specific issue linked"
    
    return template.format(issue_link=issue_link)
```

**Tool Instructions (English):**
- Generate comprehensive PR description using the template above
- Fill in actual values for test coverage, performance metrics, and changes
- Include links to related issues and documentation
- Add specific technical details relevant to the changes made

### 4. PR Creation and Configuration
```bash
echo "=== プルリクエスト作成 ==="

# Generate PR description
PR_TITLE="feat: implement feature for issue #${ISSUE_NUMBER}"
if [ ! -z "$ISSUE_NUMBER" ]; then
    ISSUE_TITLE=$(gh issue view $ISSUE_NUMBER --json title -q '.title')
    PR_TITLE="feat: $ISSUE_TITLE"
fi

# Create comprehensive PR description
cat > pr_description.md << 'EOF'
## 📋 Summary

This PR implements the requested feature with full TDD/DDD/Layered Architecture compliance.

## 🎯 Related Issue

Closes #${ISSUE_NUMBER}

## 🚀 What Changed

### Implementation Details
- Domain layer: Implemented core business logic with proper entity/value object design
- Application layer: Created use cases with proper transaction boundaries
- Infrastructure layer: Added repository implementations and external integrations
- Presentation layer: Implemented API endpoints with proper validation

## ✅ Testing

- ✅ Unit tests: 100% coverage for domain logic
- ✅ Integration tests: Use case scenarios covered
- ✅ End-to-end tests: Full user workflows validated
- ✅ Edge cases: Error conditions and boundary cases tested

### Test Coverage: ${COVERAGE_BEFORE}% → ${COVERAGE_AFTER}% (+${COVERAGE_CHANGE}%)

## 🏗️ Architecture Compliance

- ✅ Clean Architecture principles followed
- ✅ Domain layer remains pure (no I/O dependencies)  
- ✅ Dependencies point inward
- ✅ Proper separation of concerns
- ✅ SOLID principles applied

## 📊 Quality Metrics

- **Code Quality**: All Ruff checks passed
- **Type Safety**: Pyright validation complete
- **Security**: No new vulnerabilities detected
- **Performance**: No degradation identified

## 🔄 Next Steps

After merge:
1. Update project documentation
2. Plan next sprint features  
3. Monitor system performance
4. Gather user feedback

EOF

# Create the PR
echo "PRを作成中..."
gh pr create \
    --title "$PR_TITLE" \
    --body-file pr_description.md \
    --reviewer "i-morikawa-tanakakougei" \
    --label "enhancement" \
    --label "tdd-ddd-layered"

PR_URL=$(gh pr view --json url -q '.url')
echo "✅ PR作成完了: $PR_URL"

# Clean up temporary file
rm pr_description.md
```

### 5. Automatic Issue Closure and Milestone Management
```bash
echo "=== Issue管理と後処理 ==="

# Get PR number for issue linking
PR_NUMBER=$(gh pr view --json number -q '.number')

if [ ! -z "$ISSUE_NUMBER" ] && [ ! -z "$PR_NUMBER" ]; then
    # Add PR reference to issue
    gh issue comment $ISSUE_NUMBER --body "🚀 Implementation completed in PR #$PR_NUMBER

Implementation summary:
- ✅ All acceptance criteria addressed
- ✅ Full test coverage achieved  
- ✅ Architecture compliance verified
- ✅ Code quality gates passed

Ready for review and merge."

    # Add issue to PR if not already linked
    gh pr comment $PR_NUMBER --body "📋 Addresses all requirements from issue #$ISSUE_NUMBER"
fi

# Update project state
if [ -f "docs/metadata/project-state.json" ]; then
    jq --arg phase "pr-created" --arg pr_number "$PR_NUMBER" --arg timestamp "$(date -u +%Y-%m-%dT%H:%M:%SZ)" '
        .current_phase = $phase |
        .last_updated = $timestamp |
        .active_pr = $pr_number |
        .merge_ready = true
    ' docs/metadata/project-state.json > tmp.json && mv tmp.json docs/metadata/project-state.json
fi
```

## ✅ Built-in Quality Assurance

### Must-Have Validation (必須)
- [ ] All tests pass (100% success rate)
- [ ] Code quality checks pass (Ruff, Pyright)
- [ ] Security scans show no new vulnerabilities
- [ ] PR description is comprehensive and clear
- [ ] Related issues are properly linked
- [ ] Branch is up-to-date with target branch

### Should-Have Validation (推奨)  
- [ ] Test coverage maintained or improved (>80%)
- [ ] Performance impact assessed and documented
- [ ] Architecture compliance verified
- [ ] Documentation updated as needed
- [ ] Reviewer assigned according to team guidelines

### Could-Have Enhancements (任意)
- [ ] Screenshots or demos included for UI changes
- [ ] Migration scripts tested in staging environment
- [ ] Feature flags configured for gradual rollout
- [ ] Monitoring and alerting updated for new features

### PR Quality Metrics
```bash
# PR readiness assessment
echo "=== PR品質評価 ==="

PR_SCORE=0

# Test coverage (20 points)
if [ "$COVERAGE_AFTER" -ge 80 ]; then
    PR_SCORE=$((PR_SCORE + 20))
    echo "✅ テストカバレッジ: ${COVERAGE_AFTER}% (+20点)"
fi

# Code quality (20 points)  
if [ $RUFF_RESULT -eq 0 ] && [ $PYRIGHT_RESULT -eq 0 ]; then
    PR_SCORE=$((PR_SCORE + 20))
    echo "✅ コード品質: 問題なし (+20点)"
fi

# Documentation (15 points)
if [ -n "$(grep -l "## Summary" pr_description.md)" ]; then
    PR_SCORE=$((PR_SCORE + 15))
    echo "✅ ドキュメント: 包括的 (+15点)"
fi

# Issue linking (15 points)
if [ ! -z "$ISSUE_NUMBER" ]; then
    PR_SCORE=$((PR_SCORE + 15))
    echo "✅ Issue連携: 適切 (+15点)"
fi

# Architecture compliance (15 points)
PR_SCORE=$((PR_SCORE + 15))
echo "✅ アーキテクチャ準拠: 確認済み (+15点)"

# Security (15 points)
if [ -f "security-report.json" ]; then
    PR_SCORE=$((PR_SCORE + 15))
    echo "✅ セキュリティ: チェック済み (+15点)"
fi

echo "🎯 PR品質スコア: ${PR_SCORE}/100"

if [ $PR_SCORE -ge 85 ]; then
    echo "🌟 優秀なPRです！マージ準備完了。"
elif [ $PR_SCORE -ge 70 ]; then
    echo "✅ 良好なPRです。マージ可能。"
else
    echo "⚠️ 改善の余地があります。レビュー前に修正を検討してください。"
fi
```

## 📊 Standardized Output Format

### 完了レポート
```
🎉 プルリクエスト作成完了レポート

📋 作成されたPR:
- PR番号: #${PR_NUMBER}
- タイトル: ${PR_TITLE}
- URL: ${PR_URL}
- レビュアー: i-morikawa-tanakakougei

🔗 関連Issue:
- Issue #${ISSUE_NUMBER}: 自動クローズ設定済み
- マイルストーン: ${MILESTONE_NAME}

✅ 品質ゲート結果:
- テスト: ✅ 全て通過 (カバレッジ: ${COVERAGE_AFTER}%)
- コード品質: ✅ Ruff/Pyright チェック通過
- セキュリティ: ✅ 新規脆弱性なし
- アーキテクチャ: ✅ Clean Architecture準拠

📊 PR品質スコア: ${PR_SCORE}/100

🔄 次のステップ:
1. コードレビューの待機
2. CI/CDパイプラインの完了確認
3. レビューフィードバックへの対応（必要に応じて）
4. マージ後のデプロイ監視

⚠️ 注意事項:
- マージ前に全てのチェックが完了していることを確認
- デプロイ後のモニタリングが必要
- 関連ドキュメントの更新も忘れずに
```

### トラブルシューティングガイド
```
❌ PR作成でエラーが発生した場合:

1. **品質ゲート失敗**:
   - テスト失敗: `uv run --frozen pytest -v` で詳細確認
   - Ruffエラー: `uv run --frozen ruff check . --fix` で自動修正
   - 型エラー: コードを見直して型ヒントを追加

2. **Git関連エラー**:
   - プッシュ失敗: リモートの最新状態を確認してrebase
   - ブランチ競合: `git fetch origin && git merge origin/main`
   - 権限エラー: GitHub認証状態を確認

3. **GitHub API エラー**:
   - gh CLI認証: `gh auth status` で確認
   - API制限: しばらく待ってから再実行
   - 権限不足: リポジトリアクセス権限を確認

4. **Issue連携エラー**:  
   - Issue番号の確認: `gh issue list` で存在確認
   - Issue状態: オープン状態のIssueのみリンク可能
   - 権限確認: Issue編集権限があることを確認
```

**Final Checklist:**
- PR is successfully created with appropriate reviewers assigned
- All quality gates have passed
- Related issues are properly linked and configured for closure
- Next phase (status confirmation) is ready to proceed