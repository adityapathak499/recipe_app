import sqlite3

def create_database(db_path):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    create_user_table = '''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        );
    '''

    create_recipe_table = '''
        CREATE TABLE IF NOT EXISTS recipe (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            ingredients TEXT NOT NULL,
            instructions TEXT NOT NULL,
            created_by INTEGER NOT NULL,
            FOREIGN KEY (created_by) REFERENCES user (id)
        );
    '''

    cursor.execute(create_user_table)
    cursor.execute(create_recipe_table)

    connection.commit()
    connection.close()
