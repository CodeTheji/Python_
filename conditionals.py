# # age = int(input("Hello what is your age : "))
# # dob = input("Please enter you DOB as dd-mm-yyyy : ")

# # # year = int(dob[6::])
# # print(dob.split("-"))
# # year = int(dob.split("-")[2])
# # age = 2019 - year
# # print(age)

# # if age >= 21:

# #     print("Here's your drink ")
# # elif age < 21:

# #     print("Sorry too young.")

# x = 0
# y = 5

# # if x < y:                           
# #     print('yes')
# #     print("y is", bool(y), ", x is", bool(x), "and the if statement got", x < y)


# # if y < x:                           
# #     print('yes')
# #     print("y is", bool(y), ", x is", bool(x), "and the if statement got", y < x)

# # else:
# #     print('Failed')
# #     print("y is", bool(y), ", x is", bool(x), "and the if statement got", y < x)

# # if x:                               
# #     print('yes')
# #     print("y is", bool(y), ", x is", bool(x), "and the if statement got", bool(x))
# # else:
# #     print('Failed')
# #     print("y is", bool(y), ", x is", bool(x), "and the if statement got", bool(x))

# # if y:                               
# #     print('yes')



# # if x or y:                          
# #     print('yes')


# # if x and y:                         
# #     print('yes')
# # else:
# #     print("no")

# # test = "shayo"
# # name = 'Feyishayo'
# # letter = "s"

# # if test in name:               
# #     print('yes', name, "contains ", test)
# # elif letter in name:
# #     print(name, "does not contain ", test, ". But contains", letter)
# # else:
# #     print('No', name, "does not contain ", test, "and does not contain the letter", letter)

# # response =  int(input("Please enter a number to test : "))

# # if response%2 == 0:
# #     print(f"{response} is an even number ")
# # else :
# #     print(f"{response} is not an even number ")


# # headache_response = input("Do you have a headache .? respond y/n : ")

# # if headache_response == "y": #check for headache

# #     fever_response = input("Do you have a fever .? respond y/n : ")

# #     if fever_response == "y": #check for fever

# #         vomit_response = input("Have you vomitted .? respond y/n : ")

# #         if vomit_response == "y": #check for vomit
# # #  
# #             print("you have Typhoid, please see a doctor")
        
# #         elif vomit_response == "n": #check for no vomit
# #             print("you have Malaria, please see a doctor")

# #     elif fever_response == "n": #check for no fever:
# #         print("You are probably just stressed out try to rest. ")
        

# # elif  headache_response == "n": #check for no headache
# #     print("You are probably okay or maybe see a medical practitioner")

# # if <expr>: <statement_1>; <statement_2>; ...; <statement_n>
# # x = 20
# # if x == 20 : print(x), print("next statement"), print("happy syntax") #Probably unreadable syntax too many single line statements
# # if x == 20 : break #Acceptable

# #TENARY OPERATOR

# """<expr1> if <conditional_expr> else <expr2>"""

# # user_input = input("please enter your name in caps")

# # name = user_input if user_input.isupper() else "input was not upper case"

# # print(name )

# # score = int(input("please enter your score : "))
# # grade = "Good" if score > 60 else "Bad"
# # print(grade)

# # score = int(input("please enter your students score"))

# # status = "Qualified" if score >= 60 else "Not qualified"
# # print(status)

# # student_is_qualified = True if score >= 60 else False

# # if student_is_qualified :
# #     print("\nSending mail to student\n")
# #     print("Coontent: You have qualified for admission please visit our page to continue your registration")


# # if 'quux' in ['foo', 'bar', 'baz']: 
# #     print('yes')

# # boys_age = 18
# # boys_gratitude = "merci"
# # list_of_gratitudes = ["ese", "thanks", "daalu", "nagode", "merci"]

# # if boys_age >= 21:
# #     winner = "pdp"
# #     print("You are of the right age")
# #     payment = boys_age *100
# #     print("Take ", str(payment) + "USD")
# #     print("Please spend the money wisely")

# #     if boys_gratitude in list_of_gratitudes:
# #         print("\nYou are a good shyd")
    
# #     else:
# #         print("Else on inner 'If'")
# # else:
# #     winner = "apc"
# #     print("Else on outer 'If'")

# # print(winner)

