a = int(input())
li1 = list(map(int, input().split()))
li2 = []
last = 0
pre = 0
for i in range(a):
    if last > li1[i]:
        pre+=1
    else:
        last = li1[i]
        li2.append(pre)
        pre = 0
    #print(pre,big,last)
li2.append(pre)
print(max(li2))