import sys
from collections import deque
a = int(sys.stdin.readline())
for i in range(a):
    b,c = map(int ,sys.stdin.readline().split())
    li1 = list(map(int, sys.stdin.readline().split()))
    li1 = deque(li1)
    pre = c
    Max = max(li1)
    d = li1.popleft()
    ans = 1
    while pre!=0 or d != Max:
        #print(li1, pre, ans)
        if d == Max:
           ans+=1
           Max = max(li1)
           pre-=1
        else:
            if pre == 0:
                pre = len(li1)
            else:
                pre-=1
            li1.append(d)
        d = li1.popleft()
    print(ans)