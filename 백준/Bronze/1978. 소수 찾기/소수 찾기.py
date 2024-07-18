a = int(input())
b = list(map(int, input().split()))
ans = 0
def check(num, num2):
    if(num2 == 1):
        #print("true")
        return True
    elif(num%num2==0):
        #print("false")
        return False
    elif(check(num, num2-1)):
        return True
for i in range(len(b)):
    if(b[i] == 1):
        continue
    elif(b[i]==2 or b[i] == 3):
        ans+=1
        continue
    elif(b[i]%2 == 0):
        continue
    else:
        if(check(b[i], b[i]-1)):
            ans+=1
        else:
            continue
print(ans)