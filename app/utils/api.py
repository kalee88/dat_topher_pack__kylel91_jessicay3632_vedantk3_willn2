# Kyle Lee, Jessica Yu, Vedant Kothari, Will Nzeuton
# Team datTopherPack
# SoftDev
# p01
# 2024-12-07


import urllib.request
from urllib.request import Request
from urllib.request import urlopen
import json
from dotenv import load_dotenv, dotenv_values
import os
load_dotenv()

#env file is stored locally
keys = [os.getenv("europeana_key"), os.getenv("googlefonts_key"), os.getenv("search_key"), os.getenv("pinnacleodds_key")]

#We can try to handle the responses with other functions, these just get the response
def googFonts(font):
   url = f"https://www.googleapis.com/webfonts/v1/webfonts?key="
   api_key = os.getenv("googlefonts_key")
   headers = {"Authorization": f"Bearer {api_key}"}
   try:
       response = requests.get(url, headers=headers)
       if response.status_code == 200:
           fonts_data = response.txt
           response_json = json.loads(fonts_data)
           return render_template('arts.html', kind = response_json['kind'], family = response_json['family'], subsets = response_json['subsets'], menu = response_json['menu'], variants =  response_json['variants'], version = response_json['version'], axes = response_json['axes'], lastModified = response_json['lastModified'], files = response_json['files'])
       else:
           print(f'Failed to retrieve data {response.status_code}')
   except requests.exceptions.RequestException as e:
       return None


def searchEuro(query):
   api_key = os.getenv("europeana_key")
   url = f"https://api.europeana.eu/record/v2/search.json?query" + query + f"&wskey:" + api_key
   headers = {"Authorization": f"Bearer {api_key}"}
   try:
       response = requests.get(url, headers=headers)
       if response.status_code == 200:
           art_data = response.txt
           response_json = json.loads(art_data)
           return render_template('arts.html', title = response_json['title'], subject = response_json['subject'], what = response_json['what'], when = response_json['when'], where = response_json['where'], who = response_json['who'], text = response_json['text'])
       else:
           print(f"Failed to retrieve data {response.status_code}")
   except requests.exceptions.RequestException as e:
       return None

