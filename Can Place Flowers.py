def canPlaceFlowers(flowerbed, n):
    c=1
    ans=0
    for i in flowerbed:
        if i==0:
            c+=1
        else:
            ans+=(c-1)//2
            c=0
    return ans+c//2>=n

print(canPlaceFlowers([1,0,0,0,1],1))
print(canPlaceFlowers([1,0,0,0,1],2))