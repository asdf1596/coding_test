a = int(input())
ans = 0
for i in range(a):
    b,c = input().split("-")
    if int(c)<=90:
        ans+=1
print(ans)