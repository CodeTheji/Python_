import json
import pymysql.cursors
import requests
import datetime
import pandas
import json



## CREATE device table
device_codes = ["1x0d001", "1x0d002", "1x0d003", "1x0d004", "1x0d005"]



for device in device_codes:
    url = f"http://checklight.pythonanywhere.com/get_readings/{device}/1/" 
  
    response = requests.get(url)
    data = response.json()

    streets = data["streets"]

    for street in streets:
        device_id = street["device"]
        name = street["name"]
        id_id = street["id"]
        status = street["status"]
        timing = street["time"]

        file = open ("api_to_excel.csv", "a")
        print(device_id, name, id_id, status, timing, file=file, sep=",")

        

