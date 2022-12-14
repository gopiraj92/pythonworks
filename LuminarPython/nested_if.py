# nested if - if or else statement contain another if else...

# Eg. 1. Check the entered number is positive or negative or zero

# n = int(input("Enter a number = "))
#
# if n>0:
#     print("The number is positive")
# else:
#     if n<0:
#         print("The number is negative")
#     else:
#         print("The number is zero")


# Eg. 2. Largest among 3 numbers using nested if

n1 = int(input("Enter first number = "))
n2 = int(input("Enter second number = "))
n3 = int(input("Enter third number = "))

if n1 > n2:
    if n1 > n3:
        print(n1, "is the largest number")
    else:
        print(n3, "is the largest number")

else:
    if n2 > n3:
        print(n2, "is the largest number")
    else:
        print(n3, "is the largest number")
