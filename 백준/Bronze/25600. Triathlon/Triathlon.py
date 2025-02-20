mac = 0
for _ in range(int(input())) :
    a, d, g = map(int, input().split())
    if a == d + g :
        v = a * (d + g) * 2
    else :
        v = a * (d + g)
    mac = max(v, mac)
print(mac)