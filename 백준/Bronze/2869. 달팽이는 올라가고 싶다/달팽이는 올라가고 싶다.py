up, down, top = map(int, input().split())
pre = 0
day = 0
def check(a, b):
    global day
    #print("check", day, b/a)
    if(b/a == 1.0):
        day+=1
        return 0
    elif(int(b/a) < 1):
        day+=1
    else:
        day+=int(b/a)
    return int(b/a)
while(True):
    c = check(up, top)
    top-=c*up
    top+=c*down
    if(c<1):
        break
print(day)
