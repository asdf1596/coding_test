a,b = map(int, input().split())
for i in range(a):
    li1 = list(input())
    li1.reverse()
    for j in li1:
        print(j, end = "")
    print()