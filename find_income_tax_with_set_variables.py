#Calculate income tax for the given income by adhering to the rules below
#1st 1000 is 0% interest, 2nd 1000 is 10% interest, remainging is 20%
print('This is to know your income tax in thousand ex. 3000')
user_income = float(input('How much is your income? '))
computation_variable_need = (user_income-2000)

def zero_percent_rateb():
    zero_percent_rate = user_income - 1000 

for i in range (3):
     if i == 1:
         zero_percent_rate = (user_income-1000)
     if i == 2:
         one_percent_rate = (zero_percent_rate-1000)
     if i == 3:
         two_percent_rate  = (user_income-2000)
         if two_percent_rate < 0:
             two_percent_rate = 0
income_tax = zero_percent_rate + one_percent_rate + two_percent_rate
print(income_tax)
