a = int(input())
li1 = []
for i in range(a):
    b,c = map(int, input().split())
    li1.append([b,c])
ans = 0
for i,j in li1:
    ans = 1
    for k,l in li1:
        if k>i and l>j:
            ans+=1
    print(ans, end = " ")