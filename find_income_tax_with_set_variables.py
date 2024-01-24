#Calculate income tax for the given income by adhering to the rules below
#1st 1000 is 0% interest, 2nd 1000 is 10% interest, remainging is 20%
print('This is to know your income tax in thousand ex. 3000')
user_income = input('How much is your income? ')
computation_variable_need = (user_income-2000)

if user_income < 1000:
    income_tax = 0
if user_income in range (1000, 2000):
    income_tax = (user_income-1000) * 1
if user_income > 2000:
    income_tax = [(user_income-2000)*2]+1000

print(income_tax)