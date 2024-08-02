a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if(b%d==0):
    f = int(b/d)
else:
    f = b//d+1
if(c%e==0):
    g = int(c/e)
else:
    g = c//e+1
if f>g:
    print(a-f)
else:
    print(a-g)