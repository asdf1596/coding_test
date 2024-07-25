a = int(input())
b = list(input())
c = b[len(b)-5:len(b)]
d = ""
for i in c:
    d+=i
print(d)