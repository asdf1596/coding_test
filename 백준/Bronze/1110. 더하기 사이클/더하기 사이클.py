a = int(input())
ans = a
try1 = 0
b, c = 0, 0
if(a < 10):
    try1+=1
    a *=11
while(True):
    
    b = int(a/10)
    c = a%10
    d = b+c
    if(d>=10):
        d= d%10
    a = 10*c+d
    #print(a)
    try1+=1
    if(try1 > 100 or ans == a):
        break
if(ans == 0):
    try1 = 1
print(try1)