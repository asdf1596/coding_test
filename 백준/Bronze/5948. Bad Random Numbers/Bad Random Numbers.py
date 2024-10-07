a = int(input())
def check(a):
    li1 = list(str(a))
    if len(li1) == 1:
        return 0
    elif len(li1) == 2:
        return int(li1[0])
    elif len(li1) == 3:
        return int(li1[0]+li1[1])
    elif len(li1) == 4:
        return int(li1[1]+li1[2])
if len(list(str(a))) == 1:
    print(2)
else:
    ans = 1
    li2 = []
    b = -1
    while b != 0:
        b = check(a)
        d = b**2
        if d in li2:
            break
        li2.append(d)
        a = d
        ans+=1
        #print(a,b,d)
print(ans)