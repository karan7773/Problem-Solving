def isAnagram( s, t):
    if len(s)!=len(t):
        return False
    os=[0]*26
    ot=[0]*26
    for i in range(len(t)):
        x=ord(s[i])-97
        os[x]+=1
        y=ord(t[i])-97
        ot[y]+=1
    if os==ot:
        return True
    return False

print(isAnagram("anagram","mrgana"))