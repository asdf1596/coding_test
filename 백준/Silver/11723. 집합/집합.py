import sys
z = int(sys.stdin.readline())
li1 = set()
li2 = []
for _ in range(z):
    a = sys.stdin.readline().strip().split()
    if len(a) == 1:
        a,b = a,0
        a = a[0]
    else:
        a,b = a[0],a[1]
        b = int(b)
    if a == "add":
        li1.add(b)
    elif a == "remove":
        li1.discard(b)
    elif a == "check":
        if b in li1:
            print(1)
        else:
            print(0)
    elif a == "toggle":
        if b in li1:
            li1.remove(b)
        else:
            li1.add(b)
    elif a == "all":
        li1 = set([q for q in range(1,21)])
    elif a== "empty":
        li1 = set([])