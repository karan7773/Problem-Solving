price=[7,1,5,3,6,4]
maxprofit=0
profit=price[0]

for i in range(1,len(price)):
    if profit>price[i]:
        profit=price[i]
    if(price[i]-profit>maxprofit):
        maxprofit=price[i]-profit

print(maxprofit)