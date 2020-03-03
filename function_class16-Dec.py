# def dumb_func(x,y):
#     return x * y

# result = dumb_func(2,6)
# print(result)

# '''Division'''

# def dumb_func_div(x,y):
#     return x / y
# result = dumb_func_div(2,6)
# print(result)


# '''Addition'''

# def dumb_func(x,y):
#     return x + y
# result = dumb_func(2,6)
# print(result)

# def dumb_func(x,y):
    
#     print(x)
#     print(y)
#     return x + y #return is the function that shows the output it must be added to a def functions to print out the ouput
# result = dumb_func(2,6)
# print(result)

# """
# This is a simple addition function it expects 2

# print(dumb_func_add.__doc__)

# def pythagoras(a,b):
#     c = ((a**2) + (b**2))**0.5

#     return(c)
# print(pythagoras(3,5))

# def simple_interest(p,r,t):
#     # a = (p(1+(rt))/100
#     a = ((p*r*t) / 100)
#     return(a)
# print(simple_interest(1000,10,5))


# def factorial_iter(n):
#     num = 1
#     while n >= 1:
#         num = num * n
#         n = n - 1
#     return num
# print(factorial_iter(5))

''''def factorial_iter(n):
    a = {}
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num
    if a in n:
        print(str(a)
        
print(factorial_iter(5))


correction

def factorial_iter(n):
    num = 1
    max_val = n + 1
    
    while n >= 1:
        num = num * n
        if n in range(2, max_val):
            print(str(n), "*", end="")
        else:
            print(str(n), "=", end=" ")
        n = n -1
    return num
print(factorial_inter(10))'''

""" Segun style"""
# empty_list = []
# def factorial_iter(n):
#     num = 1

#     while n >= 1:
#         num = num * n
#         empty_list.append(str(n))
#         n = n - 1
#     print(" x ".join(empty_list), "=", num)
    
#     return num
# print(factorial_iter(10))

######## FIBONACCI SERIES######

# a = []
# # fn = (f1 - 1) + (f2 - 2) 
# # f0 = 1, f1
# def fibonacci(n):
#     if a < 0:
#         print("invalid")
#     elif a == 1:
#         return 0
#     elif a ==2:
#         return 1
# print(fibonacci(7))

# '''correction1'''
# def fib_seq(n):
#     seq = []

#     for i in range(n):
#         if len(seq) < 2:
#             seq.append(i)
#         else:
#             new_sequence = seq[i - 1] + seq[i - 2]
#             seq.append(new_sequence)
#     print(seq)

# fib_seq(22)

# '''correction2'''

# def fib_seq_v2(first_num, second_num, quantity):
#     seq = [first_num, second_num]

#     for i in range(2, quantity):

#             new_sequence = seq[i - 1] + seq[i - 2]
#             seq.append(new_sequence)
#     print(seq)

# fib_seq_v2(1,1,22)

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


'''Assignment-Write a function that generates 2 lists of random numbers of size(n)'''
# import random

# list_1 = []
# list_2 = []

# def gen_rand_list(n):
#     for a in range(n):
#         num_1 = random.randint(1,7)
#         num_2 = random.randint(9,16)
#         list_1.append(num_1)
#         list_2.append(num_2)

# gen_rand_list(5)
# print(f"Lists :  {list_1} and {list_2}")

'''CORRECTION 1'''

# import random

# def gen_rand_nums(num_of_lists, rand_range, sample_size):

#     rand_nums = []
#     for _ in range(num_of_lists): # _ is used in python just to pass something if you dont want to define or assign it
#         rand_list = [random.randint(0, rand_range) for _ in range(sample_size)]
#         rand_nums.append(rand_list)

#     return rand_nums

# rand_nums = gen_rand_nums(3,7,20)

# print(rand_nums)

'''CORRECTION 1B'''

# def mean_n_variance(sample):
#     mean = sum(sample)/ len(sample)

#     x_xbar = [i - mean for i in sample]

#     variance = (sum(x_xbar)**2) / (len(sample)-1)

#     return{"variance": variance, "mean": mean}

# def solve(num_of_lists, rand_range, sample_size):
    
#     random_nums = gen_rand_nums(num_of_lists, rand_range, sample_size):

#     for sample in random_nums:
#         variance_val = means_n_variance(sample)
#         print(variance_val)

# solve(3,10,20)

'''CORRECTION 1B - METHOD 2'''

import random

num_of_lists = 3
rand_range = 10
sample_size = 20

def gen_rand_nums():
    global num_of_lists
    global rand_range
    global sample_size

    rand_nums = []
    for _ in range(num_of_lists):
        rand_list = [random.randint(0, rand_range) for _ in range(sample_size)]
        rand_nums.append(rand_list)

    return rand_nums


def mean_n_variance(sample):

    mean = sum(sample) / len(sample)
    x_xbar = [i - mean for i in sample]
    variance = (sum(x_xbar)**2) / (len(sample)-1)

    return {"variance": variance, "mean": mean}


def solve():

    random_nums = gen_rand_nums()

    for sample in random_nums:
        variance_val = mean_n_variance(sample)
        print(variance_val)

solve()