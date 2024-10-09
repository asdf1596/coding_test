while True:
    a = int(input())
    if a == 0:
        break
    ans = 0
    for i in range(1, a+1):
        ans+=i
    print(ans)