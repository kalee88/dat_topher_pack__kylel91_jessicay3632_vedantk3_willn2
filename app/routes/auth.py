# Kyle Lee, Jessica Yu, Vedant Kothari, Will Nzeuton
# Team datTopherPack
# SoftDev
# p01 
# 2024-12-07

from flask import render_template, request, redirect, url_for, flash, session
from app import app

@app.route("/login", methods=['GET', 'POST'])
def login():
        return render_template("login.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
        return render_template("signup.html")