''' arg == argument uses single *
    kwarg == keyword arguments uses double **
We have variable arguments and positional arguments'''

'''Variable Arg'''

# def my_func(*names):
#     print(names)
#     # print(sum(args)) * to the variable or name ...what it does is to unwrap the content in the list then add it to the new package

data = ["atha", "deji", "tunji"]

my_func(*data)

# '''variable kwarg'''
def my_func(**names):
    print(names)
    print(sum(args))

# my_func(atha=28, john=30, seun = 17, dupe = {"x : 23"})

# '''POSITIONAL'''
# def bio(name, age, gender):
#     print("name :", name, " age: ", age, " gender : ", gender)

#     #  bio ("atha", "male", 28) #POSITIONAL ARG
#     #  bio(name = "atha", gender = "male", age = 28) # KEYWORD ARGUMENT



############### RECURSION #############
# def printer(n):
#     print(n)

#     if n == 0:
#         print("Base case was met !!!")
#         return
#     n = n-1
    
#     printer (n)
#     # return printer(n)
# printer(3)

# import requests

# data = {"username": "dtekluva", "data": [{"name":"tolu", "age":30, "class":5}, {"name":"tolu", "age":30, "class":5},{"name":"tolu", "age":30, "class":5}]}

# url = "http://localhost:8000/quick_test"
# response = requests.post(url, data)

# print(response.json())

# radius = eval(input("Enter a value for radius:"))
# area = radius * radius * 3.14159

# print("The area of the circle of radius", radius, "is", area)

# number1 = eval(input("Enter the first number:"))
# number2 = eval(input("Enter the second number:"))
# number3 = eval(input("Enter the third number:"))
# number4 = eval(input("Enter the fourth number"))

# sum_of_numbers = (number1 + number2 + number3 + number4)
# average = sum_of_numbers / 4

# print("The sum of the four number is", sum_of_numbers, "while the average is",average)
# count = 100
# count = count + 1
# print(count)

# number1, number2, number3 = eval(input("Enter three numbers seperated by a comma: "))
# sum = number1 + number2 + number3
# average = sum / 3
# print("The sum and average of", number1, ",", number2, ",", number3, "is", sum, "and", average, "respectively")

