a = int(input())
ans=0
while a%5!=0:
    if a<3:
        ans = -1
        break
    a-=3
    ans+=1
if a%5==0:
    ans+=a//5
print(ans)