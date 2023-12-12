# find the value at perticular row and col in pascal triangle
def FindValNcR(r,c):
    res=1
    for i in range(c):
        res=res*(r-i)
        res=res/(i+1)
    return res

row=6
col=3
ans = FindValNcR(row-1,col-1)
print(int(ans))


#print the row of the pascal triangle of given row
def getRow(row):
        ansList=[0]*(row+1)
        ans=1
        ansList[0]=ans
        for i in range(1,row+1):
            ans=ans*((row+1)-i)
            ans=ans/(i)
            ansList[i]=int(ans)
        return ansList
row=3
print(getRow(row))

#print the pascal triangle for given number of rows
result=[]
for i in range(6):
    result.append(getRow(i))
print(result)