N, X = map(int, input().split())
s = list(map(int, input().split()))
p = []
for i in range(N - 1):
    p.append((s[i] + s[i + 1]) * X)
print(min(p))