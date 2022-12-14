# Filter function

# syntax - filter(function, sequence)

# Eg. 1.
# lst = [1,2,3,4,5,6]
# res = filter(lambda x: x%2==0, lst)      # gives filtered o/p of even numbers only
# print(list(res))

# Eg. 2.
# lst = [1,2,3,4,5,6]
# res = filter(lambda x: x%2!=0, lst)        # gives filtered o/p of odd numbers only
# print(list(res))

# Eg. 3. input the list from console

# lst = input("Enter the list elements =").split()
# print(lst)
# lst1 = map(int, lst)
# even = filter(lambda x: x%2==0, lst1)
# print(list(even))

# Eg. 4.
# create a list from existing list which have only multiples of 5

# lst = input("Enter the list elements =").split()
# lst1 = map(int, lst)
# res = filter(lambda x: x%5==0, lst1)
# print(list(res))


# Eg 5.
#create a list which having the values greater than 5
lst = input("Enter the list elements =").split()
lst1 = map(int, lst)
res = filter(lambda x: x>5, lst1)
print(list(res))
