# # 1*1
# # print(1*1)
# # mynumber = 20.234
# # rounded_num = round(mynumber, 2)
# # print (rounded_num)
# # num = 22
# # dem = 7
# # pi = num / dem
# # print(pi)
# # rounded_num = round(pi, 3)
# # print(rounded_num)
# # name = "Elson John"
# # phone = 8023245312 * 6
# # print(phone)
# # name = "Elson"
# # surname = "John"
# # fullname = name +" " + surname
# # print(fullname)
# # day = "20"
# # month ="May"
# # year = "2019"
# # print(day +" " + month+", " + year)
# # pi = 22/7
# # statement = "pi is" + str(pi)
# # print(statement)
# # statement = "pi is " + str(round(pi, 2))
# # print(statement)
# # print(round(pi, 2))
# akara = input ("Please how many akara do you want?")
# akamu = input ("Please how many akamu do you want?")
# print(akara, akamu)
# akara_statement = "You bought" + akara + "akamu"
# akamu_statement = "You bought" + akamu + "akara"
# print(akara_statement)
# print(akamu_statement)
# akara_price = 20
# akamu_price = 50
# bill = "Your bill is : " + str(int(akara) * akara_price + int(akamu) * akamu_price) # note, str was added and all placed within a bracket, so it could all be in string
# print(bill)

# TAKING IN BOI DATA

# name = input ("Please enter your name:")
# age = input ("Please enter age:")
# birth_year = 2019
# if(birth_year%4==0 and birth_year%100!=0 or birth_year%400==0):
#     comment =f"Hello {name}, you are {age} years old, you were born in {birth_year - int(age)}, which means you were born on a leap year"
# else:
#     comment =f"hello {name}, you are {age}, you were born in {birth_year - int(age)}, which means you were not born on a leap year"
# print(comment)

# Week 2
# name = input ("Please enter your name:")
# print(name [0], name [2], name [4])
# print(name [-1])
# print(name [0:5])

#
# name = input ("Please enter your name :")
# length = input ("What is the length of name :")
# half_length = int(int(length)/2)
# print(name[half_length:])

# #Now for first two, middle two and the last two
# name = input ("Please enter your name :")
# length = input ("What is the length of name: ")
# half_length = int(int(length)/2)
# first_two_words = (name [0:2])
# last_two_words = (name [-1:-2])
# print(first_two_words)
# print(last_two_words)
# ##Corrections
# name = input ("Please enter your name :")
# length = input ("What is the length of name: ")
# half_length = int(int(length)/2)
# two_chars_up = half_length + 2 #The +2 means lets say the number of characters is 8, and you are looking for the half_length +2 ,i.e 8/2 =4 but in python would be 3, 3character plus 2 character ahead
# print(word[half_length : two_chars_up])
# ##Correction B
# first_two = word[0:2]
# last_two = words[-2:]
# mid_point = word[half_length : two_chars_up]
# statement = f"{first_two}{mid_point}{last_two}"
# ##Correction C
# first_two = word[0:2]
# last_two = words[-2:]
# mid_point = word[half_length : two_chars_up]
# statement = first_two + mid_point + last_two
# print(statement)

# Slice
# word = "Sweet mum"
# slice = word[ : : 2]
# slice = word[-5::-1]
# slice = word[-5:: 2]
# print(slice)

# New topic : Operators
# mod = 6%3
# print(mod)
# subtopic increment Operators
# x=20
# x=x+1
# print (x)
# now for the increment formula
# then x+=1, so
# x+=1
# print(x)
# print (x)


# C^2=a^2+b^2
# c= (a^2+b^2)^0.5
# a = int(input("enter a numeric value for a:"))

# b = input("enter a numeric value for b:")
# b = int(b)

# c = ((a**2) + (b**2))**0.5
# print(c)

# Now for the quadratic formalar or almighty formular
# a = int(input("enter a value for a:"))
# b = int(input("enter a value for b:"))
# c = int(input("enter a value for c:"))
# d = ((b**2) - (4*a*c))**0.5
# #d = -b + (((b**2) - (4*a*c))**0.5)/2*a (my formal formula)
# x1 = (-b + d)/(2*a)
# x2 = (-b - d)/(2*a)
# print(x1 , x2)

