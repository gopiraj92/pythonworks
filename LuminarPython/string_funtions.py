# Input a string. Count vowels in that string, spaces, consonants

str = input("Enter a string =")
# vcount = 0
# ccount = 0
# space = str.count(" ")
# for ch in str:
#     if ch in 'aeiouAEIOU':
#         vcount = vcount+1
#     else:
#         ccount = ccount+1
# print("The count of vowels in the string is =", vcount)
# print("The count of cosonants in the string is =", ccount-space)
# print("Count of spaces in the string is =", space)

# or

vowel = 0
space = 0
cons = 0
for ch in str:
    if ch in 'aeiouAEIOIU':
        vowel+=1
    elif ch == " ":
        space+=1
    else:
        cons+=1
print("The count of vowels in the string is =", vowel)
print("The count of consonants in the string is =", cons)
print("The count of spaces in the string is =", space)

