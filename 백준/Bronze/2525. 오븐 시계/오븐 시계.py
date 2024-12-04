a,b = map(int, input().split())
c = b+a*60
d = int(input())
c +=d
c%=1440
print(c//60, c%60)