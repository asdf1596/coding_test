a = int(input())
li1 = list(map(int, input().split()))
b, c = map(int, input().split())
ans = a
for i in range(a):
    if(li1[i]-b>0):
        li1[i]-=b
        ans+=(li1[i]//c)
        if(li1[i]%c!=0):
            ans+=1
print(ans)
        