a = int(input())
b = a*2-1
for i in range(a):
    for j in range(i):
        print(" ", end = "")
    for j in range((a-i)*2-1):
        print("*",end = "")
    print("")