a = int(input())
for i in range(a):
    b, c, d = map(float,input().split())
    print('$'+str(format(b*c*d,".2f")))