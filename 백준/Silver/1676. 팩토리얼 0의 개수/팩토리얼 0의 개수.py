a = int(input())
ans = 1
for i in range(2,a+1):
    ans*=i
li1 = list(str(ans))
b = 0
if "0" in li1:
    for i in range(len(li1)-1,-1,-1):
        if li1[i] != "0":
            print(b)
            break
        b+=1
else:
    print("0")