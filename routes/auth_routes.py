# routes/auth_routes.py

from flask import Blueprint, jsonify, request, session
from flask_login import login_user, logout_user, current_user
from models.user import User
import sqlite3

auth_bp = Blueprint('auth_bp', __name__)

def is_authenticated():
    if not current_user.is_authenticated:
        return jsonify({'message': 'Login required'}), 401
    return None

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']
        email = data['email']
        
        conn = sqlite3.connect('recipes.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO user (username, password, email) VALUES (?, ?, ?)', (username, password, email))
        conn.commit()
        conn.close()
        
        return jsonify({'message': 'User registered successfully'})
    except Exception as e:
        print(e)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'POST':
            data = request.get_json()
            username = data['username']
            password = data['password']
            
            user = User.get_by_username(username)
            if user and user.password == password:
                login_user(user)
                return jsonify({'message': 'Login successful'})
            else:
                return jsonify({'message': 'Login failed. Invalid username or password'}), 401
        else:
            return False
    except Exception as e:
        print(e)
        
@auth_bp.route('/logout', methods=['POST'])
def logout():
    auth_response = is_authenticated()
    if auth_response:
        return auth_response
    logout_user()
    return jsonify({'message': 'Logged out successfully'})
