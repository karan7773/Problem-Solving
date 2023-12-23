def nextGreatestLetter(letters, target):
    """
    :type letters: List[str]
    :type target: str
    :rtype: str
    """
    ans=[]
    c=0
    n=len(letters)
    for i in range(0,n):
        if letters[i]>target:
            ans.append(letters[i])
            break
        else:
            c+=1
            continue
    if c==n:
        return letters[0]
    return ans[0]
        
print(nextGreatestLetter(["c","f","j"],"a"))
print(nextGreatestLetter(["c","f","j"],"c"))