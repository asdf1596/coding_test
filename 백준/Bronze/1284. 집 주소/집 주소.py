while 1:
    N = input()
    if N == '0':
        break
    r = len(N)+1
    for n in N:
        if n == '0':
            r += 4 
        elif n == '1':
            r += 2
        else:
            r += 3
    print(r)