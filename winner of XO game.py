def tictactoe(moves):
    a,b=[0]*8,[0]*8
    for i in range(len(moves)):
        r,c=moves[i]
        if i%2==0:
            player=a
        else:
            player=b
        player[r]+=1
        player[c+3]+=1
        if r==c:
            player[6]+=1
        if r==2-c:
            player[7]+=1
    
    for i in range(len(a)):
        if a[i]==3:
            return "A"
        elif b[i]==3:
            return "B"
    
    if len(moves)==9:
        return "Draw"
    else:
        return "Pending"
print(tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))
print(tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]))