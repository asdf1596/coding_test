a = int(input())
d = 0
for i in range(a):
    b,c = map(int, input().split())
    if b==136:
        d+=1000
    elif b == 142:
        d+=5000
    elif b == 148:
        d+=10000
    elif b == 154:
        d+=50000
print(d)