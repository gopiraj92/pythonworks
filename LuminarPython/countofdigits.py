# Program to count the number of digits in a number entered.

n = int(input("Enter a number = "))

count = 0

while(n > 0):
    count = count + 1
    n = n//10
print("The number of digits in the entered number is = ", count)
