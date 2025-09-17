a = int(input())
if a == 1:
    print(2024, 8)
elif a == 5:
    print(2026, 12)
else:
    print((2024+(8+(a-1)*7)//12),(8+(a-1)*7)%12)