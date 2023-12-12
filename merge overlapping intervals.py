arr=[[1,3],[2,6],[8,10],[15,18]]
n=len(arr)
#to group them sorting is done
arr.sort()
ans=[]
for i in range(n):
    start,end=arr[i][0],arr[i][1]

    #checks if the previous list value in index 1 is less than end and ans is not empty
    if ans and end<=ans[-1][1]:
        continue

    for j in range(i+1,n):
        #checks if the start value is less than end if so then the max of them is saved in end orelse break
        if arr[j][0]<=end:
            end=max(end,arr[j][1])
        else:
            break
    #append the list to ans
    ans.append([start,end])

for i in ans:
    print(i)