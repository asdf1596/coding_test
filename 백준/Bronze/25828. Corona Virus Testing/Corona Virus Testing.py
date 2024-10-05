a, b, c = map(int, input().split())
d = a+b*c
e = a*b
if e<d:
    print(1)
elif d<e:
    print(2)
else:
    print(0)