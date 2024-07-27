li1 = []
while True:
    a = list(input())
    if a == ["E","N","D"]:
        break
    li1.append(a)
for a in li1:
    a.reverse()
    print("".join(a))