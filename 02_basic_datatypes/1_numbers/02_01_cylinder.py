'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''

# import the math library
import math

# assign the values of the radius and height
cylinder_radius = 3.14
cylinder_height = 5

# calculate the volume and area rounded to 2 decimal places
cylinder_volume = round(math.pi * cylinder_height * cylinder_radius ** 2, 2)
cylinder_area = round(2 * math.pi * cylinder_radius * cylinder_height - 2 * math.pi * cylinder_radius ** 2, 2)

# print the results
print("The area of the cylinder is ", cylinder_area)
print("The volume of the cylinder is ", cylinder_volume)
