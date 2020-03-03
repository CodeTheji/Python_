# class Animal:
#     def talk(self):
#         print("I have something to say!")
#     def walk(self):
#         print("Hey! I am walking here!")
#     def clothes(self):
#         print("I have nice clothes!")

# animal = Animal()
# animal.talk()
# animal.clothes()

'''Example from the class'''

class Account:
    # class attribute
    type = "parent"

    def __init__(self, acct_no_parameter, name_parameter):
        # intance attributes
        self.acct_no = acct_no_parameter
        self.name = name_parameter
        self.bal = 0

    def deposit(self, amount):
        self.bal += amount
        print(f"Successfully added {amount} to {self.name} balance, \nNew balance = {self.bal}")

    # For withdrawal
    def withdrawal(self, amount):
        self.bal -= amount
        print(f"Successfully withdrew {amount} to {self.name} balance, \nNew balance = {self.bal}")

# my_acct = Account(acct_no_parameter = "0021213431", name_parameter = "Bruno")
# my_acct2 = Account(acct_no_parameter = "011212123", name_parameter = "Salami")

# print(my_acct.name)
# print(my_acct.acct_no)
# print(my_acct.type)
# (my_acct.deposit(5000))

# # to withdrawl
# (my_acct.withdrawal(4000))


# print(my_acct2.name)
# print(my_acct2.acct_no)
# print(my_acct2.type)
# (my_acct2.deposit(12000))

# # to withdrawl
# (my_acct2.withdrawal(3000))



# To give it another class attibute for the Account i.e current and savings

'''Adding an instant attribute to the child, that is adding another attribute to the current_account(child) from the main Account(parent)'''


class Current_Acct(Account):
    type = "current"

    def __init__(self, acct_no_parameter, name_parameter, dollar_bal = 0):
        Account.__init__(self, acct_no_parameter, name_parameter) #inheritance from the parent to the child and now adding a new features to the child (polymophism)
        self.dollar_bal = dollar_bal


    # class Saving_Acct(Account):
    # type = "Savings"

my_curr_acct = Current_Acct(acct_no_parameter = "0021213431", name_parameter = "Bruno")
# my_acct2 = Saving_Acct(acct_no_parameter = "011212123", name_parameter = "Salami")

print(my_curr_acct.name)
print(my_curr_acct.type)
print(my_curr_acct.dollar_bal)


class Savings_Acct(Account):
    type = "savings"

    def __init__(self, acct_no_parameter, name_parameter, interest_rate = 0.05):
        Account.__init__(self, acct_no_parameter, name_parameter)
        self.interest_rate = interest_rate #ENCAPSULATION IS DONE WITH "__"

my_savings_acct = Savings_Acct(acct_no_parameter = "011212123", name_parameter = "Salami")

print(my_savings_acct.name)
print(my_savings_acct.type)
print(my_savings_acct.interest_rate)


'''ENCAPSULATION'''

class Current_Acct(Account):
    type = "current"

    
    def __init__(self, acct_no_parameter, name_parameter, dollar_bal = 0):
        Account.__init__(self, acct_no_parameter, name_parameter) 
        self.__dollar_bal = dollar_bal #ENCAPSULATED ATTRIBUTE done with "__"

    def get_dollar_bal():
        print(self.__dollar_bar)
        return(self.__dollar_bar)

    @staticmethod
    def get_dollar_bal(self):
        print(self.__dollar_bar)
        return(self.__dollar_bar)

print(my_curr_acct.name)
print(my_curr_acct.type)
print(my_curr_acct.get_dollar_bal())

print(my_curr_acct.get_dollar_bal())
print(type(my_curr_acct.get_dollar_bal_))
print(type(my_curr_acct.get_dollar_bal))