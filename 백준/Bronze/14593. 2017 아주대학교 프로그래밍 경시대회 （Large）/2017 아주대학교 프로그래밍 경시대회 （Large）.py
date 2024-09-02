import sys
a = int(sys.stdin.readline())
li1 = []
for i in range(a):
    b,c,d = map(int, sys.stdin.readline().split())
    li1.append([b,c,d, i])
li1.sort(key= lambda x : (x[0], -x[1], -x[2]), reverse=True)
print(li1[0][3]+1)