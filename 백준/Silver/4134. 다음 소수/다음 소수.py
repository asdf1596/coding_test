li1 = []
a = int(input())
def check(num):
    if 1>=num:
        return False
    if 3>=num:
        return True
    if num%2==0:
        return False
    if num%3==0:
        return False
    j = 5
    while j*j <= num:
        if num%j==0 or num%(j+2)==0:
            return False
        j+=6
    return True
for i in range(a):
    b = int(input())
    li1.append(b)
for b in li1:
    if(b<=2):
        print(2)
        continue
    if(b%2==0):
        b+=1
    while not check(b):
        b+=2
    print(b)