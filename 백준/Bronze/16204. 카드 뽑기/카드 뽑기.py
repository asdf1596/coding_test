a ,b,c = map(int, input().split())
if b == c:
    print(a)
else:
    d = b if b<c else c
    e = (a-b) if (a-b)<a-c else a-c
    print(d+e)