# import requests
# import citylist
# # data = citylist.citylist


# user_city = input("Please enter city name : ")
# user_country = input("Please enter country code : ")

# api_key = "76ebe261e81ed7b8bd0f4ff2aa488dc0"
# url = f"http://api.openweathermap.org/data/2.5/forecast?id={id}&APPID={api_key}"
# r = requests.get(url)
# data = r.json()

# location = data['loc'].split(',')
# latitude = location[0]
# longitude = location[1]

# for id in fetch_id:
#     fetch_id = fetch_id.get("id")
# print(id)

# id = fetch_id(user_city, user_country, data)

# print(id)
# api_key = "76ebe261e81ed7b8bd0f4ff2aa488dc0"
# # url = f"http://api.openweathermap.org/data/2.5/forecast?id={id}&APPID={api_key}"
# url = f"http://api.openweathermap.org/data/2.5/forecast?id={id}&APPID={api_key}"
# # fetch_id = id.get("id")
# id = fetch_id(user_city, user_country, data)
# print(id)
# r = requests.get(url)
# # print(r.json())
# file_name = "citylist.py"

# file = open(file_name, "w")
# print(r.json(), file= file)
# print(r.json())

# def fetch_id(user_city, user_country, data):
#     city_id = ""

#     for city in data:
#         if city["name"] == user_city and city["country"] == user_country:
#             city_id = city["id"]
#             print(city["name"], city["country"], city["id"], "\n\n\n\n\n")
    
#     return city_id

'''CORRECTION'''
import citylist
import requests
import time
import datetime

cities = citylist.citylist

requested_city = input("Please enter city to check \n: ").lower()

for city in cities:
    if requested_city in city["name"].lower():
        print(city["name"], city["country"])

requested_country = input("Please enter country code \n: "). lower()

for city in cities:
    if requested_city in city["name"].lower() and requested_country.lower() == city["country"].lower():
        # print(city["name"], city["country"]) for country
        print(city["name"], city["id"])
        city_id = city["id"] # to get the state id online
        break

api_key = "76ebe261e81ed7b8bd0f4ff2aa488dc0"

response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?id={city_id}&APPID={api_key}")
# # to check the raw that with a specific location e.g lagos paste this online http://api.openweathermap.org/data/2.5/forecast?id={city_id(put the lagos id here)}&APPID={api_key (and your api here}
# # http://api.openweathermap.org/data/2.5/forecast?id=2332453&APPID=76ebe261e81ed7b8bd0f4ff2aa488dc0 (then copy all and paste it on json website to format it well)
data = response.json()
# print(data.keys())

for forecast in data["list"]:
    print(forecast["dt_txt"])
    print(forecast["main"]["temp"])
    # print(forecast["main"]["temp"]["sea_level"]["grnd_level"])
    print(forecast["weather"][0]["description"])
    print()

'''Assignment- from the top, get for the longitude, latitude, wind etc'''