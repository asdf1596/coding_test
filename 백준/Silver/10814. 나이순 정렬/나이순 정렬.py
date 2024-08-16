a = int(input())
li1 = []
for i in range(a):
    b,c = input().split()
    li1.append([int(b), c])
li1.sort(key=lambda x:x[0])
for i in li1:
    print(i[0], i[1])