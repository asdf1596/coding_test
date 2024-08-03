a = int(input())
if a <= 5:
    print(a)
else:
    b = a%8
    if b==1:
        print(1)
    elif b == 2 or b==0:
        print(2)
    elif b == 3 or b==7:
        print(3)
    elif b == 4 or b == 6:
        print(4)
    else:
        print(5)