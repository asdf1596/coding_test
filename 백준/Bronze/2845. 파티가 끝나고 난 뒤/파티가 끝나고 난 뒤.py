a ,b = map(int, input().split())
li1 = list(map(int, input().split()))
a = a*b
li2 = []
for i in li1:
    li2.append(i-a)
for i in li2:
    print(i, end=" ")