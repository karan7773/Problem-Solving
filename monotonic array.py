def isMonotonic(nums):
    anum=[]
    anum.extend(nums)
    anum.sort()
    dnum=[]
    dnum.extend(nums)
    dnum.sort(reverse=True)
    print(anum,dnum)
    if nums==anum:
        return True
    elif nums==dnum:
        return True
    else:
        return False
    
print(isMonotonic([1,2,2,4]))