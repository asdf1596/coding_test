a, b, c = sorted([*map(int, input().split())])
r = 3
if a + b == c : r = 1
elif a * b == c : r = 2
print(r)