a = int(input())
b = int(input())
li1 = []
for i in range(a, b+1):
    if((i**0.5)%1 == 0.0):
        li1.append(i)
if(len(li1) == 0):
    print(-1)
else:
    print(sum(li1))
    print(min(li1))