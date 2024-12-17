# Kyle Lee, Jessica Yu, Vedant Kothari, Will Nzeuton
# Team datTopherPack
# SoftDev
# p01 
# 2024-12-07

import sqlite3
import csv
import os
from flask import Flask, render_template, request, session, redirect, url_for, flash
    
app = Flask(__name__)    
app.secret_key = os.urandom(32)

from app.utils import database, auth, api

database.setup_db()
database.create_user('username', 'user@email.com', 'password')
from app.routes import *

if __name__ == "__main__": 
    app.debug = True 
    app.run()
    
    
