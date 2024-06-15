# routes/recipe_routes.py

from flask import Blueprint, jsonify, request, session
from flask_login import current_user
import json
from models.recipe import create_recipe, get_recipe, update_recipe, delete_recipe,get_recipe_by_id

recipe_bp = Blueprint('recipe_bp', __name__)

def is_authenticated():
    if not current_user.is_authenticated:
        return jsonify({'message': 'Login required'}), 401
    return None

@recipe_bp.route('/recipes', methods=['POST'])
def create_recipe_route():
    auth_response = is_authenticated()
    if auth_response:
        return auth_response
    try:
        data = request.get_json()
        title = data['title']
        description = data.get('description', '')
        ingredients = data['ingredients']
        ingredients_json = json.dumps(ingredients)
        instructions = data['instructions']
        created_by = current_user.id
        
        create_recipe(title, description, ingredients_json, instructions, created_by)
        return jsonify({'message': 'Recipe created successfully'})
    except Exception as e:
        print(e)

@recipe_bp.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe_id(recipe_id):
    auth_response = is_authenticated()
    if auth_response:
        return auth_response
    try:
        recipe = get_recipe_by_id(recipe_id)
        if recipe:
            return jsonify({'recipe': recipe})
        else:
            return jsonify({'message': 'Recipe not found'}), 404
    except Exception as e:
        print(e)

@recipe_bp.route('/recipes', methods=['GET'])
def get_recipe_all():
    auth_response = is_authenticated()
    if auth_response:
        return auth_response
    try:
        recipe = get_recipe()
        if recipe:
            return jsonify({'recipe': recipe})
        else:
            return jsonify({'message': 'Recipe not found'}), 404
    except Exception as e:
        print(e)

@recipe_bp.route('/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe_route(recipe_id):
    auth_response = is_authenticated()
    if auth_response:
        return auth_response
    try:
        data = request.get_json()
        title = data['title']
        description = data.get('description', '')
        ingredients = data['ingredients']
        instructions = data['instructions']
        
        update_recipe(recipe_id, title, description, ingredients, instructions)
        return jsonify({'message': 'Recipe updated successfully'})
    except Exception as e:
        print(e)

@recipe_bp.route('/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe_route(recipe_id):
    auth_response = is_authenticated()
    if auth_response:
        return auth_response
    try:
        delete_recipe(recipe_id)
        return jsonify({'message': 'Recipe deleted successfully'})
    except Exception as e:
        print(e)