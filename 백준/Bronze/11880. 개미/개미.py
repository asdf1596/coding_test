a = int(input())
for i in range(a):
    b,c,d = map(int, input().split())
    e = (b+c)**2+d**2
    f = (c+d)**2+b**2
    g = (d+b)**2+c**2
    print(min([e,f,g]))