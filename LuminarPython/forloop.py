# For loop

# for iteration variable in range (start, stop, step(or increment)):
      # body of the loop

# Eg. 1.
# for i in range(1, 5, 1):
#     print("Hai...")

# Eg. 2.
# for i in range(5):
#     print(i)

# Eg. 3.
# for i in range(5):
#     print(i, end=" ")

# Eg. 4. Print even numbers under 10
# for i in range(2, 10, 2):
#     print(i, end=" ")

# Eg. 5. Print sum of even numbers under 10
# sum = 0
# for i in range(2, 10, 2):
#     print(i)
#     sum = sum + i
# print("Sum is = ", sum)

# Eg. 6. Print sum of even numbers under the limit we enter
# sum = 0
# n = int(input("Enter the limit = "))
# for i in range(2, n, 2):
#     print(i)
#     sum = sum + i
# print("Sum is = ", sum)

# Eg. 7. Print sum of odd numbers under the limit we enter
sum = 0
n = int(input("Enter the limit = "))
for i in range(1, n, 2):
    print(i)
    sum = sum + i
print("Sum is = ", sum)