# # name = 'Chidi'
# # if name == 'Tolu':
# #     print('Hello Tolu')
# # elif name == 'Tayo':
# #     print('Hello Tayo')
# # elif name == 'Chidi':
# #     print('Hello Chidi')
# # elif name == 'Shade':
# #     print('Hello Shade')
# # else:
# #     print("I don't know who you are!")

# # name = input("Please enter your name")
# # names = {
# #      'Chidi': 'Hello Chidi',
# #      'Tayo': 'Hello Tayo',
# #      'Tolu': 'Hello Tolu',
# #      'Femi': 'Hello Femi'
# #  }

# # print(names.get(name, "I don't know who you are!"))

# # def foo():
# #     print('hello i am a function')

# # population = 100000
# # votes = 225000
# # election_was_violent = True

# # if  votes <= population: print('This was a fair election') #;print("this is awesome")

# # debugging = True  # Set to True to turn debugging on.

 

# # if debugging: print('About to call function foo()'); foo()

# # if population > votes :
# #     print("Fair election")
# # elif election_was_violent :
# #     print("Bad election")

# # age = 30

# # print("you are an", "Adult " if age > 18 else "adolescent")

# # it_is_raining = False

# # print("We are going ", "to stay home " if it_is_raining else "to the beach")

# # if True:
# #     pass
# # else:
# #     pass
# # csv_file = open("clinic_log.csv", "a")
# # name = input("Hello what is your name : ")
# # print(name, sep = ",", file = csv_file)

# # headache_response = input("Do you have a headache .? respond y/n : ")
# # response = True if headache_response == "y" else False
# # print("", "Headache", response, sep = ",", file = csv_file)

# # if headache_response == "y": #check for headache

# #     fever_response = input("Do you have a fever .? respond y/n : ")
# #     response = True if fever_response == "y" else False
# #     print("", "Fever", response, sep = ",", file = csv_file)

# #     if fever_response == "y": #check for fever

# #         vomit_response = input("Have you vomitted .? respond y/n : ")
# #         response = True if vomit_response == "y" else False
# #         print("", "Vomitting", response, sep = ",", file = csv_file)

# #         if vomit_response == "y": #check for vomit
# # #  
# #             print("you have Typhoid, please see a doctor")
        
# #         elif vomit_response == "n": #check for no vomit
# #             print("you have Malaria, please see a doctor")

# #     elif fever_response == "n": #check for no fever:
# #         print("You are probably just stressed out try to rest. ")
        

# # elif  headache_response == "n": #check for no headache
# #     print("You are probably okay or maybe see a medical practitioner")

# # csv_file.close()

# # log = open("clinic_log.csv", "r")

# # data = log.read()


# # names = ("bade", "bolu", "shayo", "monday")

# # for name in names:
# #     print(f"{name.capitalize().ljust(10)} => {len(name)}")

# # for i in range(1, 21, 3):
# #     print(i, i**i)


# class Animal:
#     def talk(self):
#         print("I have something to say!")
    
#     def walk(self):
#         print("Hey! I am walking here!")

    #UNBOUND METHOD
#     @staticmethod
#     def clothes():
#         print("I have nice clothes!")

# animal = Animal()
# animal.talk()
# animal.clothes()

# print(animal)
# Animal.clothes()


# class Account:

#     # class attribute
#     type = "parent" 

#     def __init__(self, acct_no_param, name_param):
#         #instance attributes
#         self.acct_no = acct_no_param
#         self.name = name_param
#         self.bal = 0 
    
#     def deposit(self, amount):
#         self.bal += amount
#         print(f"Successfully added {amount} to {self.name} balance, \nNew balance = {self.bal}")

#     def withdraw(self, amount):
#         self.bal -= amount
#         print(f"Successfully withdrew {amount} to {self.name} balance, \nNew balance = {self.bal}")

# my_acct = Account(acct_no_param = "301229409", name_param = "Bruno")
# my_acct2 = Account(acct_no_param = "3012294300", name_param = "Salami")

# print(my_acct.name)
# print(my_acct.acct_no)
# print(my_acct.type)
# (my_acct.deposit(5000))

# print(my_acct2.name)
# print(my_acct2.acct_no)
# print(my_acct2.type)
# (my_acct2.deposit(12000))

# class Current_Acct(Account):
#     type = "current"

