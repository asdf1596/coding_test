a = float(input())
ans = a//4
a%=4
if a == 0:
    print(ans)
elif a == 1:
    print(ans+0.25)
elif a == 2:
    print(ans+0.50)
elif a == 3:
    print(ans+0.75)