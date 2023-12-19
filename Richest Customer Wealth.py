def maximumWealth(accounts):
    
    n=len(accounts)
    l=[]*0
    for i in range(n):
        l.append(sum(accounts[i]))
    m=max(l)
    return m
print(maximumWealth([[1,2,3],[3,2,1]]))
print(maximumWealth([[1,5],[7,3],[3,5]]))