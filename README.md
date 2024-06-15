# Flask Recipe Application

This is a Flask-based application for managing user accounts and recipes. Users can register, log in, and create, update, delete, and view recipes. The application uses SQLite for data storage and supports session management with Flask-Login.

## Endpoints

### Authentication Endpoints

- `POST /register`
  - Registers a new user.
  - Request Body: `{"username": "testuser", "email": "test@example.com", "password": "testpassword"}`

- `POST /login`
  - Logs in an existing user.
  - Request Body: `{"username": "testuser", "password": "testpassword"}`

- `POST /logout`
  - Logs out an existing user.

### Recipe Endpoints

- `POST /recipes`
  - Creates a new recipe.
  - Requires user to be logged in.
  - Request Body: `{"title": "Test Recipe", "description": "This is a test recipe", "ingredients": ["ingredient1", "ingredient2"], "instructions": "Test instructions"}`

- `GET /recipes`
  - Retrieves all recipes.
  - Requires user to be logged in.

- `GET /recipes/<int:recipe_id>`
  - Retrieves a specific recipe by ID.
  - Requires user to be logged in.

- `PUT /recipes/<int:recipe_id>`
  - Updates a specific recipe by ID.
  - Requires user to be logged in.
  - Request Body: `{"title": "Updated Recipe", "description": "Updated description", "ingredients": ["ingredient1", "ingredient2"], "instructions": "Updated instructions"}`

- `DELETE /recipes/<int:recipe_id>`
  - Deletes a specific recipe by ID.
  - Requires user to be logged in.