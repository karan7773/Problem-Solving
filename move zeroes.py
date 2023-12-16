def movezeros(nums):
    n=len(nums)
    i=0
    for j in range(n):
        if nums[j]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
nums=[1,0,4,3,0]
movezeros(nums)
print(nums)