time, isDrunk = map(int, input().split())
if(isDrunk or not (12 <= time <=16)):
    print(280)
else:
    print(320)