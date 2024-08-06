a,b,c= map(int, input().split())
d = int(input())
if d > 3600:
    a+=d//3600
    d%=3600
if d > 60:
    b+=d//60
    d%=60
c+=d
if c > 59:
    b+=c//60
    c%=60
if b > 59:
    a+=b//60
    b%=60
if a> 23:
    a%=24
print(a,b,c)