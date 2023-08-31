# Program to display multiplication table 

num = int(input("Enter a number : "))

for i in range(1,11):

    print("{0} * {1} = {2}".format(num,i,num*i))

