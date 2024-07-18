a = int(input())
ans = 0
a = 1000-a
if(a>=500):
    b = a//500
    ans+=b
    a -= 500*b
if(a>=100):
    b = a//100
    ans+=b
    a -= 100*b
if(a>=50):
    b = a//50
    ans+=b
    a -= 50*b
if(a>=10):
    b = a//10
    ans+=b
    a -= 10*b
if(a>=5):
    b = a//5
    ans+=b
    a -= 5*b
if(a>0):
    ans+=a
print(ans)