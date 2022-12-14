# Print numbers under the limit we enter.
# In the output, in the place of multiples of 3, print "I'm multiple of 3" instead of that number.
# output Eg
# 1
# 2
# I'm multiple of 3
# 4
# 5
# I'm multiple of 3
# 7
# 8
# I'm multiple of 3

n = int(input("Enter the limit = "))
for i in range(1, n+1, 1):
    if(i%3==0):
        print("I'm multiple of 3")
    else:
        print(i)
