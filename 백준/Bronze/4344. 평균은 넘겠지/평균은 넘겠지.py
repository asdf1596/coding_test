a = int(input())
for _ in range(a):
    c = input().split()
    b = int(c[0])
    c = [int(d) for d in c[1:]]
    d = 0
    for i in c:
        d+=i
    avr = d/b
    ans = 0
    for i in c:
        if(avr < i):
           ans+=1 
    print("%.3f"%(ans/b*100)+"%")