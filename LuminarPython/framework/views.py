# print all framework names

from framework.models import frameworks as fws

# for fw in fws:
#     print(fw.get("name"))

# in list comprehension method

# print([fw.get("name") for fw in fws])


# print framework names who having rating > 4

# for fw in fws:
#     if fw.get("rating")>4:
#         print(fw.get("name"))

# in list comprehension method

# print([fw.get("name") for fw in fws if fw.get("rating")>4])


# print framework name who having language is python

print([fw.get("name") for fw in fws if fw.get("language")=="python"])

