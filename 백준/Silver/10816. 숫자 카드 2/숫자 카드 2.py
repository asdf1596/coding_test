from collections import Counter
a = int(input())
li1 = list(map(int, input().split()))
b = int(input())
li2 = list(map(int, input().split()))
c = Counter(li1)
for i in li2:
    print(c[i], end = " ")