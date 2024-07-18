a = list(input())
li1 = [3,3,3,3,3,4,3,4]
li2 = []
try1 = 65
ans = 0
for i in range(len(li1)):
    li2.append([])
    for j in range(1,li1[i]+1):
        li2[i].append(chr(try1))
        try1+=1
for i in a:
    for j in range(len(li2)):
        if(i in li2[j]):
            #print(li2[j])
            ans = ans+j+3
print(ans)