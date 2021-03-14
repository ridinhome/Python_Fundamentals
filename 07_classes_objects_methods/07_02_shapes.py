'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''
import math
from decimal import Decimal

class Rectangle():

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Circle():

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        circle_area = 2 * math.pi * self.radius
        return round(circle_area,2)

    def perimeter(self):
        circle_perimeter = math.pi * self.radius ** 2
        return round(circle_perimeter, 2)

length, width, radius = input("Please enter the length, width and radius of a rectangle and a circle:").split()

my_rectangle = Rectangle(int(length),int(width))
my_circle = Circle(int(radius))

print (f"The area of the rectangle is {my_rectangle.area()}")
print(f"The perimeter of the rectangle is {my_rectangle.perimeter()}")

print (f"The area of the circle is {my_circle.area()}")
print(f"The perimeter of the circle is {my_circle.perimeter()}")



