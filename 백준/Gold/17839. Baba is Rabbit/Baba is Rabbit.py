import sys
a = int(sys.stdin.readline().strip())
ans = []
before = {}
d = 0
for i in range(a):
    b,_,c = sys.stdin.readline().split()
    if b == "Baba":
        ans.append(c)
    else:
        before[b]=c
while(d!=len(ans)):
    d = len(ans)
    for i in ans:
        if i in before:
            ans.append(before[i])
            del before[i]
ans = list(set(ans))
ans.sort()
for i in ans:
    print(i)