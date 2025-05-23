a = int(input())
li1 = list(map(int, input().split()))
for i in range(1, a):
    if(li1[i-1] != 0 and li1[i]!=0):
        li1[i]=li1[i-1]+1
print(sum(li1))