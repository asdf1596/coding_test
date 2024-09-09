import sys
def try1(a, b):
    while b != 0:
        a, b = b, a%b
    return a
a,b = map(int, sys.stdin.readline().split())
z = int(sys.stdin.readline())
for _ in range(z):
    c,d,e = map(int, sys.stdin.readline().split())
    if c == 1:
        if d==e:
            print(a+(d-1)*b)
        elif (e-d)%2==1:
            ans = ((a+(d-1)*b)+(a+(e-1)*b))*((e-d+1)//2)
            print(ans)
        else:
            ans = ((a+(d-1)*b)+(a+(e-1)*b))*((e-d)//2)+((a+(d-1)*b)+(a+(e-1)*b))//2
            print(ans)
    else:
        if b !=0:
            if d==e:
                print(a+(d-1)*b)
            else:
                f = try1(a+(d-1)*b, a+(d-1)*b+b)
                for i in range(a+(d-1)*b+b, a+(e-1)*b+1, b):
                    f = try1(i, f)
                print(f)
        else:
            print(a)