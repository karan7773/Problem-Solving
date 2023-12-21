def search( nums, target):
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif target<nums[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1

        
nums = [-1,0,3,5,9,12]
target = 2
print(search(nums,target))