#     def __init__(self, acct_no_param, name_param, dollar_bal = 0 ):
#         Account.__init__(self, acct_no_param, name_param)
#         self.dollar_bal = dollar_bal

    
# # class Savings_Acct(Account):
# #     type = "savings"

# my_curr_acct = Current_Acct(acct_no_param = "301229409", name_param = "John")
# # my_savings_acct = Savings_Acct(acct_no_param = "301229409", name_param = "Sule")
# print(my_curr_acct.name)
# print(my_curr_acct.type)
# print(my_curr_acct.dollar_bal)
# my_curr_acct.dollar_bal = 450000
# # print(my_savings_acct.name)
# # print(my_savings_acct.type)

# class Current_Acct(Account):
#     type = "current"

#     def __init__(self, acct_no_param, name_param, dollar_bal = 0 ):
#         Account.__init__(self, acct_no_param, name_param)
#         self.__dollar_bal = dollar_bal #ENCAPSULATED ATTRIBUTE


#     def get_dollar_bal(self):
#         print(self.__dollar_bal)
#         return(self.__dollar_bal)
    
#     @staticmethod
#     def get_dollar_bal_():
#         print(self.__dollar_bal)
#         return(self.__dollar_bal)

    
# # class Savings_Acct(Account):
# #     type = "savings"

# my_curr_acct = Current_Acct(acct_no_param = "301229409", name_param = "John")
# # my_savings_acct = Savings_Acct(acct_no_param = "301229409", name_param = "Sule")
# print(my_curr_acct.name)
# print(my_curr_acct.type)
# print(my_curr_acct.get_dollar_bal())
# # my_curr_acct.__dollar_bal = 450000

# print(my_curr_acct.get_dollar_bal())
# print(type(my_curr_acct.get_dollar_bal_))
# print(type(my_curr_acct.get_dollar_bal))
# # print(my_savings_acct.name)
# # print(my_savings_acct.type)

import datetime, random, json

def generate_acct_no():
    no = [str(random.randint(0,9)) for i in range(10)]
    acct_no = "".join(no)

    return acct_no
        
class Customer:

    def __init__(self, name = "none", username = str(datetime.datetime.now()), password = "11111111"):
        self.name = name
        self.username = username
        self.password = password
        self.creation_date = str(datetime.datetime.now())

    def details(self):
        print(self.name)
        print(self.username)
        print(self.creation_date)
        return "this is my empty return"


class Account:

    def __init__(self, type, customer, account_no = generate_acct_no()):
        self.customer = customer
        self.__balance = 0
        self.creation_date = str(datetime.datetime.now())
        self.type = type
        self.account_no = account_no 

    def get_balance(self):
        print(self.__balance)
    
    def details(self):
        print(self.customer.name)
        print(self.customer.username)
        print(self.customer.creation_date)
        print(self.account_no)

    def save(self):
        Storage.store(type = self.type, account_no = self.account_no, acct_creation_date = self.creation_date, name = self.customer.name, username = self.customer.username, password = self.customer.password, cust_creation_date = self.customer.creation_date )



class Storage():

    @staticmethod
    def store(**kwargs):
        
        data = json.dumps(kwargs)
        file = open("acct_db", "w")
        file.write(data)

cust_1 = Customer("Ahmed", "boss_of_ife", "qwerty")
acct1 = Account("savings", cust_1)

acct1.details()
acct1.save()

# cust_2 = Customer("Tolu", "boss_of_Bosses", "@@@@@@")
# acct2 = Account("savings", cust_2)
# details_2 = [acct2]

# with open ("acct_db", "w") as f:
#     for data in details_2:
#         file.write(data)
#         file.write("\n")

# acct2.details()
# acct2.save()
# # cust_2 = Customer("Tolu", "boss_of_Bosses", "@@@@@@")
# # acct2 = Account("savings", cust_2)

''' CORRECTION TO ADD NEW CUSTOMER'''

class Storage():

    @staticmethod
    def store(**kwargs):
        old_date = Storage.fetch_old()
        old_date[kwargs["username"]] = kwargs

        data = json.dumps(kwargs)
        file = open("acct_db", "w")
        file.write(data)
    @staticmethod
    def fetch_old():

        try:

            file = open("acct_db.json", "r")
            return json.loads(file.read())

        except:

            return{}


cust_1 = Customer("Shade", "boss_of_ife", "00qwerty")
acct1 = Account("savings", cust_1)

acct1.details()
acct1.save()
