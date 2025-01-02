a = int(input())
li1 = list(input())
ans = 0
for i in li1:
    i = int(i)
    if i%2==0:
        ans+=1
    elif i%2==1:
        ans-=1
    #print("ans = "+str(ans))
#print(ans)
if ans > 0:
    print(0)
elif ans < 0:
    print(1)
else:
    print(-1)