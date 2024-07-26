li1 = []
while True:
    a = list(input())
    if a[0] == "#":
        break
    li1.append(a)
for a in li1:
    b = a[2:]
    a = a[0:1]
    ans = 0
    for i in range(len(b)):
        if b[i].lower() == a[0]:
            ans+=1
    print(a[0], ans)