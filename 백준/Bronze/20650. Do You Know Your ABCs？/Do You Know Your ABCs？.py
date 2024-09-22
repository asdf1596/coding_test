li1 = list(map(int, list(input().split())))
li1.sort()
a = li1[0]
b = li1[1]
C = li1[-1]
c = C-(a+b)
print(a,b,c)