a = int(input())
li1 = list(map(int, input().split()))
ans = 0
for i in li1:
    if i < a:
        ans+=i
    else:
        ans+=a
print(ans)