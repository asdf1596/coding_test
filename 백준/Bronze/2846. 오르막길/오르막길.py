a = int(input())
li2 = list(map(int, input().split()))
li1 = [[li2[0]]]
before = li2[0]
for i in li2:
    if i > before:
        li1[-1].append(i)
    else:
        li1.append([i])
    before = i
li1 = li1[1:]
li3 = []
for i in li1:
    li3.append(i[-1]-i[0])
print(max(li3))