Please create a pull request based on the current changes compared to the main branch.

The issues to close are: $ARGUMENTS (comma-separated issue numbers)

Follow these steps:

1.  **Check for existence of argument**

    - Check if `$ARGUMENTS` is provided.
    - If `$ARGUMENTS` is not given, terminate the process immediately.
    - When terminating, prompt the user to pass the issue number argument.

2.  **Check Current Changes**

    - Use `git status` and `git diff main` to review changes
    - Ensure there are staged or unstaged changes to include in the PR

3.  **Create Pull Request**

    - Push the branch to the repository
    - Create a pull request using `gh pr create` with:
      - A clear title summarizing the changes
      - Appropriate labels (e.g., `bug`, `feature`, `enhancement`)
      - Create new labels if necessary
      - A description including a summary of changes and "Closes #<issue_number>" for each issue in $ARGUMENTS

4.  **PR Description Format**
    - Include a summary of what was changed
    - ALWAYS write the description in Japanese.
    - Include "Closes #<issue_number>" statements for each issue (parsed from $ARGUMENTS)
    - Example: If $ARGUMENTS is "123,456", include "Closes #123" and "Closes #456" in the description

Remember:

- Parse $ARGUMENTS as comma-separated issue numbers
- Use "Closes #<number>" format to auto-close issues upon PR merge
- Base the PR on current changes compared to the main branch
- Create new labels if no suitable ones exist
