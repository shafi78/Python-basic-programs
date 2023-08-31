# Program to Multiply two matrices

A = []
n = int(input("Enter N for N X N matrix : "))

for i in range(n):

    row = []

    for j in range(n):

        row.append(int(input()))
    
    A.append(row)

print(A)
print("Display Array in matrix form : ")

for i in range(n):
    for j in range(n):
        print(A[i][j],end=" ")

    print()

B = []
n = int(input("Enter N for N X N matrix : "))

for i in range(n):

    row = []

    for j in range(n):

        row.append(int(input()))

    B.append(row)

print(B)
print("Display Array in matrix form : ")

for i in range(n):
    for j in range(n):
        print(A[i][j],end=" ")

    print()

print(B)
print("Display Array in matrix form : ")

for i in range(n):
    for j in range(n):
        print(B[i][j],end=" ")

    print()

result = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):

            result[i][j] += A[i][k] * B[k][j]

print("The resultant matrix is : ")
for r in result:

    print(r)