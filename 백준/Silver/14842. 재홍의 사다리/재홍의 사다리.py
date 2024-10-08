a,b,c = map(int, input().split())
if c%2==0:
    c-=2
    ans = b*c*0.5
else:
    #h * 2/3 * 1
    ans = b * ((c-1)/c) * ((c-1)/2)
print("{:.6f}".format(ans))