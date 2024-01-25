#Calculate income tax for the given income by adhering to the rules below
#1st 1000 is 0% interest, 2nd 1000 is 10% interest, remainging is 20%
print('This is a calculator for your income ta based on these parameters')
print('1st $10,000.0 = 0% tax\n2nd $10,000.0 = 1% tax\nonwards = 2% tax')
user_income = float(input('\nSo how much is your income? '))

print('\nYour income is $'+ str(user_income), 'and your payable tax is')

if user_income < 10000:
    income_tax = 0
    print('($'+str(user_income), '* 0%) + ($0.0 * 10%) + ($0.0 * 20%) = $'+str(income_tax))

if user_income in range (10000, 20001):
    income_tax = (user_income-10000) * 0.1
    print('($10000.0 * 0%) + ($'+str(income_tax),'* 10%) + ($0.0 * 20%) = $'+str(income_tax))

if user_income > 20000:
    income_tax = ((user_income-20000)*0.2)+(10000*0.1)
    print('($10000.0 * 0%) + ($10000.0* 10%) + ($'+str(user_income-20000), '* 20%) = $'+str(income_tax))
