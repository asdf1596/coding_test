import sys
a = int(sys.stdin.readline().strip())
for i in range(a):
    print("Case #"+str(i+1)+": "+str(max(list(map(int, sys.stdin.readline().split())))))