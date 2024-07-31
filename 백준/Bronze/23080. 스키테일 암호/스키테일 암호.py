a = int(input())
b = list(input())
for i in range(len(b)):
    if(i%a==0):
        print(b[i], end="")
print("")