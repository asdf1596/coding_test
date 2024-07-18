first = input()
second = input()
third = input()
li1 = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
ans =0
for i in range(len(li1)):
    if(first == li1[i]):
        ans+=((i)*10)
    if(second == li1[i]):
        ans+=(i)
for i in range(len(li1)):
    if(third == li1[i]):
        ans*=10**i
print(ans)