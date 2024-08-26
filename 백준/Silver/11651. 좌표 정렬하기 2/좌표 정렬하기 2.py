import sys
a = int(sys.stdin.readline())
li1=[]
for i in range(a):
    b,c = map(int, sys.stdin.readline().split())
    li1.append([b,c])
li1.sort(key=lambda x:(x[1], x[0]))
for i,j in li1:
    print(i,j)