a = int(input())
b = int(input())
while (b != 0):
    if b%a == 0:
        print(f'{b} is a multiple of {a}.')
    else:
        print(f'{b} is NOT a multiple of {a}.')
    b = int(input())