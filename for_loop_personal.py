
# fruits = ("apple", "pawpaw", "mango", "fish")
# for x in fruits:
#     print(x)

# for x in "banana":
#     print(x)
#     if x == "n":
#         break

# '''To break when it reach a particular word or letter'''

# fruits = ("apple", "pawpaw", "mango", "fish")
# for x in fruits:
#     if x == "mango":
#         break
#     print(x)

# '''To skip a particular word and go to the next or letter'''

# fruits = ("apple", "pawpaw", "mango", "fish")
# for x in fruits:
#     if x == "mango":
#         continue
#     print(x)

# ''' The range function of for loop'''
# for x in range(2, 6):
#     print(x)

# ''' The range function for it to move by the increment of 3'''
# for x in range(2, 50, 3):
#     print(x)

''' The range function for it to move by the increment of 3'''
# fruits = ("apple", "pawpaw", "mango", "fish", "dish", "lash", "bash", "cash")
# for x in fruits[::2]: --> [start:stop:step]

#     print(x)

'''Else in loop'''

# for x in range(6):
#     print(x)
# else:
#     print("It is finished")

'''Nested Loops - It is a loop inside of loop'''

# adj = ["red", "big", "sharp","tasty"]
# fruits = ("apple", "pawpaw", "mango", "fish")
# for x in adj:
#     for y in fruits:
#         print(x,y)

# for x in [1,2,3]:
#     pass

import csv

files = open("country.csv", "r")

for x in files:
    print(x)