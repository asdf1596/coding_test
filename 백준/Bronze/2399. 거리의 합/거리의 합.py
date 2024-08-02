a = int(input())
li1 = list(map(int, input().split()))
ans = 0
for i in range(len(li1)):
    for j in range(i+1, len(li1)):
        ans+=abs(li1[i]-li1[j])
        #print(li1[i],li1[j])
print(ans*2)