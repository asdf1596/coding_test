a = input()
ans = 0
for i in range(len(a) - 3):
    if a[i:i+4] == "DKSH":
        ans += 1
print(ans)