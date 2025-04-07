ans = 1001
for i in range(int(input())):
    a,b = map(int, input().split())
    if b-a <= ans and b>=a:
        ans = b
if ans != 1001:
    print(ans)
else:
    print(-1)