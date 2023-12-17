def arraysign(nums):
    n=len(nums)
    product=1
    for i in range(n):
        product*=nums[i]
    if product==0:
        return 0
    elif product>0:
        return 1
    else:
        return -1

nums=[-1,-2,-3,-4,3,2,1]
print(arraysign(nums))
print(arraysign([-1,1,-1,1,-1]))
print(arraysign([-1,8,63,3,0]))