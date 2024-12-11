li1 = []
for i in range(9):
    for j in list(map(int, input().split())):
        li1.append(j)
print(max(li1))
print(li1.index(max(li1))//9+1, li1.index(max(li1))%9+1)