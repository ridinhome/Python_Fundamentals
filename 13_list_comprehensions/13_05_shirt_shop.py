'''
Using a list comprehension, create a *cartesian product* (google this!)
of the given lists.

Then open up your online shop ;)

'''
styles = []
colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]

styles = [(i,j) for i in colors for j in sizes]
print (styles)