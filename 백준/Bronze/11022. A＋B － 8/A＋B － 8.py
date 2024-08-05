a = int(input())
for i in range(1, a+1):
    b,c = map(int, input().split())
    print("Case", "#"+str(i)+":", str(b), "+ "+str(c), "=", b+c)