# File

# File - collection of data (pdf, ppt, doc, jpeg etc)

# fileobject = open('filename','mode')

# Mode
  # r - read
  # r+ - read, write
  # w - write
  # w+ - read, write
  # a - append


# Eg 1.

# f1 = open('file1', 'r')
# print("First location:", f1.tell())
# print(f1.read(3))
# print("Second location:", f1.tell())
# print(f1.read(3))
# print("Third location:", f1.seek(2))
# print(f1.read(5))
# f1.close()

# Eg 2.

# f2 = open(r"C:\Users\gopir\Desktop\abc.txt", 'r')
# print(f2.read())
# f2.close()


# Eg 3.

# f3 = open('file1', 'r')
# lst = f3.readlines()
# print(lst)
# for i in lst:
#     print(i.strip())
# f3.close()

# Eg 4.

# f1 = open('file1', 'r')
# lst = f1.readlines()
# print(lst)
# f2 = open('file2', 'w')
# f2.writelines(lst)
# f1.close()
# f2.close()

# Eg 5.
# count the number of words in a file
# f1 = open('file1', 'r')
# r = f1.read()
# print(r)
# words = r.split()
# print(words)
# # c=0
# # for i in words:
# #     c=c+1
# # print(c)
# print(len(words))

# dictionary basics
# dict = {}
# dict['hello'] = 1
# print(dict)
# dict['hello']=dict['hello']+1
# print(dict)
# dict['world'] = 1
# print(dict)

# Eg 6.
# to count how many times each words occured in a file

# def wordcount(lst):
#     dict = {}
#     for word in lst:
#         if word in dict:
#             dict[word]+= 1
#         else:
#             dict[word] = 1
#     print(dict)
#
# f1 = open('file1','r')
# r = f1.read()
# words = r.split()
# wordcount(words)

# Eg. 7.
# To print the elements of a file one by one with its key-value form

def wordcount(lst):
    dict = {}
    for word in lst:
        if word in dict:
            dict[word]+= 1
        else:
            dict[word] = 1
    for k,v in dict.items():
        print(k, " : ", v)

f1 = open('file1','r')
r = f1.read()
words = r.split()
wordcount(words)
