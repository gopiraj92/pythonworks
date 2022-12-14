# Reduce function

# Eg.
import functools
lst = [1,2,3,4,5]
res = functools.reduce(lambda x,y:x+y,lst)
print(res)
