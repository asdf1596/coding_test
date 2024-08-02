import sys
a,b = map(int, sys.stdin.readline().strip().split())
li1 = list(map(int, sys.stdin.readline().strip().split()))
li2 = li1.copy()
li2.sort()
try1 = 0
try2 = len(li1)
try3 = try2-1
isswap = True
while isswap and try1!=b:
    #print(isswap)
    isswap = False
    for j in range(try3):
        if li1[j] > li1[j+1]:
            li1[j],li1[j+1] = li1[j+1],li1[j]
            try1+=1
            isswap = True
            #print(li1,li2,  try1, isswap)
            if try1 == b or li1 == li2:
                break
if(try1 == b):
    for i in li1:
        print(i, end = " ")
else:
    print(-1)