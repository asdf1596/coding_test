import math
li1 = []
li3 = ["a","b","c"]
while True:
    li1.append(list(map(int, input().split())))
    if(li1[-1] == [0,0,0]):
        break
for i in range(len(li1)-1):
    print("Triangle #"+str(i+1))
    if(li1[i][0] == -1):
        if(li1[i][1]>=li1[i][2]):
            print("Impossible.")
        else:
            print("a =", "%.3f"%math.sqrt(li1[i][2]**2-li1[i][1]**2))
    elif(li1[i][1] == -1):
        if(li1[i][0]>=li1[i][2]):
            print("Impossible.")
        else:
            print("b =", "%.3f"%math.sqrt(li1[i][2]**2-li1[i][0]**2))
    else:
        print("c =", "%.3f"%math.sqrt(li1[i][1]**2+li1[i][0]**2))
    print("")