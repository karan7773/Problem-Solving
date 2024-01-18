def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    prev,val=1,1
    for i in range(1,n):
        prev,val=val,val+prev
    return val

print(climbStairs(2))
print(climbStairs(8))