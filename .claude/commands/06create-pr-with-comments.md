Please create a pull request based on the current changes with comprehensive GitHub issue comment analysis.

The issues to close are: $ARGUMENTS (comma-separated issue numbers)

Follow these steps:

1.  **Check for existence of argument**

    - Check if `$ARGUMENTS` is provided.
    - If `$ARGUMENTS` is not given, terminate the process immediately.
    - When terminating, prompt the user to pass the issue number argument.

2.  **Comprehensive issue analysis for each issue**:
    - Parse $ARGUMENTS as comma-separated issue numbers
    - For each issue number:
      - Use `gh issue view` to get the issue details including title, description, and labels
      - Use `gh api repos/:owner/:repo/issues/$ISSUE_NUMBER/comments` to fetch ALL comments on the issue
      - Analyze the entire conversation thread to understand:
        - Original problem statement
        - Any clarifications or additional requirements in comments
        - Technical discussions and proposed solutions
        - Implementation decisions or changes mentioned
        - Final consensus on the implementation approach

3.  **Check Current Changes**

    - Use `git status` and `git diff main` to review changes
    - Ensure there are staged or unstaged changes to include in the PR
    - Verify that the changes align with the final consensus from issue discussions

4.  **Create Pull Request**

    - Push the branch to the repository
    - Create a pull request using `gh pr create` with:
      - A clear title summarizing the changes
      - Appropriate labels based on all issues (e.g., `bug`, `feature`, `enhancement`)
      - Create new labels if necessary
      - A comprehensive description that:
        - Summarizes what was changed
        - References key decisions from issue comments
        - Includes "Closes #<issue_number>" for each issue in $ARGUMENTS
        - Mentions any important implementation details discussed in comments

5.  **PR Description Format**
    - Include a summary of what was changed
    - ALWAYS write the description in Japanese
    - Reference any important architectural decisions or implementation approaches from comments
    - Include implementation notes if comments contained specific technical guidance
    - Include "Closes #<issue_number>" statements for each issue (parsed from $ARGUMENTS)
    - Example: If $ARGUMENTS is "123,456", include "Closes #123" and "Closes #456" in the description

**Key differences from basic PR creation**:
- **Complete issue context**: Analyze ALL comments on each issue, not just the original description
- **Implementation verification**: Ensure changes match the final consensus from issue discussions
- **Comprehensive PR description**: Include key decisions and context from issue comments
- **Multiple issue handling**: Analyze comments for ALL issues listed in $ARGUMENTS

Remember:
- Parse $ARGUMENTS as comma-separated issue numbers
- Use "Closes #<number>" format to auto-close issues upon PR merge
- Base the PR on current changes compared to the main branch
- Create new labels if no suitable ones exist
- Include important context from issue comments in the PR description