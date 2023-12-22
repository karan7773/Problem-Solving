def isRobotBounded(instructions):
    d,dx,dy=0,0,0
    for i in instructions:
        if i=="L":
            d-=90
        elif i=="R":
            d+=90
        else:
            if d==0:
                dy+=1
            elif d==90 or d==-270:
                dx+=1
            elif d==-90 or d==270:
                dx-=1
            else:
                dy-=1
        d%=360
    return d!=0 or (dx==0 and dy==0)
        
        
print(isRobotBounded("GGLLGG"))
print(isRobotBounded("GG"))
print(isRobotBounded("GL"))