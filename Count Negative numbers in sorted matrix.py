def countNegatives(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    r=len(grid)
    c=len(grid[0])
    count=0
    for i in range(r):
        for j in range(c):
            if grid[i][j]<0:
                count+=1
    return count
    
print(countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
print(countNegatives([[3,2],[1,0]]))