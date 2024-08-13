import sys
li1 = [a for a in range(1,21)]
for _ in range(10):
    a,b = map(int,sys.stdin.readline().split())
    a-=1
    b-=1
    for i in range((b-a+1)//2):
        li1[a+i],li1[b-i] = li1[b-i],li1[a+i]
    #print(li1)
for i in li1:
    print(i, end=" ")