li1 = [int(input()) for _ in range(9)]
a = sum(li1)
num = a-100
for i in range(9):
    for j in range(i+1,9):
        if(li1[i]+li1[j] == num):
            num1, num2 = li1[i], li1[j]
            li1.remove(num1)
            li1.remove(num2)
            break
    if(len(li1) != 9):
        break
z = [print(a) for a in li1]