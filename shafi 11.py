# Program to find GCD and LCM 

print("Enter two numbers : ")

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

a = num1
b = num2 

while b!=0:

    temp = b
    b = a%b 
    a = temp 

gcd = a 
lcm = int((num1*num2)/gcd)

print("The LCM of {0} and {1} is {2}".format(num1,num2,lcm))
print("The GCD of {0} and {1} is {2}".format(num1,num2,gcd))