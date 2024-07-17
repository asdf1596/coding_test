a = int(input())
numli = []
stringli = []
for i in range(a):
    li = input().split()
    numli.append(int(li[0]))
    stringli.append(list(str(li[1])))
for i in range(a):
    for j in stringli[i]:
        for k in range(numli[i]):
            print(j,end="")
    print("")
    
