a = [2]
# a.append(3)
# a.append(a.append(5))
# print(a)

# radius = 20
# area = radius ** 2 * (22/7)
# print("The value for area is :", area)
# miles = 100
# kilometers = miles * 1.609
# print("The value of Kilometer is :", kilometers)

# radius = eval(input("Enter a value for radius:"))
# area = radius * radius * 3.14159

# print("The area of the circle of radius", radius, "is", area)

# num1, num2, num3, num4, num5 = eval(input("Enter five numbers seperated by comma: "))
# n = num1, num2, num3, num4, num5
# sum = num1 + num2 + num3 + num4 + num5
# no = len(n)
# average = sum / no
# print("The sum, average of", num1, num2, num3, num4, num5, "is", sum, "and", average, "respectively")

# import time
# currentTime = time.time()
# totalSeconds = int(currentTime)
# currentSecond = totalSeconds % 60
# totalMinutes = totalSeconds // 60
# currentMinute = totalMinutes % 60
# totalHours = totalMinutes // 60
# currentHour = totalHours % 24
# print("Current time is " " ", currentHour, ":", currentMinute, ":", currentSecond, "GMT")
# print(currentTime, ",", totalSeconds, ",", currentSecond, ",", totalMinutes)

# loanAmount = eval(input("Enter loan amount: "))
# annualInterestRate = eval(input("Enter interest rate: "))
# monthlyInterestRate = (annualInterestRate / 100) / 12
# numberOfYears = eval(input("Enter number of years: "))
# monthlyPayment = (loanAmount * monthlyInterestRate) / (1 - (1/(1 + monthlyInterestRate)**(numberOfYears*12)))
# totalPayment = monthlyPayment * numberOfYears * 12

# print("The monthly payment is", int(monthlyPayment * 100) / 100)
# print("The total payment is", int(totalPayment * 100)/ 100)

# noOfCandies = eval(input("Enter the number of candies you want to share equally: "))
# equallyShared = noOfCandies // 3
# remainingCandies = noOfCandies % 3

# print("Each friends will take", equallyShared, "Each, while", remainingCandies, "will be crushed")

# ''' SOLVED QUESTIONS FROM THE MATERIALS'''

# celsius = eval(input("Enter the degree of celsius in figue: "))
# fahrenheit = (9/5) * celsius + 32
# print(celsius, "Celsius is", fahrenheit, "Fahrenheit")

# radius, length = eval(input("Enter the radius and length(height) of the cylinder and seperate it by comma: "))
# area = 2 * 3.14 * radius ** 2
# volume = 3.14 * radius ** 2 * length
# print("The area and volume of the cylinder is ", area, ",", volume, "respectively")

# feet = eval(input("Enter the value for feet: "))
# meter = feet * 0.305
# print(feet, "feet is", meter, "meters")

# subtotal, gratuityRate = eval(input("Enter the subtotal and a gratuity rate seperate by comma: "))
# gratuity = (gratuityRate / 100) * subtotal
# total = round((subtotal + gratuity) ,2)

# print("The gratuity is", gratuity, "and the total is", total)

# num = int(input("Enter a four digit number: "))
# x = num // 1000
# x1 = (num - x*1000) // 100
# x2 = (num - x*1000 - x1*100) // 10
# x3 = num - x * 1000 - x1*100 -x2 * 10
# print("The sum of digits in the number is", x + x1 + x2 +)

''' import time
# currentTime = time.time()
# totalSeconds = int(currentTime)
# currentSecond = totalSeconds % 60
# totalMinutes = totalSeconds // 60
# currentMinute = totalMinutes % 60
# totalHours = totalMinutes // 60
# currentHour = totalHours % 24
# print("Current time is " " ", currentHour, ":", currentMinute, ":", currentSecond, "GMT")
# print(currentTime, ",", totalSeconds, ",", currentSecond, ",", totalMinutes)
'''
#  * 2.7 Quiz
# import time
# currentTime = time.time()
# totalSeconds = int(currentTime)

# totalMinutes = totalSeconds // 60
# totalHours = totalMinutes // 60
# aDayMins = 1440
# minsPerYear = aDayMins * 365

# minutes = eval(input("Enter the number of minutes: "))
# print(minutes, "minutes is approximately", int(minutes // 525600), "years,", int((minutes % 525600) // 1440), "days,", totalHours, "Hours and", totalMinutes, "Minutes")

# *2.8 Quiz

# water = eval(input("Enter the amount of water in kilograms: "))
# initialTemperature = eval(input("Enter the initial temperature: "))
# finalTemperature = eval(input("Enter the final temperature: "))

