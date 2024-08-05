from collections import deque
a,b = map(int, input().split())
if a!= 0:
    li1 = list(map(int, input().split()))
    li1=deque(li1)
ans=1
gram = 0
if a == 0:
    print(0)
else:
    for i in range(len(li1)):
        c = li1.popleft()
        if gram +c > b:
            ans+=1
            gram=c
        else:
            gram+=c
    print(ans)