a,b = map(int, input().split())
li1 = [[0,0] for i in range(6)]
ans = 0
for i in range(a):
    c,d= map(int, input().split())
    li1[d-1][c]+=1
for i in range(len(li1)):
    for j in range(2):
        if(li1[i][j] > 0):
            ans+=li1[i][j]//b
            if(li1[i][j]%b != 0):
                ans+=1
print(ans)