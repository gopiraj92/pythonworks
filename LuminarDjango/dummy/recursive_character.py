# Recursive character

# print the first recursive character in a pattern

pattern = "ABAACBD"
rc={}
for w in pattern:
    if w in rc:
        print(w, "is the 1st recursive character")
        break
    else:
        rc[w]=1
