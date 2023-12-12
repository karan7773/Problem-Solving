def totalMoney(n):
    w=n//7
    rw=n%7
    amount=(w*(w-1)//2)*7
    amount+=w*28
    j=w+1
    for i in range(rw):
        amount+=j
        j+=1
    return amount
n=10
print(totalMoney(n))