d = int(input())
for i in range(d):
    a,b,c = map(int, input().split())
    print(a*(c-1)+b)