# '''# formular is Q = M * (finalTemperature - initialTemparature) * 4184
# where M is the weight of water in kilograms, temperatures are in degrees Celsius, and energy Q is measured in joules.'''

# energy = water * (finalTemperature - initialTemperature) * 4184

# print("The energy needed is", energy)

# * 2.10 Quiz
# speed, acceleration = eval(input("Enter the value of speed and acceleration and seperate it by comma: "))
# length = (speed**2) / (2 * acceleration)
# print("The minimum runaway length for this airplane is", round((length), 3), "meters")

# *2.11 Quiz


# finalAccountValue = eval(input("Enter final account value: "))
# interestRate = eval(input("Enter annual interest rate in percent: "))
# numberOfYears = eval(input("Enter number of years: "))



# monthlyInterestRate = interestRate / 12
# numberOfMonths = numberOfYears * 12
# initialDepositAmount = finalAccountValue / ((1 + monthlyInterestRate) ** numberOfMonths)

# print("Initial deposit value is", initialDepositAmount)

''' FUNCTIONS, STRINGS AND OBJECTS '''
# a = 5.4
# b = 5.5
# c = 4.5
# d = 3.6
# e = 3.5

# print(round())
# # print(pow(a, b)) 78 

import math

# print("exp(1.0) =", math.exp(1))

# x1, y1, x2, y2, x3, y3 = eval(input("Enter six cordinates of three points seperated by commas: "))
# a = math.sqrt((x2-x3) * (x2-x3) + (y2-y3) * (y2-y3))
# b = math.sqrt((x1-x3) * (x1-x3) + (y1-y3) * (y2 - y3))
# c = math.sqrt((x1-x2) * (x1-x2) + (y1-y2) * (y1 -y2))

# A = math.degrees(math.acos((a*a - b*b - c*c) / (-2*b*c)))
# B = math.degrees(math.acos((b*b - a*a - c*c) / (-2*a*c)))
# C = math.degrees(math.acos((c*c - b*b - a*a) / (-2*a*b)))

# print("The three angles are", round(A * 100) / 100.0, round(B * 100) / 100.0, round(C * 100) / 100.0)
# import math
# degrees = eval(input("Enter value to be converted to radians:"))
# x = math.degrees(degrees)
# print(x)

# import turtle
# turtle.write("\u6B22\u8FCE\u03b1\u03b2\u03b3")
# turtle.done()

'''print multiple statement on a straight line'''
# print("AAA", end = " ")
# print("BBB", end = "")
# print("CCC", end = "***")
# print("DDD", end = "***")
# print("EEE", end = "     ***")
# print(math.pi)

# e.g
# radius = 3
# print("The area is", radius * radius * math.pi, end = " ")
# # print("and the perimeter is", 2 * radius, end = "      --      ")
# print("and the perimeter is", 2 * radius)

''' The string concatenation operator '+' '''
# message = "Welcome" + "to" + "Python"
# print(message)
# For the += Augmented assigment
# x = "You look nice in there"
# x += " and you are as simple as abc"
# print(x)
''' Reading strings from the console'''
# s1 = input("Enter a string: ")
# s2 = input("Enter a string: ")
# s3 = input("Enter a string: ")

# print("s1 is " + s1)
# print("s2 is " + s2)
# print("s3 is " + s3)
"""Quiz"""
# a = ord("1")
# b = ord("A")
# c = ord("B")
# d = ord("a")
# e = ord("b")

# a = chr(40)
# b = chr(59)
# c = chr(79)
# d = chr(85)
# e = chr(90)

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# x = input("Enter a character: ")
# ch = chr(ord(x) + 3)
# print(ch)
# print(ord("A"))
# print(ord("x"))
# print(chr(120))
# print(ord("D"))

# x = input("Enter a character: ")
# y = input("Enter a character: ")
# print(ord(y) - ord(x))

'''Case Study Quiz Listing 3.4'''
# amount = eval(input("Enter the amount as a decimal number such as 21.56: "))
# convertToCent = int(amount * 100)
# noOfDollars = convertToCent // 100
# remainingCents = convertToCent % 100
# noOfQuarterCents = remainingCents // 25
# remainingOfQuarterCents = remainingCents % 25
# noOfDimes = remainingCents // 10
# remainingOfDimes = remainingCents % 10
# noOfNickels = remainingCents // 5
# pennies = remainingCents % 5

# print("Your amount", amount, "consist of \n",
#     "\t", noOfDollars, "dollars \n",
#     "\t", noOfQuarterCents, "quaters \n",
#     "\t", noOfDimes, "dimes \n",
#     "\t", noOfNickels, "nickels \n,",
#     "\t", pennies, "pennies")

