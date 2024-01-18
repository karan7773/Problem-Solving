def uniqueOccurrences(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    dic={}
    s=set()
    for i in range(len(arr)):
        if arr[i] not in dic:
            dic[arr[i]]=1
        else:
            dic[arr[i]]+=1
    for i in dic:
        s.add(dic[i])
    # print(s)
    if len(dic)==len(s):
        return True
    return False
    
print(uniqueOccurrences([1,2,2,1,1,3]))
print(uniqueOccurrences([1,2]))