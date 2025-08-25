a,b = map(int, input().split())
if a%4==0:
    d = 4
    c = a//4
else:
    d = a%4
    c = a//4+1
if b%4==0:
    f = 4
    e = b//4
else:
    f = b%4
    e = b//4+1
print(abs(c-e)+abs(d-f))