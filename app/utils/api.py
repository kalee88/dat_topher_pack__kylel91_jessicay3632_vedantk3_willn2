# Kyle Lee, Jessica Yu, Vedant Kothari, Will Nzeuton
# Team datTopherPack
# SoftDev
# p01
# 2024-12-07


import urllib.request
import urllib.parse
import json
import zlib

def getPinnacleKey():
    with open("app/keys/key_pinnacleodds.txt", "r") as file:
        return file.read().strip()

def getEuropeanaKey():
    with open("app/keys/key_Europeana.txt", "r") as file:
        return file.read().strip()

def getGoogleFontKey():
    with open("app/keys/key_GoogleFonts.txt", "r") as file:
        return file.read().strip()

def getSearchKey():
    with open("app/keys/key_SearchAPI.txt", "r") as file:
        return file.read().strip()

#---Europeana Functions---#
'''
def searchEuro(query = '1500-2000'):
    api_key = getEuropeanaKey()
    if not api_key:
        print("NO API KEY :(")
        return None
    params = {
        'query': query,
        'apiKey': api_key,
        'rows': 10,
        'start': 1,
        'language': 'en',
    }
    url = f"https://api.europeana.eu/record/v2/search.json?query={urllib.parse.quote(query)}&wskey={api_key}"
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode("utf-8")
            logger.debug(f"Raw Response Data: {data}")
            print(data) 
            return json_data
    except Exception as e:
        print(f"Error : {e}")
        return None'''

def searchEuro(query="Paris"):
    api_key = getEuropeanaKey()

    if not api_key:
        print("No Europeana API key provided.")
        return None

    # Europeana search URL with query as 'Paris'
    url = f"https://api.europeana.eu/record/v2/search.json?query={urllib.parse.quote(query)}&wskey={api_key}&rows=10&start=1&lang=en&fl=title,creator,year"

    try:
        print(f"Making API request to: {url}")
        with urllib.request.urlopen(url) as response:
            data = response.read().decode("utf-8")
            #print(f"Raw Response Data: {data}")
            json_data = json.loads(data)
            for i in json_data['items']:
                #print(list(i['dcTitleLangAware'].values())[0][0])
                break
            return json_data
    except Exception as e:
        print(f"Error in searchEuro: {e}")
        return None

#---Sports Functions---#

#returns list of dictionaries containing information on ended soccer games
#page_num is just which page of results you want 
#events_num is how many events you want from said page
def getPinnacleResponse(page_num, events_num):
    url = "https://pinnacle-odds.p.rapidapi.com/kit/v1/archive"
    querystring = {"sport_id": "1", "page_num": page_num}

    query_params = urllib.parse.urlencode(querystring)
    full_url = f"{url}?{query_params}"

    headers = {
        "x-rapidapi-key": getPinnacleKey(),
        "x-rapidapi-host": "pinnacle-odds.p.rapidapi.com",
    }
    request = urllib.request.Request(full_url, headers=headers)

    try:
        with urllib.request.urlopen(request) as response:

            raw_data = response.read()
            
            data = zlib.decompress(raw_data, 16 + zlib.MAX_WBITS).decode("utf-8")

            json_data = json.loads(data)
            #hop into the json stuff and pick out what we actually need
            events = json_data['events'][:events_num]

            wanted_fields = ['league_name', 'home', 'away', 'starts']
            final_events = []
            for event in events:
                parsed_event = {}
                for field in wanted_fields:
                    parsed_event[field] = event[field]
                results = event['period_results']
                parsed_event['cancelled'] = False
                if(results[0]['cancellation_reason'] is not None):
                    parsed_event['cancelled'] = True
                parsed_event['home_score'] = results[0]['team_1_score']
                parsed_event['away_score'] = results[0]['team_2_score']
                final_events.append(parsed_event)

            return final_events
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code}, {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
    except Exception as e:
            print(e)
            return None

def generate_sport_card(event):

    html = """
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                padding: 20px;
            }
            .card {
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 15px;
                margin-bottom: 20px;
                background: #fff;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
            .card h3 {
                margin: 0;
                font-size: 1.5em;
                color: #333;
            }
            .card p {
                margin: 5px 0;
                color: #555;
            }
            .card .score {
                font-weight: bold;
                color: #007bff;
            }
        </style>
    </head>
    <body>
    """
    

    league_name = event['league_name']
    home_team = event['home']
    away_team = event['away']
    start_time = event['starts'][:10]
    home_score = event['home_score']
    away_score = event['away_score']
    cancelled = event['cancelled']
    
    card_html = f"""
    <div class="card">
        <h3>{home_team} vs {away_team}</h3>
        <p>League: {league_name}</p>
        <p>Start Time: {start_time}</p>
        <p>Score: 
            <span class="score">{home_team} {home_score} - {away_score} {away_team}</span>
        </p>
        {"<p>This event was cancelled.</p>" if cancelled else ""}
        <form method="POST" action="/favorite">
            <button type="submit" name="event" value="{event}">
                &#9733;
            </button>
        </form>
    </div>
    """
    html += card_html
    
    html += """
    </body>
    </html>
    """
    
    return html

#---weather api ----
def getWeatherResponse(latitude=40.7128, longitude=-74.006):
    url = f"https://api.weather.gov/points/{latitude},{longitude}" 
    request = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(request) as response:
            data = json.loads(response.read().decode('utf-8'))
            return data['properties']['forecast']
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code}, {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
def parseForecast(data):
    request = urllib.request.Request(data)

    try:
        with urllib.request.urlopen(request) as response:
            data = json.loads(response.read().decode('utf-8'))
            
            period = data['properties']['periods'][0]
            useful_fields = ['isDaytime', 'temperature', 'windSpeed', 'windDirection', "detailedForecast", 'icon']
            limited_data = {}
            for field in useful_fields:
                limited_data[field] = period[field]
            limited_data['probabilityOfPrecipitation'] = period['probabilityOfPrecipitation']['value']

            return limited_data
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code}, {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
