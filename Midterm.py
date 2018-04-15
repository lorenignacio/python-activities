def match_words(words):
    ctr = 0

    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
    return ctr

x=input("ENTER STRING:")
print match_words(x)

def front_x(words):
    xlist=[]
    alist=[]

    for word in words:
        if word.startswith('x'):
            xlist.append(word)
        else:
            alist.append(word)

    return sorted(xlist)+sorted(alist)

x=input("ENTER STRING:")
print front_x(x)
