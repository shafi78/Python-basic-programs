# Program to find factorial of a number 

num = int(input("Enter a number : "))
factorial = 1

if num>0:

    for i in range(1,num+1):
        
        factorial *= i 

else:

    print("Negative numbers are not allowed")
    factorial = "Invalid"

print("The factrial of {0} is {1}".format(num,factorial))