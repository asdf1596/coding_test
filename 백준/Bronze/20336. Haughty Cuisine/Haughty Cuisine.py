import sys
n = int(sys.stdin.readline())
li = [sys.stdin.readline().rstrip().split() for _ in range(n)]
for i in li[0]:
    print(i)