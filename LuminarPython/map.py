# Map function

# Eg 1.
def mul(n):
    return n*n

# num = [1,2,3,4,5]
# result = map(mul,num)    # map(fuction, sequence)
# print(list(result))

# Eg 2.
# using lambda function
# num = (1,2,3,4)
# result = map(lambda n:n*n, num)
# print(list(result))

# Eg. 3.
# num1 = [1,2,3,4]
# num2 = [5,6,7,8]
# result = map(lambda x,y: x+y, num1, num2)
# print(list(result))

# Eg 4.
# fruits = ['apple', 'orange', 'mango', 'banana', 'jackfruit']
# result = map(len, fruits)
# print(list(result))

# Eg 5.
fruits = ['apple', 'orange', 'mango', 'banana', 'jackfruit']
newlst = map(list, fruits)
print(list(newlst))
