a = int(input())
li1=(list(input()))
li2 = ["H","I","R","A","C"]
li3 = [0,0,0,0,0]
for i in li1:
    for j in range(len(li2)):
        if(i==li2[j]):
            li3[j]+=1
            break
print(min(li3))