# import sys
def maxSubarraySum(nums,n):
    maxi=nums[0]
    summ=0
    for i in range(n):
        summ+=nums[i]

        if summ>maxi:
            maxi=summ
        if summ<0:
            sum=0
    return maxi

arr = [-2,1,-3,4,-1,2,1,-5,4] 
n = len(arr)
maxSum = maxSubarraySum(arr, n)
print("The maximum subarray sum is:", maxSum)
# l=len(arr)
# for i in range(l):
#     summ=0
#     for j in range(i+1):
#         summ+=arr[j]
#         print(summ)