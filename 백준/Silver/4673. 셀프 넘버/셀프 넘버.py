li1 = {}
for i in range(1, 10001):
    li1[i] = 1
for i in range(1,10001):
    a = list(map(int, list(str(i))))
    b = sum(a)
    c = i+b
    li1[c] = 0
    if(li1[i] == 1):
        print(i)
    