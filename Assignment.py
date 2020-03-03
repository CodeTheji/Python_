#TAKING BIO DATA THAT WOULD INDICATE IF YOU WERE BORN ON A LEAP YEAR
# name = input ("Please enter your name:")
# age = input ("Please enter age:")
# current_year = 2019
# if(current_year%4==0 and current_year%100!=0 or current_year%400==0):
#     comment =f"Hello {name}, you are {age} years old, born on {current_year - int(age)}, which means you were born on a leap year"
# else:
#     comment =f"Hello {name}, you are {age} years old, born on {current_year - int(age)}, which means you were not born on a leap year"
# print(comment)

# question1 = input("Are you okay?: ")
# question2 = input("Do you have pains?: ")
# question3 = input("Did you sleep well?: ")
# question4 = input("Have you done hardwork?: ")
# question5 = input("Do you have fever?: ")
# question6 = input("Are you vommitting?: ")

# if question1=="true":
#     print(question2)
# elif question2=="true":
#     print("go get a life")
# elif question3=="true":
#         print("go get a life")

# else:
#     print("False is executed")

# # Now for the quadratic formalar or almighty formular
# a = int(input("enter a value for a:"))
# b = int(input("enter a value for b:"))
# c = int(input("enter a value for c:"))
# d = ((b**2) - (4*a*c))**0.5
# #d = -b + (((b**2) - (4*a*c))**0.5)/2*a (my formal formula)
# x1 = (-b + d)/(2*a)
# x2 = (-b - d)/(2*a)
# print(x1 , x2)

# a = ["foo", "bar", "baz"]
# for i in a:
#     print(i)
# print("x".center(4),   "|"     "x-x_bar".center(7), "x_bar2**2".center(7))
# print("____", "|", "_______", "|", "_______")
# mean = sum(range(10)) / len(range(10))
# print(mean)
# for i in range(10):
#     x_bar = i - mean
#     x_bar2 = x_bar **2
#     print(f"{i}".center(4), "|", f"{x_bar}".center(7), "|", f"{x_bar2}".center(7), sep="")
#     # print(i,  "|".center(7), i - mean)

# import collections
# # list of elements to calculate mode
# num_list = [21, 13, 19, 13,19,13]

# # Print the list
# print(num_list)

# # calculate the frequency of each item
# data = collections.Counter(num_list)
# data_list = dict(data)

# # Print the items with frequency
# print(data_list)

# # Find the highest frequency
# max_value = max(list(data.values()))
# mode_val = [num for num, freq in data_list.items() if freq == max_value]
# if len(mode_val) == len(num_list):
#    print("No mode in the list")
# else:
#    print("The Mode of the list is : " + ', '.join(map(str, mode_val)))

# name = input
# biodata = {"name":"inyang", "age":27, "gender":"male"}
# print(biodata["name"], biodata["age"], biodata["gender"],)

# print(biodata["name"].upper(), "|", int(biodata["age"]), "|", biodata["gender"].upper())

# '''to add to a dictionary list'''
# print(biodata.keys()) #to check the keys
# biodata["finance"] = "Investment proceeds"
# print(biodata)

# {  
#    "firstname" : "Ayodeji",
#       "age": 19,
#       "hobbies" : ["coding", "surfing the web", "meeting new people"],
#       "siblings" : [
#          {
#                   "firstname" : "shola"
#                   "age" : 17,
#          },
#          {
#                   "Firstname" : "damilare",
#                   "age": 13
#          }
#       ]

# }

# import json
# {
#     "firstName": "Jane",
#     "lastName": "Doe",
#     "hobbies": ["running", "sky diving", "singing"],
#     "age": 35,
#     "children": [
#         {
#             "firstName": "Alice",
#             "age": 6
#         },
#         {
#             "firstName": "Bob",
#             "age": 8
#         }
#     ]
# }

# with open("datajson_file", "w") as write_file:
#    json.dump(data, write_file)

# word = input("Enter a random word: ")
# lengthOfWords = len(word)
# print("The length of the word", word, "is", lengthOfWords)

''' QUIZ 3.1'''

# import math

# r = eval(input("Enter the length from the center to a vertex: "))
# s = int(2 * r * (math.sin (math.pi / 5)))
# area = ((3* math.sqrt(3)) / 2) * math.pow(s, 2)
# print("The area of the pentagon is", area)

''' *3.2 Geometry: great circle distance'''

# import math

# x1, x2 = eval(input("Enter point 1 (latitude and longitude) in degrees: "))
# y1, y2 = eval(input("Enter point 2 (latitude and longitude) in degrees: "))

# radius = math.radians(6371.01)

# distance = radius * math.acos(math.sin(x1)) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2)

# print("The distance between the two points is ", distance) # seems something is wrong here

# ''' *3.4 Geometry: area of a pentagon) '''
# import math
# s = eval(input("Enter the side of the pentagon: "))
# area = 5 * s**2 / (4 * math.tan(math.pi/5))

# print("The area of the pentagon is", area)
# import math

# ''' *3.5 Geometry: area of a regular polygon) '''
# n = eval(input("Enter the number of sides: "))
# s = eval(input("Enter the sides: "))
# area = (n * s**2) / (4 * math.tan(math.pi/n))
# print("The area of the polygon is", area)


'''  *3.6 Find the character of an ASCII code '''

# v = int(input("Enter an ASCII code: "))
# v1 = chr(v)
# print(v1)

''' *3.9 Financial Application: Payroll '''
# name = input("Enter employees's name: ")
# noOfHoursWorked = eval(input("Enter number of hours worked in a week: "))
# hourlyPayRate = eval(input("Enter hourly pay rate: "))
# fedTax = eval(input("Enter federal tax withholding rate: ")) / 100
# stateTax = eval(input("Enter state tax withholding rate: ")) / 100
# grossPay = noOfHoursWorked * hourlyPayRate
# # deductions:
# fWH = grossPay * fedTax
# sWH = grossPay * stateTax
# tD = fWH + sWH
# print("Federal Withholdings is", fWH)
# print("State Withholdings is", sWH)
# print("Total Deductions: ", tD)
# print("Net Pay: ", format((grossPay - tD), ".2f"))


# Python Program to Reverse a Number using While loop    
         
# n=int(input("Enter number: "))
# rev=0
# while(n>0):
#     rem=n%10
#     rev=rev*10+rem
#     n=n//10
# print("Reverse of the number:",rev)
'''OR'''

# number = eval(input("Enter any number: "))
# reverse = 0
# while(number > 0):
#     reminder = number % 10
#     reverse = reverse * 10 + reminder
#     number = number // 10
# print("Reverse pf the number:", reverse)

y = ["r", "v", "b","f"]
print(y.sort)
