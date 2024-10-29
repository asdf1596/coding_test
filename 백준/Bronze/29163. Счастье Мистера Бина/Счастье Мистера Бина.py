a = int(input())
c = 0
li1 = list(map(int, input().split()))
for j in li1:
    if j%2==0:
        c+=1
    else:
        c-=1
if c>0:
    print("Happy")
else:
    print("Sad")