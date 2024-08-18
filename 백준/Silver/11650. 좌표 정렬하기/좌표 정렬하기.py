a = int(input())
li1 = []
for i in range(a):
    b,c = map(int, input().split())
    li1.append([b,c])
li1.sort(key=lambda x:(x[0], x[1]))
for i in li1:
    print(i[0], i[1])