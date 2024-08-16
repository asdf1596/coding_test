from collections import deque
import sys
a = int(input())
li1 = deque([])
for  i in range(a):
    b = sys.stdin.readline().split()
    if len(b)==1:
        b = b[0]
        if b=="back":
            if len(li1)!=0:
                c = li1.popleft()
                print(c)
                li1.appendleft(c)
            else:
                print(-1)
        elif b=="front":
            if len(li1)!=0:
                c = li1.pop()
                print(c)
                li1.append(c)
            else:
                print(-1)
        elif b=="empty":
            if len(li1)==0:
                print(1)
            else:
                print(0)
        elif b=="size":
            print(len(li1))
        elif b=="pop":
            if len(li1)==0:
                print(-1)
            else:
                print(li1.pop())
    else:
        b,c = b[0],b[1]
        if b == "push":
            li1.appendleft(c)