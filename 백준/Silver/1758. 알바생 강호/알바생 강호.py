a = int(input())
ans = 0
li1 = []
for i in range(a):
    li1.append(int(input()))
li1.sort(reverse=True)
for i in range(len(li1)):
    #print(li1[i],i)
    if (li1[i]-i) >= 0:
        ans+=li1[i]-i
print(ans)