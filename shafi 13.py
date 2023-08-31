# Program to find sum of positive and negative numbers

n = int(input("Enter the limit : "))
a = []
psum = 0 
nsum = 0 

for i in range(n):

    x = int(input("Enter an element : "))
    a.append(x)

for i in a:

    if i>=0:
        psum +=i 

    else:
        nsum +=i 

print("The sum of positive numbers in the array is : ",psum)
print("The sum of negative numbers in the array is : ",nsum)