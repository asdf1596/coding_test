li1 = list(input())
a = 0
check = True
for i in li1:
    if i == "X":
        a+=1
    else:
        if a%2==1:
            check = False
        a=0
if a%2==1:
    check = False
a = 0
if check:
    for i in li1:
        if i == ".":
            if a!=0:
                if a%4==0:
                    for j in range(a):
                        print("A",end = "")
                else:
                    for j in range(a-2):
                        print("A",end = "")
                    print("BB",end="")
            a = 0
            print(".",end = "")
        else:
            if i == "X":
                a+=1
    #print(a)
    if a%4==0:
        for j in range(a):
            print("A",end = "")
    else:
        for j in range(a-2):
            print("A",end = "")
        print("BB",end="")
else:
    print(-1)