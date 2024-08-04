a,b = map(int, input().split())
from collections import deque
li1 = [c for c in range(1, a+1)]
li1 = deque(li1)
li2 = []
try1 = 1
while len(li1) != 0:
    c = li1.popleft()
    if(try1%b==0):
        li2.append(c)
    else:
        li1.append(c)
    try1+=1
print("<",end = "")
for i in li2:
    if i != li2[-1]:
        print(str(i)+", ", end="")
print(str(li2[-1])+">")