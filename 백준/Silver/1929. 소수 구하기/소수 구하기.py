import sys
from collections import deque
a,b = map(int, sys.stdin.readline().split())
li1 = [i for i in range(a,b+1) if (i%2==1 or i==2) and i!=1]
li1 = deque(li1)
if a==b and b==1:
    print("")
else:
    for i in range(3,int(b**(1/2))+1,2):
        for j in range(len(li1)):
            c = li1.popleft()
            if c%i!=0 or c==i:
                li1.append(c)
    for i in range(len(li1)):
        print(li1.popleft())