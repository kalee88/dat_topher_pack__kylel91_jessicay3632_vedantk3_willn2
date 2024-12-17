# Kyle Lee, Jessica Yu, Vedant Kothari, Will Nzeuton
# Team datTopherPack
# SoftDev
# p01
# 2024-12-07

from flask import render_template, request, redirect, url_for, flash, session
import json
from app import app
from app.utils.auth import get_logged_in_user
from app.utils.database import create_favorite, read_favorites

@app.route("/favorite", methods=["GET", "POST"])
def favorite():
    print("favoriting")
    try:
        user_id = get_logged_in_user()[0]
    except:
        return redirect(url_for('home'))
    data = request.form.get("data")
    if(data == None):
        return redirect(url_for('home'))
    
    data_split = data.split('BREAKBREAKBREAK')
    type = data_split[0]
    metadata = data_split[1]
    create_favorite(user_id, type, metadata.replace("'",'"'))
    return redirect(url_for('home'))

@app.route("/profile", methods=["GET", "POST"])
def profile():

    sport_favorites = read_favorites(get_logged_in_user()[0], "sport")
    sports = []
    for item in sport_favorites:
        sport = item.replace("False", "false").replace("True", "true")
        sports.append(json.loads(sport))
    
    return render_template('profile.html', sports = sports)