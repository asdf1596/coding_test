a,b,c = map(int, input().split())
d = c-a
e = d//(a-b)
f = c-(e*(a-b))
if f%a==0:
    ans = e+f//a
else:
    ans = e+f//a+1
print(ans)