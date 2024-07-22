q = int(input())
li1 = []
for _ in range(q):
    li1.append(list(map(int, input().split())))
for a,b,c in li1:
    h = str(c%a)
    if h == "0":
        h = str(a)
    if(c//a == c/a):
        r = c//a
    else:
        r = c//a+1
    if(r<10):
        r = "0"+str(r)
    else:
        r = str(r)
    if([a,b,c] == li1[-1]):
        print(h+r,end="")
    else:
            print(h+r)
