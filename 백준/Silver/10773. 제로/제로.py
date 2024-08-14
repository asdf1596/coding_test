from collections import deque
li1 = deque([])
a = int(input())
for i in range(a):
    b = int(input())
    if b:
        li1.append(b)
    else:
        li1.pop()
print(sum(li1))