a,b,c = map(int, input().split())
d,e,f = map(int, input().split())
if 100*b+c > 100*e+f:
    print(d-a-1)
else:
    print(d-a)
print(d-a+1)
print(d-a)