from collections import deque
a,b = map(int, input().split())
li1 = [a for a in range(2, a+1)]
li1 = deque(li1)
ans = 0
while len(li1)!=0:
    pre = li1.popleft()
    ans+=1
    if ans == b:
        print(pre)
        break
    for i in range(len(li1)):
        c = li1.popleft()
        #print(c)
        if c%pre != 0:
            li1.append(c)
        else:
            ans+=1
        if ans == b:
            print(c)
            break