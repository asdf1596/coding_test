a = int(input())
li1 = []
for i in range(a):
    li1.append(int(input()))
b = int(input())
ans = 0
for i in range(b):
    ans+=li1[int(input())-1]
print(ans)