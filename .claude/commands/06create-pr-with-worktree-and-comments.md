Please create a pull request based on the current changes in the active Git worktree with comprehensive GitHub issue comment analysis.

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

3.  **Check Current Worktree Changes**

    - Use `git status` to check the status of the current worktree
    - Use `git diff origin/main` to compare the current worktree's branch with the `main` branch
    - Ensure there are staged or unstaged changes to include in the PR
    - If no changes are found, exit with an error message
    - Verify that the changes align with the final consensus from issue discussions

4.  **Prepare the Branch in Worktree**

    - Identify the current branch in the worktree using `git rev-parse --abbrev-ref HEAD`
    - Stage all changes with `git add .`
    - Commit changes with a message summarizing the changes (e.g., "Implement changes for issues #$ARGUMENTS")
    - Push the branch to the remote repository using `git push origin <current-branch>`

5.  **Create Pull Request**

    - Create a pull request using `gh pr create` with:
      - A clear title summarizing the changes (e.g., "Implement fixes for issues #$ARGUMENTS")
      - Appropriate labels based on all issues (e.g., `bug`, `feature`, `enhancement`)
      - Create new labels if necessary
      - Use the current branch as the source and `main` as the target branch
      - A comprehensive description that:
        - Summarizes what was changed
        - References key decisions from issue comments
        - Includes "Closes #<issue_number>" for each issue in $ARGUMENTS
        - Mentions any important implementation details discussed in comments

6.  **PR Description Format**
    - Include a summary of what was changed
    - ALWAYS write the description in Japanese
    - Reference any important architectural decisions or implementation approaches from comments
    - Include implementation notes if comments contained specific technical guidance
    - Include "Closes #<issue_number>" statements for each issue (parsed from $ARGUMENTS)
    - Example: If $ARGUMENTS is "123,456", include "Closes #123" and "Closes #456" in the description

**Key features of this command**:
- **Worktree awareness**: Works specifically with the current Git worktree and its branch
- **Complete issue context**: Analyze ALL comments on each issue, not just the original description
- **Implementation verification**: Ensure changes match the final consensus from issue discussions
- **Comprehensive PR description**: Include key decisions and context from issue comments
- **Multiple issue handling**: Analyze comments for ALL issues listed in $ARGUMENTS

Remember:
- Parse $ARGUMENTS as comma-separated issue numbers
- Use "Closes #<number>" format to automatically close issues when PR is merged
- Base the PR on the current worktree's branch compared to the `main` branch
- Ensure the `gh` CLI is configured and authenticated
- Create new labels if no suitable ones exist
- Include important context from issue comments in the PR description