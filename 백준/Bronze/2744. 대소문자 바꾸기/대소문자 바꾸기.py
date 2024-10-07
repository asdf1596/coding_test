a = list(input())
ans = ""
for i in a:
    if i.isupper():
        ans+=i.lower()
    else:
        ans+=i.upper()
print(ans)