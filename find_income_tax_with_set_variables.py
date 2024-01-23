#Calculate income tax for the given income by adhering to the rules below
#1st 1000 is 0% interest, 2nd 1000 is 10% interest, remainging is 20%
print('This is to know your income tax in thousand ex. 3000')
user_income = float(input('How much is your income? '))
computation_variable_need = (user_income-2000)
if user_income >= 1000:
    income_tax = ((int(user_income) - 2000)*2) + 1000
    print('For an income of $',user_income, 'the income tax will be')
    print(income_tax)
if user_income < 1000:
    print("the inputted amount don't quialify the tax rules")
    print('For an amount of ', user_income, 'The tax will be $ 0')