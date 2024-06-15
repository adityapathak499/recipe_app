import sqlite3
import json

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def create_recipe(title, description, ingredients, instructions, created_by):
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()
    ingredients_json = json.dumps(ingredients)
    cursor.execute('INSERT INTO recipe (title, description, ingredients, instructions, created_by) VALUES (?, ?, ?, ?, ?)',
                   (title, description, ingredients_json, instructions, created_by))
    conn.commit()
    conn.close()

def get_recipe_by_id(recipe_id):
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM recipe WHERE id=?', (recipe_id,))
    recipe = dictfetchall(cursor)
    conn.close()
    return recipe

def get_recipe():
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM recipe')
    recipe = dictfetchall(cursor)
    conn.close()
    return recipe

def update_recipe(recipe_id, title, description, ingredients, instructions):
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()
    ingredients_json = json.dumps(ingredients)
    cursor.execute('UPDATE recipe SET title=?, description=?, ingredients=?, instructions=? WHERE id=?',
                   (title, description, ingredients_json, instructions, recipe_id))
    conn.commit()
    conn.close()

def delete_recipe(recipe_id):
    conn = sqlite3.connect('recipes.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM recipe WHERE id=?', (recipe_id,))
    conn.commit()
    conn.close()
