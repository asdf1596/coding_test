a, b = input().split()
b = int(b)
a = list(a)
#-55
ans = 0
for i in range(len(a)-1, -1, -1):
    try1 = len(a)-i-1
    #print(i)
    if(ord(a[i]) <= 57):
        i = int(a[i])
        #print(i*(b**try1))
        ans+=i*(b**try1)
    else:
        i = (ord(a[i])-55)*(b**try1)
        #print(i)
        ans+=i
print(ans)