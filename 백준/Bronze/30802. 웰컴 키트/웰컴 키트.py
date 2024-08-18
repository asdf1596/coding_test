a = int(input())
li1 = list(map(int, input().split()))
b,c = map(int, input().split())
ans=0
for i in li1:
    if i%b==0:
        ans+=i//b
    else:
        ans+=i//b+1
print(ans)
if a%c==0:
    print(a//c, 0)
else:
    print(a//c, a%c)