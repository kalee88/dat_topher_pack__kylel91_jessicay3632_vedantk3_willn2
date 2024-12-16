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