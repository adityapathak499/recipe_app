# app.py

from flask import Flask, session
from routes.recipe_routes import recipe_bp
from routes.auth_routes import auth_bp
from db.create_database import create_database
from flask_login import LoginManager
from models.user import User

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth_bp.login'

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)

# Register blueprints
app.register_blueprint(recipe_bp)
app.register_blueprint(auth_bp)

# Initialize database
create_database('./recipes.db')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
