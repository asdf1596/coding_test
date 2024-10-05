a = int(input())
for i in range(a):
    b,c = map(list, input().split())
    b.sort()
    c.sort()
    if b == c:
        print("Possible")
    else:
        print("Impossible")