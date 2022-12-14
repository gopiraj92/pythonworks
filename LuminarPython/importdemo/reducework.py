# Read a list. covert it into int, filter even list and odd list from that list. find the sum of both even and odd lists.

import functools
lst = input("Enter the list elements = ").split()
# print(lst)

lst1 = list(map(int, lst))
evenlst = list(filter(lambda x: x%2==0, lst1))
oddlst = list(filter(lambda x: x%2!=0, lst1))
print("The list is: ", lst1)
print("Even list is: ", evenlst)
print("Odd list is: ", oddlst)

evensum = functools.reduce(lambda x,y: x+y, evenlst)
oddsum = functools.reduce(lambda x,y: x+y, oddlst)
print("Even list sum is = ", evensum)
print("Odd list sum is = ", oddsum)
