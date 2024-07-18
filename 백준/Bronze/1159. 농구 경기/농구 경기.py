a = int(input())
li1 = []
for i in range(a):
    li1.append(list(input())[0])
li2 = set(li1)
ans = []
for i in li2:
    if(li1.count(i) >=5):
        ans.append(i)
if(len(ans) == 0):
    print("PREDAJA")
else:
    print(''.join(sorted(ans)))