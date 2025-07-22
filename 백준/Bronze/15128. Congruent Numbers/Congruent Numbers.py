a, b, c, d = map(int, input().split())
ans = a/b * c/d / 2
print(1 if int(ans) == ans else 0)