def dataEuro(entity_type, entity_id):
    url = f"http://data.europeana.eu/" + entity_type + f"/" + entity_id
    api_key = os.getenv("europeana_key")
    headers = {"Authorization": f"Bearer {api_key}"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            art_data = response.txt
            response_json = json.loads(art_data)
            return render_template('arts.html', id1 = response_json['id'], type1 = response_json['type'], proxyFor = response_json['proxyFor'], proxyIn = response_json['proxyln'], created = response_json['created'], modified = response_json['modified'], rights = response_json['rights'], source = response_json['source'])
        else:
            print(f"Failed to retrieve data {response.status_code}")
    except requests.exceptions.RequestException as e:
        return None

def recommendEuro(set_id):
    url = f"https://api.europeana.eu/recommend/set/" + set_id
    api_key = os.getenv("europeana_key")
    headers = {"Authorization": f"Bearer {api_key}"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            art_data = response.txt
            response_json = json.loads(art_data)
            return render_template('arts.html', title = response_json['title'], subject = response_json['subject'], what = response_json['what'], when = response_json['when'], where = response_json['where'], who = response_json['who'], text = response_json['text'])
        else:
            print(f"Failed to retrieve data {response.status_code}")
    except requests.exceptions.RequestException as e:
        return None

def searchAPI(search):
   url = f"https://www.searchapi.io/api/v1/search?apihttps://api.europeana.eu/record/v2/[_key="
   api_key = os.getenv("search_key")
   headers = {"Authorization": f"Bearer {api_key}"}
   params = {
     "engine": "google",
     "q": {search}
   }
   try:
       response = requests.get(url, headers=headers, params=params)
       if response.status_code == 200:
           search_data = response.json()
           return search_data
       else:
           print(f"Failed to retrieve data {response.status_code}")
   except requests.exceptions.RequestException as e:
       return None


#All the Pinnacle Odd methods 
def getSpecialMarkets():
    url = f"https://pinnacle-odds.p.rapidapi.com/kit/v1/special-markets"
    api_key = os.getenv("pinnacleodds_key")
    querystring = {"is_have_odds":"true", "sport_id":"1"}
    headers = {
	"x-rapidapi-key": {api_key},
	"x-rapidapi-host": "pinnacle-odds.p.rapidapi.com"
    }
    try:
       response = requests.get(url, headers=headers, params=querystring)
       if response.status_code == 200:
           sports_data = response.json()
           return sports_data
       else:
           print(f"Failed to retrieve data {response.status_code}")
    except requests.exceptions.RequestException as e:
       return None

def getEventDetails():
    url = f"https://pinnacle-odds.p.rapidapi.com/kit/v1/details"
    api_key = os.getenv("pinnacleodds_key")
    querystring = {"event_id":"1419211461"}
    headers = {
	"x-rapidapi-key": {api_key},
	"x-rapidapi-host": "pinnacle-odds.p.rapidapi.com"
    }
    try:
       response = requests.get(url, headers=headers, params=querystring)
       if response.status_code == 200:
           sports_data = response.json()
           return sports_data
       else:
           print(f"Failed to retrieve data {response.status_code}")
    except requests.exceptions.RequestException as e:
       return None

def getEventDetails(id):
    url = f"https://pinnacle-odds.p.rapidapi.com/kit/v1/details"
    api_key = os.getenv("pinnacleodds_key")
    querystring = {"event_id": id}
    headers = {
	"x-rapidapi-key": {api_key},
	"x-rapidapi-host": "pinnacle-odds.p.rapidapi.com"
    }
    try:
       response = requests.get(url, headers=headers, params=querystring)
       if response.status_code == 200:
           sports_data = response.json()
           return sports_data
       else:
           print(f"Failed to retrieve data {response.status_code}")
    except requests.exceptions.RequestException as e:
       return None

def getLeagues():
    url = f"https://pinnacle-odds.p.rapidapi.com/kit/v1/leagues"
    api_key = os.getenv("pinnacleodds_key")
    querystring = {"sport_id":"1"}
    headers = {
	"x-rapidapi-key": {api_key},
	"x-rapidapi-host": "pinnacle-odds.p.rapidapi.com"
    }
    try:
       response = requests.get(url, headers=headers, params=querystring)
       if response.status_code == 200:
           sports_data = response.json()
           return sports_data
       else:
           print(f"Failed to retrieve data {response.status_code}")
    except requests.exceptions.RequestException as e:
       return None

def getPeriods():
    url = f"https://pinnacle-odds.p.rapidapi.com/kit/v1/meta-periods"
    api_key = os.getenv("pinnacleodds_key")
    querystring = {"sport_id":"1"}
    headers = {
	"x-rapidapi-key": {api_key},
	"x-rapidapi-host": "pinnacle-odds.p.rapidapi.com"
    }
    try:
       response = requests.get(url, headers=headers, params=querystring)
       if response.status_code == 200:
           sports_data = response.json()
           return sports_data
       else:
           print(f"Failed to retrieve data {response.status_code}")
    except requests.exceptions.RequestException as e:
       return None

def getMarkets():
    url = f"https://pinnacle-odds.p.rapidapi.com/kit/v1/markets"
    api_key = os.getenv("pinnacleodds_key")
    querystring = {"sport_id":"1","is_have_odds":"true"}
    headers = {
	"x-rapidapi-key": {api_key},
	"x-rapidapi-host": "pinnacle-odds.p.rapidapi.com"
    }
    try:
       response = requests.get(url, headers=headers, params=querystring)
       if response.status_code == 200:
           sports_data = response.json()
           return sports_data
       else:
           print(f"Failed to retrieve data {response.status_code}")
    except requests.exceptions.RequestException as e:
       return None

def getArchiveEvents():
    url = f"https://pinnacle-odds.p.rapidapi.com/kit/v1/archive"
    api_key = os.getenv("pinnacleodds_key")
    querystring = {"sport_id":"1","page_num":"1"}
    headers = {
	"x-rapidapi-key": {api_key},
	"x-rapidapi-host": "pinnacle-odds.p.rapidapi.com"
}
    try:
       response = requests.get(url, headers=headers, params=querystring)
       if response.status_code == 200:
           sports_data = response.json()
           return sports_data
       else:
           print(f"Failed to retrieve data {response.status_code}")
    except requests.exceptions.RequestException as e:
       return None

def getBettingStatus():
    url = f"https://pinnacle-odds.p.rapidapi.com/kit/v1/betting-status"
    api_key = os.getenv("pinnacleodds_key")
    headers = {
	"x-rapidapi-key": {api_key},
	"x-rapidapi-host": "pinnacle-odds.p.rapidapi.com"
}
    try:
       response = requests.get(url, headers=headers)
       if response.status_code == 200:
           sports_data = response.json()
           return sports_data
       else:
           print(f"Failed to retrieve data {response.status_code}")
    except requests.exceptions.RequestException as e:
       return None

def getListOfSports():
    url = f"https://pinnacle-odds.p.rapidapi.com/kit/v1/sports"
    api_key = os.getenv("pinnacleodds_key")
    headers = {
	"x-rapidapi-key": {api_key},
	"x-rapidapi-host": "pinnacle-odds.p.rapidapi.com"
}
    try:
       response = requests.get(url, headers=headers)
       if response.status_code == 200:
           sports_data = response.json()
           return sports_data
       else:
           print(f"Failed to retrieve data {response.status_code}")
    except requests.exceptions.RequestException as e:
       return None

def nationalWeatherService(long,lat):
   url = f"https://api.weather.gov/points/{long},{lat}"
   try:
       response = response.get(url)
       if response.status_code == 200:
           weather_data = response.txt
           response_json = json.loads(weather_data)
           return render_template('weather.html', city = response_json['city'], state = response_json['state'], distance = response_json['distance'], id1 = response_json['id'], type = response_json['type'], gridX = response_json['gridX'], gridY = response_json['gridY'], relativeLocation = response_json['relativeLocation'], forecast = response_json['forecast'], forecastHourly = response_json['forecastHourly'], forecastGridData = response_json['forecastGridData'], observationStations = response_json['observationStations'])           
       else:
           print(f"Failed to retrieve data {response.status_code}")
   except requests.exceptions.RequestException as e:
       return None
