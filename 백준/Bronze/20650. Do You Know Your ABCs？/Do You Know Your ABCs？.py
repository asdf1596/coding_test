li1 = list(map(int, list(input().split())))
li1.sort()
print(li1[0],li1[1],li1[-1]-(li1[0]+li1[1]))