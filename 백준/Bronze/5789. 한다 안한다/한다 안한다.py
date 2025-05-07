a = int(input())
for i in range(a):
    b = input()
    c = len(b)
    if b[(c-1)//2] == b[(c-1)//2+1]:
        print("Do-it")
    else:
        print("Do-it-Not")