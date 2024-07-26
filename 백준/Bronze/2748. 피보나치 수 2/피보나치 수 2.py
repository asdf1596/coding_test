a = int(input())
b = 0
c = 1
ans = 1
for i in range(1,a-1):
    b = c
    c = ans
    ans = b+c
print(ans)