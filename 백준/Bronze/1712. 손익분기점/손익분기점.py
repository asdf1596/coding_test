a,b,c = input().split()
a,b,c = int(a), int(b), int(c)
if (c-b !=0):
    ans = a//(c-b)+1
if(c-b <= 0):
    ans = -1
print(ans)