# Comparison operators
# >
# <
# >=
# <=
# age = int(input("Please enter age: "))
# can_drink = age >= 20
# can_pay_tax = age >= 18
# can_take_pension = age > 60
# can_retire = age == 40
# statement = f"Can drink : {can_drink}\nCan Pay Tax : {can_pay_tax}\nCan take pension : {can_take_pension}\nCan now retire : {can_retire}"
# print(statement)


# would update monday class


# RANGE FUNCTION
# my_range = range(20)
# print(my_range)
# print(type(my_range))
# print(list(my_range))

# my_range = range(20, 60) for within numbers
# print(my_range)
# print(type(my_range))
# print(list(my_range))

# my_range = range(20, 60, 2) #to skip 2 numbers within that range
# print(my_range)
# print(type(my_range))
# print(list(my_range))

# now to reverse the range list
# my_range = range(20, 60)
# print(my_range)
# print(type(my_range))
# print(list(my_range))
# print(list(reversed(my_range)))

# # SORTED
# x = [1,2,5,3,10,1,0,4]
# print(sorted(x))
# # to sort in decending order
# print(sorted(x, reverse = True))

# x = list ("Abimbolami")
# print(sorted (x))
# try and to the reverse of this
# Answer #print(sorted(x, reverse = True))

# my_list = ["seed", "bee", "a", "checked", "print"]
# print(sorted(my_list))
# # how to sort based on how large/length of the letters
# print(sorted(my_list, key=len))
# print(sorted(my_list, key=len, reverse=True))

# DICT (DICTIONARY)
# my_dict = dict(a=20, b=30, c=100)
# print(my_dict)

# SET
# x = "abimbola"
# print(set(x))

# # MAP (iterable, function)
# nums = [1,2,3,4,5]
# mapped = map(lambda x : x*2, nums)
# print(list(mapped))

# # To add Mr at the front of these names
# names = ["ade", "john", "shola"]
# mapped = map(lambda x: 'Mr '+ x, names)
# print(list(mapped))

# # READ ON "ANY"
# word = "sharp"
# print(any(word) in "aei")

# LOWER
# word = "Axe"
# print(word.lower())
# ##FROM THE MONDAY CLASS CODE
# word = input("please write a word:")
# convert_to_lower_case = word.lower()
# response = "a" in word or "e" in word or "i" in word or "o" in word or "u" in word
# print (f"{word} contains vowels : {response}")
# print(response)

# REPLACE
# word = input("please enter any word that has pre: ")
# print(word)
# replace_word = word.replace("pre","post")
# print(replace_word)
# name = ["gem", "hem", "blem", "chem"]
# mapped = map(lambda x: x.replace("e", "a"), name)
# print(list(mapped))

# MAP IS A FUNCTION FOR WORKING INSIDE A LIST
# mapping for mean deviation, (using mean deviation formular)
# a = [1,3,1,2,2,4]
# mean = (sum(a) / len(a))
# print(mean)
# mapped = (list(map(lambda x: (x-(mean))**2, a)))
# print(mapped)
# sum_of_square = sum(mapped)
# ##mapz = list(map (lambda x: (sum_of_square) / (len(a) - 1), a))
# # print(mapz)
# print(sum_of_square/((len(a)) - 1))

# # JOIN
# x = ["Hi", "People"]
# print("".join(x))

# filename = "Brown_skin_girl.txt"
# mode = "r"

# data = open(filename, mode)
# lyrics = data.read()
# print(lyrics.find ('Lupita'))

# FINDING "brown from the lyrics"
# filename = "Brown_skin_girl.txt"
# mode = "r"

# data = open(filename, mode)
# lyrics = data.read()
# print(lyrics.count ('brown'))

# #FINDING "brown from the lyrics"
# filename = "Brown_skin_girl.txt"
# mode = "r"

