# 1) Create a Module in VS Code and Import It into jupyter notebook
# Module should have the following capabilities:

# 1a) Has a function to calculate the square footage of a house
# Reminder of Formula: Length X Width == Area

def square_footage(length, width):
    area = length * width
    return area

length = int(input("Enter length in feet: "))
width = int(input("Enter width in feet: "))
result = square_footage(length, width)

print(f"Square footage of the house is: {result} square feet")


# 1b) Has a function to calculate the circumference of a circle 2 Pi r

import math
def circumference_circle(radius):
    circumference = 2 * math.pi * radius
    return circumference

radius = float(input("Enter the radius of the circle : "))

result = circumference_circle(radius)

print(f"Circumference of the circle is : {result:.2f}")

