def mostWordsFound(sentences):
    m=0
    for i in range(len(sentences)):
        l=len(sentences[i].split(" "))
        if m<l:
            m=l
    return m

print(mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))
print(mostWordsFound(["please wait", "continue to fight", "continue to win"]))