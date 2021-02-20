'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

inv_amt = int(input("Enter investment amount:"))
int_rate = int(input("Enter an interest rate in percent:"))
horizon = int(input("Enter number of years:"))

future_value = inv_amt * (1 + int_rate / 100) ** horizon
print("Future value is:", future_value)


