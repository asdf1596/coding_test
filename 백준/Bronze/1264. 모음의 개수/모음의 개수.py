li2 = ["a","e","o","i","u"]
while True:
    ans = 0
    li1 = input()
    if li1 == "#":
        break
    li1 = li1.lower()
    li1 = list(li1)
    for i in li1:
        #print(i)
        for j in li2:
            if i == j:
                ans+=1
    print(ans)