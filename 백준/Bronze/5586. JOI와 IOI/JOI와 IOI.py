a = "JOI"
b = "IOI"
ans1,ans2 =0,0
try1 = list(input())
li1 = []
for i in range(len(try1)-2):
    li1.append(try1[i]+try1[i+1]+try1[i+2])
for i in li1:
    if i ==a:
        ans1+=1
    elif i == b:
        ans2+=1
print(ans1)
print(ans2)