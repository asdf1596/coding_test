ans = []
for _ in range(10):
    a=  int(input())
    if(a%42 in ans):
        continue
    else:
        ans.append(a%42)
print(len(ans))