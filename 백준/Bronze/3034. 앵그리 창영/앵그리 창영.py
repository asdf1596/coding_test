import math
a,b,c = map(int, input().split())
li1 = []
for i in range(a):
    li1.append(int(input()))
try1 = int(math.sqrt(b**2+c**2))
for i in li1:
    if(i <= try1):
        print("DA")
    else:
        print("NE")