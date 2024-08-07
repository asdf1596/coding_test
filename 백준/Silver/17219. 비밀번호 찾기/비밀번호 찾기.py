import sys
a,b = map(int, sys.stdin.readline().split())
li1 = {}
for i in range(a):
    c,d = sys.stdin.readline().split()
    li1[c]=d
for i in range(b):
    e = input()
    print(li1[e])