# data = open(filename, mode)
# lyrics = data.read()
# print(lyrics.count ('brown'))

# ASSIGNMENT
# import random
# for x in range(6):
#     print(random.randint(1,6) (1,6)))

# def roll_dice():
#     "print two numbers between 1 and 6 (side of the dice)"
#     print(random.randint(1, 6))

# import random
# def monopoly():
# x = random.randrange(1,6)
# y = random.randrange(1,6)
# if x = 6, y = 6

# import random

# x = random.randrange(1, 6)
# y = random.randrange(1, 6)
# print(x,y)

# if x == 6 and y == 6:
#     comment = f"You won!"
#     print(comment)
# else:
#     comment = f"opps, try again!"
#     print(comment)



# correction
# if(x==6) and (y ==6):
#     print()

# ASSIGNMENT 2
# male_names = ["Bola", "Segun", "John"]
# f_names = ["Shola", "Bisi"]
# mapped_m = map(lambda x: 'Mr '+ x, male_names)
# mapped_f = map(lambda x:'Mrs '+ x, f_names)
# print(list(mapped_m))
# print(list(mapped_f))
# CORRECTION
# names = [("Bola", "f"), ("Segun", "m"), ("John", "m"), ("Shola","f"), ("Bisi", "f")]
# raw_saluted_names = map(lambda x: "Mr " + x[0] if x[1] == "m" else "Mrs " + x[0], names) #Tenary operators
# saluted_names = list(raw_saluted_names)
# print(saluted_names)

# WEEK5
# IF/ELIF/ELSE

# if "foo" in ["foo", "bar", "baz"]:
#     print("Outer condition is true")

#     if 10 > 20:
#         print("Inner condition 1")

#     print("Between inner conditions")

#     if 10 < 20:
#         print("Inner condition 2")
    
#     print("End of outer condition")
# print("After outer condition")

# Lets test
# behaviour = "Good" or "Bad"
# age = 60
# if behaviour == "Good" and age < 18:
#     print("You get a toy")
# else:
#     print("No toy")

#     if behaviour == "Good" and age > 18:
#         print("You get a car")
#     else:
#         print("No car for you bro!")
        
#     if behaviour == "Bad" and age > 18:
#         print("Left alone")
#     else:
#         print("O.Y.O lo wa")

#COORECTION
# behaviour = "bad" #you can change "bad" to "Good"
# age = 17

# if behaviour == "good":
#     if age > 18:
#         print("Here's your car..!")
#     else:
#         print("Here's your Toy..!")
# else:
#     print("Sorry you're on your own")

# ELIF
# if "a" in "bar":
#     print("foo")
# elif 1/0:
#     print("This wont happen")
# elif var:
#     print("This wont run either")

#TENARY OPERATOR
# mark = int(input("What is your score:"))
# print("You", "passed" if mark > 50 else "failed")

# x = 3
# s = ("foo" if (x == 1) else("bar" if (x == 2)else("baz" if(x == 3)else ("qux" if (x == 4)else "quux")))) #note: the calculations is from the back
# print(s)

# # Class assessment
# question = "Are you okay?:"
# if question == "yes":
#     print(True)
# else:
#     print(False)


#27/11/2019
# a = ["foo", "bar", "baz"]
# for i in a:
#     print(i)
# print("x", "x-x_bar")
# print("__", "|", "___")
# mean = sum(range(5)) / len(range(5))
# print(mean)
# for i in range(5):
#     print(i,  "|", i - mean)

# justifying the text/numerical to the center
# print("x".center(4), "|", "x_xbar".center(7), "|", "(x_xbar)^2".center(11), sep = "") # sep = "" is use for removing the space
# print("____".center(4), "|", "_______".center(7), "|", "___________".center(11), sep = "")

# n = 5
# mean = sum(range(n)) / len(range(n))

# for i in range(n):
#     print(f"{i}".center(4), "|", f"{i - mean}".center(7), "|", f"{(i - mean)**2}".center(11), sep ="")

