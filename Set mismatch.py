def findErrorNums(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n=len(nums)
    d,m=-1,-1
    for i in range(1,n+1):
        c=nums.count(i)
        if c==2:
            d=i
        elif c==0:
            m=i
    return [d,m]
        
print(findErrorNums([1,2,2,4]))
print(findErrorNums([1,1]))