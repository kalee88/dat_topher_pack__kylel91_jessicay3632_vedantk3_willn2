# Kyle Lee, Jessica Yu, Vedant Kothari, Will Nzeuton
# Team datTopherPack
# SoftDev
# p01 
# 2024-12-07

import sqlite3
import os

#Establish database file path
DB_FILE = os.path.join(os.path.dirname(__file__), "../db.db")

#Initializing functions ---------------
def create_tables(db):
    try:
        c = db.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE COLLATE NOCASE,
                email TEXT NOT NULL UNIQUE COLLATE NOCASE,
                password TEXT NOT NULL
            );
            ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS favorites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                content_type TEXT NOT NULL,
                metadata JSON NOT NULL,
                created_at DATETIME
            );
            ''')
        db.commit()
    except sqlite3.Error as e:
        print(f"create_table: {e}")
    finally:
        c.close()

def drop_tables(db):
    try:
        c = db.cursor()
        c.execute("DROP TABLE IF EXISTS users")
        c.execute("DROP TABLE IF EXISTS favorites")
        db.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        c.close()

def setup_db():
    db = sqlite3.connect(DB_FILE)
    drop_tables(db)
    create_tables(db)
    db.commit()
    db.close()

#External functions ---------------

#Edit existing row in users table
def modify_user(id, type, new_value):
    #sql sanitation (sanitization?) 
    if type not in ['username', 'password', 'email']:
        print("Invalid column type")
    else:
        db = sqlite3.connect(DB_FILE)
        try:
            c = db.cursor()
            c.execute(f"UPDATE users SET {type} = ? WHERE id = ?", (new_value, id))
            db.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            c.close()

#Remove row from users table
def remove_user(id):
    db = sqlite3.connect(DB_FILE)
    try: 
        c = db.cursor()
        c.execute("DELETE FROM users WHERE id = ?", (id,))
        db.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        c.close()


