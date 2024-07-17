a, b = input().split()
a, b = list(a), list(b)
empty = []
li1=  [a,b]
ans = []
for i in li1:
    for j in range(len(i)):
        empty.append(i[len(i)-1-j])
    ans.append(int("".join(empty)))
    empty = []
print(max(ans))