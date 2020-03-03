# import requests
# import json

# data_dict = {
#             "username"          :   "CodeTheji",
#             "firstname"         :   "Ayodeji",
#             "lastname"          :   "Oladeji",
#             "email"             :   "oladejiayodejiadefemi@gmail.com",
#             "phone"             :   "080842055566",
#             "details"           :   "Awesome!",
#             "password"          :   "Ayodeji01",
#         }

# json_data = json.dumps(data_dict)
# url = "http://univelcity.pythonanywhere.com/data/register/"

# req = requests.post(url, json_data)
# print(req.json())

# # {'response': 'success', 'message': 'Successfully added user -->  Ayodeji', 'data': {'access_token': ' I4WVBAP5HL4mRfNpJw_r-C3H8B-oHyP7NagdIznD9C9IGQIVUY_YWQ'}}

from collections import Counter

import os
import time

result = {}

path = "C:/Users/MY PC/Desktop/Prog_python/lyrics.zip"

with os.scandir("C:/Users/MY PC/Desktop/Prog_python/lyrics/") as entries:
        for entry in entries:
                print(entry)
                the_lyrics = open(entry, "r", errors = 'ignore').read().split()
                vowel_a = the_lyrics.count("a")
                vowel_e = the_lyrics.count("e")
                vowel_i = the_lyrics.count("i")
                vowel_o = the_lyrics.count("o")
                vowel_u = the_lyrics.count("u")
                title_artist = entry.name.split("--")
                print(title_artist)
                time.sleep(1)
                the_lyrics_content = open(entry, "r", errors = 'ignore').readline()
                most_frequent_checker = Counter(the_lyrics)
                result = {"most_occuring_word" : most_frequent_checker.most_common(1)[0][0], "Vowel_a" : vowel_a, "Vowel_e" : vowel_e, "Vowel_i" : vowel_i, "Vowel_o" : vowel_o, "Vowel_u" : vowel_u,}
                print(result)