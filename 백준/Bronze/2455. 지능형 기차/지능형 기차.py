a,b,c, Max = 0,0,0,0
for i in range(4):
    a,b = map(int, input().split())
    c = c-a
    if c > Max:
        Max = c
    c+=b
    if Max < c:
        Max = c
print(Max)