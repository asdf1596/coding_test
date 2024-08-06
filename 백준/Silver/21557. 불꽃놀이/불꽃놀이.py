a= int(input())
li1 = list(map(int, input().split()))
if li1[0]>li1[-1]:
    b = li1[0]
else:
    b = li1[-1]
print(b-(a-2))