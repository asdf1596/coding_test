a,b = map(int, input().split())
li1 = []
for i in range(a):
    li1.append(int(input()))
c = 1
d = max(li1)
try1 = d//2
num=1
def check(li1,try1):
    ans = 0
    for i in li1:
        ans+=i//try1
    return ans
while True:
    if try1==0:
        try1=1
        break
    ans = check(li1,try1)
    if ans>=b:
        if check(li1,try1+1) < b:
            break
        else:
            c = try1
            try1 = (d+try1)//2
            if c == try1:
                try1+=1
    elif ans<b:
        d = try1
        try1 = (c+try1)//2
    num+=1
    # print(try1,c,d)
    # if num==10:
    #    break
print(try1)