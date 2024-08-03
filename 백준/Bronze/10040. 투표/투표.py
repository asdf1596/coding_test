a,b = map(int, input().split())
li1= []
li2 = []
for i in range(a):
    li1.append(int(input()))
    li2.append(0)
for i in range(b):
    c = int(input())
    for j in range(len(li2)):
        if c >= li1[j]:
            li2[j]+=1
            #print(li1, li2)
            break
m = max(li2)
for i in range(len(li2)):
    if m == li2[i]:
        print(i+1)
        break