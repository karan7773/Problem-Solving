def rotate(arr):
    r=len(arr)

    #transpose matrix
    for i in range(r):
        for j in range(i):
            arr[i][j],arr[j][i]=arr[j][i],arr[i][j]

    #reverse each row
    for i in range(r):
        arr[i].reverse()

    return arr

arrr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

arr=rotate(arrr)
for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j],end=" ")
    print()