'''Correction from the book NB; here the remainingAmount is still the same, i.e constant regardless of what you are dividing it by''' 

# # Receive the amount
# amount = eval(input("Enter an amount, for example, 11.56: "))

# # Convert the amount to cents
# remainingAmount = int(amount * 100)

# # Find the number of one dollars
# noOfOneDollars = remainingAmount // 100
# remainingAmount = remainingAmount % 100

# # Find the number of qarters in the remaining amount
# noOfQuarters = remainingAmount // 25
# remainingAmount = remainingAmount % 25

# # # Find the number of dimes in the remaining amount
# noOfDimes = remainingAmount // 10
# remainingAmount = remainingAmount % 10

# # Find the number of nickels in the remaining amount
# noOfNickels = remainingAmount // 5
# remainingAmount = remainingAmount % 5

# # Find the number of pennies in the remaining amount
# noOfPennies = remainingAmount

# print("Your amount", amount, "consist of \n",
#     "\t", noOfOneDollars, "dollars \n",
#     "\t", noOfQuarters, "quaters \n",
#     "\t", noOfDimes, "dimes \n",
#     "\t", noOfNickels, "nickels \n",
#     "\t", noOfPennies, "pennies")


# name = input("Enter your name in quote/string: ").strip()


# print(name)

'''FORMATING STRING AND NUMBERS (".2f" means to convert to 2 decimal place for instant 16.409, normally if you round it
to two decimal place, it will give you 16.4, but with the formatter, you get 16.40)'''

# amount = 3430589
# interestRate = 0.0013
# interestAmount = amount * interestRate
# print("The interest amount is ", interestAmount)
# print("The interest amount is ", round(interestAmount, 2))
# print("The interest amount is ", format(interestAmount, "2f"))
# print("The interest amount is ", format(interestAmount, ".2f"))
# print("The interest amount is ", format(interestAmount, ".1f"))
# print("The interest amount is ", format(interestAmount, ".3f"))

'''FORMATTING FLOAT-POINT NUMBERS'''

# print(format(57.467657, "10.2f"))
# print(format(12345678.923, "10.2f"))
# print(format(57.4, "10.2f"))
# print(format(57, "10.2f"))

# print(format(57.467657, "10.2f"))


# '''FORMATTING IN SCIENTIFIC NOTATION ( i.e when you change the f to e i.e convertion code)'''
# print(format(57.467657, "10.2e"))
# print(format(0.0033923, "10.2e"))
# print(format(57.4, "10.2e"))
# print(format(57, "10.2e"))

# '''FORMATTING AS A PERCENTAGE ( when you use the convertion code % to format a number as a percentage)'''
# print(format(0.53457, "10.2%"))
# print(format(0.0033923, "10.2%"))
# print(format(7.4, "10.2%"))
# print(format(57, "10.2%"))

# ''' JUSTIFYING FORMAT '''

# print(format(57.467657, "10.2f"))
# print(format(57.467657, "<10.2f"))
# print(format(57.467657, "<.2f"))
# print(format(57.467657, ".2f"))

''' JUSTIFYING STRINGS'''

# print(format("Welcome to python", "20s"))
# print(format("Welcome to python", "<20s"))
# print(format("Welcome to python", ">20s"))

'''Quiz solved 3.19'''
# print(format(57.467657, "9.3f"))
# print(format(12345678.923, "9.1f"))
# print(format(57.4, ".2f"))
# print(format(57.4, "10.2f"))


# print(format(57.467657, "9.3e"))
# print(format(12345678.923, "9.1e"))
# print(format(57.4, ".2e"))
# print(format(57.4, "10.2e"))

# print(format("Programming is fun", "25s"))
# print(format("Programming is fun", "<25s"))
# print(format("Programming is fun", ">25s"))

''' DRAWING SHAPES '''
# import turtle
# turtle.pensize(3)
# turtle.penup()
# turtle.goto(-150, -50)
# v = turtle.circle(5, 40, 4)

# print(v)


''' ### CHAPTER 4 SELECTIONS; BOOLEANS '''

# t = True
# z = False
# print(int(t))
# print(int(z))
# print(str(t))
# print(str(z))

''' Generating random numbers '''

# import random

# number1 = random.randint(0, 9)
# number2 = random.randint(0, 9)

# answer = eval(input("What is " + str(number1) + " + " + str(number2) + " ?  "))

# print(number1, " + ", number2, "=", answer, "is", number1 + number2 == answer)

