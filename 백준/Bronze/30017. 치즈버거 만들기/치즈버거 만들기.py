a,b = map(int, input().split())
if(b < a-1):
    ans = b*2+1
else:
    ans = a*2-1
print(ans)