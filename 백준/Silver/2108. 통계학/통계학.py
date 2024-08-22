from heapq import heappop, heappush
import math
import sys
a = int(sys.stdin.readline())
Max = -4001
Small = 4001
Sum = 0
li1 = {}
max_heap = []
min_heap = []
def push_num(a):
    if len(max_heap) == len(min_heap):
        heappush(max_heap, -a)
    else:
        heappush(min_heap, a)
    if min_heap and -max_heap[0] > min_heap[0]:
        temp_min = heappop(min_heap)
        temp_max = heappop(max_heap)
        heappush(max_heap, -temp_min)
        heappush(min_heap, -temp_max)
def find_median():
    if len(max_heap) == len(min_heap):
        return (-max_heap[0] + min_heap[0]) / 2
    else:
        return -max_heap[0]
def round_up_half(number):
    return math.floor(number + 0.5)
if a == 1:
    try1 = 0
else:
    try1 = (a-1)/2
for i in range(a):
    b = int(sys.stdin.readline())
    if b in li1:
        li1[b]+=1
    else:
        li1[b] = 1
    if b  > Max:
        Max = b
    if b<Small:
        Small = b
    Sum+=b
    push_num(b)
li2 = []
c = max(li1.values())
for i in li1.keys():
    if li1[i] == c:
        li2.append(i)
if len(li2) == 1:
    li1 = li2[0]
else:
    li2.sort()
    li1 = li2[1]
# print("--------------")
print(round_up_half(Sum/a))
print(find_median())
print(li1)
print(Max-Small)