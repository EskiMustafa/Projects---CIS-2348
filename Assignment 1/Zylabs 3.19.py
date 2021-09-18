# Mustafa Shabbir Eski
# PSID: 2046388
# Zylabs 3.19: Painting a Wall
import math

height = float(input('Enter wall height (feet):\n'))
width = float(input('Enter wall width (feet):\n'))
wallarea = height * width
print('Wall area:', int(wallarea), 'square feet')
paint_gallon = 350
paint_needed = wallarea / 350
print("Paint needed: %.2f gallons" % paint_needed)

cansneeded = math.ceil(paint_needed)  # reference:"https://kodify.net/python/math/round-integers/"
print("Cans needed:", cansneeded, "can(s)")
print()
color = input("Choose a color to paint the wall:\n")
if color == 'red':
    cost = 35 * cansneeded
elif color == 'blue':
    cost = 25 * cansneeded
elif color == 'green':
    cost = 23 * cansneeded
else:
    cost = 0
print('Cost of purchasing', color, 'paint:',"$"+str(cost))
