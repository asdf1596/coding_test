a,b = map(int , input().split())
insuboonhae = 0
for i in range(2, b):
    if(a%i==0):
        print("BAD", i)
        insuboonhae = 1
        break
if (insuboonhae== 0):
    print("GOOD")