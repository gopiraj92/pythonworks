# Largest among 3 numbers
 # f s t
 # f>s and f>t = f is largest
 # s>f and s>t = s is largest
 # t>f and t>s = t is largest

f = int(input("Enter the first number = "))
s = int(input("Enter the second number = "))
t = int(input("Enter the third number = "))

if (f>s and f>t):
    print(f, "is the largest number among 3 numbers")
elif (s>f and s>t):
    print(s, "is the largest number among 3 numbers")
elif (t>f and t>s):
    print(t, "is the largest number among 3 numbers")
else:
    print("All numbers are same")
