a,b = map(int, input().split())
li1 = list(input())
def change(li1):
    
    return li1
def check(li1):
    ans = 1
    a = li1[0]
    for i in range(1,len(li1)):
        if a!=li1[i]:
            ans+=1
        a = li1[i]
    return ans
for i in range(b):
    c,d,e = map(int, input().split())
    if c == 2:
        for j in range(d-1, e):
            if ord(li1[j])+1!=91:
                li1[j] = chr(ord(li1[j])+1)
            else:
                li1[j] = chr(65)
    else:
        print(check(li1[d-1:e]))
    #print(li1)