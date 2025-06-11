for _ in range(int(input())) :
    a = ''
    s = input()
    for i in range(len(s)) :
        if a != s[i] :
            print(s[i], end = "")
            a = s[i]
    print()