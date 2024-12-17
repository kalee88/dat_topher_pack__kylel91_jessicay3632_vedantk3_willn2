from .api import getWeatherResponse, parseForecast
weather_data = getWeatherResponse()
print(parseForecast(weather_data))