from collections import deque
a = int(input())
for i in range(a):
    li1 = list(map(int,  input().split()))
    li2= []
    for j in range(len(li1)):
        for k in range(li1[j]):
            if j == 5:
                li2.append(9)
            else:
                li2.append(j+1)
    li2.sort(reverse=True)
    li1 = deque([])
    b = len(li2)
    d = b%2
    for i in range(b):
        if d%2 == 0:
            li1.append(li2.pop())
        else:
            li1.appendleft(li2.pop()) 
        d+=1
    for i in range(len(li1)):
        print(li1.popleft(), end = " ")
    print("")