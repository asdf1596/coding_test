a = input()
a = a.upper()
a = list(a)
b = {}
for i in a:
    if(i in b.keys()):
        b[i]+=1
    else:
        b[i] = 1
c = max(b.values())
d = 0
ans = 0
e = list(b.values())
f = list(b.keys())
for i in range(len(e)):
    if c == e[i]:
        ans = i
        d+=1
if(d != 1):
    print("?")
else:
    print(f[ans])