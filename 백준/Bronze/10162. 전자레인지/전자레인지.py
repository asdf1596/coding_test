a,b,c = 0,0,0
d = int(input())
ans = 0
if(d%10 != 0):
    print(-1)
else:
    if(d>=300):
        a+=d//300
        d%=300
    if(d>=60):
        b+=d//60
        d%=60
    if(d>=10):
        c+=d//10
        d%=10
    print(a,b,c)