# word = input("Enter your name: ")
# vowels = ["a", "e", "i", "o", "u"]
# total_vowels = 0
# for letter in word:
#     if letter in vowels:
#         print(letter)
#         total_vowels = total_vowels + 1
# print(f"Total vowels : {total_vowels}")

# OR DO IT THIS WAY
# word = input("Enter your name: ")
# vowels = ["a", "e", "i", "o", "u"]
# total_vowels = 0
# for vowels in vowels:
#     if vowels in word:
#         print(vowels)
#         count = word.count(vowels)
#         total_vowels = total_vowels + count
    
# print(f"Total vowels : {total_vowels}")


# # to count the number of vowels
# word = input("Enter your name: ")
# vowels = ["a", "e", "i", "o", "u"]
# total_vowels = 0
# print(f"Vowel | Count")
# print(f"_____ |______")
# for vowel in vowels:
#     if vowel in word:
#         count = word.count(vowel)
#         total_vowels = total_vowels + count
#         print(f"{vowel.center(6)}|{str(count).center(6)}", sep = "")

# print(f"Total vowels : {total_vowels}")

# #BREAK
# word = input("Enter a word: ")

# for i in word:
#     print(i)
#     if i == "?":
#         break

# filename = "unique.csv"
# raw_data = open(filename, "r")
# data = raw_data.readlines()
# current_line = 0

# for line in data:
#     current_line += 1
#     print(line)
#     print()

#     if "Jamie" in line:
#         print("Found jamie at line: ", current_line)
#         break

# score = [20, 30, 70, 10,67,50]
# import random
# for score in scores:

#     c_assess = random.randint(10, 30)
#     f_score = score + c_assess

#     marked_up = int(f_score * 1.2)
#     if f_score > 70:
#         print(score, c_assess, f_score, f_score)
#         continue

#     print(score, c_assess, f_score, marked_up, "marked_up")

# '''12/2/2019'''
# '''while loops'''
# n = 5
# while n > 0:
#     n -= 1
#     print(n)
# '''for loops'''
# n = 5
# for i in range(n):
#     n = n-1
#     print(n)

# '''for loops used for joining'''
# x = "boy, toys, junk"
# y = "mum, girl, luck"
# n = 0
# word_length = len(x)
# while n < word_length:
#     print(x[n], y[n])
#     n += 1 '''without putting this code, it would keep running'''

# while True:
#     name = input("what is you name: ")
#     if name == "emeka":
#         x = 0
#         for i in name:
#             print(i)

'''DATA STRUCTURE
4/12/2019
Topic: Append'''

# mylist = [1,2,3,4,5,6]
# print(mylist)

# name = "Ayodeji"
# my_second_list = list(name)
# print(my_second_list)

# products = "Shoes, bags, rings, shirts"
# my_third_list = (products).split(",")
# print(my_third_list)

# # my_third_list.append("shorts")
# # print(my_third_list)

# while True:
#     new_prop =input("Enter a new prop: ")
#     my_third_list.append(new_prop)
#     print(my_third_list)

# '''Topic: Remove/add'''
# attempts = 5
# while True:
#     action = input("What would you like to do : ")

#     if action == "add":
#         #to add to list
#         new_prop = input("Enter a new prop: ")
#         my_third_list.append(new_prop)
#         print(my_third_list)
    
#     elif action == "rem":
#         #to remove from list
#         new_prop = input("Enter a prop tp remove: ")
#         my_third_list.remove(new_prop)
#         print(my_third_list)

#     attempts -=1

#     if attempts == 0:
#         print("You have ran out of attempts...!!!")
#         break

'''Topic: Remove/add
TO MAKE IT COUNT THE NO OF ITEMS IN THE LIST'''
# attempts = 5
# while True:
#     already_counted = []

    
#     for item in my_third_list:
#         if item not in already_counted:
#             occurences = my_third_list.count(item)
#             already_counted.append(item)
#             print(item, occurences)

#     action = input("What would you like to do: ")

#     if action == "add":
#         #to add to list
#         new_prop = input("Enter a new prop: ")
#         my_third_list.append(new_prop)
#         print(my_third_list)
    
