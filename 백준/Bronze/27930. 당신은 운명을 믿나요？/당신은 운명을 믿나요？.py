a = list(input())
li1 = ["K","O","R","E","A"]
li2 = ["Y","O","N","S","E","I"]
li3 = []
li4 = []
try1 = 0
try2 = 0
for i in a:
    if i == li1[try1]:
        li3.append(i)
        try1+=1
    if i == li2[try2]:
        li4.append(i)
        try2+=1
    if len(li3)==5 or try1 == 5:
        print("KOREA")
        break
    elif len(li4) == 6 or try2 == 6:
        print("YONSEI")
        break