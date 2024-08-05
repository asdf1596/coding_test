a,b = map(int, input().split())
c = b//2 if b%2==0 else b//2+1
ans = 0
for i in range(a):
    li1 = list(input())
    if li1.count("O") >= c:
        ans+=1
print(ans)