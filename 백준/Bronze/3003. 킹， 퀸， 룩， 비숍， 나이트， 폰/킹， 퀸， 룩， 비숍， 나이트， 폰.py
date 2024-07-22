li1 = list(map(int, input().split()))
li2 = [1,1,2,2,2,8]
li3 = []
for i in range(len(li1)):
    li3.append(li2[i]-li1[i])
for i in li3:
    print(i, end = " ")