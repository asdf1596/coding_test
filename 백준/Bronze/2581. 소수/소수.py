a = int(input())
b = int(input())
li1 = []
def check(num):
    if(num == 2):
        return True
    if(num < 2):
        return False
    if(num%2== 0):
        return False
    l = round(num ** 0.5) + 1
    for i in range(3, l, 2):
        if num % i == 0:
            return False
    return True
for i in range(a, b+1):
    if(check(i)):
        li1.append(i)
    else:
        continue
#print(li1)
if(len(li1) != 0):
    print(sum(li1))
    print(min(li1))
else:
    print(-1)