import sys
a = sys.stdin.readline()
li1 = list(map(int, sys.stdin.readline().split()))
ans = 0
b = len(li1)
li1.sort()
c= 0
for i in range(int(a)):
    ans+=li1[i]*i-c
    c += li1[i]
print(ans*2)