# Kyle Lee, Jessica Yu, Vedant Kothari, Will Nzeuton
# Team datTopherPack
# SoftDev
# p01 
# 2024-12-07

from flask import render_template, request, redirect, url_for, flash, session
from app import app
from .auth import *

@app.route("/")
def home():
    return render_template('index.html')