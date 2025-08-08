Please analyze and fix the GitHub issue with comprehensive comment analysis: $ARGUMENTS.

Follow these steps:

1.  Check if `$ARGUMENTS` is provided. If `$ARGUMENTS` is not given, terminate the process immediately. When terminating, prompt the user to pass the issue number argument.

2.  **Check the current branch**:
    - Verify that the current branch is neither `main` nor `master`, but a feature branch (e.g., `feature/*`).
    - If the current branch is `main` or `master`, terminate the process and prompt the user to create and switch to a new feature branch.
    - Suggest a branch name based on the issue number and title (e.g., `feature/issue-$ISSUE_NUMBER-$SHORT_TITLE`).
    - Provide instructions to create and switch to the branch using `git checkout -b <branch-name>`.

3.  **Comprehensive issue analysis**:
    - Use `gh issue view` to get the issue details including title, description, and labels.
    - Use `gh api repos/:owner/:repo/issues/$ISSUE_NUMBER/comments` to fetch ALL comments on the issue.
    - Analyze the entire conversation thread to understand:
      - Original problem statement
      - Any clarifications or additional requirements in comments
      - Technical discussions and proposed solutions
      - Architecture decisions or changes mentioned
      - Implementation constraints or preferences

4.  **Understanding phase**:
    - Synthesize the original issue description with all comment discussions
    - Identify the current implementation approach vs. any revised approaches discussed in comments
    - Note any specific technical requirements, constraints, or architectural decisions mentioned
    - Pay special attention to any "decision" or "conclusion" comments that change the original scope

5.  **Implementation planning**:
    - Based on the complete conversation analysis, create a comprehensive implementation plan
    - If comments suggest architectural changes, prioritize those over the original issue description
    - Consider backward compatibility requirements mentioned in discussions
    - Plan for any migration strategies discussed in comments

6.  Search the codebase for relevant files based on the complete understanding.

7.  **Implementation**:
    - Implement changes according to the final consensus from issue + comments analysis
    - Follow any specific implementation patterns or approaches discussed in comments
    - Ensure compatibility with existing APIs unless comments explicitly indicate breaking changes are acceptable

8.  **Testing and validation**:
    - Write and run tests to verify the fix matches the requirements from issue + comments
    - Test edge cases or specific scenarios mentioned in the comment discussions
    - Ensure backward compatibility unless explicitly waived in comments

9.  Ensure code passes linting and type checking according to project standards.

10. **Commit message**:
    - Create a descriptive commit message that references both the issue and key decisions from comments
    - Include any relevant context from the comment discussions

**Key differences from basic issue fixing**:
- **Complete conversation context**: Read and understand ALL comments, not just the original issue
- **Priority handling**: Comments often contain updated requirements that supersede the original issue
- **Architecture awareness**: Comments may contain important architectural decisions or changes
- **Implementation guidance**: Comments often contain specific technical guidance or constraints

**Example prompt for invalid branch**:
"You are currently on the main/master branch. Please create and switch to a feature branch before fixing the issue. Suggested branch name: `feature/issue-$ISSUE_NUMBER-$SHORT_TITLE`"

Remember to use the GitHub CLI (`gh`) for all GitHub-related tasks.