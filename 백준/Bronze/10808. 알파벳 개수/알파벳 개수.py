a = list(input())
li1 = [0 for i in range(26)]
for i in a:
    li1[ord(i)-97]+=1
for i in li1:
    print(i, end=" ")