def judgeCircle(moves):
    ip=[0,0]
    n=len(moves)
    for i in range(n):
        if moves[i]=="U":
            ip[1]+=1
        elif moves[i]=="D":
            ip[1]-=1
        elif moves[i]=="L":
            ip[0]-=1
        else:
            ip[0]+=1
    if ip==[0,0]:
        return True
    return False

print(judgeCircle("UU"))
print(judgeCircle("UD"))
print(judgeCircle("RR"))
print(judgeCircle("RL"))