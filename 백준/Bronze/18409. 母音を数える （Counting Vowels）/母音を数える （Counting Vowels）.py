a = int(input())
li1 = list(input())
ans = 0
for i in li1:
    if i in ['a','i','u','o','e']:
        ans+=1
print(ans)