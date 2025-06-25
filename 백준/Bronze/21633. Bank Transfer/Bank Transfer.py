a = int(input())
if 25 + a*0.01 < 100:
    print(100)
elif 25 + a*0.01 > 2000:
    print(2000)
else:
    print(25 + a*0.01)