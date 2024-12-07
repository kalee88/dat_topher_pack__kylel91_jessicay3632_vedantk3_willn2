from flask import render_template, request, redirect, url_for, flash, session
from app import app

@app.route("/login", methods=['GET', 'POST'])
def login():
        return render_template("login.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
        return render_template("signup.html")