a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
li1 = []
li1.append(a*e)
if(c<e):
    li1.append(b+(e-c)*d)
else:
    li1.append(b)
print(min(li1))