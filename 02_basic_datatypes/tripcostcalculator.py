#Ask user for the distance to be travelled
distance = float(input ("How far are you going to drive? "))

#Ask user how fuel efficient the car is

efficiency = float(input("How fuel efficient is your car? "))

#Ask user how much petrol costs

gas_price = float(input("How much does fuel cost? "))

tripcost = distance / efficiency * gas_price

print ("The cost of your trip is $", tripcost)



