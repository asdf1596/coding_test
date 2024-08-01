li1 = []
a = int(input())
for i in range(a):
    li1.append(input().split())
for i in li1:
    b = int("0b"+i[0], 2)+int("0b"+i[1], 2)
    print(bin(b)[2:])