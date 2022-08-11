
import requests
import json

api_key = "dfa5acdcf98fda9f0d4a57765083f934"

api_url = "https://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name : ")

complete_url = api_url + "appid=" + api_key + "&units=imperial" + "&q=" + city_name

response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":

        y = x["main"]

        current_temperature = y["temp"]

        min_temperature = y["temp_min"]

        max_temperature = y["temp_max"]

        current_humidity = y["humidity"]

        z = x["weather"]
        
        weather_description = z[0]["description"]

        print(" Temperature (in fahrenheit) = " +
					str(current_temperature) +
                "\n min temperature (in fahrenheit) = " +
                                        str(min_temperature) +
                "\n min temperature (in fahrenheit) = " +
                                        str(max_temperature) +
		"\n humidity (in percentage) = " +
					str(current_humidity) +
		"\n description = " +
					str(weather_description))

else:
	print(" Unable to find city ")

