arr=[1,0,2,0,2,1]
col0=0
col1=0
col2=0
for i in range(len(arr)):
    if arr[i]==0:
        col0+=1
    elif arr[i]==1:
        col1+=1
    else :
        col2+=2

for i in range(col0):
    arr[i]=0
for i in range(col0,col0+col1):
    arr[i]=1
for i in range(col1+col0,len(arr)):
    arr[i]=2

print(arr)

# print(arr[2:])

#dutch national flag algorithm

def swap(arr,a,b):
    t=arr[a]
    arr[a]=arr[b]
    arr[b]=t
    return arr

arr=[2,0,2,1,1,0]

low=0
mid=0
high=len(arr)-1
n=len(arr)
for i in range(n):
    if arr[mid]==0:
        arr=swap(arr,low,mid)
        low+=1
        mid+=1
    elif arr[mid]==1:
        mid+=1
    elif arr[mid]==2:
        arr=swap(arr,mid,high)
        high-=1

print(arr)