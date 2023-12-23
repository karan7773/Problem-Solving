def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
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
    return low

print(searchInsert([1,3,5,6],5))
print(searchInsert([1,3,5,6],2))
