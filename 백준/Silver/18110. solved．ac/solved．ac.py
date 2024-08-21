from collections import deque
a = int(input())
def round1(a):
    if a-int(a)*1.0 < 0.5:
        return int(a)
    else:
        return int(a)+1
b = round1(a*0.15)
li1 = []
for i in range(a):
    li1.append(int(input()))
li1.sort()
li1 = deque(li1)
for i in range(b):
    li1.pop()
for i in range(b):
    li1.popleft()
li1 = list(li1)
# print(li1)
if len(li1) == 0:
    print(0)
else:
    print(round1(sum(li1)/(a-b*2)))