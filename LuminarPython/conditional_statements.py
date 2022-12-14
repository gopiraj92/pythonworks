# Conditional statements

 # 1. Simple IF
 # 2. IF...ELSE
 # 3. IF...ELIF...ELSE
 # 4. Nested IF


# 1. Simple IF

 # Eg 1. Check a number is positive

# n = int(input("Enter the number ="))
#
# if n>0:
#     print("The number is positive")


 # Eg 2. Check a given number is even number

# n = int(input("Enter a number = "))
#
# if (n % 2 == 0):
#     print("The number is even number")


 # Eg 3. Check a given number is multiple of 5

# n = int(input("Enter the number = "))
#
# if (n % 5 == 0 and n % 7 == 0):
#     print("The number is multiple of 5 and 7")


# 2. IF...ELSE
 # eg 1.
# n = int(input("Enter a number = "))
#
# if n>0:
#     print("The number is positive")
# else:
#     print("The number is negative or zero")

 # Eg 2.

# n = int(input("Enter the number ="))
#
# if n % 2 == 0:
#     print("The number is even number")
# else:
#     print("The number is odd number")


 # Eg 3. Largest among two numbers
# n1 = int(input("Enter the number n1 = "))
# n2 = int(input("Enter the number n2 = "))
#
# if n1 > n2:
#     print("The number", n1, "is greater than the number", n2)
# else:
#     print("The number", n2, "is greater than the number", n1)


# 3. IF...ELIF...ELSE

 # Eg. 1. Check the given number is positive or negative or zero.

# n = int(input("Enter the number = "))
#
# if n>0:
#     print("The number is positive")
# elif n<0:
#     print("The number is negative")
# else:
#     print("The number is zero")

 # Eg. 2.  enter a number, if it is >10, print Big, if it is <10 print Small, if it is equal, print Expected.

# n = int(input("Enter a number = "))
#
# if n > 10:
#     print("The number is Big")
# elif n < 10:
#     print("The number is Small")
# else:
#     print("Expected number")

 # Eg. 3. Enter a number, check it is divisible by 5 and 7, print it, only divisible by 5, 7 only, not divisible by 5&7

n = int(input("Enter the number = "))

if (n % 5 == 0 and n % 7 == 0):
    print("The number is divisible by both 5 and 7")
elif n % 5 == 0:
    print("The number is divisible by 5 only")
elif n % 7 == 0:
    print("The number is divisible by 7 only")
else:
    print("The number is not divisible by both 5 and 7")
