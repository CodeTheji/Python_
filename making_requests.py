# import requests

# url ="http://checklight.pythonanywhere.com/streets"

# response = requests.get(url)
# data = response.json()
# # print(data)
# print(data.keys())

# print(type(data["streets"]))

# streets = data["streets"]

# # for street in streets:

#     print(type(street))
#     print(street.keys())
#     print(street.get("name"), "-", street.get("last_no_light"), "-", street.get("lga"), "-", street.get("status"))
#     print(street.get("history").get("time_line"))
#     # print(street.get(("name")).center(20), "|", s

# status = {}  
# period = data[("period")]
# in_minute = period / 60
# for time_line in (street.get("history").get("time_line").get("in_minute")):
#     if status == 1:
#         print("light On")
#     else:
#         print("light Off")
''' My error was i didnt know how to call or get the code to bring the dictionary in the time_line into display'''
'''correction'''

# import requests

# url = "https://checklight.pythonanywhere.com/streets"
# response = requests.get(url)
# data = response.json()

# print(data.keys())
# print(type(data["streets"]))

# streets = data["streets"]

# for street in streets:
#     # print(type(street))
#     # print(street.key())
#     print("\n", street.get("name").center(20), "-", street.get("last_no_light").center(20), "-", street.get("lga").center(20))

#     print("\n\t----------------TIMELINES-------------------\n")
#     timelines = street.get("history").get("time_line")
#     print(type(timelines))
#     for timeline in timelines:
#         status = "Up Nepa" if timeline.get("status") == 1 else "Down Nepa"
#         period = round(timeline.get("period")/3600, 1)
#         time = timeline.get("time")
#         print("t", str(time).center(12), (str(period)+"hours").center(12), str(status).center(12), sep = "|")

''' TO PLOT IT ON A GRAPH, YOU HAVE TO IMPORT A FUNCTION CALLED matplotlib.pyplot '''

# import requests
# import matplotlib.pyplot as plt # that is you want to plot a graph, if you want to do in in a piechart it would be as pie or so...and below too would be plt.bar
# url = "https://checklight.pythonanywhere.com/streets"
# response = requests.get(url)
# data = response.json()

# print(data.keys())
# print(type(data["streets"]))

# streets = data["streets"]

# for street in streets:
#     # print(type(street))
#     # print(street.key())
#     # print("\n", street.get("name").center(20), "-", street.get("last_no_light").center(20), "-", street.get("lga").center(20))

#     # print("\n\t----------------TIMELINES-------------------\n")
#     timelines = street.get("history").get("time_line")
#     # print(type(timelines))
#     # for timeline in timelines:
#     #     status = "Up Nepa" if timeline.get("status") == 1 else "Down Nepa"
#     #     period = round(timeline.get("period")/3600, 1)
#     #     time = timeline.get("time")
#     #     print("t", str(time).center(12), (str(period)+"hours").center(12), str(status).center(12), sep = "|")
#     daily_supply = street.get("history").get("daily_supply")
#     print(daily_supply)

#     labels = daily_supply["labels"]
#     values = daily_supply["values"]

#     plt.bar(labels, values) #plt.pie or so for piechart
#     plt.title(street.get("name"))
#     plt.show()

# import requests
# url = "http://checklight.pythonanywhere.com/get_readings/1x0d001/5/"
# response = requests.get(url)
# data = response.json()

# print(data.keys())
# # print(type(data["street"]))

# streets = data["streets"]
# count = 0

# for street in streets:
#     time = street.get("time")
#     times = time [0 : 4]
#     status = street.get("status")

    # print(time, status)
   
#     if  status == 0:
#         print(time, status)
#         count += 1
# print(count)
'''class work (count all the zeros for each day)'''
# for street in streets:
#     status = street.get("status")
#     time = street.get("time")
#     # print(data.keys())
#     if time == "0":
#         count.append(time)
#         print(time)
# print(count)
# # time [0 : 4]
# # print(time)

'''correction'''
# import requests
# url = "https://checklight.pythonanywhere.com/get_readings/1x0d001/12/"
# # predictions/1x0d001/"

# response = requests.get(url)
# data = response.json()

# streets = data["streets"]

# days = {}
# for street in streets:
#     status = street["status"]
#     time = street["time"]
#     day = time[5:7] #5 we counted it e.g Dec. 11 so the first "1" is 5 second "1" is 6, but we would call the end 7 because we are counting from zero

#     if status == 0:
#         if day not in days:
#             days[day] = 0
#         days[day] += 1
#         #print(day, status)
# print(days)

'''counting for each day'''

# import requests
# for a in range(1,5)

# device_url = f"https://checklight.pythonanywhere.com/get_readings/1x0d00{a}/12/"

# for a in device:
# # predictions/1x0d001/"

# response = requests.get(device_url)
# data = response.json()

# streets = data["streets"]

# days = {}
# for street in streets:
#     status = street["status"]
#     time = street["time"]
#     day = time[5:7] #5 we counted it e.g Dec. 11 so the first "1" is 5 second "1" is 6, but we would call the end 7 because we are counting from zero

#     if status == 0:
#         if day not in days:
#             days[day] = 0
#         days[day] += 1
#         #print(day, status)
# print(a, device)
'''correction'''

import requests

devices = ["1x0d001", "1x0d002", "1x0d003", "1x0d004"]
all_devices = {}

for device in devices:

    url = f"https://checklight.pythonanywhere.com/get_readings/{device}/12/"
    # predictions for each device/"

    response = requests.get(url)
    data = response.json()

    streets = data["streets"]

    days = {}
    for street in streets:
        status = street["status"]
        time = street["time"]
        day = time[5:7] #5 we counted it e.g Dec. 11 so the first "1" is 5 second "1" is 6, but we would call the end 7 because we are counting from zero

        if status == 0:
            if day not in days:
                days[day] = 0
            days[day] += 1
            #print(day, status)
    