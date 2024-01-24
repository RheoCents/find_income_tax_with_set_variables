#Calculate income tax for the given income by adhering to the rules below
#1st 1000 is 0% interest, 2nd 1000 is 10% interest, remainging is 20%
print('This is to know your income tax in thousand ex. 3000')
user_income = float(input('How much is your income? '))

print('Your income is', user_income, 'and your payable tax is')

if user_income < 1000:
    income_tax = 0
    print('($'+str(user_income), '* 0%) + ($0.0 * 10%) + ($0.0 * 2%) = $'+str(income_tax))

if user_income in range (1000, 2000):
    income_tax = (user_income-1000) * 1
    print('($1000.0 * 0%) + ($'+str(income_tax),'* 10%) + ($0.0 * 2%) = $'+str(income_tax))

if user_income > 2000:
    income_tax = ((user_income-2000)*2)+1000
    print('($1000.0 * 0%) + ($1000.0* 10%) + ($'+str(user_income-2000), '* 2%) = $'+str(income_tax))
