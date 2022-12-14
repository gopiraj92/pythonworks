# Word count

def wordcount(lst):
    wc = {}
    for word in lst:
        if word in wc:
            wc[word]+=1
        else:
            wc[word]=1
    print(wc)

text = "hai hello hai hi hello fuck hai hello hello hi"
print(text)
lst = text.split()
print(lst)
wordcount(lst)
