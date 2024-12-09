a = int(input())
b = a*2-1
for i in range(1,a+1):
    for j in range(a-i):
        print(" ",end = "")
    for j in range(i+(i-1)):
        print("*", end = "")
    print("")
for i in range(1, a):
    for j in range(i):
        print(" ",end = "")
    for j in range(a-i+(a-i-1)):
        print("*", end = "")
    print("")