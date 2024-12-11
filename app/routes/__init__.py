# Kyle Lee, Jessica Yu, Vedant Kothari, Will Nzeuton
# Team datTopherPack
# SoftDev
# p01
# 2024-12-07

from flask import render_template, request, redirect, url_for, flash, session
from app import app
from .auth import *
# from app.utils.api import *

@app.route("/")
def home():
    return render_template('index.html', is_logged_in = auth.is_logged_in(), logged_in_user = auth.get_logged_in_user())

@app.route("/events")
def events():
    return render_template("events.html")

@app.route("/arts")
def arts():
    return render_template("arts.html")

@app.route("/sports")
def sports():
    return render_template("sports.html")

@app.route("/weather")
def weather():
    return render_template("weather.html")
