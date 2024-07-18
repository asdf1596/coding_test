a = int(input())
li1 = [[1],[2,3,4,5,6,7]]
pre = 2
num = 3
if a == 1:
    pre = 1
elif a in li1[1]:
    pre = 2
else:
    a-=7
    while(a/6 > pre):
        pre+=num
        num+=1
    pre = num
print(pre)