li1 = list(input())
a = li1[0]
b=0
for i in range(1,len(li1)):
    if li1[i]!=a:
        b+=1
    a = li1[i]
print((b+1)//2)
#이무슨 해괴한 풀이법