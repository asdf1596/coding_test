li1 = list(map(int, input().split()))
a, b = li1[0], li1[1]
ans = [c for c in range(1, a+1)]
li1 = []
try1 = 0
def change(li2):
    global ans
    if(li2[0] != li2[1]):
        try1 = ans[li2[0]]
        ans[li2[0]] = ans[li2[1]]
        ans[li2[1]] = try1
    #print(ans)
for i in range(b):
    li1.append(list(map(int, input().split())))
    li1[i][0]-=1
    li1[i][1]-=1
for i in li1:
    change(i)
z = [print(c, end=" ") for c in ans]