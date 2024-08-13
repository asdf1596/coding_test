a,b = map(int, input().split())
li1 = []
for i in range(a):
    li1.append(list(map(int, input().split())))
e = int(input())
c,d = a-2,b-2
li2 = []
li3 = []
for i in range(1,c+1):
    for j in range(1,d+1):
        for k in range(-1,2):
            for l in range(-1,2):
                li2.append(li1[i+k][j+l])
        li2.sort()
        #print(li2)
        li3.append(li2[4])
        li2 = []
ans = 0
for i in li3:
    if i>=e:
        ans+=1
print(ans)