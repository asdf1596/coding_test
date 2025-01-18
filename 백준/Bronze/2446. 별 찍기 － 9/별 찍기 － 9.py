a = int(input())
b = a*2-1
for i in range(a):
    for j in range(i):
        print(" ", end = "")
    for j in range(b-i*2):
        print("*", end = "")
    print("")
for i in range(a-2, -1, -1):
    for j in range(i):
        print(" ", end = "")
    for j in range(b-i*2):
        print("*", end = "")
    print("")