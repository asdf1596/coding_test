a = int(input())
b = int(input())
c = int(input())
ans = 250
if a > b :
    ans += 100*((a-b)//c + [1, 0][(a - b) % c == 0])
print(ans)