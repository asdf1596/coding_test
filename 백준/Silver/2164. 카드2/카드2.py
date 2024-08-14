from collections import deque
li1 = deque([])
a = int(input())
li2 = [li1.append(b) for b in range(1,a+1)]
for i in range(a-1):
    li1.popleft()
    li1.append(li1.popleft())
print(li1.pop())