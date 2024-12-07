import urllib.request
from urllib.request import Request
from urllib.request import urlopen
import json

keys = ["key_Europeana.txt", "key_GoogleFonts.txt", "key_SearchAPI","key_pinnacleodds.txt"]
for i in range(len(keys)):
    file = open("..keys/" + keys[i], "r")
    keys[i] = file.read()
    file.close()
keys = [key.strip() for key in keys]

#Just use keys list to access api_key
#We can try to handle the responses with other functions, these just get the response
#URL - https://www.googleapis.com/webfonts/v1/webfonts?key=YOUR-API-KEY
def googFonts(url,api_key):
    headers = {"Authorization": f"Bearer {api_key}"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json() 
        else:
            #We can put some error message here
            return None
    except requests.exceptions.RequestException as e:
        #Also here
        return None

#Url - https://api.europeana.eu/...
def Europeana(url,api_key):
    headers = {"Authorization": f"Bearer {api_key}"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json() 
        else:
            #We can put some error message here
            return None
    except requests.exceptions.RequestException as e:
        #Also here
        return None

#Url???? - https://www.searchapi.io/api/v1/search \
def searchAPI(url,api_key):
    headers = {"Authorization": f"Bearer {api_key}"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json() 
        else:
            #We can put some error message here
            return None
    except requests.exceptions.RequestException as e:
        #Also here
        return None

#URL - Idk
def pinnacleOdds(url,api_key):
    headers = {"Authorization": f"Bearer {api_key}"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json() 
        else:
            #We can put some error message here
            return None
    except requests.exceptions.RequestException as e:
        #Also here
        return None

#No need for parameters as we don't need to hide our API keys
def weatherData(long,lat):
    url = f"https://api.weather.gov/points/{long},{lat}"
    try:
        response = response.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.exceptions.RequestException as e:
        return None
