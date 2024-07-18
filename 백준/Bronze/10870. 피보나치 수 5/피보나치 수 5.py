ans = 1
before = 1
before2 = 0
num = int(input())
for a in range(1, num):
    ans=before+before2
    before2 = before
    before = ans
if(num==0):
    ans = 0
print(ans)