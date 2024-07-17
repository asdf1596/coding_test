a = int(input())
li1 = []
for i in range(a):
    ans = 0
    li1.append(list(input()))
for i in li1:
    num=0
    allnum=0
    ans = 0
    for j in range(len(i)):
        if(i[j] == "X"):
            #print(num)
            ans+=allnum
            allnum=0
            num = 0
        elif(i[j] == "O" and j !=0):
            num +=1
            allnum+=num
            #print(num)
        else:
            num=1
            allnum+=num
            #print(num)
    ans+=allnum
    print(ans)