import sys
a,b = map(int, input().split())
li1 = {}
li2 = {}
for i in range(a):
    d = str(sys.stdin.readline().strip())
    li1[str(i+1)] = d
    li2[d] = str(i+1)
for i in range(b):
    c = str(sys.stdin.readline().strip())
    if c in li1:
        print(li1[c])
    else:
        print(li2[c])