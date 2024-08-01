li1 = []
for i in range(6):
    li1.append(int(input()))
li2 = li1[4:6]
li1 = li1[0:4]
li1.sort()
li2.sort()
print(li1[3]+li1[2]+li1[1]+li2[1])