# Find the sum of first n natural numbers we enter

n = int(input("Enter a limit = "))
sum = 0
for i in range(1, n+1, 1):
    sum = sum + i
print("Sum is = ", sum)
