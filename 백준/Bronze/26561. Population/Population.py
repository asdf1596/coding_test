a = int(input())
for i in range(a):
    b,c = map(int, input().split())
    b-=(c//7)
    b+=(c//4)
    print(b)