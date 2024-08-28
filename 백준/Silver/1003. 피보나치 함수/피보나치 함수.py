count0 = 0
count1 = 0
def try1(b):
    li1 = [1,1,0]
    e = 1
    c = 1
    d = 1
    if b==0:
        return 1,0
    elif b==1:
        return 0,1
    else:
        b-=1
        for i in range(b-1):
            c = li1[0]
            d = li1[1]
            li1[2] = c+d
            li1[0] = d
            li1[1] = li1[2]
            e+=1
            #print(li1)
        return li1[0], li1[1]
a = int(input())
for i in range(a):
    b,c = try1(int(input()))
    print(b,c)