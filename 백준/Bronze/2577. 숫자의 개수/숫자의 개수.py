try1 = 1
for i in range(3):
    try1*=(int(input()))
li1 = list(str(try1))
li2 = [0 for a in range(10)]
for i in range(len(li1)):
    li2[int(li1[i])]+=1
for i in li2:
    print(i)