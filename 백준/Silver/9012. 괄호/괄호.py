z = int(input())
for _ in range(z):
    a = list(input())
    b = 0
    check = True
    for i in a:
        if i =="(":
            b+=1
        else:
            b-=1
        if(b < 0):
            check = False
            break
    #print(b)
    if b == 0 and check:
        print("YES")
    else:
        print("NO")