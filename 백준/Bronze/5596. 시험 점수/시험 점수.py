a,b,c,d = map(int, input().split())
q,w,e,r = map(int, input().split())
if(a+b+c+d < q+w+e+r):
    print(q+w+e+r)
else:
    print(a+b+c+d)