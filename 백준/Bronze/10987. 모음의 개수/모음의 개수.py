a = list(input())
ans = 0
for i in ['a','e','i','o','u']:
    for j in a:
        if i == j:
            ans+=1
print(ans)