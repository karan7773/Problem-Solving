def calPoints(operations):
    l=[]
    for j in range(len(operations)):
        if operations[j]=="C":
            l.pop()
        elif operations[j]=="D":
            l.append(l[-1]*2)
        elif operations[j]=="+":
            l.append(l[-1]+l[-2])
        else:
            l.append(int(operations[j]))
    return sum(l)

print(calPoints(["5","2","C","D","+"]))
print(calPoints(["5","-2","4","C","D","9","+","+"]))