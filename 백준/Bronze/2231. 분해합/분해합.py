a = int(input())
ans = 0
for i in range(a):
    li1 = list(map(int, list(str(i))))
    if(i + sum(li1) == a):
        ans = i
        break
print(ans)