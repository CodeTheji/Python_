import requests

url = "http://checklight.pythonanywhere.com/get_readings/1x0d001/30/"

response = requests.get(url)
data = response.json()

# print(data.keys())
# print(type(data["streets"]))

streets = data["streets"]

count = 0

days = {}
time = {}
for street in streets:
    # print(type(street))
    time = street.get("time")
    name = street.get("name")
    times = time [0 : 4]
    status = street.get("status")
    day = time[5:7]
    # print(time, status, day)
    # print(time[-9 : -4])
    on_time = (time[-9 : -4].replace(":", "."))
 
    # print("On time = ",on_time)




# # For days with no light
    if status == 1:
        on_time = (time[-9 : -4].replace(":", "."))

        if day not in days:
            days[day] = 0
        days[day] += 1
        # print(status,day, on_time)

    if name == 0.0:
        # for 
        name = street.get("name")
        times = time [0 : 4]
        off_time = (times[-9 : -4].replace(":", "."))
        # if day not in days:
        #     # off_time = (time[-9 : -4].replace(":", "."))
        #     days[day] = 0
        # days[day] += 1
        # print(status,day, off_time)

        # if status == 0:
        #     count.append(status)
        #     # print(time)
        
        # print(count)
        # # print(time)
        # print(name, day, status, on_time, off_time)
        print(off_time)