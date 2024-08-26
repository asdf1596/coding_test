import sys
import math
a, b = map(int, sys.stdin.readline().split())
li1 = [True] * (b - a + 1)
if a == 1:
    li1[0] = False
for i in range(2, int(math.sqrt(b)) + 1):
    start = max(i * i, (a + i - 1) // i * i)
    for j in range(start, b + 1, i):
        li1[j - a] = False
for i in range(a, b + 1):
    if li1[i - a]:
        print(i)