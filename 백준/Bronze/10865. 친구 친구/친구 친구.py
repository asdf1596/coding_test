import sys
a,b = map(int, sys.stdin.readline().split())
li1 = [0 for i in range(a)]
for i in range(b):
    c,d = map(int, sys.stdin.readline().split())
    li1[c-1]+=1
    li1[d-1]+=1
t = [print(i) for i in li1]