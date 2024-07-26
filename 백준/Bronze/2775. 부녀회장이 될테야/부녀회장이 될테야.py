a = int(input())
li1 = []
for i in range(a):
    b = int(input())
    c = int(input())
    li1.append([b,c])
for i in li1:
    li2 = [a for a in range(1,i[1]+1)]
    ans = 0
    for j in range(i[0]):
        for k in range(i[1]-1,0,-1):
            li2[k] = sum(li2[0:k+1])
            #print(li2)
    print(li2[i[1]-1])