a = int(input())
for i in range(a):
    ans = 0
    li1 = list(map(int, list(input())))
    for j in range(len(li1)):
        if j%2==0:
            li1[j]*=2
            b,c = li1[j]//10, li1[j]%10
            li1[j] = b+c
            #print(b, c)
        ans+=li1[j]
    if ans%10==0:
        print("T")
    else:
        print("F")