Please review the local changes based on the GitHub issue and comprehensive comment analysis: $ARGUMENTS.

Follow these steps:

1.  Check if `$ARGUMENTS` is provided. If `$ARGUMENTS` is not given, terminate the process immediately. When terminating, prompt the user to pass the issue number argument.

2.  **Comprehensive issue and comments analysis**:
    - Use `gh issue view` to get the issue details including title, description, and labels.
    - Use `gh api repos/:owner/:repo/issues/$ISSUE_NUMBER/comments` to fetch ALL comments on the issue.
    - Analyze the entire conversation thread to understand:
      - Original problem statement and requirements
      - Any clarifications, updates, or additional requirements in comments
      - Technical discussions and proposed solutions
      - Architecture decisions or implementation changes mentioned
      - Implementation constraints, preferences, or specific approaches
      - Any "decision" or "conclusion" comments that modify the original scope

3.  **Requirements synthesis**:
    - Combine the original issue description with all comment discussions
    - Identify the final requirements based on the complete conversation
    - Note any changes to the original scope due to comment discussions
    - Pay special attention to comments that supersede or modify original requirements
    - Document any specific technical requirements, constraints, or architectural decisions

4.  **Local changes analysis**:
    - Check the changes of the local branch compared with the main branch using `git diff main...HEAD`
    - Analyze modified files, added files, and deleted files
    - Understand the implementation approach taken in the local changes

5.  **Comprehensive review**:
    - Compare the local implementation against the final requirements (issue + comments)
    - Evaluate if the changes fulfill ALL requirements from the issue and comment discussions
    - Check if the implementation follows any specific approaches or patterns discussed in comments
    - Verify that any architectural decisions mentioned in comments are properly implemented
    - Assess backward compatibility requirements if mentioned in discussions
    - Review code quality, maintainability, and adherence to project standards

6.  **Review feedback generation**:
    - Write detailed review feedback to `/reviews` directory in Japanese
    - Include assessment of requirement fulfillment based on issue + comments
    - Highlight any missing implementations or deviations from discussed approaches
    - Suggest improvements or corrections if needed
    - Note any positive aspects of the implementation
    - Reference specific comments when relevant to the review

**Key focus areas**:
- **Complete requirement coverage**: Ensure all requirements from issue + comments are addressed
- **Comment-driven decisions**: Prioritize requirements and decisions from comment discussions
- **Implementation approach**: Verify the approach aligns with any technical discussions in comments
- **Scope compliance**: Check that the implementation matches the final scope after comment discussions

Remember to use the GitHub CLI (`gh`) for all GitHub-related tasks.