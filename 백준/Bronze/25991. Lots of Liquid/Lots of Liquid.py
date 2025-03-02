a = int(input())
b = [*map(float, input().split())]
for i in range(a) :
    b[i] = b[i] ** 3
print(pow(sum(b), 1/3))