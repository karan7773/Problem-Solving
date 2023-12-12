def merge(nums1, n, nums2, m):
    nums3=[0]*(m+n)
    l=0
    r=0
    index=0

    #compare the value and add to new list from both lists
    while l<n and r<m:
        if nums1[l]<=nums2[r]:
            nums3[index]=nums1[l]
            index+=1
            l+=1
        else:
            nums3[index]=nums2[r]
            index+=1
            r+=1

    #add the balence elements to array
    while l<n:
        nums3[index]=nums1[l]
        index+=1
        l+=1

    while r<m:
        nums3[index]=nums2[r]
        index+=1
        r+=1
    #save both array with the values of new array
    for i in range(m+n):
        if i<n:
            nums1[i]=nums3[i]
        else:
            nums2[i-n]=nums3[i]

    print(nums1,nums2)

n = 4
arr1 = [1, 4, 8, 10] 
m = 3
arr2 = [2,3,9]
merge(arr1,n,arr2,m)