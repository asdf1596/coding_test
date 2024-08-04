from collections import deque
z = int(input())
for _ in range(z):
    input()
    a,b = map(int, input().split())
    li1 = list(map(int, input().split()))
    li2 = list(map(int, input().split()))
    li1.sort()
    li2.sort()
    li1 = deque(li1)
    li2= deque(li2)
    while len(li1)!=0 and len(li2)!=0:
        x,y = li1.popleft(),li2.popleft()
        #print("x,y",x,y)
        if x == y or x > y:
            li1.appendleft(x)
        elif x < y:
            li2.appendleft(y)
        #print(li1,li2)
    if len(li1)==0:
        print("B")
    else:
        print("S")