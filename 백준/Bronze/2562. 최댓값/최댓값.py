li1 = [0]
maxNum = 0
num = 0
for i in range(9):
    li1.append(int(input()))
for i in range(len(li1)):
    if(maxNum < li1[i]):
        maxNum = li1[i]
        num = i
print(maxNum)
print(num)
