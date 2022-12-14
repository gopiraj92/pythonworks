# Write a program to perform a simple calculator operations
 # 1. Addition
 # 2. Subtraction
 # 3. Multiplication
 # 4. Division

 # Enter two numbers
 # Display this menu
 # Enter the choice
 # Print the result


n1 = int(input("Enter the number 1 = "))
n2 = int(input("Enter the number 2 = "))

print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")

ch = int(input("Enter your choice = "))

if ch == 1:
    print("The result is =", n1+n2)
elif ch == 2:
    print("The result is =", n1-n2)
elif ch == 3:
    print("The result is =", n1*n2)
elif ch == 4:
    print("The result is =", n1/n2)
else:
    print("Wrong choice entered")
