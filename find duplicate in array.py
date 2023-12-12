arr=[1,4,6,8,4,3,2]

for i in range(len(arr)):
    for j in range(1,i+1):
        if arr[i]==arr[j]:
            print(arr[j])
            break
