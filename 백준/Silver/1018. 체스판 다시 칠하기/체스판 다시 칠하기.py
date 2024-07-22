h,w = map(int, input().split())
li1 = []
for i in range(h):
    li1.append(list(input()))
li2 = []
def check(map1):
    sm = 64
    li1 = []
    pre = ["W","B"]
    ans = 0
    for _ in range(2):
        ans = 0
        li1 = []
        for i in range(8):
            for j in range(8):
                if map1[i][j] != pre[(i+j)%2]:
                    li1.append(map1[i][j])
                    ans+=1
        #print(li1)
        #print(ans)
        if(ans < sm):
            sm = ans
        pre = ["B","W"]
    return sm
sm = 64
ans = 0
for i in range(h-7):
    for j in range(w-7):
        li2.append([])
        for k in range(8):
            li2[-1].append(li1[i+k][j:j+8])
for i in li2:
    ans = check(i)
    #print(sm)
    if(ans < sm):
        sm = ans
print(sm)