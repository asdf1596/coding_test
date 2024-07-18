chess=[]
for i in range(8):
    chess.append(list(input()))
check = 0
ans = 0
for i in range(8):
    for j in range(8):
        if(check%2==0):
            if(j%2==0 and chess[i][j] == "F"):
                ans+=1
        else:
            if(j%2==1 and chess[i][j] == "F"):
                ans+=1
    check+=1
print(ans)