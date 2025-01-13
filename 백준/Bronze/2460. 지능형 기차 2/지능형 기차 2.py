Max = -1
a = 0
for i in range(10):
    b,c = map(int, input().split())
    a-=b
    a+=c
    if a > Max:
        Max = a
    #print(Max)
print(Max)