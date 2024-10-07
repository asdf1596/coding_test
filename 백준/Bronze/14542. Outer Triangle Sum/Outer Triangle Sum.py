check = 1
while True:
    ans = 0
    a = int(input())
    if a == 0:
        break
    for i in range(1, a+1):
        li1 = list(map(int, input().split()))
        if i == a:
            ans+=sum(li1)
            #print(li1)
        elif i == 1:
            ans = sum(li1)
            #print(li1)
        else:
            ans+=li1[0]
            ans+=li1[-1]
            #print(li1[0], li1[-1])
    print("Case #"+str(check)+":"+str(ans))
    check+=1