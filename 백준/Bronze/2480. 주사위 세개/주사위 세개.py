a,b,c = map(int, input().split())
if(a==b==c):
    print(10000+(a*1000))
elif(a==b or b==c or a==c):
    if(a==b or a==c):
        print(1000+(a*100))
    else:
        print(1000+(b*100))
else:
    d = max([a,b,c])
    print(d*100)