def canMakeArithmeticProgression(arr):
    arr.sort()
    # print(arr)
    #define set to store difference
    diff=set()
    for i in range(len(arr)-1):            
        a=arr[i+1]-arr[i]
        #add values to set as it does not allow duplicates
        diff.add(a)

    if len(diff)==1:
        return True
    return False

print(canMakeArithmeticProgression([1,3,5]))
print(canMakeArithmeticProgression([1,3,6]))