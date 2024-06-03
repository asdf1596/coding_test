import sys
input = sys.stdin.readline
a= input()
a= int(a)
c = []
z =input().split()
d = input()
c.append(z)
e= 0 
for i in c[0]:
    if int(i) == int(d):
        e+=1
print(e)