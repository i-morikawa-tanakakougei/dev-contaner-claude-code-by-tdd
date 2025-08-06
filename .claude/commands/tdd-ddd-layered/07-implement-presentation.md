Implement presentation layer (API endpoints, CLI, or UI).

Follow these steps:

1. **Check Prerequisites**:
   - Verify all other layers are implemented
   - Ensure use cases are working with integration tests
   - Decide on presentation type (REST API, GraphQL, CLI, etc.)

2. **Create Presentation Structure**:
   ```
   presentation/
   ├── api/          # For REST/GraphQL
   │   ├── controllers/
   │   ├── validators/
   │   └── serializers/
   ├── cli/          # For command-line interface
   └── web/          # For web UI
   ```

3. **For REST API Implementation**:
   
   a. **Create Controllers**:
   ```python
   # presentation/api/controllers/<feature>_controller.py
   class <Feature>Controller:
       def __init__(self, use_case: <UseCase>):
           self._use_case = use_case
       
       def handle_post(self, request_data: dict) -> dict:
           # 1. Validate input
           # 2. Convert to DTO
           # 3. Call use case
           # 4. Serialize response
           # 5. Handle errors
           pass
   ```
   
   b. **Input Validation**:
   ```python
   # presentation/api/validators/<feature>_validator.py
   def validate_<feature>_request(data: dict) -> dict:
       # Validate required fields
       # Check data types
       # Return validated data or raise ValidationError
       pass
   ```
   
   c. **Response Serialization**:
   ```python
   # presentation/api/serializers/<feature>_serializer.py
   def serialize_<feature>_response(response: <ResponseDTO>) -> dict:
       # Convert DTO to JSON-serializable dict
       pass
   ```

4. **Set Up Web Framework** (e.g., FastAPI, Flask):
   ```python
   # presentation/api/app.py
   from fastapi import FastAPI, HTTPException
   
   app = FastAPI()
   
   @app.post("/<resource>")
   async def create_<resource>(request: <RequestModel>):
       try:
           controller = <Feature>Controller(use_case)
           response = controller.handle_post(request.dict())
           return response
       except ValidationError as e:
           raise HTTPException(status_code=400, detail=str(e))
   ```

5. **Error Handling**:
   - Map domain exceptions to HTTP status codes
   - Create consistent error response format
   - Log errors appropriately

6. **Write E2E Tests**:
   ```python
   # tests/e2e/api/test_<feature>_api.py
   def test_create_<resource>_success():
       # Test successful API call
       response = client.post("/<resource>", json={...})
       assert response.status_code == 201
   
   def test_create_<resource>_validation_error():
       # Test validation errors
       response = client.post("/<resource>", json={})
       assert response.status_code == 400
   ```

7. **API Documentation**:
   - Generate OpenAPI/Swagger docs
   - Document request/response schemas
   - Include example requests

8. **For CLI Implementation**:
   ```python
   # presentation/cli/<feature>_commands.py
   import click
   
   @click.command()
   @click.option('--param', required=True)
   def <feature>_command(param):
       """Execute <feature> use case from CLI"""
       # Similar flow to API controller
       pass
   ```

9. **Dependency Injection Setup**:
   - Wire up all dependencies
   - Configure database connections
   - Set up logging

10. **Run Full Test Suite**:
    - Unit tests: `pytest tests/unit/`
    - Integration tests: `pytest tests/integration/`
    - E2E tests: `pytest tests/e2e/`
    - All should pass

11. **Create Usage Documentation**:
    - API endpoint documentation
    - Example curl commands
    - Setup instructions

12. **Update Issue**:
    - Comment: `gh issue comment $ARGUMENTS --body "プレゼンテーション層の実装を完了しました。APIエンドポイントが利用可能です。"`
    - Include example API calls

13. **Final Steps**:
    - Suggest running full integration test in Japanese
    - Provide summary of implemented feature
    - Guide on deployment options

Important Notes:
- Keep presentation layer thin
- No business logic in controllers
- Proper HTTP status codes and error messages
- Consider API versioning strategy
- Security considerations (auth, CORS, rate limiting)
- All user-facing output must be in JAPANESE