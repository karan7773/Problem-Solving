def countOdds(low, high):
    count=(high-low)//2
    if high%2!=0 or low%2!=0:
        count+=1        
    return count

print(countOdds(7,9))
print(countOdds(9,10))
print(countOdds(3,7))