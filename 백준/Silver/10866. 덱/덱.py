import sys
from collections import deque
z = int(sys.stdin.readline())
li1 = deque()
for _ in range(z):
    a = sys.stdin.readline().strip().split()
    if len(a) == 1:
        a,b = a,0
        a = a[0]
    else:
        a,b = a[0],a[1]
        b = int(b)
    if a == "push_front":
        li1.append(b)
    elif a == "push_back":
        li1.appendleft(b)
    elif a == "pop_front":
        if len(li1) !=0:
            print(li1.pop())
        else:
            print(-1)
    elif a == "pop_back":
        if len(li1) !=0:
            print(li1.popleft())
        else:
            print(-1)
    elif a == "size":
        print(len(li1))
    elif a == "empty":
        if len(li1) == 0:
            print(1)
        else:
            print(0)
    elif a == "front":
        if len(li1) !=0:
            b = li1.pop()
            print(b)
            li1.append(b)
        else:
            print(-1)
    elif a == "back":
        if len(li1) !=0:
            b = li1.popleft()
            print(b)
            li1.appendleft(b)
        else:
            print(-1)
    #print(li1)