a = int(input())
b, c = 0, 0
for i in range(a):
  e = input()
  if b - c != 2 and c - b != 2:
    if e == "D":
      b += 1
    else:
      c += 1
print(str(b)+":"+str(c))
