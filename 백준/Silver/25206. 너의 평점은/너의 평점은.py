from sys import stdin
li1 = {"A+" : 4.5,"A0":4.0,"B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0,"P":-1}
e = 0
d = 0
for i in range(20):
    a,b,c = stdin.readline().split()
    if c == "P":
        continue
    b = float(b)
    e+=(b*li1[c])
    d+=b
print(e/d)