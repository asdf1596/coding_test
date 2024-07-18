li1 = list(map(int, input().split()))
if(li1 == [a for a in range(1, 9)]):
    print("ascending")
elif(li1 == [a for a in range(8, 0, -1)]):
    print("descending")
else:
    print("mixed")