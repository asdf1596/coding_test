a,b,c = map(int, input().split())
d,e = 0, 0
if a//c == a/c:
    d+=a//c
else:
    d+=a//c
    d+=1
if b//c == b/c:
    e+=b//c
else:
    e+=b//c
    e+=1
print(e*d)