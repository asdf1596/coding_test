a,b,c = map(int, input().split())
if a>c:
    print("Bus")
elif max([a,c]) > b:
    print("Bus")
elif max([a,c]) < b:
    print("Subway")
else:
    print("Anything")