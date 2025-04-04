n, h, v = map(int, input().split())
r = max(h, n-h) * max(v, n-v)
print(r*4)