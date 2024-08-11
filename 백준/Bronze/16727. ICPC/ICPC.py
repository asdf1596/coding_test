a1,b2 = map(int, input().split())
b1,a2 = map(int, input().split())
if a1+a2 == b1+b2:
    if a2> b2:
        print("Persepolis")
    elif b2>a2:
        print("Esteghlal")
    else:
        print("Penalty")
elif a1+a2 > b1+b2:
    print("Persepolis")
else:
    print("Esteghlal")