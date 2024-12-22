a = int(input())
li1 = list(map(int, input().split()))
c = int(input())
e = 0
for i in range(a):
    if li1[i] == 0:
        continue
    elif li1[i] > c:
        e += li1[i]//c
        #print(li1[i]//c)
        #print(e)
        if li1[i]%c!=0:
            e+=1
    else:
        e+=1
print(e*c)