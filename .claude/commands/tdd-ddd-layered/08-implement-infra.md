Implement infrastructure layer for persistence and external services.

Follow these steps:

1. **Check Arguments**:

   - Verify that `$ARGUMENTS` is provided
   - If not provided, terminate immediately and prompt the user to pass the issue number argument in Japanese

2. **Check Prerequisites**:

   - Verify domain and application layers are implemented
   - Check repository interfaces in `domain/repositories/`
   - Identify external dependencies needed

3. **Create Infrastructure Structure**:

   ```
   infrastructure/
   ├── repositories/
   ├── persistence/
   │   ├── models/
   │   └── mappers/
   ├── external/
   └── config/
   ```

4. **Implement Repository Concrete Classes**:

   - Choose persistence technology (e.g., SQLAlchemy, MongoDB)
   - Create concrete implementations in `infrastructure/repositories/`

   Example with SQLAlchemy:

   ```python
   # infrastructure/repositories/sql_<repository>.py
   class Sql<Repository>(<RepositoryInterface>):
       def __init__(self, session):
           self._session = session

       def save(self, entity):
           model = self._to_model(entity)
           self._session.add(model)
           self._session.commit()

       def find_by_id(self, id):
           model = self._session.query(<Model>).filter_by(id=id).first()
           return self._to_entity(model) if model else None

       def _to_model(self, entity):
           # Map domain entity to DB model
           pass

       def _to_entity(self, model):
           # Map DB model to domain entity
           pass
   ```

5. **Create Database Models**:

   - Define ORM models in `infrastructure/persistence/models/`
   - Keep models separate from domain entities

   Example:

   ```python
   # infrastructure/persistence/models/<model>.py
   class <Model>(Base):
       __tablename__ = '<table_name>'

       id = Column(Integer, primary_key=True)
       # Other columns
   ```

6. **Implement Mappers**:

   - Create mappers in `infrastructure/persistence/mappers/`
   - Handle conversion between domain objects and DB models
   - Ensure proper handling of value objects

7. **Database Migrations**:

   - Set up migration tool (e.g., Alembic)
   - Create initial migration for the feature
   - Document migration commands

8. **External Service Adapters** (if needed):

   - Implement adapters in `infrastructure/external/`
   - Use interfaces to keep domain independent
   - Handle API calls, message queues, etc.

9. **Configuration Management**:

   - Create config files in `infrastructure/config/`
   - Handle database connections
   - Environment-specific settings

10. **Write Integration Tests**:

- Test repositories with real database
- Use test database or in-memory DB
- Test transaction handling

```python
# tests/integration/repositories/test_sql_<repository>.py
def test_save_and_find():
    # Test with real database connection
    pass
```

11. **Run All Tests**:

    - Unit tests: `pytest tests/unit/`
    - Integration tests: `pytest tests/integration/`
    - Ensure all tests pass

12. **Update Documentation**:

    - Document infrastructure choices
    - Add setup instructions for database
    - Include connection string examples

13. **Update Issue**:

    - Comment: `gh issue comment $ARGUMENTS --body "インフラストラクチャ層の実装を完了しました。データベース永続化と外部サービス連携が可能になりました。"`

14. **Guide Next Steps**:
    - Suggest implementing presentation layer (`/implement-presentation`) in Japanese
    - Or suggest end-to-end testing

Important Notes:

- Keep infrastructure details isolated from domain
- Use dependency injection for flexibility
- Test with real infrastructure when possible
- Handle connection pooling and transactions properly
- Consider using repository pattern with Unit of Work
- All user-facing output must be in JAPANESE
