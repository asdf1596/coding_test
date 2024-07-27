set1 = set()
a = int(input())
for i in range(a):
    set1.add(input())
li1 = list(set1)
li1.sort(key=len)
li2 = [[li1[0]]]
for i in range(1,len(li1)):
    if len(li1[i]) != len(li1[i-1]):
        li2.append([])
        li2[-1].append(li1[i])
    else:
        li2[-1].append(li1[i])
for i in range(len(li2)):
    li2[i] = sorted(li2[i])
for i in li2:
    for j in i:
        print(j)