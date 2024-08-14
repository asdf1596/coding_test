import sys
a = int(input())
li1 = list(map(int, sys.stdin.readline().split()))
li1.sort()
ans=0
b=0
for i in li1:
    b+=i
    ans+=b
print(ans)