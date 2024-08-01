li1 = []
a = int(input())
x1,y1,x2,y2 = map(int, input().split())
if(x1*a+y1 == x2*a+y2):
    print("Yes", x1*a+y1)
else:
    print("No")