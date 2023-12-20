def lemonadeChange(bills):
    if bills[0]==10 or bills[0]==20:
        return False
    a,b,c=0,0,0
    for i in bills:
        if i==5:
            a+=1
        elif i==10:
            b+=1
            a-=1
        else:
            if b>0 and a>0:
                b-=1
                a-=1
            elif a>2:
                a-=2
            else:
                return False
    return True

print(lemonadeChange([5,5,5,10,20]))
print(lemonadeChange([5,5,10,10,20]))
