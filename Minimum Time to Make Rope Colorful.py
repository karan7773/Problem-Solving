def minCost(colors, neededTime):
    """
    :type colors: str
    :type neededTime: List[int]
    :rtype: int
    """
    tot=0
    curr=colors[0]
    maxt=neededTime[0]
    
    for i in range(1,len(neededTime)):
        if curr==colors[i]:
            if neededTime[i]>maxt:
                tot+=maxt
                maxt=neededTime[i]
            else:
                tot+=neededTime[i]
        else:
            curr=colors[i]
            maxt=neededTime[i]
    return tot

colors = "aaabbbabbbb" 
neededTime = [3,5,10,7,5,3,5,5,4,8,1]

print(minCost(colors,neededTime))