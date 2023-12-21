def addBinary(a, b):
    carry=0
    res=''
    a=list(a)
    b=list(b)
    while a or b or carry:
        if a:
            carry +=int(a.pop())
            # print(carry)
        if b:
            carry +=int(b.pop())
            # print(carry)
        res += str(carry%2)
        carry//=2
        # print( res)
    return res[::-1]   

print(addBinary("11","1"))
print(addBinary("1010","1011"))