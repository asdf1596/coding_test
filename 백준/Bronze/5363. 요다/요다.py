li1 = []
a = int(input())
for i in range(a):
    li1.append(input().split())
for i in li1:
    i.append(i[0])
    i.append(i[1])
    i = i[2:]
    for j in range(len(i)):
        print(i[j], end=" ")
    print("")