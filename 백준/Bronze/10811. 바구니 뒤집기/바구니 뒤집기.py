li1 = list(map(int, input().split()))
a, b = li1[0], li1[1]
ans = [c for c in range(1, a+1)]
li1 = []
try1 = 0
def change(li2):
    #print(li2)
    global ans
    try2 = 0
    li3 = ans[li2[0]:li2[1]+1]
    li2 = [c for c in range(li2[0], li2[1]+1)]
    #print(li3)
    li4 = []
    for j in range(len(li3)):
        li4.append(li3[len(li3)-j-1])
    for j in li2:
        #print(j)
        ans[j] = li4[try2]
        try2+=1
    #print(li4, ans)
    return li4
for i in range(b):
    li1.append(list(map(int, input().split())))
    li1[i][0]-=1
    li1[i][1]-=1
for i in li1:
    change(i)
z = [print(c, end=" ") for c in ans]