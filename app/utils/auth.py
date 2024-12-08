# Kyle Lee, Jessica Yu, Vedant Kothari, Will Nzeuton
# Team datTopherPack
# SoftDev
# p01 
# 2024-12-07
import os
import sqlite3
from flask import session

DB_FILE = os.path.join(os.path.dirname(__file__), "../db.db")

def is_valid_username(username):
    return not any(c in ' ~!@#$%^&*()`\\\'\";:[]{«»‘“}|,<>/?' for c in username)

def email_password_match(email, password):
    db = sqlite3.connect(DB_FILE)
    try:
        c = db.cursor()
        c.execute("SELECT password FROM users WHERE email = ?", (email,))
        res = c.fetchone()[0]
        db.commit()
    except sqlite3.Error as e:
        print(f"email_password_math: {e}")
    finally:
        c.close()

    return res == password

def user_exists(value, type):
    db = sqlite3.connect(DB_FILE)
    try:
        c = db.cursor()
        c.execute(f"SELECT 1 FROM users WHERE {type} = ?", (value,))
        result = c.fetchone()
        print(f"{result is not None}: {value}")
        return result is not None
    except sqlite3.Error as e:
        print(f"user_exists: {e}")
    finally:
        c.close()

#Add row into users table
def insert_user(username, email, password):
    db = sqlite3.connect(DB_FILE)
    try:
        c = db.cursor()
        c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
        db.commit()
    except sqlite3.IntegrityError:
        return -1
    finally:
        c.close()

#Retrieve user id by username or email
def user_column_to_id(value, type):
    res = -1
    if type not in ['username', 'email']:
        return -2
    db = sqlite3.connect(DB_FILE)
    try:
        c = db.cursor()
        c.execute(f"SELECT id FROM users WHERE {type} = ?", (value,))
        res = c.fetchone()[0]
        db.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        c.close()
        return res
    
def fetch_user(id):
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
    
def is_logged_in():
    return 'user' in session

def get_logged_in_user():
    return session.get('user', None)