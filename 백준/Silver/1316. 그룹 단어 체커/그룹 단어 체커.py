a = int(input())
ans= 0
for i in range(a):
    pro = False
    li2 = list(input())
    li1 = [li2[0]]
    for j in range(1, len(li2)):
        if(li2[j] != li1[-1]):
            li1.append(li2[j])
    #print(li1)
    for j in range(len(li1)):
        #print(li1[j] ,li1[0:j], li1[j+1:])
        if li1[j] in li1[0:j] or li1[j] in li1[j+1:]:
            pro = True
            #print("pro")
    if not pro:
        ans+=1
print(ans)