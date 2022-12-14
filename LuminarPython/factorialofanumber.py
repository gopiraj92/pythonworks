# Find the factorial of a number we enter

# Factorial of 5 is find as 1*2*3*4*5=120
n = int(input("Enter a number = "))
sum = 1
for i in range(1, n+1, 1):
    sum = sum * i
print("The factorial of", n, "is = ", sum)
