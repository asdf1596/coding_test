z = int(input())
li1 = []
for _ in range(z):
    a,b,c = map(int, input().split())
    li1.append([a,b,c])
li1.sort(key= lambda x:x[2], reverse=True)
li2 = [0 for i in range(max([li1[i][0] for i in range(len(li1))]))]
for i in li1:
    if li2[i[0]-1] <=1:
        print(i[0], i[1])
        li2[i[0]-1]+=1
    if sum(li2) == 3:
        break
    