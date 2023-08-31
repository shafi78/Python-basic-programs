# Program to find total number of vowels and letters in a string

totlet = 0
totvow = 0

str = input("Enter a string : ")

for i in range(len(str)):

    if str[i].isalpha():

        totlet += 1

    if str[i] in ['a','e','i','o','u']:

        totvow += 1

print("The number of letters are : ",totlet)
print("The number of vowels are : ",totvow)