# import random
# x = random.randint(0,9)
# y = random.randint(0,9)
# x1 =random.randrange(0,9)
# y1 = random.randrange(0,9)
# print(x,y,x1,y1)
import random

# num_1 = random.randint(0,9)
# num_2 = random.randint(0,9)
# # answer = num_1 + num_2
# answer = eval(input("What is  " + str(num_1) + " +  " + str(num_2) + " ?" + " ="))
# if str(num_1) + "+" + str(num_2) != answer:
#     print("incorrect")
# print(num_1, " + ", num_2, "=", answer, "is", num_1 + num_2 == answer )

# dice_1 = random.randint(1,6)
# dice_2 = random.randint(1,6)
# print("You have thrown", dice_1, ",", dice_2)
# if dice_1 == 6 and dice_2 == 6:
#     print("You won!!")
# else:
#     print("ooops, try again")

# print("Okay")

''' PAGE 96, Lisiting 4.2 to calculate the multiple of a number using the if statement'''
# number = eval(input("Enter any number: "))

# if number % 5 == 0:
#     print("HiFive!!")

# if number % 2 == 0:
#     print("HiEven")

''' SOLVED CHECK POINT 4.7'''
# y = random.randrange(-2, 5)
# print("y is", y)
# if y >= 0:
#     print("1 = x")
# if y < 0:
#     print("y has a negetive value")

''' SOLVED CHECK POINT 4.8'''

# score = random.randint(80, 1200)

# rate = 0.03 * score
# increased = score + rate

# if score > 90:
#     print("Your pay which is ", score, "has been increased by 3%, which is now approximately ", int(increased))

# if score < 90:
#     print("You pay is still the same bro!, because it is", score)

''' LISTING 4.3 GUESS BIRTHDAY'''

# day = 0 # birth day to be determined

# # prompt the user to answer the first question
# question_1 = "Is your birthday in Set1?\n" + \
#     "   1   3   5   7\n" + \
#     "   9   11  13  15\n" + \
#     "   17  19  21  15\n" + \
#     "   25  27  29  31\n" + \
#     "\nEnter 0 for No and 1 for Yes: "

# answer = eval(input(question_1))

# if answer == 1:
#     day+=1

# question_2 = "Is your birthday in Set2?\n" + \
#     "   2   3   6   7\n" + \
#     "   10  11  14  15\n" + \
#     "   18  19  22  23\n" + \
#     "   26  27  30  31\n" + \
#     "\nEnter 0 for No and 1 for Yes: "

# answer = eval(input(question_2))

# if answer == 1:
#     day+=2

# question_3 = "Is your birthday in Set3?\n" + \
#     "   4   5   6   7\n" + \
#     "   12  13  14  15\n" + \
#     "   20  21  22  23\n" + \
#     "   28  29  30  31\n" + \
#     "\nEnter 0 for No and 1 for Yes: "

# answer = eval(input(question_3))

# if answer == 1:
#     day+=4

# question_4 = "Is your birthday in Set4?\n" + \
#     "   8   9   10  11\n" + \
#     "   12  13  14  15\n" + \
#     "   24  25  26  27\n" + \
#     "   28  29  30  31\n" + \
#     "\nEnter 0 for No and 1 for Yes: "

# answer = eval(input(question_4))

# if answer == 1:
#     day+=8

# question_5 = "Is your birthday in Set5?\n" + \
#     "   16  17  18  19\n" + \
#     "   20  21  22  23\n" + \
#     "   24  25  26  27\n" + \
#     "   28  29  30  31\n" + \
#     "\nEnter 0 for No and 1 for Yes: "

# answer = eval(input(question_5))

# if answer == 1:
#     day+=16


# print("\nYour birthday is" + str(day) + "!")

# //
# import random
# ''' swaping no done'''

# num_1 = random.randint(0,9)
# num_2 = random.randint(0,9)

# print("number1 is: ", num_1)
# print("number2 is: ", num_2)

# if num_1 < num_2:
#     num_1, num_2 = num_2, num_1

# print("num_1 is: ", num_1)
# print("num_2 is: ", num_2)

# answer = eval(input("What is " + str(num_1) + "-" + str(num_2) + "  ? "))

# if num_1 - num_2 == answer:
#     print("Correct Answer!!")

# else:
#     print("You are wrong!\n", num_1, "-", num_2, "is", num_1 - num_2, ".")

# print(answer)


# ''' Question 4.9 Page 101'''
# import random
# pay = random.randint(0, 1000)

# if pay > 90:
#     print("You pay which is", pay, " has increased by 3% !!, Now it is: ", int(pay*1.03))

# else:
#     print("You pay which is", pay, " has increased by 1%!!, Now it is: ", int(pay*1.01))

