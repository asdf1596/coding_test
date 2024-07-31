ans = 0
li1 = []
for i in range(10):
    li1.append(int(input()))
for a in li1:
    if(ans+a>=100):
        if(ans+a-100 == 100-ans):
            ans+=a
            break
        elif(ans+a-100 > 100-ans):
            break
        else:
            ans+=a
            break
    else:
        ans+=a
print(ans)