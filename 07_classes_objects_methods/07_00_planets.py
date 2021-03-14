'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''

class Planet():

    def __init__(self,name,color,system):
        self.name = name
        self.color = color
        self.system = system

    def __str__(self):
        return f"The name of the planet is {self.name}, it is {self.color} in color and it is in the {self.system} system."

my_planet = Planet("Earth","Red","Solar")
print (my_planet)
