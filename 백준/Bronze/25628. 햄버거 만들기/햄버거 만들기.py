a,b = map(int, input().split())
if a%2==1:
    a-=1
print(a//2 if a//2 < b else b)