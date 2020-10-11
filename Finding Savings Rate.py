'''You are now going to try to find the best rate of savings to 
achieve a down payment on a house in 36 months. Since hitting this 
exactly is a challenge, we simply want your savings to be within 
$100 of the required down payment.'''

house_cost = float(input("How much is the house you are saving for? "))
down_payment = 0.25*house_cost
semi_annual_raise = 0.07
annual_interest_rate = 0.04
starting_salary = float(input("What is your annual salary? "))
monthly_salary = starting_salary / 12
low = 0
high = 10000
savings_rate = (low + high)/2.0
savings = 0
month = 0
steps = 0
while abs(savings - down_payment) >= 100:
    savings = 0
    while month < 36 :
        savings += savings*(annual_interest_rate/12)
        savings += monthly_salary * (savings_rate/10000)
        month += 1
        if month%6 == 0 :
            monthly_salary += monthly_salary*semi_annual_raise
    if savings < down_payment:
        low = savings_rate
    else:
        high = savings_rate
    savings_rate = (low + high)/2.0
    steps += 1
    month = 0
    monthly_salary = starting_salary / 12
print ("Your savings rate is " + str(round((savings_rate/100),2)) + "%!")
print ("It took " + str(steps) + " steps.")

