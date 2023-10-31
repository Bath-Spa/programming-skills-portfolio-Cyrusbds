#Exercise 1: Print Strings
print("TWINKLE TWINKLE:")
print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are!")

#Exercise 2: Print the Version of Python
import sys
print("PYTHON VERSION:")
print(sys.version)

#Exercise 3: Print date and Time
import datetime
print("DATE AND TIME:")
print(datetime.datetime.now())

#Exercise 4: Strings Concatination
print("THREE STRINGS:")
var1 = "My Name "
var2 = "is "
var3 = "Cyrus"
print(var1, var2, var3)

#Exercise 5: Compute area of Circle
import math
print("RADIUS OF A CIRCLE:")
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius * radius
print("The area of %0.3f in the circle is %0.3f"%(radius, area))