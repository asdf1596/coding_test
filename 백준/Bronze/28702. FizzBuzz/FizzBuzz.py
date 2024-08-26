c = -1
d = -1
for i in range(3):
    a = input()
    if a == 'FizzBuzz':
        b = 15
    elif a == "Fizz":
        b = 3
    elif a == "Buzz":
        b = 5
    else:
        b = 0
    if b == 0:
        c = i
        d = a
e = int(d)+(3-c)
if e%15==0:
    print('FizzBuzz')
elif e%3==0:
    print('Fizz')
elif e%5==0:
    print('Buzz')
else:
    print(e)