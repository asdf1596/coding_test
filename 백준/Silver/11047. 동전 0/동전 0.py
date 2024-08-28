import sys
a, b = map(int, sys.stdin.readline().split())
li1 = []
for i in range(a):
    c = int(sys.stdin.readline())
    if c <= b:
        d = i
    li1.append(c)
ans = 0
for j in range(i, -1, -1):
    f=(b//li1[j])
    ans+=f
    b-=(f*li1[j])
    if b==0:
        break
print(ans)