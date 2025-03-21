ans = 0
li1 = []
for i in range(15):
    li1.append(list(input().split()))
for li2 in li1:
    if "w" in li2:
        print("chunbae")
        break
    if "b" in li2:
        print("nabi")
        break
    if "g" in li2:
        print("yeongcheol")
        break