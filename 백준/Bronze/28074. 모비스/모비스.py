a = list(input())
li1 = ["M","O","B","I","S"]
ans = 0
for i in li1:
    if i in a:
        ans+=1
if ans==5:
    print("YES")
else:
    print("NO")