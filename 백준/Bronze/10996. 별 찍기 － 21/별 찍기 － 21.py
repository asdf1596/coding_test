a = int(input())
li1 = ["*", " "]
if(a == 1):
    print("*")
else:
    for i in range(a*2):
        for j in range(a):
            print(li1[(j+i%2)%2],end="")
        print("")