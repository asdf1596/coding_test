import sys
a = int(sys.stdin.readline().strip())
li1 = list(map(int, sys.stdin.readline().strip().split()))
b = int(sys.stdin.readline().strip())
li2 = list(map(int, sys.stdin.readline().strip().split()))
li1 = set(li1)
li3 = []
for i in li2:
    if i in li1:
        print(1, end = " ")
    else:
        print(0, end = " ")