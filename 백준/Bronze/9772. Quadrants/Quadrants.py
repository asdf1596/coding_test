while True:
    a,b = map(float, input().split())
    if a == 0.0 and b==0.0:
        print("AXIS")
        break
    if a == 0.0 or b==0.0:
        print("AXIS")
    elif a>0.0:
        if b>0.0:
            print("Q1")
        else:
            print("Q4")
    else:
        if b>0.0:
            print("Q2")
        else:
            print("Q3")