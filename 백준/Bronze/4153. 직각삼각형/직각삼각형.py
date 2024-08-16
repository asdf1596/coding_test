while True:
    a,b,c = map(int, input().split())
    if a==0 and b==0 and c==0:
        break
    li1 = [a,b,c]
    li1.sort()
    if li1[0]**2+li1[1]**2 == li1[2]**2:
        print("right")
    else:
        print("wrong")