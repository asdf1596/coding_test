import sys
a,b = map(int, sys.stdin.readline().split())
if a%b==0:
    print("Yes")
else:
    print("No")