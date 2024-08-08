
while True:
    li1 = list(input())
    if li1 == ["#"]:
        break
    if li1[-1]=="e":
        if li1.count("1")%2==1:
            li1[-1] = "1"
        else:
            li1[-1] = "0"
    else:
        if li1.count("1")%2==1:
            li1[-1] = "0"
        else:
            li1[-1] = "1"
    for i in li1:
        print(i,end="")
    print("")