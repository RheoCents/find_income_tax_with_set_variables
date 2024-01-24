#Calculate income tax for the given income by adhering to the rules below
#1st 1000 is 0% interest, 2nd 1000 is 10% interest, remainging is 20%
print('This is a calculator for your income ta based on these parameters')
print('1st $1000.0 = 0% tax\n2nd $1000.0 = 1% tax\nonwards = 2% tax')
user_income = float(input('\nSo how much is your income? '))

print('Your income is', user_income, 'and your payable tax is')

if user_income < 1000:
    income_tax = 0
    print('($'+str(user_income), '* 0%) + ($0.0 * 10%) + ($0.0 * 2%) = $'+str(income_tax))

if user_income in range (1000, 2001):
    income_tax = (user_income-1000) * 1
    print('($1000.0 * 0%) + ($'+str(income_tax),'* 10%) + ($0.0 * 2%) = $'+str(income_tax))

if user_income > 2000:
    income_tax = ((user_income-2000)*2)+1000
    print('($1000.0 * 0%) + ($1000.0* 10%) + ($'+str(user_income-2000), '* 2%) = $'+str(income_tax))