#     elif action == "rem":
#         #to remove from list
#         new_prop = input("Enter a prop tp remove: ")
#         my_third_list.remove(new_prop)
#         print(my_third_list)

#     attempts -=1

#     if attempts == 0:
#         print("You have ran out of attempts...!!!")

# attempts = 5
# import random
# random_no = []
# already_counted = []

# for i in range(20):
#     if i not in already_counted:
#         randomNumb = random.randint(1,20)
#         random_no.append(randomNumb)
#         # already_counted.append()
#         print(already_counted, randomNumb)
'''CORRECTION'''
# import random
# random_nums = []

# for i in range(20):
#     rand_num = random.randint(1,5) #that is 20 numbers but within 1 to 5
#     random_nums.append(rand_num)
# print(random_nums)

# already_counted = []

# for item in random_nums:
#     if item not in already_counted:
#         occurences = random_nums.count(item)
#         already_counted.append(item)
#         print(item, occurences)

'''LIST COMPREHENSION'''
# word ="Shayo"
# cap_word = [x.upper() for x in word]
# print(cap_word)

# q = [1,2,3,4,5,8,5]
# squared = [x**2 for x in q]
# print(squared)

'''09/12/2019 DICTIONARY'''
# name = input
# biodata = {"name":"inyang", "age":"27", "gender":"male"}
# print(biodata["name"], biodata["age"], biodata["gender"],)
# print(biodata["name"].upper(), "|", int(biodata["age"]), "|", biodata["gender"].upper(),)

# # '''to add to a dictionary list'''
# # print(biodata.keys()) to check the keys
# # biodata["Courses"] = "Finance",
# print(biodata.keys())
# biodata["hobby"] = "sciencing"
# print(biodata.keys())
# print(biodata)

# biodata["Course"] = " "
# print(biodata)
# # to change the age in biodata
# biodata["age"] = 30
# print(biodata)
# # to delete
# del biodata["age"] = 30
# print(biodata)

# new_dict = dict(
#             (
#                 (1, [2,3, "name"]),
#                 (2, 3),
#                 (4,1)
#             )
#             )
# print(new_dict)
# print(biodata.items())
# biodata.update({"comlexion": "dark"})
# print(biodata)
# third_dict = dict.fromkeys.([1,2,3], 0)
# print(third_dict)

'''' Adding two songslyrics'''

# perfect = open("perfect.txt", "r")
# risky = open("risky.txt", "r")
# data = perfect.readlines()
# lyrics_dict ={}
# line_num = 1

# for line in perfect:
#     print(line)
#     lyrics_dict[line_num] = line
#     line_num+=1

# print(lyrics_dict)

# while True:
#     requested_line = int(input("Please what line would you like to get: "))
#     print(lyrics_dict[requested_line])

# risky = "risky"
# perfect = "perfect"
# '''for the third one(mafo)'''
# mafo = "mafo"
# file = open(f"{risky}.txt", "r")

# data = file.readlines()
# lyrics_dict = {}
# line_num = 1
# lyrics_dict[risky] = {}

# for line in data:
#     lyrics_dict[risky][line_num] = line
#     line_num+=1
# file.close()


# '''For perfect lyrics now'''

# file = open(f"{perfect}.txt", "r")

# data = file.readlines()
# line_num = 1
# lyrics_dict[perfect] = {}

# for line in data:
#     lyrics_dict[perfect][line_num] = line
#     line_num+=1
# file.close()

# print(lyrics_dict.keys())

# '''For mafo lyrics'''

# file = open(f"{mafo}.txt", "r")

# data = file.readlines()
# line_num = 1
# lyrics_dict[mafo] = {}

# for line in data:
#     lyrics_dict[mafo][line_num] = line
#     line_num+=1
# file.close()

# print(lyrics_dict.keys())


# while True:
    
#     requested_song = (input("Please what song would you like to get: "))
#     print(lyrics_dict.keys())
#     requested_line = int(input("Please what line would you like to get: "))

#     print(lyrics_dict[requested_song][requested_line])