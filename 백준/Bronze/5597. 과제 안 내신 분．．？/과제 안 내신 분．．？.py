li1 = [a for a in range(1,31)]
for i in range(28):
    a = int(input())
    li1.remove(a)
li1.sort()
print(li1[0])
print(li1[1])