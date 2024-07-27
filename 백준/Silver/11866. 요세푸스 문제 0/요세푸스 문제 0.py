a,b = map(int, input().split())
li1 = [a+1 for a in range(a)]
li2 = []
c = b-1
while len(li1) != 0:
    for i in range(b):
        li1.append(li1[0])
        li1 = li1[1:]
    li2.append(li1.pop())
print("<",end = "")
for i in li2:
    if i != li2[-1]:
        print(str(i)+", ",end = "")
    else:
        print(str(i),end = "")
print(">")