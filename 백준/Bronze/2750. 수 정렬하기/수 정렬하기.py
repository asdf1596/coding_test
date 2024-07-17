a = int(input())
li1 = []
for i in range(a):
    b = int(input())
    if(b not in li1):
        li1.append(b)
li1.sort()
c = [print(d) for d in li1]