a = int(input())
b, c = map(int, input().split())
ans = 0
if a > (b//2)+c:
    print(b//2+c)
else:
    print(a)