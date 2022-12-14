# Print the multiplication table of 5 using for loop
# 1 * 5 = 5
# 2 * 5 = 10
# 3 * 5 = 15

# for i in range(1, 11, 1):
#     print(i, "* 5 =", i*5)

# Eg. 2. Print multiplication table of any number we enter

n = int(input("Enter a number = "))
for i in range(1, 11, 1):
    print(i, "*", n, "=", i*n)
