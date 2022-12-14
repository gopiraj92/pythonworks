# Eg 1.
# To search a word in a file using regular expression

# import re
#
# f1 = open('file1', 'r')
# text = f1.readlines()
# print(text)
# for line in text:
#     rslt = re.search('you', line)
#     if(rslt):
#         print(line)

# Eg 2.

import re
f1 = open('file1', 'r')
text = f1.readlines()
for line in text:
    result = re.search(r'\bs.e\b', line)
    if result:
        print(line)
