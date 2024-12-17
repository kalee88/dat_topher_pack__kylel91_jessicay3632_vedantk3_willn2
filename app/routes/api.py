from flask import render_template, request
from app import app
from app.utils.api import *
from app.utils.auth import is_logged_in

@app.route("/events")
def events():
    news = findNews()
    return render_template('events.html', news=news["organic_results"], logged_in = is_logged_in())

@app.route("/arts")
def arts():
    query = request.args.get('query', default='Paris', type=str)
    results = searchEuro(query)
    if results:
        return render_template('arts.html', results=results, logged_in = is_logged_in())
    else:
        return render_template('arts.html', results=None, error="No results found or there was an error.")

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

@app.route("/weather")
def weather():
    weather_data = getWeatherResponse()
    data = parseForecast(weather_data)
    img = data['icon']
    day = data['isDaytime']
    windSpeed = data['windSpeed']



    windDirection = data['windDirection']
    description = data['detailedForecast']
    rainChance = data['probabilityOfPrecipitation']
    temp = data['temperature']
    return render_template("weather.html", temp = temp, img=img, day = day, windSpeed = windSpeed, windDirection=windDirection, description = description, rainChance = rainChance)
