from collections import deque
a = int(input())
ansList = deque([])
for i in range(a):
    ansList.append(int(input()))
li1 = [i for i in range(1,a+1)]
li1 = deque(li1)
li2 = deque([])
li3 = deque([])
check = True
while len(ansList) !=0 and check:
    ans = ansList.popleft()
    while True:
        if len(li2)!=0:
            b = li2.pop()
            if ans==b:
                li3.append("-")
                break
            else:
                li2.append(b)
        if len(li1) == 0:
            check = False
            li3.append("NO")
            break
        b = li1.popleft()
        li3.append("+")
        if ans == b:
            li3.append("-")
            break
        else:
            li2.append(b)
b = li3.pop()
if b == "NO":
    print(b)
else:
    for i in range(len(li3)):
        print(li3.popleft())
    print(b)