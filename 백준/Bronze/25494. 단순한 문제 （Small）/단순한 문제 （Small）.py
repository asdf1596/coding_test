ans = int(input())
while ans > 0 :
    a, b, c = map(int, input().split())
    print(min(a, min(b, c)))
    ans -= 1