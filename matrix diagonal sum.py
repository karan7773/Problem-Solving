def diagonalSum(mat):
    s=0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i==j:
                s+=mat[i][j]
            elif (i+j)==(len(mat)-1):
                s+=mat[i][j]
    return s
mat1 = [[1,2,3],[4,5,6],[7,8,9]]
mat2 = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
print(diagonalSum(mat1))
print(diagonalSum(mat2))