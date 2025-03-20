ans = 0
li1 = []
for i in range(5):
    j = int(input())
    if j in li1:
        ans-=j
        li1.remove(j)
    else:
        ans+=j
        li1.append(j)
print(ans)