# num = eval(input("Enter a value for number: "))

# if number % 2 == 0:
#     print(number, "is even")

# # print(number, "is odd")


# if num % 2 == 0:
#     print(num, "is even")

# else:
#     print(num, "is odd")


# ''' Nested If and Multi-Way if - elif-else statements '''
# import random

# score = random.randint(0, 100)




# if score >= 90:
#     grade = "A"
# elif score >= 70:
#     grade = "C"
# elif score >= 50:
#     grade = "E"
# elif score >= 60:
#     grade = "D"
# elif score >= 80:
#     grade = "B"
# else:
#     grade = "F"

# print(score, grade)

# ''' Mine version '''
# if score >= 70:
#     print(score, " is A")
# elif score >= 60 < 70:
#     print(score, " is B")
# elif score >= 50 < 60:
#     print(score, " is C")
# elif score >= 40 < 50:
#     print(score, " is D")
# elif score == 40:
#     print(score, " is E")

# else:
#     print(score, " is F")



# ''' Zodiac Sign solved Listing 4.5 page 104'''
# year = eval(input("Enter your year: "))
# zodiac_year = year % 12

# if zodiac_year == 0:
#     print(zodiac_year, " Na monkey o")

# elif zodiac_year == 1:
#     print(zodiac_year, " Na roster sha")

# elif zodiac_year == 2:
#     print(zodiac_year, " Chai na dog o")

# elif zodiac_year == 3:
#     print(zodiac_year, " Chai na pig o")

# elif zodiac_year == 4:
#     print(zodiac_year, " na ewoooo na rat o")

# elif zodiac_year == 5:
#     print(zodiac_year,  "na ox sha")

# elif zodiac_year == 6:
#     print(zodiac_year, " hmmmm chinko, Tiger")

# elif zodiac_year == 7:
#     print(zodiac_year, " rabbit ni bobo yen sha")

# elif zodiac_year == 8:
#     print(zodiac_year, " dragon, eyan drakulaa o")

# elif zodiac_year == 9:
#     print(zodiac_year, " Snake!!!!!!!!!")

# elif zodiac_year == 10:
#     print(zodiac_year, " Horse ")

# else:
#     print(zodiac_year, " hmmmmm... meek as a Sheep")


# import random

# score = random.randint(0,100)

# if score >= 60.0:
#     grade = "D"

# elif score >= 70:
#     grade = "C"

# elif score >= 80:
#     grade = "B"

# elif score >= 90:
#     grade = "A"

# else:
#     grade = "F"

# print(score, grade)

# oxford = {
# "noun": "Name of person animal place or thing",
# "pronoun": "Used instead of a noun",
# "verb": "Action word",
# "adjective": "describes a noun"
# }

# print(oxford['adjective'])

# _class = {
#     "chidi":["sleeping", "eating", "travelling"],
#     "tolu":["coding", "reading complex stuff", "writing advanced code"],
#     "femi":["speaking big grammar", "lightening class mood", "teaching complex math",  "analysing grammar"],
#     "omotayo":[ "drinking sweet stuff", "chowing biscuit", "pressing phone"],
#     "Mr tayo": ["Selling insurance", "Giving updates", "Encyclopedia"],
#     "shade" : ["accounting", "coming late", "shalaye'ing"],
#     "attah": ["being cool", "being calm", "being collected", "being awesome", "eating affang"]
# }

# for item in _class["Mr tayo"]:
#     print(item[0 : 3])

# _class = {
#     "chidi":{
#         "surname": "Igbo",
#         "hobbies":["sleeping", "eating", "travelling"],
#         "phone": "0804465862"
#         },
#     "tolu":{
#         "surname": "Igbo",
#         "hobbies":["sleeping", "eating", "travelling"],
#         "phone": "0804465862"
#         },
#     "femi":["speaking big grammar", "lightening class mood", "teaching complex math",  "analysing grammar"],
#     "omotayo":[ "drinking sweet stuff", "chowing biscuit", "pressing phone"],
#     "Mr tayo": ["Selling insurance", "Giving updates", "Encyclopedia"],
#     "shade" : ["accounting", "coming late", "shalaye'ing"],
#     "attah": ["being cool", "being calm", "being collected", "being awesome", "eating affang"]
# }

# print(_class["chidi"]["hobbies"][-1])
# # creating dictionaries VIA TUPLES

# # print(_class["chidi"])
# # print((_class["chidi"]))
# # print(type(_class["chidi"]))

# # y = ''.join(_class["attah"])
# y = ''.join(map(str, "attah"))
# z = int(y)
# print(z)

