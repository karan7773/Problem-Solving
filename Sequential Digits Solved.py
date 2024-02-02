def sequentialDigits( low, high):
    """
    :type low: int
    :type high: int
    :rtype: List[int]
    """
    a=[]
    for i in range(1,10):
        num=i
        nxt=i+1
        while num<=high and nxt<=9:
            num=num*10+nxt
            if low<=num<=high:
                a.append(num)
            nxt+=1
    a.sort()
    return a

print(sequentialDigits(100,300))
print(sequentialDigits(1000,4000))
