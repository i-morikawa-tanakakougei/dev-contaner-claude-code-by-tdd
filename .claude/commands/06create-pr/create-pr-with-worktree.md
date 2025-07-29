Please create a pull request based on the current changes in the active Git worktree compared to the main branch.

The issues to close are: $ARGUMENTS (comma-separated issue numbers)

Follow these steps:

1.  **Check for existence of argument**

    - Check if `$ARGUMENTS` is provided.
    - If `$ARGUMENTS` is not given, terminate the process immediately.
    - When terminating, prompt the user to pass the issue number argument.

2.  **Check Current Changes**

    - Use `git status` to check the status of the current worktree
    - Use `git diff origin/main` to compare the current worktree's branch with the `main` branch
    - Ensure there are staged or unstaged changes to include in the PR
    - If no changes are found, exit with an error message

3.  **Prepare the Branch**

    - Identify the current branch in the worktree using `git rev-parse --abbrev-ref HEAD`
    - Stage all changes with `git add .`
    - Commit changes with a message summarizing the changes (e.g., "Implement changes for issues #$ARGUMENTS")
    - Push the branch to the remote repository using `git push origin <current-branch>`

4.  **Create Pull Request**

    - Create a pull request using `gh pr create` with:
      - A title summarizing the changes (e.g., "Implement fixes for issues #$ARGUMENTS")
      - A description in Japanese that summarizes the changes
      - Include "Closes #<issue_number>" for each issue in $ARGUMENTS
    - Use the current branch as the source and `main` as the target branch

5.  **PR Description Format**
    - Write the description in Japanese, summarizing the changes
    - Include "Closes #<issue_number>" for each issue in $ARGUMENTS
    - Example: If $ARGUMENTS is "123,456", include "Closes #123" and "Closes #456" in the description

Remember:

- Parse $ARGUMENTS as comma-separated issue numbers
- Use "Closes #<number>" format to automatically close issues when PR is merged
- Base the PR on the current worktree's branch compared to the `main` branch
- Ensure the `gh` CLI is configured and authenticated
