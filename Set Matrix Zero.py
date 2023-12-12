#brute force
def makerow0(mat,r,c,i):
    for j in range(c):
        if mat[i][j]!=0:
            mat[i][j]=-1
        
def makecol0(mat,r,c,j):
    for i in range(r):
        if mat[i][j]!=0:
            mat[i][j]=-1

mat=[[1,1,1],[1,0,1],[1,1,1]]

r=len(mat)
c=len(mat[0])

for i in range(r):
    for j in range(c):
        if mat[i][j]==0:
            makerow0(mat,r,c,i)
            makecol0(mat,r,c,j)

for i in range(r):
    for j in range(c):
        if(mat[i][j])==-1:
            mat[i][j]=0

print(mat)


#better
def setZeroes(matrix):
        r=len(matrix)
        c=len(matrix[0])

        row=[0] * r
        col=[0] * c

        for i in range (r):
            for j in range(c):
                if matrix[i][j]==0:
                    row[i]=1
                    col[j]=1
        
        for i in range(r):
            for j in range(c):
                if row[i]==1 or col[j]==1:
                    matrix[i][j]=0

matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setZeroes(matrix)
print(matrix)
