import sys
a = int(sys.stdin.readline())
for i in range(a):
    b = (sys.stdin.readline().strip())
    if b[-1] != ".":
        print(b+".")
    else:
        print(b)
