# loan_amount = 300000
# rate = 0.05
# time = 2
# payments_per_year = 12
# principal = loan_amount

# def get_monthly_payment(principal, rate, time, no_payments_per_year):

#     monthly_pay = (principal*(rate/no_payments_per_year))/(1-(1+(rate/no_payments_per_year))**((no_payments_per_year*-1)*time))

#     payment_times = time * no_payments_per_year
#     # print(monthly_pay, payment_times)
#     return monthly_pay, payment_times

# repayment, no_payments = (get_monthly_payment(principal,rate, time, payments_per_year))

# print("Period".center(5),"AMOUNT".center(11),"INTEREST".center(11),"PRINCIPAL".center(11), "BALANCE".center(11),"\n ")
# loan_interest = 0
# for payment in range(no_payments + 1):


#     if payment == 0:
#         print(str(payment).center(5),"-".center(11), "-".center(11), "-".center(11), str(loan_amount).center(11))
#     else:
#         interest = loan_amount * (rate/payments_per_year)
#         loan_amount = loan_amount - (repayment - interest)
#         principal = (repayment - interest)
#         principal = round(principal,2)
#         loan_interest += interest
#         repayment, interest, loan_amount = round(repayment,2), round(interest,2), round(loan_amount,2)

#         print(str(payment).center(5),str(repayment).center(11), str(interest).center(11), str(principal).center(11), str(loan_amount).center(11))
# print(loan_interest)

# loan_amount = 300000
# rate = 0.05
# time = 2
# payments_per_year = 12
# principal = loan_amount

# repayment = (principal*(rate/payments_per_year))/(1-(1+(rate/payments_per_year))**((payments_per_year*-1)*time))

# no_payments = time * payments_per_year

# print("Period".center(5),"AMOUNT".center(11),"INTEREST".center(11),"PRINCIPAL".center(11), "BALANCE".center(11),"\n ")

# loan_interest = 0
# for payment in range(no_payments + 1):


#     if payment == 0:
#         print(str(payment).center(5),"-".center(11), "-".center(11), "-".center(11), str(loan_amount).center(11))
#     else:
#         interest = loan_amount * (rate/payments_per_year)
#         loan_amount = loan_amount - (repayment - interest)
#         principal = (repayment - interest)
#         principal = round(principal,2)
#         loan_interest += interest
#         repayment, interest, loan_amount = round(repayment,2), round(interest,2), round(loan_amount,2)

#         print(str(payment).center(5),str(repayment).center(11), str(interest).center(11), str(principal).center(11), str(loan_amount).center(11))
# print(loan_interest)

t = newTable("Table1")
