a = int(input())
li1 = {}
ans=0
for i in range(a):
    b,c = map(int, input().split())
    if b in li1:
        d = li1[b]
        if d != c:
            li1[b] = c
            ans+=1
    else:
        li1[b] = c
print(ans)