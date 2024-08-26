import sys
a = int(sys.stdin.readline())
li1 = {}
for i in range(a):
    b = int(sys.stdin.readline())
    if b in li1.keys():
        li1[b]+=1
    else:
        li1[b]=1
li2 = sorted(list(li1.keys()))
for i in li2:
    for j in range(li1[i]):
        print(i)