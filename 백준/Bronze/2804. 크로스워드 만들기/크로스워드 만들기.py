li1,li2 = input().split()
li1,li2 = list(li1), list(li2)
a,b = "",""
for i in li1:
    for j in li2:
        if i ==j:
            a = i
            b = j
            break
    if a!="":
        break
li3 = [["." for _ in range(len(li1))] for i in range(len(li2))]
c,d = li1.index(a), li2.index(b)
li3[d] = [i for i in li1]
for i in range(len(li2)):
    li3[i][c] = li2[i]
for i in range(len(li2)):
    for j in range(len(li1)):
        print(li3[i][j], end="")
    print("")