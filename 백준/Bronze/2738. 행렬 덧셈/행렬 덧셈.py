a,b = map(int, input().split())
li1 = []
for i in range(a*2):
    li1.append(list(map(int, input().split())))
for i in range(a):
    for k in range(b):
        li1[i][k]+=li1[i+a][k]
for i in range(a):
    for j in range(b):
        print(li1[i][j], end= " ")
    print("")