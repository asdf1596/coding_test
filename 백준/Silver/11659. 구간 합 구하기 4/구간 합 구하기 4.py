import sys
a,b  = map(int, sys.stdin.readline().split())
li1 = list(map(int, sys.stdin.readline().split()))
li2 = [li1[0]]
for i in range(1, len(li1)):
    li2.append(li1[i]+li2[-1])
for i in range(b):
    c,d = map(int, sys.stdin.readline().split())
    if c!=1:
        print(li2[d-1]-li2[c-2])
    else:
        print(li2[d-1])