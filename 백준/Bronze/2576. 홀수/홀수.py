li1 = []
for i in range(7):
    a = int(input())
    if(a%2==1):
        li1.append(a)
if(len(li1)==0):
    print(-1)
else:
    li1.sort()
    print(sum(li1))
    print(li1[0])