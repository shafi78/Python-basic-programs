# Program to swap two variables 

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

print("\n Before swapping")
print("The value of a : ",a)
print("The value of b : ",b)

temp = a
a = b 
b = temp

print("\n After swapping")
print("The value of a : ",a)
print("The value of b : ",b)