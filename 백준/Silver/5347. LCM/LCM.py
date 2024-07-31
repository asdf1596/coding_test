a = int(input())
for i in range(a):
    b,c = map(int, input().split())
    d = b*c
    e,f = b,c
    ans = d
    while e!=d and f!=d:
        if(e%c==0):
            ans = e
            break
        if(f%b==0):
            ans = f
            break
        e+=b
        f+=c
    print(ans)