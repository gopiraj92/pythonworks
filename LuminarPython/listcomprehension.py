# List comprehension

# flowers = ['lilly','lotus','rose','sunflower']
# newflowers=[]
#
# for flower in flowers:
#     if 'o' in flower:
#         newflowers.append(flower)
# print(newflowers)

# in list comprehension method
# newflowers = [i for i in flowers if 'o' in i]
# newflowers = [i.upper() for i in flowers]
# newflowers = ['hibiscus' if i!='lilly' else 'lilly' for i in flowers]
# newflowers = ['hibiscus' if i=='sunflower' else i for i in flowers]
# print(newflowers)


# num = [2,3,4,5,6,7,8]
# newnum = [i for i in num if i%2==0]
# print(newnum)


# lst2 = [1,2,3,4,5,6]
# newlst = ['even' if(i%2==0) else 'odd' for i in lst2]
# print(lst2)
# print(newlst)

# eg
lst = [1,2,3,4,5,6,7,8,9,10]
newlst = [i if i%2==0 else i*i for i in lst]
print(newlst)
