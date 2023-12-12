def findTheDifference(s, t):
    for i in t:
        if s.count(i) != t.count(i):
            return i
s = "abcd"
t = "abcde"
diff=findTheDifference(s,t)
print(diff)