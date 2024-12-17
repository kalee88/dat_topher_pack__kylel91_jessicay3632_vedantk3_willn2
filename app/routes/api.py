from flask import render_template, request
from app import app
from app.utils.api import *

@app.route("/events")
def events():
    return render_template("events.html")

@app.route("/arts")
def arts():
    return render_template("arts.html")

@app.route("/sports")
def sports():
    page_num = request.args.get('pageNum')
    if(page_num == None):
        page_num = 1
    events = getPinnacleResponse(page_num, 10)
    if(events == None):
        return render_template('sports.html', cards = [])
    cards = []
    for event in events:
        html = generate_sport_card(event)
        cards.append(html)
    return render_template('sports.html', cards = cards, page_num = int(page_num))

@app.route('/sport/<int:sport_id>')
def sportGames(id):
    events = getEventDetails(id)
    event_details = event.get('events', [])[0]
    return render_template('sportGames.html',event = events, event_details=event_details)

@app.route("/weather")
def weather():
    return render_template("weather.html")
