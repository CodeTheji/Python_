
import random

import pymysql.cursors

connection = pymysql.connect(host= "localhost",
                            user="root",
                            password="",
                            db="my_db",
                            charset="utf8mb4",
                            cursorclass=pymysql.cursors.DictCursor)


# names = open("lists_of_random_names.txt", "r").read()
# data = names.read()

# # print(data)

# s_data = data.strip().replace(" ", "").replace(")", "").lower().split()

# fname = 
# lname =
# email = 
# age = random.randint(10,50)
# salary = random.randint(10000,50000)

# print(s_data)


''' CORRECTIONS'''

with connection.cursor() as cs:
    #Create a new record

    filename = "C:/Users/MY PC/Desktop/Prog_python/lists_of_random_names.txt"
    raw_data = open(filename, "r").read()

    for name in raw_data.splitlines():
        #print(name) #PRINT LINE WHICH CONTAINGS INDIVIDUAL FULL NAME

        frame, lname = name.split()

       
        domain = random.choice(["@gmail.com", "@yahoo.com", "@live.com"])
        user_mail = frame[:3] + lname[:3] + domain
        user_age = random.randint(10,50)
        salary = random.randint(10000, 50000)

        print(f"Firstname - {frame}, Lastname - {lname}, Age - {user_age}, Email - {user_mail}, Salary - {salary}")

        sql_cmd = f'INSERT into person(frame, lname, age, address, email, salary) values ("{frame}", "{lname}", {user_age}, "abuja", "{user_mail}", "{salary}")' #Note the f'INSERT, the approstophy is a single quote


        cs.execute(sql_cmd)
        connection.commit()



''' 22/01/2020'''



with connection.cursor() as cs:
    # create a new record
    
    sql_cmd = f'create table product (id int(3) AUTO_INCREMENT PRIMARY KEY NO NULL, namr varchar(30), price int(5), weight float(5,5))'

    cs.execute(sql_cmd)
    connection.commit()