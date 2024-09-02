import sys
#a = int(sys.stdin.readline())
li1 = []
for i in range(3):
    b,c,d = sys.stdin.readline().split()
    c = int(c)%100
    li1.append([int(b),int(c),d])
li1.sort(key= lambda x : -x[1], reverse=True)
for i in range(3):
    print(str(li1[i][1]), end = "")
print("")
li1.sort(key= lambda x : x[0], reverse=True)
for i in range(3):
    print(li1[i][2][0], end="")