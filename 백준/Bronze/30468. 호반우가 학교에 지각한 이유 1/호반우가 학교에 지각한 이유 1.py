a,b,c,d,e = map(int, input().split())
f = e*4
if (a+b+c+d)<=f:
    print(f-(a+b+c+d))
else:
    print(0)