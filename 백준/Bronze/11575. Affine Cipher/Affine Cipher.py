a = int(input())
for i in range(a):
    b,c = map(int, input().split())
    li1 = list(input())
    for j in li1:
        d = ord(j)-65
        e = (b*d+c)%26+65
        print(chr(e), end = "")
        #print(e)
    print("")
        