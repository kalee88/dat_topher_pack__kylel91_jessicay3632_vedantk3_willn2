# Kyle Lee, Jessica Yu, Vedant Kothari, Will Nzeuton
# Team datTopherPack
# SoftDev
# p01
# 2024-12-07

from flask import render_template, request, redirect, url_for, flash, session
from app import app
from .auth import *
from app.utils.api import *

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
    special_markets = getSpecialMarkets()
    event_details = getEventDetails()
    leagues = getLeagues()
    periods = getPeriods()
    markets = getMarkets()
    archive_events = getArchiveEvents()
    betting_status = getBettingStatus()
    sports = getListOfSports()
    return render_template('sports.html', special_markets=special_markets, event_details=event_details, leagues=leagues, periods = period, markets = markets, archive_events = archive_events, betting_status = betting_status, sports=sports)

@app.route('/sport/<int:sport_id>')
def sportGames(id):
    events = getEventDetails(id)
    event_details = event.get('events', [])[0]
    return render_template('sportGames.html',event = events, event_details=event_details)

@app.route("/weather")
def weather():
    return render_template("weather.html")
