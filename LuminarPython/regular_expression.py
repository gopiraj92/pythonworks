# Regular expression

# import re
# str = 'i love python programming'
# result = re.match('i', str)         # re.search('pattern to be searched', string)
# if result:
#     print("Pattern exists")
# else:
#     print("Pattern not exists")

# findall
# import re
# zipcode = '123-22 ssaf 2'
# print(zipcode)
# new = re.findall('\d',zipcode)
# print(new)
# new1 = re.sub('\D','@',zipcode)
# print(new1)


# Eg. Password
import re
p = input("Enter a password of your choice = ")

if len(p) < 6 or len(p) > 16:
    print("Invalid Password")
elif not re.search('[a-z]', p):
    print("Invalid Password")
elif not re.search('[A-Z]', p):
    print("Invalid Password")
elif not re.search('[0-9]', p):
    print("Invalid Password")
elif not re.search('[!@#$%^&*]', p):
    print("Invalid Password")
else:
    print("Valid Password")
