a = input()
b = input()
a, b = int(a), int(b)
if(a<0 and b<0):
    c = 3
elif(a<0 and b>0):
    c = 2
elif(a>0 and b>0):
    c = 1
else:
    c = 4
print(c)