import math
a = int(input())
li1 = []
for i in range(a):
    li1.append(list(map(int, input().split())))
for x1,y1,r1,x2,y2,r2 in li1:
    r3 = math.sqrt((x1-x2)**2+(y1-y2)**2)
    if(x1 == x2 and y1 == y2 and r1==r2):
        print(-1)
    elif(r1+r2 < r3 or abs(r1-r2) > r3 or (x1==x2 and y1==y2 and r1!=r2)):
        print(0)
    elif(r1+r2 == r3 or abs(r1-r2) == r3):
        print(1)
    elif(abs(r1-r2)<r3<r1+r2):
        print(2)