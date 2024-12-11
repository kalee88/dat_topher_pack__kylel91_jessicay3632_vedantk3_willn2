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
           return [response_json['kind'],
                   response_json['family'],
                   response_json['subsets'],
                   response_json['menu'],
                   response_json['variants'],
                   response_json['version'],
                   response_json['axes'],
                   response_json['lastModified'],
                   response_json['files']
           ]
       else:
           print(f'Failed to retrieve data {response.status_code}')
   except requests.exceptions.RequestException as e:
       #Also here
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
           return [response_json['title'],
                   response_json['subject'],
                   response_json['what'],
                   response_json['when'],
                   response_json['where'],
                   response_json['who'],
                   response_json['text']
           ]
       else:
           print(f"Failed to retrieve data {response.status_code}")
   except requests.exceptions.RequestException as e:
       #Also here
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
            return [response_json['id'],
                    response_json['type'],
                    response_json['proxyFor'],
                    response_json['proxyln'],
                    response_json['created'],
                    response_json['modified'],
                    response_json['rights']
                    response_json['source']
            ]
        else:
            print(f"Failed to retrieve data {response.status_code}")
    except requests.exceptions.RequestException as e:
        #Also here
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
            return [response_json['title'],
                    response_json['subject'],
                    response_json['what'],
                    response_json['when'],
                    response_json['where'],
                    response_json['who'],
                    response_json['text']
            ]
        else:
            print(f"Failed to retrieve data {response.status_code}")
    except requests.exceptions.RequestException as e:
        #Also here
        return None

# Couldn't find all the fields for this dictionary
def searchAPI():
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
       #Also here
       return None


def pinnacleOdds():
   url = f"https://pinnacle-odds.p.rapidapi.com/kit/v1/special-markets"
   api_key = os.getenv("pinnacleodds_key")
   querystring = {
    "sport_id": {sid},
    "is_have_odds": {odds},
    "event_id": {eid}
    }
   headers = {
   "x-rapidapi-key": {api_key},
   "x-rapidapi-host": "pinnacle-odds.p.rapidapi.com"
   }
   try:
       response = requests.get(url, headers=headers)
       if response.status_code == 200:
           sports_data = response.txt
           sports_json = json.loads(sport_data)
           return [sports_json['sports_id'],
                   sports_json['sport_name'],
                   sports_json['last'],
                   sports_json['events'],
                   sports_json['event_id'],
                   sports_json['league_id'],
                   sports_json['league_name'],
                   sports_json['starts'],
                   sports_json['last'],
                   sports_json['home']
           ]
       else:
           print(f"Failed to retrieve data {response.status_code}")
   except requests.exceptions.RequestException as e:
       #Also here
       return None


def nationalWeatherService(long,lat):
   url = f"https://api.weather.gov/points/{long},{lat}"
   try:
       response = response.get(url)
       if response.status_code == 200:
           weather_data = response.txt
           weather_json = json.loads(weather_data)
           return [weather_json['city'],
                   weather_json['state'],
                   weather_json['distance'],
                   weather_json['id'],
                   weather_json['type'],
                   weather_json['gridX'],
                   weather_json['gridY'],
                   weather_json['relativeLocation'],
                   weather_json['bearing'],
                   weather_json['unitCode'],
                   weather_json['forecast'],
                   weather_json['forecastHourly'],
                   weather_json['forecastGridData'],
                   weather_json['observationStations']
           ]
       else:
           print(f"Failed to retrieve data {response.status_code}")
   except requests.exceptions.RequestException as e:
       return None
