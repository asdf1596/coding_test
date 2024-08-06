import sys
from collections import deque
input = sys.stdin.readline
a= int(input())
li1 = deque(list(map(int, input().split())))
c,d = li1.popleft(),li1.pop()
if c>d:
    b = c
else:
    b = d
print(b-(a-2))