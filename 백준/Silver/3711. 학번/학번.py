z = int(input())
for i in range(z):
    x = int(input())
    li1 = []
    li2 = []
    try1 = 2
    for j in range(x):
        li1.append(int(input()))
    if len(li1) == 1:
        print(1)
    elif li1.count(li1[0]) == len(li1):
        print(1)
    else:
        v = min(li1)
        while len(li2) != len(li1):
            li2 = []
            for j in li1:
                if j%try1 not in li2:
                    li2.append(j%try1)
            try1+=1        
            #print(li2)
        if v == try1:
            print("v:", v)
        else:
            print(try1-1)