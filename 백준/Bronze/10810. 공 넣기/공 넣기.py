a,b = map(int, input().split())
li1 = [0 for i in range(a)]
for i in range(b):
    c,d,e = map(int, input().split())
    for j in range(c-1, d):
        li1[j] = e
[print(i) for i in li1]