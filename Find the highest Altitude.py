def largestAltitude( gain):
    m=0
    c=0
    for i in gain:
        c+=i
        if m<c:
            m=c
    return m

print(largestAltitude([-5,1,5,0,-7]))
print(largestAltitude([-4,-3,-2,-1,4,3,2]))