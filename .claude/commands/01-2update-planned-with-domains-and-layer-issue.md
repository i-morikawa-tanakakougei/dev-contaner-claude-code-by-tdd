Please analyze and update the GitHub issue: $ARGUMENTS.

Follow these steps:

1. **Validate Input**: Check if `$ARGUMENTS` is provided. If `$ARGUMENTS` is not given, terminate the process immediately and prompt the user to provide the issue number argument.

2. **Retrieve Issue Details**: Use `gh issue view $ARGUMENTS` to fetch the details of the specified GitHub issue.

3. **Understand the Problem**: Analyze the issue description to identify the problem, requirements, and context.

4. **Domain and Functionality Analysis**:

   - Identify the domain(s) relevant to the issue using **event storming** techniques to map out key use cases, events, and aggregates.
   - Document the primary use cases and business events to ensure alignment with the domain model.
   - Break down the functionality into clear, domain-specific responsibilities.

5. **Layered Architecture Design**:

   - Design the solution using a layered architecture with the following layers:
     - **Data Layer**: Define data models, repositories, and persistence logic for each domain, ensuring separation by domain-specific folders (e.g., `src/domains/<domain>/data/`).
     - **Service Layer**: Encapsulate business logic in domain-specific services, organized in domain-specific folders (e.g., `src/domains/<domain>/services/`).
     - **Controller Layer**: Handle input/output, API endpoints, or UI interactions, organized in domain-specific folders (e.g., `src/domains/<domain>/controllers/`).
   - Ensure each layer is modular and respects domain boundaries to support scalability and maintainability in large-scale development.

6. **Codebase Search**: Search the codebase for relevant files (e.g., existing domain models, services, or controllers) to identify areas impacted by the issue. Use the folder structure `src/domains/<domain>/*` to guide the search.

7. **Plan Changes**:

   - Propose changes to address the issue, ensuring alignment with the domain model and layered architecture.
   - Specify new or modified files, organized by domain and layer (e.g., `src/domains/<domain>/data/<entity>.py`, `src/domains/<domain>/services/<service>.py`).
   - Ensure changes maintain separation of concerns and promote scalability.

8. **Update Issue**: Update the existing GitHub issue `$ARGUMENTS` with the proposed solution, including:
   - A summary of the domain and use case analysis.
   - A description of the layered architecture design.
   - A list of planned changes with file paths and their purpose.
   - Use `gh issue comment $ARGUMENTS` to add the update. NEVER create a new issue.

**Additional Guidelines**:

- Organize the codebase with a domain-driven folder structure (e.g., `src/domains/<domain>/{data,services,controllers}`) to ensure scalability and clarity.
- Validate that the design adheres to domain-driven design principles and supports large-scale development.
- Use the GitHub CLI (`gh`) for all GitHub-related operations.

**Example Folder Structure**:

```
src/
    domains/
        user/
            data/
                UserRepository.py
                UserEntity.py
            services/
                UserService.py
            controllers/
                UserController.py
        order/
            data/
                OrderRepository.py
                OrderEntity.py
            services/
                OrderService.py
            controllers/
                OrderController.py
```
