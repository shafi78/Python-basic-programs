# Program to find area of triangle 

import math

a = int(input("Enter the value of first side : "))
b = int(input("Enter the value of second side : "))
c = int(input("Enter the value of third side : "))

s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print("The value of first side is {0}".format(a))
print("The value of second side is {0}".format(b))
print("The value of third side is {0}".format(c))
print("The value of triangle is {0}".format(area))