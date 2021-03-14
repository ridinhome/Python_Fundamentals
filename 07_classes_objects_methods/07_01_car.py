'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''

class Car():
    def __init__(self,model,year,max_speed):
        self.model = model
        self.year = year
        self.speed = max_speed

    def accelerate(self):
        self.speed += 5

    def __str__(self):
        return(f"The {self.model} is from {self.year} and has a maximum speed of {self.speed}.")

my_car1 = Car("BMW",2020,90)
my_car2 = Car("Toyota",2019,70)

print (my_car1)
print (my_car2)

my_car1.accelerate()
print (my_car1)

my_car2 = Car("Honda",2018,65)
print (my_car2)
