a,b,c,d = map(int, input().split())
x,y,r = map(int, input().split())
li1 = [a,b,c,d]
ans = 0
for i in range(len(li1)):
    if li1[i] == x:
        ans = i+1
print(ans)