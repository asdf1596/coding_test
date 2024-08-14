import sys
a = int(input())
li1 = set(map(int, sys.stdin.readline().split()))
b = int(input())
li2 = list(map(int, sys.stdin.readline().split()))
for i in range(len(li2)):
    if li2[i] in li1:
        print(1)
    else:
        print(0)