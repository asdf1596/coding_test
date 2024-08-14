while True:
    li1 = list(input())
    if li1 == ["0"]:
        break
    a = True
    for i in range(len(li1)//2):
        if li1[i] != li1[len(li1)-1-i]:
            a = False
    if a:
        print("yes")
    else:
        print("no")