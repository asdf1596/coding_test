a = int(input())
b = int(input())
a = a//100*100
#print(a,b)
for i in range(100):
    if((a+i)%b==0):
        break
a+=i
ans = str(a%100)
if(a%100 < 10):
    ans = "0"+str(a%100)
print(ans)