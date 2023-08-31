# Program to search an element using linear search

def linear_search(list1,n,key):

    for i in range(0,n):
        if (list1[i] == key):
            return i
    return -1

num = []
p = int(input("Enter the no of elements : "))
for i in range(p):

    p = int(input("Enter the elements : "))
    num.append(p)

print("The elements of the array are : ")
print(num)
key = int(input("Enter the element to search : "))

n = len(num)
res = linear_search(num,n,key)

if (res == -1):
    print("The element ",key," not found")

else:
    print("The element ",key," is found at index : ",res)
