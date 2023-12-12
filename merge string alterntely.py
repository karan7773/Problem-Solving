def mergeAlternately(word1, word2):
    n1=len(word1)
    n2=len(word2)
    count=min(n1,n2)
    word3=""
    for i in range(count):
        word3+=word1[i]
        word3+=word2[i]
    word3+=word1[count:]+word2[count:]
    return word3

word1 = "abc" 
word2 = "pqr"
word3=mergeAlternately(word1,word2)
print(word3)