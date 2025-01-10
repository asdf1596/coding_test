import sys
a = int(sys.stdin.readline().strip())
b = a-1
c = 0
for i in range(a):
    c+=int(sys.stdin.readline().strip())
c-=b
print(c)