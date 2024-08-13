a = int(input())
li1 = list(input())
for i in range(a-1):
    li2 = list(input())
    if len(li1) > len(li2):
        for i in range(len(li2)):
            if li1[i] != li2[i]:
                li1[i] = "?"
    else:
        for i in range(len(li1)):
            if li1[i] != li2[i]:
                li1[i] = "?"
for i in li1:
    print(i,end="")