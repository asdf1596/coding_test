a = int(input())
li1 = []
for i in range(a):
    li1.append(list(input()))
for i in li1:
    print(i[0], end = "")
    print(i[-1])