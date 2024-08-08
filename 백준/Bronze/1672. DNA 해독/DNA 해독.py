def change(a,b):
    if a == "A":
        if b == "A" or b=="C":
            return "A"
        elif b=="G":
            return "C"
        elif b=="T":
            return "G"
    elif a=="G":
        if b=="A":
            return "C"
        elif b=="G":
            return "G"
        elif b=="C":
            return "T"
        else:
            return "A"
    elif a=="C":
        if b=="A":
            return "A"
        elif b=="G":
            return "T"
        elif b=="C":
            return "C"
        else:
            return "G"
    elif a == "T":
        if b == "A" or b=="C":
            return "G"
        elif b=="G":
            return "A"
        elif b=="T":
            return "T"
a = int(input())
li1 = list(input())
while len(li1) !=1:
    c = li1.pop()
    d = li1.pop()
    li1.append(change(c,d))
print(li1[0])