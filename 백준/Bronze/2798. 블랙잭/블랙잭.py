a, b = input().split()
a, b = int(a), int(b)
li1 = list(map(int, input().split()))
ans = 0
for i in range(a-2):
    for j in range(i+1,a):
        for k in range(j+1,a):
            if(b-ans > b-(li1[i]+li1[j]+li1[k]) and 0 <= b-(li1[i]+li1[j]+li1[k])):
                #print((li1[i],li1[j],li1[k]),(li1[i]+li1[j]+li1[k]))
                ans = (li1[i]+li1[j]+li1[k])
            if(ans == a):
                break
            
print(ans)