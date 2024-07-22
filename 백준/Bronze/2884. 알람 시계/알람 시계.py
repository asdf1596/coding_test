a,b = map(int, input().split())
c = 60*a+b
if(c<45):
    c+=1440
c-=45
print(c//60, c%60)