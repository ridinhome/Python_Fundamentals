'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets at least three attributes
- Include a __str__ method in each class that prints out the attributes
    in a nicely formatted string.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Create at least two instances of each class.
- Once the objects are created, change some of their attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, card games, sports teams, trees, people etc...

'''

class Ball():

    def __init__(self, size,color,material,sport):
        self.size = size
        self.color = color
        self.material = material
        self.sport = sport

    def __str__(self):
        print (f"The ball is {self.size} cm in diameter, it is {self.color} in color, made of {self.material} and use in {self.sport}")

    def __add__(self,other):
        return self.size + other.size

class Bat():

    def __init__(self,length,material,sport):
        self.length = length
        self.material = material
        self.sport = sport

    def __str__(self):
        print (f"The bat is {self.length} inches long, made of {self.material} and is used in {self.sport}.")

class Shoes():

    def __init__(self, size, material, sport):
        self.size = size
        self.material = material
        self.sport = sport

    def __str__(self):
        return (f"The shoes are size {self.size}, made of {self.material} and used in {self.sport}")

ball1 = Ball(20,"Red","Rubber","Basketball")
ball2 = Ball(10,"White","Leather","Baseball")

bat1 = Bat(10,"Wood","Baseball")
bat2 = Bat(15,"Graphite","Tennis")

shoes1 = Shoes(10,"Leather","Basketball")
shoes2 = Shoes(12,"Rubber","Baseball")

ball1.__str__()
ball2.__str__()
bat1.__str__()
bat2.__str__()
shoes1.__str__()
shoes2.__str__()

print (ball1.__add__(ball2))

