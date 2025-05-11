Max = 0
Max2 = 0
for i in range(5):
    a = sum(list(map(int, input().split())))
    if a > Max2:
        Max2 = a
        Max = i+1
print(Max, Max2)