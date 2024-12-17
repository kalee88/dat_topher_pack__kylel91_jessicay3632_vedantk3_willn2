# Kyle Lee, Jessica Yu, Vedant Kothari, Will Nzeuton
# Team datTopherPack
# SoftDev
# p01
# 2024-12-07

import sqlite3
import os
from .auth import password_hash, user_exists
#Establish database file path
DB_FILE = os.path.join(os.path.dirname(__file__), "../db.db")

# --------------- Initializing functions ---------------
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
        print(f"drop_tables: {e}")
    finally:
        c.close()

def setup_db():
    db = sqlite3.connect(DB_FILE)
    drop_tables(db)
    create_tables(db)
    db.commit()
    db.close()

# --------------- Operational Functions ---------------

# ----- users Functions -----

def create_user(username, email, password):
    db = sqlite3.connect(DB_FILE)
    try:
        c = db.cursor()
        c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password_hash(password)[0]))
        db.commit()
    except sqlite3.IntegrityError:
        print(f"create_user: {e}")
    finally:
        c.close()

def read_user(id):
    db = sqlite3.connect(DB_FILE)
    try:
        c = db.cursor()
        c.execute("SELECT * FROM users WHERE id = ?", (id,))
        user = c.fetchone()
    except sqlite3.Error as e:
        print(f"fetch_user: {e}")
    finally:
        c.close()
        return user

def update_user(id, type, new_value):
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
            print(f"update_user: {e}")
        finally:
            c.close()

def delete_user(id):
    db = sqlite3.connect(DB_FILE)
    try:
        c = db.cursor()
        c.execute("DELETE FROM users WHERE id = ?", (id,))
        db.commit()
    except sqlite3.Error as e:
        print(f"delete_user: {e}")
    finally:
        c.close()

# ----- favorites Functions -----

def create_favorite(user_id, content_type, metadata, created_at):
    valid_types = ["story", "art", "sport"]
    if(not user_exists(user_id)):
        raise KeyError(f"Could not locate user with id: {user_id}")
    if(content_type not in valid_types):
        raise KeyError(f"{contet_type} is not a valid content type")
    else:
        db = sqlite3.connect(DB_FILE)
        try:
            c = db.cursor()
            c.execute("INSERT INTO favorites (user_id, content_type, metadata, created_at) VALUES (?, ?, ?, ?)", (user_id, content_type, metadata, created_at))
            db.commit()
        except sqlite3.Error:
            print(f"create_favorite: {e}")
        finally:
            c.close()