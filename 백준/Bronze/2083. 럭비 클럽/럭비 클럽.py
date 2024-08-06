while True:
    a = ""
    b,c=0,0
    a,b,c = input().split()
    b,c = int(b), int(c)
    if a == "#":
        break
    if b>=18 or c>=80:
        print(a, "Senior")
    else:
        print(a,"Junior")