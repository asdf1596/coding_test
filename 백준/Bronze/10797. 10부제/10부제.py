a = int(input())
li1 = map(int, input().split())
ans = 0
for i in li1:
    if a == i:
        ans+=1
print(ans)