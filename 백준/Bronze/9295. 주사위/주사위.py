a = int(input())
li1 = []
for i in range(a):
    c,d = map(int, input().split())
    li1.append([c,d])
for i in range(a):
    print("Case",str(i+1)+":", li1[i][0]+li1[i][1])