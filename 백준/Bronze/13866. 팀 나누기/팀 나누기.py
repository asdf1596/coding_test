import sys
sum = 0
a,b,c,d = map(int, sys.stdin.readline().split())
print(abs((a+d)-(c+b)))