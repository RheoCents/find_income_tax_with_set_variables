#Calculate income tax for the given income by adhering to the rules below
#1st 1000 is 0% interest, 2nd 1000 is 10% interest, remainging is 20%
print('This is to know your income tax in thousand ex. 3000')
user_income = float(input('How much is your income? '))

income_tax = ((int(user_income) - 2000)*2) + 1000
print(income_tax)